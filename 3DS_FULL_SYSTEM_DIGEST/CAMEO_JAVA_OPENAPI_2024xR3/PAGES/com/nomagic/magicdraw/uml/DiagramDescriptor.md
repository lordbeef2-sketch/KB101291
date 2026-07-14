# JAVA OPENAPI: DiagramDescriptor (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/DiagramDescriptor.html
- source_path: `com/nomagic/magicdraw/uml/DiagramDescriptor.html`
- source_sha256: `3969816aa740d68bacf1947b9f1dd078a4ddbdcd995a21c2c3934e8e1290257e`
- captured_utc: `2026-07-14T16:55:54.675450+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class DiagramDescriptor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.DiagramDescriptor

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[NonSymbolDiagramDescriptor](diagrams/NonSymbolDiagramDescriptor.html)`

@OpenApipublic abstract classDiagramDescriptor
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)

Descriptor of some extended diagram. 

 This descriptor is used to define a new diagram type in the MagicDraw application. New diagram type be extended
 from some already existing type. New diagram will have separate diagram panel with its own toolbar.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramDescriptor](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`protected [DiagramDescriptor](DiagramDescriptor.html)`
`[clone](#clone())()`

`void`
`[configureNewDiagram](#configureNewDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) parent)`
Configure new created diagram
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getAbbreviation](#getAbbreviation())()`

`com.nomagic.ui.banners.Banner`
`[getBanner](#getBanner())()`
Gets banner for this diagram descriptor.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getCategory](#getCategory())()`
Diagram category name.
`[MDActionsManager](../actions/MDActionsManager.html)`
`[getDiagramActions](#getDiagramActions())()`
Returns manager of actions used in the diagram.
`abstract [DiagramContextAMConfigurator](../actions/DiagramContextAMConfigurator.html)`
`[getDiagramContextConfigurator](#getDiagramContextConfigurator())()`

`abstract [AMConfigurator](../../actions/AMConfigurator.html)`
`[getDiagramShortcutsConfigurator](#getDiagramShortcutsConfigurator())()`

`abstract [AMConfigurator](../../actions/AMConfigurator.html)`
`[getDiagramToolbarConfigurator](#getDiagramToolbarConfigurator())()`

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramTypeId](#getDiagramTypeId())()`
Return diagram type id.
`com.nomagic.magicdraw.uml.DiagramDescriptor.DiagramWrapper`
`[getDiagramWrapper](#getDiagramWrapper())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHelpID](#getHelpID())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getKind](#getKind())()`
Returns a diagram kind used for grouping diagrams by their nature - symbolic diagram, table and so on.
`[AMConfigurator](../../actions/AMConfigurator.html)`
`[getMainMenuConfigurator](#getMainMenuConfigurator())()`

`[AMConfigurator](../../actions/AMConfigurator.html)`
`[getMainToolbarConfigurator](#getMainToolbarConfigurator())()`

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPluralDiagramTypeHumanName](#getPluralDiagramTypeHumanName())()`
Return diagram human name.
`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?>`
`[getProfiles](#getProfiles())()`
Returns path for profile of this diagram.
`com.nomagic.magicdraw.uml.symbols.RequiredFeature`
`[getRequiredFeature](#getRequiredFeature())()`
Gets required feature by this diagram descriptor.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.core.Feature>`
`[getRequiredFeatures](#getRequiredFeatures())()`
Gets required features which are needed by this diagram descriptor.
`final com.nomagic.magicdraw.plugins.RequiredPluginInfo`
`[getRequiredPlugin](#getRequiredPlugin())()`
Required plugin for this diagram
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getResourceProviderID](#getResourceProviderID())()`

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSingularDiagramTypeHumanName](#getSingularDiagramTypeHumanName())()`
Return diagram human name.
`[ResizableIcon](../../ui/ResizableIcon.html)`
`[getSmallIcon](#getSmallIcon())()`
If descriptor provides icon URL, this method should not be overridden.
`abstract [URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html)`
`[getSmallIconURL](#getSmallIconURL())()`
URL of small icon for diagram.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getSmartManipulatorsActions](#getSmartManipulatorsActions(boolean))(boolean superType)`

`com.nomagic.magicdraw.actions.SmartManipulatorsAMConfigurator`
`[getSmartManipulatorsConfigurator](#getSmartManipulatorsConfigurator())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getStereotypes](#getStereotypes(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSuperType](#getSuperType())()`
Returns super type of this diagram.
`abstract [ResizableIcon](../../ui/ResizableIcon.html)`
`[getSVGIcon](#getSVGIcon())()`
Resizable icon for diagram.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getTargetsManipulatorsActions](#getTargetsManipulatorsActions(boolean))(boolean superType)`

`[TargetElementAMConfigurator](../actions/TargetElementAMConfigurator.html)`
`[getTargetsManipulatorsConfigurator](#getTargetsManipulatorsConfigurator())()`

`boolean`
`[hasContent](#hasContent())()`
Does diagram has content.
`boolean`
`[importProfile](#importProfile(com.nomagic.magicdraw.core.Project,boolean))([Project](../core/Project.html) project,
 boolean ui)`
Import profile for this diagram into a given project.
`abstract boolean`
`[isCreatable](#isCreatable())()`
Returns creatable flag.
`boolean`
`[isProfileLoaded](#isProfileLoaded(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`

`boolean`
`[isSupported](#isSupported())()`
Indicates if all necessary prerequisites are available to support this type of diagram.
`static boolean`
`[isSupported](#isSupported(com.nomagic.magicdraw.uml.DiagramDescriptor))([DiagramDescriptor](DiagramDescriptor.html) diagramDescriptor)`

`boolean`
`[isUsedForSymbols](#isUsedForSymbols())()`
Check if this diagram is used to draw symbols.
`protected boolean`
`[profileLoaded](#profileLoaded(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Checks if UML Profile for this diagram already loaded in the model.
`void`
`[setBanner](#setBanner(com.nomagic.ui.banners.Banner))(com.nomagic.ui.banners.Banner banner)`
Sets banner for this diagram descriptor.
`void`
`[setCategory](#setCategory(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) category)`
Set diagram category name.
`void`
`[setHelpID](#setHelpID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)`

`void`
`[setRequiredFeatures](#setRequiredFeatures(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.core.Feature> requiredFeatures)`
Sets required features which are needed by this diagram descriptor.
`void`
`[setRequiredPlugin](#setRequiredPlugin(com.nomagic.magicdraw.plugins.RequiredPluginInfo))(com.nomagic.magicdraw.plugins.RequiredPluginInfo plugin)`
Sets required plugin for this diagram.
`void`
`[setResourceProviderID](#setResourceProviderID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourceProviderID)`
Usual diagrams should provide resource provider id, in other case buttons groups and descriptions will be not translatable.
`protected void`
`[setSmallIcon](#setSmallIcon(com.nomagic.ui.ResizableIcon))([ResizableIcon](../../ui/ResizableIcon.html) icon)`

`boolean`
`[storeDiagramProperties](#storeDiagramProperties())()`
Checks if diagram properties for this diagram should be stored.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramDescriptor
public DiagramDescriptor()
 ============ METHOD DETAIL ========== 
Method Details
getSuperType
@OpenApipublic abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSuperType()
Returns super type of this diagram.
Returns:
String the 'super diagram' type of the diagram type.
 E.g. `Interaction Diagram` is a 'super diagram' for `Collaboration Diagram` and
 `Sequence Diagram`.
isCreatable
@OpenApipublic abstract boolean isCreatable()
Returns creatable flag.
Returns:
boolean flag indicating if the diagram will be creatable.
isUsedForSymbols
@OpenApipublic boolean isUsedForSymbols()
Check if this diagram is used to draw symbols. Some diagram may be used to display tables,
 graphs or other components (for example dependency matrix table)
Returns:
true if diagram is used to draw symbols
storeDiagramProperties
public boolean storeDiagramProperties()
Checks if diagram properties for this diagram should be stored.
Returns:
true if diagram properties for this diagram should be stored.
getDiagramToolbarConfigurator
@CheckForNull
@OpenApipublic abstract [AMConfigurator](../../actions/AMConfigurator.html) getDiagramToolbarConfigurator()
Returns:
AMConfigurator which configures described diagram toolbar.
getDiagramShortcutsConfigurator
@CheckForNull
@OpenApipublic abstract [AMConfigurator](../../actions/AMConfigurator.html) getDiagramShortcutsConfigurator()
Returns:
AMConfigurator which configures described diagram shortcuts.
getDiagramContextConfigurator
@CheckForNull
@OpenApipublic abstract [DiagramContextAMConfigurator](../actions/DiagramContextAMConfigurator.html) getDiagramContextConfigurator()
Returns:
AMConfigurator which configures described diagram context menu actions.
getDiagramTypeId
@OpenApipublic abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramTypeId()
Return diagram type id. It is used to identify the diagram.
Returns:
String used to identify diagram type.
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)
getAbbreviation
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAbbreviation()
Returns:
the abbreviation
getSingularDiagramTypeHumanName
@OpenApipublic abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSingularDiagramTypeHumanName()
Return diagram human name. It is used to show the diagram type in the UI.
Returns:
human diagram name in singular.
getPluralDiagramTypeHumanName
@OpenApipublic abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPluralDiagramTypeHumanName()
Return diagram human name. It is used to show the diagram type in the UI.
Returns:
human diagram name in plural.
getSVGIcon
@CheckForNull
@OpenApipublic abstract [ResizableIcon](../../ui/ResizableIcon.html) getSVGIcon()
Resizable icon for diagram. svg and wmf format. Used in Content diagram.
Returns:
resizable icon in svg or wmf formats.
getSmallIconURL
@CheckForNull
@OpenApipublic abstract [URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html) getSmallIconURL()
URL of small icon for diagram. Used in browser and menu.
Returns:
URL to icon shown diagram in browser and menu items.
getResourceProviderID
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getResourceProviderID()
Returns:
resource provider id which is used to translate text read from descriptor file. May be null.
setResourceProviderID
public void setResourceProviderID(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourceProviderID)
Usual diagrams should provide resource provider id, in other case buttons groups and descriptions will be not translatable.
Parameters:
`resourceProviderID` - provider id which is used to translate text read from descriptor file. May be null.
getHelpID
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHelpID()
Returns:
online help page name
setHelpID
public void setHelpID(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)
Parameters:
`helpID` - new online page name
setSmallIcon
protected void setSmallIcon(@CheckForNull
 [ResizableIcon](../../ui/ResizableIcon.html) icon)
getSmallIcon
@CheckForNullpublic [ResizableIcon](../../ui/ResizableIcon.html) getSmallIcon()
If descriptor provides icon URL, this method should not be overridden.
Returns:
icon
getMainMenuConfigurator
@CheckForNullpublic [AMConfigurator](../../actions/AMConfigurator.html) getMainMenuConfigurator()
Returns:
AMConfigurator which configures main menu for adding this diagram specific actions.
getMainToolbarConfigurator
@CheckForNullpublic [AMConfigurator](../../actions/AMConfigurator.html) getMainToolbarConfigurator()
Returns:
AMConfigurator which configures main toolbar for adding this diagram specific actions.
profileLoaded
protected boolean profileLoaded([Project](../core/Project.html) project)
Checks if UML Profile for this diagram already loaded in the model.
Parameters:
`project` - project
Returns:
true, if profile already loaded. Here returns true.
isProfileLoaded
public boolean isProfileLoaded([Project](../core/Project.html) project)
Parameters:
`project` - project
Returns:
true if required profile is loaded.
getProfiles
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> getProfiles()
Returns path for profile of this diagram. If path is not null, profile will be loaded during diagram creation.
Returns:
some path to xml file of profile or null if profile does not exist for this type of the diagram.
getDiagramWrapper
public com.nomagic.magicdraw.uml.DiagramDescriptor.DiagramWrapper getDiagramWrapper()
importProfile
public boolean importProfile([Project](../core/Project.html) project,
 boolean ui)
Import profile for this diagram into a given project.
Parameters:
`project` - project
`ui` - show ui messages in case of some problems
Returns:
true if required profiles are attached to project
getDiagramActions
@OpenApi
@CheckForNullpublic [MDActionsManager](../actions/MDActionsManager.html) getDiagramActions()
Returns manager of actions used in the diagram.
 Later these actions must be configured for toolbar or shortcuts.
 Only one instance of action must be used in the configurators. If this rule is not applied, some problems may
 occur(for example changed by user keyboard shortcuts for action may not be saved).
Returns:
manager of actions.
clone
protected [DiagramDescriptor](DiagramDescriptor.html) clone()
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
getStereotypes
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getStereotypes([Project](../core/Project.html) project)
Parameters:
`project` - project
Returns:
list of stereotypes ids, these stereotypes will be assigned to the diagram element.
getSmartManipulatorsConfigurator
@CheckForNullpublic com.nomagic.magicdraw.actions.SmartManipulatorsAMConfigurator getSmartManipulatorsConfigurator()
getTargetsManipulatorsConfigurator
@CheckForNullpublic [TargetElementAMConfigurator](../actions/TargetElementAMConfigurator.html) getTargetsManipulatorsConfigurator()
getSmartManipulatorsActions
public [ActionsManager](../../actions/ActionsManager.html) getSmartManipulatorsActions(boolean superType)
getTargetsManipulatorsActions
public [ActionsManager](../../actions/ActionsManager.html) getTargetsManipulatorsActions(boolean superType)
getRequiredPlugin
@CheckForNullpublic final com.nomagic.magicdraw.plugins.RequiredPluginInfo getRequiredPlugin()
Required plugin for this diagram
Returns:
required plugin for this diagram. If plugin is not available diagram will be not loaded. If returns null no plugin is required.
setRequiredPlugin
public void setRequiredPlugin(@CheckForNull
 com.nomagic.magicdraw.plugins.RequiredPluginInfo plugin)
Sets required plugin for this diagram.
 If required plugin is not available diagram should not be loaded.
Parameters:
`plugin` - new required feature. Can be null.
getRequiredFeatures
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.core.Feature> getRequiredFeatures()
Gets required features which are needed by this diagram descriptor.
Returns:
required features which are needed by this diagram descriptor.
setRequiredFeatures
public void setRequiredFeatures([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.core.Feature> requiredFeatures)
Sets required features which are needed by this diagram descriptor.
Parameters:
`requiredFeatures` - required features which are needed by this diagram descriptor.
isSupported
public boolean isSupported()
Indicates if all necessary prerequisites are available to support this type of diagram.
 It can be required plugin or required feature.
Returns:
true if diagram is supported, false otherwise.
isSupported
public static boolean isSupported(@CheckForNull
 [DiagramDescriptor](DiagramDescriptor.html) diagramDescriptor)
getCategory
@CheckForNull
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getCategory()
Diagram category name.
Returns:
diagram category
getKind
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getKind()
Returns a diagram kind used for grouping diagrams by their nature - symbolic diagram, table and so on.
Returns:
diagram kind
setCategory
@OpenApipublic void setCategory(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) category)
Set diagram category name.
Parameters:
`category` - category diagram category name
getRequiredFeature
@CheckForNullpublic com.nomagic.magicdraw.uml.symbols.RequiredFeature getRequiredFeature()
Gets required feature by this diagram descriptor.
Returns:
required feature by this diagram descriptor.
getBanner
@CheckForNullpublic com.nomagic.ui.banners.Banner getBanner()
Gets banner for this diagram descriptor.
Returns:
banner for this diagram descriptor.
setBanner
public void setBanner(@CheckForNull
 com.nomagic.ui.banners.Banner banner)
Sets banner for this diagram descriptor.
Parameters:
`banner` - banner to set.
configureNewDiagram
public void configureNewDiagram([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 @CheckForNull
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) parent)
Configure new created diagram
Parameters:
`diagram` - diagram
`parent` - parent
hasContent
public boolean hasContent()
Does diagram has content. e.g. does diagram has content for locking/unlocking
Returns:
does diagram has content

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class DiagramDescriptor">Class DiagramDescriptor</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.DiagramDescriptor</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="diagrams/NonSymbolDiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml.diagrams">NonSymbolDiagramDescriptor</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">DiagramDescriptor</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></span></div>
<div class="block">Descriptor of some extended diagram.<br/>
 This descriptor is used to define a new diagram type in the MagicDraw application. New diagram type be extended
 from some already existing type. New diagram will have separate diagram panel with its own toolbar.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DiagramDescriptor</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#configureNewDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">configureNewDiagram</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> parent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configure new created diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbbreviation()">getAbbreviation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ui.banners.Banner</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBanner()">getBanner</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets banner for this diagram descriptor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCategory()">getCategory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Diagram category name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../actions/MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramActions()">getDiagramActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns manager of actions used in the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="../actions/DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramContextConfigurator()">getDiagramContextConfigurator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramShortcutsConfigurator()">getDiagramShortcutsConfigurator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramToolbarConfigurator()">getDiagramToolbarConfigurator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramTypeId()">getDiagramTypeId</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return diagram type id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.DiagramDescriptor.DiagramWrapper</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramWrapper()">getDiagramWrapper</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHelpID()">getHelpID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getKind()">getKind</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a diagram kind used for grouping diagrams by their nature - symbolic diagram, table and so on.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMainMenuConfigurator()">getMainMenuConfigurator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMainToolbarConfigurator()">getMainToolbarConfigurator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPluralDiagramTypeHumanName()">getPluralDiagramTypeHumanName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return diagram human name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProfiles()">getProfiles</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns path for profile of this diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.RequiredFeature</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiredFeature()">getRequiredFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets required feature by this diagram descriptor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.core.Feature&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiredFeatures()">getRequiredFeatures</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets required features which are needed by this diagram descriptor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final com.nomagic.magicdraw.plugins.RequiredPluginInfo</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiredPlugin()">getRequiredPlugin</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Required plugin for this diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourceProviderID()">getResourceProviderID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSingularDiagramTypeHumanName()">getSingularDiagramTypeHumanName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return diagram human name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSmallIcon()">getSmallIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If descriptor provides icon URL,  this method should not be overridden.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSmallIconURL()">getSmallIconURL</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">URL of small icon for diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSmartManipulatorsActions(boolean)">getSmartManipulatorsActions</a><wbr/>(boolean superType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.actions.SmartManipulatorsAMConfigurator</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSmartManipulatorsConfigurator()">getSmartManipulatorsConfigurator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypes(com.nomagic.magicdraw.core.Project)">getStereotypes</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSuperType()">getSuperType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns super type of this diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSVGIcon()">getSVGIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Resizable icon for diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetsManipulatorsActions(boolean)">getTargetsManipulatorsActions</a><wbr/>(boolean superType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../actions/TargetElementAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">TargetElementAMConfigurator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetsManipulatorsConfigurator()">getTargetsManipulatorsConfigurator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasContent()">hasContent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Does diagram has content.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#importProfile(com.nomagic.magicdraw.core.Project,boolean)">importProfile</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean ui)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Import profile for this diagram into a given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isCreatable()">isCreatable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns creatable flag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isProfileLoaded(com.nomagic.magicdraw.core.Project)">isProfileLoaded</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSupported()">isSupported</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if all necessary prerequisites are available to support this type of diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSupported(com.nomagic.magicdraw.uml.DiagramDescriptor)">isSupported</a><wbr/>(<a href="DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a> diagramDescriptor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUsedForSymbols()">isUsedForSymbols</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if this diagram is used to draw symbols.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#profileLoaded(com.nomagic.magicdraw.core.Project)">profileLoaded</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if UML Profile for this diagram already loaded in the model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBanner(com.nomagic.ui.banners.Banner)">setBanner</a><wbr/>(com.nomagic.ui.banners.Banner banner)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets banner for this diagram descriptor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCategory(java.lang.String)">setCategory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> category)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set diagram category name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHelpID(java.lang.String)">setHelpID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRequiredFeatures(java.util.Collection)">setRequiredFeatures</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.core.Feature&gt; requiredFeatures)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets required features which are needed by this diagram descriptor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRequiredPlugin(com.nomagic.magicdraw.plugins.RequiredPluginInfo)">setRequiredPlugin</a><wbr/>(com.nomagic.magicdraw.plugins.RequiredPluginInfo plugin)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets required plugin for this diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setResourceProviderID(java.lang.String)">setResourceProviderID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceProviderID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Usual diagrams should provide resource provider id, in other case buttons groups and descriptions will be not translatable.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSmallIcon(com.nomagic.ui.ResizableIcon)">setSmallIcon</a><wbr/>(<a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#storeDiagramProperties()">storeDiagramProperties</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if diagram properties for this diagram should be stored.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>DiagramDescriptor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramDescriptor</span>()</div>
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
<section class="detail" id="getSuperType()">
<h3>getSuperType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSuperType</span>()</div>
<div class="block">Returns super type of this diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>String the 'super diagram' type of the diagram type.
 E.g. <code>Interaction Diagram</code> is a 'super diagram' for <code>Collaboration Diagram</code> and
 <code>Sequence Diagram</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreatable()">
<h3>isCreatable</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type">boolean</span> <span class="element-name">isCreatable</span>()</div>
<div class="block">Returns creatable flag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean flag indicating if the diagram will be creatable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUsedForSymbols()">
<h3>isUsedForSymbols</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUsedForSymbols</span>()</div>
<div class="block">Check if this diagram is used to draw symbols. Some diagram may be used to display tables,
 graphs or other components (for example  dependency matrix table)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if diagram is used to draw symbols</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="storeDiagramProperties()">
<h3>storeDiagramProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">storeDiagramProperties</span>()</div>
<div class="block">Checks if diagram properties for this diagram should be stored.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if diagram properties for this diagram should be stored.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramToolbarConfigurator()">
<h3>getDiagramToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></span> <span class="element-name">getDiagramToolbarConfigurator</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>AMConfigurator which configures described diagram toolbar.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramShortcutsConfigurator()">
<h3>getDiagramShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></span> <span class="element-name">getDiagramShortcutsConfigurator</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>AMConfigurator which configures described diagram shortcuts.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContextConfigurator()">
<h3>getDiagramContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a href="../actions/DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a></span> <span class="element-name">getDiagramContextConfigurator</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>AMConfigurator which configures described diagram context menu actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramTypeId()">
<h3>getDiagramTypeId</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramTypeId</span>()</div>
<div class="block">Return diagram type id. It is used to identify the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>String used to identify diagram type.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbbreviation()">
<h3>getAbbreviation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAbbreviation</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the abbreviation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSingularDiagramTypeHumanName()">
<h3>getSingularDiagramTypeHumanName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSingularDiagramTypeHumanName</span>()</div>
<div class="block">Return diagram human name. It is used to show the diagram type in the UI.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>human diagram name in singular.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPluralDiagramTypeHumanName()">
<h3>getPluralDiagramTypeHumanName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPluralDiagramTypeHumanName</span>()</div>
<div class="block">Return diagram human name. It is used to show the diagram type in the UI.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>human diagram name in plural.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSVGIcon()">
<h3>getSVGIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getSVGIcon</span>()</div>
<div class="block">Resizable icon for diagram. svg and wmf format. Used in Content diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>resizable icon in svg or wmf formats.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSmallIconURL()">
<h3>getSmallIconURL</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a></span> <span class="element-name">getSmallIconURL</span>()</div>
<div class="block">URL of small icon for diagram. Used in browser and menu.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>URL to icon shown diagram in browser and menu items.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResourceProviderID()">
<h3>getResourceProviderID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getResourceProviderID</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>resource provider id which is used to translate text read from descriptor file. May be null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setResourceProviderID(java.lang.String)">
<h3>setResourceProviderID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setResourceProviderID</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceProviderID)</span></div>
<div class="block">Usual diagrams should provide resource provider id, in other case buttons groups and descriptions will be not translatable.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resourceProviderID</code> - provider id which is used to translate text read from descriptor file. May be null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHelpID()">
<h3>getHelpID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHelpID</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>online help page name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHelpID(java.lang.String)">
<h3>setHelpID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHelpID</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>helpID</code> - new online page name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSmallIcon(com.nomagic.ui.ResizableIcon)">
<h3>setSmallIcon</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setSmallIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSmallIcon()">
<h3>getSmallIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getSmallIcon</span>()</div>
<div class="block">If descriptor provides icon URL,  this method should not be overridden.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMainMenuConfigurator()">
<h3>getMainMenuConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></span> <span class="element-name">getMainMenuConfigurator</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>AMConfigurator which configures main menu for adding this diagram specific actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMainToolbarConfigurator()">
<h3>getMainToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></span> <span class="element-name">getMainToolbarConfigurator</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>AMConfigurator which configures main toolbar for adding this diagram specific actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="profileLoaded(com.nomagic.magicdraw.core.Project)">
<h3>profileLoaded</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">profileLoaded</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Checks if UML Profile for this diagram already loaded in the model.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>true, if profile already loaded. Here returns true.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isProfileLoaded(com.nomagic.magicdraw.core.Project)">
<h3>isProfileLoaded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isProfileLoaded</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>true if required profile is loaded.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProfiles()">
<h3>getProfiles</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</span> <span class="element-name">getProfiles</span>()</div>
<div class="block">Returns path for profile of this diagram. If path is not null, profile will be loaded during diagram creation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>some path to xml file of profile or null if profile does not exist for this type of the diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramWrapper()">
<h3>getDiagramWrapper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.DiagramDescriptor.DiagramWrapper</span> <span class="element-name">getDiagramWrapper</span>()</div>
</section>
</li>
<li>
<section class="detail" id="importProfile(com.nomagic.magicdraw.core.Project,boolean)">
<h3>importProfile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">importProfile</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean ui)</span></div>
<div class="block">Import profile for this diagram into a given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>ui</code> - show ui messages in case of some problems</dd>
<dt>Returns:</dt>
<dd>true if required profiles are attached to project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramActions()">
<h3>getDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../actions/MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">getDiagramActions</span>()</div>
<div class="block">Returns manager of actions used in the diagram.
 Later these actions must be configured for toolbar or shortcuts.
 Only one instance of action must be used in the configurators. If this rule is not applied, some problems may
 occur(for example changed by user keyboard shortcuts for action may not be saved).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager of actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypes(com.nomagic.magicdraw.core.Project)">
<h3>getStereotypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getStereotypes</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>list of stereotypes ids, these stereotypes will be assigned to the diagram element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSmartManipulatorsConfigurator()">
<h3>getSmartManipulatorsConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.actions.SmartManipulatorsAMConfigurator</span> <span class="element-name">getSmartManipulatorsConfigurator</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTargetsManipulatorsConfigurator()">
<h3>getTargetsManipulatorsConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../actions/TargetElementAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">TargetElementAMConfigurator</a></span> <span class="element-name">getTargetsManipulatorsConfigurator</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSmartManipulatorsActions(boolean)">
<h3>getSmartManipulatorsActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getSmartManipulatorsActions</span><wbr/><span class="parameters">(boolean superType)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTargetsManipulatorsActions(boolean)">
<h3>getTargetsManipulatorsActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getTargetsManipulatorsActions</span><wbr/><span class="parameters">(boolean superType)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRequiredPlugin()">
<h3>getRequiredPlugin</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type">com.nomagic.magicdraw.plugins.RequiredPluginInfo</span> <span class="element-name">getRequiredPlugin</span>()</div>
<div class="block">Required plugin for this diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>required plugin for this diagram. If plugin is not available diagram will be not loaded. If returns null no plugin is required.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRequiredPlugin(com.nomagic.magicdraw.plugins.RequiredPluginInfo)">
<h3>setRequiredPlugin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRequiredPlugin</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.magicdraw.plugins.RequiredPluginInfo plugin)</span></div>
<div class="block">Sets required plugin for this diagram.
 If required plugin is not available diagram should not be loaded.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>plugin</code> - new required feature. Can be null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiredFeatures()">
