# JAVA OPENAPI: Browser (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/ui/browser/Browser.html
- source_path: `com/nomagic/magicdraw/ui/browser/Browser.html`
- source_sha256: `001c4d714da8d71dd9bc1e693ab3d72a0979059501187afc22cf04b45d466692`
- captured_utc: `2026-07-14T16:55:49.190389+00:00`

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
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
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
`[BrowserTabTree](BrowserTabTree.html)`
`[getActiveTree](#getActiveTree())()`
Returns reference to the active tree.
`[ContainmentTree](ContainmentTree.html)`
`[getContainmentTree](#getContainmentTree())()`
Returns containment tree.
`[DiagramsTree](DiagramsTree.html)`
`[getDiagramsTree](#getDiagramsTree())()`
Returns diagrams tree.
`[ExtensionsTree](ExtensionsTree.html)`
`[getExtensionsTree](#getExtensionsTree())()`
Returns extensions tree.
`[ExtensionsTree](ExtensionsTree.html)`
`[getExtensionsTree](#getExtensionsTree(boolean))(boolean addIfNotExists)`
Returns extensions tree.
`[InheritanceTree](InheritanceTree.html)`
`[getInheritanceTree](#getInheritanceTree())()`
Returns inheritance tree if it exists, otherwise null
`[LockViewTree](../../teamwork2/ui/LockViewTree.html)`
`[getLockViewTree](#getLockViewTree())()`
Returns Lock view tree.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExtendedPanel](../../../ui/ExtendedPanel.html)>`
`[getPanels](#getPanels())()`

`[SearchResultsTree](SearchResultsTree.html)`
`[getSearchResultsTree](#getSearchResultsTree())()`
Returns last active or newly added search results tree.
`[SearchResultsTree](SearchResultsTree.html)`
`[getSearchResultsTree](#getSearchResultsTree(boolean))(boolean addIfNotExists)`
Returns last active or newly added search results tree.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BrowserTabTree](BrowserTabTree.html)>`
`[getTrees](#getTrees())()`

`static void`
`[removeBrowserInitializer](#removeBrowserInitializer(com.nomagic.magicdraw.ui.browser.Browser.BrowserInitializer))([Browser.BrowserInitializer](Browser.BrowserInitializer.html) initializer)`
Remove browser initializer.
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
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
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
getActiveTree
@CheckForNull
@OpenApipublic [BrowserTabTree](BrowserTabTree.html) getActiveTree()
Returns reference to the active tree.
Returns:
active tree.
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
getTrees
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BrowserTabTree](BrowserTabTree.html)> getTrees()
Returns:
a list of browser trees
getPanels
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExtendedPanel](../../../ui/ExtendedPanel.html)> getPanels()
Returns:
a list of browser panels.
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addBrowserInitializer(com.nomagic.magicdraw.ui.browser.Browser.BrowserInitializer)">addBrowserInitializer</a><wbr/>(<a href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser">Browser.BrowserInitializer</a> initializer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Add new browser initializer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPanel(com.nomagic.ui.ExtendedPanel)">addPanel</a><wbr/>(<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a> panel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a new browser panel.Should be called during browser initialization only.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPanel(com.nomagic.ui.ExtendedPanel,int)">addPanel</a><wbr/>(<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a> panel,
 int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a new browser panel.Should be called during browser initialization only.</div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveTree()">getActiveTree</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns reference to the active tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ContainmentTree.html" title="class in com.nomagic.magicdraw.ui.browser">ContainmentTree</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContainmentTree()">getContainmentTree</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns containment tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DiagramsTree.html" title="class in com.nomagic.magicdraw.ui.browser">DiagramsTree</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramsTree()">getDiagramsTree</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns diagrams tree.</div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../teamwork2/ui/LockViewTree.html" title="class in com.nomagic.magicdraw.teamwork2.ui">LockViewTree</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLockViewTree()">getLockViewTree</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns Lock view tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPanels()">getPanels</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SearchResultsTree.html" title="class in com.nomagic.magicdraw.ui.browser">SearchResultsTree</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSearchResultsTree()">getSearchResultsTree</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns last active or newly added search results tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SearchResultsTree.html" title="class in com.nomagic.magicdraw.ui.browser">SearchResultsTree</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSearchResultsTree(boolean)">getSearchResultsTree</a><wbr/>(boolean addIfNotExists)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns last active or newly added search results tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTrees()">getTrees</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeBrowserInitializer(com.nomagic.magicdraw.ui.browser.Browser.BrowserInitializer)">removeBrowserInitializer</a><wbr/>(<a href="Browser.BrowserInitializer.html" title="interface in com.nomagic.magicdraw.ui.browser">Browser.BrowserInitializer</a> initializer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Remove browser initializer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePanel(com.nomagic.ui.ExtendedPanel)">removePanel</a><wbr/>(<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a> panel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes browser panel.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">removeTree</a><wbr/>(<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a tree from the browser.Should be called during browser initialization only.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeTree(com.nomagic.magicdraw.ui.browser.BrowserTabTree,boolean)">removeTree</a><wbr/>(<a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree,
 boolean saveLayout)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a tree from the browser.Should be called during browser initialization only.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
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
