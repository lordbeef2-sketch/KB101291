# JAVA OPENAPI: Tree (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/browser/Tree.html
- source_path: `com/nomagic/magicdraw/ui/browser/Tree.html`
- source_sha256: `1fde08054c4a46ac43da096013e1f313755d738965628b9c204d56de97f271a5`
- captured_utc: `2026-07-14T16:55:52.473428+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.browser](package-summary.html)

## Class Tree

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.awt.Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)
[java.awt.Container](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html)
[javax.swing.JComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html)
[javax.swing.JPanel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html)
[com.nomagic.ui.ExtendedPanel](../../../ui/ExtendedPanel.html)
[com.nomagic.magicdraw.ui.browser.AbstractTree](AbstractTree.html)
com.nomagic.magicdraw.ui.browser.Tree

All Implemented Interfaces:
`com.nomagic.awt.PopupOwner`, `com.nomagic.magicdraw.ui.Updatable`, `[Cachable](../../../ui/Cachable.html)`, `[Autoscroll](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/dnd/Autoscroll.html)`, `[FocusListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/FocusListener.html)`, `[ImageObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html)`, `[MenuContainer](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/MenuContainer.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`, `[Accessible](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/accessibility/Accessible.html)`

Direct Known Subclasses:
`[BrowserTabTree](BrowserTabTree.html)`

@OpenApipublic classTree
extends [AbstractTree](AbstractTree.html)
implements [Autoscroll](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/dnd/Autoscroll.html), com.nomagic.awt.PopupOwner, com.nomagic.magicdraw.ui.Updatable, [Cachable](../../../ui/Cachable.html)

The tree used in MagicDraw browser.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.ui.browser.Tree)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected static final [Node](Node.html)[]`
`[LOADING_DUMMY_NODE_DISTINCTION](#LOADING_DUMMY_NODE_DISTINCTION)`
Fields inherited from class com.nomagic.magicdraw.ui.browser.[AbstractTree](AbstractTree.html)
`[MAX_AUTO_EXPAND_DEPTH](AbstractTree.html#MAX_AUTO_EXPAND_DEPTH)`
Fields inherited from class com.nomagic.ui.[ExtendedPanel](../../../ui/ExtendedPanel.html)
`[DEFAULT_FOCUSABLE](../../../ui/ExtendedPanel.html#DEFAULT_FOCUSABLE)`
Fields inherited from class javax.swing.[JComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html)
`[listenerList](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#listenerList), [TOOL_TIP_TEXT_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#TOOL_TIP_TEXT_KEY), [ui](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#ui), [UNDEFINED_CONDITION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#UNDEFINED_CONDITION), [WHEN_ANCESTOR_OF_FOCUSED_COMPONENT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#WHEN_ANCESTOR_OF_FOCUSED_COMPONENT), [WHEN_FOCUSED](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#WHEN_FOCUSED), [WHEN_IN_FOCUSED_WINDOW](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#WHEN_IN_FOCUSED_WINDOW)`
Fields inherited from class java.awt.[Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)
`[accessibleContext](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#accessibleContext), [BOTTOM_ALIGNMENT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#BOTTOM_ALIGNMENT), [CENTER_ALIGNMENT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#CENTER_ALIGNMENT), [LEFT_ALIGNMENT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#LEFT_ALIGNMENT), [RIGHT_ALIGNMENT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#RIGHT_ALIGNMENT), [TOP_ALIGNMENT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#TOP_ALIGNMENT)`
Fields inherited from interface java.awt.image.[ImageObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html)
`[ABORT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#ABORT), [ALLBITS](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#ALLBITS), [ERROR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#ERROR), [FRAMEBITS](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#FRAMEBITS), [HEIGHT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#HEIGHT), [PROPERTIES](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#PROPERTIES), [SOMEBITS](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#SOMEBITS), [WIDTH](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#WIDTH)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Tree](#%3Cinit%3E(com.nomagic.magicdraw.ui.browser.TreeParams))(com.nomagic.magicdraw.ui.browser.TreeParams params)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addTreeSelectionParticipant](#addTreeSelectionParticipant(com.nomagic.magicdraw.ui.browser.Tree.TreeSelectionParticipant))(com.nomagic.magicdraw.ui.browser.Tree.TreeSelectionParticipant participant)`
Adds tree selection participant
`void`
`[autoscroll](#autoscroll(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)`
Implementation of auto-scroll interface method
 auto-scroll(Point)
 Scrolls to specified point.
`protected void`
`[browserUpdateDelayed](#browserUpdateDelayed(boolean))(boolean updateOnlyDirty)`
Called if browser lazy and update vas delayed
`boolean`
`[canDelete](#canDelete(com.nomagic.magicdraw.ui.browser.Node%5B%5D))([Node](Node.html)[] node)`
Test if all nodes can be deleted
`void`
`[collectSelectedNodes](#collectSelectedNodes(com.nomagic.magicdraw.ui.browser.TreeModel,javax.swing.tree.TreePath,com.nomagic.magicdraw.ui.browser.TreeSelectionTracker))(com.nomagic.magicdraw.ui.browser.TreeModel treeModel,
 [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html) parentPath,
 com.nomagic.magicdraw.ui.browser.TreeSelectionTracker selectionTracker)`
Collects selected nodes.
`void`
`[decorateTree](#decorateTree())()`

`void`
`[delete](#delete(com.nomagic.magicdraw.ui.browser.Node%5B%5D))([Node](Node.html)[] node)`

`void`
`[delete](#delete(com.nomagic.magicdraw.ui.browser.Node%5B%5D,boolean,com.dassault_systemes.modeler.foundation.editing.MacroCommand))([Node](Node.html)[] nodes,
 boolean useSpecificDeletion,
 com.dassault_systemes.modeler.foundation.editing.MacroCommand macroCommand)`
Deletes nodes
`void`
`[dispose](#dispose())()`
Removes all nodes recursively.
`void`
`[disposeNodes](#disposeNodes())()`
Dispose nodes added into the tree.
`protected void`
`[doBeforeOpenNode](#doBeforeOpenNode())()`

`protected void`
`[doubleClick](#doubleClick(javax.swing.tree.DefaultMutableTreeNode,java.awt.event.MouseEvent))([DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html) node,
 [MouseEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html) event)`
called on mouse double click on nod.
`void`
`[doubleClickAction](#doubleClickAction(com.nomagic.magicdraw.ui.browser.Node,java.awt.event.MouseEvent))([Node](Node.html) node,
 [MouseEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html) event)`
Edit action invoked if somebody did double click on some node
`void`
`[editAction](#editAction(com.nomagic.magicdraw.ui.browser.Node,java.awt.AWTEvent))([Node](Node.html) node,
 [AWTEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html) event)`
Edit action invoked if somebody pressed Enter on node
`void`
`[editPath](#editPath(javax.swing.tree.TreePath))([TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html) path)`

`protected [ActionsManager](../../../actions/ActionsManager.html)`
`[getActions](#getActions())()`
Returns shortcuts action manager for this browser.
`[Insets](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Insets.html)`
`[getAutoscrollInsets](#getAutoscrollInsets())()`

`[Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)`
`[getDefaultFocusable](#getDefaultFocusable())()`
Request Focus for some component.
`[Node](Node.html)`
`[getNode](#getNode(int))(int row)`
Returns first selected node in the tree.
`com.nomagic.magicdraw.ui.browser.TreeParams`
`[getParams](#getParams())()`

`[Node](Node.html)`
`[getRootNode](#getRootNode())()`
Returns root node of the tree.
`[Node](Node.html)`
`[getSelectedNode](#getSelectedNode())()`
Returns first selected node in the tree.
`[Node](Node.html)[]`
`[getSelectedNodes](#getSelectedNodes())()`
Returns all selected nodes in the tree.
`com.nomagic.magicdraw.ui.browser.TreeModel`
`[getTreeModel](#getTreeModel())()`

`void`
`[init](#init())()`

`void`
`[init](#init(com.nomagic.magicdraw.ui.browser.Node))([Node](Node.html) rootNode)`

`<A> void`
`[initAsync](#initAsync(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler))(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler)`

`<A> void`
`[initAsync](#initAsync(com.nomagic.magicdraw.ui.browser.Node,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler))([Node](Node.html) root,
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler)`

`protected boolean`
`[isShowOwner](#isShowOwner())()`

`boolean`
`[isUpdateIfShowing](#isUpdateIfShowing())()`
Returns if tree only updates when showing
`protected static <A> void`
`[maybeInvokeChainedCH](#maybeInvokeChainedCH(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,java.lang.Throwable))(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) exc)`

`protected <A> void`
`[maybeInvokeChainedHandler](#maybeInvokeChainedHandler(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,com.nomagic.magicdraw.ui.browser.TreeModel,java.lang.Throwable))(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler,
 com.nomagic.magicdraw.ui.browser.TreeModel browserModel,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) exc)`

`protected static <A> void`
`[maybeInvokeChainedHandler](#maybeInvokeChainedHandler(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,java.lang.Throwable))(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) exc)`

`final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html)`
`[openNode](#openNode(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) object)`
Opens(expands) node for a give Element.
`final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html)`
`[openNode](#openNode(com.nomagic.magicdraw.uml.BaseElement,boolean))([BaseElement](../../uml/BaseElement.html) object,
 boolean requestFocus)`
Opens(expands) node for a give Element.
`final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html)`
`[openNode](#openNode(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean))([BaseElement](../../uml/BaseElement.html) object,
 boolean select,
 boolean requestFocus)`
Opens(expands) node for a give Element.
`final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html)`
`[openNode](#openNode(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean))([BaseElement](../../uml/BaseElement.html) object,
 boolean select,
 boolean appendSelection,
 boolean requestFocus)`
Opens(expands) node for a give Element.
`final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html)`
`[openNode](#openNode(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,boolean))([BaseElement](../../uml/BaseElement.html) object,
 boolean select,
 boolean appendSelection,
 boolean requestFocus,
 boolean scrollToVisible)`
Opens(expands) node for a give Element.
`final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html)`
`[openNode](#openNode(com.nomagic.magicdraw.uml.BaseElement,com.dassault_systemes.modeler.magic.ui.ElementSelection,boolean))([BaseElement](../../uml/BaseElement.html) object,
 com.dassault_systemes.modeler.magic.ui.ElementSelection selection,
 boolean appendSelection)`

`final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html)`
`[openNode](#openNode(com.nomagic.magicdraw.uml.BaseElement,com.dassault_systemes.modeler.magic.ui.ElementSelection,boolean,boolean,boolean,boolean))([BaseElement](../../uml/BaseElement.html) object,
 com.dassault_systemes.modeler.magic.ui.ElementSelection selection,
 boolean select,
 boolean appendSelection,
 boolean requestFocus,
 boolean scrollToVisible)`

`void`
`[openNode](#openNode(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../../uml/BaseElement.html)> elements)`

`<T extends [BaseElement](../../uml/BaseElement.html)> 
void`
`[openNode](#openNode(java.util.Collection,java.util.function.Consumer))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> elements,
 [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<T> failedConsumer)`

`void`
`[removeAction](#removeAction(com.nomagic.magicdraw.ui.browser.Node%5B%5D))([Node](Node.html)[] node)`
Edit action invoked if somebody pressed DELETE on node
`void`
`[reset](#reset())()`
Cache managers invokes this method to free resources.
`protected static void`
`[setBrowserForActions](#setBrowserForActions(com.nomagic.magicdraw.ui.browser.Tree,com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.ui.ElementSelectionProvider))([Tree](Tree.html) tree,
 [ActionsManager](../../../actions/ActionsManager.html) manager,
 com.nomagic.magicdraw.ui.ElementSelectionProvider provider)`

`void`
`[setIgnoreLock](#setIgnoreLock(boolean))(boolean ignoreLock)`

`void`
`[setSelectedNodes](#setSelectedNodes(com.nomagic.magicdraw.ui.browser.Node%5B%5D))([Node](Node.html)[] nodes)`
Selects given nodes in the tree.
`void`
`[setUpdateIfShowing](#setUpdateIfShowing(boolean))(boolean updateIfShowing)`
Allows setting tree to update only if showing
`void`
`[showPopupMenu](#showPopupMenu(java.awt.event.MouseEvent))([MouseEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html) evt)`

`protected void`
`[specificUpdateBrowser](#specificUpdateBrowser(boolean))(boolean updateOnlyDirty)`

`static [Node](Node.html)[]`
`[toNodes](#toNodes(javax.swing.tree.TreePath%5B%5D))([TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html)[] paths)`
Utility method for converting array of paths to array of nodes
`protected static [Node](Node.html)[]`
`[toNodes](#toNodes(javax.swing.tree.TreePath%5B%5D,boolean))([TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html)[] paths,
 boolean loadingDummyNodeDistinction)`

`static [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html)[]`
`[toTreePaths](#toTreePaths(com.nomagic.magicdraw.ui.browser.Node%5B%5D))([Node](Node.html)[] nodes)`
Utility method for converting array of nodes to array of paths
`void`
`[update](#update(boolean))(boolean deepUpdate)`
Update component UI by model.
`final boolean`
`[updateBrowser](#updateBrowser())()`
Updates dirty nodes in tree with the newest data and shows it.
`final boolean`
`[updateBrowser](#updateBrowser(boolean))(boolean updateOnlyDirty)`
Updates tree with the newest data and shows it.
`final boolean`
`[updateBrowser](#updateBrowser(boolean,boolean))(boolean updateOnlyDirty,
 boolean updateNotShowing)`
Updates tree with the newest data and shows it.
`<A> void`
`[updateBrowserAsync](#updateBrowserAsync(boolean,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,com.nomagic.task.ProgressStatus))(boolean updateOnlyDirty,
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`

`protected <A> boolean`
`[updateOnlyDirtyNodes](#updateOnlyDirtyNodes(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,boolean))(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler,
 boolean updateAll)`

`void`
`[updateUI](#updateUI())()`

`protected boolean`
`[waitForPreviousEventsOnOpeningNode](#waitForPreviousEventsOnOpeningNode())()`
Methods inherited from class com.nomagic.magicdraw.ui.browser.[AbstractTree](AbstractTree.html)
`[close](AbstractTree.html#close()), [getCookies](AbstractTree.html#getCookies()), [getScrollPane](AbstractTree.html#getScrollPane()), [getTree](AbstractTree.html#getTree()), [isAutoExpandMode](AbstractTree.html#isAutoExpandMode()), [open](AbstractTree.html#open()), [openPath](AbstractTree.html#openPath(javax.swing.tree.TreePath)), [openPath](AbstractTree.html#openPath(javax.swing.tree.TreePath,boolean,boolean,boolean)), [openPath](AbstractTree.html#openPath(javax.swing.tree.TreePath,boolean,boolean,boolean,boolean)), [setAutoExpandMode](AbstractTree.html#setAutoExpandMode(boolean)), [setTree](AbstractTree.html#setTree(javax.swing.JTree))`
Methods inherited from class com.nomagic.ui.[ExtendedPanel](../../../ui/ExtendedPanel.html)
`[addActionListenerFor](../../../ui/ExtendedPanel.html#addActionListenerFor(java.awt.event.ActionListener,java.awt.Component)), [addEnterOKListener](../../../ui/ExtendedPanel.html#addEnterOKListener(java.awt.event.KeyListener)), [addFocusListenerFor](../../../ui/ExtendedPanel.html#addFocusListenerFor(java.awt.event.FocusListener,java.awt.Component)), [addKeyListenerFor](../../../ui/ExtendedPanel.html#addKeyListenerFor(java.awt.event.KeyListener,java.awt.Component)), [cancel](../../../ui/ExtendedPanel.html#cancel()), [clear](../../../ui/ExtendedPanel.html#clear()), [enableComponent](../../../ui/ExtendedPanel.html#enableComponent(boolean,java.awt.Component)), [focusGained](../../../ui/ExtendedPanel.html#focusGained(java.awt.event.FocusEvent)), [focusLost](../../../ui/ExtendedPanel.html#focusLost(java.awt.event.FocusEvent)), [getEditingState](../../../ui/ExtendedPanel.html#getEditingState()), [getErrorString](../../../ui/ExtendedPanel.html#getErrorString()), [getParentWindow](../../../ui/ExtendedPanel.html#getParentWindow()), [initialize](../../../ui/ExtendedPanel.html#initialize()), [isDataValid](../../../ui/ExtendedPanel.html#isDataValid()), [ok](../../../ui/ExtendedPanel.html#ok()), [removeFocusListenerFor](../../../ui/ExtendedPanel.html#removeFocusListenerFor(java.awt.event.FocusListener,java.awt.Component)), [removeKeyListenerFor](../../../ui/ExtendedPanel.html#removeKeyListenerFor(java.awt.event.KeyListener,java.awt.Component)), [setEditingState](../../../ui/ExtendedPanel.html#setEditingState(boolean)), [setEnabled](../../../ui/ExtendedPanel.html#setEnabled(boolean,java.awt.Component)), [setEnabledAll](../../../ui/ExtendedPanel.html#setEnabledAll(boolean)), [updateByStateRecursively](../../../ui/ExtendedPanel.html#updateByStateRecursively(boolean,java.awt.Component)), [updatePanelByEditingState](../../../ui/ExtendedPanel.html#updatePanelByEditingState()), [updatePanelByEditingState](../../../ui/ExtendedPanel.html#updatePanelByEditingState(boolean))`
Methods inherited from class javax.swing.[JPanel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html)
`[getAccessibleContext](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html#getAccessibleContext()), [getUI](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html#getUI()), [getUIClassID](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html#getUIClassID()), [paramString](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html#paramString()), [setUI](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html#setUI(javax.swing.plaf.PanelUI))`
Methods inherited from class javax.swing.[JComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html)
`[addAncestorListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#addAncestorListener(javax.swing.event.AncestorListener)), [addNotify](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#addNotify()), [addVetoableChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#addVetoableChangeListener(java.beans.VetoableChangeListener)), [computeVisibleRect](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#computeVisibleRect(java.awt.Rectangle)), [contains](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#contains(int,int)), [createToolTip](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#createToolTip()), [disable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#disable()), [enable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#enable()), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#firePropertyChange(java.lang.String,boolean,boolean)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#firePropertyChange(java.lang.String,char,char)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#firePropertyChange(java.lang.String,int,int)), [fireVetoableChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#fireVetoableChange(java.lang.String,java.lang.Object,java.lang.Object)), [getActionForKeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getActionForKeyStroke(javax.swing.KeyStroke)), [getActionMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getActionMap()), [getAlignmentX](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getAlignmentX()), [getAlignmentY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getAlignmentY()), [getAncestorListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getAncestorListeners()), [getAutoscrolls](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getAutoscrolls()), [getBaseline](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getBaseline(int,int)), [getBaselineResizeBehavior](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getBaselineResizeBehavior()), [getBorder](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getBorder()), [getBounds](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getBounds(java.awt.Rectangle)), [getClientProperty](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getClientProperty(java.lang.Object)), [getComponentGraphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getComponentGraphics(java.awt.Graphics)), [getComponentPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getComponentPopupMenu()), [getConditionForKeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getConditionForKeyStroke(javax.swing.KeyStroke)), [getDebugGraphicsOptions](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getDebugGraphicsOptions()), [getDefaultLocale](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getDefaultLocale()), [getFontMetrics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getFontMetrics(java.awt.Font)), [getGraphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getGraphics()), [getHeight](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getHeight()), [getInheritsPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getInheritsPopupMenu()), [getInputMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getInputMap()), [getInputMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getInputMap(int)), [getInputVerifier](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getInputVerifier()), [getInsets](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getInsets()), [getInsets](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getInsets(java.awt.Insets)), [getListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getListeners(java.lang.Class)), [getLocation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getLocation(java.awt.Point)), [getMaximumSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getMaximumSize()), [getMinimumSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getMinimumSize()), [getNextFocusableComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getNextFocusableComponent()), [getPopupLocation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getPopupLocation(java.awt.event.MouseEvent)), [getPreferredSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getPreferredSize()), [getRegisteredKeyStrokes](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getRegisteredKeyStrokes()), [getRootPane](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getRootPane()), [getSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getSize(java.awt.Dimension)), [getToolTipLocation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getToolTipLocation(java.awt.event.MouseEvent)), [getToolTipText](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getToolTipText()), [getToolTipText](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getToolTipText(java.awt.event.MouseEvent)), [getTopLevelAncestor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getTopLevelAncestor()), [getTransferHandler](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getTransferHandler()), [getVerifyInputWhenFocusTarget](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getVerifyInputWhenFocusTarget()), [getVetoableChangeListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getVetoableChangeListeners()), [getVisibleRect](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getVisibleRect()), [getWidth](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getWidth()), [getX](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getX()), [getY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getY()), [grabFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#grabFocus()), [hide](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#hide()), [isDoubleBuffered](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isDoubleBuffered()), [isLightweightComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isLightweightComponent(java.awt.Component)), [isManagingFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isManagingFocus()), [isOpaque](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isOpaque()), [isOptimizedDrawingEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isOptimizedDrawingEnabled()), [isPaintingForPrint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isPaintingForPrint()), [isPaintingOrigin](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isPaintingOrigin()), [isPaintingTile](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isPaintingTile()), [isRequestFocusEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isRequestFocusEnabled()), [isValidateRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isValidateRoot()), [paint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#paint(java.awt.Graphics)), [paintBorder](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#paintBorder(java.awt.Graphics)), [paintChildren](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#paintChildren(java.awt.Graphics)), [paintComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#paintComponent(java.awt.Graphics)), [paintImmediately](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#paintImmediately(int,int,int,int)), [paintImmediately](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#paintImmediately(java.awt.Rectangle)), [print](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#print(java.awt.Graphics)), [printAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#printAll(java.awt.Graphics)), [printBorder](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#printBorder(java.awt.Graphics)), [printChildren](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#printChildren(java.awt.Graphics)), [printComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#printComponent(java.awt.Graphics)), [processComponentKeyEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#processComponentKeyEvent(java.awt.event.KeyEvent)), [processKeyBinding](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#processKeyBinding(javax.swing.KeyStroke,java.awt.event.KeyEvent,int,boolean)), [processKeyEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#processKeyEvent(java.awt.event.KeyEvent)), [processMouseEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#processMouseEvent(java.awt.event.MouseEvent)), [processMouseMotionEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#processMouseMotionEvent(java.awt.event.MouseEvent)), [putClientProperty](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#putClientProperty(java.lang.Object,java.lang.Object)), [registerKeyboardAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#registerKeyboardAction(java.awt.event.ActionListener,java.lang.String,javax.swing.KeyStroke,int)), [registerKeyboardAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#registerKeyboardAction(java.awt.event.ActionListener,javax.swing.KeyStroke,int)), [removeAncestorListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#removeAncestorListener(javax.swing.event.AncestorListener)), [removeNotify](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#removeNotify()), [removeVetoableChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#removeVetoableChangeListener(java.beans.VetoableChangeListener)), [repaint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#repaint(long,int,int,int,int)), [repaint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#repaint(java.awt.Rectangle)), [requestDefaultFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#requestDefaultFocus()), [requestFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#requestFocus()), [requestFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#requestFocus(boolean)), [requestFocusInWindow](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#requestFocusInWindow()), [requestFocusInWindow](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#requestFocusInWindow(boolean)), [resetKeyboardActions](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#resetKeyboardActions()), [reshape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#reshape(int,int,int,int)), [revalidate](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#revalidate()), [scrollRectToVisible](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#scrollRectToVisible(java.awt.Rectangle)), [setActionMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setActionMap(javax.swing.ActionMap)), [setAlignmentX](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setAlignmentX(float)), [setAlignmentY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setAlignmentY(float)), [setAutoscrolls](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setAutoscrolls(boolean)), [setBackground](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setBackground(java.awt.Color)), [setBorder](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setBorder(javax.swing.border.Border)), [setComponentPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setComponentPopupMenu(javax.swing.JPopupMenu)), [setDebugGraphicsOptions](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setDebugGraphicsOptions(int)), [setDefaultLocale](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setDefaultLocale(java.util.Locale)), [setDoubleBuffered](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setDoubleBuffered(boolean)), [setEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setEnabled(boolean)), [setFocusTraversalKeys](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setFocusTraversalKeys(int,java.util.Set)), [setFont](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setFont(java.awt.Font)), [setForeground](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setForeground(java.awt.Color)), [setInheritsPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setInheritsPopupMenu(boolean)), [setInputMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setInputMap(int,javax.swing.InputMap)), [setInputVerifier](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setInputVerifier(javax.swing.InputVerifier)), [setMaximumSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setMaximumSize(java.awt.Dimension)), [setMinimumSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setMinimumSize(java.awt.Dimension)), [setNextFocusableComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setNextFocusableComponent(java.awt.Component)), [setOpaque](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setOpaque(boolean)), [setPreferredSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setPreferredSize(java.awt.Dimension)), [setRequestFocusEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setRequestFocusEnabled(boolean)), [setToolTipText](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setToolTipText(java.lang.String)), [setTransferHandler](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setTransferHandler(javax.swing.TransferHandler)), [setUI](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setUI(javax.swing.plaf.ComponentUI)), [setVerifyInputWhenFocusTarget](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setVerifyInputWhenFocusTarget(boolean)), [setVisible](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setVisible(boolean)), [unregisterKeyboardAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#unregisterKeyboardAction(javax.swing.KeyStroke)), [update](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#update(java.awt.Graphics))`
Methods inherited from class java.awt.[Container](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html)
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component)), [add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component,int)), [add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component,java.lang.Object)), [add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component,java.lang.Object,int)), [add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.lang.String,java.awt.Component)), [addContainerListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#addContainerListener(java.awt.event.ContainerListener)), [addImpl](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#addImpl(java.awt.Component,java.lang.Object,int)), [addPropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addPropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)), [applyComponentOrientation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#applyComponentOrientation(java.awt.ComponentOrientation)), [areFocusTraversalKeysSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#areFocusTraversalKeysSet(int)), [countComponents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#countComponents()), [deliverEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#deliverEvent(java.awt.Event)), [doLayout](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#doLayout()), [findComponentAt](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#findComponentAt(int,int)), [findComponentAt](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#findComponentAt(java.awt.Point)), [getComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponent(int)), [getComponentAt](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentAt(int,int)), [getComponentAt](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentAt(java.awt.Point)), [getComponentCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentCount()), [getComponents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponents()), [getComponentZOrder](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentZOrder(java.awt.Component)), [getContainerListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getContainerListeners()), [getFocusTraversalKeys](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getFocusTraversalKeys(int)), [getFocusTraversalPolicy](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getFocusTraversalPolicy()), [getLayout](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getLayout()), [getMousePosition](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getMousePosition(boolean)), [insets](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#insets()), [invalidate](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#invalidate()), [isAncestorOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isAncestorOf(java.awt.Component)), [isFocusCycleRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusCycleRoot()), [isFocusCycleRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusCycleRoot(java.awt.Container)), [isFocusTraversalPolicyProvider](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusTraversalPolicyProvider()), [isFocusTraversalPolicySet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusTraversalPolicySet()), [layout](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#layout()), [list](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#list(java.io.PrintStream,int)), [list](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#list(java.io.PrintWriter,int)), [locate](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#locate(int,int)), [minimumSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#minimumSize()), [paintComponents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#paintComponents(java.awt.Graphics)), [preferredSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#preferredSize()), [printComponents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#printComponents(java.awt.Graphics)), [processContainerEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#processContainerEvent(java.awt.event.ContainerEvent)), [processEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#processEvent(java.awt.AWTEvent)), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#remove(int)), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#remove(java.awt.Component)), [removeAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#removeAll()), [removeContainerListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#removeContainerListener(java.awt.event.ContainerListener)), [setComponentZOrder](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setComponentZOrder(java.awt.Component,int)), [setFocusCycleRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFocusCycleRoot(boolean)), [setFocusTraversalPolicy](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)), [setFocusTraversalPolicyProvider](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFocusTraversalPolicyProvider(boolean)), [setLayout](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setLayout(java.awt.LayoutManager)), [transferFocusDownCycle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#transferFocusDownCycle()), [validate](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#validate()), [validateTree](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#validateTree())`
Methods inherited from class java.awt.[Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)
`[action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#action(java.awt.Event,java.lang.Object)), [add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#add(java.awt.PopupMenu)), [addComponentListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addComponentListener(java.awt.event.ComponentListener)), [addFocusListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addFocusListener(java.awt.event.FocusListener)), [addHierarchyBoundsListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)), [addHierarchyListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addHierarchyListener(java.awt.event.HierarchyListener)), [addInputMethodListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addInputMethodListener(java.awt.event.InputMethodListener)), [addKeyListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addKeyListener(java.awt.event.KeyListener)), [addMouseListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addMouseListener(java.awt.event.MouseListener)), [addMouseMotionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addMouseMotionListener(java.awt.event.MouseMotionListener)), [addMouseWheelListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addMouseWheelListener(java.awt.event.MouseWheelListener)), [bounds](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#bounds()), [checkImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#checkImage(java.awt.Image,int,int,java.awt.image.ImageObserver)), [checkImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#checkImage(java.awt.Image,java.awt.image.ImageObserver)), [coalesceEvents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#coalesceEvents(java.awt.AWTEvent,java.awt.AWTEvent)), [contains](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#contains(java.awt.Point)), [createImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createImage(int,int)), [createImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createImage(java.awt.image.ImageProducer)), [createVolatileImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createVolatileImage(int,int)), [createVolatileImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createVolatileImage(int,int,java.awt.ImageCapabilities)), [disableEvents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#disableEvents(long)), [dispatchEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#dispatchEvent(java.awt.AWTEvent)), [enable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enable(boolean)), [enableEvents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enableEvents(long)), [enableInputMethods](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enableInputMethods(boolean)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,byte,byte)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,double,double)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,float,float)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,long,long)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,short,short)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getBackground](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBackground()), [getBounds](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBounds()), [getColorModel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getColorModel()), [getComponentListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getComponentListeners()), [getComponentOrientation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getComponentOrientation()), [getCursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getCursor()), [getDropTarget](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getDropTarget()), [getFocusCycleRootAncestor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFocusCycleRootAncestor()), [getFocusListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFocusListeners()), [getFocusTraversalKeysEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFocusTraversalKeysEnabled()), [getFont](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFont()), [getForeground](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getForeground()), [getGraphicsConfiguration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getGraphicsConfiguration()), [getHierarchyBoundsListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getHierarchyBoundsListeners()), [getHierarchyListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getHierarchyListeners()), [getIgnoreRepaint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getIgnoreRepaint()), [getInputContext](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getInputContext()), [getInputMethodListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getInputMethodListeners()), [getInputMethodRequests](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getInputMethodRequests()), [getKeyListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getKeyListeners()), [getLocale](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getLocale()), [getLocation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getLocation()), [getLocationOnScreen](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getLocationOnScreen()), [getMouseListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMouseListeners()), [getMouseMotionListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMouseMotionListeners()), [getMousePosition](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMousePosition()), [getMouseWheelListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMouseWheelListeners()), [getName](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getName()), [getParent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getParent()), [getPropertyChangeListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getPropertyChangeListeners()), [getPropertyChangeListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getPropertyChangeListeners(java.lang.String)), [getSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getSize()), [getToolkit](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getToolkit()), [getTreeLock](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getTreeLock()), [gotFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#gotFocus(java.awt.Event,java.lang.Object)), [handleEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#handleEvent(java.awt.Event)), [hasFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#hasFocus()), [imageUpdate](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#imageUpdate(java.awt.Image,int,int,int,int,int)), [inside](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#inside(int,int)), [isBackgroundSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isBackgroundSet()), [isCursorSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isCursorSet()), [isDisplayable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isDisplayable()), [isEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isEnabled()), [isFocusable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFocusable()), [isFocusOwner](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFocusOwner()), [isFocusTraversable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFocusTraversable()), [isFontSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFontSet()), [isForegroundSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isForegroundSet()), [isLightweight](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isLightweight()), [isMaximumSizeSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isMaximumSizeSet()), [isMinimumSizeSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isMinimumSizeSet()), [isPreferredSizeSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isPreferredSizeSet()), [isShowing](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isShowing()), [isValid](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isValid()), [isVisible](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isVisible()), [keyDown](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#keyDown(java.awt.Event,int)), [keyUp](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#keyUp(java.awt.Event,int)), [list](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#list()), [list](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#list(java.io.PrintStream)), [list](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#list(java.io.PrintWriter)), [location](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#location()), [lostFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#lostFocus(java.awt.Event,java.lang.Object)), [mouseDown](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseDown(java.awt.Event,int,int)), [mouseDrag](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseDrag(java.awt.Event,int,int)), [mouseEnter](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseEnter(java.awt.Event,int,int)), [mouseExit](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseExit(java.awt.Event,int,int)), [mouseMove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseMove(java.awt.Event,int,int)), [mouseUp](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseUp(java.awt.Event,int,int)), [move](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#move(int,int)), [nextFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#nextFocus()), [paintAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#paintAll(java.awt.Graphics)), [postEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#postEvent(java.awt.Event)), [prepareImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#prepareImage(java.awt.Image,int,int,java.awt.image.ImageObserver)), [prepareImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#prepareImage(java.awt.Image,java.awt.image.ImageObserver)), [processComponentEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processComponentEvent(java.awt.event.ComponentEvent)), [processFocusEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processFocusEvent(java.awt.event.FocusEvent)), [processHierarchyBoundsEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processHierarchyBoundsEvent(java.awt.event.HierarchyEvent)), [processHierarchyEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processHierarchyEvent(java.awt.event.HierarchyEvent)), [processInputMethodEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processInputMethodEvent(java.awt.event.InputMethodEvent)), [processMouseWheelEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processMouseWheelEvent(java.awt.event.MouseWheelEvent)), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#remove(java.awt.MenuComponent)), [removeComponentListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeComponentListener(java.awt.event.ComponentListener)), [removeFocusListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeFocusListener(java.awt.event.FocusListener)), [removeHierarchyBoundsListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)), [removeHierarchyListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeHierarchyListener(java.awt.event.HierarchyListener)), [removeInputMethodListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeInputMethodListener(java.awt.event.InputMethodListener)), [removeKeyListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeKeyListener(java.awt.event.KeyListener)), [removeMouseListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeMouseListener(java.awt.event.MouseListener)), [removeMouseMotionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeMouseMotionListener(java.awt.event.MouseMotionListener)), [removeMouseWheelListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeMouseWheelListener(java.awt.event.MouseWheelListener)), [removePropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [removePropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removePropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)), [repaint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#repaint()), [repaint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#repaint(int,int,int,int)), [repaint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#repaint(long)), [requestFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocus(boolean,java.awt.event.FocusEvent.Cause)), [requestFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocus(java.awt.event.FocusEvent.Cause)), [requestFocusInWindow](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocusInWindow(java.awt.event.FocusEvent.Cause)), [resize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#resize(int,int)), [resize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#resize(java.awt.Dimension)), [setBounds](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setBounds(int,int,int,int)), [setBounds](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setBounds(java.awt.Rectangle)), [setComponentOrientation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setComponentOrientation(java.awt.ComponentOrientation)), [setCursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setCursor(java.awt.Cursor)), [setDropTarget](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setDropTarget(java.awt.dnd.DropTarget)), [setFocusable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setFocusable(boolean)), [setFocusTraversalKeysEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setFocusTraversalKeysEnabled(boolean)), [setIgnoreRepaint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setIgnoreRepaint(boolean)), [setLocale](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setLocale(java.util.Locale)), [setLocation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setLocation(int,int)), [setLocation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setLocation(java.awt.Point)), [setMixingCutoutShape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setMixingCutoutShape(java.awt.Shape)), [setName](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setName(java.lang.String)), [setSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setSize(int,int)), [setSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setSize(java.awt.Dimension)), [show](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#show()), [show](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#show(boolean)), [size](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#size()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#toString()), [transferFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#transferFocus()), [transferFocusBackward](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#transferFocusBackward()), [transferFocusUpCycle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#transferFocusUpCycle())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.ui.Updatable
`afterAllUpdates, beforeAllUpdates`

============ FIELD DETAIL =========== 
Field Details
LOADING_DUMMY_NODE_DISTINCTION
protected static final [Node](Node.html)[] LOADING_DUMMY_NODE_DISTINCTION
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Tree
public Tree(com.nomagic.magicdraw.ui.browser.TreeParams params)
 ============ METHOD DETAIL ========== 
Method Details
setIgnoreLock
public void setIgnoreLock(boolean ignoreLock)
doubleClick
protected void doubleClick([DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html) node,
 [MouseEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html) event)
Description copied from class: `[AbstractTree](AbstractTree.html#doubleClick(javax.swing.tree.DefaultMutableTreeNode,java.awt.event.MouseEvent))`
called on mouse double click on nod.
Overrides:
`[doubleClick](AbstractTree.html#doubleClick(javax.swing.tree.DefaultMutableTreeNode,java.awt.event.MouseEvent))` in class `[AbstractTree](AbstractTree.html)`
Parameters:
`node` - node on which double click was called.
`event` - double click event
doubleClickAction
public void doubleClickAction([Node](Node.html) node,
 [MouseEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html) event)
Edit action invoked if somebody did double click on some node
Parameters:
`node` - node
`event` - event
editAction
public void editAction([Node](Node.html) node,
 [AWTEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html) event)
Edit action invoked if somebody pressed Enter on node
Parameters:
`node` - node
`event` - action event
removeAction
public void removeAction([Node](Node.html)[] node)
Edit action invoked if somebody pressed DELETE on node
Parameters:
`node` - node
isShowOwner
protected boolean isShowOwner()
updateUI
public void updateUI()
Overrides:
`[updateUI](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html#updateUI())` in class `[JPanel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html)`
update
public void update(boolean deepUpdate)
Description copied from interface: `com.nomagic.magicdraw.ui.Updatable`
Update component UI by model. If deep update component must assume that anything in the model
 could be changed and these changes were not fired (for example when reversing code, or doing teamwork
 update).
Specified by:
`update` in interface `com.nomagic.magicdraw.ui.Updatable`
Parameters:
`deepUpdate` - true if component must assume that anything in the model was changed.
addTreeSelectionParticipant
public void addTreeSelectionParticipant(com.nomagic.magicdraw.ui.browser.Tree.TreeSelectionParticipant participant)
Adds tree selection participant
Parameters:
`participant` - tree selection participant to execute additional methods before and after selection
init
public void init()
init
public void init([Node](Node.html) rootNode)
initAsync
public <A> void initAsync(@CheckForNull
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler)
Type Parameters:
`A` - The type of the object attached to the completion handler
Parameters:
`attachment` - the object for completion handler attached to this operation
`handler` - the handler to consume completion of this operation, see
 [`initAsync(Node, Object, com.nomagic.magicdraw.utils.concurrent.CompletionHandler)`](#initAsync(com.nomagic.magicdraw.ui.browser.Node,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler))
initAsync
public <A> void initAsync([Node](Node.html) root,
 @CheckForNull
 A attachment,
 @CheckForNull
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler)
Parameters:
`root` - root
`attachment` - the object for completion handler attached to this operation
`handler` - the handler to consume completion of this operation or `null`. The
 handler is always invoked on `EventQueue` dispatch thread
maybeInvokeChainedHandler
protected static <A> void maybeInvokeChainedHandler(@CheckForNull
 A attachment,
 @CheckForNull
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler,
 @CheckForNull
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) exc)
maybeInvokeChainedCH
protected static <A> void maybeInvokeChainedCH(@CheckForNull
 A attachment,
 @CheckForNull
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler,
 @CheckForNull
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) exc)
updateBrowser
public final boolean updateBrowser()
Updates dirty nodes in tree with the newest data and shows it.
 The current thread will be blocked until tree update is complete,
 but the event dispatcher is going to continue to process events.
Returns:
true if update was performed
delete
public void delete([Node](Node.html)[] node)
delete
public void delete([Node](Node.html)[] nodes,
 boolean useSpecificDeletion,
 @CheckForNull
 com.dassault_systemes.modeler.foundation.editing.MacroCommand macroCommand)
Deletes nodes
Parameters:
`nodes` - nodes which will be deleted
`useSpecificDeletion` - if true deletes nodes with specific remove command
`macroCommand` - to add delete commands
canDelete
public boolean canDelete([Node](Node.html)[] node)
Test if all nodes can be deleted
Parameters:
`node` - array to check
Returns:
true if all elements can be deleted
updateBrowser
public final boolean updateBrowser(boolean updateOnlyDirty)
Updates tree with the newest data and shows it. The current thread will
 be blocked until tree update is complete, but the event dispatcher
 is going to continue to process events.
Parameters:
`updateOnlyDirty` - - if `true` updates only dirty expanded nodes,
 otherwise - updates all expanded tree nodes
Returns:
true if update was performed
updateBrowser
public final boolean updateBrowser(boolean updateOnlyDirty,
 boolean updateNotShowing)
Updates tree with the newest data and shows it. The current thread will
 be blocked until tree update is complete, but the event dispatcher
 is going to continue to process events.
Parameters:
`updateOnlyDirty` - if `true` updates only dirty expanded nodes,
 otherwise - updates all expanded tree nodes.
`updateNotShowing` - forces update even if component is not showing.
Returns:
true if update was performed
browserUpdateDelayed
protected void browserUpdateDelayed(boolean updateOnlyDirty)
Called if browser lazy and update vas delayed
Parameters:
`updateOnlyDirty` - if `true` updates only dirty expanded nodes,
 otherwise - updates all expanded tree nodes
specificUpdateBrowser
protected void specificUpdateBrowser(boolean updateOnlyDirty)
updateBrowserAsync
public <A> void updateBrowserAsync(boolean updateOnlyDirty,
 @CheckForNull
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler,
 [ProgressStatus](../../../task/ProgressStatus.html) status)
updateOnlyDirtyNodes
protected <A> boolean updateOnlyDirtyNodes(@CheckForNull
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler,
 boolean updateAll)
maybeInvokeChainedHandler
protected <A> void maybeInvokeChainedHandler(@CheckForNull
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<?,? super A> handler,
 com.nomagic.magicdraw.ui.browser.TreeModel browserModel,
 @CheckForNull
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) exc)
getSelectedNode
@CheckForNull
@OpenApipublic [Node](Node.html) getSelectedNode()
Returns first selected node in the tree.
Returns:
first selected node.
getNode
@CheckForNull
@OpenApipublic [Node](Node.html) getNode(int row)
Returns first selected node in the tree.
Returns:
first selected node.
getSelectedNodes
@OpenApipublic [Node](Node.html)[] getSelectedNodes()
Returns all selected nodes in the tree.
Returns:
all selected nodes in the tree.
toNodes
public static [Node](Node.html)[] toNodes(@CheckForNull
 [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html)[] paths)
