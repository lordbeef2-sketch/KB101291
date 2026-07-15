# JAVA OPENAPI: ActionsProvider (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/actions/ActionsProvider.html
- source_path: `com/nomagic/magicdraw/actions/ActionsProvider.html`
- source_sha256: `b97874a3f0fb35b87fba13cd18ed69a981c5aa23db64c8ee2b3aedd7f21e1eaf`
- captured_utc: `2026-07-14T16:51:00.992933+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.actions](package-summary.html)

## Class ActionsProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.actions.ActionsProvider

@OpenApipublic final classActionsProvider
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The singleton class used for accessing actions in different parts (diagrams, browsers, main menu and etc.) of MagicDraw application.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[ActionsManager](../../actions/ActionsManager.html)`
`[getCommandBarActions](#getCommandBarActions(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) diagram)`
Returns actions of command bar for given diagram.
`static [ActionsManager](../../actions/ActionsManager.html)`
`[getContainmentBrowserContextActions](#getContainmentBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree))([BrowserTabTree](../ui/browser/BrowserTabTree.html) tree)`
Returns context actions manager for containment browser.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getContainmentBrowserShortcutsActions](#getContainmentBrowserShortcutsActions())()`
Returns actions manager for containment browser shortcuts.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getCreateDiagramDialogActions](#getCreateDiagramDialogActions())()`
Creates, configures and returns diagram creation actions to display in Create Diagram dialog (action in main menu and main toolbar)
`[ActionsCreator](ActionsCreator.html)`
`[getCreator](#getCreator())()`
Returns instance of actions creator.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getDiagramCommandBarActions](#getDiagramCommandBarActions(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)`
Returns actions of command bar for given diagram type.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getDiagramContextActions](#getDiagramContextActions(java.lang.String,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement%5B%5D,com.nomagic.magicdraw.uml.symbols.PresentationElement))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) diagram,
 [PresentationElement](../uml/symbols/PresentationElement.html)[] selected,
 [PresentationElement](../uml/symbols/PresentationElement.html) requester)`
Returns context AM for given diagram type.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getDiagramContextToolbarActions](#getDiagramContextToolbarActions(java.lang.String,com.nomagic.magicdraw.uml.symbols.PresentationElement))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [PresentationElement](../uml/symbols/PresentationElement.html) requester)`
Returns context AM for given diagram type.
`static [ActionsManager](../../actions/ActionsManager.html)`
`[getDiagramsBrowserContextActions](#getDiagramsBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree))([BrowserTabTree](../ui/browser/BrowserTabTree.html) tree)`
Returns context actions manager for diagrams browser.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getDiagramsBrowserShortcutsActions](#getDiagramsBrowserShortcutsActions())()`
Returns actions manager for diagrams browser shortcuts.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getDiagramShortcutActions](#getDiagramShortcutActions(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) diagram)`
Returns AM for given diagram
`[ActionsManager](../../actions/ActionsManager.html)`
`[getDiagramShortcutActions](#getDiagramShortcutActions(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)`
Returns AM for given diagram type shortcuts.
`[DiagramToolbarConfiguration](../ui/DiagramToolbarConfiguration.html)`
`[getDiagramToolbarConfiguration](#getDiagramToolbarConfiguration(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) diagram)`
Returns AM for diagram toolbar.
`[DiagramToolbarConfiguration](../ui/DiagramToolbarConfiguration.html)`
`[getDiagramToolbarConfiguration](#getDiagramToolbarConfiguration(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)`
Returns AM for diagram toolbar.
`static [ActionsManager](../../actions/ActionsManager.html)`
`[getExtensionsBrowserContextActions](#getExtensionsBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree))([BrowserTabTree](../ui/browser/BrowserTabTree.html) tree)`
Returns context actions manager for containment browser.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getExtensionsBrowserShortcutsActions](#getExtensionsBrowserShortcutsActions())()`
Returns shortcuts actions manager for inheritance browser.
`static [ActionsManager](../../actions/ActionsManager.html)`
`[getInheritanceBrowserContextActions](#getInheritanceBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree))([BrowserTabTree](../ui/browser/BrowserTabTree.html) tree)`
Returns context actions manager for inheritance browser.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getInheritanceBrowserShortcutsActions](#getInheritanceBrowserShortcutsActions())()`
Returns shortcuts actions manager for inheritance browser.
`static [ActionsProvider](ActionsProvider.html)`
`[getInstance](#getInstance())()`
Returns single instance of this class.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getLockViewBrowserShortcutsActions](#getLockViewBrowserShortcutsActions())()`
Returns shortcuts actions manager for inheritance browser.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getMainMenuActions](#getMainMenuActions())()`
Returns actions manager for main menu actions.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getMainShortcutsActions](#getMainShortcutsActions())()`
Returns actions manager for main shortcuts.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getMainToolbarActions](#getMainToolbarActions())()`
Returns manager with actions for main toolbar.
`static [ActionsManager](../../actions/ActionsManager.html)`
`[getSearchBrowserContextActions](#getSearchBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree))([BrowserTabTree](../ui/browser/BrowserTabTree.html) tree)`
Returns context actions manager for search browser.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getSearchBrowserShortcutsActions](#getSearchBrowserShortcutsActions())()`
Returns shortcuts actions manager for search browser.
`[ActionsManager](../../actions/ActionsManager.html)`
`[getTargetElementAMActions](#getTargetElementAMActions(java.lang.String,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [PresentationElement](../uml/symbols/PresentationElement.html) requester,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pathActionID)`
Returns context AM for given diagram type.
`void`
`[registerAction](#registerAction(com.nomagic.actions.NMAction))([NMAction](../../actions/NMAction.html) action)`
Registers the action as available in application - other components (such as Perspectives) should know what actions are available. 

**Action id must be stable/constant,
 It is not necessary to use the same action instance used when configuring appropriate menu/toolbar.**
`void`
`[unregisterAction](#unregisterAction(com.nomagic.actions.NMAction))([NMAction](../../actions/NMAction.html) action)`
Remove the action as available in application.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
@OpenApipublic static [ActionsProvider](ActionsProvider.html) getInstance()
Returns single instance of this class.
Returns:
the instance of ActionsProvider.
getDiagramContextActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getDiagramContextActions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) diagram,
 [PresentationElement](../uml/symbols/PresentationElement.html)[] selected,
 @CheckForNull
 [PresentationElement](../uml/symbols/PresentationElement.html) requester)
