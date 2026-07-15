# JAVA OPENAPI: ColorChooseAction (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/actions/ColorChooseAction.html
- source_path: `com/nomagic/actions/ColorChooseAction.html`
- source_sha256: `d7c81cc00c22bf20bfb60616b0afde786ed4acca04a2ac53a2bf7f1e5a319a24`
- captured_utc: `2026-07-14T16:57:41.799353+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.actions](package-summary.html)

## Class ColorChooseAction

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[javax.swing.AbstractAction](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html)
[com.nomagic.actions.NMAction](NMAction.html)
com.nomagic.actions.ColorChooseAction

All Implemented Interfaces:
`[ActionListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)`, `[Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html)`

@OpenApipublic classColorChooseAction
extends [NMAction](NMAction.html)

Action for choosing a color.

See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.actions.ColorChooseAction)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.actions.[NMAction](NMAction.html)
`[ACTION_SHORTCUTS](NMAction.html#ACTION_SHORTCUTS), [BELONGS_TO_SEPARATE_GROUP_IN_UI](NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI), [DO_NO_SHOW_ACTION_NAME_IN_UI](NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI), [DO_NOT_REGISTER_ACTION_TO_COMPONENTS](NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS), [GENERATED_ID_PREFIX](NMAction.html#GENERATED_ID_PREFIX), [GROUP](NMAction.html#GROUP), [ID](NMAction.html#ID), [LARGE_ICON](NMAction.html#LARGE_ICON), [MENU_SHORTCUT_MASK](NMAction.html#MENU_SHORTCUT_MASK), [TINY_ICON](NMAction.html#TINY_ICON)`
Fields inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[changeSupport](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#changeSupport), [enabled](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#enabled)`
Fields inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html)
`[ACCELERATOR_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#ACCELERATOR_KEY), [ACTION_COMMAND_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#ACTION_COMMAND_KEY), [DEFAULT](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#DEFAULT), [DISPLAYED_MNEMONIC_INDEX_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#DISPLAYED_MNEMONIC_INDEX_KEY), [LARGE_ICON_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#LARGE_ICON_KEY), [LONG_DESCRIPTION](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#LONG_DESCRIPTION), [MNEMONIC_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#MNEMONIC_KEY), [NAME](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#NAME), [SELECTED_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SELECTED_KEY), [SHORT_DESCRIPTION](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SHORT_DESCRIPTION), [SMALL_ICON](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SMALL_ICON)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ColorChooseAction](#%3Cinit%3E(java.lang.String,java.lang.String,boolean,java.awt.Color%5B%5D))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) moreLabel,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) noFillLabel,
 boolean noFillAvailable,
 [Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html)[] recentColors)`
Constructs new color action.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[actionPerformed](#actionPerformed(java.awt.event.ActionEvent))([ActionEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionEvent.html) e)`
Shows ColorPallet in JPopupMenu when this action is performed.
`[Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html)`
`[getColor](#getColor())()`
Returns color selected by this action.
Methods inherited from class com.nomagic.actions.[NMAction](NMAction.html)
`[accept](NMAction.html#accept(com.nomagic.actions.ActionsVisitor)), [addAction](NMAction.html#addAction(com.nomagic.actions.NMAction)), [addPropertyChangeListener](NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addShortcut](NMAction.html#addShortcut(javax.swing.KeyStroke)), [addShotcut](NMAction.html#addShotcut(javax.swing.KeyStroke)), [addWeakPropertyChangeListener](NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [clone](NMAction.html#clone()), [compareTo](NMAction.html#compareTo(java.lang.Object)), [createMenuItem](NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)), [equals](NMAction.html#equals(java.lang.Object)), [firePropertyChange](NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [forEach](NMAction.html#forEach(java.util.function.Consumer)), [forEachIncludingSelf](NMAction.html#forEachIncludingSelf(java.util.function.Consumer)), [getActions](NMAction.html#getActions()), [getCommandKey](NMAction.html#getCommandKey()), [getDescription](NMAction.html#getDescription()), [getGroup](NMAction.html#getGroup()), [getIcon](NMAction.html#getIcon()), [getID](NMAction.html#getID()), [getLargeIcon](NMAction.html#getLargeIcon()), [getLargeOrSmallIcon](NMAction.html#getLargeOrSmallIcon()), [getMenuShortcutMaskAsString](NMAction.html#getMenuShortcutMaskAsString()), [getMnemonicKey](NMAction.html#getMnemonicKey()), [getName](NMAction.html#getName()), [getPropertyChangeListeners](NMAction.html#getPropertyChangeListeners()), [getShortcuts](NMAction.html#getShortcuts()), [getSmallIcon](NMAction.html#getSmallIcon()), [getSmallOrLargeIcon](NMAction.html#getSmallOrLargeIcon()), [getTinyIcon](NMAction.html#getTinyIcon()), [hashCode](NMAction.html#hashCode()), [hasMenuShortcutMask](NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)), [isIDGenerated](NMAction.html#isIDGenerated()), [removeAction](NMAction.html#removeAction(com.nomagic.actions.NMAction)), [removeIf](NMAction.html#removeIf(java.util.function.Predicate)), [removePropertyChangeListener](NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [removeShortcut](NMAction.html#removeShortcut(javax.swing.KeyStroke)), [removeWeakPropertyChangeListener](NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [setActions](NMAction.html#setActions(java.util.List)), [setDescription](NMAction.html#setDescription(java.lang.String)), [setGroup](NMAction.html#setGroup(java.lang.String)), [setIcon](NMAction.html#setIcon(javax.swing.Icon)), [setLargeIcon](NMAction.html#setLargeIcon(javax.swing.Icon)), [setMnemonicKey](NMAction.html#setMnemonicKey(int)), [setName](NMAction.html#setName(java.lang.String)), [setShortcuts](NMAction.html#setShortcuts(java.util.List)), [setSmallIcon](NMAction.html#setSmallIcon(javax.swing.Icon)), [setTinyIcon](NMAction.html#setTinyIcon(javax.swing.Icon)), [shallowClone](NMAction.html#shallowClone()), [toString](NMAction.html#toString()), [updateState](NMAction.html#updateState())`
Methods inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[getKeys](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()), [getValue](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)), [isEnabled](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()), [putValue](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)), [setEnabled](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html)
`[accept](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ColorChooseAction
@OpenApipublic ColorChooseAction([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) moreLabel,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) noFillLabel,
 boolean noFillAvailable,
 [Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html)[] recentColors)
Constructs new color action.
Parameters:
`moreLabel` - the text of more label.
`noFillLabel` - the text of no fill label.
`noFillAvailable` - no fill available or not?
 ============ METHOD DETAIL ========== 
Method Details
actionPerformed
@OpenApipublic void actionPerformed([ActionEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionEvent.html) e)
Shows ColorPallet in JPopupMenu when this action is performed.
 For showing popup event source parent is used.
Specified by:
`[actionPerformed](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionListener.html#actionPerformed(java.awt.event.ActionEvent))` in interface `[ActionListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionListener.html)`
Specified by:
`[actionPerformed](NMAction.html#actionPerformed(java.awt.event.ActionEvent))` in class `[NMAction](NMAction.html)`
Parameters:
`e` - an event caused invocation
getColor
@OpenApipublic [Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html) getColor()
Returns color selected by this action.
Returns:
the selected color.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.actions</a></div>
<h1 class="title" title="Class ColorChooseAction">Class ColorChooseAction</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">javax.swing.AbstractAction</a>
<div class="inheritance"><a href="NMAction.html" title="class in com.nomagic.actions">com.nomagic.actions.NMAction</a>
<div class="inheritance">com.nomagic.actions.ColorChooseAction</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ColorChooseAction</span>
<span class="extends-implements">extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></span></div>
<div class="block">Action for choosing a color.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../serialized-form.html#com.nomagic.actions.ColorChooseAction">Serialized Form</a></li>
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
<h3 id="fields-inherited-from-class-com.nomagic.actions.NMAction">Fields inherited from class com.nomagic.actions.<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="NMAction.html#ACTION_SHORTCUTS">ACTION_SHORTCUTS</a>, <a href="NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI">BELONGS_TO_SEPARATE_GROUP_IN_UI</a>, <a href="NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI">DO_NO_SHOW_ACTION_NAME_IN_UI</a>, <a href="NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS">DO_NOT_REGISTER_ACTION_TO_COMPONENTS</a>, <a href="NMAction.html#GENERATED_ID_PREFIX">GENERATED_ID_PREFIX</a>, <a href="NMAction.html#GROUP">GROUP</a>, <a href="NMAction.html#ID">ID</a>, <a href="NMAction.html#LARGE_ICON">LARGE_ICON</a>, <a href="NMAction.html#MENU_SHORTCUT_MASK">MENU_SHORTCUT_MASK</a>, <a href="NMAction.html#TINY_ICON">TINY_ICON</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.AbstractAction">Fields inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">AbstractAction</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#changeSupport" title="class or interface in javax.swing">changeSupport</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#enabled" title="class or interface in javax.swing">enabled</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.Action">Fields inherited from interface javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#ACCELERATOR_KEY" title="class or interface in javax.swing">ACCELERATOR_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#ACTION_COMMAND_KEY" title="class or interface in javax.swing">ACTION_COMMAND_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#DEFAULT" title="class or interface in javax.swing">DEFAULT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#DISPLAYED_MNEMONIC_INDEX_KEY" title="class or interface in javax.swing">DISPLAYED_MNEMONIC_INDEX_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#LARGE_ICON_KEY" title="class or interface in javax.swing">LARGE_ICON_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#LONG_DESCRIPTION" title="class or interface in javax.swing">LONG_DESCRIPTION</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#MNEMONIC_KEY" title="class or interface in javax.swing">MNEMONIC_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#NAME" title="class or interface in javax.swing">NAME</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SELECTED_KEY" title="class or interface in javax.swing">SELECTED_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SHORT_DESCRIPTION" title="class or interface in javax.swing">SHORT_DESCRIPTION</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SMALL_ICON" title="class or interface in javax.swing">SMALL_ICON</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,boolean,java.awt.Color%5B%5D)">ColorChooseAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> moreLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noFillLabel,
 boolean noFillAvailable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a>[] recentColors)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs new color action.</div>