Utility method for converting array of paths to array of nodes
Parameters:
`paths` - tree paths
Returns:
nodes
toNodes
protected static [Node](Node.html)[] toNodes(@CheckForNull
 [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html)[] paths,
 boolean loadingDummyNodeDistinction)
setSelectedNodes
public void setSelectedNodes(@CheckForNull
 [Node](Node.html)[] nodes)
Selects given nodes in the tree. Deselects everything if nodes are null.
Parameters:
`nodes` - nodes
toTreePaths
@CheckForNullpublic static [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html)[] toTreePaths(@CheckForNull
 [Node](Node.html)[] nodes)
Utility method for converting array of nodes to array of paths
Parameters:
`nodes` - nodes
Returns:
tree paths
openNode
@CheckForNull
@OpenApipublic final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html) openNode(@CheckForNull
 [BaseElement](../../uml/BaseElement.html) object)
Opens(expands) node for a give Element.
Parameters:
`object` - the element to expand in the tree
Returns:
path of opened node
openNode
@CheckForNull
@OpenApipublic final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html) openNode(@CheckForNull
 [BaseElement](../../uml/BaseElement.html) object,
 boolean requestFocus)
Opens(expands) node for a give Element. May request focus for a tree.
Parameters:
`object` - the element to expand in the tree
`requestFocus` - request focus for a tree.
Returns:
path of opened node
openNode
@CheckForNull
@OpenApipublic final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html) openNode(@CheckForNull
 [BaseElement](../../uml/BaseElement.html) object,
 boolean select,
 boolean appendSelection,
 boolean requestFocus)