Returns context AM for given diagram type.
Parameters:
`diagramType` - diagram type
`diagram` - the given diagram.
`selected` - array of selected symbols.
`requester` - symbol which requests actions, can be null if requester is diagram.
Returns:
manager with actions.
getTargetElementAMActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getTargetElementAMActions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [PresentationElement](../uml/symbols/PresentationElement.html) requester,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pathActionID)
Returns context AM for given diagram type.
Parameters:
`diagramType` - diagram type
`requester` - symbol which requests actions, can be null if requester is diagram.
`pathActionID` - path action id
Returns:
manager with actions.
getDiagramContextToolbarActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getDiagramContextToolbarActions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [PresentationElement](../uml/symbols/PresentationElement.html) requester)
Returns context AM for given diagram type.
Parameters:
`diagramType` - diagram type
`requester` - symbol which requests actions, can be null if requester is diagram.
Returns:
manager with actions.
getDiagramToolbarConfiguration
@OpenApipublic [DiagramToolbarConfiguration](../ui/DiagramToolbarConfiguration.html) getDiagramToolbarConfiguration([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)
Returns AM for diagram toolbar.
Parameters:
`diagramType` - diagram type
Returns:
DiagramToolbarConfiguration object for specified diagram type.
getDiagramToolbarConfiguration
@OpenApipublic [DiagramToolbarConfiguration](../ui/DiagramToolbarConfiguration.html) getDiagramToolbarConfiguration([AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) diagram)
Returns AM for diagram toolbar.
Parameters:
`diagram` - diagram
Returns:
DiagramToolbarConfiguration object for specified diagram
getDiagramCommandBarActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getDiagramCommandBarActions(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)
Returns actions of command bar for given diagram type.
Parameters:
`diagramType` - diagram type
Returns:
manager with actions.
getCommandBarActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getCommandBarActions([AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) diagram)
Returns actions of command bar for given diagram.
Parameters:
`diagram` - diagram
Returns:
manager with actions
getDiagramShortcutActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getDiagramShortcutActions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)
Returns AM for given diagram type shortcuts.
Parameters:
`diagramType` - diagram type
Returns:
manager with actions.
getDiagramShortcutActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getDiagramShortcutActions([AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) diagram)
Returns AM for given diagram
Parameters:
`diagram` - diagram
Returns:
manager with actions
getMainMenuActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getMainMenuActions()
Returns actions manager for main menu actions.
Returns:
manager with actions.
getMainToolbarActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getMainToolbarActions()
Returns manager with actions for main toolbar.
Returns:
manager with main toolbar actions.
getMainShortcutsActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getMainShortcutsActions()
Returns actions manager for main shortcuts.
Returns:
manager with actions.
getContainmentBrowserContextActions
@OpenApipublic static [ActionsManager](../../actions/ActionsManager.html) getContainmentBrowserContextActions([BrowserTabTree](../ui/browser/BrowserTabTree.html) tree)
Returns context actions manager for containment browser.
Parameters:
`tree` - instance of tree.
Returns:
manager with actions.
getExtensionsBrowserContextActions
@OpenApipublic static [ActionsManager](../../actions/ActionsManager.html) getExtensionsBrowserContextActions([BrowserTabTree](../ui/browser/BrowserTabTree.html) tree)
Returns context actions manager for containment browser.
Parameters:
`tree` - instance of tree.
Returns:
manager with actions.
getSearchBrowserContextActions
@OpenApipublic static [ActionsManager](../../actions/ActionsManager.html) getSearchBrowserContextActions([BrowserTabTree](../ui/browser/BrowserTabTree.html) tree)
Returns context actions manager for search browser.
Parameters:
`tree` - instance of tree.
Returns:
manager with actions.
getDiagramsBrowserContextActions
@OpenApipublic static [ActionsManager](../../actions/ActionsManager.html) getDiagramsBrowserContextActions([BrowserTabTree](../ui/browser/BrowserTabTree.html) tree)
Returns context actions manager for diagrams browser.
Parameters:
`tree` - instance of tree.
Returns:
manager with actions.
getInheritanceBrowserContextActions
@OpenApipublic static [ActionsManager](../../actions/ActionsManager.html) getInheritanceBrowserContextActions([BrowserTabTree](../ui/browser/BrowserTabTree.html) tree)
Returns context actions manager for inheritance browser.
Parameters:
`tree` - instance of tree.
Returns:
manager with actions.
getContainmentBrowserShortcutsActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getContainmentBrowserShortcutsActions()
Returns actions manager for containment browser shortcuts.
Returns:
manager with actions.
getDiagramsBrowserShortcutsActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getDiagramsBrowserShortcutsActions()
Returns actions manager for diagrams browser shortcuts.
Returns:
manager with actions.
getInheritanceBrowserShortcutsActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getInheritanceBrowserShortcutsActions()
Returns shortcuts actions manager for inheritance browser.
Returns:
manager with actions.
getLockViewBrowserShortcutsActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getLockViewBrowserShortcutsActions()
Returns shortcuts actions manager for inheritance browser.
Returns:
manager with actions.
getExtensionsBrowserShortcutsActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getExtensionsBrowserShortcutsActions()
Returns shortcuts actions manager for inheritance browser.
Returns:
manager with actions.
getSearchBrowserShortcutsActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getSearchBrowserShortcutsActions()
Returns shortcuts actions manager for search browser.
Returns:
manager with actions.
getCreator
@OpenApipublic [ActionsCreator](ActionsCreator.html) getCreator()
Returns instance of actions creator.
Returns:
the actions creator.
getCreateDiagramDialogActions
@OpenApipublic [ActionsManager](../../actions/ActionsManager.html) getCreateDiagramDialogActions()
Creates, configures and returns diagram creation actions to display in Create Diagram dialog (action in main menu and main toolbar)
Returns:
manager with diagram creation actions
registerAction
@OpenApipublic void registerAction([NMAction](../../actions/NMAction.html) action)
Registers the action as available in application - other components (such as Perspectives) should know what actions are available. 