<h3>getRequiredFeatures</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.core.Feature&gt;</span> <span class="element-name">getRequiredFeatures</span>()</div>
<div class="block">Gets required features which are needed by this diagram descriptor.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>required features which are needed by this diagram descriptor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRequiredFeatures(java.util.Collection)">
<h3>setRequiredFeatures</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRequiredFeatures</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.core.Feature&gt; requiredFeatures)</span></div>
<div class="block">Sets required features which are needed by this diagram descriptor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>requiredFeatures</code> - required features which are needed by this diagram descriptor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSupported()">
<h3>isSupported</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSupported</span>()</div>
<div class="block">Indicates if all necessary prerequisites are available to support this type of diagram.
 It can be required plugin or required feature.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if diagram is supported, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSupported(com.nomagic.magicdraw.uml.DiagramDescriptor)">
<h3>isSupported</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSupported</span><wbr/><span class="parameters">(@CheckForNull
 <a href="DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a> diagramDescriptor)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCategory()">
<h3>getCategory</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCategory</span>()</div>
<div class="block">Diagram category name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram category</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getKind()">
<h3>getKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getKind</span>()</div>
<div class="block">Returns a diagram kind used for grouping diagrams by their nature - symbolic diagram, table and so on.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram kind</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCategory(java.lang.String)">
<h3>setCategory</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCategory</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> category)</span></div>
<div class="block">Set diagram category name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - category diagram category name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiredFeature()">
<h3>getRequiredFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.RequiredFeature</span> <span class="element-name">getRequiredFeature</span>()</div>
<div class="block">Gets required feature by this diagram descriptor.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>required feature by this diagram descriptor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBanner()">
<h3>getBanner</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.ui.banners.Banner</span> <span class="element-name">getBanner</span>()</div>
<div class="block">Gets banner for this diagram descriptor.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>banner for this diagram descriptor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBanner(com.nomagic.ui.banners.Banner)">
<h3>setBanner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBanner</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.ui.banners.Banner banner)</span></div>
<div class="block">Sets banner for this diagram descriptor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>banner</code> - banner to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="configureNewDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>configureNewDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">configureNewDiagram</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> parent)</span></div>
<div class="block">Configure new created diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram</dd>
<dd><code>parent</code> - parent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasContent()">
<h3>hasContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasContent</span>()</div>
<div class="block">Does diagram has content. e.g. does diagram has content for locking/unlocking</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>does diagram has content</dd>
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