Opens(expands) node for a give Element. May request focus for a tree.
Parameters:
`object` - the element to expand in the tree
`select` - select node.
`appendSelection` - append to old selection or clear old selection
`requestFocus` - request focus for a tree.
Returns:
path of opened node
openNode
@CheckForNull
@OpenApipublic final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html) openNode(@CheckForNull
 [BaseElement](../../uml/BaseElement.html) object,
 boolean select,
 boolean requestFocus)
Opens(expands) node for a give Element. May request focus for a tree.
Parameters:
`object` - the element to expand in the tree
`select` - select node.
`requestFocus` - request focus for a tree.
Returns:
path of opened node
openNode
@CheckForNull
@OpenApipublic final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html) openNode(@CheckForNull
 [BaseElement](../../uml/BaseElement.html) object,
 boolean select,
 boolean appendSelection,
 boolean requestFocus,
 boolean scrollToVisible)
Opens(expands) node for a give Element. May request focus for a tree.
Parameters:
`object` - the element to expand in the tree.
`select` - select node.
`appendSelection` - append to old selection or clear old selection
`requestFocus` - request focus for a tree.
`scrollToVisible` - do we need to scroll to visible?
Returns:
path of opened node.
openNode
@CheckForNullpublic final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html) openNode(@CheckForNull
 [BaseElement](../../uml/BaseElement.html) object,
 @CheckForNull
 com.dassault_systemes.modeler.magic.ui.ElementSelection selection,
 boolean appendSelection)