</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionEvent.html" title="class or interface in java.awt.event">ActionEvent</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows ColorPallet in JPopupMenu when this action is performed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColor()">getColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns color selected by this action.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.NMAction">Methods inherited from class com.nomagic.actions.<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="NMAction.html#accept(com.nomagic.actions.ActionsVisitor)">accept</a>, <a href="NMAction.html#addAction(com.nomagic.actions.NMAction)">addAction</a>, <a href="NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="NMAction.html#addShortcut(javax.swing.KeyStroke)">addShortcut</a>, <a href="NMAction.html#addShotcut(javax.swing.KeyStroke)">addShotcut</a>, <a href="NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)">addWeakPropertyChangeListener</a>, <a href="NMAction.html#clone()">clone</a>, <a href="NMAction.html#compareTo(java.lang.Object)">compareTo</a>, <a href="NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)">createMenuItem</a>, <a href="NMAction.html#equals(java.lang.Object)">equals</a>, <a href="NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="NMAction.html#forEach(java.util.function.Consumer)">forEach</a>, <a href="NMAction.html#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a>, <a href="NMAction.html#getActions()">getActions</a>, <a href="NMAction.html#getCommandKey()">getCommandKey</a>, <a href="NMAction.html#getDescription()">getDescription</a>, <a href="NMAction.html#getGroup()">getGroup</a>, <a href="NMAction.html#getIcon()">getIcon</a>, <a href="NMAction.html#getID()">getID</a>, <a href="NMAction.html#getLargeIcon()">getLargeIcon</a>, <a href="NMAction.html#getLargeOrSmallIcon()">getLargeOrSmallIcon</a>, <a href="NMAction.html#getMenuShortcutMaskAsString()">getMenuShortcutMaskAsString</a>, <a href="NMAction.html#getMnemonicKey()">getMnemonicKey</a>, <a href="NMAction.html#getName()">getName</a>, <a href="NMAction.html#getPropertyChangeListeners()">getPropertyChangeListeners</a>, <a href="NMAction.html#getShortcuts()">getShortcuts</a>, <a href="NMAction.html#getSmallIcon()">getSmallIcon</a>, <a href="NMAction.html#getSmallOrLargeIcon()">getSmallOrLargeIcon</a>, <a href="NMAction.html#getTinyIcon()">getTinyIcon</a>, <a href="NMAction.html#hashCode()">hashCode</a>, <a href="NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)">hasMenuShortcutMask</a>, <a href="NMAction.html#isIDGenerated()">isIDGenerated</a>, <a href="NMAction.html#removeAction(com.nomagic.actions.NMAction)">removeAction</a>, <a href="NMAction.html#removeIf(java.util.function.Predicate)">removeIf</a>, <a href="NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="NMAction.html#removeShortcut(javax.swing.KeyStroke)">removeShortcut</a>, <a href="NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)">removeWeakPropertyChangeListener</a>, <a href="NMAction.html#setActions(java.util.List)">setActions</a>, <a href="NMAction.html#setDescription(java.lang.String)">setDescription</a>, <a href="NMAction.html#setGroup(java.lang.String)">setGroup</a>, <a href="NMAction.html#setIcon(javax.swing.Icon)">setIcon</a>, <a href="NMAction.html#setLargeIcon(javax.swing.Icon)">setLargeIcon</a>, <a href="NMAction.html#setMnemonicKey(int)">setMnemonicKey</a>, <a href="NMAction.html#setName(java.lang.String)">setName</a>, <a href="NMAction.html#setShortcuts(java.util.List)">setShortcuts</a>, <a href="NMAction.html#setSmallIcon(javax.swing.Icon)">setSmallIcon</a>, <a href="NMAction.html#setTinyIcon(javax.swing.Icon)">setTinyIcon</a>, <a href="NMAction.html#shallowClone()">shallowClone</a>, <a href="NMAction.html#toString()">toString</a>, <a href="NMAction.html#updateState()">updateState</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.AbstractAction">Methods inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">AbstractAction</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()" title="class or interface in javax.swing">getKeys</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)" title="class or interface in javax.swing">getValue</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()" title="class or interface in javax.swing">isEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)" title="class or interface in javax.swing">putValue</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean)" title="class or interface in javax.swing">setEnabled</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.Action">Methods inherited from interface javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object)" title="class or interface in javax.swing">accept</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,boolean,java.awt.Color[])">
<h3>ColorChooseAction</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">ColorChooseAction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> moreLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noFillLabel,
 boolean noFillAvailable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a>[] recentColors)</span></div>
<div class="block">Constructs new color action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>moreLabel</code> - the text of more label.</dd>
<dd><code>noFillLabel</code> - the text of no fill label.</dd>
<dd><code>noFillAvailable</code> - no fill available or not?</dd>
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
<section class="detail" id="actionPerformed(java.awt.event.ActionEvent)">
<h3>actionPerformed</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">actionPerformed</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionEvent.html" title="class or interface in java.awt.event">ActionEvent</a> e)</span></div>
<div class="block">Shows ColorPallet in JPopupMenu when this action is performed.
 For showing popup event source parent is used.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionListener.html#actionPerformed(java.awt.event.ActionEvent)" title="class or interface in java.awt.event">actionPerformed</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="NMAction.html#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>e</code> - an event caused invocation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColor()">
<h3>getColor</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">getColor</span>()</div>
<div class="block">Returns color selected by this action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the selected color.</dd>
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
