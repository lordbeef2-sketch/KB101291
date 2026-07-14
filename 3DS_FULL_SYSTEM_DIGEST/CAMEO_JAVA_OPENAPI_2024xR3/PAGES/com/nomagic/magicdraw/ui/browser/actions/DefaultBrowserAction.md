# JAVA OPENAPI: DefaultBrowserAction (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/browser/actions/DefaultBrowserAction.html
- source_path: `com/nomagic/magicdraw/ui/browser/actions/DefaultBrowserAction.html`
- source_sha256: `1c2bc3923b7569f48d4d0a2c1ad620910caeaa66bba93562b89b14de04ac501c`
- captured_utc: `2026-07-14T16:55:51.707416+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.browser.actions](package-summary.html)

## Class DefaultBrowserAction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[javax.swing.AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
[com.nomagic.actions.NMAction](../../../../actions/NMAction.html)
[com.nomagic.magicdraw.actions.MDAction](../../../actions/MDAction.html)
com.nomagic.magicdraw.ui.browser.actions.DefaultBrowserAction

All Implemented Interfaces:
`[BrowserAction](../../../actions/BrowserAction.html)`, `com.nomagic.magicdraw.actions.ShortcutSchemaAction`, `[ActionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`, `[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)`

@OpenApiAllpublic classDefaultBrowserAction
extends [MDAction](../../../actions/MDAction.html)
implements [BrowserAction](../../../actions/BrowserAction.html)

The default implementation of BrowserAction and simple MDAction

See Also:
[Serialized Form](../../../../../../serialized-form.html#com.nomagic.magicdraw.ui.browser.actions.DefaultBrowserAction)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.actions.[NMAction](../../../../actions/NMAction.html)
`[ACTION_SHORTCUTS](../../../../actions/NMAction.html#ACTION_SHORTCUTS), [BELONGS_TO_SEPARATE_GROUP_IN_UI](../../../../actions/NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI), [DO_NO_SHOW_ACTION_NAME_IN_UI](../../../../actions/NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI), [DO_NOT_REGISTER_ACTION_TO_COMPONENTS](../../../../actions/NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS), [GENERATED_ID_PREFIX](../../../../actions/NMAction.html#GENERATED_ID_PREFIX), [GROUP](../../../../actions/NMAction.html#GROUP), [ID](../../../../actions/NMAction.html#ID), [LARGE_ICON](../../../../actions/NMAction.html#LARGE_ICON), [MENU_SHORTCUT_MASK](../../../../actions/NMAction.html#MENU_SHORTCUT_MASK), [TINY_ICON](../../../../actions/NMAction.html#TINY_ICON)`
Fields inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[changeSupport](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#changeSupport), [enabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#enabled)`
Fields inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[ACCELERATOR_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACCELERATOR_KEY), [ACTION_COMMAND_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACTION_COMMAND_KEY), [DEFAULT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DEFAULT), [DISPLAYED_MNEMONIC_INDEX_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DISPLAYED_MNEMONIC_INDEX_KEY), [LARGE_ICON_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LARGE_ICON_KEY), [LONG_DESCRIPTION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LONG_DESCRIPTION), [MNEMONIC_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#MNEMONIC_KEY), [NAME](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#NAME), [SELECTED_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SELECTED_KEY), [SHORT_DESCRIPTION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SHORT_DESCRIPTION), [SMALL_ICON](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SMALL_ICON)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DefaultBrowserAction](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionName,
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`
Constructs new action.
`[DefaultBrowserAction](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionName,
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 boolean useShortcutSchema)`
Constructs new action.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Tree](../Tree.html)`
`[getActiveTree](#getActiveTree())()`

`[BaseElement](../../../uml/BaseElement.html)`
`[getFirstElement](#getFirstElement())()`
Returns the first selected element.
`[BaseElement](../../../uml/BaseElement.html)`
`[getFirstElement](#getFirstElement(com.nomagic.magicdraw.ui.browser.Tree))([Tree](../Tree.html) tree)`
Returns the first selected element in a given tree.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../../../uml/BaseElement.html)>`
`[getSelectedBaseElements](#getSelectedBaseElements())()`
Collects selected base elements in the tree
`protected [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getSelectedObject](#getSelectedObject())()`

`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getSelectedObject](#getSelectedObject(com.nomagic.magicdraw.ui.browser.Tree))([Tree](../Tree.html) tree)`
Returns the first selected object in a given tree.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?>`
`[getSelectedObjects](#getSelectedObjects())()`
Collect selected user objects in the tree
`static [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getSelectedObjectsStream](#getSelectedObjectsStream(com.nomagic.magicdraw.ui.browser.Tree))([Tree](../Tree.html) tree)`

`[Tree](../Tree.html)`
`[getTree](#getTree())()`
Return tree of this action.
`protected [Tree](../Tree.html)`
`[getTreeOrActiveTree](#getTreeOrActiveTree())()`

`void`
`[setTree](#setTree(com.nomagic.magicdraw.ui.browser.Tree))([Tree](../Tree.html) tree)`
Set the tree for this action.
Methods inherited from class com.nomagic.magicdraw.actions.[MDAction](../../../actions/MDAction.html)
`[actionPerformed](../../../actions/MDAction.html#actionPerformed(java.awt.event.ActionEvent)), [isUseShortcutSchema](../../../actions/MDAction.html#isUseShortcutSchema()), [updateState](../../../actions/MDAction.html#updateState())`
Methods inherited from class com.nomagic.actions.[NMAction](../../../../actions/NMAction.html)
`[accept](../../../../actions/NMAction.html#accept(com.nomagic.actions.ActionsVisitor)), [addAction](../../../../actions/NMAction.html#addAction(com.nomagic.actions.NMAction)), [addPropertyChangeListener](../../../../actions/NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addShortcut](../../../../actions/NMAction.html#addShortcut(javax.swing.KeyStroke)), [addShotcut](../../../../actions/NMAction.html#addShotcut(javax.swing.KeyStroke)), [addWeakPropertyChangeListener](../../../../actions/NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [clone](../../../../actions/NMAction.html#clone()), [compareTo](../../../../actions/NMAction.html#compareTo(java.lang.Object)), [createMenuItem](../../../../actions/NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)), [equals](../../../../actions/NMAction.html#equals(java.lang.Object)), [firePropertyChange](../../../../actions/NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [forEach](../../../../actions/NMAction.html#forEach(java.util.function.Consumer)), [forEachIncludingSelf](../../../../actions/NMAction.html#forEachIncludingSelf(java.util.function.Consumer)), [getActions](../../../../actions/NMAction.html#getActions()), [getCommandKey](../../../../actions/NMAction.html#getCommandKey()), [getDescription](../../../../actions/NMAction.html#getDescription()), [getGroup](../../../../actions/NMAction.html#getGroup()), [getIcon](../../../../actions/NMAction.html#getIcon()), [getID](../../../../actions/NMAction.html#getID()), [getLargeIcon](../../../../actions/NMAction.html#getLargeIcon()), [getLargeOrSmallIcon](../../../../actions/NMAction.html#getLargeOrSmallIcon()), [getMenuShortcutMaskAsString](../../../../actions/NMAction.html#getMenuShortcutMaskAsString()), [getMnemonicKey](../../../../actions/NMAction.html#getMnemonicKey()), [getName](../../../../actions/NMAction.html#getName()), [getPropertyChangeListeners](../../../../actions/NMAction.html#getPropertyChangeListeners()), [getShortcuts](../../../../actions/NMAction.html#getShortcuts()), [getSmallIcon](../../../../actions/NMAction.html#getSmallIcon()), [getSmallOrLargeIcon](../../../../actions/NMAction.html#getSmallOrLargeIcon()), [getTinyIcon](../../../../actions/NMAction.html#getTinyIcon()), [hashCode](../../../../actions/NMAction.html#hashCode()), [hasMenuShortcutMask](../../../../actions/NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)), [isIDGenerated](../../../../actions/NMAction.html#isIDGenerated()), [removeAction](../../../../actions/NMAction.html#removeAction(com.nomagic.actions.NMAction)), [removeIf](../../../../actions/NMAction.html#removeIf(java.util.function.Predicate)), [removePropertyChangeListener](../../../../actions/NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [removeShortcut](../../../../actions/NMAction.html#removeShortcut(javax.swing.KeyStroke)), [removeWeakPropertyChangeListener](../../../../actions/NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [setActions](../../../../actions/NMAction.html#setActions(java.util.List)), [setDescription](../../../../actions/NMAction.html#setDescription(java.lang.String)), [setGroup](../../../../actions/NMAction.html#setGroup(java.lang.String)), [setIcon](../../../../actions/NMAction.html#setIcon(javax.swing.Icon)), [setLargeIcon](../../../../actions/NMAction.html#setLargeIcon(javax.swing.Icon)), [setMnemonicKey](../../../../actions/NMAction.html#setMnemonicKey(int)), [setName](../../../../actions/NMAction.html#setName(java.lang.String)), [setShortcuts](../../../../actions/NMAction.html#setShortcuts(java.util.List)), [setSmallIcon](../../../../actions/NMAction.html#setSmallIcon(javax.swing.Icon)), [setTinyIcon](../../../../actions/NMAction.html#setTinyIcon(javax.swing.Icon)), [shallowClone](../../../../actions/NMAction.html#shallowClone()), [toString](../../../../actions/NMAction.html#toString())`
Methods inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[getKeys](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()), [getValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)), [isEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()), [putValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)), [setEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[accept](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DefaultBrowserAction
@OpenApipublic DefaultBrowserAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionName,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
Constructs new action.
Parameters:
`actionID` - the action ID
`actionName` - the action name
`stroke` - the action stroke
`group` - the action group
DefaultBrowserAction
@OpenApipublic DefaultBrowserAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionName,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 boolean useShortcutSchema)
Constructs new action.
Parameters:
`actionID` - the action ID
`actionName` - the action name
`stroke` - the action stroke
`group` - the action group
`useShortcutSchema` - use shortcut schema
 ============ METHOD DETAIL ========== 
Method Details
setTree
public void setTree(@CheckForNull
 [Tree](../Tree.html) tree)
Set the tree for this action.
Specified by:
`[setTree](../../../actions/BrowserAction.html#setTree(com.nomagic.magicdraw.ui.browser.Tree))` in interface `[BrowserAction](../../../actions/BrowserAction.html)`
Parameters:
`tree` - the browser for this action
getTree
@CheckForNullpublic [Tree](../Tree.html) getTree()
Return tree of this action.
 MagicDraw framework guarantees that the tree will set if this method is called from updateState() or
 actionPerformed(ActionEvent) methods.
Returns:
browser of this action
getTreeOrActiveTree
@CheckForNullprotected [Tree](../Tree.html) getTreeOrActiveTree()
Returns:
action's tree or active tree in browser of action's tree is null
getActiveTree
@CheckForNullpublic static [Tree](../Tree.html) getActiveTree()
getSelectedObject
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getSelectedObject(@CheckForNull
 [Tree](../Tree.html) tree)
Returns the first selected object in a given tree.
Parameters:
`tree` - the given tree
Returns:
first selected object
getFirstElement
@CheckForNullpublic [BaseElement](../../../uml/BaseElement.html) getFirstElement(@CheckForNull
 [Tree](../Tree.html) tree)
Returns the first selected element in a given tree.
Parameters:
`tree` - the given tree
Returns:
first selected element
getFirstElement
@CheckForNullpublic [BaseElement](../../../uml/BaseElement.html) getFirstElement()
Returns the first selected element.
Returns:
the first selected element
getSelectedObject
@CheckForNullprotected [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getSelectedObject()
Returns:
selected object in the tree
getSelectedObjects
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> getSelectedObjects()
Collect selected user objects in the tree
Returns:
collection of selected objects. Empty collection is nothing is selected
getSelectedBaseElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../../../uml/BaseElement.html)> getSelectedBaseElements()
Collects selected base elements in the tree
Returns:
collection of selected base elements. Empty collection is nothing is selected
getSelectedObjectsStream
public static [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getSelectedObjectsStream(@CheckForNull
 [Tree](../Tree.html) tree)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.browser.actions</a></div>
<h1 class="title" title="Class DefaultBrowserAction">Class DefaultBrowserAction</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">javax.swing.AbstractAction</a>
<div class="inheritance"><a href="../../../../actions/NMAction.html" title="class in com.nomagic.actions">com.nomagic.actions.NMAction</a>
<div class="inheritance"><a href="../../../actions/MDAction.html" title="class in com.nomagic.magicdraw.actions">com.nomagic.magicdraw.actions.MDAction</a>
<div class="inheritance">com.nomagic.magicdraw.ui.browser.actions.DefaultBrowserAction</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../actions/BrowserAction.html" title="interface in com.nomagic.magicdraw.actions">BrowserAction</a></code>, <code>com.nomagic.magicdraw.actions.ShortcutSchemaAction</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DefaultBrowserAction</span>
<span class="extends-implements">extends <a href="../../../actions/MDAction.html" title="class in com.nomagic.magicdraw.actions">MDAction</a>
implements <a href="../../../actions/BrowserAction.html" title="interface in com.nomagic.magicdraw.actions">BrowserAction</a></span></div>
<div class="block">The default implementation of BrowserAction and simple MDAction</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../serialized-form.html#com.nomagic.magicdraw.ui.browser.actions.DefaultBrowserAction">Serialized Form</a></li>
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
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.actions.NMAction">Fields inherited from class com.nomagic.actions.<a href="../../../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="../../../../actions/NMAction.html#ACTION_SHORTCUTS">ACTION_SHORTCUTS</a>, <a href="../../../../actions/NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI">BELONGS_TO_SEPARATE_GROUP_IN_UI</a>, <a href="../../../../actions/NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI">DO_NO_SHOW_ACTION_NAME_IN_UI</a>, <a href="../../../../actions/NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS">DO_NOT_REGISTER_ACTION_TO_COMPONENTS</a>, <a href="../../../../actions/NMAction.html#GENERATED_ID_PREFIX">GENERATED_ID_PREFIX</a>, <a href="../../../../actions/NMAction.html#GROUP">GROUP</a>, <a href="../../../../actions/NMAction.html#ID">ID</a>, <a href="../../../../actions/NMAction.html#LARGE_ICON">LARGE_ICON</a>, <a href="../../../../actions/NMAction.html#MENU_SHORTCUT_MASK">MENU_SHORTCUT_MASK</a>, <a href="../../../../actions/NMAction.html#TINY_ICON">TINY_ICON</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.AbstractAction">Fields inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">AbstractAction</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#changeSupport" title="class or interface in javax.swing">changeSupport</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#enabled" title="class or interface in javax.swing">enabled</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.Action">Fields inherited from interface javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACCELERATOR_KEY" title="class or interface in javax.swing">ACCELERATOR_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACTION_COMMAND_KEY" title="class or interface in javax.swing">ACTION_COMMAND_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DEFAULT" title="class or interface in javax.swing">DEFAULT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DISPLAYED_MNEMONIC_INDEX_KEY" title="class or interface in javax.swing">DISPLAYED_MNEMONIC_INDEX_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LARGE_ICON_KEY" title="class or interface in javax.swing">LARGE_ICON_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LONG_DESCRIPTION" title="class or interface in javax.swing">LONG_DESCRIPTION</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#MNEMONIC_KEY" title="class or interface in javax.swing">MNEMONIC_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#NAME" title="class or interface in javax.swing">NAME</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SELECTED_KEY" title="class or interface in javax.swing">SELECTED_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SHORT_DESCRIPTION" title="class or interface in javax.swing">SHORT_DESCRIPTION</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SMALL_ICON" title="class or interface in javax.swing">SMALL_ICON</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String)">DefaultBrowserAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs new action.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String,boolean)">DefaultBrowserAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 boolean useShortcutSchema)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs new action.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveTree()">getActiveTree</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstElement()">getFirstElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the first selected element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstElement(com.nomagic.magicdraw.ui.browser.Tree)">getFirstElement</a><wbr/>(<a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the first selected element in a given tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedBaseElements()">getSelectedBaseElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects selected base elements in the tree</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedObject()">getSelectedObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedObject(com.nomagic.magicdraw.ui.browser.Tree)">getSelectedObject</a><wbr/>(<a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first selected object in a given tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedObjects()">getSelectedObjects</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collect selected user objects in the tree</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedObjectsStream(com.nomagic.magicdraw.ui.browser.Tree)">getSelectedObjectsStream</a><wbr/>(<a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTree()">getTree</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return tree of this action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTreeOrActiveTree()">getTreeOrActiveTree</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTree(com.nomagic.magicdraw.ui.browser.Tree)">setTree</a><wbr/>(<a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the tree for this action.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.actions.MDAction">Methods inherited from class com.nomagic.magicdraw.actions.<a href="../../../actions/MDAction.html" title="class in com.nomagic.magicdraw.actions">MDAction</a></h3>
<code><a href="../../../actions/MDAction.html#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a>, <a href="../../../actions/MDAction.html#isUseShortcutSchema()">isUseShortcutSchema</a>, <a href="../../../actions/MDAction.html#updateState()">updateState</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.NMAction">Methods inherited from class com.nomagic.actions.<a href="../../../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="../../../../actions/NMAction.html#accept(com.nomagic.actions.ActionsVisitor)">accept</a>, <a href="../../../../actions/NMAction.html#addAction(com.nomagic.actions.NMAction)">addAction</a>, <a href="../../../../actions/NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../actions/NMAction.html#addShortcut(javax.swing.KeyStroke)">addShortcut</a>, <a href="../../../../actions/NMAction.html#addShotcut(javax.swing.KeyStroke)">addShotcut</a>, <a href="../../../../actions/NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)">addWeakPropertyChangeListener</a>, <a href="../../../../actions/NMAction.html#clone()">clone</a>, <a href="../../../../actions/NMAction.html#compareTo(java.lang.Object)">compareTo</a>, <a href="../../../../actions/NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)">createMenuItem</a>, <a href="../../../../actions/NMAction.html#equals(java.lang.Object)">equals</a>, <a href="../../../../actions/NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../actions/NMAction.html#forEach(java.util.function.Consumer)">forEach</a>, <a href="../../../../actions/NMAction.html#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a>, <a href="../../../../actions/NMAction.html#getActions()">getActions</a>, <a href="../../../../actions/NMAction.html#getCommandKey()">getCommandKey</a>, <a href="../../../../actions/NMAction.html#getDescription()">getDescription</a>, <a href="../../../../actions/NMAction.html#getGroup()">getGroup</a>, <a href="../../../../actions/NMAction.html#getIcon()">getIcon</a>, <a href="../../../../actions/NMAction.html#getID()">getID</a>, <a href="../../../../actions/NMAction.html#getLargeIcon()">getLargeIcon</a>, <a href="../../../../actions/NMAction.html#getLargeOrSmallIcon()">getLargeOrSmallIcon</a>, <a href="../../../../actions/NMAction.html#getMenuShortcutMaskAsString()">getMenuShortcutMaskAsString</a>, <a href="../../../../actions/NMAction.html#getMnemonicKey()">getMnemonicKey</a>, <a href="../../../../actions/NMAction.html#getName()">getName</a>, <a href="../../../../actions/NMAction.html#getPropertyChangeListeners()">getPropertyChangeListeners</a>, <a href="../../../../actions/NMAction.html#getShortcuts()">getShortcuts</a>, <a href="../../../../actions/NMAction.html#getSmallIcon()">getSmallIcon</a>, <a href="../../../../actions/NMAction.html#getSmallOrLargeIcon()">getSmallOrLargeIcon</a>, <a href="../../../../actions/NMAction.html#getTinyIcon()">getTinyIcon</a>, <a href="../../../../actions/NMAction.html#hashCode()">hashCode</a>, <a href="../../../../actions/NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)">hasMenuShortcutMask</a>, <a href="../../../../actions/NMAction.html#isIDGenerated()">isIDGenerated</a>, <a href="../../../../actions/NMAction.html#removeAction(com.nomagic.actions.NMAction)">removeAction</a>, <a href="../../../../actions/NMAction.html#removeIf(java.util.function.Predicate)">removeIf</a>, <a href="../../../../actions/NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../actions/NMAction.html#removeShortcut(javax.swing.KeyStroke)">removeShortcut</a>, <a href="../../../../actions/NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)">removeWeakPropertyChangeListener</a>, <a href="../../../../actions/NMAction.html#setActions(java.util.List)">setActions</a>, <a href="../../../../actions/NMAction.html#setDescription(java.lang.String)">setDescription</a>, <a href="../../../../actions/NMAction.html#setGroup(java.lang.String)">setGroup</a>, <a href="../../../../actions/NMAction.html#setIcon(javax.swing.Icon)">setIcon</a>, <a href="../../../../actions/NMAction.html#setLargeIcon(javax.swing.Icon)">setLargeIcon</a>, <a href="../../../../actions/NMAction.html#setMnemonicKey(int)">setMnemonicKey</a>, <a href="../../../../actions/NMAction.html#setName(java.lang.String)">setName</a>, <a href="../../../../actions/NMAction.html#setShortcuts(java.util.List)">setShortcuts</a>, <a href="../../../../actions/NMAction.html#setSmallIcon(javax.swing.Icon)">setSmallIcon</a>, <a href="../../../../actions/NMAction.html#setTinyIcon(javax.swing.Icon)">setTinyIcon</a>, <a href="../../../../actions/NMAction.html#shallowClone()">shallowClone</a>, <a href="../../../../actions/NMAction.html#toString()">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.AbstractAction">Methods inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">AbstractAction</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()" title="class or interface in javax.swing">getKeys</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)" title="class or interface in javax.swing">getValue</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()" title="class or interface in javax.swing">isEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)" title="class or interface in javax.swing">putValue</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean)" title="class or interface in javax.swing">setEnabled</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.Action">Methods inherited from interface javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object)" title="class or interface in javax.swing">accept</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String)">
<h3>DefaultBrowserAction</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">DefaultBrowserAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Constructs new action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionID</code> - the action ID</dd>
<dd><code>actionName</code> - the action name</dd>
<dd><code>stroke</code> - the action stroke</dd>
<dd><code>group</code> - the action group</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String,boolean)">
<h3>DefaultBrowserAction</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">DefaultBrowserAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 boolean useShortcutSchema)</span></div>
<div class="block">Constructs new action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionID</code> - the action ID</dd>
<dd><code>actionName</code> - the action name</dd>
<dd><code>stroke</code> - the action stroke</dd>
<dd><code>group</code> - the action group</dd>
<dd><code>useShortcutSchema</code> - use shortcut schema</dd>
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
<section class="detail" id="setTree(com.nomagic.magicdraw.ui.browser.Tree)">
<h3>setTree</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTree</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</span></div>
<div class="block">Set the tree for this action.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../actions/BrowserAction.html#setTree(com.nomagic.magicdraw.ui.browser.Tree)">setTree</a></code> in interface <code><a href="../../../actions/BrowserAction.html" title="interface in com.nomagic.magicdraw.actions">BrowserAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>tree</code> - the browser for this action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTree()">
<h3>getTree</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a></span> <span class="element-name">getTree</span>()</div>
<div class="block">Return tree of this action.
 MagicDraw framework guarantees that the tree will set if this method is called from updateState() or
 actionPerformed(ActionEvent) methods.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>browser of this action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTreeOrActiveTree()">
<h3>getTreeOrActiveTree</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a></span> <span class="element-name">getTreeOrActiveTree</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>action's tree or active tree in browser of action's tree is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActiveTree()">
<h3>getActiveTree</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a></span> <span class="element-name">getActiveTree</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSelectedObject(com.nomagic.magicdraw.ui.browser.Tree)">
<h3>getSelectedObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getSelectedObject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</span></div>
<div class="block">Returns the first selected object in a given tree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - the given tree</dd>
<dt>Returns:</dt>
<dd>first selected object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstElement(com.nomagic.magicdraw.ui.browser.Tree)">
<h3>getFirstElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getFirstElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</span></div>
<div class="block">Returns the first selected element in a given tree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - the given tree</dd>
<dt>Returns:</dt>
<dd>first selected element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstElement()">
<h3>getFirstElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getFirstElement</span>()</div>
<div class="block">Returns the first selected element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the first selected element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedObject()">
<h3>getSelectedObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getSelectedObject</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>selected object in the tree</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedObjects()">
<h3>getSelectedObjects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</span> <span class="element-name">getSelectedObjects</span>()</div>
<div class="block">Collect selected user objects in the tree</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of selected objects. Empty collection is nothing is selected</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedBaseElements()">
<h3>getSelectedBaseElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getSelectedBaseElements</span>()</div>
<div class="block">Collects selected base elements in the tree</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of selected base elements. Empty collection is nothing is selected</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedObjectsStream(com.nomagic.magicdraw.ui.browser.Tree)">
<h3>getSelectedObjectsStream</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getSelectedObjectsStream</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</span></div>
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
