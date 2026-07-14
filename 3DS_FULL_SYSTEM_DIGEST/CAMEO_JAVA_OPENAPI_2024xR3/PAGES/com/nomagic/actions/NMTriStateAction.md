# JAVA OPENAPI: NMTriStateAction (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/actions/NMTriStateAction.html
- source_path: `com/nomagic/actions/NMTriStateAction.html`
- source_sha256: `9417f526e55aa23f73cb73610699bfbff84693488c253c8072194dc87c95b68f`
- captured_utc: `2026-07-14T16:55:01.515853+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.actions](package-summary.html)

## Class NMTriStateAction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[javax.swing.AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
[com.nomagic.actions.NMAction](NMAction.html)
[com.nomagic.actions.BaseNMStateAction](BaseNMStateAction.html)
com.nomagic.actions.NMTriStateAction

All Implemented Interfaces:
`[ActionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`, `[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)`

Direct Known Subclasses:
`[MDTriStateAction](../magicdraw/actions/MDTriStateAction.html)`

@OpenApiAllpublic classNMTriStateAction
extends [BaseNMStateAction](BaseNMStateAction.html)

See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.actions.NMTriStateAction)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static enum`
`[NMTriStateAction.ACTION_STATE](NMTriStateAction.ACTION_STATE.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TRI_STATE](#TRI_STATE)`
The state property.
Fields inherited from class com.nomagic.actions.[BaseNMStateAction](BaseNMStateAction.html)
`[GROUPED](BaseNMStateAction.html#GROUPED)`
Fields inherited from class com.nomagic.actions.[NMAction](NMAction.html)
`[ACTION_SHORTCUTS](NMAction.html#ACTION_SHORTCUTS), [BELONGS_TO_SEPARATE_GROUP_IN_UI](NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI), [DO_NO_SHOW_ACTION_NAME_IN_UI](NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI), [DO_NOT_REGISTER_ACTION_TO_COMPONENTS](NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS), [GENERATED_ID_PREFIX](NMAction.html#GENERATED_ID_PREFIX), [GROUP](NMAction.html#GROUP), [ID](NMAction.html#ID), [LARGE_ICON](NMAction.html#LARGE_ICON), [MENU_SHORTCUT_MASK](NMAction.html#MENU_SHORTCUT_MASK), [TINY_ICON](NMAction.html#TINY_ICON)`
Fields inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[changeSupport](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#changeSupport), [enabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#enabled)`
Fields inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[ACCELERATOR_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACCELERATOR_KEY), [ACTION_COMMAND_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACTION_COMMAND_KEY), [DEFAULT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DEFAULT), [DISPLAYED_MNEMONIC_INDEX_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DISPLAYED_MNEMONIC_INDEX_KEY), [LARGE_ICON_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LARGE_ICON_KEY), [LONG_DESCRIPTION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LONG_DESCRIPTION), [MNEMONIC_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#MNEMONIC_KEY), [NAME](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#NAME), [SELECTED_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SELECTED_KEY), [SHORT_DESCRIPTION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SHORT_DESCRIPTION), [SMALL_ICON](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SMALL_ICON)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[NMTriStateAction](#%3Cinit%3E(java.lang.String,java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int mnemonic)`

`[NMTriStateAction](#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int mnemonic,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`

`[NMTriStateAction](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke)`

`[NMTriStateAction](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.actions.ActionsVisitor))([ActionsVisitor](ActionsVisitor.html) visitor)`
Accepts ActionsVisitor using Visitor design pattern.
`void`
`[actionPerformed](#actionPerformed(java.awt.event.ActionEvent))([ActionEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionEvent.html) e)`
Executes given action.
`[NMTriStateAction.ACTION_STATE](NMTriStateAction.ACTION_STATE.html)`
`[getState](#getState())()`

`void`
`[setMixedIconSupplier](#setMixedIconSupplier(java.util.function.Supplier))([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)> mixedIconSupplier)`

`void`
`[setSelectedIconSupplier](#setSelectedIconSupplier(java.util.function.Supplier))([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)> selectedIconSupplier)`

`void`
`[setState](#setState(com.nomagic.actions.NMTriStateAction.ACTION_STATE))([NMTriStateAction.ACTION_STATE](NMTriStateAction.ACTION_STATE.html) state)`
Sets action String state.
`void`
`[setUnselectedIconSupplier](#setUnselectedIconSupplier(java.util.function.Supplier))([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)> unselectedIconSupplier)`
Methods inherited from class com.nomagic.actions.[BaseNMStateAction](BaseNMStateAction.html)
`[isGrouped](BaseNMStateAction.html#isGrouped()), [setGrouped](BaseNMStateAction.html#setGrouped(boolean))`
Methods inherited from class com.nomagic.actions.[NMAction](NMAction.html)
`[addAction](NMAction.html#addAction(com.nomagic.actions.NMAction)), [addPropertyChangeListener](NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addShortcut](NMAction.html#addShortcut(javax.swing.KeyStroke)), [addShotcut](NMAction.html#addShotcut(javax.swing.KeyStroke)), [addWeakPropertyChangeListener](NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [clone](NMAction.html#clone()), [compareTo](NMAction.html#compareTo(java.lang.Object)), [createMenuItem](NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)), [equals](NMAction.html#equals(java.lang.Object)), [firePropertyChange](NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [forEach](NMAction.html#forEach(java.util.function.Consumer)), [forEachIncludingSelf](NMAction.html#forEachIncludingSelf(java.util.function.Consumer)), [getActions](NMAction.html#getActions()), [getCommandKey](NMAction.html#getCommandKey()), [getDescription](NMAction.html#getDescription()), [getGroup](NMAction.html#getGroup()), [getIcon](NMAction.html#getIcon()), [getID](NMAction.html#getID()), [getLargeIcon](NMAction.html#getLargeIcon()), [getLargeOrSmallIcon](NMAction.html#getLargeOrSmallIcon()), [getMenuShortcutMaskAsString](NMAction.html#getMenuShortcutMaskAsString()), [getMnemonicKey](NMAction.html#getMnemonicKey()), [getName](NMAction.html#getName()), [getPropertyChangeListeners](NMAction.html#getPropertyChangeListeners()), [getShortcuts](NMAction.html#getShortcuts()), [getSmallIcon](NMAction.html#getSmallIcon()), [getSmallOrLargeIcon](NMAction.html#getSmallOrLargeIcon()), [getTinyIcon](NMAction.html#getTinyIcon()), [hashCode](NMAction.html#hashCode()), [hasMenuShortcutMask](NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)), [isIDGenerated](NMAction.html#isIDGenerated()), [removeAction](NMAction.html#removeAction(com.nomagic.actions.NMAction)), [removeIf](NMAction.html#removeIf(java.util.function.Predicate)), [removePropertyChangeListener](NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [removeShortcut](NMAction.html#removeShortcut(javax.swing.KeyStroke)), [removeWeakPropertyChangeListener](NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [setActions](NMAction.html#setActions(java.util.List)), [setDescription](NMAction.html#setDescription(java.lang.String)), [setGroup](NMAction.html#setGroup(java.lang.String)), [setIcon](NMAction.html#setIcon(javax.swing.Icon)), [setLargeIcon](NMAction.html#setLargeIcon(javax.swing.Icon)), [setMnemonicKey](NMAction.html#setMnemonicKey(int)), [setName](NMAction.html#setName(java.lang.String)), [setShortcuts](NMAction.html#setShortcuts(java.util.List)), [setSmallIcon](NMAction.html#setSmallIcon(javax.swing.Icon)), [setTinyIcon](NMAction.html#setTinyIcon(javax.swing.Icon)), [shallowClone](NMAction.html#shallowClone()), [toString](NMAction.html#toString()), [updateState](NMAction.html#updateState())`
Methods inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[getKeys](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()), [getValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)), [isEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()), [putValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)), [setEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[accept](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object))`

============ FIELD DETAIL =========== 
Field Details
TRI_STATE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRI_STATE
The state property. Value of this property is an enumeration
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.NMTriStateAction.TRI_STATE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
NMTriStateAction
public NMTriStateAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
NMTriStateAction
public NMTriStateAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int mnemonic,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
NMTriStateAction
public NMTriStateAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke)
NMTriStateAction
public NMTriStateAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int mnemonic)
 ============ METHOD DETAIL ========== 
Method Details
setState
public void setState([NMTriStateAction.ACTION_STATE](NMTriStateAction.ACTION_STATE.html) state)
Sets action String state.
Parameters:
`state` - new state of action.
getState
public [NMTriStateAction.ACTION_STATE](NMTriStateAction.ACTION_STATE.html) getState()
Returns:
the state of the action
setMixedIconSupplier
public void setMixedIconSupplier([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)> mixedIconSupplier)
setSelectedIconSupplier
public void setSelectedIconSupplier([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)> selectedIconSupplier)
setUnselectedIconSupplier
public void setUnselectedIconSupplier([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)> unselectedIconSupplier)
actionPerformed
public void actionPerformed(@CheckForNull
 [ActionEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionEvent.html) e)
Executes given action.
Specified by:
`[actionPerformed](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html#actionPerformed(java.awt.event.ActionEvent))` in interface `[ActionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html)`
Specified by:
`[actionPerformed](NMAction.html#actionPerformed(java.awt.event.ActionEvent))` in class `[NMAction](NMAction.html)`
Parameters:
`e` - event caused execution.
accept
public void accept([ActionsVisitor](ActionsVisitor.html) visitor)
Accepts ActionsVisitor using Visitor design pattern.
Overrides:
`[accept](NMAction.html#accept(com.nomagic.actions.ActionsVisitor))` in class `[NMAction](NMAction.html)`
Parameters:
`visitor` - visitor to accept.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.actions</a></div>
<h1 class="title" title="Class NMTriStateAction">Class NMTriStateAction</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">javax.swing.AbstractAction</a>
<div class="inheritance"><a href="NMAction.html" title="class in com.nomagic.actions">com.nomagic.actions.NMAction</a>
<div class="inheritance"><a href="BaseNMStateAction.html" title="class in com.nomagic.actions">com.nomagic.actions.BaseNMStateAction</a>
<div class="inheritance">com.nomagic.actions.NMTriStateAction</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../magicdraw/actions/MDTriStateAction.html" title="class in com.nomagic.magicdraw.actions">MDTriStateAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">NMTriStateAction</span>
<span class="extends-implements">extends <a href="BaseNMStateAction.html" title="class in com.nomagic.actions">BaseNMStateAction</a></span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../serialized-form.html#com.nomagic.actions.NMTriStateAction">Serialized Form</a></li>
</ul>
</dd>
</dl>
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
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="NMTriStateAction.ACTION_STATE.html" title="enum class in com.nomagic.actions">NMTriStateAction.ACTION_STATE</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TRI_STATE">TRI_STATE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The state property.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.actions.BaseNMStateAction">Fields inherited from class com.nomagic.actions.<a href="BaseNMStateAction.html" title="class in com.nomagic.actions">BaseNMStateAction</a></h3>
<code><a href="BaseNMStateAction.html#GROUPED">GROUPED</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.actions.NMAction">Fields inherited from class com.nomagic.actions.<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="NMAction.html#ACTION_SHORTCUTS">ACTION_SHORTCUTS</a>, <a href="NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI">BELONGS_TO_SEPARATE_GROUP_IN_UI</a>, <a href="NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI">DO_NO_SHOW_ACTION_NAME_IN_UI</a>, <a href="NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS">DO_NOT_REGISTER_ACTION_TO_COMPONENTS</a>, <a href="NMAction.html#GENERATED_ID_PREFIX">GENERATED_ID_PREFIX</a>, <a href="NMAction.html#GROUP">GROUP</a>, <a href="NMAction.html#ID">ID</a>, <a href="NMAction.html#LARGE_ICON">LARGE_ICON</a>, <a href="NMAction.html#MENU_SHORTCUT_MASK">MENU_SHORTCUT_MASK</a>, <a href="NMAction.html#TINY_ICON">TINY_ICON</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,int)">NMTriStateAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int mnemonic)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.String)">NMTriStateAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int mnemonic,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke)">NMTriStateAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String)">NMTriStateAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.actions.ActionsVisitor)">accept</a><wbr/>(<a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts ActionsVisitor using Visitor design pattern.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionEvent.html" title="class or interface in java.awt.event">ActionEvent</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Executes given action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NMTriStateAction.ACTION_STATE.html" title="enum class in com.nomagic.actions">NMTriStateAction.ACTION_STATE</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getState()">getState</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMixedIconSupplier(java.util.function.Supplier)">setMixedIconSupplier</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a>&gt; mixedIconSupplier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSelectedIconSupplier(java.util.function.Supplier)">setSelectedIconSupplier</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a>&gt; selectedIconSupplier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setState(com.nomagic.actions.NMTriStateAction.ACTION_STATE)">setState</a><wbr/>(<a href="NMTriStateAction.ACTION_STATE.html" title="enum class in com.nomagic.actions">NMTriStateAction.ACTION_STATE</a> state)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets action String state.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUnselectedIconSupplier(java.util.function.Supplier)">setUnselectedIconSupplier</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a>&gt; unselectedIconSupplier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.BaseNMStateAction">Methods inherited from class com.nomagic.actions.<a href="BaseNMStateAction.html" title="class in com.nomagic.actions">BaseNMStateAction</a></h3>
<code><a href="BaseNMStateAction.html#isGrouped()">isGrouped</a>, <a href="BaseNMStateAction.html#setGrouped(boolean)">setGrouped</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.NMAction">Methods inherited from class com.nomagic.actions.<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="NMAction.html#addAction(com.nomagic.actions.NMAction)">addAction</a>, <a href="NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="NMAction.html#addShortcut(javax.swing.KeyStroke)">addShortcut</a>, <a href="NMAction.html#addShotcut(javax.swing.KeyStroke)">addShotcut</a>, <a href="NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)">addWeakPropertyChangeListener</a>, <a href="NMAction.html#clone()">clone</a>, <a href="NMAction.html#compareTo(java.lang.Object)">compareTo</a>, <a href="NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)">createMenuItem</a>, <a href="NMAction.html#equals(java.lang.Object)">equals</a>, <a href="NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="NMAction.html#forEach(java.util.function.Consumer)">forEach</a>, <a href="NMAction.html#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a>, <a href="NMAction.html#getActions()">getActions</a>, <a href="NMAction.html#getCommandKey()">getCommandKey</a>, <a href="NMAction.html#getDescription()">getDescription</a>, <a href="NMAction.html#getGroup()">getGroup</a>, <a href="NMAction.html#getIcon()">getIcon</a>, <a href="NMAction.html#getID()">getID</a>, <a href="NMAction.html#getLargeIcon()">getLargeIcon</a>, <a href="NMAction.html#getLargeOrSmallIcon()">getLargeOrSmallIcon</a>, <a href="NMAction.html#getMenuShortcutMaskAsString()">getMenuShortcutMaskAsString</a>, <a href="NMAction.html#getMnemonicKey()">getMnemonicKey</a>, <a href="NMAction.html#getName()">getName</a>, <a href="NMAction.html#getPropertyChangeListeners()">getPropertyChangeListeners</a>, <a href="NMAction.html#getShortcuts()">getShortcuts</a>, <a href="NMAction.html#getSmallIcon()">getSmallIcon</a>, <a href="NMAction.html#getSmallOrLargeIcon()">getSmallOrLargeIcon</a>, <a href="NMAction.html#getTinyIcon()">getTinyIcon</a>, <a href="NMAction.html#hashCode()">hashCode</a>, <a href="NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)">hasMenuShortcutMask</a>, <a href="NMAction.html#isIDGenerated()">isIDGenerated</a>, <a href="NMAction.html#removeAction(com.nomagic.actions.NMAction)">removeAction</a>, <a href="NMAction.html#removeIf(java.util.function.Predicate)">removeIf</a>, <a href="NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="NMAction.html#removeShortcut(javax.swing.KeyStroke)">removeShortcut</a>, <a href="NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)">removeWeakPropertyChangeListener</a>, <a href="NMAction.html#setActions(java.util.List)">setActions</a>, <a href="NMAction.html#setDescription(java.lang.String)">setDescription</a>, <a href="NMAction.html#setGroup(java.lang.String)">setGroup</a>, <a href="NMAction.html#setIcon(javax.swing.Icon)">setIcon</a>, <a href="NMAction.html#setLargeIcon(javax.swing.Icon)">setLargeIcon</a>, <a href="NMAction.html#setMnemonicKey(int)">setMnemonicKey</a>, <a href="NMAction.html#setName(java.lang.String)">setName</a>, <a href="NMAction.html#setShortcuts(java.util.List)">setShortcuts</a>, <a href="NMAction.html#setSmallIcon(javax.swing.Icon)">setSmallIcon</a>, <a href="NMAction.html#setTinyIcon(javax.swing.Icon)">setTinyIcon</a>, <a href="NMAction.html#shallowClone()">shallowClone</a>, <a href="NMAction.html#toString()">toString</a>, <a href="NMAction.html#updateState()">updateState</a></code></div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="TRI_STATE">
<h3>TRI_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRI_STATE</span></div>
<div class="block">The state property. Value of this property is an enumeration</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.NMTriStateAction.TRI_STATE">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String)">
<h3>NMTriStateAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NMTriStateAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,int,java.lang.String)">
<h3>NMTriStateAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NMTriStateAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int mnemonic,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,javax.swing.KeyStroke)">
<h3>NMTriStateAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NMTriStateAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,int)">
<h3>NMTriStateAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NMTriStateAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int mnemonic)</span></div>
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
<section class="detail" id="setState(com.nomagic.actions.NMTriStateAction.ACTION_STATE)">
<h3>setState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setState</span><wbr/><span class="parameters">(<a href="NMTriStateAction.ACTION_STATE.html" title="enum class in com.nomagic.actions">NMTriStateAction.ACTION_STATE</a> state)</span></div>
<div class="block">Sets action String state.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>state</code> - new state of action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getState()">
<h3>getState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="NMTriStateAction.ACTION_STATE.html" title="enum class in com.nomagic.actions">NMTriStateAction.ACTION_STATE</a></span> <span class="element-name">getState</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the state of the action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMixedIconSupplier(java.util.function.Supplier)">
<h3>setMixedIconSupplier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMixedIconSupplier</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a>&gt; mixedIconSupplier)</span></div>
</section>
</li>
<li>
<section class="detail" id="setSelectedIconSupplier(java.util.function.Supplier)">
<h3>setSelectedIconSupplier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectedIconSupplier</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a>&gt; selectedIconSupplier)</span></div>
</section>
</li>
<li>
<section class="detail" id="setUnselectedIconSupplier(java.util.function.Supplier)">
<h3>setUnselectedIconSupplier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUnselectedIconSupplier</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a>&gt; unselectedIconSupplier)</span></div>
</section>
</li>
<li>
<section class="detail" id="actionPerformed(java.awt.event.ActionEvent)">
<h3>actionPerformed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">actionPerformed</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionEvent.html" title="class or interface in java.awt.event">ActionEvent</a> e)</span></div>
<div class="block">Executes given action.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html#actionPerformed(java.awt.event.ActionEvent)" title="class or interface in java.awt.event">actionPerformed</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="NMAction.html#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>e</code> - event caused execution.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.actions.ActionsVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a> visitor)</span></div>
<div class="block">Accepts ActionsVisitor using Visitor design pattern.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="NMAction.html#accept(com.nomagic.actions.ActionsVisitor)">accept</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - visitor to accept.</dd>
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
