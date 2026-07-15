# JAVA OPENAPI: SpecificationDialogManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/dialogs/specifications/SpecificationDialogManager.html
- source_path: `com/nomagic/magicdraw/ui/dialogs/specifications/SpecificationDialogManager.html`
- source_sha256: `008e1fd32d51ee717df266c1761786211b80775fc43e16257273fadec9596d14`
- captured_utc: `2026-07-14T16:55:52.508428+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dialogs.specifications](package-summary.html)

## Class SpecificationDialogManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter](../../../core/project/ProjectEventListenerAdapter.html)
com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager

All Implemented Interfaces:
`[ProjectEventListener](../../../core/project/ProjectEventListener.html)`

@OpenApipublic final classSpecificationDialogManager
extends [ProjectEventListenerAdapter](../../../core/project/ProjectEventListenerAdapter.html)

The manager of specification windows for all types of model elements.
 This manager knows exactly what specification dialog to open for every specific element.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addConfigurator](#addConfigurator(java.lang.Class,com.nomagic.magicdraw.ui.dialogs.specifications.configurator.ISpecificationNodeConfigurator))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> elementClass,
 [ISpecificationNodeConfigurator](configurator/ISpecificationNodeConfigurator.html) configurator)`
Adds specification node configurator for given Element type
`void`
`[addSpecificationGeneralComponentFactoryCreator](#addSpecificationGeneralComponentFactoryCreator(com.nomagic.magicdraw.ui.dialogs.specifications.panels.SpecificationGeneralComponentFactoryCreator))(com.nomagic.magicdraw.ui.dialogs.specifications.panels.SpecificationGeneralComponentFactoryCreator factoryCreator)`
Adds component factory creator
`void`
`[addValueOwnerEditor](#addValueOwnerEditor(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor))(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor editor)`

`void`
`[addValueOwnerEditorConfigurator](#addValueOwnerEditorConfigurator(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator))(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator configurator)`

`void`
`[closeDialog](#closeDialog(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog,com.nomagic.magicdraw.core.Project))(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog dialog,
 [Project](../../../core/Project.html) project)`

`void`
`[configure](#configure(com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.SpecificationNode,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))(com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.SpecificationNode node,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[disposeDialogs](#disposeDialogs(com.nomagic.magicdraw.core.Project))([Project](../../../core/Project.html) project)`
Closes all specification dialogs opened in particular project.
`void`
`[editSpecification](#editSpecification(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord))([SpecificationRecord](SpecificationRecord.html) record)`
Opens non-modal specification dialog activated pane specified by record.
`void`
`[editSpecification](#editSpecification(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord,boolean))([SpecificationRecord](SpecificationRecord.html) record,
 boolean modal)`