openNode
@CheckForNullpublic final [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html) openNode(@CheckForNull
 [BaseElement](../../uml/BaseElement.html) object,
 @CheckForNull
 com.dassault_systemes.modeler.magic.ui.ElementSelection selection,
 boolean select,
 boolean appendSelection,
 boolean requestFocus,
 boolean scrollToVisible)
waitForPreviousEventsOnOpeningNode
protected boolean waitForPreviousEventsOnOpeningNode()
doBeforeOpenNode
protected void doBeforeOpenNode()
openNode
public void openNode([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../../uml/BaseElement.html)> elements)
openNode
public <T extends [BaseElement](../../uml/BaseElement.html)> void openNode([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> elements,
 [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<T> failedConsumer)
getAutoscrollInsets
public [Insets](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Insets.html) getAutoscrollInsets()
Specified by:
`[getAutoscrollInsets](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/dnd/Autoscroll.html#getAutoscrollInsets())` in interface `[Autoscroll](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/dnd/Autoscroll.html)`
getActions
protected [ActionsManager](../../../actions/ActionsManager.html) getActions()
Returns shortcuts action manager for this browser.
Returns:
ActionsManager with actions to register in this browser as KeyListeners
setBrowserForActions
protected static void setBrowserForActions(@CheckForNull
 [Tree](Tree.html) tree,
 [ActionsManager](../../../actions/ActionsManager.html) manager,
 @CheckForNull
 com.nomagic.magicdraw.ui.ElementSelectionProvider provider)
showPopupMenu
public void showPopupMenu(@CheckForNull
 [MouseEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html) evt)
Specified by:
`showPopupMenu` in interface `com.nomagic.awt.PopupOwner`
decorateTree
public void decorateTree()
getDefaultFocusable
public [Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) getDefaultFocusable()
Description copied from class: `[ExtendedPanel](../../../ui/ExtendedPanel.html#getDefaultFocusable())`
Request Focus for some component. Here it is empty.
Overrides:
`[getDefaultFocusable](../../../ui/ExtendedPanel.html#getDefaultFocusable())` in class `[ExtendedPanel](../../../ui/ExtendedPanel.html)`
editPath
public void editPath([TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html) path)
autoscroll
public void autoscroll([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)
Implementation of auto-scroll interface method
 auto-scroll(Point)
 Scrolls to specified point.
Specified by:
`[autoscroll](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/dnd/Autoscroll.html#autoscroll(java.awt.Point))` in interface `[Autoscroll](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/dnd/Autoscroll.html)`
Parameters:
`pt` - - Point
getRootNode
@OpenApipublic [Node](Node.html) getRootNode()
Returns root node of the tree.
Overrides:
`[getRootNode](AbstractTree.html#getRootNode())` in class `[AbstractTree](AbstractTree.html)`
Returns:
root node.
dispose
public void dispose()
Removes all nodes recursively.
Overrides:
`[dispose](AbstractTree.html#dispose())` in class `[AbstractTree](AbstractTree.html)`
disposeNodes
public void disposeNodes()
Dispose nodes added into the tree.
getTreeModel
public com.nomagic.magicdraw.ui.browser.TreeModel getTreeModel()
Overrides:
`[getTreeModel](AbstractTree.html#getTreeModel())` in class `[AbstractTree](AbstractTree.html)`
collectSelectedNodes
public void collectSelectedNodes(com.nomagic.magicdraw.ui.browser.TreeModel treeModel,
 [TreePath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html) parentPath,
 com.nomagic.magicdraw.ui.browser.TreeSelectionTracker selectionTracker)
Collects selected nodes.
 During event dispatching node state can change from [`Node`](Node.html) <-> `LoadingDummyNode`
 If node was selected it must be selected when node state is changed.
 On treeStructureChanged event all selected tree paths are collected, on treeNodesChanged event they are selected.
Parameters:
`treeModel` - model
`parentPath` - parent path
`selectionTracker` - selection tracker
reset
public void reset()
Description copied from interface: `[Cachable](../../../ui/Cachable.html#reset())`
Cache managers invokes this method to free resources. Usually this method must drop references to external objects
 in order to enable garbage collection of them.
Specified by:
`[reset](../../../ui/Cachable.html#reset())` in interface `[Cachable](../../../ui/Cachable.html)`
getParams
public com.nomagic.magicdraw.ui.browser.TreeParams getParams()
isUpdateIfShowing
public boolean isUpdateIfShowing()
Returns if tree only updates when showing
Returns:
true if tree only updates when showing
setUpdateIfShowing
public void setUpdateIfShowing(boolean updateIfShowing)
Allows setting tree to update only if showing
Parameters:
`updateIfShowing` - true if tree should only update when showing

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.browser</a></div>
<h1 class="title" title="Class Tree">Class Tree</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">java.awt.Component</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html" title="class or interface in java.awt">java.awt.Container</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html" title="class or interface in javax.swing">javax.swing.JComponent</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html" title="class or interface in javax.swing">javax.swing.JPanel</a>
<div class="inheritance"><a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">com.nomagic.ui.ExtendedPanel</a>
<div class="inheritance"><a href="AbstractTree.html" title="class in com.nomagic.magicdraw.ui.browser">com.nomagic.magicdraw.ui.browser.AbstractTree</a>
<div class="inheritance">com.nomagic.magicdraw.ui.browser.Tree</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.awt.PopupOwner</code>, <code>com.nomagic.magicdraw.ui.Updatable</code>, <code><a href="../../../ui/Cachable.html" title="interface in com.nomagic.ui">Cachable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/dnd/Autoscroll.html" title="class or interface in java.awt.dnd">Autoscroll</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/FocusListener.html" title="class or interface in java.awt.event">FocusListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html" title="class or interface in java.awt.image">ImageObserver</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/MenuContainer.html" title="class or interface in java.awt">MenuContainer</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/accessibility/Accessible.html" title="class or interface in javax.accessibility">Accessible</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Tree</span>
<span class="extends-implements">extends <a href="AbstractTree.html" title="class in com.nomagic.magicdraw.ui.browser">AbstractTree</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/dnd/Autoscroll.html" title="class or interface in java.awt.dnd">Autoscroll</a>, com.nomagic.awt.PopupOwner, com.nomagic.magicdraw.ui.Updatable, <a href="../../../ui/Cachable.html" title="interface in com.nomagic.ui">Cachable</a></span></div>
<div class="block">The tree used in MagicDraw browser.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.ui.browser.Tree">Serialized Form</a></li>
</ul>
</dd>
</dl>
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
<div class="col-first even-row-color"><code>protected static final <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[]</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOADING_DUMMY_NODE_DISTINCTION">LOADING_DUMMY_NODE_DISTINCTION</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.ui.browser.AbstractTree">Fields inherited from class com.nomagic.magicdraw.ui.browser.<a href="AbstractTree.html" title="class in com.nomagic.magicdraw.ui.browser">AbstractTree</a></h3>
<code><a href="AbstractTree.html#MAX_AUTO_EXPAND_DEPTH">MAX_AUTO_EXPAND_DEPTH</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.ui.ExtendedPanel">Fields inherited from class com.nomagic.ui.<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a></h3>
<code><a href="../../../ui/ExtendedPanel.html#DEFAULT_FOCUSABLE">DEFAULT_FOCUSABLE</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.JComponent">Fields inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html" title="class or interface in javax.swing">JComponent</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#listenerList" title="class or interface in javax.swing">listenerList</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#TOOL_TIP_TEXT_KEY" title="class or interface in javax.swing">TOOL_TIP_TEXT_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#ui" title="class or interface in javax.swing">ui</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#UNDEFINED_CONDITION" title="class or interface in javax.swing">UNDEFINED_CONDITION</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#WHEN_ANCESTOR_OF_FOCUSED_COMPONENT" title="class or interface in javax.swing">WHEN_ANCESTOR_OF_FOCUSED_COMPONENT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#WHEN_FOCUSED" title="class or interface in javax.swing">WHEN_FOCUSED</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#WHEN_IN_FOCUSED_WINDOW" title="class or interface in javax.swing">WHEN_IN_FOCUSED_WINDOW</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-java.awt.Component">Fields inherited from class java.awt.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#accessibleContext" title="class or interface in java.awt">accessibleContext</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#BOTTOM_ALIGNMENT" title="class or interface in java.awt">BOTTOM_ALIGNMENT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#CENTER_ALIGNMENT" title="class or interface in java.awt">CENTER_ALIGNMENT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#LEFT_ALIGNMENT" title="class or interface in java.awt">LEFT_ALIGNMENT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#RIGHT_ALIGNMENT" title="class or interface in java.awt">RIGHT_ALIGNMENT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#TOP_ALIGNMENT" title="class or interface in java.awt">TOP_ALIGNMENT</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-java.awt.image.ImageObserver">Fields inherited from interface java.awt.image.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html" title="class or interface in java.awt.image">ImageObserver</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#ABORT" title="class or interface in java.awt.image">ABORT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#ALLBITS" title="class or interface in java.awt.image">ALLBITS</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#ERROR" title="class or interface in java.awt.image">ERROR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#FRAMEBITS" title="class or interface in java.awt.image">FRAMEBITS</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#HEIGHT" title="class or interface in java.awt.image">HEIGHT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#PROPERTIES" title="class or interface in java.awt.image">PROPERTIES</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#SOMEBITS" title="class or interface in java.awt.image">SOMEBITS</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#WIDTH" title="class or interface in java.awt.image">WIDTH</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.ui.browser.TreeParams)">Tree</a><wbr/>(com.nomagic.magicdraw.ui.browser.TreeParams params)</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addTreeSelectionParticipant(com.nomagic.magicdraw.ui.browser.Tree.TreeSelectionParticipant)">addTreeSelectionParticipant</a><wbr/>(com.nomagic.magicdraw.ui.browser.Tree.TreeSelectionParticipant participant)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds tree selection participant</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#autoscroll(java.awt.Point)">autoscroll</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Implementation of auto-scroll interface method
 auto-scroll(Point)
 Scrolls to specified point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#browserUpdateDelayed(boolean)">browserUpdateDelayed</a><wbr/>(boolean updateOnlyDirty)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called if browser lazy and update vas delayed</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canDelete(com.nomagic.magicdraw.ui.browser.Node%5B%5D)">canDelete</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Test if all nodes can be deleted</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectSelectedNodes(com.nomagic.magicdraw.ui.browser.TreeModel,javax.swing.tree.TreePath,com.nomagic.magicdraw.ui.browser.TreeSelectionTracker)">collectSelectedNodes</a><wbr/>(com.nomagic.magicdraw.ui.browser.TreeModel treeModel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a> parentPath,
 com.nomagic.magicdraw.ui.browser.TreeSelectionTracker selectionTracker)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects selected nodes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#decorateTree()">decorateTree</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#delete(com.nomagic.magicdraw.ui.browser.Node%5B%5D)">delete</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] node)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#delete(com.nomagic.magicdraw.ui.browser.Node%5B%5D,boolean,com.dassault_systemes.modeler.foundation.editing.MacroCommand)">delete</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] nodes,
 boolean useSpecificDeletion,
 com.dassault_systemes.modeler.foundation.editing.MacroCommand macroCommand)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Deletes nodes</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all nodes recursively.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#disposeNodes()">disposeNodes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dispose nodes added into the tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#doBeforeOpenNode()">doBeforeOpenNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#doubleClick(javax.swing.tree.DefaultMutableTreeNode,java.awt.event.MouseEvent)">doubleClick</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a> node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html" title="class or interface in java.awt.event">MouseEvent</a> event)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">called on mouse double click on nod.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#doubleClickAction(com.nomagic.magicdraw.ui.browser.Node,java.awt.event.MouseEvent)">doubleClickAction</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html" title="class or interface in java.awt.event">MouseEvent</a> event)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Edit action invoked if somebody did double click on some node</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editAction(com.nomagic.magicdraw.ui.browser.Node,java.awt.AWTEvent)">editAction</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html" title="class or interface in java.awt">AWTEvent</a> event)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Edit action invoked if somebody pressed Enter on node</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editPath(javax.swing.tree.TreePath)">editPath</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a> path)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActions()">getActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns shortcuts action manager for this browser.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Insets.html" title="class or interface in java.awt">Insets</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAutoscrollInsets()">getAutoscrollInsets</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultFocusable()">getDefaultFocusable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Request Focus for some component.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNode(int)">getNode</a><wbr/>(int row)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns first selected node in the tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.browser.TreeParams</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParams()">getParams</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRootNode()">getRootNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns root node of the tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedNode()">getSelectedNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns first selected node in the tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedNodes()">getSelectedNodes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all selected nodes in the tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.browser.TreeModel</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTreeModel()">getTreeModel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init()">init</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init(com.nomagic.magicdraw.ui.browser.Node)">init</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> rootNode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;A&gt; void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initAsync(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">initAsync</a><wbr/>(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;A&gt; void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initAsync(com.nomagic.magicdraw.ui.browser.Node,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">initAsync</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> root,
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowOwner()">isShowOwner</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUpdateIfShowing()">isUpdateIfShowing</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns if tree only updates when showing</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static &lt;A&gt; void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#maybeInvokeChainedCH(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,java.lang.Throwable)">maybeInvokeChainedCH</a><wbr/>(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> exc)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected &lt;A&gt; void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#maybeInvokeChainedHandler(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,com.nomagic.magicdraw.ui.browser.TreeModel,java.lang.Throwable)">maybeInvokeChainedHandler</a><wbr/>(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler,
 com.nomagic.magicdraw.ui.browser.TreeModel browserModel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> exc)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static &lt;A&gt; void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#maybeInvokeChainedHandler(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,java.lang.Throwable)">maybeInvokeChainedHandler</a><wbr/>(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> exc)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openNode(com.nomagic.magicdraw.uml.BaseElement)">openNode</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens(expands) node for a give Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openNode(com.nomagic.magicdraw.uml.BaseElement,boolean)">openNode</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object,
 boolean requestFocus)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens(expands) node for a give Element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openNode(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean)">openNode</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object,
 boolean select,
 boolean requestFocus)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens(expands) node for a give Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openNode(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean)">openNode</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object,
 boolean select,
 boolean appendSelection,
 boolean requestFocus)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens(expands) node for a give Element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openNode(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,boolean)">openNode</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object,
 boolean select,
 boolean appendSelection,
 boolean requestFocus,
 boolean scrollToVisible)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens(expands) node for a give Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openNode(com.nomagic.magicdraw.uml.BaseElement,com.dassault_systemes.modeler.magic.ui.ElementSelection,boolean)">openNode</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object,
 com.dassault_systemes.modeler.magic.ui.ElementSelection selection,
 boolean appendSelection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openNode(com.nomagic.magicdraw.uml.BaseElement,com.dassault_systemes.modeler.magic.ui.ElementSelection,boolean,boolean,boolean,boolean)">openNode</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object,
 com.dassault_systemes.modeler.magic.ui.ElementSelection selection,
 boolean select,
 boolean appendSelection,
 boolean requestFocus,
 boolean scrollToVisible)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openNode(java.util.Collection)">openNode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;<br/>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openNode(java.util.Collection,java.util.function.Consumer)">openNode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;T&gt; failedConsumer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAction(com.nomagic.magicdraw.ui.browser.Node%5B%5D)">removeAction</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] node)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Edit action invoked if somebody pressed DELETE on node</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reset()">reset</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Cache managers invokes this method to free resources.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setBrowserForActions(com.nomagic.magicdraw.ui.browser.Tree,com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.ui.ElementSelectionProvider)">setBrowserForActions</a><wbr/>(<a href="Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree,
 <a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 com.nomagic.magicdraw.ui.ElementSelectionProvider provider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIgnoreLock(boolean)">setIgnoreLock</a><wbr/>(boolean ignoreLock)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSelectedNodes(com.nomagic.magicdraw.ui.browser.Node%5B%5D)">setSelectedNodes</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] nodes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Selects given nodes in the tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUpdateIfShowing(boolean)">setUpdateIfShowing</a><wbr/>(boolean updateIfShowing)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Allows setting tree to update only if showing</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showPopupMenu(java.awt.event.MouseEvent)">showPopupMenu</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html" title="class or interface in java.awt.event">MouseEvent</a> evt)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#specificUpdateBrowser(boolean)">specificUpdateBrowser</a><wbr/>(boolean updateOnlyDirty)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toNodes(javax.swing.tree.TreePath%5B%5D)">toNodes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a>[] paths)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Utility method for converting array of paths to array of nodes</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toNodes(javax.swing.tree.TreePath%5B%5D,boolean)">toNodes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a>[] paths,
 boolean loadingDummyNodeDistinction)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toTreePaths(com.nomagic.magicdraw.ui.browser.Node%5B%5D)">toTreePaths</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] nodes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Utility method for converting array of nodes to array of paths</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#update(boolean)">update</a><wbr/>(boolean deepUpdate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Update component UI by model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateBrowser()">updateBrowser</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates dirty nodes in tree with the newest data and shows it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateBrowser(boolean)">updateBrowser</a><wbr/>(boolean updateOnlyDirty)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates tree with the newest data and shows it.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateBrowser(boolean,boolean)">updateBrowser</a><wbr/>(boolean updateOnlyDirty,
 boolean updateNotShowing)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates tree with the newest data and shows it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;A&gt; void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateBrowserAsync(boolean,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,com.nomagic.task.ProgressStatus)">updateBrowserAsync</a><wbr/>(boolean updateOnlyDirty,
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected &lt;A&gt; boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateOnlyDirtyNodes(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,boolean)">updateOnlyDirtyNodes</a><wbr/>(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler,
 boolean updateAll)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateUI()">updateUI</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#waitForPreviousEventsOnOpeningNode()">waitForPreviousEventsOnOpeningNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.ui.browser.AbstractTree">Methods inherited from class com.nomagic.magicdraw.ui.browser.<a href="AbstractTree.html" title="class in com.nomagic.magicdraw.ui.browser">AbstractTree</a></h3>
