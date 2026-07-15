# JAVA OPENAPI: DiagramInnerToolbarConfiguration (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/actions/DiagramInnerToolbarConfiguration.html
- source_path: `com/nomagic/magicdraw/actions/DiagramInnerToolbarConfiguration.html`
- source_sha256: `56268df3ac33a7089ef5bee826742a375d87a3131754488b60f53f72d14cd393`
- captured_utc: `2026-07-14T16:45:07.605104+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.actions](package-summary.html)

## Class DiagramInnerToolbarConfiguration

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[javax.swing.AbstractAction](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html)
[com.nomagic.actions.NMAction](../../actions/NMAction.html)
[com.nomagic.actions.ActionsCategory](../../actions/ActionsCategory.html)
[com.nomagic.magicdraw.actions.MDActionsCategory](MDActionsCategory.html)
com.nomagic.magicdraw.actions.DiagramInnerToolbarConfiguration

All Implemented Interfaces:
`com.nomagic.magicdraw.actions.ShortcutSchemaAction`, `[ActionListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)`, `[Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html)`

@OpenApiAllpublic classDiagramInnerToolbarConfiguration
extends [MDActionsCategory](MDActionsCategory.html)

See Also:
[Serialized Form](../../../../serialized-form.html#com.nomagic.magicdraw.actions.DiagramInnerToolbarConfiguration)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.actions.[ActionsCategory](../../actions/ActionsCategory.html)
`[ACTIONS_PROPERTY](../../actions/ActionsCategory.html#ACTIONS_PROPERTY), [ADDED_ACTION_PROPERTY](../../actions/ActionsCategory.html#ADDED_ACTION_PROPERTY), [CHANGE_ACTIONS_PROPERTY](../../actions/ActionsCategory.html#CHANGE_ACTIONS_PROPERTY), [DISABLE_IF_EMPTY](../../actions/ActionsCategory.html#DISABLE_IF_EMPTY), [MAX_CATEGORY_ACTIONS](../../actions/ActionsCategory.html#MAX_CATEGORY_ACTIONS), [REMOVE_IF_EMPTY](../../actions/ActionsCategory.html#REMOVE_IF_EMPTY), [REMOVED_ACTION_PROPERTY](../../actions/ActionsCategory.html#REMOVED_ACTION_PROPERTY), [USE_AS_SEPARATOR_IN_UI](../../actions/ActionsCategory.html#USE_AS_SEPARATOR_IN_UI)`
Fields inherited from class com.nomagic.actions.[NMAction](../../actions/NMAction.html)
`[ACTION_SHORTCUTS](../../actions/NMAction.html#ACTION_SHORTCUTS), [BELONGS_TO_SEPARATE_GROUP_IN_UI](../../actions/NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI), [DO_NO_SHOW_ACTION_NAME_IN_UI](../../actions/NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI), [DO_NOT_REGISTER_ACTION_TO_COMPONENTS](../../actions/NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS), [GENERATED_ID_PREFIX](../../actions/NMAction.html#GENERATED_ID_PREFIX), [GROUP](../../actions/NMAction.html#GROUP), [ID](../../actions/NMAction.html#ID), [LARGE_ICON](../../actions/NMAction.html#LARGE_ICON), [MENU_SHORTCUT_MASK](../../actions/NMAction.html#MENU_SHORTCUT_MASK), [TINY_ICON](../../actions/NMAction.html#TINY_ICON)`
Fields inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[changeSupport](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#changeSupport), [enabled](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#enabled)`
Fields inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html)
`[ACCELERATOR_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#ACCELERATOR_KEY), [ACTION_COMMAND_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#ACTION_COMMAND_KEY), [DEFAULT](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#DEFAULT), [DISPLAYED_MNEMONIC_INDEX_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#DISPLAYED_MNEMONIC_INDEX_KEY), [LARGE_ICON_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#LARGE_ICON_KEY), [LONG_DESCRIPTION](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#LONG_DESCRIPTION), [MNEMONIC_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#MNEMONIC_KEY), [NAME](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#NAME), [SELECTED_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SELECTED_KEY), [SHORT_DESCRIPTION](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SHORT_DESCRIPTION), [SMALL_ICON](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SMALL_ICON)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramInnerToolbarConfiguration](#%3Cinit%3E(java.lang.String,javax.swing.Icon,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`

`[DiagramInnerToolbarConfiguration](#%3Cinit%3E(java.lang.String,javax.swing.Icon,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean expandedByDefault)`

`[DiagramInnerToolbarConfiguration](#%3Cinit%3E(java.lang.String,javax.swing.Icon,java.lang.String,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean expandedByDefault,
 boolean showText)`

`[DiagramInnerToolbarConfiguration](#%3Cinit%3E(javax.swing.Icon,java.lang.String))([Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`

`[DiagramInnerToolbarConfiguration](#%3Cinit%3E(javax.swing.Icon,java.lang.String,boolean))([Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean expandedByDefault)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[DiagramInnerToolbarConfiguration](DiagramInnerToolbarConfiguration.html)`
`[clone](#clone())()`
Clones the category.
`[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
`[getLargeIcon](#getLargeIcon())()`
Returns the large icon of the action.
`boolean`
`[isExpandByDefault](#isExpandByDefault())()`

`boolean`
`[isShowText](#isShowText())()`

`void`
`[setExpandByDefault](#setExpandByDefault(boolean))(boolean expandByDefault)`

`[DiagramInnerToolbarConfiguration](DiagramInnerToolbarConfiguration.html)`
`[shallowClone](#shallowClone())()`
Clones the category.
Methods inherited from class com.nomagic.magicdraw.actions.[MDActionsCategory](MDActionsCategory.html)
`[isUseShortcutSchema](MDActionsCategory.html#isUseShortcutSchema()), [updateState](MDActionsCategory.html#updateState())`
Methods inherited from class com.nomagic.actions.[ActionsCategory](../../actions/ActionsCategory.html)
`[accept](../../actions/ActionsCategory.html#accept(com.nomagic.actions.ActionsVisitor)), [actionPerformed](../../actions/ActionsCategory.html#actionPerformed(java.awt.event.ActionEvent)), [addAction](../../actions/ActionsCategory.html#addAction(com.nomagic.actions.NMAction)), [addAction](../../actions/ActionsCategory.html#addAction(com.nomagic.actions.NMAction,int)), [addActionNearTheGiven](../../actions/ActionsCategory.html#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction)), [addActions](../../actions/ActionsCategory.html#addActions(java.util.List)), [breakActions](../../actions/ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)), [breakActions](../../actions/ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean,int)), [breakActions](../../actions/ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List)), [breakeActions](../../actions/ActionsCategory.html#breakeActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)), [createSeparatorCategory](../../actions/ActionsCategory.html#createSeparatorCategory()), [forEach](../../actions/ActionsCategory.html#forEach(java.util.function.Consumer)), [forEachIncludingSelf](../../actions/ActionsCategory.html#forEachIncludingSelf(java.util.function.Consumer)), [getAction](../../actions/ActionsCategory.html#getAction(java.lang.String)), [getActions](../../actions/ActionsCategory.html#getActions()), [getActionsRecursively](../../actions/ActionsCategory.html#getActionsRecursively(boolean)), [getCategories](../../actions/ActionsCategory.html#getCategories()), [isDisplayHeader](../../actions/ActionsCategory.html#isDisplayHeader()), [isEmpty](../../actions/ActionsCategory.html#isEmpty()), [isNested](../../actions/ActionsCategory.html#isNested()), [isUseActionForDisable](../../actions/ActionsCategory.html#isUseActionForDisable()), [removeAction](../../actions/ActionsCategory.html#removeAction(com.nomagic.actions.NMAction)), [removeIf](../../actions/ActionsCategory.html#removeIf(java.util.function.Predicate)), [setActions](../../actions/ActionsCategory.html#setActions(java.util.List)), [setDisplayHeader](../../actions/ActionsCategory.html#setDisplayHeader(boolean)), [setNested](../../actions/ActionsCategory.html#setNested(boolean)), [setUseActionForDisable](../../actions/ActionsCategory.html#setUseActionForDisable(boolean)), [size](../../actions/ActionsCategory.html#size()), [sort](../../actions/ActionsCategory.html#sort())`
Methods inherited from class com.nomagic.actions.[NMAction](../../actions/NMAction.html)
`[addPropertyChangeListener](../../actions/NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addShortcut](../../actions/NMAction.html#addShortcut(javax.swing.KeyStroke)), [addShotcut](../../actions/NMAction.html#addShotcut(javax.swing.KeyStroke)), [addWeakPropertyChangeListener](../../actions/NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [compareTo](../../actions/NMAction.html#compareTo(java.lang.Object)), [createMenuItem](../../actions/NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)), [equals](../../actions/NMAction.html#equals(java.lang.Object)), [firePropertyChange](../../actions/NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getCommandKey](../../actions/NMAction.html#getCommandKey()), [getDescription](../../actions/NMAction.html#getDescription()), [getGroup](../../actions/NMAction.html#getGroup()), [getIcon](../../actions/NMAction.html#getIcon()), [getID](../../actions/NMAction.html#getID()), [getLargeOrSmallIcon](../../actions/NMAction.html#getLargeOrSmallIcon()), [getMenuShortcutMaskAsString](../../actions/NMAction.html#getMenuShortcutMaskAsString()), [getMnemonicKey](../../actions/NMAction.html#getMnemonicKey()), [getName](../../actions/NMAction.html#getName()), [getPropertyChangeListeners](../../actions/NMAction.html#getPropertyChangeListeners()), [getShortcuts](../../actions/NMAction.html#getShortcuts()), [getSmallIcon](../../actions/NMAction.html#getSmallIcon()), [getSmallOrLargeIcon](../../actions/NMAction.html#getSmallOrLargeIcon()), [getTinyIcon](../../actions/NMAction.html#getTinyIcon()), [hashCode](../../actions/NMAction.html#hashCode()), [hasMenuShortcutMask](../../actions/NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)), [isIDGenerated](../../actions/NMAction.html#isIDGenerated()), [removePropertyChangeListener](../../actions/NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [removeShortcut](../../actions/NMAction.html#removeShortcut(javax.swing.KeyStroke)), [removeWeakPropertyChangeListener](../../actions/NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [setDescription](../../actions/NMAction.html#setDescription(java.lang.String)), [setGroup](../../actions/NMAction.html#setGroup(java.lang.String)), [setIcon](../../actions/NMAction.html#setIcon(javax.swing.Icon)), [setLargeIcon](../../actions/NMAction.html#setLargeIcon(javax.swing.Icon)), [setMnemonicKey](../../actions/NMAction.html#setMnemonicKey(int)), [setName](../../actions/NMAction.html#setName(java.lang.String)), [setShortcuts](../../actions/NMAction.html#setShortcuts(java.util.List)), [setSmallIcon](../../actions/NMAction.html#setSmallIcon(javax.swing.Icon)), [setTinyIcon](../../actions/NMAction.html#setTinyIcon(javax.swing.Icon)), [toString](../../actions/NMAction.html#toString())`
Methods inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[getKeys](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()), [getValue](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)), [isEnabled](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()), [putValue](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)), [setEnabled](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html)
`[accept](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramInnerToolbarConfiguration
public DiagramInnerToolbarConfiguration(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
DiagramInnerToolbarConfiguration
public DiagramInnerToolbarConfiguration([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
DiagramInnerToolbarConfiguration
public DiagramInnerToolbarConfiguration(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean expandedByDefault)
DiagramInnerToolbarConfiguration
public DiagramInnerToolbarConfiguration(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean expandedByDefault)
DiagramInnerToolbarConfiguration
public DiagramInnerToolbarConfiguration(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean expandedByDefault,
 boolean showText)
 ============ METHOD DETAIL ========== 
Method Details
isExpandByDefault
public boolean isExpandByDefault()
isShowText
public boolean isShowText()
setExpandByDefault
public void setExpandByDefault(boolean expandByDefault)
clone
public [DiagramInnerToolbarConfiguration](DiagramInnerToolbarConfiguration.html) clone()
Description copied from class: `[ActionsCategory](../../actions/ActionsCategory.html#clone())`
Clones the category. During clone does not fire any property change events.
 Does deep clone.
Overrides:
`[clone](../../actions/ActionsCategory.html#clone())` in class `[ActionsCategory](../../actions/ActionsCategory.html)`
Returns:
deep clone of category.
shallowClone
public [DiagramInnerToolbarConfiguration](DiagramInnerToolbarConfiguration.html) shallowClone()
Description copied from class: `[ActionsCategory](../../actions/ActionsCategory.html#shallowClone())`
Clones the category. During clone does not fire any property change events.
 Does deep clone.
Overrides:
`[shallowClone](../../actions/ActionsCategory.html#shallowClone())` in class `[ActionsCategory](../../actions/ActionsCategory.html)`
Returns:
deep clone of category.
getLargeIcon
@CheckForNullpublic [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) getLargeIcon()
Description copied from class: `[NMAction](../../actions/NMAction.html#getLargeIcon())`
Returns the large icon of the action.
Overrides:
`[getLargeIcon](../../actions/NMAction.html#getLargeIcon())` in class `[NMAction](../../actions/NMAction.html)`
Returns:
the large icon of the action.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.actions</a></div>
<h1 class="title" title="Class DiagramInnerToolbarConfiguration">Class DiagramInnerToolbarConfiguration</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">javax.swing.AbstractAction</a>
<div class="inheritance"><a href="../../actions/NMAction.html" title="class in com.nomagic.actions">com.nomagic.actions.NMAction</a>
<div class="inheritance"><a href="../../actions/ActionsCategory.html" title="class in com.nomagic.actions">com.nomagic.actions.ActionsCategory</a>
<div class="inheritance"><a href="MDActionsCategory.html" title="class in com.nomagic.magicdraw.actions">com.nomagic.magicdraw.actions.MDActionsCategory</a>
<div class="inheritance">com.nomagic.magicdraw.actions.DiagramInnerToolbarConfiguration</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.actions.ShortcutSchemaAction</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramInnerToolbarConfiguration</span>
<span class="extends-implements">extends <a href="MDActionsCategory.html" title="class in com.nomagic.magicdraw.actions">MDActionsCategory</a></span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../serialized-form.html#com.nomagic.magicdraw.actions.DiagramInnerToolbarConfiguration">Serialized Form</a></li>
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
<h3 id="fields-inherited-from-class-com.nomagic.actions.ActionsCategory">Fields inherited from class com.nomagic.actions.<a href="../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></h3>
<code><a href="../../actions/ActionsCategory.html#ACTIONS_PROPERTY">ACTIONS_PROPERTY</a>, <a href="../../actions/ActionsCategory.html#ADDED_ACTION_PROPERTY">ADDED_ACTION_PROPERTY</a>, <a href="../../actions/ActionsCategory.html#CHANGE_ACTIONS_PROPERTY">CHANGE_ACTIONS_PROPERTY</a>, <a href="../../actions/ActionsCategory.html#DISABLE_IF_EMPTY">DISABLE_IF_EMPTY</a>, <a href="../../actions/ActionsCategory.html#MAX_CATEGORY_ACTIONS">MAX_CATEGORY_ACTIONS</a>, <a href="../../actions/ActionsCategory.html#REMOVE_IF_EMPTY">REMOVE_IF_EMPTY</a>, <a href="../../actions/ActionsCategory.html#REMOVED_ACTION_PROPERTY">REMOVED_ACTION_PROPERTY</a>, <a href="../../actions/ActionsCategory.html#USE_AS_SEPARATOR_IN_UI">USE_AS_SEPARATOR_IN_UI</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.actions.NMAction">Fields inherited from class com.nomagic.actions.<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="../../actions/NMAction.html#ACTION_SHORTCUTS">ACTION_SHORTCUTS</a>, <a href="../../actions/NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI">BELONGS_TO_SEPARATE_GROUP_IN_UI</a>, <a href="../../actions/NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI">DO_NO_SHOW_ACTION_NAME_IN_UI</a>, <a href="../../actions/NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS">DO_NOT_REGISTER_ACTION_TO_COMPONENTS</a>, <a href="../../actions/NMAction.html#GENERATED_ID_PREFIX">GENERATED_ID_PREFIX</a>, <a href="../../actions/NMAction.html#GROUP">GROUP</a>, <a href="../../actions/NMAction.html#ID">ID</a>, <a href="../../actions/NMAction.html#LARGE_ICON">LARGE_ICON</a>, <a href="../../actions/NMAction.html#MENU_SHORTCUT_MASK">MENU_SHORTCUT_MASK</a>, <a href="../../actions/NMAction.html#TINY_ICON">TINY_ICON</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,javax.swing.Icon,java.lang.String)">DiagramInnerToolbarConfiguration</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,javax.swing.Icon,java.lang.String,boolean)">DiagramInnerToolbarConfiguration</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean expandedByDefault)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,javax.swing.Icon,java.lang.String,boolean,boolean)">DiagramInnerToolbarConfiguration</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean expandedByDefault,
 boolean showText)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(javax.swing.Icon,java.lang.String)">DiagramInnerToolbarConfiguration</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(javax.swing.Icon,java.lang.String,boolean)">DiagramInnerToolbarConfiguration</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean expandedByDefault)</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DiagramInnerToolbarConfiguration.html" title="class in com.nomagic.magicdraw.actions">DiagramInnerToolbarConfiguration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the category.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLargeIcon()">getLargeIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the large icon of the action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isExpandByDefault()">isExpandByDefault</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowText()">isShowText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExpandByDefault(boolean)">setExpandByDefault</a><wbr/>(boolean expandByDefault)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DiagramInnerToolbarConfiguration.html" title="class in com.nomagic.magicdraw.actions">DiagramInnerToolbarConfiguration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#shallowClone()">shallowClone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the category.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.actions.MDActionsCategory">Methods inherited from class com.nomagic.magicdraw.actions.<a href="MDActionsCategory.html" title="class in com.nomagic.magicdraw.actions">MDActionsCategory</a></h3>