**Action id must be stable/constant,
It is not necessary to use the same action instance used when configuring appropriate menu/toolbar.**
Parameters:
`action` - action to register.
See Also:
[`unregisterAction(com.nomagic.actions.NMAction)`](#unregisterAction(com.nomagic.actions.NMAction))
unregisterAction
@OpenApipublic void unregisterAction([NMAction](../../actions/NMAction.html) action)
Remove the action as available in application.
Parameters:
`action` - action to remove.
See Also:
[`registerAction(com.nomagic.actions.NMAction)`](#registerAction(com.nomagic.actions.NMAction))

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.actions</a></div>
<h1 class="title" title="Class ActionsProvider">Class ActionsProvider</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.actions.ActionsProvider</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">ActionsProvider</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The singleton class used for accessing actions in different parts (diagrams, browsers, main menu and etc.) of MagicDraw application.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCommandBarActions(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getCommandBarActions</a><wbr/>(<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns actions of command bar for given diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getContainmentBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">getContainmentBrowserContextActions</a><wbr/>(<a href="../ui/browser/BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns context actions manager for containment browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContainmentBrowserShortcutsActions()">getContainmentBrowserShortcutsActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns actions manager for containment browser shortcuts.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreateDiagramDialogActions()">getCreateDiagramDialogActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates, configures and returns diagram creation actions to display in Create Diagram dialog (action in main menu and main toolbar)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsCreator.html" title="class in com.nomagic.magicdraw.actions">ActionsCreator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreator()">getCreator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns instance of actions creator.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramCommandBarActions(java.lang.String)">getDiagramCommandBarActions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns actions of command bar for given diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramContextActions(java.lang.String,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement%5B%5D,com.nomagic.magicdraw.uml.symbols.PresentationElement)">getDiagramContextActions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram,
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>[] selected,
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> requester)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns context AM for given diagram type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramContextToolbarActions(java.lang.String,com.nomagic.magicdraw.uml.symbols.PresentationElement)">getDiagramContextToolbarActions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> requester)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns context AM for given diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramsBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">getDiagramsBrowserContextActions</a><wbr/>(<a href="../ui/browser/BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns context actions manager for diagrams browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramsBrowserShortcutsActions()">getDiagramsBrowserShortcutsActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns actions manager for diagrams browser shortcuts.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramShortcutActions(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getDiagramShortcutActions</a><wbr/>(<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns AM for given diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramShortcutActions(java.lang.String)">getDiagramShortcutActions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns AM for given diagram type shortcuts.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ui/DiagramToolbarConfiguration.html" title="class in com.nomagic.magicdraw.ui">DiagramToolbarConfiguration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramToolbarConfiguration(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getDiagramToolbarConfiguration</a><wbr/>(<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns AM for diagram toolbar.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ui/DiagramToolbarConfiguration.html" title="class in com.nomagic.magicdraw.ui">DiagramToolbarConfiguration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramToolbarConfiguration(java.lang.String)">getDiagramToolbarConfiguration</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns AM for diagram toolbar.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensionsBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">getExtensionsBrowserContextActions</a><wbr/>(<a href="../ui/browser/BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns context actions manager for containment browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensionsBrowserShortcutsActions()">getExtensionsBrowserShortcutsActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns shortcuts actions manager for inheritance browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInheritanceBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">getInheritanceBrowserContextActions</a><wbr/>(<a href="../ui/browser/BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns context actions manager for inheritance browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInheritanceBrowserShortcutsActions()">getInheritanceBrowserShortcutsActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns shortcuts actions manager for inheritance browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ActionsProvider.html" title="class in com.nomagic.magicdraw.actions">ActionsProvider</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns single instance of this class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLockViewBrowserShortcutsActions()">getLockViewBrowserShortcutsActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns shortcuts actions manager for inheritance browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMainMenuActions()">getMainMenuActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns actions manager for main menu actions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMainShortcutsActions()">getMainShortcutsActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns actions manager for main shortcuts.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMainToolbarActions()">getMainToolbarActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns manager with actions for main toolbar.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSearchBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">getSearchBrowserContextActions</a><wbr/>(<a href="../ui/browser/BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns context actions manager for search browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSearchBrowserShortcutsActions()">getSearchBrowserShortcutsActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns shortcuts actions manager for search browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetElementAMActions(java.lang.String,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">getTargetElementAMActions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> requester,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pathActionID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns context AM for given diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerAction(com.nomagic.actions.NMAction)">registerAction</a><wbr/>(<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers the action as available in application - other components (such as Perspectives) should know what actions are available.<br/>
<strong>
 Action id must be stable/constant,
 It is not necessary to use the same action instance used when configuring appropriate  menu/toolbar.
 </strong></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#unregisterAction(com.nomagic.actions.NMAction)">unregisterAction</a><wbr/>(<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove the action as available in application.</div>
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
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ActionsProvider.html" title="class in com.nomagic.magicdraw.actions">ActionsProvider</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Returns single instance of this class.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the instance of ActionsProvider.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContextActions(java.lang.String,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement[],com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getDiagramContextActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getDiagramContextActions</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram,
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>[] selected,
 @CheckForNull
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> requester)</span></div>
<div class="block">Returns context AM for given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>diagram</code> - the given diagram.</dd>
<dd><code>selected</code> - array of selected symbols.</dd>
<dd><code>requester</code> - symbol which requests actions, can be null if requester is diagram.</dd>
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetElementAMActions(java.lang.String,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">
<h3>getTargetElementAMActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getTargetElementAMActions</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> requester,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pathActionID)</span></div>
<div class="block">Returns context AM for given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>requester</code> - symbol which requests actions, can be null if requester is diagram.</dd>
<dd><code>pathActionID</code> - path action id</dd>
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContextToolbarActions(java.lang.String,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getDiagramContextToolbarActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getDiagramContextToolbarActions</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> requester)</span></div>
<div class="block">Returns context AM for given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>requester</code> - symbol which requests actions, can be null if requester is diagram.</dd>
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramToolbarConfiguration(java.lang.String)">
<h3>getDiagramToolbarConfiguration</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../ui/DiagramToolbarConfiguration.html" title="class in com.nomagic.magicdraw.ui">DiagramToolbarConfiguration</a></span> <span class="element-name">getDiagramToolbarConfiguration</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="block">Returns AM for diagram toolbar.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dt>Returns:</dt>
<dd>DiagramToolbarConfiguration object for specified diagram type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramToolbarConfiguration(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>getDiagramToolbarConfiguration</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../ui/DiagramToolbarConfiguration.html" title="class in com.nomagic.magicdraw.ui">DiagramToolbarConfiguration</a></span> <span class="element-name">getDiagramToolbarConfiguration</span><wbr/><span class="parameters">(<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</span></div>
<div class="block">Returns AM for diagram toolbar.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram</dd>
<dt>Returns:</dt>
<dd>DiagramToolbarConfiguration object for specified diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramCommandBarActions(java.lang.String)">
<h3>getDiagramCommandBarActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getDiagramCommandBarActions</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="block">Returns actions of command bar for given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCommandBarActions(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>getCommandBarActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getCommandBarActions</span><wbr/><span class="parameters">(<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</span></div>
<div class="block">Returns actions of command bar for given diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram</dd>
<dt>Returns:</dt>
<dd>manager with actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramShortcutActions(java.lang.String)">
<h3>getDiagramShortcutActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getDiagramShortcutActions</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="block">Returns AM for given diagram type shortcuts.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramShortcutActions(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>getDiagramShortcutActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getDiagramShortcutActions</span><wbr/><span class="parameters">(<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</span></div>
<div class="block">Returns AM for given diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram</dd>
<dt>Returns:</dt>
<dd>manager with actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMainMenuActions()">
<h3>getMainMenuActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getMainMenuActions</span>()</div>
<div class="block">Returns actions manager for main menu actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMainToolbarActions()">
<h3>getMainToolbarActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getMainToolbarActions</span>()</div>
<div class="block">Returns manager with actions for main toolbar.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager with main toolbar actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMainShortcutsActions()">
<h3>getMainShortcutsActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getMainShortcutsActions</span>()</div>
<div class="block">Returns actions manager for main shortcuts.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContainmentBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">
<h3>getContainmentBrowserContextActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getContainmentBrowserContextActions</span><wbr/><span class="parameters">(<a href="../ui/browser/BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree)</span></div>
<div class="block">Returns context actions manager for containment browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - instance of tree.</dd>
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensionsBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">
<h3>getExtensionsBrowserContextActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getExtensionsBrowserContextActions</span><wbr/><span class="parameters">(<a href="../ui/browser/BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree)</span></div>
<div class="block">Returns context actions manager for containment browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - instance of tree.</dd>
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSearchBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">
<h3>getSearchBrowserContextActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getSearchBrowserContextActions</span><wbr/><span class="parameters">(<a href="../ui/browser/BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree)</span></div>
<div class="block">Returns context actions manager for search browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - instance of tree.</dd>
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramsBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">
<h3>getDiagramsBrowserContextActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getDiagramsBrowserContextActions</span><wbr/><span class="parameters">(<a href="../ui/browser/BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree)</span></div>
<div class="block">Returns context actions manager for diagrams browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - instance of tree.</dd>
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInheritanceBrowserContextActions(com.nomagic.magicdraw.ui.browser.BrowserTabTree)">
<h3>getInheritanceBrowserContextActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getInheritanceBrowserContextActions</span><wbr/><span class="parameters">(<a href="../ui/browser/BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a> tree)</span></div>
<div class="block">Returns context actions manager for inheritance browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - instance of tree.</dd>
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContainmentBrowserShortcutsActions()">
<h3>getContainmentBrowserShortcutsActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getContainmentBrowserShortcutsActions</span>()</div>
<div class="block">Returns actions manager for containment browser shortcuts.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramsBrowserShortcutsActions()">
<h3>getDiagramsBrowserShortcutsActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getDiagramsBrowserShortcutsActions</span>()</div>
<div class="block">Returns actions manager for diagrams browser shortcuts.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInheritanceBrowserShortcutsActions()">
<h3>getInheritanceBrowserShortcutsActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getInheritanceBrowserShortcutsActions</span>()</div>
<div class="block">Returns shortcuts actions manager for inheritance browser.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLockViewBrowserShortcutsActions()">
<h3>getLockViewBrowserShortcutsActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getLockViewBrowserShortcutsActions</span>()</div>
<div class="block">Returns shortcuts actions manager for inheritance browser.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensionsBrowserShortcutsActions()">
<h3>getExtensionsBrowserShortcutsActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getExtensionsBrowserShortcutsActions</span>()</div>
<div class="block">Returns shortcuts actions manager for inheritance browser.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSearchBrowserShortcutsActions()">
<h3>getSearchBrowserShortcutsActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getSearchBrowserShortcutsActions</span>()</div>
<div class="block">Returns shortcuts actions manager for search browser.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager with actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreator()">
<h3>getCreator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="ActionsCreator.html" title="class in com.nomagic.magicdraw.actions">ActionsCreator</a></span> <span class="element-name">getCreator</span>()</div>
<div class="block">Returns instance of actions creator.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the actions creator.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreateDiagramDialogActions()">
<h3>getCreateDiagramDialogActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getCreateDiagramDialogActions</span>()</div>
<div class="block">Creates, configures and returns diagram creation actions to display in Create Diagram dialog (action in main menu and main toolbar)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager with diagram creation actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerAction(com.nomagic.actions.NMAction)">
<h3>registerAction</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerAction</span><wbr/><span class="parameters">(<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Registers the action as available in application - other components (such as Perspectives) should know what actions are available.<br/>
<strong><ul>
<li>Action id must be stable/constant,</li>
<li>It is not necessary to use the same action instance used when configuring appropriate  menu/toolbar.</li>
</ul></strong></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - action to register.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#unregisterAction(com.nomagic.actions.NMAction)"><code>unregisterAction(com.nomagic.actions.NMAction)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregisterAction(com.nomagic.actions.NMAction)">
<h3>unregisterAction</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">unregisterAction</span><wbr/><span class="parameters">(<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Remove the action as available in application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - action to remove.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#registerAction(com.nomagic.actions.NMAction)"><code>registerAction(com.nomagic.actions.NMAction)</code></a></li>
</ul>
</dd>
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