Opens specification dialog and activated pane specified by record.
`void`
`[editSpecification](#editSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Opens specification dialog for given ModelElement.
`void`
`[editSpecification](#editSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean modal)`
Opens specification dialog for given ModelElement.
`com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog`
`[getDialog](#getDialog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`static [SpecificationDialogManager](SpecificationDialogManager.html)`
`[getManager](#getManager())()`
Returns shared instance of this manager.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html),com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog>`
`[getProjectDialogs](#getProjectDialogs(com.nomagic.magicdraw.core.Project,boolean))([Project](../../../core/Project.html) project,
 boolean create)`

`com.nomagic.ui.SimpleBaseDialog`
`[getSimpleBaseDialog](#getSimpleBaseDialog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[SpecificationTitleCreator](SpecificationTitleCreator.html)`
`[getTitleCreator](#getTitleCreator())()`
Returns current specification dialog title creator.
`com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor`
`[getValueOwnerEditor](#getValueOwnerEditor(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerWrapper))(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerWrapper valueOwnerWrapper)`
Choose editor by 3 criteria: value, type, priority.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator>`
`[getValueOwnerEditorConfigurators](#getValueOwnerEditorConfigurators())()`

`void`
`[projectActivated](#projectActivated(com.nomagic.magicdraw.core.Project))([Project](../../../core/Project.html) project)`
Method is called when inactive project became active project.
`void`
`[projectDeActivated](#projectDeActivated(com.nomagic.magicdraw.core.Project))([Project](../../../core/Project.html) project)`
Method is called when active project becomes not active.
`void`
`[projectOpened](#projectOpened(com.nomagic.magicdraw.core.Project))([Project](../../../core/Project.html) project)`
Method is called when project was opened, created or loaded from teamwork server.
`void`
`[projectPreClosed](#projectPreClosed(com.nomagic.magicdraw.core.Project))([Project](../../../core/Project.html) project)`
Method is called before closing the project.
`[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<com.nomagic.magicdraw.ui.dialogs.specifications.panels.SpecificationGeneralComponentFactoryCreator>`
`[registeredSpecificationGeneralComponentFactoryCreators](#registeredSpecificationGeneralComponentFactoryCreators())()`
Returns iterator of registered specification general factory creators
`void`
`[removeConfigurator](#removeConfigurator(java.lang.Class,com.nomagic.magicdraw.ui.dialogs.specifications.configurator.ISpecificationNodeConfigurator))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> elementClass,
 [ISpecificationNodeConfigurator](configurator/ISpecificationNodeConfigurator.html) configurator)`
Removes specification dialog node configurator for given Element type.
`void`
`[removeValueOwnerEditor](#removeValueOwnerEditor(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor))(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor editor)`

`void`
`[removeValueOwnerEditorConfigurator](#removeValueOwnerEditorConfigurator(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator))(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator configurator)`

`void`
`[reuseDialog](#reuseDialog(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog dialog,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`static com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager.OpenMode`
`[setOpenModalMode](#setOpenModalMode(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager.OpenMode))(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager.OpenMode value)`

`void`
`[setTitleCreator](#setTitleCreator(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationTitleCreator))([SpecificationTitleCreator](SpecificationTitleCreator.html) titleCreator)`
Sets specification dialog title creator
`void`
`[updateDialogs](#updateDialogs())()`
Methods inherited from class com.nomagic.magicdraw.core.project.[ProjectEventListenerAdapter](../../../core/project/ProjectEventListenerAdapter.html)
`[projectActivatedFromGUI](../../../core/project/ProjectEventListenerAdapter.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)), [projectClosed](../../../core/project/ProjectEventListenerAdapter.html#projectClosed(com.nomagic.magicdraw.core.Project)), [projectCreated](../../../core/project/ProjectEventListenerAdapter.html#projectCreated(com.nomagic.magicdraw.core.Project)), [projectOpenedFromGUI](../../../core/project/ProjectEventListenerAdapter.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectPreActivated](../../../core/project/ProjectEventListenerAdapter.html#projectPreActivated(com.nomagic.magicdraw.core.Project)), [projectPreClosedFinal](../../../core/project/ProjectEventListenerAdapter.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)), [projectPreDeActivated](../../../core/project/ProjectEventListenerAdapter.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)), [projectPreSaved](../../../core/project/ProjectEventListenerAdapter.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)), [projectReplaced](../../../core/project/ProjectEventListenerAdapter.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)), [projectSaved](../../../core/project/ProjectEventListenerAdapter.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.core.project.[ProjectEventListener](../../../core/project/ProjectEventListener.html)
`[projectPreOpenedFromGUI](../../../core/project/ProjectEventListener.html#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectUsedFromGUI](../../../core/project/ProjectEventListener.html#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject))`

============ METHOD DETAIL ========== 
Method Details
setOpenModalMode
public static com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager.OpenMode setOpenModalMode(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager.OpenMode value)
getManager
@OpenApipublic static [SpecificationDialogManager](SpecificationDialogManager.html) getManager()
Returns shared instance of this manager.
Returns:
instance of this manager.
registeredSpecificationGeneralComponentFactoryCreators
public [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<com.nomagic.magicdraw.ui.dialogs.specifications.panels.SpecificationGeneralComponentFactoryCreator> registeredSpecificationGeneralComponentFactoryCreators()
Returns iterator of registered specification general factory creators
Returns:
iterator
addSpecificationGeneralComponentFactoryCreator
public void addSpecificationGeneralComponentFactoryCreator(com.nomagic.magicdraw.ui.dialogs.specifications.panels.SpecificationGeneralComponentFactoryCreator factoryCreator)
Adds component factory creator
Parameters:
`factoryCreator` - creator
editSpecification
@OpenApipublic void editSpecification([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Opens specification dialog for given ModelElement. Dialog is not modal.
Parameters:
`element` - the given Element.
editSpecification
@OpenApipublic void editSpecification([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean modal)
Opens specification dialog for given ModelElement.
Parameters:
`element` - the given Element.
`modal` - open modal specification window
editSpecification
@OpenApipublic void editSpecification([SpecificationRecord](SpecificationRecord.html) record)
Opens non-modal specification dialog activated pane specified by record.
Parameters:
`record` - specification dialog record containing a reference to element and pane to activate
editSpecification
@OpenApipublic void editSpecification([SpecificationRecord](SpecificationRecord.html) record,
 boolean modal)
Opens specification dialog and activated pane specified by record.
Parameters:
`record` - specification dialog record containing a reference to element and pane to activate
`modal` - open modal specification window
addValueOwnerEditor
public void addValueOwnerEditor(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor editor)
removeValueOwnerEditor
public void removeValueOwnerEditor(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor editor)
getValueOwnerEditor
@CheckForNullpublic com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor getValueOwnerEditor(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerWrapper valueOwnerWrapper)
Choose editor by 3 criteria: value, type, priority.
 Most important - value, least important priority.
Returns:
most suitable editor for given value owner
getProjectDialogs
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html),com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog> getProjectDialogs([Project](../../../core/Project.html) project,
 boolean create)
getDialog
@CheckForNullpublic com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog getDialog([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getSimpleBaseDialog
@CheckForNullpublic com.nomagic.ui.SimpleBaseDialog getSimpleBaseDialog([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
reuseDialog
public void reuseDialog(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog dialog,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
closeDialog
public void closeDialog(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog dialog,
 [Project](../../../core/Project.html) project)
addConfigurator
@OpenApipublic void addConfigurator([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> elementClass,
 [ISpecificationNodeConfigurator](configurator/ISpecificationNodeConfigurator.html) configurator)
Adds specification node configurator for given Element type
Parameters:
`elementClass` - the specific class of Element(for example com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)
`configurator` - the given configurator.
removeConfigurator
@OpenApipublic void removeConfigurator([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> elementClass,
 [ISpecificationNodeConfigurator](configurator/ISpecificationNodeConfigurator.html) configurator)
Removes specification dialog node configurator for given Element type.
Parameters:
`elementClass` - the specific class of Element(for example com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)
`configurator` - the given configurator.
configure
public void configure(com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.SpecificationNode node,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
disposeDialogs
public void disposeDialogs([Project](../../../core/Project.html) project)
Closes all specification dialogs opened in particular project.
 Method is used for performance testing purposes (SpecificationDialogPerformanceTest).
Parameters:
`project` - project
updateDialogs
public void updateDialogs()
getTitleCreator
@OpenApipublic [SpecificationTitleCreator](SpecificationTitleCreator.html) getTitleCreator()
Returns current specification dialog title creator.
Returns:
title creator
setTitleCreator
@OpenApipublic void setTitleCreator([SpecificationTitleCreator](SpecificationTitleCreator.html) titleCreator)
Sets specification dialog title creator
Parameters:
`titleCreator` - title creator.
projectOpened
public void projectOpened([Project](../../../core/Project.html) project)
Description copied from interface: `[ProjectEventListener](../../../core/project/ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project))`
Method is called when project was opened, created or loaded from teamwork server.
 Opened project is active project and no projectActivated(Project) is called for this project.
Specified by:
`[projectOpened](../../../core/project/ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](../../../core/project/ProjectEventListener.html)`
Overrides:
`[projectOpened](../../../core/project/ProjectEventListenerAdapter.html#projectOpened(com.nomagic.magicdraw.core.Project))` in class `[ProjectEventListenerAdapter](../../../core/project/ProjectEventListenerAdapter.html)`
Parameters:
`project` - project which was opened.
See Also:
[`ProjectEventListener.projectActivated(Project)`](../../../core/project/ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project))
projectPreClosed
public void projectPreClosed([Project](../../../core/Project.html) project)
Description copied from interface: `[ProjectEventListener](../../../core/project/ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project))`
Method is called before closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is not marked as "closing" in this step.
Specified by:
`[projectPreClosed](../../../core/project/ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](../../../core/project/ProjectEventListener.html)`
Overrides:
`[projectPreClosed](../../../core/project/ProjectEventListenerAdapter.html#projectPreClosed(com.nomagic.magicdraw.core.Project))` in class `[ProjectEventListenerAdapter](../../../core/project/ProjectEventListenerAdapter.html)`
Parameters:
`project` - project which will be closed.
See Also:
[`ProjectEventListener.projectPreClosed(com.nomagic.magicdraw.core.Project)`](../../../core/project/ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project))
projectActivated
public void projectActivated([Project](../../../core/Project.html) project)
Description copied from interface: `[ProjectEventListener](../../../core/project/ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project))`
Method is called when inactive project became active project.
Specified by:
`[projectActivated](../../../core/project/ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](../../../core/project/ProjectEventListener.html)`
Overrides:
`[projectActivated](../../../core/project/ProjectEventListenerAdapter.html#projectActivated(com.nomagic.magicdraw.core.Project))` in class `[ProjectEventListenerAdapter](../../../core/project/ProjectEventListenerAdapter.html)`
Parameters:
`project` - new active project.
See Also:
[`ProjectEventListener.projectActivated(Project)`](../../../core/project/ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project))
projectDeActivated
public void projectDeActivated([Project](../../../core/Project.html) project)
Description copied from interface: `[ProjectEventListener](../../../core/project/ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project))`
Method is called when active project becomes not active.
Specified by:
`[projectDeActivated](../../../core/project/ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](../../../core/project/ProjectEventListener.html)`
Overrides:
`[projectDeActivated](../../../core/project/ProjectEventListenerAdapter.html#projectDeActivated(com.nomagic.magicdraw.core.Project))` in class `[ProjectEventListenerAdapter](../../../core/project/ProjectEventListenerAdapter.html)`
Parameters:
`project` - inactive project.
See Also:
[`ProjectEventListener.projectDeActivated(Project)`](../../../core/project/ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project))
getValueOwnerEditorConfigurators
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator> getValueOwnerEditorConfigurators()
addValueOwnerEditorConfigurator
public void addValueOwnerEditorConfigurator(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator configurator)
removeValueOwnerEditorConfigurator
public void removeValueOwnerEditorConfigurator(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator configurator)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dialogs.specifications</a></div>
<h1 class="title" title="Class SpecificationDialogManager">Class SpecificationDialogManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../../core/project/ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../core/project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">SpecificationDialogManager</span>
<span class="extends-implements">extends <a href="../../../core/project/ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter</a></span></div>
<div class="block">The manager of specification windows for all types of model elements.
 This manager knows exactly what specification dialog to open for every specific element.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addConfigurator(java.lang.Class,com.nomagic.magicdraw.ui.dialogs.specifications.configurator.ISpecificationNodeConfigurator)">addConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; elementClass,
 <a href="configurator/ISpecificationNodeConfigurator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.configurator">ISpecificationNodeConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds specification node configurator for given Element type</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSpecificationGeneralComponentFactoryCreator(com.nomagic.magicdraw.ui.dialogs.specifications.panels.SpecificationGeneralComponentFactoryCreator)">addSpecificationGeneralComponentFactoryCreator</a><wbr/>(com.nomagic.magicdraw.ui.dialogs.specifications.panels.SpecificationGeneralComponentFactoryCreator factoryCreator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds component factory creator</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addValueOwnerEditor(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor)">addValueOwnerEditor</a><wbr/>(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor editor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addValueOwnerEditorConfigurator(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator)">addValueOwnerEditorConfigurator</a><wbr/>(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeDialog(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog,com.nomagic.magicdraw.core.Project)">closeDialog</a><wbr/>(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog dialog,
 <a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#configure(com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.SpecificationNode,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">configure</a><wbr/>(com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.SpecificationNode node,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#disposeDialogs(com.nomagic.magicdraw.core.Project)">disposeDialogs</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Closes all specification dialogs opened in particular project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editSpecification(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord)">editSpecification</a><wbr/>(<a href="SpecificationRecord.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationRecord</a> record)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens non-modal specification dialog activated pane specified by record.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editSpecification(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord,boolean)">editSpecification</a><wbr/>(<a href="SpecificationRecord.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationRecord</a> record,
 boolean modal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens specification dialog and activated pane specified by record.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">editSpecification</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens specification dialog for given ModelElement.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">editSpecification</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean modal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens specification dialog for given ModelElement.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDialog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getDialog</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SpecificationDialogManager.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationDialogManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getManager()">getManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of this manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>,<wbr/>com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectDialogs(com.nomagic.magicdraw.core.Project,boolean)">getProjectDialogs</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean create)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ui.SimpleBaseDialog</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSimpleBaseDialog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getSimpleBaseDialog</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SpecificationTitleCreator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationTitleCreator</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTitleCreator()">getTitleCreator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns current specification dialog title creator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueOwnerEditor(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerWrapper)">getValueOwnerEditor</a><wbr/>(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerWrapper valueOwnerWrapper)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Choose editor by 3 criteria: value, type, priority.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueOwnerEditorConfigurators()">getValueOwnerEditorConfigurators</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectActivated(com.nomagic.magicdraw.core.Project)">projectActivated</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called when inactive project became active project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectDeActivated(com.nomagic.magicdraw.core.Project)">projectDeActivated</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called when active project becomes not active.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectOpened(com.nomagic.magicdraw.core.Project)">projectOpened</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called when project was opened, created or loaded from teamwork server.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectPreClosed(com.nomagic.magicdraw.core.Project)">projectPreClosed</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called before closing the project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;com.nomagic.magicdraw.ui.dialogs.specifications.panels.SpecificationGeneralComponentFactoryCreator&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registeredSpecificationGeneralComponentFactoryCreators()">registeredSpecificationGeneralComponentFactoryCreators</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns iterator of registered specification general factory creators</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeConfigurator(java.lang.Class,com.nomagic.magicdraw.ui.dialogs.specifications.configurator.ISpecificationNodeConfigurator)">removeConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; elementClass,
 <a href="configurator/ISpecificationNodeConfigurator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.configurator">ISpecificationNodeConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes specification dialog node configurator for given Element type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeValueOwnerEditor(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor)">removeValueOwnerEditor</a><wbr/>(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor editor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeValueOwnerEditorConfigurator(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator)">removeValueOwnerEditorConfigurator</a><wbr/>(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reuseDialog(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">reuseDialog</a><wbr/>(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog dialog,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager.OpenMode</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setOpenModalMode(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager.OpenMode)">setOpenModalMode</a><wbr/>(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager.OpenMode value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTitleCreator(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationTitleCreator)">setTitleCreator</a><wbr/>(<a href="SpecificationTitleCreator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationTitleCreator</a> titleCreator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets specification dialog title creator</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateDialogs()">updateDialogs</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter">Methods inherited from class com.nomagic.magicdraw.core.project.<a href="../../../core/project/ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter</a></h3>
<code><a href="../../../core/project/ProjectEventListenerAdapter.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">projectActivatedFromGUI</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectClosed(com.nomagic.magicdraw.core.Project)">projectClosed</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectCreated(com.nomagic.magicdraw.core.Project)">projectCreated</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectOpenedFromGUI</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectPreActivated(com.nomagic.magicdraw.core.Project)">projectPreActivated</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)">projectPreClosedFinal</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)">projectPreDeActivated</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">projectPreSaved</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">projectReplaced</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)">projectSaved</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.project.ProjectEventListener">Methods inherited from interface com.nomagic.magicdraw.core.project.<a href="../../../core/project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></h3>
<code><a href="../../../core/project/ProjectEventListener.html#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectPreOpenedFromGUI</a>, <a href="../../../core/project/ProjectEventListener.html#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject)">projectUsedFromGUI</a></code></div>
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
<section class="detail" id="setOpenModalMode(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager.OpenMode)">
<h3>setOpenModalMode</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager.OpenMode</span> <span class="element-name">setOpenModalMode</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager.OpenMode value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getManager()">
<h3>getManager</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="SpecificationDialogManager.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationDialogManager</a></span> <span class="element-name">getManager</span>()</div>
<div class="block">Returns shared instance of this manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instance of this manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registeredSpecificationGeneralComponentFactoryCreators()">
<h3>registeredSpecificationGeneralComponentFactoryCreators</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;com.nomagic.magicdraw.ui.dialogs.specifications.panels.SpecificationGeneralComponentFactoryCreator&gt;</span> <span class="element-name">registeredSpecificationGeneralComponentFactoryCreators</span>()</div>
<div class="block">Returns iterator of registered specification general factory creators</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSpecificationGeneralComponentFactoryCreator(com.nomagic.magicdraw.ui.dialogs.specifications.panels.SpecificationGeneralComponentFactoryCreator)">
<h3>addSpecificationGeneralComponentFactoryCreator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSpecificationGeneralComponentFactoryCreator</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.dialogs.specifications.panels.SpecificationGeneralComponentFactoryCreator factoryCreator)</span></div>
<div class="block">Adds component factory creator</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factoryCreator</code> - creator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="editSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>editSpecification</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">editSpecification</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Opens specification dialog for given ModelElement. Dialog is not modal.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="editSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>editSpecification</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">editSpecification</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean modal)</span></div>
<div class="block">Opens specification dialog for given ModelElement.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given Element.</dd>
<dd><code>modal</code> - open modal specification window</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="editSpecification(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord)">
<h3>editSpecification</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">editSpecification</span><wbr/><span class="parameters">(<a href="SpecificationRecord.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationRecord</a> record)</span></div>
<div class="block">Opens non-modal specification dialog activated pane specified by record.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>record</code> - specification dialog record containing a reference to element and pane to activate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="editSpecification(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord,boolean)">
<h3>editSpecification</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">editSpecification</span><wbr/><span class="parameters">(<a href="SpecificationRecord.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationRecord</a> record,
 boolean modal)</span></div>
<div class="block">Opens specification dialog and activated pane specified by record.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>record</code> - specification dialog record containing a reference to element and pane to activate</dd>
<dd><code>modal</code> - open modal specification window</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addValueOwnerEditor(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor)">
<h3>addValueOwnerEditor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addValueOwnerEditor</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor editor)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeValueOwnerEditor(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor)">
<h3>removeValueOwnerEditor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeValueOwnerEditor</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor editor)</span></div>
</section>
</li>
<li>
<section class="detail" id="getValueOwnerEditor(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerWrapper)">
<h3>getValueOwnerEditor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditor</span> <span class="element-name">getValueOwnerEditor</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerWrapper valueOwnerWrapper)</span></div>
<div class="block">Choose editor by 3 criteria: value, type, priority.
 Most important - value, least important priority.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>most suitable editor for given value owner</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectDialogs(com.nomagic.magicdraw.core.Project,boolean)">
<h3>getProjectDialogs</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>,<wbr/>com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog&gt;</span> <span class="element-name">getProjectDialogs</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean create)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDialog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getDialog</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog</span> <span class="element-name">getDialog</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSimpleBaseDialog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getSimpleBaseDialog</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.ui.SimpleBaseDialog</span> <span class="element-name">getSimpleBaseDialog</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="reuseDialog(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>reuseDialog</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reuseDialog</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog dialog,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="closeDialog(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog,com.nomagic.magicdraw.core.Project)">
<h3>closeDialog</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">closeDialog</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialog dialog,
 <a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
</section>
</li>
<li>
<section class="detail" id="addConfigurator(java.lang.Class,com.nomagic.magicdraw.ui.dialogs.specifications.configurator.ISpecificationNodeConfigurator)">
<h3>addConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; elementClass,
 <a href="configurator/ISpecificationNodeConfigurator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.configurator">ISpecificationNodeConfigurator</a> configurator)</span></div>
<div class="block">Adds specification node configurator for given Element type</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementClass</code> - the specific class of Element(for example com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)</dd>
<dd><code>configurator</code> - the given configurator.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeConfigurator(java.lang.Class,com.nomagic.magicdraw.ui.dialogs.specifications.configurator.ISpecificationNodeConfigurator)">
<h3>removeConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; elementClass,
 <a href="configurator/ISpecificationNodeConfigurator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.configurator">ISpecificationNodeConfigurator</a> configurator)</span></div>
<div class="block">Removes specification dialog node configurator for given Element type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementClass</code> - the specific class of Element(for example com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)</dd>
<dd><code>configurator</code> - the given configurator.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="configure(com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.SpecificationNode,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>configure</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">configure</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.SpecificationNode node,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="disposeDialogs(com.nomagic.magicdraw.core.Project)">
<h3>disposeDialogs</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disposeDialogs</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Closes all specification dialogs opened in particular project.
 Method is used for performance testing purposes (SpecificationDialogPerformanceTest).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateDialogs()">
<h3>updateDialogs</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateDialogs</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTitleCreator()">
<h3>getTitleCreator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="SpecificationTitleCreator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationTitleCreator</a></span> <span class="element-name">getTitleCreator</span>()</div>
<div class="block">Returns current specification dialog title creator.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>title creator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTitleCreator(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationTitleCreator)">
<h3>setTitleCreator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTitleCreator</span><wbr/><span class="parameters">(<a href="SpecificationTitleCreator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationTitleCreator</a> titleCreator)</span></div>
<div class="block">Sets specification dialog title creator</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>titleCreator</code> - title creator.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectOpened(com.nomagic.magicdraw.core.Project)">
<h3>projectOpened</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectOpened</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../../core/project/ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called when project was opened, created or loaded from teamwork server.
 Opened project is active project and no projectActivated(Project) is called for this project.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../core/project/ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project)">projectOpened</a></code> in interface <code><a href="../../../core/project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../../../core/project/ProjectEventListenerAdapter.html#projectOpened(com.nomagic.magicdraw.core.Project)">projectOpened</a></code> in class <code><a href="../../../core/project/ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project which was opened.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../core/project/ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectActivated(Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPreClosed(com.nomagic.magicdraw.core.Project)">
<h3>projectPreClosed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectPreClosed</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../../core/project/ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called before closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is not marked as "closing" in this step.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../core/project/ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project)">projectPreClosed</a></code> in interface <code><a href="../../../core/project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../../../core/project/ProjectEventListenerAdapter.html#projectPreClosed(com.nomagic.magicdraw.core.Project)">projectPreClosed</a></code> in class <code><a href="../../../core/project/ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project which will be closed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../core/project/ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectPreClosed(com.nomagic.magicdraw.core.Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectActivated(com.nomagic.magicdraw.core.Project)">
<h3>projectActivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectActivated</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../../core/project/ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called when inactive project became active project.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../core/project/ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)">projectActivated</a></code> in interface <code><a href="../../../core/project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../../../core/project/ProjectEventListenerAdapter.html#projectActivated(com.nomagic.magicdraw.core.Project)">projectActivated</a></code> in class <code><a href="../../../core/project/ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - new active project.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../core/project/ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectActivated(Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectDeActivated(com.nomagic.magicdraw.core.Project)">
<h3>projectDeActivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectDeActivated</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../../core/project/ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called when active project becomes not active.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../core/project/ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project)">projectDeActivated</a></code> in interface <code><a href="../../../core/project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../../../core/project/ProjectEventListenerAdapter.html#projectDeActivated(com.nomagic.magicdraw.core.Project)">projectDeActivated</a></code> in class <code><a href="../../../core/project/ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - inactive project.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../core/project/ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectDeActivated(Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueOwnerEditorConfigurators()">
<h3>getValueOwnerEditorConfigurators</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator&gt;</span> <span class="element-name">getValueOwnerEditorConfigurators</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addValueOwnerEditorConfigurator(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator)">
<h3>addValueOwnerEditorConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addValueOwnerEditorConfigurator</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator configurator)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeValueOwnerEditorConfigurator(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator)">
<h3>removeValueOwnerEditorConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeValueOwnerEditorConfigurator</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.dialogs.specifications.panels.slots.ValueOwnerEditorConfigurator configurator)</span></div>
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