<code><a href="AbstractTree.html#close()">close</a>, <a href="AbstractTree.html#getCookies()">getCookies</a>, <a href="AbstractTree.html#getScrollPane()">getScrollPane</a>, <a href="AbstractTree.html#getTree()">getTree</a>, <a href="AbstractTree.html#isAutoExpandMode()">isAutoExpandMode</a>, <a href="AbstractTree.html#open()">open</a>, <a href="AbstractTree.html#openPath(javax.swing.tree.TreePath)">openPath</a>, <a href="AbstractTree.html#openPath(javax.swing.tree.TreePath,boolean,boolean,boolean)">openPath</a>, <a href="AbstractTree.html#openPath(javax.swing.tree.TreePath,boolean,boolean,boolean,boolean)">openPath</a>, <a href="AbstractTree.html#setAutoExpandMode(boolean)">setAutoExpandMode</a>, <a href="AbstractTree.html#setTree(javax.swing.JTree)">setTree</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.ui.ExtendedPanel">Methods inherited from class com.nomagic.ui.<a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a></h3>
<code><a href="../../../ui/ExtendedPanel.html#addActionListenerFor(java.awt.event.ActionListener,java.awt.Component)">addActionListenerFor</a>, <a href="../../../ui/ExtendedPanel.html#addEnterOKListener(java.awt.event.KeyListener)">addEnterOKListener</a>, <a href="../../../ui/ExtendedPanel.html#addFocusListenerFor(java.awt.event.FocusListener,java.awt.Component)">addFocusListenerFor</a>, <a href="../../../ui/ExtendedPanel.html#addKeyListenerFor(java.awt.event.KeyListener,java.awt.Component)">addKeyListenerFor</a>, <a href="../../../ui/ExtendedPanel.html#cancel()">cancel</a>, <a href="../../../ui/ExtendedPanel.html#clear()">clear</a>, <a href="../../../ui/ExtendedPanel.html#enableComponent(boolean,java.awt.Component)">enableComponent</a>, <a href="../../../ui/ExtendedPanel.html#focusGained(java.awt.event.FocusEvent)">focusGained</a>, <a href="../../../ui/ExtendedPanel.html#focusLost(java.awt.event.FocusEvent)">focusLost</a>, <a href="../../../ui/ExtendedPanel.html#getEditingState()">getEditingState</a>, <a href="../../../ui/ExtendedPanel.html#getErrorString()">getErrorString</a>, <a href="../../../ui/ExtendedPanel.html#getParentWindow()">getParentWindow</a>, <a href="../../../ui/ExtendedPanel.html#initialize()">initialize</a>, <a href="../../../ui/ExtendedPanel.html#isDataValid()">isDataValid</a>, <a href="../../../ui/ExtendedPanel.html#ok()">ok</a>, <a href="../../../ui/ExtendedPanel.html#removeFocusListenerFor(java.awt.event.FocusListener,java.awt.Component)">removeFocusListenerFor</a>, <a href="../../../ui/ExtendedPanel.html#removeKeyListenerFor(java.awt.event.KeyListener,java.awt.Component)">removeKeyListenerFor</a>, <a href="../../../ui/ExtendedPanel.html#setEditingState(boolean)">setEditingState</a>, <a href="../../../ui/ExtendedPanel.html#setEnabled(boolean,java.awt.Component)">setEnabled</a>, <a href="../../../ui/ExtendedPanel.html#setEnabledAll(boolean)">setEnabledAll</a>, <a href="../../../ui/ExtendedPanel.html#updateByStateRecursively(boolean,java.awt.Component)">updateByStateRecursively</a>, <a href="../../../ui/ExtendedPanel.html#updatePanelByEditingState()">updatePanelByEditingState</a>, <a href="../../../ui/ExtendedPanel.html#updatePanelByEditingState(boolean)">updatePanelByEditingState</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.JPanel">Methods inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html" title="class or interface in javax.swing">JPanel</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html#getAccessibleContext()" title="class or interface in javax.swing">getAccessibleContext</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html#getUI()" title="class or interface in javax.swing">getUI</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html#getUIClassID()" title="class or interface in javax.swing">getUIClassID</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html#paramString()" title="class or interface in javax.swing">paramString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html#setUI(javax.swing.plaf.PanelUI)" title="class or interface in javax.swing">setUI</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.JComponent">Methods inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html" title="class or interface in javax.swing">JComponent</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#addAncestorListener(javax.swing.event.AncestorListener)" title="class or interface in javax.swing">addAncestorListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#addNotify()" title="class or interface in javax.swing">addNotify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#addVetoableChangeListener(java.beans.VetoableChangeListener)" title="class or interface in javax.swing">addVetoableChangeListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#computeVisibleRect(java.awt.Rectangle)" title="class or interface in javax.swing">computeVisibleRect</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#contains(int,int)" title="class or interface in javax.swing">contains</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#createToolTip()" title="class or interface in javax.swing">createToolTip</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#disable()" title="class or interface in javax.swing">disable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#enable()" title="class or interface in javax.swing">enable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#firePropertyChange(java.lang.String,boolean,boolean)" title="class or interface in javax.swing">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#firePropertyChange(java.lang.String,char,char)" title="class or interface in javax.swing">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#firePropertyChange(java.lang.String,int,int)" title="class or interface in javax.swing">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#fireVetoableChange(java.lang.String,java.lang.Object,java.lang.Object)" title="class or interface in javax.swing">fireVetoableChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getActionForKeyStroke(javax.swing.KeyStroke)" title="class or interface in javax.swing">getActionForKeyStroke</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getActionMap()" title="class or interface in javax.swing">getActionMap</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getAlignmentX()" title="class or interface in javax.swing">getAlignmentX</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getAlignmentY()" title="class or interface in javax.swing">getAlignmentY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getAncestorListeners()" title="class or interface in javax.swing">getAncestorListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getAutoscrolls()" title="class or interface in javax.swing">getAutoscrolls</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getBaseline(int,int)" title="class or interface in javax.swing">getBaseline</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getBaselineResizeBehavior()" title="class or interface in javax.swing">getBaselineResizeBehavior</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getBorder()" title="class or interface in javax.swing">getBorder</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getBounds(java.awt.Rectangle)" title="class or interface in javax.swing">getBounds</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getClientProperty(java.lang.Object)" title="class or interface in javax.swing">getClientProperty</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getComponentGraphics(java.awt.Graphics)" title="class or interface in javax.swing">getComponentGraphics</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getComponentPopupMenu()" title="class or interface in javax.swing">getComponentPopupMenu</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getConditionForKeyStroke(javax.swing.KeyStroke)" title="class or interface in javax.swing">getConditionForKeyStroke</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getDebugGraphicsOptions()" title="class or interface in javax.swing">getDebugGraphicsOptions</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getDefaultLocale()" title="class or interface in javax.swing">getDefaultLocale</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getFontMetrics(java.awt.Font)" title="class or interface in javax.swing">getFontMetrics</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getGraphics()" title="class or interface in javax.swing">getGraphics</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getHeight()" title="class or interface in javax.swing">getHeight</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getInheritsPopupMenu()" title="class or interface in javax.swing">getInheritsPopupMenu</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getInputMap()" title="class or interface in javax.swing">getInputMap</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getInputMap(int)" title="class or interface in javax.swing">getInputMap</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getInputVerifier()" title="class or interface in javax.swing">getInputVerifier</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getInsets()" title="class or interface in javax.swing">getInsets</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getInsets(java.awt.Insets)" title="class or interface in javax.swing">getInsets</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getListeners(java.lang.Class)" title="class or interface in javax.swing">getListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getLocation(java.awt.Point)" title="class or interface in javax.swing">getLocation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getMaximumSize()" title="class or interface in javax.swing">getMaximumSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getMinimumSize()" title="class or interface in javax.swing">getMinimumSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getNextFocusableComponent()" title="class or interface in javax.swing">getNextFocusableComponent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getPopupLocation(java.awt.event.MouseEvent)" title="class or interface in javax.swing">getPopupLocation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getPreferredSize()" title="class or interface in javax.swing">getPreferredSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getRegisteredKeyStrokes()" title="class or interface in javax.swing">getRegisteredKeyStrokes</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getRootPane()" title="class or interface in javax.swing">getRootPane</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getSize(java.awt.Dimension)" title="class or interface in javax.swing">getSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getToolTipLocation(java.awt.event.MouseEvent)" title="class or interface in javax.swing">getToolTipLocation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getToolTipText()" title="class or interface in javax.swing">getToolTipText</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getToolTipText(java.awt.event.MouseEvent)" title="class or interface in javax.swing">getToolTipText</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getTopLevelAncestor()" title="class or interface in javax.swing">getTopLevelAncestor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getTransferHandler()" title="class or interface in javax.swing">getTransferHandler</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getVerifyInputWhenFocusTarget()" title="class or interface in javax.swing">getVerifyInputWhenFocusTarget</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getVetoableChangeListeners()" title="class or interface in javax.swing">getVetoableChangeListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getVisibleRect()" title="class or interface in javax.swing">getVisibleRect</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getWidth()" title="class or interface in javax.swing">getWidth</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getX()" title="class or interface in javax.swing">getX</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#getY()" title="class or interface in javax.swing">getY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#grabFocus()" title="class or interface in javax.swing">grabFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#hide()" title="class or interface in javax.swing">hide</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isDoubleBuffered()" title="class or interface in javax.swing">isDoubleBuffered</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isLightweightComponent(java.awt.Component)" title="class or interface in javax.swing">isLightweightComponent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isManagingFocus()" title="class or interface in javax.swing">isManagingFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isOpaque()" title="class or interface in javax.swing">isOpaque</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isOptimizedDrawingEnabled()" title="class or interface in javax.swing">isOptimizedDrawingEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isPaintingForPrint()" title="class or interface in javax.swing">isPaintingForPrint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isPaintingOrigin()" title="class or interface in javax.swing">isPaintingOrigin</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isPaintingTile()" title="class or interface in javax.swing">isPaintingTile</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isRequestFocusEnabled()" title="class or interface in javax.swing">isRequestFocusEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#isValidateRoot()" title="class or interface in javax.swing">isValidateRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#paint(java.awt.Graphics)" title="class or interface in javax.swing">paint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#paintBorder(java.awt.Graphics)" title="class or interface in javax.swing">paintBorder</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#paintChildren(java.awt.Graphics)" title="class or interface in javax.swing">paintChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#paintComponent(java.awt.Graphics)" title="class or interface in javax.swing">paintComponent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#paintImmediately(int,int,int,int)" title="class or interface in javax.swing">paintImmediately</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#paintImmediately(java.awt.Rectangle)" title="class or interface in javax.swing">paintImmediately</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#print(java.awt.Graphics)" title="class or interface in javax.swing">print</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#printAll(java.awt.Graphics)" title="class or interface in javax.swing">printAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#printBorder(java.awt.Graphics)" title="class or interface in javax.swing">printBorder</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#printChildren(java.awt.Graphics)" title="class or interface in javax.swing">printChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#printComponent(java.awt.Graphics)" title="class or interface in javax.swing">printComponent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#processComponentKeyEvent(java.awt.event.KeyEvent)" title="class or interface in javax.swing">processComponentKeyEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#processKeyBinding(javax.swing.KeyStroke,java.awt.event.KeyEvent,int,boolean)" title="class or interface in javax.swing">processKeyBinding</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#processKeyEvent(java.awt.event.KeyEvent)" title="class or interface in javax.swing">processKeyEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#processMouseEvent(java.awt.event.MouseEvent)" title="class or interface in javax.swing">processMouseEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#processMouseMotionEvent(java.awt.event.MouseEvent)" title="class or interface in javax.swing">processMouseMotionEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#putClientProperty(java.lang.Object,java.lang.Object)" title="class or interface in javax.swing">putClientProperty</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#registerKeyboardAction(java.awt.event.ActionListener,java.lang.String,javax.swing.KeyStroke,int)" title="class or interface in javax.swing">registerKeyboardAction</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#registerKeyboardAction(java.awt.event.ActionListener,javax.swing.KeyStroke,int)" title="class or interface in javax.swing">registerKeyboardAction</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#removeAncestorListener(javax.swing.event.AncestorListener)" title="class or interface in javax.swing">removeAncestorListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#removeNotify()" title="class or interface in javax.swing">removeNotify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#removeVetoableChangeListener(java.beans.VetoableChangeListener)" title="class or interface in javax.swing">removeVetoableChangeListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#repaint(long,int,int,int,int)" title="class or interface in javax.swing">repaint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#repaint(java.awt.Rectangle)" title="class or interface in javax.swing">repaint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#requestDefaultFocus()" title="class or interface in javax.swing">requestDefaultFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#requestFocus()" title="class or interface in javax.swing">requestFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#requestFocus(boolean)" title="class or interface in javax.swing">requestFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#requestFocusInWindow()" title="class or interface in javax.swing">requestFocusInWindow</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#requestFocusInWindow(boolean)" title="class or interface in javax.swing">requestFocusInWindow</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#resetKeyboardActions()" title="class or interface in javax.swing">resetKeyboardActions</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#reshape(int,int,int,int)" title="class or interface in javax.swing">reshape</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#revalidate()" title="class or interface in javax.swing">revalidate</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#scrollRectToVisible(java.awt.Rectangle)" title="class or interface in javax.swing">scrollRectToVisible</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setActionMap(javax.swing.ActionMap)" title="class or interface in javax.swing">setActionMap</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setAlignmentX(float)" title="class or interface in javax.swing">setAlignmentX</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setAlignmentY(float)" title="class or interface in javax.swing">setAlignmentY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setAutoscrolls(boolean)" title="class or interface in javax.swing">setAutoscrolls</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setBackground(java.awt.Color)" title="class or interface in javax.swing">setBackground</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setBorder(javax.swing.border.Border)" title="class or interface in javax.swing">setBorder</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setComponentPopupMenu(javax.swing.JPopupMenu)" title="class or interface in javax.swing">setComponentPopupMenu</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setDebugGraphicsOptions(int)" title="class or interface in javax.swing">setDebugGraphicsOptions</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setDefaultLocale(java.util.Locale)" title="class or interface in javax.swing">setDefaultLocale</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setDoubleBuffered(boolean)" title="class or interface in javax.swing">setDoubleBuffered</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setEnabled(boolean)" title="class or interface in javax.swing">setEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setFocusTraversalKeys(int,java.util.Set)" title="class or interface in javax.swing">setFocusTraversalKeys</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setFont(java.awt.Font)" title="class or interface in javax.swing">setFont</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setForeground(java.awt.Color)" title="class or interface in javax.swing">setForeground</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setInheritsPopupMenu(boolean)" title="class or interface in javax.swing">setInheritsPopupMenu</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setInputMap(int,javax.swing.InputMap)" title="class or interface in javax.swing">setInputMap</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setInputVerifier(javax.swing.InputVerifier)" title="class or interface in javax.swing">setInputVerifier</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setMaximumSize(java.awt.Dimension)" title="class or interface in javax.swing">setMaximumSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setMinimumSize(java.awt.Dimension)" title="class or interface in javax.swing">setMinimumSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setNextFocusableComponent(java.awt.Component)" title="class or interface in javax.swing">setNextFocusableComponent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setOpaque(boolean)" title="class or interface in javax.swing">setOpaque</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setPreferredSize(java.awt.Dimension)" title="class or interface in javax.swing">setPreferredSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setRequestFocusEnabled(boolean)" title="class or interface in javax.swing">setRequestFocusEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setToolTipText(java.lang.String)" title="class or interface in javax.swing">setToolTipText</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setTransferHandler(javax.swing.TransferHandler)" title="class or interface in javax.swing">setTransferHandler</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setUI(javax.swing.plaf.ComponentUI)" title="class or interface in javax.swing">setUI</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setVerifyInputWhenFocusTarget(boolean)" title="class or interface in javax.swing">setVerifyInputWhenFocusTarget</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#setVisible(boolean)" title="class or interface in javax.swing">setVisible</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#unregisterKeyboardAction(javax.swing.KeyStroke)" title="class or interface in javax.swing">unregisterKeyboardAction</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html#update(java.awt.Graphics)" title="class or interface in javax.swing">update</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.awt.Container">Methods inherited from class java.awt.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html" title="class or interface in java.awt">Container</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component)" title="class or interface in java.awt">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component,int)" title="class or interface in java.awt">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component,java.lang.Object)" title="class or interface in java.awt">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component,java.lang.Object,int)" title="class or interface in java.awt">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.lang.String,java.awt.Component)" title="class or interface in java.awt">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#addContainerListener(java.awt.event.ContainerListener)" title="class or interface in java.awt">addContainerListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#addImpl(java.awt.Component,java.lang.Object,int)" title="class or interface in java.awt">addImpl</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#addPropertyChangeListener(java.beans.PropertyChangeListener)" title="class or interface in java.awt">addPropertyChangeListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)" title="class or interface in java.awt">addPropertyChangeListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#applyComponentOrientation(java.awt.ComponentOrientation)" title="class or interface in java.awt">applyComponentOrientation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#areFocusTraversalKeysSet(int)" title="class or interface in java.awt">areFocusTraversalKeysSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#countComponents()" title="class or interface in java.awt">countComponents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#deliverEvent(java.awt.Event)" title="class or interface in java.awt">deliverEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#doLayout()" title="class or interface in java.awt">doLayout</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#findComponentAt(int,int)" title="class or interface in java.awt">findComponentAt</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#findComponentAt(java.awt.Point)" title="class or interface in java.awt">findComponentAt</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponent(int)" title="class or interface in java.awt">getComponent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentAt(int,int)" title="class or interface in java.awt">getComponentAt</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentAt(java.awt.Point)" title="class or interface in java.awt">getComponentAt</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentCount()" title="class or interface in java.awt">getComponentCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponents()" title="class or interface in java.awt">getComponents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentZOrder(java.awt.Component)" title="class or interface in java.awt">getComponentZOrder</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getContainerListeners()" title="class or interface in java.awt">getContainerListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getFocusTraversalKeys(int)" title="class or interface in java.awt">getFocusTraversalKeys</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getFocusTraversalPolicy()" title="class or interface in java.awt">getFocusTraversalPolicy</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getLayout()" title="class or interface in java.awt">getLayout</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getMousePosition(boolean)" title="class or interface in java.awt">getMousePosition</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#insets()" title="class or interface in java.awt">insets</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#invalidate()" title="class or interface in java.awt">invalidate</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isAncestorOf(java.awt.Component)" title="class or interface in java.awt">isAncestorOf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusCycleRoot()" title="class or interface in java.awt">isFocusCycleRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusCycleRoot(java.awt.Container)" title="class or interface in java.awt">isFocusCycleRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusTraversalPolicyProvider()" title="class or interface in java.awt">isFocusTraversalPolicyProvider</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusTraversalPolicySet()" title="class or interface in java.awt">isFocusTraversalPolicySet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#layout()" title="class or interface in java.awt">layout</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#list(java.io.PrintStream,int)" title="class or interface in java.awt">list</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#list(java.io.PrintWriter,int)" title="class or interface in java.awt">list</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#locate(int,int)" title="class or interface in java.awt">locate</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#minimumSize()" title="class or interface in java.awt">minimumSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#paintComponents(java.awt.Graphics)" title="class or interface in java.awt">paintComponents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#preferredSize()" title="class or interface in java.awt">preferredSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#printComponents(java.awt.Graphics)" title="class or interface in java.awt">printComponents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#processContainerEvent(java.awt.event.ContainerEvent)" title="class or interface in java.awt">processContainerEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#processEvent(java.awt.AWTEvent)" title="class or interface in java.awt">processEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#remove(int)" title="class or interface in java.awt">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#remove(java.awt.Component)" title="class or interface in java.awt">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#removeAll()" title="class or interface in java.awt">removeAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#removeContainerListener(java.awt.event.ContainerListener)" title="class or interface in java.awt">removeContainerListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setComponentZOrder(java.awt.Component,int)" title="class or interface in java.awt">setComponentZOrder</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFocusCycleRoot(boolean)" title="class or interface in java.awt">setFocusCycleRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)" title="class or interface in java.awt">setFocusTraversalPolicy</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFocusTraversalPolicyProvider(boolean)" title="class or interface in java.awt">setFocusTraversalPolicyProvider</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setLayout(java.awt.LayoutManager)" title="class or interface in java.awt">setLayout</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#transferFocusDownCycle()" title="class or interface in java.awt">transferFocusDownCycle</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#validate()" title="class or interface in java.awt">validate</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#validateTree()" title="class or interface in java.awt">validateTree</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.awt.Component">Methods inherited from class java.awt.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#action(java.awt.Event,java.lang.Object)" title="class or interface in java.awt">action</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#add(java.awt.PopupMenu)" title="class or interface in java.awt">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addComponentListener(java.awt.event.ComponentListener)" title="class or interface in java.awt">addComponentListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addFocusListener(java.awt.event.FocusListener)" title="class or interface in java.awt">addFocusListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)" title="class or interface in java.awt">addHierarchyBoundsListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addHierarchyListener(java.awt.event.HierarchyListener)" title="class or interface in java.awt">addHierarchyListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addInputMethodListener(java.awt.event.InputMethodListener)" title="class or interface in java.awt">addInputMethodListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addKeyListener(java.awt.event.KeyListener)" title="class or interface in java.awt">addKeyListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addMouseListener(java.awt.event.MouseListener)" title="class or interface in java.awt">addMouseListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addMouseMotionListener(java.awt.event.MouseMotionListener)" title="class or interface in java.awt">addMouseMotionListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addMouseWheelListener(java.awt.event.MouseWheelListener)" title="class or interface in java.awt">addMouseWheelListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#bounds()" title="class or interface in java.awt">bounds</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#checkImage(java.awt.Image,int,int,java.awt.image.ImageObserver)" title="class or interface in java.awt">checkImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#checkImage(java.awt.Image,java.awt.image.ImageObserver)" title="class or interface in java.awt">checkImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#coalesceEvents(java.awt.AWTEvent,java.awt.AWTEvent)" title="class or interface in java.awt">coalesceEvents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#contains(java.awt.Point)" title="class or interface in java.awt">contains</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createImage(int,int)" title="class or interface in java.awt">createImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createImage(java.awt.image.ImageProducer)" title="class or interface in java.awt">createImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createVolatileImage(int,int)" title="class or interface in java.awt">createVolatileImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createVolatileImage(int,int,java.awt.ImageCapabilities)" title="class or interface in java.awt">createVolatileImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#disableEvents(long)" title="class or interface in java.awt">disableEvents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#dispatchEvent(java.awt.AWTEvent)" title="class or interface in java.awt">dispatchEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enable(boolean)" title="class or interface in java.awt">enable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enableEvents(long)" title="class or interface in java.awt">enableEvents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enableInputMethods(boolean)" title="class or interface in java.awt">enableInputMethods</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,byte,byte)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,double,double)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,float,float)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,long,long)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,short,short)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBackground()" title="class or interface in java.awt">getBackground</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBounds()" title="class or interface in java.awt">getBounds</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getColorModel()" title="class or interface in java.awt">getColorModel</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getComponentListeners()" title="class or interface in java.awt">getComponentListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getComponentOrientation()" title="class or interface in java.awt">getComponentOrientation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getCursor()" title="class or interface in java.awt">getCursor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getDropTarget()" title="class or interface in java.awt">getDropTarget</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFocusCycleRootAncestor()" title="class or interface in java.awt">getFocusCycleRootAncestor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFocusListeners()" title="class or interface in java.awt">getFocusListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFocusTraversalKeysEnabled()" title="class or interface in java.awt">getFocusTraversalKeysEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFont()" title="class or interface in java.awt">getFont</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getForeground()" title="class or interface in java.awt">getForeground</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getGraphicsConfiguration()" title="class or interface in java.awt">getGraphicsConfiguration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getHierarchyBoundsListeners()" title="class or interface in java.awt">getHierarchyBoundsListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getHierarchyListeners()" title="class or interface in java.awt">getHierarchyListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getIgnoreRepaint()" title="class or interface in java.awt">getIgnoreRepaint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getInputContext()" title="class or interface in java.awt">getInputContext</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getInputMethodListeners()" title="class or interface in java.awt">getInputMethodListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getInputMethodRequests()" title="class or interface in java.awt">getInputMethodRequests</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getKeyListeners()" title="class or interface in java.awt">getKeyListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getLocale()" title="class or interface in java.awt">getLocale</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getLocation()" title="class or interface in java.awt">getLocation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getLocationOnScreen()" title="class or interface in java.awt">getLocationOnScreen</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMouseListeners()" title="class or interface in java.awt">getMouseListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMouseMotionListeners()" title="class or interface in java.awt">getMouseMotionListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMousePosition()" title="class or interface in java.awt">getMousePosition</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMouseWheelListeners()" title="class or interface in java.awt">getMouseWheelListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getName()" title="class or interface in java.awt">getName</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getParent()" title="class or interface in java.awt">getParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getPropertyChangeListeners()" title="class or interface in java.awt">getPropertyChangeListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getPropertyChangeListeners(java.lang.String)" title="class or interface in java.awt">getPropertyChangeListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getSize()" title="class or interface in java.awt">getSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getToolkit()" title="class or interface in java.awt">getToolkit</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getTreeLock()" title="class or interface in java.awt">getTreeLock</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#gotFocus(java.awt.Event,java.lang.Object)" title="class or interface in java.awt">gotFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#handleEvent(java.awt.Event)" title="class or interface in java.awt">handleEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#hasFocus()" title="class or interface in java.awt">hasFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#imageUpdate(java.awt.Image,int,int,int,int,int)" title="class or interface in java.awt">imageUpdate</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#inside(int,int)" title="class or interface in java.awt">inside</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isBackgroundSet()" title="class or interface in java.awt">isBackgroundSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isCursorSet()" title="class or interface in java.awt">isCursorSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isDisplayable()" title="class or interface in java.awt">isDisplayable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isEnabled()" title="class or interface in java.awt">isEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFocusable()" title="class or interface in java.awt">isFocusable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFocusOwner()" title="class or interface in java.awt">isFocusOwner</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFocusTraversable()" title="class or interface in java.awt">isFocusTraversable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFontSet()" title="class or interface in java.awt">isFontSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isForegroundSet()" title="class or interface in java.awt">isForegroundSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isLightweight()" title="class or interface in java.awt">isLightweight</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isMaximumSizeSet()" title="class or interface in java.awt">isMaximumSizeSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isMinimumSizeSet()" title="class or interface in java.awt">isMinimumSizeSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isPreferredSizeSet()" title="class or interface in java.awt">isPreferredSizeSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isShowing()" title="class or interface in java.awt">isShowing</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isValid()" title="class or interface in java.awt">isValid</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isVisible()" title="class or interface in java.awt">isVisible</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#keyDown(java.awt.Event,int)" title="class or interface in java.awt">keyDown</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#keyUp(java.awt.Event,int)" title="class or interface in java.awt">keyUp</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#list()" title="class or interface in java.awt">list</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#list(java.io.PrintStream)" title="class or interface in java.awt">list</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#list(java.io.PrintWriter)" title="class or interface in java.awt">list</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#location()" title="class or interface in java.awt">location</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#lostFocus(java.awt.Event,java.lang.Object)" title="class or interface in java.awt">lostFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseDown(java.awt.Event,int,int)" title="class or interface in java.awt">mouseDown</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseDrag(java.awt.Event,int,int)" title="class or interface in java.awt">mouseDrag</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseEnter(java.awt.Event,int,int)" title="class or interface in java.awt">mouseEnter</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseExit(java.awt.Event,int,int)" title="class or interface in java.awt">mouseExit</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseMove(java.awt.Event,int,int)" title="class or interface in java.awt">mouseMove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseUp(java.awt.Event,int,int)" title="class or interface in java.awt">mouseUp</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#move(int,int)" title="class or interface in java.awt">move</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#nextFocus()" title="class or interface in java.awt">nextFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#paintAll(java.awt.Graphics)" title="class or interface in java.awt">paintAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#postEvent(java.awt.Event)" title="class or interface in java.awt">postEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#prepareImage(java.awt.Image,int,int,java.awt.image.ImageObserver)" title="class or interface in java.awt">prepareImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#prepareImage(java.awt.Image,java.awt.image.ImageObserver)" title="class or interface in java.awt">prepareImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processComponentEvent(java.awt.event.ComponentEvent)" title="class or interface in java.awt">processComponentEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processFocusEvent(java.awt.event.FocusEvent)" title="class or interface in java.awt">processFocusEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processHierarchyBoundsEvent(java.awt.event.HierarchyEvent)" title="class or interface in java.awt">processHierarchyBoundsEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processHierarchyEvent(java.awt.event.HierarchyEvent)" title="class or interface in java.awt">processHierarchyEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processInputMethodEvent(java.awt.event.InputMethodEvent)" title="class or interface in java.awt">processInputMethodEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processMouseWheelEvent(java.awt.event.MouseWheelEvent)" title="class or interface in java.awt">processMouseWheelEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#remove(java.awt.MenuComponent)" title="class or interface in java.awt">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeComponentListener(java.awt.event.ComponentListener)" title="class or interface in java.awt">removeComponentListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeFocusListener(java.awt.event.FocusListener)" title="class or interface in java.awt">removeFocusListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)" title="class or interface in java.awt">removeHierarchyBoundsListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeHierarchyListener(java.awt.event.HierarchyListener)" title="class or interface in java.awt">removeHierarchyListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeInputMethodListener(java.awt.event.InputMethodListener)" title="class or interface in java.awt">removeInputMethodListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeKeyListener(java.awt.event.KeyListener)" title="class or interface in java.awt">removeKeyListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeMouseListener(java.awt.event.MouseListener)" title="class or interface in java.awt">removeMouseListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeMouseMotionListener(java.awt.event.MouseMotionListener)" title="class or interface in java.awt">removeMouseMotionListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeMouseWheelListener(java.awt.event.MouseWheelListener)" title="class or interface in java.awt">removeMouseWheelListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removePropertyChangeListener(java.beans.PropertyChangeListener)" title="class or interface in java.awt">removePropertyChangeListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removePropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)" title="class or interface in java.awt">removePropertyChangeListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#repaint()" title="class or interface in java.awt">repaint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#repaint(int,int,int,int)" title="class or interface in java.awt">repaint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#repaint(long)" title="class or interface in java.awt">repaint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocus(boolean,java.awt.event.FocusEvent.Cause)" title="class or interface in java.awt">requestFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocus(java.awt.event.FocusEvent.Cause)" title="class or interface in java.awt">requestFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocusInWindow(java.awt.event.FocusEvent.Cause)" title="class or interface in java.awt">requestFocusInWindow</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#resize(int,int)" title="class or interface in java.awt">resize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#resize(java.awt.Dimension)" title="class or interface in java.awt">resize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setBounds(int,int,int,int)" title="class or interface in java.awt">setBounds</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setBounds(java.awt.Rectangle)" title="class or interface in java.awt">setBounds</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setComponentOrientation(java.awt.ComponentOrientation)" title="class or interface in java.awt">setComponentOrientation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setCursor(java.awt.Cursor)" title="class or interface in java.awt">setCursor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setDropTarget(java.awt.dnd.DropTarget)" title="class or interface in java.awt">setDropTarget</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setFocusable(boolean)" title="class or interface in java.awt">setFocusable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setFocusTraversalKeysEnabled(boolean)" title="class or interface in java.awt">setFocusTraversalKeysEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setIgnoreRepaint(boolean)" title="class or interface in java.awt">setIgnoreRepaint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setLocale(java.util.Locale)" title="class or interface in java.awt">setLocale</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setLocation(int,int)" title="class or interface in java.awt">setLocation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setLocation(java.awt.Point)" title="class or interface in java.awt">setLocation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setMixingCutoutShape(java.awt.Shape)" title="class or interface in java.awt">setMixingCutoutShape</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setName(java.lang.String)" title="class or interface in java.awt">setName</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setSize(int,int)" title="class or interface in java.awt">setSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setSize(java.awt.Dimension)" title="class or interface in java.awt">setSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#show()" title="class or interface in java.awt">show</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#show(boolean)" title="class or interface in java.awt">show</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#size()" title="class or interface in java.awt">size</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#toString()" title="class or interface in java.awt">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#transferFocus()" title="class or interface in java.awt">transferFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#transferFocusBackward()" title="class or interface in java.awt">transferFocusBackward</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#transferFocusUpCycle()" title="class or interface in java.awt">transferFocusUpCycle</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.ui.Updatable">Methods inherited from interface com.nomagic.magicdraw.ui.Updatable</h3>
<code>afterAllUpdates, beforeAllUpdates</code></div>
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
<section class="detail" id="LOADING_DUMMY_NODE_DISTINCTION">
<h3>LOADING_DUMMY_NODE_DISTINCTION</h3>
<div class="member-signature"><span class="modifiers">protected static final</span> <span class="return-type"><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[]</span> <span class="element-name">LOADING_DUMMY_NODE_DISTINCTION</span></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.ui.browser.TreeParams)">
<h3>Tree</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Tree</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.browser.TreeParams params)</span></div>
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
<section class="detail" id="setIgnoreLock(boolean)">
<h3>setIgnoreLock</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIgnoreLock</span><wbr/><span class="parameters">(boolean ignoreLock)</span></div>
</section>
</li>
<li>
<section class="detail" id="doubleClick(javax.swing.tree.DefaultMutableTreeNode,java.awt.event.MouseEvent)">
<h3>doubleClick</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">doubleClick</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a> node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html" title="class or interface in java.awt.event">MouseEvent</a> event)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractTree.html#doubleClick(javax.swing.tree.DefaultMutableTreeNode,java.awt.event.MouseEvent)">AbstractTree</a></code></span></div>
<div class="block">called on mouse double click on nod.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractTree.html#doubleClick(javax.swing.tree.DefaultMutableTreeNode,java.awt.event.MouseEvent)">doubleClick</a></code> in class <code><a href="AbstractTree.html" title="class in com.nomagic.magicdraw.ui.browser">AbstractTree</a></code></dd>
<dt>Parameters:</dt>
<dd><code>node</code> - node on which double click was called.</dd>
<dd><code>event</code> - double click event</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="doubleClickAction(com.nomagic.magicdraw.ui.browser.Node,java.awt.event.MouseEvent)">
<h3>doubleClickAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">doubleClickAction</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html" title="class or interface in java.awt.event">MouseEvent</a> event)</span></div>
<div class="block">Edit action invoked if somebody did double click on some node</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - node</dd>
<dd><code>event</code> - event</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="editAction(com.nomagic.magicdraw.ui.browser.Node,java.awt.AWTEvent)">
<h3>editAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">editAction</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html" title="class or interface in java.awt">AWTEvent</a> event)</span></div>
<div class="block">Edit action invoked if somebody pressed Enter on node</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - node</dd>
<dd><code>event</code> - action event</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAction(com.nomagic.magicdraw.ui.browser.Node[])">
<h3>removeAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAction</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] node)</span></div>
<div class="block">Edit action invoked if somebody pressed DELETE on node</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowOwner()">
<h3>isShowOwner</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isShowOwner</span>()</div>
</section>
</li>
<li>
<section class="detail" id="updateUI()">
<h3>updateUI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateUI</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html#updateUI()" title="class or interface in javax.swing">updateUI</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html" title="class or interface in javax.swing">JPanel</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="update(boolean)">
<h3>update</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">update</span><wbr/><span class="parameters">(boolean deepUpdate)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.ui.Updatable</code></span></div>
<div class="block">Update component UI by model. If deep update  component must assume that anything in the model
 could be changed and these changes were not fired (for example when reversing code, or doing teamwork
 update).</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>update</code> in interface <code>com.nomagic.magicdraw.ui.Updatable</code></dd>
