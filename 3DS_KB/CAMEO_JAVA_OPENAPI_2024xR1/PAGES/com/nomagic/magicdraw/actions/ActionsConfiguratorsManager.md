# JAVA OPENAPI: ActionsConfiguratorsManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/actions/ActionsConfiguratorsManager.html
- source_path: `com/nomagic/magicdraw/actions/ActionsConfiguratorsManager.html`
- source_sha256: `90944e9d6fe1ca2a212765a3849b2084bc2f6f1f1be0e22840ca6a86a3c1c56c`
- captured_utc: `2026-07-14T16:51:01.132936+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.actions](package-summary.html)

## Class ActionsConfiguratorsManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.actions.ActionsConfiguratorsManager

@OpenApipublic final classActionsConfiguratorsManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The singleton class for adding/removing configurations of actions managers in MagicDraw application.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[addAnyDiagramCommandBarConfigurator](#addAnyDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Registers configurator for any type of diagrams.
`void`
`[addAnyDiagramShortcutsConfigurator](#addAnyDiagramShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds configurator for any type diagram.
`void`
`[addBaseDiagramContextConfigurator](#addBaseDiagramContextConfigurator(java.lang.String,com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramContextAMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramContextAMConfigurator configurator)`
Adds new diagram context configurator for given diagram type.
`void`
`[addBaseDiagramContextConfigurator](#addBaseDiagramContextConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextAMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextAMConfigurator](DiagramContextAMConfigurator.html) configurator)`
Adds new diagram context configurator for given diagram type.
`void`
`[addContainmentBrowserContextConfigurator](#addContainmentBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator))([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)`
Adds new context configurator to containment browser.
`void`
`[addContainmentBrowserShortcutsConfigurator](#addContainmentBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds new shortcuts' configurator to containment browser.
`void`
`[addContainmentBrowserToolbarConfigurator](#addContainmentBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator))([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)`
Adds new Toolbar configurator to containment browser.
`void`
`[addCreateDiagramDialogConfigurator](#addCreateDiagramDialogConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds configurator to configure actions inside the dialog which opens when action in main menu or toolbar "Create Diagram" is executed.
`void`
`[addCustomizableShortcutsConfigurator](#addCustomizableShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds configurator for main shortcuts.
`void`
`[addDiagramCommandBarConfigurator](#addDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Deprecated.
deprecated because of too generic name.
`void`
`[addDiagramCommandBarConfigurator](#addDiagramCommandBarConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Add configurator for diagram of given type.
`void`
`[addDiagramContextConfigurator](#addDiagramContextConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextAMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextAMConfigurator](DiagramContextAMConfigurator.html) configurator)`
Adds new diagram context configurator for given diagram type.
`void`
`[addDiagramContextToolbarConfigurator](#addDiagramContextToolbarConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextToolbarAMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextToolbarAMConfigurator](DiagramContextToolbarAMConfigurator.html) configurator)`
Adds new toolbar configurator for given diagram type.
`void`
`[addDiagramNavigationConfigurator](#addDiagramNavigationConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds configurator to diagram navigation toolbar.
`void`
`[addDiagramsBrowserContextConfigurator](#addDiagramsBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator))([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)`
Adds new context configurator to diagrams browser.
`void`
`[addDiagramsBrowserShortcutsConfigurator](#addDiagramsBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds new shortcuts' configurator to diagrams browser.
`void`
`[addDiagramsBrowserToolbarConfigurator](#addDiagramsBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator))([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)`
Adds new Toolbar configurator to diagrams browser.
`void`
`[addDiagramShortcutsConfigurator](#addDiagramShortcutsConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds new shortcuts' configurator for given diagram type.
`void`
`[addDiagramToolbarActionsProvider](#addDiagramToolbarActionsProvider(java.lang.String,com.nomagic.magicdraw.ui.actions.CustomizableDiagramToolbarActionsProvider))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [CustomizableDiagramToolbarActionsProvider](../ui/actions/CustomizableDiagramToolbarActionsProvider.html) provider)`
Adds new toolbar provider for given diagram type.
`void`
`[addDiagramToolbarConfigurator](#addDiagramToolbarConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds new toolbar configurator for given diagram type.
`static void`
`[addDialogActionsConfigurator](#addDialogActionsConfigurator(java.lang.String,com.nomagic.actions.ActionsManager,com.nomagic.actions.AMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) categoryID,
 [ActionsManager](../../actions/ActionsManager.html) manager,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds configurator to configure actions inside specific popup dialog which constructs its actions only when respective popup menu item is clicked.
`void`
`[addExtensionsBrowserContextConfigurator](#addExtensionsBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator))([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)`
Adds new context configurator to extensions browser.
`void`
`[addExtensionsBrowserShortcutsConfigurator](#addExtensionsBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds new shortcuts' configurator to extensions browser.
`void`
`[addExtensionsBrowserToolbarConfigurator](#addExtensionsBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator))([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)`
Adds new Toolbar configurator to extensions browser.
`void`
`[addInheritanceBrowserContextConfigurator](#addInheritanceBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator))([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)`
Adds new context configurator to inheritance browser.
`void`
`[addInheritanceBrowserShortcutsConfigurator](#addInheritanceBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds new shortcuts' configurator to inheritance browser.
`void`
`[addInheritanceBrowserToolbarConfigurator](#addInheritanceBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator))([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)`
Adds new context configurator to inheritance browser.
`void`
`[addLockViewBrowserContextConfigurator](#addLockViewBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator))([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)`
Adds new context configurator to lock view browser.
`void`
`[addLockViewBrowserShortcutsConfigurator](#addLockViewBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds new shortcuts' configurator to lock view browser.
`void`
`[addLockViewBrowserToolbarConfigurator](#addLockViewBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator))([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)`
Adds new context configurator to inheritance browser.
`void`
`[addMainMenuConfigurator](#addMainMenuConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds configurator to main menu.
`void`
`[addMainShortcutsConfigurator](#addMainShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds configurator for main shortcuts.
`void`
`[addMainToolbarConfigurator](#addMainToolbarConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds configurator to main toolbar.
`void`
`[addSearchBrowserContextConfigurator](#addSearchBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator))([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)`
Adds new context configurator for search browser.
`void`
`[addSearchBrowserShortcutsConfigurator](#addSearchBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds new shortcuts' configurator to search browser.
`void`
`[addSearchBrowserToolbarConfigurator](#addSearchBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator))([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)`
Adds new Toolbar configurator for search browser.
`void`
`[addSymbolDiagramCommandBarConfigurator](#addSymbolDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Add configurator for any type of "symbol" diagrams Those do not include tables, maps, matrices, etc.
`void`
`[addSymbolDiagramShortcutsConfigurator](#addSymbolDiagramShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Adds configurator for any "symbol" diagram.
`void`
`[addTargetElementAMConfigurator](#addTargetElementAMConfigurator(java.lang.String,com.nomagic.magicdraw.actions.TargetElementAMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [TargetElementAMConfigurator](TargetElementAMConfigurator.html) configurator)`
Adds new drawable targets configurator in context toolbar for given diagram type
`void`
`[configureTargetElementAM](#configureTargetElementAM(java.lang.String,com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [ActionsManager](../../actions/ActionsManager.html) manager,
 [PresentationElement](../uml/symbols/PresentationElement.html) requestor,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pathActionID)`
Configures given diagram type drawable targets.
`static [ActionsConfiguratorsManager](ActionsConfiguratorsManager.html)`
`[getInstance](#getInstance())()`
Returns shared instance of this manager.
`void`
`[removeAnyDiagramCommandBarConfigurator](#removeAnyDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Remove configurator for any type diagrams.
`void`
`[removeAnyDiagramShortcutsConfigurator](#removeAnyDiagramShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes configurator from any type diagram.
`void`
`[removeBaseDiagramContextConfigurator](#removeBaseDiagramContextConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextAMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextAMConfigurator](DiagramContextAMConfigurator.html) configurator)`
Removes given configurator from given diagram type context configurators.
`void`
`[removeBaseDiagramContextToolbarConfigurator](#removeBaseDiagramContextToolbarConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextToolbarAMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextToolbarAMConfigurator](DiagramContextToolbarAMConfigurator.html) configurator)`
Removes given configurator from given diagram type context configurators.
`void`
`[removeContainmentBrowserContextConfigurator](#removeContainmentBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator))([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)`
Removes context configurator from containment browser.
`void`
`[removeContainmentBrowserShortcutsConfigurator](#removeContainmentBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes shortcuts configurator from containment browser.
`void`
`[removeContainmentBrowserToolbarConfigurator](#removeContainmentBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator))([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)`
Removes Toolbar configurator from containment browser.
`void`
`[removeCreateDiagramDialogConfigurator](#removeCreateDiagramDialogConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Remove configurator to configure actions inside "Create Diagram" dialog.
`void`
`[removeCustomizableShortcutsConfigurator](#removeCustomizableShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes configurator for main shortcuts.
`void`
`[removeDiagramCommandBarConfigurator](#removeDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Deprecated.
deprecated because of too generic name.
`void`
`[removeDiagramCommandBarConfigurator](#removeDiagramCommandBarConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Remove configurator for diagram of given type.
`void`
`[removeDiagramContextConfigurator](#removeDiagramContextConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextAMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextAMConfigurator](DiagramContextAMConfigurator.html) configurator)`
Removes given configurator from given diagram type context configurators.
`void`
`[removeDiagramContextToolbarConfigurator](#removeDiagramContextToolbarConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextToolbarAMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextToolbarAMConfigurator](DiagramContextToolbarAMConfigurator.html) configurator)`
Removes configurator from given diagram toolbar configurators.
`void`
`[removeDiagramNavigationConfigurator](#removeDiagramNavigationConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes configurator from diagram navigation configuration.
`void`
`[removeDiagramsBrowserContextConfigurator](#removeDiagramsBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator))([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)`
Removes context configurator from diagrams browser.
`void`
`[removeDiagramsBrowserShortcutsConfigurator](#removeDiagramsBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes shortcuts configurator from diagrams browser.
`void`
`[removeDiagramsBrowserToolbarConfigurator](#removeDiagramsBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator))([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)`
Removes Toolbar configurator from diagrams browser.
`void`
`[removeDiagramShortcutsConfigurator](#removeDiagramShortcutsConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes configurator from given diagram type shortcuts configurators.
`void`
`[removeDiagramToolbarActionsProvider](#removeDiagramToolbarActionsProvider(java.lang.String,com.nomagic.magicdraw.ui.actions.CustomizableDiagramToolbarActionsProvider))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [CustomizableDiagramToolbarActionsProvider](../ui/actions/CustomizableDiagramToolbarActionsProvider.html) provider)`
Removes action provider for specified diagram type.
`void`
`[removeDiagramToolbarConfigurator](#removeDiagramToolbarConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes configurator from given diagram toolbar configurators.
`void`
`[removeExtensionsBrowserContextConfigurator](#removeExtensionsBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator))([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)`
Removes context configurator from extensions browser.
`void`
`[removeExtensionsBrowserShortcutsConfigurator](#removeExtensionsBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes shortcuts configurator from extensions browser.
`void`
`[removeExtensionsBrowserToolbarConfigurator](#removeExtensionsBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator))([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)`
Removes Toolbar configurator from extensions browser.
`void`
`[removeInheritanceBrowserContextConfigurator](#removeInheritanceBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator))([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)`
Removes context configurator from inheritance browser.
`void`
`[removeInheritanceBrowserShortcutsConfigurator](#removeInheritanceBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes shortcuts configurator from inheritance browser.
`void`
`[removeInheritanceBrowserToolbarConfigurator](#removeInheritanceBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator))([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)`
Removes context configurator from inheritance browser.
`void`
`[removeLockViewBrowserContextConfigurator](#removeLockViewBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator))([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)`
Removes context configurator from lock view browser.
`void`
`[removeLockViewBrowserShortcutsConfigurator](#removeLockViewBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes shortcuts configurator from lock view browser.
`void`
`[removeLockViewBrowserToolbarConfigurator](#removeLockViewBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator))([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)`
Removes context configurator from inheritance browser.
`void`
`[removeMainMenuConfigurator](#removeMainMenuConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes configurator from main menu configuration.
`void`
`[removeMainShortcutsConfigurator](#removeMainShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes configurator for main shortcuts.
`void`
`[removeMainToolbarConfigurator](#removeMainToolbarConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes configurator from main toolbar.
`void`
`[removeSearchBrowserContextConfigurator](#removeSearchBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator))([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)`
Removes context configurator from search browser.
`void`
`[removeSearchBrowserShortcutsConfigurator](#removeSearchBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes shortcuts configurator from search browser.
`void`
`[removeSearchBrowserToolbarConfigurator](#removeSearchBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator))([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)`
Removes Toolbar configurator from search browser.
`void`
`[removeSymbolDiagramCommandBarConfigurator](#removeSymbolDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Remove configurator for any type "symbol" diagrams Those do not include tables, maps, matrices, etc.
`void`
`[removeSymbolDiagramShortcutsConfigurator](#removeSymbolDiagramShortcutsConfigurator(com.nomagic.actions.AMConfigurator))([AMConfigurator](../../actions/AMConfigurator.html) configurator)`
Removes configurator from any "symbol" diagram.
`void`
`[removeTargetElementAMConfigurator](#removeTargetElementAMConfigurator(java.lang.String,com.nomagic.magicdraw.actions.TargetElementAMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [TargetElementAMConfigurator](TargetElementAMConfigurator.html) configurator)`
Removes drawable targets' configurator for given diagram type
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
@OpenApipublic static [ActionsConfiguratorsManager](ActionsConfiguratorsManager.html) getInstance()
Returns shared instance of this manager.
addTargetElementAMConfigurator
@OpenApipublic void addTargetElementAMConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [TargetElementAMConfigurator](TargetElementAMConfigurator.html) configurator)
Adds new drawable targets configurator in context toolbar for given diagram type
Parameters:
`diagramType` - diagram type
`configurator` - configurator to be added.
removeTargetElementAMConfigurator
@OpenApipublic void removeTargetElementAMConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [TargetElementAMConfigurator](TargetElementAMConfigurator.html) configurator)
Removes drawable targets' configurator for given diagram type
Parameters:
`diagramType` - diagram type
`configurator` - configurator to be added.
configureTargetElementAM
@OpenApipublic void configureTargetElementAM([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [ActionsManager](../../actions/ActionsManager.html) manager,
 [PresentationElement](../uml/symbols/PresentationElement.html) requestor,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pathActionID)
Configures given diagram type drawable targets.
Parameters:
`diagramType` - diagram type
`manager` - manager to be configured.
`requestor` - - object which requests actions, can be null if requestor is diagram window.
addDiagramContextToolbarConfigurator
@OpenApipublic void addDiagramContextToolbarConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextToolbarAMConfigurator](DiagramContextToolbarAMConfigurator.html) configurator)
Adds new toolbar configurator for given diagram type.
Parameters:
`diagramType` - diagram type
`configurator` - configurator to be added.
removeDiagramContextToolbarConfigurator
@OpenApipublic void removeDiagramContextToolbarConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextToolbarAMConfigurator](DiagramContextToolbarAMConfigurator.html) configurator)
Removes configurator from given diagram toolbar configurators.
Parameters:
`diagramType` - diagram type
`configurator` - configurator to be removed.
removeBaseDiagramContextToolbarConfigurator
@OpenApipublic void removeBaseDiagramContextToolbarConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextToolbarAMConfigurator](DiagramContextToolbarAMConfigurator.html) configurator)
Removes given configurator from given diagram type context configurators. This configurator will be removed to the given type of the
Parameters:
`diagramType` - diagram type
`configurator` - configurator to remove.
addDiagramContextConfigurator
@OpenApipublic void addDiagramContextConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextAMConfigurator](DiagramContextAMConfigurator.html) configurator)
Adds new diagram context configurator for given diagram type.
Parameters:
`diagramType` - diagram type
`configurator` - new configurator to add.
addBaseDiagramContextConfigurator
@OpenApipublic void addBaseDiagramContextConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextAMConfigurator](DiagramContextAMConfigurator.html) configurator)
Adds new diagram context configurator for given diagram type. This configurator will be added to the given type of the
 diagram and to all derived diagram types.
Parameters:
`diagramType` - diagram type
`configurator` - new configurator to add.
addBaseDiagramContextConfigurator
@OpenApipublic void addBaseDiagramContextConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramContextAMConfigurator configurator)
Adds new diagram context configurator for given diagram type. This configurator will be added to the given type of the
 diagram and to all derived diagram types.
Parameters:
`diagramType` - diagram type
`configurator` - new configurator to add.
removeDiagramContextConfigurator
@OpenApipublic void removeDiagramContextConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextAMConfigurator](DiagramContextAMConfigurator.html) configurator)
Removes given configurator from given diagram type context configurators.
Parameters:
`diagramType` - diagram type
`configurator` - configurator to remove.
removeBaseDiagramContextConfigurator
@OpenApipublic void removeBaseDiagramContextConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramContextAMConfigurator](DiagramContextAMConfigurator.html) configurator)
Removes given configurator from given diagram type context configurators. This configurator will be removed to the given type of the
Parameters:
`diagramType` - diagram type
`configurator` - configurator to remove.
addDiagramCommandBarConfigurator
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void addDiagramCommandBarConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Deprecated.
deprecated because of too generic name. Use [`addSymbolDiagramCommandBarConfigurator(AMConfigurator)`](#addSymbolDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator))
Add configurator for any type of "symbol" diagrams Those do not include tables, maps, matrices, etc.
Parameters:
`configurator` - configurator to be added.
removeDiagramCommandBarConfigurator
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void removeDiagramCommandBarConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Deprecated.
deprecated because of too generic name. Use [`removeSymbolDiagramCommandBarConfigurator(AMConfigurator)`](#removeSymbolDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator))
Remove configurator for any type "symbol" diagrams Those do not include tables, maps, matrices, etc.
Parameters:
`configurator` - configurator to be removed.
addSymbolDiagramCommandBarConfigurator
@OpenApipublic void addSymbolDiagramCommandBarConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Add configurator for any type of "symbol" diagrams Those do not include tables, maps, matrices, etc.
Parameters:
`configurator` - configurator to be added.
removeSymbolDiagramCommandBarConfigurator
@OpenApipublic void removeSymbolDiagramCommandBarConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Remove configurator for any type "symbol" diagrams Those do not include tables, maps, matrices, etc.
Parameters:
`configurator` - configurator to be removed.
addAnyDiagramCommandBarConfigurator
@OpenApipublic void addAnyDiagramCommandBarConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Registers configurator for any type of diagrams.
Parameters:
`configurator` - configurator to be added.
removeAnyDiagramCommandBarConfigurator
@OpenApipublic void removeAnyDiagramCommandBarConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Remove configurator for any type diagrams.
Parameters:
`configurator` - configurator to be removed.
addDiagramCommandBarConfigurator
@OpenApipublic void addDiagramCommandBarConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)
Add configurator for diagram of given type.
Parameters:
`diagramType` - diagram type
`configurator` - configurator to be added.
removeDiagramCommandBarConfigurator
@OpenApipublic void removeDiagramCommandBarConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)
Remove configurator for diagram of given type.
Parameters:
`diagramType` - diagram type
`configurator` - configurator to be removed.
addDiagramToolbarConfigurator
@OpenApipublic void addDiagramToolbarConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds new toolbar configurator for given diagram type.
Parameters:
`diagramType` - diagram type
`configurator` - configurator to be added.
removeDiagramToolbarConfigurator
@OpenApipublic void removeDiagramToolbarConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes configurator from given diagram toolbar configurators.
Parameters:
`diagramType` - diagram type
`configurator` - configurator to be removed.
addAnyDiagramShortcutsConfigurator
@OpenApipublic void addAnyDiagramShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds configurator for any type diagram.
Parameters:
`configurator` - configurator to be added.
removeAnyDiagramShortcutsConfigurator
@OpenApipublic void removeAnyDiagramShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes configurator from any type diagram.
Parameters:
`configurator` - configurator to be removed.
addSymbolDiagramShortcutsConfigurator
@OpenApipublic void addSymbolDiagramShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds configurator for any "symbol" diagram. Those diagrams do not include tables, maps, matrices, etc.
Parameters:
`configurator` - configurator to be added.
removeSymbolDiagramShortcutsConfigurator
@OpenApipublic void removeSymbolDiagramShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes configurator from any "symbol" diagram. Those diagrams do not include tables, maps, matrices, etc.
Parameters:
`configurator` - configurator to be removed.
addDiagramShortcutsConfigurator
@OpenApipublic void addDiagramShortcutsConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds new shortcuts' configurator for given diagram type.
Parameters:
`diagramType` - diagram type
`configurator` - configurator to be added.
removeDiagramShortcutsConfigurator
@OpenApipublic void removeDiagramShortcutsConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes configurator from given diagram type shortcuts configurators.
Parameters:
`diagramType` - diagram type
`configurator` - configurator to be removed.
addInheritanceBrowserContextConfigurator
@OpenApipublic void addInheritanceBrowserContextConfigurator([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)
Adds new context configurator to inheritance browser.
Parameters:
`configurator` - configurator to be added.
removeInheritanceBrowserContextConfigurator
@OpenApipublic void removeInheritanceBrowserContextConfigurator([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)
Removes context configurator from inheritance browser.
Parameters:
`configurator` - configurator to be removed.
addDiagramsBrowserContextConfigurator
@OpenApipublic void addDiagramsBrowserContextConfigurator([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)
Adds new context configurator to diagrams browser.
Parameters:
`configurator` - configurator to be added.
removeDiagramsBrowserContextConfigurator
@OpenApipublic void removeDiagramsBrowserContextConfigurator([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)
Removes context configurator from diagrams browser.
Parameters:
`configurator` - configurator to be removed.
addLockViewBrowserContextConfigurator
@OpenApipublic void addLockViewBrowserContextConfigurator([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)
Adds new context configurator to lock view browser.
Parameters:
`configurator` - configurator to be added.
removeLockViewBrowserContextConfigurator
@OpenApipublic void removeLockViewBrowserContextConfigurator([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)
Removes context configurator from lock view browser.
Parameters:
`configurator` - configurator to be removed.
addContainmentBrowserContextConfigurator
@OpenApipublic void addContainmentBrowserContextConfigurator([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)
Adds new context configurator to containment browser.
Parameters:
`configurator` - configurator to be added.
removeContainmentBrowserContextConfigurator
@OpenApipublic void removeContainmentBrowserContextConfigurator([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)
Removes context configurator from containment browser.
Parameters:
`configurator` - configurator to be removed.
addExtensionsBrowserContextConfigurator
@OpenApipublic void addExtensionsBrowserContextConfigurator([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)
Adds new context configurator to extensions browser.
Parameters:
`configurator` - configurator to be added.
removeExtensionsBrowserContextConfigurator
@OpenApipublic void removeExtensionsBrowserContextConfigurator([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)
Removes context configurator from extensions browser.
Parameters:
`configurator` - configurator to be removed.
addSearchBrowserContextConfigurator
@OpenApipublic void addSearchBrowserContextConfigurator([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)
Adds new context configurator for search browser.
Parameters:
`configurator` - configurator to be added.
removeSearchBrowserContextConfigurator
@OpenApipublic void removeSearchBrowserContextConfigurator([BrowserContextAMConfigurator](BrowserContextAMConfigurator.html) configurator)
Removes context configurator from search browser.
Parameters:
`configurator` - configurator to be removed.
addInheritanceBrowserToolbarConfigurator
@OpenApipublic void addInheritanceBrowserToolbarConfigurator([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)
Adds new context configurator to inheritance browser.
Parameters:
`configurator` - configurator to be added.
removeInheritanceBrowserToolbarConfigurator
@OpenApipublic void removeInheritanceBrowserToolbarConfigurator([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)
Removes context configurator from inheritance browser.
Parameters:
`configurator` - configurator to be removed.
addDiagramsBrowserToolbarConfigurator
@OpenApipublic void addDiagramsBrowserToolbarConfigurator([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)
Adds new Toolbar configurator to diagrams browser.
Parameters:
`configurator` - configurator to be added.
removeDiagramsBrowserToolbarConfigurator
@OpenApipublic void removeDiagramsBrowserToolbarConfigurator([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)
Removes Toolbar configurator from diagrams browser.
Parameters:
`configurator` - configurator to be removed.
addLockViewBrowserToolbarConfigurator
@OpenApipublic void addLockViewBrowserToolbarConfigurator([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)
Adds new context configurator to inheritance browser.
Parameters:
`configurator` - configurator to be added.
removeLockViewBrowserToolbarConfigurator
@OpenApipublic void removeLockViewBrowserToolbarConfigurator([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)
Removes context configurator from inheritance browser.
Parameters:
`configurator` - configurator to be removed.
addContainmentBrowserToolbarConfigurator
@OpenApipublic void addContainmentBrowserToolbarConfigurator([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)
Adds new Toolbar configurator to containment browser.
Parameters:
`configurator` - configurator to be added.
removeContainmentBrowserToolbarConfigurator
@OpenApipublic void removeContainmentBrowserToolbarConfigurator([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)
Removes Toolbar configurator from containment browser.
Parameters:
`configurator` - configurator to be removed.
addExtensionsBrowserToolbarConfigurator
@OpenApipublic void addExtensionsBrowserToolbarConfigurator([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)
Adds new Toolbar configurator to extensions browser.
Parameters:
`configurator` - configurator to be added.
removeExtensionsBrowserToolbarConfigurator
@OpenApipublic void removeExtensionsBrowserToolbarConfigurator([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)
Removes Toolbar configurator from extensions browser.
Parameters:
`configurator` - configurator to be removed.
addSearchBrowserToolbarConfigurator
@OpenApipublic void addSearchBrowserToolbarConfigurator([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)
Adds new Toolbar configurator for search browser.
Parameters:
`configurator` - configurator to be added.
removeSearchBrowserToolbarConfigurator
@OpenApipublic void removeSearchBrowserToolbarConfigurator([BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html) configurator)
Removes Toolbar configurator from search browser.
Parameters:
`configurator` - configurator to be removed.
addInheritanceBrowserShortcutsConfigurator
@OpenApipublic void addInheritanceBrowserShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds new shortcuts' configurator to inheritance browser.
Parameters:
`configurator` - configurator to be added.
removeInheritanceBrowserShortcutsConfigurator
@OpenApipublic void removeInheritanceBrowserShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes shortcuts configurator from inheritance browser.
Parameters:
`configurator` - configurator to be removed.
addDiagramsBrowserShortcutsConfigurator
@OpenApipublic void addDiagramsBrowserShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds new shortcuts' configurator to diagrams browser.
Parameters:
`configurator` - configurator to be added.
removeDiagramsBrowserShortcutsConfigurator
@OpenApipublic void removeDiagramsBrowserShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes shortcuts configurator from diagrams browser.
Parameters:
`configurator` - configurator to be removed.
addLockViewBrowserShortcutsConfigurator
@OpenApipublic void addLockViewBrowserShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds new shortcuts' configurator to lock view browser.
Parameters:
`configurator` - configurator to be added.
removeLockViewBrowserShortcutsConfigurator
@OpenApipublic void removeLockViewBrowserShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes shortcuts configurator from lock view browser.
Parameters:
`configurator` - configurator to be removed.
addExtensionsBrowserShortcutsConfigurator
@OpenApipublic void addExtensionsBrowserShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds new shortcuts' configurator to extensions browser.
Parameters:
`configurator` - configurator to be added.
removeExtensionsBrowserShortcutsConfigurator
@OpenApipublic void removeExtensionsBrowserShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes shortcuts configurator from extensions browser.
Parameters:
`configurator` - configurator to be removed.
addSearchBrowserShortcutsConfigurator
@OpenApipublic void addSearchBrowserShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds new shortcuts' configurator to search browser.
Parameters:
`configurator` - configurator to be added.
removeSearchBrowserShortcutsConfigurator
@OpenApipublic void removeSearchBrowserShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes shortcuts configurator from search browser.
Parameters:
`configurator` - configurator to be removed.
addContainmentBrowserShortcutsConfigurator
@OpenApipublic void addContainmentBrowserShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds new shortcuts' configurator to containment browser.
Parameters:
`configurator` - configurator to be added.
removeContainmentBrowserShortcutsConfigurator
@OpenApipublic void removeContainmentBrowserShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes shortcuts configurator from containment browser.
Parameters:
`configurator` - configurator to be removed.
removeMainMenuConfigurator
@OpenApipublic void removeMainMenuConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes configurator from main menu configuration.
Parameters:
`configurator` - configurator to remove.
addMainMenuConfigurator
@OpenApipublic void addMainMenuConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds configurator to main menu. This method should be called before menu becomes visible.
Parameters:
`configurator` - configurator will be added.
addCreateDiagramDialogConfigurator
@OpenApipublic void addCreateDiagramDialogConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds configurator to configure actions inside the dialog which opens when action in main menu or toolbar "Create Diagram" is executed.
 To configure actions inside context menu please see [`addDialogActionsConfigurator(String, ActionsManager, AMConfigurator)`](#addDialogActionsConfigurator(java.lang.String,com.nomagic.actions.ActionsManager,com.nomagic.actions.AMConfigurator))
Parameters:
`configurator` - actions configurator
removeCreateDiagramDialogConfigurator
@OpenApipublic void removeCreateDiagramDialogConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Remove configurator to configure actions inside "Create Diagram" dialog.
Parameters:
`configurator` - configurator to be removed
addDialogActionsConfigurator
@OpenApipublic static void addDialogActionsConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) categoryID,
 [ActionsManager](../../actions/ActionsManager.html) manager,
 [AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds configurator to configure actions inside specific popup dialog which constructs its actions only when respective popup menu item is clicked. 

Call this method inside [`BrowserContextAMConfigurator.configure(ActionsManager, Tree)`](BrowserContextAMConfigurator.html#configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.ui.browser.Tree)) in order to configure browser context menu actions.
 Call this method inside (@link [`DiagramContextAMConfigurator.configure(ActionsManager, DiagramPresentationElement, PresentationElement[], PresentationElement)`](DiagramContextAMConfigurator.html#configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement%5B%5D,com.nomagic.magicdraw.uml.symbols.PresentationElement))
 to configure diagram context menu actions
Parameters:
`categoryID` - id of the category which represents the dialog to be configured. Most common examples: 

[`ActionsID.NEW_ELEMENT_CATEGORY_ID`](ActionsID.html#NEW_ELEMENT_CATEGORY_ID) - to configure "Create Element" context action 

[`ActionsID.NEW_DIAGRAM_CATEGORY_ID`](ActionsID.html#NEW_DIAGRAM_CATEGORY_ID) - to configure "Create Diagram" context action 

[`ActionsID.NEW_RELATION_CATEGORY_FROM_ID`](ActionsID.html#NEW_RELATION_CATEGORY_FROM_ID) - to configure "Create Relation->Outgoing" context action 

[`ActionsID.NEW_RELATION_CATEGORY_TO_ID`](ActionsID.html#NEW_RELATION_CATEGORY_TO_ID) - to configure "Create Relation->Outgoing" context action
`manager` - actions manager that contains the category with the given id.
 Category may be empty at the time this method is called. since category actions are only created when the menu item is clicked
 Category may not exist in the manager, in that case nothing will get configured.
 Category should not be added to the manager manually if it is not present.
`configurator` - actions configurator which will be called when constructing actions (when displaying the dialog with actions)
removeDiagramNavigationConfigurator
@OpenApipublic void removeDiagramNavigationConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes configurator from diagram navigation configuration.
Parameters:
`configurator` - configurator to remove.
addDiagramNavigationConfigurator
@OpenApipublic void addDiagramNavigationConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds configurator to diagram navigation toolbar. This method should be called before menu becomes visible.
Parameters:
`configurator` - configurator to add.
removeMainShortcutsConfigurator
@OpenApipublic void removeMainShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes configurator for main shortcuts.
Parameters:
`configurator` - configurator will be removed.
addMainShortcutsConfigurator
@OpenApipublic void addMainShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds configurator for main shortcuts.
Parameters:
`configurator` - configurator will be added.
removeCustomizableShortcutsConfigurator
@OpenApipublic void removeCustomizableShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes configurator for main shortcuts.
Parameters:
`configurator` - configurator will be removed.
addCustomizableShortcutsConfigurator
@OpenApipublic void addCustomizableShortcutsConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds configurator for main shortcuts.
Parameters:
`configurator` - configurator will be added.
addMainToolbarConfigurator
@OpenApipublic void addMainToolbarConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Adds configurator to main toolbar. This method should be called before toolbar becomes visible.
Parameters:
`configurator` - configurator will be added.
removeMainToolbarConfigurator
@OpenApipublic void removeMainToolbarConfigurator([AMConfigurator](../../actions/AMConfigurator.html) configurator)
Removes configurator from main toolbar.
Parameters:
`configurator` - configurator will be removed.
addDiagramToolbarActionsProvider
@OpenApipublic void addDiagramToolbarActionsProvider([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [CustomizableDiagramToolbarActionsProvider](../ui/actions/CustomizableDiagramToolbarActionsProvider.html) provider)
Adds new toolbar provider for given diagram type.
Parameters:
`diagramType` - diagram type.
`provider` - action provider to be added.
removeDiagramToolbarActionsProvider
@OpenApipublic void removeDiagramToolbarActionsProvider([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [CustomizableDiagramToolbarActionsProvider](../ui/actions/CustomizableDiagramToolbarActionsProvider.html) provider)
Removes action provider for specified diagram type.
Parameters:
`diagramType` - diagram type
`provider` - action provider to be removed.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.actions</a></div>
<h1 class="title" title="Class ActionsConfiguratorsManager">Class ActionsConfiguratorsManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.actions.ActionsConfiguratorsManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">ActionsConfiguratorsManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The singleton class for adding/removing configurations of actions managers in MagicDraw application.</div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAnyDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)">addAnyDiagramCommandBarConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers configurator for any type of diagrams.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAnyDiagramShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">addAnyDiagramShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds configurator for any type diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addBaseDiagramContextConfigurator(java.lang.String,com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramContextAMConfigurator)">addBaseDiagramContextConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramContextAMConfigurator configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new diagram context configurator for given diagram type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addBaseDiagramContextConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextAMConfigurator)">addBaseDiagramContextConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new diagram context configurator for given diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addContainmentBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">addContainmentBrowserContextConfigurator</a><wbr/>(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new context configurator to containment browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addContainmentBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">addContainmentBrowserShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new shortcuts' configurator to containment browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addContainmentBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">addContainmentBrowserToolbarConfigurator</a><wbr/>(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new Toolbar configurator to containment browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCreateDiagramDialogConfigurator(com.nomagic.actions.AMConfigurator)">addCreateDiagramDialogConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds configurator to configure actions inside the dialog which opens when action in main menu or toolbar "Create Diagram" is executed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCustomizableShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">addCustomizableShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds configurator for main shortcuts.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)">addDiagramCommandBarConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">deprecated because of too generic name.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addDiagramCommandBarConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">addDiagramCommandBarConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add configurator for diagram of given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addDiagramContextConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextAMConfigurator)">addDiagramContextConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new diagram context configurator for given diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addDiagramContextToolbarConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextToolbarAMConfigurator)">addDiagramContextToolbarConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new toolbar configurator for given diagram type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addDiagramNavigationConfigurator(com.nomagic.actions.AMConfigurator)">addDiagramNavigationConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds configurator to diagram navigation toolbar.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addDiagramsBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">addDiagramsBrowserContextConfigurator</a><wbr/>(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new context configurator to diagrams browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addDiagramsBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">addDiagramsBrowserShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new shortcuts' configurator to diagrams browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addDiagramsBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">addDiagramsBrowserToolbarConfigurator</a><wbr/>(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new Toolbar configurator to diagrams browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addDiagramShortcutsConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">addDiagramShortcutsConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new shortcuts' configurator for given diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addDiagramToolbarActionsProvider(java.lang.String,com.nomagic.magicdraw.ui.actions.CustomizableDiagramToolbarActionsProvider)">addDiagramToolbarActionsProvider</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../ui/actions/CustomizableDiagramToolbarActionsProvider.html" title="interface in com.nomagic.magicdraw.ui.actions">CustomizableDiagramToolbarActionsProvider</a> provider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new toolbar provider for given diagram type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addDiagramToolbarConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">addDiagramToolbarConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new toolbar configurator for given diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addDialogActionsConfigurator(java.lang.String,com.nomagic.actions.ActionsManager,com.nomagic.actions.AMConfigurator)">addDialogActionsConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> categoryID,
 <a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds configurator to configure actions inside specific popup dialog which constructs its actions only when respective popup menu item is clicked.<br/></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addExtensionsBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">addExtensionsBrowserContextConfigurator</a><wbr/>(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new context configurator to extensions browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addExtensionsBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">addExtensionsBrowserShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new shortcuts' configurator to extensions browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addExtensionsBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">addExtensionsBrowserToolbarConfigurator</a><wbr/>(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new Toolbar configurator to extensions browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addInheritanceBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">addInheritanceBrowserContextConfigurator</a><wbr/>(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new context configurator to inheritance browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addInheritanceBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">addInheritanceBrowserShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new shortcuts' configurator to inheritance browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addInheritanceBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">addInheritanceBrowserToolbarConfigurator</a><wbr/>(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new context configurator to inheritance browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addLockViewBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">addLockViewBrowserContextConfigurator</a><wbr/>(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new context configurator to lock view browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addLockViewBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">addLockViewBrowserShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new shortcuts' configurator to lock view browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addLockViewBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">addLockViewBrowserToolbarConfigurator</a><wbr/>(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new context configurator to inheritance browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMainMenuConfigurator(com.nomagic.actions.AMConfigurator)">addMainMenuConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds configurator to main menu.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMainShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">addMainShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds configurator for main shortcuts.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMainToolbarConfigurator(com.nomagic.actions.AMConfigurator)">addMainToolbarConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds configurator to main toolbar.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSearchBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">addSearchBrowserContextConfigurator</a><wbr/>(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new context configurator for search browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSearchBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">addSearchBrowserShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new shortcuts' configurator to search browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSearchBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">addSearchBrowserToolbarConfigurator</a><wbr/>(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new Toolbar configurator for search browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSymbolDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)">addSymbolDiagramCommandBarConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add configurator for any type of "symbol" diagrams Those do not include tables, maps, matrices, etc.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSymbolDiagramShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">addSymbolDiagramShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds configurator for any "symbol" diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addTargetElementAMConfigurator(java.lang.String,com.nomagic.magicdraw.actions.TargetElementAMConfigurator)">addTargetElementAMConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="TargetElementAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">TargetElementAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new drawable targets configurator in context toolbar for given diagram type</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#configureTargetElementAM(java.lang.String,com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">configureTargetElementAM</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> requestor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pathActionID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures given diagram type drawable targets.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ActionsConfiguratorsManager.html" title="class in com.nomagic.magicdraw.actions">ActionsConfiguratorsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of this manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAnyDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)">removeAnyDiagramCommandBarConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove configurator for any type diagrams.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAnyDiagramShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">removeAnyDiagramShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes configurator from any type diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeBaseDiagramContextConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextAMConfigurator)">removeBaseDiagramContextConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given configurator from given diagram type context configurators.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeBaseDiagramContextToolbarConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextToolbarAMConfigurator)">removeBaseDiagramContextToolbarConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given configurator from given diagram type context configurators.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeContainmentBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">removeContainmentBrowserContextConfigurator</a><wbr/>(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  context configurator from containment browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeContainmentBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">removeContainmentBrowserShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  shortcuts configurator from containment browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeContainmentBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">removeContainmentBrowserToolbarConfigurator</a><wbr/>(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  Toolbar configurator from containment browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeCreateDiagramDialogConfigurator(com.nomagic.actions.AMConfigurator)">removeCreateDiagramDialogConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove configurator to configure actions inside "Create Diagram" dialog.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeCustomizableShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">removeCustomizableShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes configurator for main shortcuts.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#removeDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)">removeDiagramCommandBarConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">deprecated because of too generic name.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDiagramCommandBarConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">removeDiagramCommandBarConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove configurator for diagram of given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDiagramContextConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextAMConfigurator)">removeDiagramContextConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given configurator from given diagram type context configurators.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDiagramContextToolbarConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextToolbarAMConfigurator)">removeDiagramContextToolbarConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes configurator from given diagram toolbar configurators.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDiagramNavigationConfigurator(com.nomagic.actions.AMConfigurator)">removeDiagramNavigationConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes configurator from diagram navigation configuration.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDiagramsBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">removeDiagramsBrowserContextConfigurator</a><wbr/>(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  context configurator from diagrams browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDiagramsBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">removeDiagramsBrowserShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  shortcuts configurator from diagrams browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDiagramsBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">removeDiagramsBrowserToolbarConfigurator</a><wbr/>(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes Toolbar configurator from diagrams browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDiagramShortcutsConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">removeDiagramShortcutsConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes configurator from given diagram type shortcuts configurators.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDiagramToolbarActionsProvider(java.lang.String,com.nomagic.magicdraw.ui.actions.CustomizableDiagramToolbarActionsProvider)">removeDiagramToolbarActionsProvider</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../ui/actions/CustomizableDiagramToolbarActionsProvider.html" title="interface in com.nomagic.magicdraw.ui.actions">CustomizableDiagramToolbarActionsProvider</a> provider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes action provider for specified diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDiagramToolbarConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">removeDiagramToolbarConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes configurator from given diagram toolbar configurators.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeExtensionsBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">removeExtensionsBrowserContextConfigurator</a><wbr/>(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes context configurator from extensions browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeExtensionsBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">removeExtensionsBrowserShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes shortcuts configurator from extensions browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeExtensionsBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">removeExtensionsBrowserToolbarConfigurator</a><wbr/>(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  Toolbar configurator from extensions browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeInheritanceBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">removeInheritanceBrowserContextConfigurator</a><wbr/>(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  context configurator from inheritance browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeInheritanceBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">removeInheritanceBrowserShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  shortcuts configurator from inheritance browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeInheritanceBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">removeInheritanceBrowserToolbarConfigurator</a><wbr/>(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  context configurator from inheritance browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeLockViewBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">removeLockViewBrowserContextConfigurator</a><wbr/>(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  context configurator from lock view browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeLockViewBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">removeLockViewBrowserShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  shortcuts configurator from lock view browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeLockViewBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">removeLockViewBrowserToolbarConfigurator</a><wbr/>(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  context configurator from inheritance browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMainMenuConfigurator(com.nomagic.actions.AMConfigurator)">removeMainMenuConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes configurator from main menu configuration.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMainShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">removeMainShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes configurator for main shortcuts.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMainToolbarConfigurator(com.nomagic.actions.AMConfigurator)">removeMainToolbarConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes configurator from main toolbar.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSearchBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">removeSearchBrowserContextConfigurator</a><wbr/>(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes context configurator from search browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSearchBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">removeSearchBrowserShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes shortcuts configurator from search browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSearchBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">removeSearchBrowserToolbarConfigurator</a><wbr/>(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes Toolbar configurator from search browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSymbolDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)">removeSymbolDiagramCommandBarConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove configurator for any type "symbol" diagrams Those do not include tables, maps, matrices, etc.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSymbolDiagramShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">removeSymbolDiagramShortcutsConfigurator</a><wbr/>(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes configurator from any "symbol" diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeTargetElementAMConfigurator(java.lang.String,com.nomagic.magicdraw.actions.TargetElementAMConfigurator)">removeTargetElementAMConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="TargetElementAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">TargetElementAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes drawable targets' configurator for given diagram type</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ActionsConfiguratorsManager.html" title="class in com.nomagic.magicdraw.actions">ActionsConfiguratorsManager</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Returns shared instance of this manager.</div>
</section>
</li>
<li>
<section class="detail" id="addTargetElementAMConfigurator(java.lang.String,com.nomagic.magicdraw.actions.TargetElementAMConfigurator)">
<h3>addTargetElementAMConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addTargetElementAMConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="TargetElementAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">TargetElementAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new drawable targets configurator in context toolbar for given diagram type</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeTargetElementAMConfigurator(java.lang.String,com.nomagic.magicdraw.actions.TargetElementAMConfigurator)">
<h3>removeTargetElementAMConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeTargetElementAMConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="TargetElementAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">TargetElementAMConfigurator</a> configurator)</span></div>
<div class="block">Removes drawable targets' configurator for given diagram type</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="configureTargetElementAM(java.lang.String,com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">
<h3>configureTargetElementAM</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">configureTargetElementAM</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> requestor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pathActionID)</span></div>
<div class="block">Configures given diagram type drawable targets.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>manager</code> - manager to be configured.</dd>
<dd><code>requestor</code> - -  object which requests actions, can be null if requestor is diagram window.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addDiagramContextToolbarConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextToolbarAMConfigurator)">
<h3>addDiagramContextToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addDiagramContextToolbarConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new toolbar configurator for given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeDiagramContextToolbarConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextToolbarAMConfigurator)">
<h3>removeDiagramContextToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeDiagramContextToolbarConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Removes configurator from given diagram toolbar configurators.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeBaseDiagramContextToolbarConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextToolbarAMConfigurator)">
<h3>removeBaseDiagramContextToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeBaseDiagramContextToolbarConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Removes given configurator from given diagram type context configurators. This configurator will be removed to the given type of the</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - configurator to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addDiagramContextConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextAMConfigurator)">
<h3>addDiagramContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addDiagramContextConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new diagram context configurator for given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - new configurator to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addBaseDiagramContextConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextAMConfigurator)">
<h3>addBaseDiagramContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addBaseDiagramContextConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new diagram context configurator for given diagram type. This configurator will be added to the given type of the
 diagram and to all derived diagram types.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - new configurator to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addBaseDiagramContextConfigurator(java.lang.String,com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramContextAMConfigurator)">
<h3>addBaseDiagramContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addBaseDiagramContextConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramContextAMConfigurator configurator)</span></div>
<div class="block">Adds new diagram context configurator for given diagram type. This configurator will be added to the given type of the
 diagram and to all derived diagram types.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - new configurator to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeDiagramContextConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextAMConfigurator)">
<h3>removeDiagramContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeDiagramContextConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a> configurator)</span></div>
<div class="block">Removes given configurator from given diagram type context configurators.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - configurator to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeBaseDiagramContextConfigurator(java.lang.String,com.nomagic.magicdraw.actions.DiagramContextAMConfigurator)">
<h3>removeBaseDiagramContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeBaseDiagramContextConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a> configurator)</span></div>
<div class="block">Removes given configurator from given diagram type context configurators. This configurator will be removed to the given type of the</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - configurator to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addDiagramCommandBarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addDiagramCommandBarConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">deprecated because of too generic name. Use <a href="#addSymbolDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)"><code>addSymbolDiagramCommandBarConfigurator(AMConfigurator)</code></a></div>
</div>
<div class="block">Add configurator for any type of "symbol" diagrams Those do not include tables, maps, matrices, etc.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeDiagramCommandBarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeDiagramCommandBarConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">deprecated because of too generic name. Use <a href="#removeSymbolDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)"><code>removeSymbolDiagramCommandBarConfigurator(AMConfigurator)</code></a></div>
</div>
<div class="block">Remove configurator for any type "symbol" diagrams Those do not include tables, maps, matrices, etc.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSymbolDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addSymbolDiagramCommandBarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSymbolDiagramCommandBarConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Add configurator for any type of "symbol" diagrams Those do not include tables, maps, matrices, etc.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSymbolDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeSymbolDiagramCommandBarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeSymbolDiagramCommandBarConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Remove configurator for any type "symbol" diagrams Those do not include tables, maps, matrices, etc.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAnyDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addAnyDiagramCommandBarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAnyDiagramCommandBarConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Registers configurator for any type of diagrams.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAnyDiagramCommandBarConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeAnyDiagramCommandBarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAnyDiagramCommandBarConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Remove configurator for any type diagrams.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addDiagramCommandBarConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">
<h3>addDiagramCommandBarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addDiagramCommandBarConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Add configurator for diagram of given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeDiagramCommandBarConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">
<h3>removeDiagramCommandBarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeDiagramCommandBarConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Remove configurator for diagram of given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addDiagramToolbarConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">
<h3>addDiagramToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addDiagramToolbarConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds new toolbar configurator for given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeDiagramToolbarConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">
<h3>removeDiagramToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeDiagramToolbarConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes configurator from given diagram toolbar configurators.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAnyDiagramShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addAnyDiagramShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAnyDiagramShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds configurator for any type diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAnyDiagramShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeAnyDiagramShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAnyDiagramShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes configurator from any type diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSymbolDiagramShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addSymbolDiagramShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSymbolDiagramShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds configurator for any "symbol" diagram. Those diagrams do not include tables, maps, matrices, etc.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSymbolDiagramShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeSymbolDiagramShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeSymbolDiagramShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes configurator from any "symbol" diagram. Those diagrams do not include tables, maps, matrices, etc.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addDiagramShortcutsConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">
<h3>addDiagramShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addDiagramShortcutsConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds new shortcuts' configurator for given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeDiagramShortcutsConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">
<h3>removeDiagramShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeDiagramShortcutsConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes configurator from given diagram type shortcuts configurators.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addInheritanceBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">
<h3>addInheritanceBrowserContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addInheritanceBrowserContextConfigurator</span><wbr/><span class="parameters">(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new context configurator to inheritance browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeInheritanceBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">
<h3>removeInheritanceBrowserContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeInheritanceBrowserContextConfigurator</span><wbr/><span class="parameters">(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</span></div>
<div class="block">Removes  context configurator from inheritance browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addDiagramsBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">
<h3>addDiagramsBrowserContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addDiagramsBrowserContextConfigurator</span><wbr/><span class="parameters">(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new context configurator to diagrams browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeDiagramsBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">
<h3>removeDiagramsBrowserContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeDiagramsBrowserContextConfigurator</span><wbr/><span class="parameters">(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</span></div>
<div class="block">Removes  context configurator from diagrams browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addLockViewBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">
<h3>addLockViewBrowserContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addLockViewBrowserContextConfigurator</span><wbr/><span class="parameters">(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new context configurator to lock view browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeLockViewBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">
<h3>removeLockViewBrowserContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeLockViewBrowserContextConfigurator</span><wbr/><span class="parameters">(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</span></div>
<div class="block">Removes  context configurator from lock view browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addContainmentBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">
<h3>addContainmentBrowserContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addContainmentBrowserContextConfigurator</span><wbr/><span class="parameters">(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new context configurator to containment browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeContainmentBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">
<h3>removeContainmentBrowserContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeContainmentBrowserContextConfigurator</span><wbr/><span class="parameters">(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</span></div>
<div class="block">Removes  context configurator from containment browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addExtensionsBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">
<h3>addExtensionsBrowserContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addExtensionsBrowserContextConfigurator</span><wbr/><span class="parameters">(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new context configurator to extensions browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeExtensionsBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">
<h3>removeExtensionsBrowserContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeExtensionsBrowserContextConfigurator</span><wbr/><span class="parameters">(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</span></div>
<div class="block">Removes context configurator from extensions browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSearchBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">
<h3>addSearchBrowserContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSearchBrowserContextConfigurator</span><wbr/><span class="parameters">(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new context configurator for search browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSearchBrowserContextConfigurator(com.nomagic.magicdraw.actions.BrowserContextAMConfigurator)">
<h3>removeSearchBrowserContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeSearchBrowserContextConfigurator</span><wbr/><span class="parameters">(<a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a> configurator)</span></div>
<div class="block">Removes context configurator from search browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addInheritanceBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">
<h3>addInheritanceBrowserToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addInheritanceBrowserToolbarConfigurator</span><wbr/><span class="parameters">(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new context configurator to inheritance browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeInheritanceBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">
<h3>removeInheritanceBrowserToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeInheritanceBrowserToolbarConfigurator</span><wbr/><span class="parameters">(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Removes  context configurator from inheritance browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addDiagramsBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">
<h3>addDiagramsBrowserToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addDiagramsBrowserToolbarConfigurator</span><wbr/><span class="parameters">(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new Toolbar configurator to diagrams browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeDiagramsBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">
<h3>removeDiagramsBrowserToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeDiagramsBrowserToolbarConfigurator</span><wbr/><span class="parameters">(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Removes Toolbar configurator from diagrams browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addLockViewBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">
<h3>addLockViewBrowserToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addLockViewBrowserToolbarConfigurator</span><wbr/><span class="parameters">(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new context configurator to inheritance browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeLockViewBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">
<h3>removeLockViewBrowserToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeLockViewBrowserToolbarConfigurator</span><wbr/><span class="parameters">(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Removes  context configurator from inheritance browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addContainmentBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">
<h3>addContainmentBrowserToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addContainmentBrowserToolbarConfigurator</span><wbr/><span class="parameters">(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new Toolbar configurator to containment browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeContainmentBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">
<h3>removeContainmentBrowserToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeContainmentBrowserToolbarConfigurator</span><wbr/><span class="parameters">(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Removes  Toolbar configurator from containment browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addExtensionsBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">
<h3>addExtensionsBrowserToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addExtensionsBrowserToolbarConfigurator</span><wbr/><span class="parameters">(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new Toolbar configurator to extensions browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeExtensionsBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">
<h3>removeExtensionsBrowserToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeExtensionsBrowserToolbarConfigurator</span><wbr/><span class="parameters">(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Removes  Toolbar configurator from extensions browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSearchBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">
<h3>addSearchBrowserToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSearchBrowserToolbarConfigurator</span><wbr/><span class="parameters">(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Adds new Toolbar configurator for search browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSearchBrowserToolbarConfigurator(com.nomagic.magicdraw.actions.BrowserToolbarAMConfigurator)">
<h3>removeSearchBrowserToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeSearchBrowserToolbarConfigurator</span><wbr/><span class="parameters">(<a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a> configurator)</span></div>
<div class="block">Removes Toolbar configurator from search browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addInheritanceBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addInheritanceBrowserShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addInheritanceBrowserShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds new shortcuts' configurator to inheritance browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeInheritanceBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeInheritanceBrowserShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeInheritanceBrowserShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes  shortcuts configurator from inheritance browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addDiagramsBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addDiagramsBrowserShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addDiagramsBrowserShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds new shortcuts' configurator to diagrams browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeDiagramsBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeDiagramsBrowserShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeDiagramsBrowserShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes  shortcuts configurator from diagrams browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addLockViewBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addLockViewBrowserShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addLockViewBrowserShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds new shortcuts' configurator to lock view browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeLockViewBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeLockViewBrowserShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeLockViewBrowserShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes  shortcuts configurator from lock view browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addExtensionsBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addExtensionsBrowserShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addExtensionsBrowserShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds new shortcuts' configurator to extensions browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeExtensionsBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeExtensionsBrowserShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeExtensionsBrowserShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes shortcuts configurator from extensions browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSearchBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addSearchBrowserShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSearchBrowserShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds new shortcuts' configurator to search browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSearchBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeSearchBrowserShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeSearchBrowserShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes shortcuts configurator from search browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addContainmentBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addContainmentBrowserShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addContainmentBrowserShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds new shortcuts' configurator to containment browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeContainmentBrowserShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeContainmentBrowserShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeContainmentBrowserShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes  shortcuts configurator from containment browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMainMenuConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeMainMenuConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMainMenuConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes configurator from main menu configuration.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addMainMenuConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addMainMenuConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMainMenuConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds configurator to main menu. This method should be called before menu becomes visible.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator will be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addCreateDiagramDialogConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addCreateDiagramDialogConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCreateDiagramDialogConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds configurator to configure actions inside the dialog which opens when action in main menu or toolbar "Create Diagram" is executed.
 To configure actions inside context menu please see <a href="#addDialogActionsConfigurator(java.lang.String,com.nomagic.actions.ActionsManager,com.nomagic.actions.AMConfigurator)"><code>addDialogActionsConfigurator(String, ActionsManager, AMConfigurator)</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - actions configurator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeCreateDiagramDialogConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeCreateDiagramDialogConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeCreateDiagramDialogConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Remove configurator to configure actions inside "Create Diagram" dialog.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to be removed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addDialogActionsConfigurator(java.lang.String,com.nomagic.actions.ActionsManager,com.nomagic.actions.AMConfigurator)">
<h3>addDialogActionsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addDialogActionsConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> categoryID,
 <a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds configurator to configure actions inside specific popup dialog which constructs its actions only when respective popup menu item is clicked.<br/>
<p>
 Call this method inside <a href="BrowserContextAMConfigurator.html#configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.ui.browser.Tree)"><code>BrowserContextAMConfigurator.configure(ActionsManager, Tree)</code></a> in order to configure browser context menu actions.
 Call this method inside (@link <a href="DiagramContextAMConfigurator.html#configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement%5B%5D,com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>DiagramContextAMConfigurator.configure(ActionsManager, DiagramPresentationElement, PresentationElement[], PresentationElement)</code></a>
 to configure diagram context menu actions</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>categoryID</code> - id of the category which represents the dialog to be configured. Most common examples:<br/>
<a href="ActionsID.html#NEW_ELEMENT_CATEGORY_ID"><code>ActionsID.NEW_ELEMENT_CATEGORY_ID</code></a> - to configure "Create Element" context action<br/>
<a href="ActionsID.html#NEW_DIAGRAM_CATEGORY_ID"><code>ActionsID.NEW_DIAGRAM_CATEGORY_ID</code></a> - to configure "Create Diagram" context action<br/>
<a href="ActionsID.html#NEW_RELATION_CATEGORY_FROM_ID"><code>ActionsID.NEW_RELATION_CATEGORY_FROM_ID</code></a> - to configure "Create Relation-&gt;Outgoing" context action<br/>
<a href="ActionsID.html#NEW_RELATION_CATEGORY_TO_ID"><code>ActionsID.NEW_RELATION_CATEGORY_TO_ID</code></a> - to configure "Create Relation-&gt;Outgoing" context action<br/></dd>
<dd><code>manager</code> - actions manager that contains the category with the given id.
                     Category may be empty at the time this method is called. since category actions are only created when the menu item is clicked
                     Category may not exist in the manager, in that case nothing will get configured.
                     Category should not be added to the manager manually if it is not present.</dd>
<dd><code>configurator</code> - actions configurator which will be called when constructing actions (when displaying the dialog with actions)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeDiagramNavigationConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeDiagramNavigationConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeDiagramNavigationConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes configurator from diagram navigation configuration.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addDiagramNavigationConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addDiagramNavigationConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addDiagramNavigationConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds configurator to diagram navigation toolbar. This method should be called before menu becomes visible.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMainShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeMainShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMainShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes configurator for main shortcuts.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator will be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addMainShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addMainShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMainShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds configurator for main shortcuts.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator will be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeCustomizableShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeCustomizableShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeCustomizableShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes configurator for main shortcuts.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator will be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addCustomizableShortcutsConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addCustomizableShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCustomizableShortcutsConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds configurator for main shortcuts.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator will be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addMainToolbarConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>addMainToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMainToolbarConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Adds configurator to main toolbar. This method should be called before toolbar becomes visible.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator will be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMainToolbarConfigurator(com.nomagic.actions.AMConfigurator)">
<h3>removeMainToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMainToolbarConfigurator</span><wbr/><span class="parameters">(<a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Removes configurator from main toolbar.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator will be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addDiagramToolbarActionsProvider(java.lang.String,com.nomagic.magicdraw.ui.actions.CustomizableDiagramToolbarActionsProvider)">
<h3>addDiagramToolbarActionsProvider</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addDiagramToolbarActionsProvider</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../ui/actions/CustomizableDiagramToolbarActionsProvider.html" title="interface in com.nomagic.magicdraw.ui.actions">CustomizableDiagramToolbarActionsProvider</a> provider)</span></div>
<div class="block">Adds new toolbar provider for given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type.</dd>
<dd><code>provider</code> - action provider to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeDiagramToolbarActionsProvider(java.lang.String,com.nomagic.magicdraw.ui.actions.CustomizableDiagramToolbarActionsProvider)">
<h3>removeDiagramToolbarActionsProvider</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeDiagramToolbarActionsProvider</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../ui/actions/CustomizableDiagramToolbarActionsProvider.html" title="interface in com.nomagic.magicdraw.ui.actions">CustomizableDiagramToolbarActionsProvider</a> provider)</span></div>
<div class="block">Removes action provider for specified diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>provider</code> - action provider to be removed.</dd>
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