<code><a href="MDActionsCategory.html#isUseShortcutSchema()">isUseShortcutSchema</a>, <a href="MDActionsCategory.html#updateState()">updateState</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.ActionsCategory">Methods inherited from class com.nomagic.actions.<a href="../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></h3>
<code><a href="../../actions/ActionsCategory.html#accept(com.nomagic.actions.ActionsVisitor)">accept</a>, <a href="../../actions/ActionsCategory.html#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a>, <a href="../../actions/ActionsCategory.html#addAction(com.nomagic.actions.NMAction)">addAction</a>, <a href="../../actions/ActionsCategory.html#addAction(com.nomagic.actions.NMAction,int)">addAction</a>, <a href="../../actions/ActionsCategory.html#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction)">addActionNearTheGiven</a>, <a href="../../actions/ActionsCategory.html#addActions(java.util.List)">addActions</a>, <a href="../../actions/ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)">breakActions</a>, <a href="../../actions/ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean,int)">breakActions</a>, <a href="../../actions/ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List)">breakActions</a>, <a href="../../actions/ActionsCategory.html#breakeActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)">breakeActions</a>, <a href="../../actions/ActionsCategory.html#createSeparatorCategory()">createSeparatorCategory</a>, <a href="../../actions/ActionsCategory.html#forEach(java.util.function.Consumer)">forEach</a>, <a href="../../actions/ActionsCategory.html#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a>, <a href="../../actions/ActionsCategory.html#getAction(java.lang.String)">getAction</a>, <a href="../../actions/ActionsCategory.html#getActions()">getActions</a>, <a href="../../actions/ActionsCategory.html#getActionsRecursively(boolean)">getActionsRecursively</a>, <a href="../../actions/ActionsCategory.html#getCategories()">getCategories</a>, <a href="../../actions/ActionsCategory.html#isDisplayHeader()">isDisplayHeader</a>, <a href="../../actions/ActionsCategory.html#isEmpty()">isEmpty</a>, <a href="../../actions/ActionsCategory.html#isNested()">isNested</a>, <a href="../../actions/ActionsCategory.html#isUseActionForDisable()">isUseActionForDisable</a>, <a href="../../actions/ActionsCategory.html#removeAction(com.nomagic.actions.NMAction)">removeAction</a>, <a href="../../actions/ActionsCategory.html#removeIf(java.util.function.Predicate)">removeIf</a>, <a href="../../actions/ActionsCategory.html#setActions(java.util.List)">setActions</a>, <a href="../../actions/ActionsCategory.html#setDisplayHeader(boolean)">setDisplayHeader</a>, <a href="../../actions/ActionsCategory.html#setNested(boolean)">setNested</a>, <a href="../../actions/ActionsCategory.html#setUseActionForDisable(boolean)">setUseActionForDisable</a>, <a href="../../actions/ActionsCategory.html#size()">size</a>, <a href="../../actions/ActionsCategory.html#sort()">sort</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.NMAction">Methods inherited from class com.nomagic.actions.<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="../../actions/NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../actions/NMAction.html#addShortcut(javax.swing.KeyStroke)">addShortcut</a>, <a href="../../actions/NMAction.html#addShotcut(javax.swing.KeyStroke)">addShotcut</a>, <a href="../../actions/NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)">addWeakPropertyChangeListener</a>, <a href="../../actions/NMAction.html#compareTo(java.lang.Object)">compareTo</a>, <a href="../../actions/NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)">createMenuItem</a>, <a href="../../actions/NMAction.html#equals(java.lang.Object)">equals</a>, <a href="../../actions/NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../actions/NMAction.html#getCommandKey()">getCommandKey</a>, <a href="../../actions/NMAction.html#getDescription()">getDescription</a>, <a href="../../actions/NMAction.html#getGroup()">getGroup</a>, <a href="../../actions/NMAction.html#getIcon()">getIcon</a>, <a href="../../actions/NMAction.html#getID()">getID</a>, <a href="../../actions/NMAction.html#getLargeOrSmallIcon()">getLargeOrSmallIcon</a>, <a href="../../actions/NMAction.html#getMenuShortcutMaskAsString()">getMenuShortcutMaskAsString</a>, <a href="../../actions/NMAction.html#getMnemonicKey()">getMnemonicKey</a>, <a href="../../actions/NMAction.html#getName()">getName</a>, <a href="../../actions/NMAction.html#getPropertyChangeListeners()">getPropertyChangeListeners</a>, <a href="../../actions/NMAction.html#getShortcuts()">getShortcuts</a>, <a href="../../actions/NMAction.html#getSmallIcon()">getSmallIcon</a>, <a href="../../actions/NMAction.html#getSmallOrLargeIcon()">getSmallOrLargeIcon</a>, <a href="../../actions/NMAction.html#getTinyIcon()">getTinyIcon</a>, <a href="../../actions/NMAction.html#hashCode()">hashCode</a>, <a href="../../actions/NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)">hasMenuShortcutMask</a>, <a href="../../actions/NMAction.html#isIDGenerated()">isIDGenerated</a>, <a href="../../actions/NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../actions/NMAction.html#removeShortcut(javax.swing.KeyStroke)">removeShortcut</a>, <a href="../../actions/NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)">removeWeakPropertyChangeListener</a>, <a href="../../actions/NMAction.html#setDescription(java.lang.String)">setDescription</a>, <a href="../../actions/NMAction.html#setGroup(java.lang.String)">setGroup</a>, <a href="../../actions/NMAction.html#setIcon(javax.swing.Icon)">setIcon</a>, <a href="../../actions/NMAction.html#setLargeIcon(javax.swing.Icon)">setLargeIcon</a>, <a href="../../actions/NMAction.html#setMnemonicKey(int)">setMnemonicKey</a>, <a href="../../actions/NMAction.html#setName(java.lang.String)">setName</a>, <a href="../../actions/NMAction.html#setShortcuts(java.util.List)">setShortcuts</a>, <a href="../../actions/NMAction.html#setSmallIcon(javax.swing.Icon)">setSmallIcon</a>, <a href="../../actions/NMAction.html#setTinyIcon(javax.swing.Icon)">setTinyIcon</a>, <a href="../../actions/NMAction.html#toString()">toString</a></code></div>
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
<section class="detail" id="&lt;init&gt;(javax.swing.Icon,java.lang.String)">
<h3>DiagramInnerToolbarConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramInnerToolbarConfiguration</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,javax.swing.Icon,java.lang.String)">
<h3>DiagramInnerToolbarConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramInnerToolbarConfiguration</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(javax.swing.Icon,java.lang.String,boolean)">
<h3>DiagramInnerToolbarConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramInnerToolbarConfiguration</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean expandedByDefault)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,javax.swing.Icon,java.lang.String,boolean)">
<h3>DiagramInnerToolbarConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramInnerToolbarConfiguration</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean expandedByDefault)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,javax.swing.Icon,java.lang.String,boolean,boolean)">
<h3>DiagramInnerToolbarConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramInnerToolbarConfiguration</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean expandedByDefault,
 boolean showText)</span></div>
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
<section class="detail" id="isExpandByDefault()">
<h3>isExpandByDefault</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExpandByDefault</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowText()">
<h3>isShowText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowText</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setExpandByDefault(boolean)">
<h3>setExpandByDefault</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExpandByDefault</span><wbr/><span class="parameters">(boolean expandByDefault)</span></div>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DiagramInnerToolbarConfiguration.html" title="class in com.nomagic.magicdraw.actions">DiagramInnerToolbarConfiguration</a></span> <span class="element-name">clone</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="../../actions/ActionsCategory.html#clone()">ActionsCategory</a></code></span></div>
<div class="block">Clones the category. During clone does not fire any property change events.
 Does deep clone.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../actions/ActionsCategory.html#clone()">clone</a></code> in class <code><a href="../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></code></dd>
<dt>Returns:</dt>
<dd>deep clone of category.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="shallowClone()">
<h3>shallowClone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DiagramInnerToolbarConfiguration.html" title="class in com.nomagic.magicdraw.actions">DiagramInnerToolbarConfiguration</a></span> <span class="element-name">shallowClone</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="../../actions/ActionsCategory.html#shallowClone()">ActionsCategory</a></code></span></div>
<div class="block">Clones the category. During clone does not fire any property change events.
 Does deep clone.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../actions/ActionsCategory.html#shallowClone()">shallowClone</a></code> in class <code><a href="../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></code></dd>
<dt>Returns:</dt>
<dd>deep clone of category.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLargeIcon()">
<h3>getLargeIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getLargeIcon</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="../../actions/NMAction.html#getLargeIcon()">NMAction</a></code></span></div>
<div class="block">Returns the large icon of the action.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../actions/NMAction.html#getLargeIcon()">getLargeIcon</a></code> in class <code><a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Returns:</dt>
<dd>the large icon of the action.</dd>
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