<dt>Parameters:</dt>
<dd><code>deepUpdate</code> - true if component must assume that anything in the model was changed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addTreeSelectionParticipant(com.nomagic.magicdraw.ui.browser.Tree.TreeSelectionParticipant)">
<h3>addTreeSelectionParticipant</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addTreeSelectionParticipant</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.browser.Tree.TreeSelectionParticipant participant)</span></div>
<div class="block">Adds tree selection participant</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>participant</code> - tree selection participant to execute additional methods before and after selection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="init()">
<h3>init</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">init</span>()</div>
</section>
</li>
<li>
<section class="detail" id="init(com.nomagic.magicdraw.ui.browser.Node)">
<h3>init</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> rootNode)</span></div>
</section>
</li>
<li>
<section class="detail" id="initAsync(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">
<h3 id="initAsync(java.lang.Object,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">initAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;A&gt;</span> <span class="return-type">void</span> <span class="element-name">initAsync</span><wbr/><span class="parameters">(@CheckForNull
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler)</span></div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>A</code> - The type of the object attached to the completion handler</dd>
<dt>Parameters:</dt>
<dd><code>attachment</code> - the object for completion handler attached to this operation</dd>
<dd><code>handler</code> - the handler to consume completion of this operation, see
                   <a href="#initAsync(com.nomagic.magicdraw.ui.browser.Node,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)"><code>initAsync(Node, Object, com.nomagic.magicdraw.utils.concurrent.CompletionHandler)</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initAsync(com.nomagic.magicdraw.ui.browser.Node,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">
<h3 id="initAsync(com.nomagic.magicdraw.ui.browser.Node,java.lang.Object,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">initAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;A&gt;</span> <span class="return-type">void</span> <span class="element-name">initAsync</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> root,
 @CheckForNull
 A attachment,
 @CheckForNull
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root</dd>
<dd><code>attachment</code> - the object for completion handler attached to this operation</dd>
<dd><code>handler</code> - the handler to consume completion of this operation or <code>null</code>. The
                   handler is always invoked on <code>EventQueue</code> dispatch thread</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="maybeInvokeChainedHandler(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,java.lang.Throwable)">
<h3 id="maybeInvokeChainedHandler(java.lang.Object,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,java.lang.Throwable)">maybeInvokeChainedHandler</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="type-parameters">&lt;A&gt;</span> <span class="return-type">void</span> <span class="element-name">maybeInvokeChainedHandler</span><wbr/><span class="parameters">(@CheckForNull
 A attachment,
 @CheckForNull
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> exc)</span></div>
</section>
</li>
<li>
<section class="detail" id="maybeInvokeChainedCH(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,java.lang.Throwable)">
<h3 id="maybeInvokeChainedCH(java.lang.Object,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,java.lang.Throwable)">maybeInvokeChainedCH</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="type-parameters">&lt;A&gt;</span> <span class="return-type">void</span> <span class="element-name">maybeInvokeChainedCH</span><wbr/><span class="parameters">(@CheckForNull
 A attachment,
 @CheckForNull
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> exc)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateBrowser()">
<h3>updateBrowser</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">updateBrowser</span>()</div>
<div class="block">Updates dirty nodes in tree with the newest data and shows it.
 The current thread will be blocked until tree update is complete,
 but the event dispatcher is going to continue to process events.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if update was performed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="delete(com.nomagic.magicdraw.ui.browser.Node[])">
<h3>delete</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">delete</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] node)</span></div>
</section>
</li>
<li>
<section class="detail" id="delete(com.nomagic.magicdraw.ui.browser.Node[],boolean,com.dassault_systemes.modeler.foundation.editing.MacroCommand)">
<h3>delete</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">delete</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] nodes,
 boolean useSpecificDeletion,
 @CheckForNull
 com.dassault_systemes.modeler.foundation.editing.MacroCommand macroCommand)</span></div>
