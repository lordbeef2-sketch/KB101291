# JAVA OPENAPI: Project (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/Project.html
- source_path: `com/nomagic/magicdraw/core/Project.html`
- source_sha256: `06c17aacb7876f0572661327630a357463af93a08dca9011fe8895ad77bd7ccf`
- captured_utc: `2026-07-14T16:55:12.099974+00:00`

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
`[DIRTY_PROPERTY](#DIRTY_PROPERTY)`
Project "dirty" flag change
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[FILE_NAME_PROPERTY](#FILE_NAME_PROPERTY)`
Project file name property
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MANY_CLASSES_UPDATED](#MANY_CLASSES_UPDATED)`
Event type when many elements in project are changed (for example after project update,massive source reverse operation and etc)
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SELECTION_CHANGED](#SELECTION_CHANGED)`
Deprecated.
now SelectionProvider fires selection changed,
 use [`SelectionProvider.SelectionChangedListener`](../ui/SelectionProvider.SelectionChangedListener.html)
 The diagram objects selecting event type and naming.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Project](#%3Cinit%3E())()`
Constructor creates project.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.AbstractVisitor))([AbstractVisitor](../uml/AbstractVisitor.html) visitor)`
Method accepts a visitor, and calls method visit < class name > (this) of visitor.
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.Visitor))([Visitor](../uml/Visitor.html) visitor)`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
`void`
`[addElementByID](#addElementByID(com.nomagic.magicdraw.uml.BaseElement,java.lang.String))([BaseElement](../uml/BaseElement.html) obj,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) oldID)`
Register the object by id.
`static void`
`[addFeature](#addFeature(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) feature)`
Register a feature for a new project.
`void`
`[addPropertyChangeListener](#addPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Registers the listener to the element.
`void`
`[addToProjectRepository](#addToProjectRepository(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Adds element into this project repository and removes it from previous
 project repository.
`void`
`[addToQueryChangeRegistry](#addToQueryChangeRegistry(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`

`void`
`[addWindow](#addWindow(com.nomagic.magicdraw.ui.ProjectWindow))([ProjectWindow](../ui/ProjectWindow.html) window)`

`void`
`[atInsert](#atInsert())()`
This method is called then this element is added into the project.
`final boolean`
`[canAdd](#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean))([BaseElement](../uml/BaseElement.html) element,
 boolean checkPermissions)`
Checks if this element can add a given element.
`boolean`
`[canAddChild](#canAddChild())()`
Checks if new elements can be added to this element
`boolean`
`[canAddChild](#canAddChild(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) o)`

`boolean`
`[canAddInstance](#canAddInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) o)`
Checks if this object can add element of given type.
`boolean`
`[canBeDeleted](#canBeDeleted())()`
Checks if an element can be deleted from a project.
`boolean`
`[canChangeParent](#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) elements,
 [BaseElement](../uml/BaseElement.html) newParent)`
Returns true, if element can change parent.
`boolean`
`[canDeleteChild](#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) child)`
Checks if given element can be deleted from this element.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[clone](#clone())()`

`int`
`[compareTo](#compareTo(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`
Compares sort key at index 1 with given element's sort key at index 1.
`void`
`[dispose](#dispose())()`
Destroys the project.
`void`
`[elementAdded](#elementAdded(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Marks element as added, if it was previously removed its id is removed from id collection.
`void`
`[elementRemoved](#elementRemoved(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) obj)`
Marks element removed, its id added to mDeletedObjectIDS.
`boolean`
`[executeIntensiveAction](#executeIntensiveAction(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) reason)`
Executes time-intensive action if user agrees to.
`void`
`[firePropertyChange](#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)`
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[generateID](#generateID())()`
Generate ID.
`[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)`
`[getActiveAbstractDiagram](#getActiveAbstractDiagram())()`

`[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)`
`[getActiveDiagram](#getActiveDiagram())()`
Returns currently active diagram.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../uml/BaseElement.html)>`
`[getAllElements](#getAllElements())()`
Gets collection of all model elements in the project
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getAllIDS](#getAllIDS())()`
Returns the collection of all ids in the project.
`com.nomagic.magicdraw.core.BinaryStreamAtticCleaner`
`[getBinaryStreamAtticCleaner](#getBinaryStreamAtticCleaner())()`

`[Browser](../ui/browser/Browser.html)`
`[getBrowser](#getBrowser())()`
Get browser.
`[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)`
`[getClassType](#getClassType())()`
Gets the type of the element class.
`com.nomagic.magicdraw.commands.CommandHistory`
`[getCommandHistory](#getCommandHistory())()`

`com.nomagic.magicdraw.core.MDCounter`
`[getCounter](#getCounter())()`

`[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)`
`[getDiagram](#getDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagramElement)`
Returns diagram presentation element for specified diagram model element.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)>`
`[getDiagrams](#getDiagrams())()`
Returns all existing diagrams stored in this Project.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)>`
`[getDiagrams](#getDiagrams(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Returns existing diagrams of given type stored in Project.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDirectory](#getDirectory())()`
Deprecated.
use #getFile.getParent
`[StateChangeHandler.DirtyType](../utils/StateChangeHandler.DirtyType.html)`
`[getDirtyType](#getDirtyType())()`
Returns project dirty type if project is dirty, otherwise - null.
`com.nomagic.magicdraw.dsl.DSL`
`[getDSL](#getDSL())()`
Returns project DSL service instance.
`com.nomagic.magicdraw.ui.dsl.DSLManager`
`[getDSLManager](#getDSLManager())()`
Deprecated.
use [`getDSL()`](#getDSL())
`[BaseElement](../uml/BaseElement.html)`
`[getElementByID](#getElementByID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Return the element with given id.
`com.nomagic.magicdraw.core.Project.ElementByIDFetcher`
`[getElementByIDQuerier](#getElementByIDQuerier())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)>`
`[getElementsByIDs](#getElementsByIDs(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> ids)`
Return the objects by given ids.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)>`
`[getElementsByIDs](#getElementsByIDs(java.util.Collection,java.util.function.Supplier))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> ids,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../uml/BaseElement.html)>> collectionFactory)`
Return the objects by given ids.
`[ElementsFactory](../../uml2/impl/ElementsFactory.html)`
`[getElementsFactory](#getElementsFactory())()`
Provides UML elements factory
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getElementsIDs](#getElementsIDs(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> elements)`
Retrieves the elements ids from DTObjects collection.
`[XmiExporterDescription](../../persistence/XmiExporterDescription.html)`
`[getExporterDescription](#getExporterDescription())()`

`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getFeatures](#getFeatures())()`
Return registered features for a new project.
`com.nomagic.utils.ExtendedFile`
`[getFile](#getFile())()`
Method returns file of this project.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFileName](#getFileName())()`
Method returns file name of this project.
`boolean`
`[getHasUnloadedManuallyReachableModules](#getHasUnloadedManuallyReachableModules())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHumanName](#getHumanName())()`
Returns human representation of the element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHumanType](#getHumanType())()`
Returns human representation of the element type.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getID](#getID())()`
Returns the ID of the `Element`.
`[ProjectDescriptor](project/ProjectDescriptor.html)`
`[getLoadedFrom](#getLoadedFrom())()`
Return location from were project was loaded.
`org.eclipse.emf.common.util.URI`
`[getLocationUri](#getLocationUri())()`
Get URI location according the primary project.
`[Model](../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html)`
`[getModel](#getModel())()`
Deprecated.
deprecated because of ambiguity with historical API evolution
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)>`
`[getModels](#getModels())()`
Returns a list of models in the project
 (the primary model of the project and all the models of the modules (attached projects)).
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Returns project name.
`[BaseElement](../uml/BaseElement.html)`
`[getObjectParent](#getObjectParent())()`
Returns the element parent.
`[ProjectOptions](options/ProjectOptions.html)`
`[getOptions](#getOptions())()`
Getter for project options.
`[BaseElement](../uml/BaseElement.html)`
`[getPresentationElementByID](#getPresentationElementByID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementID)`
Return the presentation element with given id from currently registered elements.
`[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)`
`[getPrimaryModel](#getPrimaryModel())()`
Returns a primary model of this project.
`com.nomagic.ci.persistence.IPrimaryProject`
`[getPrimaryProject](#getPrimaryProject())()`
Primary project of MagicDraw project.
`static [Project](Project.html)`
`[getProject](#getProject(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Returns Project for a given element
`static [Project](Project.html)`
`[getProject](#getProject(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> elements)`
Returns Project from first given element
`com.nomagic.magicdraw.ui.ProjectEditorWindowsManager`
`[getProjectEditorWindowsManager](#getProjectEditorWindowsManager())()`

`[Project](Project.html)`
`[getProjectImpl](#getProjectImpl())()`
This method is deprecated and will be removed soon.
`[ProxyManager](proxy/ProxyManager.html)`
`[getProxyManager](#getProxyManager())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRemoteID](#getRemoteID())()`

`[AbstractRepository](../../uml2/ext/jmi/reflect/AbstractRepository.html)`
`[getRepository](#getRepository())()`
Get project repository.
`[RepositoryListenerRegistry](../../uml2/ext/jmi/RepositoryListenerRegistry.html)`
`[getRepositoryListenerRegistry](#getRepositoryListenerRegistry())()`
Return listener registry for repository.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getResourceID](#getResourceID())()`

`[SmartEventSupport](../../uml2/ext/jmi/smartlistener/SmartEventSupport.html)`
`[getSmartEventSupport](#getSmartEventSupport())()`
Returns registry that allows to register smart listener configurations by element type.
`final com.dassault_systemes.modeler.foundation.common.sort.SortKeys`
`[getSortKeys](#getSortKeys())()`
Implementation of getSortKeys() from Sortable interface.
`[StateChangeHandler](../utils/StateChangeHandler.html)`
`[getStateChangeHandler](#getStateChangeHandler())()`

`com.nomagic.magicdraw.uml.symbols.StereotypesStyleChangeManager`
`[getStereotypesStyleChangeHandler](#getStereotypesStyleChangeHandler())()`

`[StyleManager](../properties/StyleManager.html)`
`[getStyleManager](#getStyleManager())()`
Returns style manager
`[SymbolElementMap](../uml/symbols/SymbolElementMap.html)`
`[getSymbolElementMap](#getSymbolElementMap())()`
Get element symbol map.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTitle](#getTitle())()`

`[TransactionManager](../../uml2/transaction/TransactionManager.html)`
`[getTransactionsManager](#getTransactionsManager())()`
Return transaction manager.
`com.nomagic.magicdraw.uml.UMLModelProjectFeature`
`[getUMLModelStorageFeature](#getUMLModelStorageFeature())()`

`[ProjectWindow](../ui/ProjectWindow.html)`
`[getWindow](#getWindow(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectWindow](../ui/ProjectWindow.html)>`
`[getWindows](#getWindows())()`

`boolean`
`[hasListeners](#hasListeners())()`

`boolean`
`[hasWindow](#hasWindow(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`

`void`
`[invalidateHasUnloadedManuallyReachableModules](#invalidateHasUnloadedManuallyReachableModules())()`
Invalidates the [`getHasUnloadedManuallyReachableModules()`](#getHasUnloadedManuallyReachableModules()) flag
`boolean`
`[isClosing](#isClosing())()`

`static boolean`
`[isCreateBrowser](#isCreateBrowser())()`

`boolean`
`[isDirty](#isDirty())()`
Returns true if this project was modified after last save/load.
`boolean`
`[isDisposed](#isDisposed(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Check if given element is unregistered from project.
`boolean`
`[isEditable](#isEditable())()`
Checks if an element can be edited.
`static boolean`
`[isElementDisposed](#isElementDisposed(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`
Check if given element is unregistered from project.
`boolean`
`[isElementInProject](#isElementInProject(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Check if element with a given id is in this project.
`boolean`
`[isEMFProxiesSupported](#isEMFProxiesSupported())()`
Returns whether the registry supports EMF proxies.
`boolean`
`[isEsiProject](#isEsiProject())()`
Determines whether this is an ESI project
`boolean`
`[isFrozen](#isFrozen())()`

`boolean`
`[isLoaded](#isLoaded())()`
Return value of "loaded" flag
`boolean`
`[isModel](#isModel(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Checks if the given element is a one of the models in this project.
`boolean`
`[isModel](#isModel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) element)`
Checks if the given element is a one of the models in this project.
`boolean`
`[isNeedLocallySave](#isNeedLocallySave())()`
Teamwork projects after commit can be saved locally, using flag to hold state about teamwork
 projects were saved locally.
`boolean`
`[isNew](#isNew())()`

`boolean`
`[isParentOf](#isParentOf(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) obj)`
Returns true, if current element is parent of given element.
`boolean`
`[isPreloadProject](#isPreloadProject())()`

`boolean`
`[isProjectClosed](#isProjectClosed())()`
Checks if this project was already disposed(closed).
`boolean`
`[isProjectDisposed](#isProjectDisposed())()`
Deprecated.
use #isProjectClosed
`boolean`
`[isReady](#isReady())()`

`boolean`
`[isRelocatedIn](#isRelocatedIn())()`

`boolean`
`[isRemote](#isRemote())()`
Returns the remote or not remote state of the project.
`boolean`
`[isUMLProject](#isUMLProject())()`
To check if project is for UML models.
`void`
`[refAddInstance](#refAddInstance(javax.jmi.reflect.RefBaseObject))(javax.jmi.reflect.RefBaseObject instance)`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<javax.jmi.reflect.RefBaseObject>`
`[refAllOfClasses](#refAllOfClasses(java.util.Set))([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass> classes)`

`void`
`[refRemoveInstance](#refRemoveInstance(javax.jmi.reflect.RefBaseObject))(javax.jmi.reflect.RefBaseObject instance)`

`<T> void`
`[register](#register(java.lang.Class,T))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> type,
 T service)`
Registers the specified service.
`void`
`[removeAllPropertyChangeListeners](#removeAllPropertyChangeListeners())()`
Removes all property change listeners from this element.
`void`
`[removeElementByID](#removeElementByID(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) obj)`
Unregister the object by id.
`static void`
`[removeFeature](#removeFeature(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) feature)`
Unregister a feature for a new project.
`void`
`[removeFromQueryChangeRegistry](#removeFromQueryChangeRegistry(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement modelElement)`

`void`
`[removePropertyChangeListener](#removePropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Unregisters the given listener from the element.
`void`
`[removeWindow](#removeWindow(com.nomagic.magicdraw.ui.ProjectWindow))([ProjectWindow](../ui/ProjectWindow.html) window)`

`void`
`[reSetDirty](#reSetDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType))(boolean dirty,
 [StateChangeHandler.DirtyType](../utils/StateChangeHandler.DirtyType.html) dirtyType)`
Marks this project modified and sets modification type without checking previous project's dirty type.
`void`
`[resetDynamicRepository](#resetDynamicRepository())()`
Removes current dynamic repository if such exist and installs a new dynamic repository.
`void`
`[setClosing](#setClosing(boolean))(boolean closing)`
Set closing project state
`void`
`[setCounter](#setCounter(com.nomagic.magicdraw.core.MDCounter))(com.nomagic.magicdraw.core.MDCounter c)`
Sets the counter for the project.
`static void`
`[setCreateBrowser](#setCreateBrowser(boolean))(boolean createBrowser)`

`void`
`[setDirectory](#setDirectory(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dir)`
Deprecated.
use [`setFileName(String)`](#setFileName(java.lang.String))
`void`
`[setDirty](#setDirty(boolean))(boolean dirty)`
Deprecated.
Use `[setDirty(boolean dirty, DirtyType dirtyType)](#setDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType))`.
`void`
`[setDirty](#setDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType))(boolean dirty,
 [StateChangeHandler.DirtyType](../utils/StateChangeHandler.DirtyType.html) dirtyType)`
Marks this project modified and sets modification type depending on previous type.
`void`
`[setExporterDescription](#setExporterDescription(com.nomagic.persistence.XmiExporterDescription))([XmiExporterDescription](../../persistence/XmiExporterDescription.html) exporterDescription)`

`void`
`[setFileName](#setFileName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName)`
Set the name of file as location of this project.
`void`
`[setFrozen](#setFrozen(boolean))(boolean frozen)`
Set frozen flag.
`void`
`[setID](#setID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Sets the specified ID to the `Element`.
`void`
`[setLoaded](#setLoaded(boolean))(boolean loaded)`
Set "Loaded" flag for project.
`void`
`[setModel](#setModel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) p)`

`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Deprecated.
use [`setFileName(String)`](#setFileName(java.lang.String))
`void`
`[setNeedLocallySave](#setNeedLocallySave(boolean))(boolean locallySaved)`

`void`
`[setPrimaryProject](#setPrimaryProject(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject primaryProject)`

`void`
`[setPrimaryProject](#setPrimaryProject(com.nomagic.ci.persistence.IProject,boolean,boolean))(com.nomagic.ci.persistence.IProject primaryProject,
 boolean closeOldProject,
 boolean changeModel)`
Set primary project.
`void`
`[setRelocatingIn](#setRelocatingIn(boolean))(boolean relocating)`
Set project state to relocating.
`void`
`[setTitle](#setTitle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)`

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[sGetID](#sGetID())()`
Returns the actual ID of the `Element`.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toDebugRepresentation](#toDebugRepresentation())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Returns string representation of this element.
Methods inherited from class com.dassault_systemes.modeler.foundation.project.ModelElementProjectImpl
`getOptionalService, getService, getServiceProvider`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../uml/BaseElement.html)
`[canAdd](../uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../uml/BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.nomagic.magicdraw.uml.[MDElement](../uml/MDElement.html)
`[getProject](../uml/MDElement.html#getProject())`
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
MANY_CLASSES_UPDATED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MANY_CLASSES_UPDATED
Event type when many elements in project are changed (for example after project update,massive source reverse operation and etc)
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.Project.MANY_CLASSES_UPDATED)
FILE_NAME_PROPERTY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FILE_NAME_PROPERTY
Project file name property
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.Project.FILE_NAME_PROPERTY)
DIRTY_PROPERTY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIRTY_PROPERTY
Project "dirty" flag change
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.Project.DIRTY_PROPERTY)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Project
public Project()
Constructor creates project.
 ============ METHOD DETAIL ========== 
Method Details
isCreateBrowser
public static boolean isCreateBrowser()
setCreateBrowser
public static void setCreateBrowser(boolean createBrowser)
getElementsIDs
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getElementsIDs([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> elements)
Retrieves the elements ids from DTObjects collection.
Parameters:
`elements` - collection of elements to get ID's for
Returns:
the collection of elements ids from the DTObjects collection.
executeIntensiveAction
public boolean executeIntensiveAction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) reason)
Executes time-intensive action if user agrees to.
Parameters:
`reason` - reason why the action might take a long time
Returns:
true if execute action
getProxyManager
@OpenApipublic [ProxyManager](proxy/ProxyManager.html) getProxyManager()
Returns:
proxy manager of the project
getDSL
public com.nomagic.magicdraw.dsl.DSL getDSL()
Returns project DSL service instance.
Returns:
the manager.
getDSLManager
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public com.nomagic.magicdraw.ui.dsl.DSLManager getDSLManager()
Deprecated.
use [`getDSL()`](#getDSL())
Returns project customization manager.
Returns:
the manager
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
getCommandHistory
public com.nomagic.magicdraw.commands.CommandHistory getCommandHistory()
Returns:
project command history.
getElementByIDQuerier
public com.nomagic.magicdraw.core.Project.ElementByIDFetcher getElementByIDQuerier()
getActiveDiagram
@CheckForNull
@OpenApipublic [DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) getActiveDiagram()
Returns currently active diagram.
Returns:
currently active diagram presentation element.
See Also:
[`DiagramPresentationElement`](../uml/symbols/DiagramPresentationElement.html)
getActiveAbstractDiagram
@CheckForNullpublic [AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) getActiveAbstractDiagram()
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
setModel
public void setModel([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) p)
getTitle
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTitle()
Returns:
project title
setTitle
public void setTitle([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)
getFileName
@CheckForNull
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFileName()
Method returns file name of this project. If file name is undefined returns project name.
Returns:
file name of this project.
getDirectory
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDirectory()
Deprecated.
use #getFile.getParent
Returns project directory.
Returns:
project location directory.
setDirectory
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void setDirectory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dir)
Deprecated.
use [`setFileName(String)`](#setFileName(java.lang.String))
Sets the project directory.
Parameters:
`dir` - the new project directory.
setName
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void setName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Deprecated.
use [`setFileName(String)`](#setFileName(java.lang.String))
Sets the project name.
Parameters:
`name` - the new project name.
getFile
public com.nomagic.utils.ExtendedFile getFile()
Method returns file of this project.
Returns:
file of this project
setFileName
public void setFileName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName)
Set the name of file as location of this project. Only local projects or locally saved remote projects can have file name.
Parameters:
`fileName` - absolute file path
getCounter
public com.nomagic.magicdraw.core.MDCounter getCounter()
Returns:
id counter
getStyleManager
@CheckForNullpublic [StyleManager](../properties/StyleManager.html) getStyleManager()
Returns style manager
Returns:
style manager
getProjectEditorWindowsManager
public com.nomagic.magicdraw.ui.ProjectEditorWindowsManager getProjectEditorWindowsManager()
Returns:
editor windows manager
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
isUMLProject
public boolean isUMLProject()
To check if project is for UML models.
Returns:
true if project is suitable for creating UML models
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
setCounter
public void setCounter(com.nomagic.magicdraw.core.MDCounter c)
Sets the counter for the project.
Parameters:
`c` - the new counter;
addElementByID
public void addElementByID([BaseElement](../uml/BaseElement.html) obj,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) oldID)
Register the object by id.
 The record about this object and its old id is removed.
Specified by:
`addElementByID` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRegistry`
Parameters:
`obj` - the object to register.
`oldID` - the old id of the object.
addToProjectRepository
@OpenApipublic void addToProjectRepository([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Adds element into this project repository and removes it from previous
 project repository. If element does not have an ID then it will be
 created. 
After this operation element can be retrieved from project by [`getElementByID(String)`](#getElementByID(java.lang.String)).
Parameters:
`element` - any element
removeElementByID
public void removeElementByID([BaseElement](../uml/BaseElement.html) obj)
Unregister the object by id.
 The record about this object and is removed.
Specified by:
`removeElementByID` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRegistry`
Parameters:
`obj` - the object.
addToQueryChangeRegistry
public void addToQueryChangeRegistry(com.dassault_systemes.modeler.foundation.model.ModelElement element)
removeFromQueryChangeRegistry
public void removeFromQueryChangeRegistry(com.dassault_systemes.modeler.foundation.model.ModelElement modelElement)
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
getPresentationElementByID
@CheckForNullpublic [BaseElement](../uml/BaseElement.html) getPresentationElementByID([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementID)
Return the presentation element with given id from currently registered elements.
Parameters:
`elementID` - the id of the element, cannot be null
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
getElementsByIDs
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> getElementsByIDs([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> ids)
Return the objects by given ids.
Parameters:
`ids` - the collection of the ids of the objects.
Returns:
the collection of objects with given ids.
getElementsByIDs
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> getElementsByIDs([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> ids,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../uml/BaseElement.html)>> collectionFactory)
Return the objects by given ids.
Parameters:
`ids` - the collection of the ids of the objects.
Returns:
the collection of objects with given ids.
getAllIDS
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getAllIDS()
Returns the collection of all ids in the project.
Returns:
the collection of all ids in the project.
getAllElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../uml/BaseElement.html)> getAllElements()
Gets collection of all model elements in the project
Specified by:
`getAllElements` in interface `com.nomagic.uml2.ext.jmi.reflect.ElementRegistry`
Returns:
collection of elements
isProjectClosed
public boolean isProjectClosed()
Checks if this project was already disposed(closed). Such project cannot be activated any more.
Specified by:
`isProjectClosed` in interface `com.dassault_systemes.modeler.foundation.project.ModelElementProject`
Returns:
true if project was disposed (closed)
isProjectDisposed
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public boolean isProjectDisposed()
Deprecated.
use #isProjectClosed
Checks if this project was already disposed(closed). Such project cannot be activated any more.
Returns:
true if project was disposed (closed)
isClosing
public boolean isClosing()
Specified by:
`isClosing` in interface `com.dassault_systemes.modeler.foundation.project.ModelElementProject`
Returns:
true if project is closing (preCloseFinal event is fired)
setClosing
public void setClosing(boolean closing)
Set closing project state
Parameters:
`closing` - true if project is closing
getStateChangeHandler
@OpenApipublic [StateChangeHandler](../utils/StateChangeHandler.html) getStateChangeHandler()
Returns:
StateChangeHandler for this project.
elementAdded
public void elementAdded([BaseElement](../uml/BaseElement.html) element)
Marks element as added, if it was previously removed its id is removed from id collection.
Parameters:
`element` - element id which was added.
elementRemoved
public void elementRemoved([BaseElement](../uml/BaseElement.html) obj)
Marks element removed, its id added to mDeletedObjectIDS.
Parameters:
`obj` - element which was removed.
isElementInProject
public boolean isElementInProject([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Check if element with a given id is in this project.
Parameters:
`id` - element id
Returns:
true if element with given id is registered in project and is not removed.
addWindow
public void addWindow([ProjectWindow](../ui/ProjectWindow.html) window)
removeWindow
public void removeWindow([ProjectWindow](../ui/ProjectWindow.html) window)
getWindows
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectWindow](../ui/ProjectWindow.html)> getWindows()
hasWindow
public boolean hasWindow([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
getWindow
public [ProjectWindow](../ui/ProjectWindow.html) getWindow([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
getStereotypesStyleChangeHandler
public com.nomagic.magicdraw.uml.symbols.StereotypesStyleChangeManager getStereotypesStyleChangeHandler()
getRepository
@OpenApipublic [AbstractRepository](../../uml2/ext/jmi/reflect/AbstractRepository.html) getRepository()
Get project repository.
Specified by:
`getRepository` in interface `com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider`
Returns:
repository.
resetDynamicRepository
public void resetDynamicRepository()
Removes current dynamic repository if such exist and installs a new dynamic repository.
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
isModel
public boolean isModel(@CheckForNull
 [BaseElement](../uml/BaseElement.html) element)
Checks if the given element is a one of the models in this project.
Parameters:
`element` - element to check.
Returns:
true if given element is a one of the models in this project.
isModel
public boolean isModel([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) element)
Description copied from interface: `com.nomagic.uml2.project.ElementProject`
Checks if the given element is a one of the models in this project.
Specified by:
`isModel` in interface `com.nomagic.uml2.project.ElementProject`
Parameters:
`element` - element to check
Returns:
true if given package belongs to models of this project
See Also:
`ElementProject.getModels()`
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
Description copied from interface: `com.nomagic.uml2.project.ElementProject`
Returns a list of models in the project
 (the primary model of the project and all the models of the modules (attached projects)).
Specified by:
`getModels` in interface `com.nomagic.uml2.project.ElementProject`
Returns:
models
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
getRemoteID
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRemoteID()
isLoaded
public boolean isLoaded()
Return value of "loaded" flag
Returns:
true if this project was loaded from some location or is saved to some location (is not just created from template)
getLoadedFrom
public [ProjectDescriptor](project/ProjectDescriptor.html) getLoadedFrom()
Return location from were project was loaded.
 For Teamwork project returns local file if project was saved into file (or was loaded from file).
Returns:
location of project
setLoaded
public void setLoaded(boolean loaded)
Set "Loaded" flag for project. Project created from template is not "loaded"
Parameters:
`loaded` - loaded flag
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
Returns Project for a given element
Parameters:
`element` - project element.
Returns:
project in which a given element exists.
See Also:
`ProjectProvider`
getExporterDescription
@CheckForNullpublic [XmiExporterDescription](../../persistence/XmiExporterDescription.html) getExporterDescription()
setExporterDescription
public void setExporterDescription([XmiExporterDescription](../../persistence/XmiExporterDescription.html) exporterDescription)
getTransactionsManager
public [TransactionManager](../../uml2/transaction/TransactionManager.html) getTransactionsManager()
Return transaction manager.
Returns:
transaction manager
isNeedLocallySave
public boolean isNeedLocallySave()
Teamwork projects after commit can be saved locally, using flag to hold state about teamwork
 projects were saved locally.
Returns:
true if project was not locally saved. Should be used only for teamwork projects.
setNeedLocallySave
public void setNeedLocallySave(boolean locallySaved)
setPrimaryProject
public void setPrimaryProject(com.nomagic.ci.persistence.IProject primaryProject)
setPrimaryProject
public void setPrimaryProject(com.nomagic.ci.persistence.IProject primaryProject,
 boolean closeOldProject,
 boolean changeModel)
Set primary project.
Parameters:
`primaryProject` - project to set.
`closeOldProject` - close old project (do not close project when adding to teamwork).
`changeModel` - dispose old model (do not dispose UML model when adding to teamwork)
getPrimaryProject
@OpenApipublic com.nomagic.ci.persistence.IPrimaryProject getPrimaryProject()
Primary project of MagicDraw project.
Returns:
primary project.
addFeature
public static void addFeature([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) feature)
Register a feature for a new project.
Parameters:
`feature` - feature name
removeFeature
public static void removeFeature([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) feature)
Unregister a feature for a new project.
Parameters:
`feature` - name
getFeatures
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getFeatures()
Return registered features for a new project.
Returns:
registered features for a new project.
getUMLModelStorageFeature
public com.nomagic.magicdraw.uml.UMLModelProjectFeature getUMLModelStorageFeature()
isNew
public boolean isNew()
Returns:
true if project is new and was never saved
getLocationUri
public org.eclipse.emf.common.util.URI getLocationUri()
Get URI location according the primary project.
Returns:
URI.
isFrozen
public boolean isFrozen()
Returns:
true if project is frozen
setFrozen
public void setFrozen(boolean frozen)
Set frozen flag. Frozen projects do not provide some data.
Parameters:
`frozen` - frozen flag
isReady
public boolean isReady()
Returns:
true if project is ready to use. It has primary project, it is not closed.
isRelocatedIn
public boolean isRelocatedIn()
Returns:
true if project is in relocating state
setRelocatingIn
public void setRelocatingIn(boolean relocating)
Set project state to relocating. Project is relocating if project content is coming from other project.
 This other project is in "relocated" state.
Parameters:
`relocating` - relocating state
refAddInstance
public void refAddInstance(javax.jmi.reflect.RefBaseObject instance)
Specified by:
`refAddInstance` in interface `com.nomagic.uml2.ext.jmi.reflect.ElementRegistry`
refRemoveInstance
public void refRemoveInstance(javax.jmi.reflect.RefBaseObject instance)
Specified by:
`refRemoveInstance` in interface `com.nomagic.uml2.ext.jmi.reflect.ElementRegistry`
refAllOfClasses
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<javax.jmi.reflect.RefBaseObject> refAllOfClasses([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass> classes)
Specified by:
`refAllOfClasses` in interface `com.nomagic.uml2.ext.jmi.reflect.ElementRegistry`
isPreloadProject
public boolean isPreloadProject()
Specified by:
`isPreloadProject` in interface `com.nomagic.uml2.ext.jmi.reflect.ElementRegistry`
Specified by:
`isPreloadProject` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRegistry`
getBinaryStreamAtticCleaner
public com.nomagic.magicdraw.core.BinaryStreamAtticCleaner getBinaryStreamAtticCleaner()
getHasUnloadedManuallyReachableModules
public boolean getHasUnloadedManuallyReachableModules()
Returns:
the hasUnloadedManuallyReachableModules
invalidateHasUnloadedManuallyReachableModules
public void invalidateHasUnloadedManuallyReachableModules()
Invalidates the [`getHasUnloadedManuallyReachableModules()`](#getHasUnloadedManuallyReachableModules()) flag
toDebugRepresentation
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toDebugRepresentation()
register
public <T> void register([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> type,
 T service)
Registers the specified service.
Type Parameters:
`T` - type of the service.
Parameters:
`type` - service type.
`service` - the service.
isEMFProxiesSupported
public boolean isEMFProxiesSupported()
Description copied from interface: `com.nomagic.uml2.ext.jmi.reflect.ElementRegistry`
Returns whether the registry supports EMF proxies.
Specified by:
`isEMFProxiesSupported` in interface `com.nomagic.uml2.ext.jmi.reflect.ElementRegistry`
Specified by:
`isEMFProxiesSupported` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRegistry`
Returns:
true if the element registry supports EMF proxies, otherwise - false.
generateID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) generateID()
Generate ID.
getID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getID()
Description copied from interface: `[BaseElement](../uml/BaseElement.html#getID())`
Returns the ID of the `Element`.
 If the ID is `null`, new id for an element is generated.
 Element id is persistence and does not change during project save/load.
Specified by:
`[getID](../uml/BaseElement.html#getID())` in interface `[BaseElement](../uml/BaseElement.html)`
Returns:
the ID of the `Element`.
sGetID
public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sGetID()
Description copied from interface: `[BaseElement](../uml/BaseElement.html#sGetID())`
Returns the actual ID of the `Element`. May return null if ID was not generated
 or set for this element.
Specified by:
`[sGetID](../uml/BaseElement.html#sGetID())` in interface `[BaseElement](../uml/BaseElement.html)`
Returns:
the ID of the `Element`.
See Also:
[`BaseElement.getID()`](../uml/BaseElement.html#getID())
setID
public void setID([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Description copied from interface: `[BaseElement](../uml/BaseElement.html#setID(java.lang.String))`
Sets the specified ID to the `Element`.
Specified by:
`[setID](../uml/BaseElement.html#setID(java.lang.String))` in interface `[BaseElement](../uml/BaseElement.html)`
Parameters:
`id` - the id to be set.
clone
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) clone()
 throws [CloneNotSupportedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CloneNotSupportedException.html)
Specified by:
`[clone](../uml/BaseElement.html#clone())` in interface `[BaseElement](../uml/BaseElement.html)`
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Throws:
`[CloneNotSupportedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CloneNotSupportedException.html)`
addPropertyChangeListener
public void addPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Description copied from interface: `[BaseElement](../uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener))`
Registers the listener to the element. The given listener will get notifications about
 property changes in this element.
Specified by:
`[addPropertyChangeListener](../uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener))` in interface `[BaseElement](../uml/BaseElement.html)`
Parameters:
`listener` - the `PropertyChangeListener` to be added.
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
hasListeners
public boolean hasListeners()
removePropertyChangeListener
public void removePropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Description copied from interface: `[BaseElement](../uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener))`
Unregisters the given listener from the element. The given listener will not get any notifications about
 property changes in this element.
Specified by:
`[removePropertyChangeListener](../uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener))` in interface `[BaseElement](../uml/BaseElement.html)`
Parameters:
`listener` - the PropertyChangeListener to be removed.
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
removeAllPropertyChangeListeners
public void removeAllPropertyChangeListeners()
Description copied from interface: `[BaseElement](../uml/BaseElement.html#removeAllPropertyChangeListeners())`
Removes all property change listeners from this element.
Specified by:
`[removeAllPropertyChangeListeners](../uml/BaseElement.html#removeAllPropertyChangeListeners())` in interface `[BaseElement](../uml/BaseElement.html)`
firePropertyChange
public void firePropertyChange([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)
Description copied from interface: `[BaseElement](../uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))`
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new values are equal or null.
Specified by:
`[firePropertyChange](../uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))` in interface `[BaseElement](../uml/BaseElement.html)`
Parameters:
`propertyName` - the programmatic name of the property that was changed.
`oldValue` - the old value of the property
`newValue` - the new value of the property
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
atInsert
public void atInsert()
Description copied from interface: `[BaseElement](../uml/BaseElement.html#atInsert())`
This method is called then this element is added into the project.
Specified by:
`[atInsert](../uml/BaseElement.html#atInsert())` in interface `[BaseElement](../uml/BaseElement.html)`
dispose
public void dispose()
Destroys the project. After this method call project can not be used any more.
Specified by:
`[dispose](../uml/BaseElement.html#dispose())` in interface `[BaseElement](../uml/BaseElement.html)`
accept
public void accept([Visitor](../uml/Visitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../uml/MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
 See "Visitor" pattern for more details.
Specified by:
`[accept](../uml/MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../uml/MDElement.html)`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
accept
public void accept([AbstractVisitor](../uml/AbstractVisitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[BaseElement](../uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor))`
Method accepts a visitor, and calls method visit < class name > (this) of visitor.
Specified by:
`[accept](../uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor))` in interface `[BaseElement](../uml/BaseElement.html)`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
getName
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Returns project name.
Specified by:
`[getName](../uml/MDElement.html#getName())` in interface `[MDElement](../uml/MDElement.html)`
Returns:
project name.
getHumanName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHumanName()
Description copied from interface: `[BaseElement](../uml/BaseElement.html#getHumanName())`
Returns human representation of the element. Usually human name is constructed from element class type
 and name.
Specified by:
`[getHumanName](../uml/BaseElement.html#getHumanName())` in interface `[BaseElement](../uml/BaseElement.html)`
Returns:
the human name of the element.
getProjectImpl
public [Project](Project.html) getProjectImpl()
Description copied from interface: `[MDElement](../uml/MDElement.html#getProjectImpl())`
This method is deprecated and will be removed soon.
Specified by:
`[getProjectImpl](../uml/MDElement.html#getProjectImpl())` in interface `[MDElement](../uml/MDElement.html)`
Returns:
project
getSortKeys
public final com.dassault_systemes.modeler.foundation.common.sort.SortKeys getSortKeys()
Description copied from interface: `[MDElement](../uml/MDElement.html#getSortKeys())`
Implementation of getSortKeys() from Sortable interface.
Specified by:
`[getSortKeys](../uml/MDElement.html#getSortKeys())` in interface `[MDElement](../uml/MDElement.html)`
Returns:
the array of predefined sort keys.
getHumanType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHumanType()
Description copied from interface: `[BaseElement](../uml/BaseElement.html#getHumanType())`
Returns human representation of the element type. Contains only element type without element name.
Specified by:
`[getHumanType](../uml/BaseElement.html#getHumanType())` in interface `[BaseElement](../uml/BaseElement.html)`
Returns:
the human type of the element.
getResourceID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getResourceID()
Specified by:
`[getResourceID](../uml/MDElement.html#getResourceID())` in interface `[MDElement](../uml/MDElement.html)`
canAdd
public final boolean canAdd([BaseElement](../uml/BaseElement.html) element,
 boolean checkPermissions)
Description copied from interface: `[BaseElement](../uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean))`
Checks if this element can add a given element.
 

 Following rules must be true to have result true: 

 1.if checkTeamworkLock == true, this element must be locked for edit. 

 2.element can add given element as instance (class types are checked). 

 3.element can add given element as child (a given element is not a parent of current element etc.).
Specified by:
`[canAdd](../uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean))` in interface `[BaseElement](../uml/BaseElement.html)`
Parameters:
`element` - the element to add.
`checkPermissions` - check or not permissions.
Returns:
true if an element can add the given element as a child.
canDeleteChild
public boolean canDeleteChild([BaseElement](../uml/BaseElement.html) child)
Description copied from interface: `[BaseElement](../uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement))`
Checks if given element can be deleted from this element.
 Following rules must be true to have result true:
 1.this element must be editable.
 2.project must be editable.
 3.the type of given child must be valid for teamwork lock for edit operation
 (for example, class, package etc., not Attribute).
Specified by:
`[canDeleteChild](../uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement))` in interface `[BaseElement](../uml/BaseElement.html)`
Parameters:
`child` - a given child
Returns:
true, if the given element can be deleted from the current element.
canBeDeleted
public boolean canBeDeleted()
Description copied from interface: `[BaseElement](../uml/BaseElement.html#canBeDeleted())`
Checks if an element can be deleted from a project.
 Element cannot be deleted if it is not isEditable(),
 parent is not set, or parent does not allow to remove this element.
Specified by:
`[canBeDeleted](../uml/BaseElement.html#canBeDeleted())` in interface `[BaseElement](../uml/BaseElement.html)`
Returns:
true, if an element can be deleted from a project.
See Also:
[`BaseElement.isEditable()`](../uml/BaseElement.html#isEditable())
canAddInstance
public boolean canAddInstance([BaseElement](../uml/BaseElement.html) o)
Description copied from interface: `[BaseElement](../uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement))`
Checks if this object can add element of given type.
 Current implementation returns false.
Specified by:
`[canAddInstance](../uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement))` in interface `[BaseElement](../uml/BaseElement.html)`
Returns:
true if this object can elements of a given type.
canAddChild
public boolean canAddChild([BaseElement](../uml/BaseElement.html) o)
Specified by:
`[canAddChild](../uml/MDElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement))` in interface `[MDElement](../uml/MDElement.html)`
isEditable
public boolean isEditable()
Description copied from interface: `[BaseElement](../uml/BaseElement.html#isEditable())`
Checks if an element can be edited.
Specified by:
`[isEditable](../uml/BaseElement.html#isEditable())` in interface `[BaseElement](../uml/BaseElement.html)`
Returns:
true, if an element can be edited.
canAddChild
public boolean canAddChild()
Description copied from interface: `[BaseElement](../uml/BaseElement.html#canAddChild())`
Checks if new elements can be added to this element
Specified by:
`[canAddChild](../uml/BaseElement.html#canAddChild())` in interface `[BaseElement](../uml/BaseElement.html)`
Returns:
true, if new sub elements can be added.
getObjectParent
@CheckForNullpublic [BaseElement](../uml/BaseElement.html) getObjectParent()
Description copied from interface: `[BaseElement](../uml/BaseElement.html#getObjectParent())`
Returns the element parent.
 This implementation returns null. Should be overridden in subclasses.
Specified by:
`[getObjectParent](../uml/BaseElement.html#getObjectParent())` in interface `[BaseElement](../uml/BaseElement.html)`
Returns:
the parent of the element.
compareTo
public int compareTo(@Nonnull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Compares sort key at index 1 with given element's sort key at index 1.
Specified by:
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))` in interface `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`
Parameters:
`o` - the given object to compare to.
Returns:
key's comparison result(String.compareTo()).
isParentOf
public boolean isParentOf([BaseElement](../uml/BaseElement.html) obj)
Description copied from interface: `[BaseElement](../uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement))`
Returns true, if current element is parent of given element.
 Return false in this implementation.
Specified by:
`[isParentOf](../uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement))` in interface `[BaseElement](../uml/BaseElement.html)`
Parameters:
`obj` - the given element(possible child).
Returns:
true if obj is the parent of this object.
getClassType
public [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) getClassType()
Description copied from interface: `[BaseElement](../uml/BaseElement.html#getClassType())`
Gets the type of the element class.
 Every element has its own ClassType.
 Usually this class type is class of element or class interface of an element.
 All types are registered in ClassTypes.
Specified by:
`[getClassType](../uml/BaseElement.html#getClassType())` in interface `[BaseElement](../uml/BaseElement.html)`
Returns:
the type of the element.
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Returns string representation of this element.
 Useful for debugging purposes.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
canChangeParent
public boolean canChangeParent([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) elements,
 [BaseElement](../uml/BaseElement.html) newParent)
Description copied from interface: `[BaseElement](../uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement))`
Returns true, if element can change parent.
Specified by:
`[canChangeParent](../uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement))` in interface `[BaseElement](../uml/BaseElement.html)`
Parameters:
`elements` - collection of the elements, whose will change the parent together with this.
`newParent` - new parent object.
Returns:
true if an element can change parent.

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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIRTY_PROPERTY">DIRTY_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Project "dirty" flag change</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FILE_NAME_PROPERTY">FILE_NAME_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Project file name property</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MANY_CLASSES_UPDATED">MANY_CLASSES_UPDATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Event type when many elements in project are changed (for example after project update,massive source reverse operation and etc)</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SELECTION_CHANGED">SELECTION_CHANGED</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">now SelectionProvider fires selection changed,
 use <a href="../ui/SelectionProvider.SelectionChangedListener.html" title="interface in com.nomagic.magicdraw.ui"><code>SelectionProvider.SelectionChangedListener</code></a>
 The diagram objects selecting event type and naming.</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Project</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor creates project.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a><wbr/>(<a href="../uml/AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml">AbstractVisitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method accepts a visitor, and calls method visit &lt; class name &gt; (this) of visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a><wbr/>(<a href="../uml/Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method accepts a visitor, and calls method "visit&lt;class name&gt;(this)" of a visitor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addElementByID(com.nomagic.magicdraw.uml.BaseElement,java.lang.String)">addElementByID</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> oldID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Register the object by id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addFeature(java.lang.String)">addFeature</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Register a feature for a new project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers the listener to the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addToProjectRepository(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addToProjectRepository</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds element into this project repository and removes it from previous
 project repository.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addToQueryChangeRegistry(com.dassault_systemes.modeler.foundation.model.ModelElement)">addToQueryChangeRegistry</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addWindow(com.nomagic.magicdraw.ui.ProjectWindow)">addWindow</a><wbr/>(<a href="../ui/ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> window)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#atInsert()">atInsert</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method is called then this element is added into the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean checkPermissions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if this element can add a given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddChild()">canAddChild</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if new elements can be added to this element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if this object can add element of given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canBeDeleted()">canBeDeleted</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if an element can be deleted from a project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> elements,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> newParent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if element can change parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">canDeleteChild</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if given element can be deleted from this element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareTo(java.lang.Object)">compareTo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Compares sort key at index 1 with given element's sort key at index 1.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Destroys the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#elementAdded(com.nomagic.magicdraw.uml.BaseElement)">elementAdded</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks element as added, if it was previously removed its id is removed from id collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#elementRemoved(com.nomagic.magicdraw.uml.BaseElement)">elementRemoved</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks element removed, its id added to mDeletedObjectIDS.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#executeIntensiveAction(java.lang.String)">executeIntensiveAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reason)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Executes time-intensive action if user agrees to.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generateID()">generateID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generate ID.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveAbstractDiagram()">getActiveAbstractDiagram</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveDiagram()">getActiveDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns currently active diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllElements()">getAllElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets collection of all model elements in the project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllIDS()">getAllIDS</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the collection of all ids in the project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.BinaryStreamAtticCleaner</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBinaryStreamAtticCleaner()">getBinaryStreamAtticCleaner</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ui/browser/Browser.html" title="class in com.nomagic.magicdraw.ui.browser">Browser</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBrowser()">getBrowser</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the type of the element class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.commands.CommandHistory</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCommandHistory()">getCommandHistory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.MDCounter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCounter()">getCounter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDirectory()">getDirectory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use #getFile.getParent</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../utils/StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirtyType()">getDirtyType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns project dirty type if project is dirty, otherwise - null.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.dsl.DSL</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDSL()">getDSL</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns project DSL service instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>com.nomagic.magicdraw.ui.dsl.DSLManager</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDSLManager()">getDSLManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getDSL()"><code>getDSL()</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementByID(java.lang.String)">getElementByID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the element with given id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.Project.ElementByIDFetcher</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementByIDQuerier()">getElementByIDQuerier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsByIDs(java.util.Collection)">getElementsByIDs</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the objects by given ids.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsByIDs(java.util.Collection,java.util.function.Supplier)">getElementsByIDs</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;&gt; collectionFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the objects by given ids.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsFactory()">getElementsFactory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Provides UML elements factory</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsIDs(java.util.Collection)">getElementsIDs</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves the elements ids from DTObjects collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExporterDescription()">getExporterDescription</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeatures()">getFeatures</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return registered features for a new project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.utils.ExtendedFile</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFile()">getFile</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method returns file of this project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileName()">getFileName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method returns file name of this project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHasUnloadedManuallyReachableModules()">getHasUnloadedManuallyReachableModules</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHumanName()">getHumanName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns human representation of the element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHumanType()">getHumanType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns human representation of the element type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the ID of the <code>Element</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoadedFrom()">getLoadedFrom</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return location from were project was loaded.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.util.URI</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLocationUri()">getLocationUri</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get URI location according the primary project.</div>
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
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a list of models in the project
 (the primary model of the project and all the models of the modules (attached projects)).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns project name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectParent()">getObjectParent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the element parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="options/ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOptions()">getOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Getter for project options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementByID(java.lang.String)">getPresentationElementByID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the presentation element with given id from currently registered elements.</div>
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
<div class="block">Returns Project for a given element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject(java.util.Collection)">getProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns Project from first given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.ProjectEditorWindowsManager</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectEditorWindowsManager()">getProjectEditorWindowsManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectImpl()">getProjectImpl</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method is deprecated and will be removed soon.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="proxy/ProxyManager.html" title="interface in com.nomagic.magicdraw.core.proxy">ProxyManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProxyManager()">getProxyManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemoteID()">getRemoteID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/jmi/reflect/AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepository()">getRepository</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get project repository.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/jmi/RepositoryListenerRegistry.html" title="interface in com.nomagic.uml2.ext.jmi">RepositoryListenerRegistry</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepositoryListenerRegistry()">getRepositoryListenerRegistry</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return listener registry for repository.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourceID()">getResourceID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/jmi/smartlistener/SmartEventSupport.html" title="interface in com.nomagic.uml2.ext.jmi.smartlistener">SmartEventSupport</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSmartEventSupport()">getSmartEventSupport</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns registry that allows to register smart listener configurations by element type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final com.dassault_systemes.modeler.foundation.common.sort.SortKeys</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSortKeys()">getSortKeys</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Implementation of getSortKeys() from Sortable interface.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../utils/StateChangeHandler.html" title="class in com.nomagic.magicdraw.utils">StateChangeHandler</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStateChangeHandler()">getStateChangeHandler</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.StereotypesStyleChangeManager</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypesStyleChangeHandler()">getStereotypesStyleChangeHandler</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyleManager()">getStyleManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns style manager</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/symbols/SymbolElementMap.html" title="class in com.nomagic.magicdraw.uml.symbols">SymbolElementMap</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSymbolElementMap()">getSymbolElementMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get element symbol map.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTitle()">getTitle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/transaction/TransactionManager.html" title="interface in com.nomagic.uml2.transaction">TransactionManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransactionsManager()">getTransactionsManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return transaction manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.UMLModelProjectFeature</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUMLModelStorageFeature()">getUMLModelStorageFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ui/ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWindow(java.lang.String)">getWindow</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../ui/ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWindows()">getWindows</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasListeners()">hasListeners</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasWindow(java.lang.String)">hasWindow</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#invalidateHasUnloadedManuallyReachableModules()">invalidateHasUnloadedManuallyReachableModules</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invalidates the <a href="#getHasUnloadedManuallyReachableModules()"><code>getHasUnloadedManuallyReachableModules()</code></a> flag</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isClosing()">isClosing</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateBrowser()">isCreateBrowser</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDirty()">isDirty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if this project was modified after last save/load.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisposed(com.nomagic.magicdraw.uml.BaseElement)">isDisposed</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if given element is unregistered from project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEditable()">isEditable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if an element can be edited.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementDisposed(com.dassault_systemes.modeler.foundation.model.ModelElement)">isElementDisposed</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given element is unregistered from project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementInProject(java.lang.String)">isElementInProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if element with a given id is in this project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEMFProxiesSupported()">isEMFProxiesSupported</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether the registry supports EMF proxies.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEsiProject()">isEsiProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Determines whether this is an ESI project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFrozen()">isFrozen</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLoaded()">isLoaded</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return value of "loaded" flag</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isModel(com.nomagic.magicdraw.uml.BaseElement)">isModel</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if the given element is a one of the models in this project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isModel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">isModel</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if the given element is a one of the models in this project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNeedLocallySave()">isNeedLocallySave</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Teamwork projects after commit can be saved locally, using flag to hold state about teamwork
 projects were saved locally.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNew()">isNew</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if current element is parent of given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isPreloadProject()">isPreloadProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isProjectClosed()">isProjectClosed</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if this project was already disposed(closed).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isProjectDisposed()">isProjectDisposed</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use #isProjectClosed</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isReady()">isReady</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRelocatedIn()">isRelocatedIn</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemote()">isRemote</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the remote or not remote state of the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUMLProject()">isUMLProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">To check if project is for UML models.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refAddInstance(javax.jmi.reflect.RefBaseObject)">refAddInstance</a><wbr/>(javax.jmi.reflect.RefBaseObject instance)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;javax.jmi.reflect.RefBaseObject&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refAllOfClasses(java.util.Set)">refAllOfClasses</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass&gt; classes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refRemoveInstance(javax.jmi.reflect.RefBaseObject)">refRemoveInstance</a><wbr/>(javax.jmi.reflect.RefBaseObject instance)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T&gt; void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#register(java.lang.Class,T)">register</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type,
 T service)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers the specified service.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAllPropertyChangeListeners()">removeAllPropertyChangeListeners</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all property change listeners from this element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeElementByID(com.nomagic.magicdraw.uml.BaseElement)">removeElementByID</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregister the object by id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeFeature(java.lang.String)">removeFeature</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Unregister a feature for a new project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeFromQueryChangeRegistry(com.dassault_systemes.modeler.foundation.model.ModelElement)">removeFromQueryChangeRegistry</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement modelElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregisters the given listener from the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeWindow(com.nomagic.magicdraw.ui.ProjectWindow)">removeWindow</a><wbr/>(<a href="../ui/ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> window)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reSetDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType)">reSetDirty</a><wbr/>(boolean dirty,
 <a href="../utils/StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a> dirtyType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks this project modified and sets modification type without checking previous project's dirty type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resetDynamicRepository()">resetDynamicRepository</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes current dynamic repository if such exist and installs a new dynamic repository.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setClosing(boolean)">setClosing</a><wbr/>(boolean closing)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set closing project state</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCounter(com.nomagic.magicdraw.core.MDCounter)">setCounter</a><wbr/>(com.nomagic.magicdraw.core.MDCounter c)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the counter for the project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setCreateBrowser(boolean)">setCreateBrowser</a><wbr/>(boolean createBrowser)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setDirectory(java.lang.String)">setDirectory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dir)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#setFileName(java.lang.String)"><code>setFileName(String)</code></a></div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExporterDescription(com.nomagic.persistence.XmiExporterDescription)">setExporterDescription</a><wbr/>(<a href="../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a> exporterDescription)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFileName(java.lang.String)">setFileName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the name of file as location of this project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFrozen(boolean)">setFrozen</a><wbr/>(boolean frozen)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set frozen flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setID(java.lang.String)">setID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the specified ID to the <code>Element</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoaded(boolean)">setLoaded</a><wbr/>(boolean loaded)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set "Loaded" flag for project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setModel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setModel</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> p)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#setFileName(java.lang.String)"><code>setFileName(String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNeedLocallySave(boolean)">setNeedLocallySave</a><wbr/>(boolean locallySaved)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPrimaryProject(com.nomagic.ci.persistence.IProject)">setPrimaryProject</a><wbr/>(com.nomagic.ci.persistence.IProject primaryProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPrimaryProject(com.nomagic.ci.persistence.IProject,boolean,boolean)">setPrimaryProject</a><wbr/>(com.nomagic.ci.persistence.IProject primaryProject,
 boolean closeOldProject,
 boolean changeModel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set primary project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRelocatingIn(boolean)">setRelocatingIn</a><wbr/>(boolean relocating)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set project state to relocating.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTitle(java.lang.String)">setTitle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sGetID()">sGetID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the actual ID of the <code>Element</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toDebugRepresentation()">toDebugRepresentation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns string representation of this element.</div>
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
<code><a href="../uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../uml/MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></h3>
<code><a href="../uml/MDElement.html#getProject()">getProject</a></code></div>
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
<li>
<section class="detail" id="MANY_CLASSES_UPDATED">
<h3>MANY_CLASSES_UPDATED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MANY_CLASSES_UPDATED</span></div>
<div class="block">Event type when many elements in project are changed (for example after project update,massive source reverse operation and etc)</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.Project.MANY_CLASSES_UPDATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FILE_NAME_PROPERTY">
<h3>FILE_NAME_PROPERTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FILE_NAME_PROPERTY</span></div>
<div class="block">Project file name property</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.Project.FILE_NAME_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIRTY_PROPERTY">
<h3>DIRTY_PROPERTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIRTY_PROPERTY</span></div>
<div class="block">Project "dirty" flag change</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.Project.DIRTY_PROPERTY">Constant Field Values</a></li>
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
<h3>Project</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Project</span>()</div>
<div class="block">Constructor creates project.</div>
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
<section class="detail" id="isCreateBrowser()">
<h3>isCreateBrowser</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCreateBrowser</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCreateBrowser(boolean)">
<h3>setCreateBrowser</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setCreateBrowser</span><wbr/><span class="parameters">(boolean createBrowser)</span></div>
</section>
</li>
<li>
<section class="detail" id="getElementsIDs(java.util.Collection)">
<h3>getElementsIDs</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getElementsIDs</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elements)</span></div>
<div class="block">Retrieves the elements ids from DTObjects collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - collection of elements to get ID's for</dd>
<dt>Returns:</dt>
<dd>the collection of elements ids from the DTObjects collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="executeIntensiveAction(java.lang.String)">
<h3>executeIntensiveAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">executeIntensiveAction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reason)</span></div>
<div class="block">Executes time-intensive action if user agrees to.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reason</code> - reason why the action might take a long time</dd>
<dt>Returns:</dt>
<dd>true if execute action</dd>
</dl>
</section>
</li>
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
<section class="detail" id="getDSL()">
<h3>getDSL</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.dsl.DSL</span> <span class="element-name">getDSL</span>()</div>
<div class="block">Returns project DSL service instance.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDSLManager()">
<h3>getDSLManager</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.dsl.DSLManager</span> <span class="element-name">getDSLManager</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getDSL()"><code>getDSL()</code></a></div>
</div>
<div class="block">Returns project customization manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the manager</dd>
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
<section class="detail" id="getCommandHistory()">
<h3>getCommandHistory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.commands.CommandHistory</span> <span class="element-name">getCommandHistory</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project command history.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementByIDQuerier()">
<h3>getElementByIDQuerier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.Project.ElementByIDFetcher</span> <span class="element-name">getElementByIDQuerier</span>()</div>
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
<section class="detail" id="getActiveAbstractDiagram()">
<h3>getActiveAbstractDiagram</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></span> <span class="element-name">getActiveAbstractDiagram</span>()</div>
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
<section class="detail" id="setModel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>setModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setModel</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> p)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTitle()">
<h3>getTitle</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTitle</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project title</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTitle(java.lang.String)">
<h3>setTitle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTitle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</span></div>
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
<section class="detail" id="getDirectory()">
<h3>getDirectory</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDirectory</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use #getFile.getParent</div>
</div>
<div class="block">Returns project directory.
 <p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project location directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDirectory(java.lang.String)">
<h3>setDirectory</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirectory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dir)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#setFileName(java.lang.String)"><code>setFileName(String)</code></a></div>
</div>
<div class="block">Sets the project directory.
 <p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dir</code> - the new project directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#setFileName(java.lang.String)"><code>setFileName(String)</code></a></div>
</div>
<div class="block">Sets the project name.
 <p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the new project name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFile()">
<h3>getFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.utils.ExtendedFile</span> <span class="element-name">getFile</span>()</div>
<div class="block">Method returns file of this project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>file of this project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFileName(java.lang.String)">
<h3>setFileName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFileName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</span></div>
<div class="block">Set the name of file as location of this project. Only local projects or locally saved remote projects can have file name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - absolute file path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCounter()">
<h3>getCounter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.MDCounter</span> <span class="element-name">getCounter</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>id counter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStyleManager()">
<h3>getStyleManager</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a></span> <span class="element-name">getStyleManager</span>()</div>
<div class="block">Returns style manager</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>style manager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectEditorWindowsManager()">
<h3>getProjectEditorWindowsManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.ProjectEditorWindowsManager</span> <span class="element-name">getProjectEditorWindowsManager</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>editor windows manager</dd>
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
<section class="detail" id="isUMLProject()">
<h3>isUMLProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUMLProject</span>()</div>
<div class="block">To check if project is for UML models.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if project is suitable for creating UML models</dd>
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
<section class="detail" id="setCounter(com.nomagic.magicdraw.core.MDCounter)">
<h3>setCounter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCounter</span><wbr/><span class="parameters">(com.nomagic.magicdraw.core.MDCounter c)</span></div>
<div class="block">Sets the counter for the project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>c</code> - the new counter;</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addElementByID(com.nomagic.magicdraw.uml.BaseElement,java.lang.String)">
<h3>addElementByID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addElementByID</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> oldID)</span></div>
<div class="block">Register the object by id.
 The record about this object and its old id is removed.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>addElementByID</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRegistry</code></dd>
<dt>Parameters:</dt>
<dd><code>obj</code> - the object to register.</dd>
<dd><code>oldID</code> - the old id of the object.</dd>
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
<section class="detail" id="removeElementByID(com.nomagic.magicdraw.uml.BaseElement)">
<h3>removeElementByID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeElementByID</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</span></div>
<div class="block">Unregister the object by id.
 The record about this object and is removed.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>removeElementByID</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRegistry</code></dd>
<dt>Parameters:</dt>
<dd><code>obj</code> - the object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addToQueryChangeRegistry(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>addToQueryChangeRegistry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addToQueryChangeRegistry</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeFromQueryChangeRegistry(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>removeFromQueryChangeRegistry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeFromQueryChangeRegistry</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement modelElement)</span></div>
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
<section class="detail" id="getPresentationElementByID(java.lang.String)">
<h3>getPresentationElementByID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getPresentationElementByID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementID)</span></div>
<div class="block">Return the presentation element with given id from currently registered elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementID</code> - the id of the element, cannot be null</dd>
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
<section class="detail" id="getElementsByIDs(java.util.Collection)">
<h3>getElementsByIDs</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getElementsByIDs</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids)</span></div>
<div class="block">Return the objects by given ids.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ids</code> - the collection of the ids of the objects.</dd>
<dt>Returns:</dt>
<dd>the collection of objects with given ids.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementsByIDs(java.util.Collection,java.util.function.Supplier)">
<h3>getElementsByIDs</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getElementsByIDs</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;&gt; collectionFactory)</span></div>
<div class="block">Return the objects by given ids.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ids</code> - the collection of the ids of the objects.</dd>
<dt>Returns:</dt>
<dd>the collection of objects with given ids.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllIDS()">
<h3>getAllIDS</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAllIDS</span>()</div>
<div class="block">Returns the collection of all ids in the project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the collection of all ids in the project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllElements()">
<h3>getAllElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getAllElements</span>()</div>
<div class="block">Gets collection of all model elements in the project</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getAllElements</code> in interface <code>com.nomagic.uml2.ext.jmi.reflect.ElementRegistry</code></dd>
<dt>Returns:</dt>
<dd>collection of elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isProjectClosed()">
<h3>isProjectClosed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isProjectClosed</span>()</div>
<div class="block">Checks if this project was already disposed(closed). Such project cannot be activated any more.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isProjectClosed</code> in interface <code>com.dassault_systemes.modeler.foundation.project.ModelElementProject</code></dd>
<dt>Returns:</dt>
<dd>true if project was disposed (closed)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isProjectDisposed()">
<h3>isProjectDisposed</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isProjectDisposed</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use #isProjectClosed</div>
</div>
<div class="block">Checks if this project was already disposed(closed). Such project cannot be activated any more.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if project was disposed (closed)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isClosing()">
<h3>isClosing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isClosing</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isClosing</code> in interface <code>com.dassault_systemes.modeler.foundation.project.ModelElementProject</code></dd>
<dt>Returns:</dt>
<dd>true if project is closing (preCloseFinal event is fired)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClosing(boolean)">
<h3>setClosing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setClosing</span><wbr/><span class="parameters">(boolean closing)</span></div>
<div class="block">Set closing project state</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>closing</code> - true if project is closing</dd>
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
<section class="detail" id="elementAdded(com.nomagic.magicdraw.uml.BaseElement)">
<h3>elementAdded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">elementAdded</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Marks element as added, if it was previously removed its id is removed from id collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element id which was added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="elementRemoved(com.nomagic.magicdraw.uml.BaseElement)">
<h3>elementRemoved</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">elementRemoved</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</span></div>
<div class="block">Marks element removed, its id added to mDeletedObjectIDS.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - element which was removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isElementInProject(java.lang.String)">
<h3>isElementInProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isElementInProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Check if element with a given id is in this project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - element id</dd>
<dt>Returns:</dt>
<dd>true if element with given id is registered in project and is not removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addWindow(com.nomagic.magicdraw.ui.ProjectWindow)">
<h3>addWindow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addWindow</span><wbr/><span class="parameters">(<a href="../ui/ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> window)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeWindow(com.nomagic.magicdraw.ui.ProjectWindow)">
<h3>removeWindow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeWindow</span><wbr/><span class="parameters">(<a href="../ui/ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> window)</span></div>
</section>
</li>
<li>
<section class="detail" id="getWindows()">
<h3>getWindows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../ui/ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a>&gt;</span> <span class="element-name">getWindows</span>()</div>
</section>
</li>
<li>
<section class="detail" id="hasWindow(java.lang.String)">
<h3>hasWindow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasWindow</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
</section>
</li>
<li>
<section class="detail" id="getWindow(java.lang.String)">
<h3>getWindow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ui/ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a></span> <span class="element-name">getWindow</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
</section>
</li>
<li>
<section class="detail" id="getStereotypesStyleChangeHandler()">
<h3>getStereotypesStyleChangeHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.StereotypesStyleChangeManager</span> <span class="element-name">getStereotypesStyleChangeHandler</span>()</div>
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
<section class="detail" id="resetDynamicRepository()">
<h3>resetDynamicRepository</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resetDynamicRepository</span>()</div>
<div class="block">Removes current dynamic repository if such exist and installs a new dynamic repository.</div>
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
<section class="detail" id="isModel(com.nomagic.magicdraw.uml.BaseElement)">
<h3>isModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isModel</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Checks if the given element is a one of the models in this project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check.</dd>
<dt>Returns:</dt>
<dd>true if given element is a one of the models in this project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isModel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>isModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isModel</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> element)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.uml2.project.ElementProject</code></span></div>
<div class="block">Checks if the given element is a one of the models in this project.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isModel</code> in interface <code>com.nomagic.uml2.project.ElementProject</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - element to check</dd>
<dt>Returns:</dt>
<dd>true if given package belongs to models of this project</dd>
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
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.uml2.project.ElementProject</code></span></div>
<div class="block">Returns a list of models in the project
 (the primary model of the project and all the models of the modules (attached projects)).</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getModels</code> in interface <code>com.nomagic.uml2.project.ElementProject</code></dd>
<dt>Returns:</dt>
<dd>models</dd>
</dl>
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
<section class="detail" id="getRemoteID()">
<h3>getRemoteID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRemoteID</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isLoaded()">
<h3>isLoaded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLoaded</span>()</div>
<div class="block">Return value of "loaded" flag</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this project was loaded from some location or is saved to some location (is not just created from template)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLoadedFrom()">
<h3>getLoadedFrom</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">getLoadedFrom</span>()</div>
<div class="block">Return location from were project was loaded.
 For Teamwork project returns local file if project was saved into file (or was loaded from file).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>location of project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLoaded(boolean)">
<h3>setLoaded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLoaded</span><wbr/><span class="parameters">(boolean loaded)</span></div>
<div class="block">Set "Loaded" flag for project. Project created from template is not "loaded"</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>loaded</code> - loaded flag</dd>
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
<div class="block">Returns Project for a given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - project element.</dd>
<dt>Returns:</dt>
<dd>project in which a given element exists.</dd>
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
<section class="detail" id="getExporterDescription()">
<h3>getExporterDescription</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a></span> <span class="element-name">getExporterDescription</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setExporterDescription(com.nomagic.persistence.XmiExporterDescription)">
<h3>setExporterDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExporterDescription</span><wbr/><span class="parameters">(<a href="../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a> exporterDescription)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTransactionsManager()">
<h3>getTransactionsManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/transaction/TransactionManager.html" title="interface in com.nomagic.uml2.transaction">TransactionManager</a></span> <span class="element-name">getTransactionsManager</span>()</div>
<div class="block">Return transaction manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>transaction manager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNeedLocallySave()">
<h3>isNeedLocallySave</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNeedLocallySave</span>()</div>
<div class="block">Teamwork projects after commit can be saved locally, using flag to hold state about teamwork
 projects were saved locally.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if project was not locally saved. Should be used only for teamwork projects.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNeedLocallySave(boolean)">
<h3>setNeedLocallySave</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNeedLocallySave</span><wbr/><span class="parameters">(boolean locallySaved)</span></div>
</section>
</li>
<li>
<section class="detail" id="setPrimaryProject(com.nomagic.ci.persistence.IProject)">
<h3>setPrimaryProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPrimaryProject</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject primaryProject)</span></div>
</section>
</li>
<li>
<section class="detail" id="setPrimaryProject(com.nomagic.ci.persistence.IProject,boolean,boolean)">
<h3>setPrimaryProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPrimaryProject</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject primaryProject,
 boolean closeOldProject,
 boolean changeModel)</span></div>
<div class="block">Set primary project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>primaryProject</code> - project to set.</dd>
<dd><code>closeOldProject</code> - close old project (do not close project when adding to teamwork).</dd>
<dd><code>changeModel</code> - dispose old model (do not dispose UML model when adding to teamwork)</dd>
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
<section class="detail" id="addFeature(java.lang.String)">
<h3>addFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addFeature</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> feature)</span></div>
<div class="block">Register a feature for a new project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - feature name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeFeature(java.lang.String)">
<h3>removeFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeFeature</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> feature)</span></div>
<div class="block">Unregister a feature for a new project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeatures()">
<h3>getFeatures</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getFeatures</span>()</div>
<div class="block">Return registered features for a new project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>registered features for a new project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUMLModelStorageFeature()">
<h3>getUMLModelStorageFeature</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.UMLModelProjectFeature</span> <span class="element-name">getUMLModelStorageFeature</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isNew()">
<h3>isNew</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNew</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if project is new and was never saved</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocationUri()">
<h3>getLocationUri</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.util.URI</span> <span class="element-name">getLocationUri</span>()</div>
<div class="block">Get URI location according the primary project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>URI.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFrozen()">
<h3>isFrozen</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFrozen</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if project is frozen</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFrozen(boolean)">
<h3>setFrozen</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFrozen</span><wbr/><span class="parameters">(boolean frozen)</span></div>
<div class="block">Set frozen flag. Frozen projects do not provide some data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>frozen</code> - frozen flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReady()">
<h3>isReady</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isReady</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if project is ready to use. It has primary project, it is not closed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRelocatedIn()">
<h3>isRelocatedIn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRelocatedIn</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if project is in relocating state</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRelocatingIn(boolean)">
<h3>setRelocatingIn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRelocatingIn</span><wbr/><span class="parameters">(boolean relocating)</span></div>
<div class="block">Set project state to relocating. Project is relocating if project content is coming from other project.
 This other project is in "relocated" state.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relocating</code> - relocating state</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refAddInstance(javax.jmi.reflect.RefBaseObject)">
<h3>refAddInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">refAddInstance</span><wbr/><span class="parameters">(javax.jmi.reflect.RefBaseObject instance)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refAddInstance</code> in interface <code>com.nomagic.uml2.ext.jmi.reflect.ElementRegistry</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refRemoveInstance(javax.jmi.reflect.RefBaseObject)">
<h3>refRemoveInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">refRemoveInstance</span><wbr/><span class="parameters">(javax.jmi.reflect.RefBaseObject instance)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refRemoveInstance</code> in interface <code>com.nomagic.uml2.ext.jmi.reflect.ElementRegistry</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refAllOfClasses(java.util.Set)">
<h3>refAllOfClasses</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;javax.jmi.reflect.RefBaseObject&gt;</span> <span class="element-name">refAllOfClasses</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass&gt; classes)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refAllOfClasses</code> in interface <code>com.nomagic.uml2.ext.jmi.reflect.ElementRegistry</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPreloadProject()">
<h3>isPreloadProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPreloadProject</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isPreloadProject</code> in interface <code>com.nomagic.uml2.ext.jmi.reflect.ElementRegistry</code></dd>
<dt>Specified by:</dt>
<dd><code>isPreloadProject</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRegistry</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBinaryStreamAtticCleaner()">
<h3>getBinaryStreamAtticCleaner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.BinaryStreamAtticCleaner</span> <span class="element-name">getBinaryStreamAtticCleaner</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getHasUnloadedManuallyReachableModules()">
<h3>getHasUnloadedManuallyReachableModules</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getHasUnloadedManuallyReachableModules</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the hasUnloadedManuallyReachableModules</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invalidateHasUnloadedManuallyReachableModules()">
<h3>invalidateHasUnloadedManuallyReachableModules</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">invalidateHasUnloadedManuallyReachableModules</span>()</div>
<div class="block">Invalidates the <a href="#getHasUnloadedManuallyReachableModules()"><code>getHasUnloadedManuallyReachableModules()</code></a> flag</div>
</section>
</li>
<li>
<section class="detail" id="toDebugRepresentation()">
<h3>toDebugRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toDebugRepresentation</span>()</div>
</section>
</li>
<li>
<section class="detail" id="register(java.lang.Class,T)">
<h3 id="register(java.lang.Class,java.lang.Object)">register</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">void</span> <span class="element-name">register</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type,
 T service)</span></div>
<div class="block">Registers the specified service.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - type of the service.</dd>
<dt>Parameters:</dt>
<dd><code>type</code> - service type.</dd>
<dd><code>service</code> - the service.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEMFProxiesSupported()">
<h3>isEMFProxiesSupported</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEMFProxiesSupported</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.uml2.ext.jmi.reflect.ElementRegistry</code></span></div>
<div class="block">Returns whether the registry supports EMF proxies.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isEMFProxiesSupported</code> in interface <code>com.nomagic.uml2.ext.jmi.reflect.ElementRegistry</code></dd>
<dt>Specified by:</dt>
<dd><code>isEMFProxiesSupported</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRegistry</code></dd>
<dt>Returns:</dt>
<dd>true if the element registry supports EMF proxies, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="generateID()">
<h3>generateID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">generateID</span>()</div>
<div class="block">Generate ID.</div>
</section>
</li>
<li>
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#getID()">BaseElement</a></code></span></div>
<div class="block">Returns the ID of the <code>Element</code>.
 If the ID is <code>null</code>, new id for an element is generated.
 Element id is persistence and does not change during project save/load.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#getID()">getID</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Returns:</dt>
<dd>the ID of the <code>Element</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sGetID()">
<h3>sGetID</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">sGetID</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#sGetID()">BaseElement</a></code></span></div>
<div class="block">Returns the actual ID of the <code>Element</code>. May return null if ID was not generated
 or set for this element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#sGetID()">sGetID</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Returns:</dt>
<dd>the ID of the <code>Element</code>.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../uml/BaseElement.html#getID()"><code>BaseElement.getID()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setID(java.lang.String)">
<h3>setID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#setID(java.lang.String)">BaseElement</a></code></span></div>
<div class="block">Sets the specified ID to the <code>Element</code>.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#setID(java.lang.String)">setID</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>id</code> - the id to be set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">clone</span>()
             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CloneNotSupportedException.html" title="class or interface in java.lang">CloneNotSupportedException</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#clone()">clone</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CloneNotSupportedException.html" title="class or interface in java.lang">CloneNotSupportedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>addPropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">BaseElement</a></code></span></div>
<div class="block">Registers the listener to the element. The given listener will get notifications about
 property changes in this element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - the <code>PropertyChangeListener</code> to be added.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasListeners()">
<h3>hasListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasListeners</span>()</div>
</section>
</li>
<li>
<section class="detail" id="removePropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>removePropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">BaseElement</a></code></span></div>
<div class="block">Unregisters the given listener from the element. The given listener will not get any notifications about
 property changes in this element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - the PropertyChangeListener to be removed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAllPropertyChangeListeners()">
<h3>removeAllPropertyChangeListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllPropertyChangeListeners</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#removeAllPropertyChangeListeners()">BaseElement</a></code></span></div>
<div class="block">Removes all property change listeners from this element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#removeAllPropertyChangeListeners()">removeAllPropertyChangeListeners</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">BaseElement</a></code></span></div>
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new values are equal or null.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>propertyName</code> - the programmatic name of the property that was changed.</dd>
<dd><code>oldValue</code> - the old value of the property</dd>
<dd><code>newValue</code> - the new value of the property</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="atInsert()">
<h3>atInsert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">atInsert</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#atInsert()">BaseElement</a></code></span></div>
<div class="block">This method is called then this element is added into the project.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#atInsert()">atInsert</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">Destroys the project. After this method call project can not be used any more.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#dispose()">dispose</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.Visitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../uml/Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">MDElement</a></code></span></div>
<div class="block">Method accepts a visitor, and calls method "visit&lt;class name&gt;(this)" of a visitor.
 See "Visitor" pattern for more details.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a></code> in interface <code><a href="../uml/MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.AbstractVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../uml/AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml">AbstractVisitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">BaseElement</a></code></span></div>
<div class="block">Method accepts a visitor, and calls method visit &lt; class name &gt; (this) of visitor.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
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
<li>
<section class="detail" id="getHumanName()">
<h3>getHumanName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHumanName</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#getHumanName()">BaseElement</a></code></span></div>
<div class="block">Returns human representation of the element. Usually human name is constructed from element class type
 and name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#getHumanName()">getHumanName</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Returns:</dt>
<dd>the human name of the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectImpl()">
<h3>getProjectImpl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProjectImpl</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/MDElement.html#getProjectImpl()">MDElement</a></code></span></div>
<div class="block">This method is deprecated and will be removed soon.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/MDElement.html#getProjectImpl()">getProjectImpl</a></code> in interface <code><a href="../uml/MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Returns:</dt>
<dd>project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSortKeys()">
<h3>getSortKeys</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">com.dassault_systemes.modeler.foundation.common.sort.SortKeys</span> <span class="element-name">getSortKeys</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/MDElement.html#getSortKeys()">MDElement</a></code></span></div>
<div class="block">Implementation of getSortKeys() from Sortable interface.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/MDElement.html#getSortKeys()">getSortKeys</a></code> in interface <code><a href="../uml/MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Returns:</dt>
<dd>the array of predefined sort keys.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHumanType()">
<h3>getHumanType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHumanType</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#getHumanType()">BaseElement</a></code></span></div>
<div class="block">Returns human representation of the element type. Contains only element type without element name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#getHumanType()">getHumanType</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Returns:</dt>
<dd>the human type of the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResourceID()">
<h3>getResourceID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getResourceID</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/MDElement.html#getResourceID()">getResourceID</a></code> in interface <code><a href="../uml/MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">
<h3>canAdd</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">canAdd</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean checkPermissions)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">BaseElement</a></code></span></div>
<div class="block">Checks if this element can add a given element.
 <br/>
 Following rules must be true to have result true:<br/>
 1.if checkTeamworkLock == true, this element must be locked for edit.<br/>
 2.element can add given element as instance (class types are checked).<br/>
 3.element can add given element as child (a given element is not a parent of current element etc.).<br/></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the element to add.</dd>
<dd><code>checkPermissions</code> - check or not permissions.</dd>
<dt>Returns:</dt>
<dd>true if an element can add the given element as a child.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canDeleteChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canDeleteChild</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> child)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">BaseElement</a></code></span></div>
<div class="block">Checks if given element can be deleted from this element.
 Following rules must be true to have result true:
 1.this element must be editable.
 2.project must be editable.
 3.the type of given child must be valid for teamwork lock for edit operation
 (for example, class, package etc., not Attribute).</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">canDeleteChild</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>child</code> - a given child</dd>
<dt>Returns:</dt>
<dd>true, if the given element can be deleted from the current element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeDeleted()">
<h3>canBeDeleted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canBeDeleted</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#canBeDeleted()">BaseElement</a></code></span></div>
<div class="block">Checks if an element can be deleted from a project.
 Element cannot be deleted if it is not isEditable(),
 parent is not set, or parent does not allow to remove this element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#canBeDeleted()">canBeDeleted</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Returns:</dt>
<dd>true, if an element can be deleted from a project.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../uml/BaseElement.html#isEditable()"><code>BaseElement.isEditable()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canAddInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAddInstance</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> o)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">BaseElement</a></code></span></div>
<div class="block">Checks if this object can add element of given type.
 Current implementation returns false.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if this object can elements of a given type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddChild(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canAddChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAddChild</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> o)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/MDElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a></code> in interface <code><a href="../uml/MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEditable()">
<h3>isEditable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEditable</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#isEditable()">BaseElement</a></code></span></div>
<div class="block">Checks if an element can be edited.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#isEditable()">isEditable</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Returns:</dt>
<dd>true, if an element can be edited.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddChild()">
<h3>canAddChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAddChild</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#canAddChild()">BaseElement</a></code></span></div>
<div class="block">Checks if new elements can be added to this element</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#canAddChild()">canAddChild</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Returns:</dt>
<dd>true, if new sub elements can be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectParent()">
<h3>getObjectParent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getObjectParent</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#getObjectParent()">BaseElement</a></code></span></div>
<div class="block">Returns the element parent.
 This implementation returns null. Should be overridden in subclasses.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#getObjectParent()">getObjectParent</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Returns:</dt>
<dd>the parent of the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareTo(java.lang.Object)">
<h3>compareTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">compareTo</span><wbr/><span class="parameters">(@Nonnull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<div class="block">Compares sort key at index 1 with given element's sort key at index 1.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code></dd>
<dt>Parameters:</dt>
<dd><code>o</code> - the given object to compare to.</dd>
<dt>Returns:</dt>
<dd>key's comparison result(String.compareTo()).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParentOf(com.nomagic.magicdraw.uml.BaseElement)">
<h3>isParentOf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isParentOf</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">BaseElement</a></code></span></div>
<div class="block">Returns true, if current element is parent of given element.
 Return false in this implementation.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>obj</code> - the given element(possible child).</dd>
<dt>Returns:</dt>
<dd>true if obj is the parent of this object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassType()">
<h3>getClassType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a></span> <span class="element-name">getClassType</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#getClassType()">BaseElement</a></code></span></div>
<div class="block">Gets the type of the element class.
 Every element has its own ClassType.
 Usually this class type is class of element or class interface of an element.
 All types are registered in ClassTypes.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#getClassType()">getClassType</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Returns:</dt>
<dd>the type of the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Returns string representation of this element.
 Useful for debugging purposes.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">
<h3>canChangeParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canChangeParent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> elements,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> newParent)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">BaseElement</a></code></span></div>
<div class="block">Returns true, if element can change parent.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a></code> in interface <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>elements</code> - collection of the elements, whose will change the parent together with this.</dd>
<dd><code>newParent</code> - new parent object.</dd>
<dt>Returns:</dt>
<dd>true if an element can change parent.</dd>
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
