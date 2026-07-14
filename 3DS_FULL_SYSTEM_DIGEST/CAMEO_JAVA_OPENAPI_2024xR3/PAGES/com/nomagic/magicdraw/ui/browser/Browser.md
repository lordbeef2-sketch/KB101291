# JAVA OPENAPI: Browser (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/browser/Browser.html
- source_path: `com/nomagic/magicdraw/ui/browser/Browser.html`
- source_sha256: `8e91efe2ef7efe43c395e4834a51b11a5c72f67bc81eb31ad7f94348485a44bd`
- captured_utc: `2026-07-14T16:55:51.758417+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.browser](package-summary.html)

## Class Browser

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.browser.Browser

@OpenApipublic classBrowser
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The MagicDraw application UI part with trees, documentation, zoom and search panels.
 The primary purpose of this class is to manages predefined Trees and Panels in MagicDraw application Browser.
 It has five trees:
 containment
 diagrams
 inheritance
 extensions
 search results
Also it has two panels:
 documentation
 zoom control
Sample of accessing Swing JTree of containment tree:
 getContainmentTree().getTree()

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static interface`
`[Browser.BrowserInitializer](Browser.BrowserInitializer.html)`
Browser initializer is an extension point for browser creation.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Browser](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[activateVisibleTrees](#activateVisibleTrees())()`
Activate all visible on-screen trees.
`static void`
`[addBrowserInitializer](#addBrowserInitializer(com.nomagic.magicdraw.ui.browser.Browser.BrowserInitializer))([Browser.BrowserInitializer](Browser.BrowserInitializer.html) initializer)`
Add new browser initializer.
`void`
`[addPanel](#addPanel(com.nomagic.ui.ExtendedPanel))([ExtendedPanel](../../../ui/ExtendedPanel.html) panel)`
Adds a new browser panel.Should be called during browser initialization only.
`void`
`[addPanel](#addPanel(com.nomagic.ui.ExtendedPanel,int))([ExtendedPanel](../../../ui/ExtendedPanel.html) panel,
 int index)`
Adds a new browser panel.Should be called during browser initialization only.
`[SearchResultsTree](SearchResultsTree.html)`
`[addSearchResultsTree](#addSearchResultsTree())()`
Adds new browser tab tree for search results
`[BrowserTabTree](BrowserTabTree.html)`
`[addTree](#addTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree,boolean,boolean))([BrowserTabTree](BrowserTabTree.html) tree,
 boolean drag,
 boolean drop)`
Adds and does set up a new tree to the browser.
`[BrowserTabTree](BrowserTabTree.html)`
`[addTree](#addTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree,boolean,boolean,int))([BrowserTabTree](BrowserTabTree.html) tree,
 boolean drag,
 boolean drop,
 int index)`
Adds and does set up a new tree to the browser.
`void`
`[decorateBrowser](#decorateBrowser())()`
changes browser's trees decoration
`void`
`[dispose](#dispose())()`

`[BrowserTabTree](BrowserTabTree.html)`
`[getActiveTree](#getActiveTree())()`
Returns reference to the active tree.
`static [WindowComponentInfo](../WindowComponentInfo.html)[]`
`[getAllComponentInfo](#getAllComponentInfo())()`
Used in JIDE to create actions for these components
`[BrowserTabTree](BrowserTabTree.html)`
`[getBrowserTreeForNode](#getBrowserTreeForNode(com.nomagic.magicdraw.ui.browser.Node))([Node](Node.html) node)`

`[BrowserTabTree](BrowserTabTree.html)`
`[getBrowserTreeForNode](#getBrowserTreeForNode(com.nomagic.magicdraw.ui.browser.Node,java.lang.String))([Node](Node.html) node,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`

`[ContainmentTree](ContainmentTree.html)`
`[getContainmentTree](#getContainmentTree())()`
Returns containment tree.
`[DiagramsTree](DiagramsTree.html)`
`[getDiagramsTree](#getDiagramsTree())()`
Returns diagrams tree.
`com.nomagic.magicdraw.ui.browser.BrowserDocumentationPanel`
`[getDocPanel](#getDocPanel())()`
Returns documentation panel.
`[ExtensionsTree](ExtensionsTree.html)`
`[getExtensionsTree](#getExtensionsTree())()`
Returns extensions tree.
`[ExtensionsTree](ExtensionsTree.html)`
`[getExtensionsTree](#getExtensionsTree(boolean))(boolean addIfNotExists)`
Returns extensions tree.
`[InheritanceTree](InheritanceTree.html)`
`[getInheritanceTree](#getInheritanceTree())()`
Returns inheritance tree if it exists, otherwise null
`[BrowserTabTree](BrowserTabTree.html)`
`[getLastActiveTree](#getLastActiveTree(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`

`[LockViewTree](../../teamwork2/ui/LockViewTree.html)`
`[getLockViewTree](#getLockViewTree())()`
Returns Lock view tree.
`com.nomagic.magicdraw.ui.browser.BrowserNodeMap`
`[getNodeMap](#getNodeMap())()`

`com.nomagic.magicdraw.ui.diagramoverview.DiagramOverviewPanel`
`[getOverviewPanel](#getOverviewPanel())()`
Returns zoom panel.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExtendedPanel](../../../ui/ExtendedPanel.html)>`
`[getPanels](#getPanels())()`

`[Project](../../core/Project.html)`
`[getProject](#getProject())()`

`com.nomagic.magicdraw.properties.qproperties.ui.QPropertiesPanel`
`[getQPanel](#getQPanel())()`

`[SearchResultsTree](SearchResultsTree.html)`
`[getSearchResultsTree](#getSearchResultsTree())()`
Returns last active or newly added search results tree.
`[SearchResultsTree](SearchResultsTree.html)`
`[getSearchResultsTree](#getSearchResultsTree(boolean))(boolean addIfNotExists)`
Returns last active or newly added search results tree.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SearchResultsTree](SearchResultsTree.html)>`
`[getSearchResultTrees](#getSearchResultTrees())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BrowserTabTree](BrowserTabTree.html)>`
`[getTreeActivationHistory](#getTreeActivationHistory())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BrowserTabTree](BrowserTabTree.html)>`
`[getTreeActivationHistory](#getTreeActivationHistory(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BrowserTabTree](BrowserTabTree.html)>`
`[getTrees](#getTrees())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BrowserTabTree](BrowserTabTree.html)>`
`[getTrees](#getTrees(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`

`void`
`[initBrowser](#initBrowser(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`

`void`
`[initTrees](#initTrees())()`

`void`
`[initTrees](#initTrees(boolean))(boolean activateTree)`

`void`
`[initTrees](#initTrees(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 boolean activateTree)`

`void`
`[initTrees](#initTrees(java.util.List,boolean))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BrowserTabTree](BrowserTabTree.html)> trees,
 boolean activateTree)`
Init the browser.
`boolean`
`[isExtensionTreeAllowed](#isExtensionTreeAllowed())()`

`boolean`
`[isInitialized](#isInitialized())()`

`protected boolean`
`[isTreeExpandStateRestored](#isTreeExpandStateRestored())()`
True if expand state is restored, else false.
`void`
`[loadTrees](#loadTrees())()`
Loads persistent trees specified in project options
`void`
`[reInitTrees](#reInitTrees())()`
ReInit browser trees
`void`
`[rememberState](#rememberState())()`
Remembers all expanded nodes in all trees.
`void`
`[removeAllRemovablePanels](#removeAllRemovablePanels())()`
Removes all removable panels.
`void`
`[removeAllRemovableTrees](#removeAllRemovableTrees())()`
Removes all removable trees.
`static void`
`[removeBrowserInitializer](#removeBrowserInitializer(com.nomagic.magicdraw.ui.browser.Browser.BrowserInitializer))([Browser.BrowserInitializer](Browser.BrowserInitializer.html) initializer)`
Remove browser initializer.
`void`
`[removeComponentInfo](#removeComponentInfo(com.nomagic.magicdraw.ui.WindowComponentInfo))([WindowComponentInfo](../WindowComponentInfo.html) info)`
Remove information about registered component
`void`
`[removePanel](#removePanel(com.nomagic.ui.ExtendedPanel))([ExtendedPanel](../../../ui/ExtendedPanel.html) panel)`
Removes browser panel.
`void`
`[removeTree](#removeTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree))([BrowserTabTree](BrowserTabTree.html) tree)`
Removes a tree from the browser.Should be called during browser initialization only.
`void`
`[removeTree](#removeTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree,boolean))([BrowserTabTree](BrowserTabTree.html) tree,
 boolean saveLayout)`
Removes a tree from the browser.Should be called during browser initialization only.
`void`
`[removeTreeFromBrowser](#removeTreeFromBrowser(com.nomagic.magicdraw.ui.browser.BrowserTabTree,boolean))([BrowserTabTree](BrowserTabTree.html) tree,
 boolean saveLayout)`
Remove given tree and also close a window of tree if any
`void`
`[restoreState](#restoreState())()`
Restores all expanded nodes in all trees.
`void`
`[saveTreesLayout](#saveTreesLayout())()`
Save information about trees layout into project options
`void`
`[setActiveTree](#setActiveTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree))([BrowserTabTree](BrowserTabTree.html) activeTree)`
Sets active tree.
`void`
`[sortAllTrees](#sortAllTrees())()`
Sorts the nodes in all trees.
`void`
`[updateBrowser](#updateBrowser(boolean))(boolean updateOnlyDirty)`

`void`
`[updateBrowser](#updateBrowser(boolean,java.lang.String))(boolean updateOnlyDirty,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`
Updates the nodes in all trees.
`void`
`[updateSortAlwaysFlag](#updateSortAlwaysFlag())()`
Updates the sort always flag in trees' models.
`void`
`[updateSortAlwaysFlagForDifferentTrees](#updateSortAlwaysFlagForDifferentTrees())()`
Updates the sort always flag in trees' models.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Browser
public Browser()
 ============ METHOD DETAIL ========== 
Method Details
isInitialized
public boolean isInitialized()
initBrowser
public void initBrowser([Project](../../core/Project.html) project)
getProject
public [Project](../../core/Project.html) getProject()
loadTrees
public void loadTrees()
Loads persistent trees specified in project options
addPanel
@OpenApipublic void addPanel([ExtendedPanel](../../../ui/ExtendedPanel.html) panel)
Adds a new browser panel.Should be called during browser initialization only.
Parameters:
`panel` - panel
See Also:
[`Browser.BrowserInitializer`](Browser.BrowserInitializer.html)
addPanel
@OpenApipublic void addPanel([ExtendedPanel](../../../ui/ExtendedPanel.html) panel,
 int index)
Adds a new browser panel.Should be called during browser initialization only.
Parameters:
`panel` - panel
`index` - index
See Also:
[`Browser.BrowserInitializer`](Browser.BrowserInitializer.html)
removePanel
@OpenApipublic void removePanel([ExtendedPanel](../../../ui/ExtendedPanel.html) panel)
Removes browser panel. Should be called during browser initialization only.
Parameters:
`panel` - panel
See Also:
[`Browser.BrowserInitializer`](Browser.BrowserInitializer.html)
addTree
@OpenApipublic [BrowserTabTree](BrowserTabTree.html) addTree([BrowserTabTree](BrowserTabTree.html) tree,
 boolean drag,
 boolean drop)
Adds and does set up a new tree to the browser. Should be called during browser initialization only.
Parameters:
`tree` - a new tree
`drag` - tree should be a drag operation source
`drop` - tree should be a drop operation source
Returns:
added tree
See Also:
[`Browser.BrowserInitializer`](Browser.BrowserInitializer.html)
addTree
@OpenApipublic [BrowserTabTree](BrowserTabTree.html) addTree(@Nonnull
 [BrowserTabTree](BrowserTabTree.html) tree,
 boolean drag,
 boolean drop,
 int index)
Adds and does set up a new tree to the browser. Should be called during browser initialization only.
Parameters:
`tree` - a new tree
`drag` - tree should be a drag operation source
`drop` - tree should be a drop operation source
`index` - the position of new tree among other trees
Returns:
added tree
See Also:
[`Browser.BrowserInitializer`](Browser.BrowserInitializer.html)
removeTree
@OpenApipublic void removeTree([BrowserTabTree](BrowserTabTree.html) tree)
Removes a tree from the browser.Should be called during browser initialization only.
Parameters:
`tree` - a new tree
See Also:
[`Browser.BrowserInitializer`](Browser.BrowserInitializer.html)
removeTree
@OpenApipublic void removeTree([BrowserTabTree](BrowserTabTree.html) tree,
 boolean saveLayout)
Removes a tree from the browser.Should be called during browser initialization only.
Parameters:
`tree` - a new tree
`saveLayout` - save information about existing trees into project options
See Also:
[`Browser.BrowserInitializer`](Browser.BrowserInitializer.html)
removeComponentInfo
public void removeComponentInfo([WindowComponentInfo](../WindowComponentInfo.html) info)
Remove information about registered component
Parameters:
`info` - component info
setActiveTree
public void setActiveTree([BrowserTabTree](BrowserTabTree.html) activeTree)
Sets active tree. Does not select this tree in TabbedPane, just changes the reference to active tree in code.
Parameters:
`activeTree` - a new active tree for this browser.
getActiveTree
@CheckForNull
@OpenApipublic [BrowserTabTree](BrowserTabTree.html) getActiveTree()
Returns reference to the active tree.
Returns:
active tree.
initTrees
public void initTrees([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 boolean activateTree)
initTrees
public void initTrees()
initTrees
public void initTrees(boolean activateTree)
initTrees
public void initTrees([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BrowserTabTree](BrowserTabTree.html)> trees,
 boolean activateTree)
Init the browser. Init all browser trees.
Parameters:
`trees` - trees to init
`activateTree` - activate tree
activateVisibleTrees
public void activateVisibleTrees()
Activate all visible on-screen trees.
sortAllTrees
public void sortAllTrees()
Sorts the nodes in all trees.
updateSortAlwaysFlag
public void updateSortAlwaysFlag()
Updates the sort always flag in trees' models.
 If sort flag is true, sorts the trees.
updateSortAlwaysFlagForDifferentTrees
public void updateSortAlwaysFlagForDifferentTrees()
Updates the sort always flag in trees' models.
 If sort flag is true, sorts tress that had different flag.
reInitTrees
public void reInitTrees()
ReInit browser trees
updateBrowser
public void updateBrowser(boolean updateOnlyDirty,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
Updates the nodes in all trees. Updates documentation panel also.
Parameters:
`updateOnlyDirty` - true if only dirty nodes will be updated. on false all nodes will be updated
`group` - trees group
updateBrowser
public void updateBrowser(boolean updateOnlyDirty)
decorateBrowser
public void decorateBrowser()
changes browser's trees decoration
getDocPanel
@CheckForNullpublic com.nomagic.magicdraw.ui.browser.BrowserDocumentationPanel getDocPanel()
Returns documentation panel.
Returns:
documentation panel.
getOverviewPanel
public com.nomagic.magicdraw.ui.diagramoverview.DiagramOverviewPanel getOverviewPanel()
Returns zoom panel.
Returns:
zoom panel.
getQPanel
@CheckForNullpublic com.nomagic.magicdraw.properties.qproperties.ui.QPropertiesPanel getQPanel()
getInheritanceTree
@OpenApi
@CheckForNullpublic [InheritanceTree](InheritanceTree.html) getInheritanceTree()
Returns inheritance tree if it exists, otherwise null
Returns:
inheritance tree.
getLockViewTree
@CheckForNull
@OpenApipublic [LockViewTree](../../teamwork2/ui/LockViewTree.html) getLockViewTree()
Returns Lock view tree.
Returns:
lock view tree.
getLastActiveTree
@CheckForNullpublic [BrowserTabTree](BrowserTabTree.html) getLastActiveTree([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
getContainmentTree
@OpenApipublic [ContainmentTree](ContainmentTree.html) getContainmentTree()
Returns containment tree.
Returns:
containment tree.
getDiagramsTree
@OpenApipublic [DiagramsTree](DiagramsTree.html) getDiagramsTree()
Returns diagrams tree.
Returns:
diagrams tree.
getExtensionsTree
@OpenApi
@CheckForNullpublic [ExtensionsTree](ExtensionsTree.html) getExtensionsTree()
Returns extensions tree.
Returns:
extensions tree.
getExtensionsTree
@OpenApi
@CheckForNullpublic [ExtensionsTree](ExtensionsTree.html) getExtensionsTree(boolean addIfNotExists)
Returns extensions tree.
Parameters:
`addIfNotExists` - add tree if not exists and it is allowed to have extension tree
Returns:
extensions tree.
getSearchResultsTree
@OpenApipublic [SearchResultsTree](SearchResultsTree.html) getSearchResultsTree()
Returns last active or newly added search results tree.
Returns:
search results tree.
getSearchResultsTree
@CheckForNull
@OpenApipublic [SearchResultsTree](SearchResultsTree.html) getSearchResultsTree(boolean addIfNotExists)
Returns last active or newly added search results tree.
Parameters:
`addIfNotExists` - add search result tree if it does not exist
Returns:
search results tree.
addSearchResultsTree
@CheckForNullpublic [SearchResultsTree](SearchResultsTree.html) addSearchResultsTree()
Adds new browser tab tree for search results
Returns:
search results tree
getNodeMap
public com.nomagic.magicdraw.ui.browser.BrowserNodeMap getNodeMap()
rememberState
public void rememberState()
Remembers all expanded nodes in all trees.
 Later these expanded nodes can be restored with method restoreExpandedNodes().
See Also:
[`restoreState()`](#restoreState())
`TreeStateManager`
restoreState
public void restoreState()
Restores all expanded nodes in all trees.
 Method rememberExpandedNodes must be called first.
See Also:
[`rememberState()`](#rememberState())
`TreeStateManager`
isTreeExpandStateRestored
protected boolean isTreeExpandStateRestored()
True if expand state is restored, else false.
Returns:
true if expand state is restored, else false.
getTrees
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BrowserTabTree](BrowserTabTree.html)> getTrees()
Returns:
a list of browser trees
getTrees
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BrowserTabTree](BrowserTabTree.html)> getTrees([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
getSearchResultTrees
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SearchResultsTree](SearchResultsTree.html)> getSearchResultTrees()
getPanels
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExtendedPanel](../../../ui/ExtendedPanel.html)> getPanels()
Returns:
a list of browser panels.
dispose
public void dispose()
getAllComponentInfo
public static [WindowComponentInfo](../WindowComponentInfo.html)[] getAllComponentInfo()
Used in JIDE to create actions for these components
Returns:
info about all windows components related to browser
getTreeActivationHistory
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BrowserTabTree](BrowserTabTree.html)> getTreeActivationHistory()
getTreeActivationHistory
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BrowserTabTree](BrowserTabTree.html)> getTreeActivationHistory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
removeTreeFromBrowser
public void removeTreeFromBrowser([BrowserTabTree](BrowserTabTree.html) tree,
 boolean saveLayout)
Remove given tree and also close a window of tree if any
Parameters:
`tree` - tree
`saveLayout` - save information about trees layout
saveTreesLayout
public void saveTreesLayout()
Save information about trees layout into project options
removeAllRemovableTrees
public void removeAllRemovableTrees()
Removes all removable trees.
removeAllRemovablePanels
public void removeAllRemovablePanels()
Removes all removable panels. Removables panels are of type BrowserPanelInfo and have field showByDefault set to true.
getBrowserTreeForNode
@CheckForNullpublic [BrowserTabTree](BrowserTabTree.html) getBrowserTreeForNode([Node](Node.html) node)
getBrowserTreeForNode
@CheckForNullpublic [BrowserTabTree](BrowserTabTree.html) getBrowserTreeForNode([Node](Node.html) node,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
isExtensionTreeAllowed
public boolean isExtensionTreeAllowed()
Returns:
true if Extensions tree can be created in a browser
addBrowserInitializer
@OpenApipublic static void addBrowserInitializer([Browser.BrowserInitializer](Browser.BrowserInitializer.html) initializer)
Add new browser initializer.
Parameters:
`initializer` - initializer
removeBrowserInitializer
@OpenApipublic static void removeBrowserInitializer([Browser.BrowserInitializer](Browser.BrowserInitializer.html) initializer)
Remove browser initializer.
Parameters:
`initializer` - initializer

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.browser</a></div>
<h1 class="title" title="Class Browser">Class Browser</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.browser.Browser</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Browser</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The MagicDraw application UI part with trees, documentation, zoom and search panels.
 The primary purpose of this class is to manages predefined Trees and Panels in MagicDraw application Browser.
 <p></p>It has five trees:
 <ul>
<li>containment
 <li>diagrams
 <li>inheritance
 <li>extensions
 <li>search results
 </li></li></li></li></li></ul>
<p></p>Also it has two panels:
 <ul>
<li>documentation
 <li>zoom control
 </li></li></ul>
<p>
 Sample of accessing Swing JTree of containment tree:
 <pre>getContainmentTree().getTree()</pre></p></div>
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
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser">Browser.BrowserInitializer</a></code></div>
<div class="col-last even-row-color">
<div class="block">Browser initializer is an extension point for browser creation.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Browser</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#activateVisibleTrees()">activateVisibleTrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Activate all visible on-screen trees.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addBrowserInitializer(com.nomagic.magicdraw.ui.browser.Browser.BrowserInitializer)">addBrowserInitializer</a><wbr/>(<a href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser">Browser.BrowserInitializer</a> initializer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Add new browser initializer.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPanel(com.nomagic.ui.ExtendedPanel)">addPanel</a><wbr/>(<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a> panel)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a new browser panel.Should be called during browser initialization only.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPanel(com.nomagic.ui.ExtendedPanel,int)">addPanel</a><wbr/>(<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a> panel,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a new browser panel.Should be called during browser initialization only.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SearchResultsTree.html" title="class in com.nomagic.magicdraw.ui.browser">SearchResultsTree</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSearchResultsTree()">addSearchResultsTree</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new browser tab tree for search results</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree,boolean,boolean)">addTree</a><wbr/>(<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree,
 boolean drag,
 boolean drop)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds and does set up a new tree to the browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree,boolean,boolean,int)">addTree</a><wbr/>(<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree,
 boolean drag,
 boolean drop,
 int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds and does set up a new tree to the browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#decorateBrowser()">decorateBrowser</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">changes browser's trees decoration</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveTree()">getActiveTree</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns reference to the active tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../WindowComponentInfo.html" title="class in com.nomagic.magicdraw.ui">WindowComponentInfo</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllComponentInfo()">getAllComponentInfo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Used in JIDE to create actions for these components</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBrowserTreeForNode(com.nomagic.magicdraw.ui.browser.Node)">getBrowserTreeForNode</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBrowserTreeForNode(com.nomagic.magicdraw.ui.browser.Node,java.lang.String)">getBrowserTreeForNode</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ContainmentTree.html" title="class in com.nomagic.magicdraw.ui.browser">ContainmentTree</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContainmentTree()">getContainmentTree</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns containment tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DiagramsTree.html" title="class in com.nomagic.magicdraw.ui.browser">DiagramsTree</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramsTree()">getDiagramsTree</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns diagrams tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.browser.BrowserDocumentationPanel</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocPanel()">getDocPanel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns documentation panel.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ExtensionsTree.html" title="class in com.nomagic.magicdraw.ui.browser">ExtensionsTree</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensionsTree()">getExtensionsTree</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns extensions tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ExtensionsTree.html" title="class in com.nomagic.magicdraw.ui.browser">ExtensionsTree</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensionsTree(boolean)">getExtensionsTree</a><wbr/>(boolean addIfNotExists)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns extensions tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="InheritanceTree.html" title="class in com.nomagic.magicdraw.ui.browser">InheritanceTree</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInheritanceTree()">getInheritanceTree</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns inheritance tree if it exists, otherwise null</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastActiveTree(java.lang.String)">getLastActiveTree</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../teamwork2/ui/LockViewTree.html" title="class in com.nomagic.magicdraw.teamwork2.ui">LockViewTree</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLockViewTree()">getLockViewTree</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns Lock view tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.browser.BrowserNodeMap</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNodeMap()">getNodeMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.diagramoverview.DiagramOverviewPanel</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOverviewPanel()">getOverviewPanel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns zoom panel.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPanels()">getPanels</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.properties.qproperties.ui.QPropertiesPanel</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getQPanel()">getQPanel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SearchResultsTree.html" title="class in com.nomagic.magicdraw.ui.browser">SearchResultsTree</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSearchResultsTree()">getSearchResultsTree</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns last active or newly added search results tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SearchResultsTree.html" title="class in com.nomagic.magicdraw.ui.browser">SearchResultsTree</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSearchResultsTree(boolean)">getSearchResultsTree</a><wbr/>(boolean addIfNotExists)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns last active or newly added search results tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="SearchResultsTree.html" title="class in com.nomagic.magicdraw.ui.browser">SearchResultsTree</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSearchResultTrees()">getSearchResultTrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTreeActivationHistory()">getTreeActivationHistory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTreeActivationHistory(java.lang.String)">getTreeActivationHistory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTrees()">getTrees</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTrees(java.lang.String)">getTrees</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initBrowser(com.nomagic.magicdraw.core.Project)">initBrowser</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initTrees()">initTrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initTrees(boolean)">initTrees</a><wbr/>(boolean activateTree)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initTrees(java.lang.String,boolean)">initTrees</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 boolean activateTree)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initTrees(java.util.List,boolean)">initTrees</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a>&gt; trees,
 boolean activateTree)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Init the browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isExtensionTreeAllowed()">isExtensionTreeAllowed</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isInitialized()">isInitialized</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTreeExpandStateRestored()">isTreeExpandStateRestored</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">True if expand state is restored, else false.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadTrees()">loadTrees</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Loads persistent trees specified in project options</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reInitTrees()">reInitTrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">ReInit browser trees</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#rememberState()">rememberState</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remembers all expanded nodes in all trees.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAllRemovablePanels()">removeAllRemovablePanels</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all removable panels.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAllRemovableTrees()">removeAllRemovableTrees</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all removable trees.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeBrowserInitializer(com.nomagic.magicdraw.ui.browser.Browser.BrowserInitializer)">removeBrowserInitializer</a><wbr/>(<a href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser">Browser.BrowserInitializer</a> initializer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Remove browser initializer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeComponentInfo(com.nomagic.magicdraw.ui.WindowComponentInfo)">removeComponentInfo</a><wbr/>(<a href="../WindowComponentInfo.html" title="class in com.nomagic.magicdraw.ui">WindowComponentInfo</a> info)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove information about registered component</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePanel(com.nomagic.ui.ExtendedPanel)">removePanel</a><wbr/>(<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a> panel)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes browser panel.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">removeTree</a><wbr/>(<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a tree from the browser.Should be called during browser initialization only.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree,boolean)">removeTree</a><wbr/>(<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree,
 boolean saveLayout)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a tree from the browser.Should be called during browser initialization only.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeTreeFromBrowser(com.nomagic.magicdraw.ui.browser.BrowserTabTree,boolean)">removeTreeFromBrowser</a><wbr/>(<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree,
 boolean saveLayout)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove given tree and also close a window of tree if any</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#restoreState()">restoreState</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Restores all expanded nodes in all trees.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveTreesLayout()">saveTreesLayout</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Save information about trees layout into project options</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setActiveTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">setActiveTree</a><wbr/>(<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> activeTree)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets active tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sortAllTrees()">sortAllTrees</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sorts the nodes in all trees.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateBrowser(boolean)">updateBrowser</a><wbr/>(boolean updateOnlyDirty)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateBrowser(boolean,java.lang.String)">updateBrowser</a><wbr/>(boolean updateOnlyDirty,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates the nodes in all trees.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateSortAlwaysFlag()">updateSortAlwaysFlag</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates the sort always flag in trees' models.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateSortAlwaysFlagForDifferentTrees()">updateSortAlwaysFlagForDifferentTrees</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates the sort always flag in trees' models.</div>
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
<h3>Browser</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Browser</span>()</div>
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
<section class="detail" id="isInitialized()">
<h3>isInitialized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isInitialized</span>()</div>
</section>
</li>
<li>
<section class="detail" id="initBrowser(com.nomagic.magicdraw.core.Project)">
<h3>initBrowser</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">initBrowser</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
</section>
</li>
<li>
<section class="detail" id="loadTrees()">
<h3>loadTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadTrees</span>()</div>
<div class="block">Loads persistent trees specified in project options</div>
</section>
</li>
<li>
<section class="detail" id="addPanel(com.nomagic.ui.ExtendedPanel)">
<h3>addPanel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPanel</span><wbr/><span class="parameters">(<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a> panel)</span></div>
<div class="block">Adds a new browser panel.Should be called during browser initialization only.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>panel</code> - panel</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser"><code>Browser.BrowserInitializer</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPanel(com.nomagic.ui.ExtendedPanel,int)">
<h3>addPanel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPanel</span><wbr/><span class="parameters">(<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a> panel,
 int index)</span></div>
<div class="block">Adds a new browser panel.Should be called during browser initialization only.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>panel</code> - panel</dd>
<dd><code>index</code> - index</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser"><code>Browser.BrowserInitializer</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePanel(com.nomagic.ui.ExtendedPanel)">
<h3>removePanel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePanel</span><wbr/><span class="parameters">(<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a> panel)</span></div>
<div class="block">Removes browser panel. Should be called during browser initialization only.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>panel</code> - panel</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser"><code>Browser.BrowserInitializer</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree,boolean,boolean)">
<h3>addTree</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></span> <span class="element-name">addTree</span><wbr/><span class="parameters">(<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree,
 boolean drag,
 boolean drop)</span></div>
<div class="block">Adds and does set up a new tree to the browser. Should be called during browser initialization only.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - a new tree</dd>
<dd><code>drag</code> - tree should be a drag operation source</dd>
<dd><code>drop</code> - tree should be a drop operation source</dd>
<dt>Returns:</dt>
<dd>added tree</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser"><code>Browser.BrowserInitializer</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree,boolean,boolean,int)">
<h3>addTree</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></span> <span class="element-name">addTree</span><wbr/><span class="parameters">(@Nonnull
 <a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree,
 boolean drag,
 boolean drop,
 int index)</span></div>
<div class="block">Adds and does set up a new tree to the browser. Should be called during browser initialization only.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - a new tree</dd>
<dd><code>drag</code> - tree should be a drag operation source</dd>
<dd><code>drop</code> - tree should be a drop operation source</dd>
<dd><code>index</code> - the position of new tree among other trees</dd>
<dt>Returns:</dt>
<dd>added tree</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser"><code>Browser.BrowserInitializer</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">
<h3>removeTree</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeTree</span><wbr/><span class="parameters">(<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree)</span></div>
<div class="block">Removes a tree from the browser.Should be called during browser initialization only.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - a new tree</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser"><code>Browser.BrowserInitializer</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree,boolean)">
<h3>removeTree</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeTree</span><wbr/><span class="parameters">(<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree,
 boolean saveLayout)</span></div>
<div class="block">Removes a tree from the browser.Should be called during browser initialization only.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - a new tree</dd>
<dd><code>saveLayout</code> - save information about existing trees into project options</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser"><code>Browser.BrowserInitializer</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeComponentInfo(com.nomagic.magicdraw.ui.WindowComponentInfo)">
<h3>removeComponentInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeComponentInfo</span><wbr/><span class="parameters">(<a href="../WindowComponentInfo.html" title="class in com.nomagic.magicdraw.ui">WindowComponentInfo</a> info)</span></div>
<div class="block">Remove information about registered component</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>info</code> - component info</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActiveTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">
<h3>setActiveTree</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActiveTree</span><wbr/><span class="parameters">(<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> activeTree)</span></div>
<div class="block">Sets active tree. Does not select this tree in TabbedPane, just changes the reference to active tree in code.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>activeTree</code> - a new active tree for this browser.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActiveTree()">
<h3>getActiveTree</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></span> <span class="element-name">getActiveTree</span>()</div>
<div class="block">Returns reference to the active tree.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>active tree.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initTrees(java.lang.String,boolean)">
<h3>initTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">initTrees</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 boolean activateTree)</span></div>
</section>
</li>
<li>
<section class="detail" id="initTrees()">
<h3>initTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">initTrees</span>()</div>
</section>
</li>
<li>
<section class="detail" id="initTrees(boolean)">
<h3>initTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">initTrees</span><wbr/><span class="parameters">(boolean activateTree)</span></div>
</section>
</li>
<li>
<section class="detail" id="initTrees(java.util.List,boolean)">
<h3>initTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">initTrees</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a>&gt; trees,
 boolean activateTree)</span></div>