<div class="block">Deletes nodes</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>nodes</code> - nodes which will be deleted</dd>
<dd><code>useSpecificDeletion</code> - if true deletes nodes with specific remove command</dd>
<dd><code>macroCommand</code> - to add delete commands</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canDelete(com.nomagic.magicdraw.ui.browser.Node[])">
<h3>canDelete</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canDelete</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] node)</span></div>
<div class="block">Test if all nodes can be deleted</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - array to check</dd>
<dt>Returns:</dt>
<dd>true if all elements can be deleted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateBrowser(boolean)">
<h3>updateBrowser</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">updateBrowser</span><wbr/><span class="parameters">(boolean updateOnlyDirty)</span></div>
<div class="block">Updates tree with the newest data and shows it. The current thread will
 be blocked until tree update is complete, but the event dispatcher
 is going to continue to process events.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>updateOnlyDirty</code> - - if <code>true</code> updates only dirty expanded nodes,
                        otherwise - updates all expanded tree nodes</dd>
<dt>Returns:</dt>
<dd>true if update was performed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateBrowser(boolean,boolean)">
<h3>updateBrowser</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">updateBrowser</span><wbr/><span class="parameters">(boolean updateOnlyDirty,
 boolean updateNotShowing)</span></div>
<div class="block">Updates tree with the newest data and shows it. The current thread will
 be blocked until tree update is complete, but the event dispatcher
 is going to continue to process events.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>updateOnlyDirty</code> - if <code>true</code> updates only dirty expanded nodes,
                         otherwise - updates all expanded tree nodes.</dd>
