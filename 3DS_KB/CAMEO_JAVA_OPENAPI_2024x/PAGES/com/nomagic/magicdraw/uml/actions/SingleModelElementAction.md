# JAVA OPENAPI: SingleModelElementAction (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml/actions/SingleModelElementAction.html
- source_path: `com/nomagic/magicdraw/uml/actions/SingleModelElementAction.html`
- source_sha256: `e5b319d8583085317178df29c2606eccf9bd03fa4dd2338a325046d18b39ca9b`
- captured_utc: `2026-07-14T16:52:10.570859+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.actions](package-summary.html)

## Class SingleModelElementAction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[javax.swing.AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
[com.nomagic.actions.NMAction](../../../actions/NMAction.html)
[com.nomagic.magicdraw.actions.MDAction](../../actions/MDAction.html)
com.nomagic.magicdraw.uml.actions.SingleModelElementAction

All Implemented Interfaces:
`com.nomagic.magicdraw.actions.ShortcutSchemaAction`, `[ISingleModelElementAction](ISingleModelElementAction.html)`, `[ActionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`, `[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)`

Direct Known Subclasses:
`[MultipleModelElementAction](MultipleModelElementAction.html)`

@OpenApiAllpublic classSingleModelElementAction
extends [MDAction](../../actions/MDAction.html)
implements [ISingleModelElementAction](ISingleModelElementAction.html)

Base class for actions to work with one model element selection.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.uml.actions.SingleModelElementAction)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.actions.[NMAction](../../../actions/NMAction.html)
`[ACTION_SHORTCUTS](../../../actions/NMAction.html#ACTION_SHORTCUTS), [BELONGS_TO_SEPARATE_GROUP_IN_UI](../../../actions/NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI), [DO_NO_SHOW_ACTION_NAME_IN_UI](../../../actions/NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI), [DO_NOT_REGISTER_ACTION_TO_COMPONENTS](../../../actions/NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS), [GENERATED_ID_PREFIX](../../../actions/NMAction.html#GENERATED_ID_PREFIX), [GROUP](../../../actions/NMAction.html#GROUP), [ID](../../../actions/NMAction.html#ID), [LARGE_ICON](../../../actions/NMAction.html#LARGE_ICON), [MENU_SHORTCUT_MASK](../../../actions/NMAction.html#MENU_SHORTCUT_MASK), [TINY_ICON](../../../actions/NMAction.html#TINY_ICON)`
Fields inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[changeSupport](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#changeSupport), [enabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#enabled)`
Fields inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[ACCELERATOR_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACCELERATOR_KEY), [ACTION_COMMAND_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACTION_COMMAND_KEY), [DEFAULT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DEFAULT), [DISPLAYED_MNEMONIC_INDEX_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DISPLAYED_MNEMONIC_INDEX_KEY), [LARGE_ICON_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LARGE_ICON_KEY), [LONG_DESCRIPTION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LONG_DESCRIPTION), [MNEMONIC_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#MNEMONIC_KEY), [NAME](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#NAME), [SELECTED_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SELECTED_KEY), [SHORT_DESCRIPTION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SHORT_DESCRIPTION), [SMALL_ICON](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SMALL_ICON)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SingleModelElementAction](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionName,
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`
Constructor for ModelElementAction.
`[SingleModelElementAction](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionName,
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 boolean useSchema)`
Constructor for ModelElementAction.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElement](#getElement())()`
Returns data from selected node.
`[ModelElementProvider](../ModelElementProvider.html)`
`[getProvider](#getProvider())()`
Gets the provider.
`void`
`[setProvider](#setProvider(com.nomagic.magicdraw.uml.ModelElementProvider))([ModelElementProvider](../ModelElementProvider.html) provider)`
Sets the provider.
Methods inherited from class com.nomagic.magicdraw.actions.[MDAction](../../actions/MDAction.html)
`[actionPerformed](../../actions/MDAction.html#actionPerformed(java.awt.event.ActionEvent)), [isUseShortcutSchema](../../actions/MDAction.html#isUseShortcutSchema()), [updateState](../../actions/MDAction.html#updateState())`
Methods inherited from class com.nomagic.actions.[NMAction](../../../actions/NMAction.html)
`[accept](../../../actions/NMAction.html#accept(com.nomagic.actions.ActionsVisitor)), [addAction](../../../actions/NMAction.html#addAction(com.nomagic.actions.NMAction)), [addPropertyChangeListener](../../../actions/NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addShortcut](../../../actions/NMAction.html#addShortcut(javax.swing.KeyStroke)), [addShotcut](../../../actions/NMAction.html#addShotcut(javax.swing.KeyStroke)), [addWeakPropertyChangeListener](../../../actions/NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [clone](../../../actions/NMAction.html#clone()), [compareTo](../../../actions/NMAction.html#compareTo(java.lang.Object)), [createMenuItem](../../../actions/NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)), [equals](../../../actions/NMAction.html#equals(java.lang.Object)), [firePropertyChange](../../../actions/NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [forEach](../../../actions/NMAction.html#forEach(java.util.function.Consumer)), [forEachIncludingSelf](../../../actions/NMAction.html#forEachIncludingSelf(java.util.function.Consumer)), [getActions](../../../actions/NMAction.html#getActions()), [getCommandKey](../../../actions/NMAction.html#getCommandKey()), [getDescription](../../../actions/NMAction.html#getDescription()), [getGroup](../../../actions/NMAction.html#getGroup()), [getIcon](../../../actions/NMAction.html#getIcon()), [getID](../../../actions/NMAction.html#getID()), [getLargeIcon](../../../actions/NMAction.html#getLargeIcon()), [getLargeOrSmallIcon](../../../actions/NMAction.html#getLargeOrSmallIcon()), [getMenuShortcutMaskAsString](../../../actions/NMAction.html#getMenuShortcutMaskAsString()), [getMnemonicKey](../../../actions/NMAction.html#getMnemonicKey()), [getName](../../../actions/NMAction.html#getName()), [getPropertyChangeListeners](../../../actions/NMAction.html#getPropertyChangeListeners()), [getShortcuts](../../../actions/NMAction.html#getShortcuts()), [getSmallIcon](../../../actions/NMAction.html#getSmallIcon()), [getSmallOrLargeIcon](../../../actions/NMAction.html#getSmallOrLargeIcon()), [getTinyIcon](../../../actions/NMAction.html#getTinyIcon()), [hashCode](../../../actions/NMAction.html#hashCode()), [hasMenuShortcutMask](../../../actions/NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)), [isIDGenerated](../../../actions/NMAction.html#isIDGenerated()), [removeAction](../../../actions/NMAction.html#removeAction(com.nomagic.actions.NMAction)), [removeIf](../../../actions/NMAction.html#removeIf(java.util.function.Predicate)), [removePropertyChangeListener](../../../actions/NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [removeShortcut](../../../actions/NMAction.html#removeShortcut(javax.swing.KeyStroke)), [removeWeakPropertyChangeListener](../../../actions/NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [setActions](../../../actions/NMAction.html#setActions(java.util.List)), [setDescription](../../../actions/NMAction.html#setDescription(java.lang.String)), [setGroup](../../../actions/NMAction.html#setGroup(java.lang.String)), [setIcon](../../../actions/NMAction.html#setIcon(javax.swing.Icon)), [setLargeIcon](../../../actions/NMAction.html#setLargeIcon(javax.swing.Icon)), [setMnemonicKey](../../../actions/NMAction.html#setMnemonicKey(int)), [setName](../../../actions/NMAction.html#setName(java.lang.String)), [setShortcuts](../../../actions/NMAction.html#setShortcuts(java.util.List)), [setSmallIcon](../../../actions/NMAction.html#setSmallIcon(javax.swing.Icon)), [setTinyIcon](../../../actions/NMAction.html#setTinyIcon(javax.swing.Icon)), [shallowClone](../../../actions/NMAction.html#shallowClone()), [toString](../../../actions/NMAction.html#toString())`
Methods inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[getKeys](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()), [getValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)), [isEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()), [putValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)), [setEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[accept](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SingleModelElementAction
public SingleModelElementAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionName,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
Constructor for ModelElementAction.
Parameters:
`actionID` - action id
`actionName` - action name
`stroke` - stroke
`group` - group
SingleModelElementAction
public SingleModelElementAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionName,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 boolean useSchema)
Constructor for ModelElementAction.
Parameters:
`actionID` - action id
`actionName` - action name
`stroke` - stroke
`group` - group
`useSchema` - use shortcuts schema
 ============ METHOD DETAIL ========== 
Method Details
getElement
@CheckForNullprotected [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElement()
Returns data from selected node.
 If there are no selected nodes, or more than one selected node returns null.
Returns:
element or null
getProvider
public [ModelElementProvider](../ModelElementProvider.html) getProvider()
Gets the provider.
Specified by:
`[getProvider](ISingleModelElementAction.html#getProvider())` in interface `[ISingleModelElementAction](ISingleModelElementAction.html)`
Returns:
Returns a ModelElementProvider
setProvider
public void setProvider([ModelElementProvider](../ModelElementProvider.html) provider)
Sets the provider.
Specified by:
`[setProvider](ISingleModelElementAction.html#setProvider(com.nomagic.magicdraw.uml.ModelElementProvider))` in interface `[ISingleModelElementAction](ISingleModelElementAction.html)`
Parameters:
`provider` - The provider to set

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.actions</a></div>
<h1 class="title" title="Class SingleModelElementAction">Class SingleModelElementAction</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">javax.swing.AbstractAction</a>
<div class="inheritance"><a href="../../../actions/NMAction.html" title="class in com.nomagic.actions">com.nomagic.actions.NMAction</a>
<div class="inheritance"><a href="../../actions/MDAction.html" title="class in com.nomagic.magicdraw.actions">com.nomagic.magicdraw.actions.MDAction</a>
<div class="inheritance">com.nomagic.magicdraw.uml.actions.SingleModelElementAction</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.actions.ShortcutSchemaAction</code>, <code><a href="ISingleModelElementAction.html" title="interface in com.nomagic.magicdraw.uml.actions">ISingleModelElementAction</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="MultipleModelElementAction.html" title="class in com.nomagic.magicdraw.uml.actions">MultipleModelElementAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SingleModelElementAction</span>
<span class="extends-implements">extends <a href="../../actions/MDAction.html" title="class in com.nomagic.magicdraw.actions">MDAction</a>
implements <a href="ISingleModelElementAction.html" title="interface in com.nomagic.magicdraw.uml.actions">ISingleModelElementAction</a></span></div>
<div class="block">Base class for actions to work with one model element selection.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.uml.actions.SingleModelElementAction">Serialized Form</a></li>
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
<h3 id="fields-inherited-from-class-com.nomagic.actions.NMAction">Fields inherited from class com.nomagic.actions.<a href="../../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="../../../actions/NMAction.html#ACTION_SHORTCUTS">ACTION_SHORTCUTS</a>, <a href="../../../actions/NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI">BELONGS_TO_SEPARATE_GROUP_IN_UI</a>, <a href="../../../actions/NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI">DO_NO_SHOW_ACTION_NAME_IN_UI</a>, <a href="../../../actions/NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS">DO_NOT_REGISTER_ACTION_TO_COMPONENTS</a>, <a href="../../../actions/NMAction.html#GENERATED_ID_PREFIX">GENERATED_ID_PREFIX</a>, <a href="../../../actions/NMAction.html#GROUP">GROUP</a>, <a href="../../../actions/NMAction.html#ID">ID</a>, <a href="../../../actions/NMAction.html#LARGE_ICON">LARGE_ICON</a>, <a href="../../../actions/NMAction.html#MENU_SHORTCUT_MASK">MENU_SHORTCUT_MASK</a>, <a href="../../../actions/NMAction.html#TINY_ICON">TINY_ICON</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String)">SingleModelElementAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor for ModelElementAction.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String,boolean)">SingleModelElementAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 boolean useSchema)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor for ModelElementAction.</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns data from selected node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProvider()">getProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the provider.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProvider(com.nomagic.magicdraw.uml.ModelElementProvider)">setProvider</a><wbr/>(<a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a> provider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the provider.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.actions.MDAction">Methods inherited from class com.nomagic.magicdraw.actions.<a href="../../actions/MDAction.html" title="class in com.nomagic.magicdraw.actions">MDAction</a></h3>
<code><a href="../../actions/MDAction.html#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a>, <a href="../../actions/MDAction.html#isUseShortcutSchema()">isUseShortcutSchema</a>, <a href="../../actions/MDAction.html#updateState()">updateState</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.NMAction">Methods inherited from class com.nomagic.actions.<a href="../../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="../../../actions/NMAction.html#accept(com.nomagic.actions.ActionsVisitor)">accept</a>, <a href="../../../actions/NMAction.html#addAction(com.nomagic.actions.NMAction)">addAction</a>, <a href="../../../actions/NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../actions/NMAction.html#addShortcut(javax.swing.KeyStroke)">addShortcut</a>, <a href="../../../actions/NMAction.html#addShotcut(javax.swing.KeyStroke)">addShotcut</a>, <a href="../../../actions/NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)">addWeakPropertyChangeListener</a>, <a href="../../../actions/NMAction.html#clone()">clone</a>, <a href="../../../actions/NMAction.html#compareTo(java.lang.Object)">compareTo</a>, <a href="../../../actions/NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)">createMenuItem</a>, <a href="../../../actions/NMAction.html#equals(java.lang.Object)">equals</a>, <a href="../../../actions/NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../actions/NMAction.html#forEach(java.util.function.Consumer)">forEach</a>, <a href="../../../actions/NMAction.html#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a>, <a href="../../../actions/NMAction.html#getActions()">getActions</a>, <a href="../../../actions/NMAction.html#getCommandKey()">getCommandKey</a>, <a href="../../../actions/NMAction.html#getDescription()">getDescription</a>, <a href="../../../actions/NMAction.html#getGroup()">getGroup</a>, <a href="../../../actions/NMAction.html#getIcon()">getIcon</a>, <a href="../../../actions/NMAction.html#getID()">getID</a>, <a href="../../../actions/NMAction.html#getLargeIcon()">getLargeIcon</a>, <a href="../../../actions/NMAction.html#getLargeOrSmallIcon()">getLargeOrSmallIcon</a>, <a href="../../../actions/NMAction.html#getMenuShortcutMaskAsString()">getMenuShortcutMaskAsString</a>, <a href="../../../actions/NMAction.html#getMnemonicKey()">getMnemonicKey</a>, <a href="../../../actions/NMAction.html#getName()">getName</a>, <a href="../../../actions/NMAction.html#getPropertyChangeListeners()">getPropertyChangeListeners</a>, <a href="../../../actions/NMAction.html#getShortcuts()">getShortcuts</a>, <a href="../../../actions/NMAction.html#getSmallIcon()">getSmallIcon</a>, <a href="../../../actions/NMAction.html#getSmallOrLargeIcon()">getSmallOrLargeIcon</a>, <a href="../../../actions/NMAction.html#getTinyIcon()">getTinyIcon</a>, <a href="../../../actions/NMAction.html#hashCode()">hashCode</a>, <a href="../../../actions/NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)">hasMenuShortcutMask</a>, <a href="../../../actions/NMAction.html#isIDGenerated()">isIDGenerated</a>, <a href="../../../actions/NMAction.html#removeAction(com.nomagic.actions.NMAction)">removeAction</a>, <a href="../../../actions/NMAction.html#removeIf(java.util.function.Predicate)">removeIf</a>, <a href="../../../actions/NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../actions/NMAction.html#removeShortcut(javax.swing.KeyStroke)">removeShortcut</a>, <a href="../../../actions/NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)">removeWeakPropertyChangeListener</a>, <a href="../../../actions/NMAction.html#setActions(java.util.List)">setActions</a>, <a href="../../../actions/NMAction.html#setDescription(java.lang.String)">setDescription</a>, <a href="../../../actions/NMAction.html#setGroup(java.lang.String)">setGroup</a>, <a href="../../../actions/NMAction.html#setIcon(javax.swing.Icon)">setIcon</a>, <a href="../../../actions/NMAction.html#setLargeIcon(javax.swing.Icon)">setLargeIcon</a>, <a href="../../../actions/NMAction.html#setMnemonicKey(int)">setMnemonicKey</a>, <a href="../../../actions/NMAction.html#setName(java.lang.String)">setName</a>, <a href="../../../actions/NMAction.html#setShortcuts(java.util.List)">setShortcuts</a>, <a href="../../../actions/NMAction.html#setSmallIcon(javax.swing.Icon)">setSmallIcon</a>, <a href="../../../actions/NMAction.html#setTinyIcon(javax.swing.Icon)">setTinyIcon</a>, <a href="../../../actions/NMAction.html#shallowClone()">shallowClone</a>, <a href="../../../actions/NMAction.html#toString()">toString</a></code></div>
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
<h3>SingleModelElementAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SingleModelElementAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Constructor for ModelElementAction.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionID</code> - action id</dd>
<dd><code>actionName</code> - action name</dd>
<dd><code>stroke</code> - stroke</dd>
<dd><code>group</code> - group</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String,boolean)">
<h3>SingleModelElementAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SingleModelElementAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 boolean useSchema)</span></div>
<div class="block">Constructor for ModelElementAction.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionID</code> - action id</dd>
<dd><code>actionName</code> - action name</dd>
<dd><code>stroke</code> - stroke</dd>
<dd><code>group</code> - group</dd>
<dd><code>useSchema</code> - use shortcuts schema</dd>
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
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElement</span>()</div>
<div class="block">Returns data from selected node.
 If there are no selected nodes, or more than one selected node returns null.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProvider()">
<h3>getProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></span> <span class="element-name">getProvider</span>()</div>
<div class="block">Gets the provider.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ISingleModelElementAction.html#getProvider()">getProvider</a></code> in interface <code><a href="ISingleModelElementAction.html" title="interface in com.nomagic.magicdraw.uml.actions">ISingleModelElementAction</a></code></dd>
<dt>Returns:</dt>
<dd>Returns a ModelElementProvider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProvider(com.nomagic.magicdraw.uml.ModelElementProvider)">
<h3>setProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProvider</span><wbr/><span class="parameters">(<a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a> provider)</span></div>
<div class="block">Sets the provider.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ISingleModelElementAction.html#setProvider(com.nomagic.magicdraw.uml.ModelElementProvider)">setProvider</a></code> in interface <code><a href="ISingleModelElementAction.html" title="interface in com.nomagic.magicdraw.uml.actions">ISingleModelElementAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>provider</code> - The provider to set</dd>
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