<div class="block">Init the browser. Init all browser trees.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>trees</code> - trees to init</dd>
<dd><code>activateTree</code> - activate tree</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="activateVisibleTrees()">
<h3>activateVisibleTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">activateVisibleTrees</span>()</div>
<div class="block">Activate all visible on-screen trees.</div>
</section>
</li>
<li>
<section class="detail" id="sortAllTrees()">
<h3>sortAllTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sortAllTrees</span>()</div>
<div class="block">Sorts the nodes in all trees.</div>
</section>
</li>
<li>
<section class="detail" id="updateSortAlwaysFlag()">
<h3>updateSortAlwaysFlag</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateSortAlwaysFlag</span>()</div>
<div class="block">Updates the sort always flag in trees' models.
 If sort flag is true, sorts the trees.</div>
</section>
</li>
<li>
<section class="detail" id="updateSortAlwaysFlagForDifferentTrees()">
<h3>updateSortAlwaysFlagForDifferentTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateSortAlwaysFlagForDifferentTrees</span>()</div>
<div class="block">Updates the sort always flag in trees' models.
 If sort flag is true, sorts tress that had different flag.</div>
</section>
</li>
<li>
<section class="detail" id="reInitTrees()">
<h3>reInitTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reInitTrees</span>()</div>
<div class="block">ReInit browser trees</div>
</section>
</li>
<li>
<section class="detail" id="updateBrowser(boolean,java.lang.String)">
<h3>updateBrowser</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateBrowser</span><wbr/><span class="parameters">(boolean updateOnlyDirty,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Updates the nodes in all trees. Updates documentation panel also.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>updateOnlyDirty</code> - true if only dirty nodes will be updated. on false all nodes will be updated</dd>
<dd><code>group</code> - trees group</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateBrowser(boolean)">
<h3>updateBrowser</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateBrowser</span><wbr/><span class="parameters">(boolean updateOnlyDirty)</span></div>
</section>
</li>
<li>
<section class="detail" id="decorateBrowser()">
<h3>decorateBrowser</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">decorateBrowser</span>()</div>
<div class="block">changes browser's trees decoration</div>
</section>
</li>
<li>
<section class="detail" id="getDocPanel()">
<h3>getDocPanel</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.browser.BrowserDocumentationPanel</span> <span class="element-name">getDocPanel</span>()</div>
<div class="block">Returns documentation panel.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>documentation panel.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOverviewPanel()">
<h3>getOverviewPanel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.diagramoverview.DiagramOverviewPanel</span> <span class="element-name">getOverviewPanel</span>()</div>
<div class="block">Returns zoom panel.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>zoom panel.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQPanel()">
<h3>getQPanel</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.properties.qproperties.ui.QPropertiesPanel</span> <span class="element-name">getQPanel</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getInheritanceTree()">
<h3>getInheritanceTree</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="InheritanceTree.html" title="class in com.nomagic.magicdraw.ui.browser">InheritanceTree</a></span> <span class="element-name">getInheritanceTree</span>()</div>
<div class="block">Returns inheritance tree if it exists, otherwise null</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>inheritance tree.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLockViewTree()">
<h3>getLockViewTree</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../teamwork2/ui/LockViewTree.html" title="class in com.nomagic.magicdraw.teamwork2.ui">LockViewTree</a></span> <span class="element-name">getLockViewTree</span>()</div>
<div class="block">Returns Lock view tree.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>lock view tree.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastActiveTree(java.lang.String)">
<h3>getLastActiveTree</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></span> <span class="element-name">getLastActiveTree</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
</section>
</li>
<li>
<section class="detail" id="getContainmentTree()">
<h3>getContainmentTree</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="ContainmentTree.html" title="class in com.nomagic.magicdraw.ui.browser">ContainmentTree</a></span> <span class="element-name">getContainmentTree</span>()</div>
<div class="block">Returns containment tree.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>containment tree.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramsTree()">
<h3>getDiagramsTree</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="DiagramsTree.html" title="class in com.nomagic.magicdraw.ui.browser">DiagramsTree</a></span> <span class="element-name">getDiagramsTree</span>()</div>
<div class="block">Returns diagrams tree.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagrams tree.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensionsTree()">
<h3>getExtensionsTree</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ExtensionsTree.html" title="class in com.nomagic.magicdraw.ui.browser">ExtensionsTree</a></span> <span class="element-name">getExtensionsTree</span>()</div>
<div class="block">Returns extensions tree.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>extensions tree.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensionsTree(boolean)">
<h3>getExtensionsTree</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ExtensionsTree.html" title="class in com.nomagic.magicdraw.ui.browser">ExtensionsTree</a></span> <span class="element-name">getExtensionsTree</span><wbr/><span class="parameters">(boolean addIfNotExists)</span></div>
<div class="block">Returns extensions tree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>addIfNotExists</code> - add tree if not exists and it is allowed to have extension tree</dd>
<dt>Returns:</dt>
<dd>extensions tree.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSearchResultsTree()">
<h3>getSearchResultsTree</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="SearchResultsTree.html" title="class in com.nomagic.magicdraw.ui.browser">SearchResultsTree</a></span> <span class="element-name">getSearchResultsTree</span>()</div>
<div class="block">Returns last active or newly added search results tree.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>search results tree.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSearchResultsTree(boolean)">
<h3>getSearchResultsTree</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="SearchResultsTree.html" title="class in com.nomagic.magicdraw.ui.browser">SearchResultsTree</a></span> <span class="element-name">getSearchResultsTree</span><wbr/><span class="parameters">(boolean addIfNotExists)</span></div>
<div class="block">Returns last active or newly added search results tree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>addIfNotExists</code> - add search result tree if it does not exist</dd>
<dt>Returns:</dt>
<dd>search results tree.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSearchResultsTree()">
<h3>addSearchResultsTree</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="SearchResultsTree.html" title="class in com.nomagic.magicdraw.ui.browser">SearchResultsTree</a></span> <span class="element-name">addSearchResultsTree</span>()</div>
<div class="block">Adds new browser tab tree for search results</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>search results tree</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNodeMap()">
<h3>getNodeMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.browser.BrowserNodeMap</span> <span class="element-name">getNodeMap</span>()</div>
</section>
</li>
<li>
<section class="detail" id="rememberState()">
<h3>rememberState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">rememberState</span>()</div>
<div class="block">Remembers all expanded nodes in all trees.
 Later these expanded nodes can be restored with method  restoreExpandedNodes().</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#restoreState()"><code>restoreState()</code></a></li>
<li><code>TreeStateManager</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="restoreState()">
<h3>restoreState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">restoreState</span>()</div>
<div class="block">Restores all expanded nodes in all trees.
 Method rememberExpandedNodes must be called first.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#rememberState()"><code>rememberState()</code></a></li>
<li><code>TreeStateManager</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTreeExpandStateRestored()">
<h3>isTreeExpandStateRestored</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isTreeExpandStateRestored</span>()</div>
<div class="block">True if expand state is restored, else false.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if expand state is restored, else false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrees()">
<h3>getTrees</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a>&gt;</span> <span class="element-name">getTrees</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of browser trees</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrees(java.lang.String)">
<h3>getTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a>&gt;</span> <span class="element-name">getTrees</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSearchResultTrees()">
<h3>getSearchResultTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="SearchResultsTree.html" title="class in com.nomagic.magicdraw.ui.browser">SearchResultsTree</a>&gt;</span> <span class="element-name">getSearchResultTrees</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getPanels()">
<h3>getPanels</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a>&gt;</span> <span class="element-name">getPanels</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of browser panels.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAllComponentInfo()">
<h3>getAllComponentInfo</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../WindowComponentInfo.html" title="class in com.nomagic.magicdraw.ui">WindowComponentInfo</a>[]</span> <span class="element-name">getAllComponentInfo</span>()</div>
<div class="block">Used in JIDE to create actions for these components</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>info about all windows components related to browser</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTreeActivationHistory()">
<h3>getTreeActivationHistory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a>&gt;</span> <span class="element-name">getTreeActivationHistory</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTreeActivationHistory(java.lang.String)">
<h3>getTreeActivationHistory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a>&gt;</span> <span class="element-name">getTreeActivationHistory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeTreeFromBrowser(com.nomagic.magicdraw.ui.browser.BrowserTabTree,boolean)">
<h3>removeTreeFromBrowser</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeTreeFromBrowser</span><wbr/><span class="parameters">(<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree,
 boolean saveLayout)</span></div>
<div class="block">Remove given tree and also close a window of tree if any</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - tree</dd>
<dd><code>saveLayout</code> - save information about trees layout</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveTreesLayout()">
<h3>saveTreesLayout</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">saveTreesLayout</span>()</div>
<div class="block">Save information about trees layout into project options</div>
</section>
</li>
<li>
<section class="detail" id="removeAllRemovableTrees()">
<h3>removeAllRemovableTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllRemovableTrees</span>()</div>
<div class="block">Removes all removable trees.</div>
</section>
</li>
<li>
<section class="detail" id="removeAllRemovablePanels()">
<h3>removeAllRemovablePanels</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllRemovablePanels</span>()</div>
<div class="block">Removes all removable panels. Removables panels are of type BrowserPanelInfo and have field showByDefault set to true.</div>
</section>
</li>
<li>
<section class="detail" id="getBrowserTreeForNode(com.nomagic.magicdraw.ui.browser.Node)">
<h3>getBrowserTreeForNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></span> <span class="element-name">getBrowserTreeForNode</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node)</span></div>
</section>
</li>
<li>
<section class="detail" id="getBrowserTreeForNode(com.nomagic.magicdraw.ui.browser.Node,java.lang.String)">
<h3>getBrowserTreeForNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></span> <span class="element-name">getBrowserTreeForNode</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
</section>
</li>
<li>
<section class="detail" id="isExtensionTreeAllowed()">
<h3>isExtensionTreeAllowed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExtensionTreeAllowed</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if Extensions tree can be created in a browser</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addBrowserInitializer(com.nomagic.magicdraw.ui.browser.Browser.BrowserInitializer)">
<h3>addBrowserInitializer</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addBrowserInitializer</span><wbr/><span class="parameters">(<a href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser">Browser.BrowserInitializer</a> initializer)</span></div>
<div class="block">Add new browser initializer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>initializer</code> - initializer</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeBrowserInitializer(com.nomagic.magicdraw.ui.browser.Browser.BrowserInitializer)">
<h3>removeBrowserInitializer</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeBrowserInitializer</span><wbr/><span class="parameters">(<a href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser">Browser.BrowserInitializer</a> initializer)</span></div>
<div class="block">Remove browser initializer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>initializer</code> - initializer</dd>
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