<dd><code>updateNotShowing</code> - forces update even if component is not showing.</dd>
<dt>Returns:</dt>
<dd>true if update was performed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="browserUpdateDelayed(boolean)">
<h3>browserUpdateDelayed</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">browserUpdateDelayed</span><wbr/><span class="parameters">(boolean updateOnlyDirty)</span></div>
<div class="block">Called if browser lazy and update vas delayed</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>updateOnlyDirty</code> - if <code>true</code> updates only dirty expanded nodes,
                        otherwise - updates all expanded tree nodes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="specificUpdateBrowser(boolean)">
<h3>specificUpdateBrowser</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">specificUpdateBrowser</span><wbr/><span class="parameters">(boolean updateOnlyDirty)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateBrowserAsync(boolean,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,com.nomagic.task.ProgressStatus)">
<h3 id="updateBrowserAsync(boolean,java.lang.Object,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,com.nomagic.task.ProgressStatus)">updateBrowserAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;A&gt;</span> <span class="return-type">void</span> <span class="element-name">updateBrowserAsync</span><wbr/><span class="parameters">(boolean updateOnlyDirty,
 @CheckForNull
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateOnlyDirtyNodes(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,boolean)">
<h3 id="updateOnlyDirtyNodes(java.lang.Object,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,boolean)">updateOnlyDirtyNodes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="type-parameters">&lt;A&gt;</span> <span class="return-type">boolean</span> <span class="element-name">updateOnlyDirtyNodes</span><wbr/><span class="parameters">(@CheckForNull
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler,
 boolean updateAll)</span></div>
</section>
</li>
<li>
<section class="detail" id="maybeInvokeChainedHandler(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,com.nomagic.magicdraw.ui.browser.TreeModel,java.lang.Throwable)">
<h3 id="maybeInvokeChainedHandler(java.lang.Object,com.nomagic.magicdraw.utils.concurrent.CompletionHandler,com.nomagic.magicdraw.ui.browser.TreeModel,java.lang.Throwable)">maybeInvokeChainedHandler</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="type-parameters">&lt;A&gt;</span> <span class="return-type">void</span> <span class="element-name">maybeInvokeChainedHandler</span><wbr/><span class="parameters">(@CheckForNull
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;?,<wbr/>? super A&gt; handler,
 com.nomagic.magicdraw.ui.browser.TreeModel browserModel,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> exc)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSelectedNode()">
<h3>getSelectedNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></span> <span class="element-name">getSelectedNode</span>()</div>
<div class="block">Returns first selected node in the tree.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>first selected node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNode(int)">
<h3>getNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></span> <span class="element-name">getNode</span><wbr/><span class="parameters">(int row)</span></div>
<div class="block">Returns first selected node in the tree.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>first selected node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedNodes()">
<h3>getSelectedNodes</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[]</span> <span class="element-name">getSelectedNodes</span>()</div>
<div class="block">Returns all selected nodes in the tree.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all selected nodes in the tree.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toNodes(javax.swing.tree.TreePath[])">
<h3>toNodes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[]</span> <span class="element-name">toNodes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a>[] paths)</span></div>
<div class="block">Utility method for converting array of paths to array of nodes</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>paths</code> - tree paths</dd>
<dt>Returns:</dt>
<dd>nodes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toNodes(javax.swing.tree.TreePath[],boolean)">
<h3>toNodes</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type"><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[]</span> <span class="element-name">toNodes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a>[] paths,
 boolean loadingDummyNodeDistinction)</span></div>
</section>
</li>
<li>
<section class="detail" id="setSelectedNodes(com.nomagic.magicdraw.ui.browser.Node[])">
<h3>setSelectedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectedNodes</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] nodes)</span></div>
<div class="block">Selects given nodes in the tree. Deselects everything if nodes are null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>nodes</code> - nodes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toTreePaths(com.nomagic.magicdraw.ui.browser.Node[])">
<h3>toTreePaths</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a>[]</span> <span class="element-name">toTreePaths</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] nodes)</span></div>
<div class="block">Utility method for converting array of nodes to array of paths</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>nodes</code> - nodes</dd>
<dt>Returns:</dt>
<dd>tree paths</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openNode(com.nomagic.magicdraw.uml.BaseElement)">
<h3>openNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></span> <span class="element-name">openNode</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object)</span></div>
<div class="block">Opens(expands) node for a give Element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the element to expand in the tree</dd>
<dt>Returns:</dt>
<dd>path of opened node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openNode(com.nomagic.magicdraw.uml.BaseElement,boolean)">
<h3>openNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></span> <span class="element-name">openNode</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object,
 boolean requestFocus)</span></div>
<div class="block">Opens(expands) node for a give Element. May request focus for a tree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the element to expand in the tree</dd>
<dd><code>requestFocus</code> - request focus for a tree.</dd>
<dt>Returns:</dt>
<dd>path of opened node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openNode(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean)">
<h3>openNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></span> <span class="element-name">openNode</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object,
 boolean select,
 boolean appendSelection,
 boolean requestFocus)</span></div>
<div class="block">Opens(expands) node for a give Element. May request focus for a tree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the element to expand in the tree</dd>
<dd><code>select</code> - select node.</dd>
<dd><code>appendSelection</code> - append to old selection or clear old selection</dd>
<dd><code>requestFocus</code> - request focus for a tree.</dd>
<dt>Returns:</dt>
<dd>path of opened node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openNode(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean)">
<h3>openNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></span> <span class="element-name">openNode</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object,
 boolean select,
 boolean requestFocus)</span></div>
<div class="block">Opens(expands) node for a give Element. May request focus for a tree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the element to expand in the tree</dd>
<dd><code>select</code> - select node.</dd>
<dd><code>requestFocus</code> - request focus for a tree.</dd>
<dt>Returns:</dt>
<dd>path of opened node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openNode(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,boolean)">
<h3>openNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></span> <span class="element-name">openNode</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object,
 boolean select,
 boolean appendSelection,
 boolean requestFocus,
 boolean scrollToVisible)</span></div>
<div class="block">Opens(expands) node for a give Element. May request focus for a tree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the element to expand in the tree.</dd>
<dd><code>select</code> - select node.</dd>
<dd><code>appendSelection</code> - append to old selection or clear old selection</dd>
<dd><code>requestFocus</code> - request focus for a tree.</dd>
<dd><code>scrollToVisible</code> - do we need to scroll to visible?</dd>
<dt>Returns:</dt>
<dd>path of opened node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openNode(com.nomagic.magicdraw.uml.BaseElement,com.dassault_systemes.modeler.magic.ui.ElementSelection,boolean)">
<h3>openNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></span> <span class="element-name">openNode</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object,
 @CheckForNull
 com.dassault_systemes.modeler.magic.ui.ElementSelection selection,
 boolean appendSelection)</span></div>
</section>
</li>
<li>
<section class="detail" id="openNode(com.nomagic.magicdraw.uml.BaseElement,com.dassault_systemes.modeler.magic.ui.ElementSelection,boolean,boolean,boolean,boolean)">
<h3>openNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a></span> <span class="element-name">openNode</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object,
 @CheckForNull
 com.dassault_systemes.modeler.magic.ui.ElementSelection selection,
 boolean select,
 boolean appendSelection,
 boolean requestFocus,
 boolean scrollToVisible)</span></div>
</section>
</li>
<li>
<section class="detail" id="waitForPreviousEventsOnOpeningNode()">
<h3>waitForPreviousEventsOnOpeningNode</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">waitForPreviousEventsOnOpeningNode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="doBeforeOpenNode()">
<h3>doBeforeOpenNode</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">doBeforeOpenNode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="openNode(java.util.Collection)">
<h3>openNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">openNode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elements)</span></div>
</section>
</li>
<li>
<section class="detail" id="openNode(java.util.Collection,java.util.function.Consumer)">
<h3>openNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="return-type">void</span> <span class="element-name">openNode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;T&gt; failedConsumer)</span></div>
</section>
</li>
<li>
<section class="detail" id="getAutoscrollInsets()">
<h3>getAutoscrollInsets</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Insets.html" title="class or interface in java.awt">Insets</a></span> <span class="element-name">getAutoscrollInsets</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/dnd/Autoscroll.html#getAutoscrollInsets()" title="class or interface in java.awt.dnd">getAutoscrollInsets</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/dnd/Autoscroll.html" title="class or interface in java.awt.dnd">Autoscroll</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActions()">
<h3>getActions</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getActions</span>()</div>
<div class="block">Returns shortcuts action manager for this browser.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ActionsManager with actions to register in this browser as KeyListeners</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBrowserForActions(com.nomagic.magicdraw.ui.browser.Tree,com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.ui.ElementSelectionProvider)">
<h3>setBrowserForActions</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type">void</span> <span class="element-name">setBrowserForActions</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree,
 <a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 @CheckForNull
 com.nomagic.magicdraw.ui.ElementSelectionProvider provider)</span></div>
</section>
</li>
<li>
<section class="detail" id="showPopupMenu(java.awt.event.MouseEvent)">
<h3>showPopupMenu</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showPopupMenu</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html" title="class or interface in java.awt.event">MouseEvent</a> evt)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>showPopupMenu</code> in interface <code>com.nomagic.awt.PopupOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="decorateTree()">
<h3>decorateTree</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">decorateTree</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDefaultFocusable()">
<h3>getDefaultFocusable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></span> <span class="element-name">getDefaultFocusable</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../../../ui/ExtendedPanel.html#getDefaultFocusable()">ExtendedPanel</a></code></span></div>
<div class="block">Request Focus for some component. Here it is empty.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../../ui/ExtendedPanel.html#getDefaultFocusable()">getDefaultFocusable</a></code> in class <code><a href="../../../ui/ExtendedPanel.html" title="class in com.nomagic.ui">ExtendedPanel</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="editPath(javax.swing.tree.TreePath)">
<h3>editPath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">editPath</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a> path)</span></div>
</section>
</li>
<li>
<section class="detail" id="autoscroll(java.awt.Point)">
<h3>autoscroll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">autoscroll</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</span></div>
<div class="block">Implementation of auto-scroll interface method
 auto-scroll(Point)
 Scrolls to specified point.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/dnd/Autoscroll.html#autoscroll(java.awt.Point)" title="class or interface in java.awt.dnd">autoscroll</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/dnd/Autoscroll.html" title="class or interface in java.awt.dnd">Autoscroll</a></code></dd>
<dt>Parameters:</dt>
<dd><code>pt</code> - - Point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRootNode()">
<h3>getRootNode</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></span> <span class="element-name">getRootNode</span>()</div>
<div class="block">Returns root node of the tree.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractTree.html#getRootNode()">getRootNode</a></code> in class <code><a href="AbstractTree.html" title="class in com.nomagic.magicdraw.ui.browser">AbstractTree</a></code></dd>
<dt>Returns:</dt>
<dd>root node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">Removes all nodes recursively.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractTree.html#dispose()">dispose</a></code> in class <code><a href="AbstractTree.html" title="class in com.nomagic.magicdraw.ui.browser">AbstractTree</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disposeNodes()">
<h3>disposeNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disposeNodes</span>()</div>
<div class="block">Dispose nodes added into the tree.</div>
</section>
</li>
<li>
<section class="detail" id="getTreeModel()">
<h3>getTreeModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.browser.TreeModel</span> <span class="element-name">getTreeModel</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractTree.html#getTreeModel()">getTreeModel</a></code> in class <code><a href="AbstractTree.html" title="class in com.nomagic.magicdraw.ui.browser">AbstractTree</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectSelectedNodes(com.nomagic.magicdraw.ui.browser.TreeModel,javax.swing.tree.TreePath,com.nomagic.magicdraw.ui.browser.TreeSelectionTracker)">
<h3>collectSelectedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">collectSelectedNodes</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.browser.TreeModel treeModel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreePath.html" title="class or interface in javax.swing.tree">TreePath</a> parentPath,
 com.nomagic.magicdraw.ui.browser.TreeSelectionTracker selectionTracker)</span></div>
<div class="block">Collects selected nodes.
 <p>
 During event dispatching node state can change from <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser"><code>Node</code></a> &lt;-&gt; <code>LoadingDummyNode</code>
 If node was selected it must be selected when node state is changed.
 On treeStructureChanged event all selected tree paths are collected, on treeNodesChanged event they are selected.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>treeModel</code> - model</dd>
<dd><code>parentPath</code> - parent path</dd>
<dd><code>selectionTracker</code> - selection tracker</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reset()">
<h3>reset</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reset</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../../ui/Cachable.html#reset()">Cachable</a></code></span></div>
<div class="block">Cache managers invokes this method to free resources. Usually this method must drop references to external objects
 in order to enable garbage collection of them.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../ui/Cachable.html#reset()">reset</a></code> in interface <code><a href="../../../ui/Cachable.html" title="interface in com.nomagic.ui">Cachable</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParams()">
<h3>getParams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.browser.TreeParams</span> <span class="element-name">getParams</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isUpdateIfShowing()">
<h3>isUpdateIfShowing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUpdateIfShowing</span>()</div>
<div class="block">Returns if tree only updates when showing</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if tree only updates when showing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUpdateIfShowing(boolean)">
<h3>setUpdateIfShowing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUpdateIfShowing</span><wbr/><span class="parameters">(boolean updateIfShowing)</span></div>
<div class="block">Allows setting tree to update only if showing</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>updateIfShowing</code> - true if tree should only update when showing</dd>
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
