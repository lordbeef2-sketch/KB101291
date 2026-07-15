# JAVA OPENAPI: SetFontAction (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/actions/SetFontAction.html
- source_path: `com/nomagic/actions/SetFontAction.html`
- source_sha256: `72c7d1b995670c69d52680fa11f647f23bfeba395b0dc59eafcb8bbe5daf49cc`
- captured_utc: `2026-07-14T16:45:06.911093+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.actions](package-summary.html)

## Class SetFontAction

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[javax.swing.AbstractAction](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html)
[com.nomagic.actions.NMAction](NMAction.html)
[com.nomagic.actions.ActionsCategory](ActionsCategory.html)
com.nomagic.actions.SetFontAction

All Implemented Interfaces:
`com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction`, `com.nomagic.actions.ShortcutsNotCustomizable`, `com.nomagic.actions.StandaloneAction`, `[ActionListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionListener.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)`, `[Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html)`

@OpenApiAllpublic abstract classSetFontAction
extends [ActionsCategory](ActionsCategory.html)
implements [PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html), com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction, com.nomagic.actions.StandaloneAction, com.nomagic.actions.ShortcutsNotCustomizable

Action for choosing font(size and font face).

See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.actions.SetFontAction)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.actions.[ActionsCategory](ActionsCategory.html)
`[ACTIONS_PROPERTY](ActionsCategory.html#ACTIONS_PROPERTY), [ADDED_ACTION_PROPERTY](ActionsCategory.html#ADDED_ACTION_PROPERTY), [CHANGE_ACTIONS_PROPERTY](ActionsCategory.html#CHANGE_ACTIONS_PROPERTY), [DISABLE_IF_EMPTY](ActionsCategory.html#DISABLE_IF_EMPTY), [MAX_CATEGORY_ACTIONS](ActionsCategory.html#MAX_CATEGORY_ACTIONS), [REMOVE_IF_EMPTY](ActionsCategory.html#REMOVE_IF_EMPTY), [REMOVED_ACTION_PROPERTY](ActionsCategory.html#REMOVED_ACTION_PROPERTY), [USE_AS_SEPARATOR_IN_UI](ActionsCategory.html#USE_AS_SEPARATOR_IN_UI)`
Fields inherited from class com.nomagic.actions.[NMAction](NMAction.html)
`[ACTION_SHORTCUTS](NMAction.html#ACTION_SHORTCUTS), [BELONGS_TO_SEPARATE_GROUP_IN_UI](NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI), [DO_NO_SHOW_ACTION_NAME_IN_UI](NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI), [DO_NOT_REGISTER_ACTION_TO_COMPONENTS](NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS), [GENERATED_ID_PREFIX](NMAction.html#GENERATED_ID_PREFIX), [GROUP](NMAction.html#GROUP), [ID](NMAction.html#ID), [LARGE_ICON](NMAction.html#LARGE_ICON), [MENU_SHORTCUT_MASK](NMAction.html#MENU_SHORTCUT_MASK), [TINY_ICON](NMAction.html#TINY_ICON)`
Fields inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[changeSupport](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#changeSupport), [enabled](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#enabled)`
Fields inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html)
`[ACCELERATOR_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#ACCELERATOR_KEY), [ACTION_COMMAND_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#ACTION_COMMAND_KEY), [DEFAULT](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#DEFAULT), [DISPLAYED_MNEMONIC_INDEX_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#DISPLAYED_MNEMONIC_INDEX_KEY), [LARGE_ICON_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#LARGE_ICON_KEY), [LONG_DESCRIPTION](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#LONG_DESCRIPTION), [MNEMONIC_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#MNEMONIC_KEY), [NAME](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#NAME), [SELECTED_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SELECTED_KEY), [SHORT_DESCRIPTION](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SHORT_DESCRIPTION), [SMALL_ICON](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SMALL_ICON)`
Fields inherited from interface com.nomagic.actions.ShortcutsNotCustomizable
`SHORTCUTS_NOT_CUSTOMIZABLE`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SetFontAction](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [KeyStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) group)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`abstract void`
`[changeFontFace](#changeFontFace(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) newFontFace)`
This method is called then inner action for font face name changes its value.
`abstract void`
`[changeFontSize](#changeFontSize(int))(int newSize)`
This method is called then inner action for font size changes its value.
`[SetFontAction](SetFontAction.html)`
`[clone](#clone())()`
Clones the category.
`[AbstractDiagramPresentationElement](../magicdraw/uml/symbols/AbstractDiagramPresentationElement.html)`
`[getDiagram](#getDiagram())()`

`[SetFontFaceAction](SetFontFaceAction.html)`
`[getSetFontFaceAction](#getSetFontFaceAction())()`
Returns inner font face action.
`[SetFontSizeAction](SetFontSizeAction.html)`
`[getSetFontSizeAction](#getSetFontSizeAction())()`
Returns inner font size action.
`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)`

`void`
`[setDiagram](#setDiagram(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../magicdraw/uml/symbols/AbstractDiagramPresentationElement.html) diagram)`
Sets diagram for action.
`void`
`[setEnabled](#setEnabled(boolean))(boolean val)`
Enables or disables this action.
`void`
`[setSetFontFaceAction](#setSetFontFaceAction(com.nomagic.actions.SetFontFaceAction))([SetFontFaceAction](SetFontFaceAction.html) fontFaceAction)`
Sets new font face inner action.
`void`
`[setSetFontSizeAction](#setSetFontSizeAction(com.nomagic.actions.SetFontSizeAction))([SetFontSizeAction](SetFontSizeAction.html) fontSizeAction)`
Sets new font size inner action.
Methods inherited from class com.nomagic.actions.[ActionsCategory](ActionsCategory.html)
`[accept](ActionsCategory.html#accept(com.nomagic.actions.ActionsVisitor)), [actionPerformed](ActionsCategory.html#actionPerformed(java.awt.event.ActionEvent)), [addAction](ActionsCategory.html#addAction(com.nomagic.actions.NMAction)), [addAction](ActionsCategory.html#addAction(com.nomagic.actions.NMAction,int)), [addActionNearTheGiven](ActionsCategory.html#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction)), [addActions](ActionsCategory.html#addActions(java.util.List)), [breakActions](ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)), [breakActions](ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean,int)), [breakActions](ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List)), [breakeActions](ActionsCategory.html#breakeActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)), [createSeparatorCategory](ActionsCategory.html#createSeparatorCategory()), [forEach](ActionsCategory.html#forEach(java.util.function.Consumer)), [forEachIncludingSelf](ActionsCategory.html#forEachIncludingSelf(java.util.function.Consumer)), [getAction](ActionsCategory.html#getAction(java.lang.String)), [getActions](ActionsCategory.html#getActions()), [getActionsRecursively](ActionsCategory.html#getActionsRecursively(boolean)), [getCategories](ActionsCategory.html#getCategories()), [isDisplayHeader](ActionsCategory.html#isDisplayHeader()), [isEmpty](ActionsCategory.html#isEmpty()), [isNested](ActionsCategory.html#isNested()), [isUseActionForDisable](ActionsCategory.html#isUseActionForDisable()), [removeAction](ActionsCategory.html#removeAction(com.nomagic.actions.NMAction)), [removeIf](ActionsCategory.html#removeIf(java.util.function.Predicate)), [setActions](ActionsCategory.html#setActions(java.util.List)), [setDisplayHeader](ActionsCategory.html#setDisplayHeader(boolean)), [setNested](ActionsCategory.html#setNested(boolean)), [setUseActionForDisable](ActionsCategory.html#setUseActionForDisable(boolean)), [shallowClone](ActionsCategory.html#shallowClone()), [size](ActionsCategory.html#size()), [sort](ActionsCategory.html#sort())`
Methods inherited from class com.nomagic.actions.[NMAction](NMAction.html)
`[addPropertyChangeListener](NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addShortcut](NMAction.html#addShortcut(javax.swing.KeyStroke)), [addShotcut](NMAction.html#addShotcut(javax.swing.KeyStroke)), [addWeakPropertyChangeListener](NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [compareTo](NMAction.html#compareTo(java.lang.Object)), [createMenuItem](NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)), [equals](NMAction.html#equals(java.lang.Object)), [firePropertyChange](NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getCommandKey](NMAction.html#getCommandKey()), [getDescription](NMAction.html#getDescription()), [getGroup](NMAction.html#getGroup()), [getIcon](NMAction.html#getIcon()), [getID](NMAction.html#getID()), [getLargeIcon](NMAction.html#getLargeIcon()), [getLargeOrSmallIcon](NMAction.html#getLargeOrSmallIcon()), [getMenuShortcutMaskAsString](NMAction.html#getMenuShortcutMaskAsString()), [getMnemonicKey](NMAction.html#getMnemonicKey()), [getName](NMAction.html#getName()), [getPropertyChangeListeners](NMAction.html#getPropertyChangeListeners()), [getShortcuts](NMAction.html#getShortcuts()), [getSmallIcon](NMAction.html#getSmallIcon()), [getSmallOrLargeIcon](NMAction.html#getSmallOrLargeIcon()), [getTinyIcon](NMAction.html#getTinyIcon()), [hashCode](NMAction.html#hashCode()), [hasMenuShortcutMask](NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)), [isIDGenerated](NMAction.html#isIDGenerated()), [removePropertyChangeListener](NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [removeShortcut](NMAction.html#removeShortcut(javax.swing.KeyStroke)), [removeWeakPropertyChangeListener](NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [setDescription](NMAction.html#setDescription(java.lang.String)), [setGroup](NMAction.html#setGroup(java.lang.String)), [setIcon](NMAction.html#setIcon(javax.swing.Icon)), [setLargeIcon](NMAction.html#setLargeIcon(javax.swing.Icon)), [setMnemonicKey](NMAction.html#setMnemonicKey(int)), [setName](NMAction.html#setName(java.lang.String)), [setShortcuts](NMAction.html#setShortcuts(java.util.List)), [setSmallIcon](NMAction.html#setSmallIcon(javax.swing.Icon)), [setTinyIcon](NMAction.html#setTinyIcon(javax.swing.Icon)), [toString](NMAction.html#toString()), [updateState](NMAction.html#updateState())`
Methods inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[getKeys](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()), [getValue](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)), [isEnabled](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()), [putValue](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html)
`[accept](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SetFontAction
public SetFontAction([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) group)
 ============ METHOD DETAIL ========== 
Method Details
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
changeFontSize
public abstract void changeFontSize(int newSize)
This method is called then inner action for font size changes its value.
Parameters:
`newSize` - the new font size.
changeFontFace
public abstract void changeFontFace([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) newFontFace)
This method is called then inner action for font face name changes its value.
Parameters:
`newFontFace` - the name of new font face.
setSetFontFaceAction
public void setSetFontFaceAction([SetFontFaceAction](SetFontFaceAction.html) fontFaceAction)
Sets new font face inner action. Old font face action will be removed.
Parameters:
`fontFaceAction` - the new font face action.
getSetFontFaceAction
public [SetFontFaceAction](SetFontFaceAction.html) getSetFontFaceAction()
Returns inner font face action.
Returns:
inner font face action.
setSetFontSizeAction
public void setSetFontSizeAction([SetFontSizeAction](SetFontSizeAction.html) fontSizeAction)
Sets new font size inner action. Old font size action will be removed.
Parameters:
`fontSizeAction` - the new font size action.
getSetFontSizeAction
public [SetFontSizeAction](SetFontSizeAction.html) getSetFontSizeAction()
Returns inner font size action.
Returns:
inner font size action.
setEnabled
public void setEnabled(boolean val)
Enables or disables this action. Inner font size and font face actions also will be
 enabled or disabled.
Specified by:
`[setEnabled](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#setEnabled(boolean))` in interface `[Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html)`
Overrides:
`[setEnabled](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean))` in class `[AbstractAction](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html)`
Parameters:
`val` - the new enable flag.
setDiagram
public void setDiagram([AbstractDiagramPresentationElement](../magicdraw/uml/symbols/AbstractDiagramPresentationElement.html) diagram)
Description copied from interface: `com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction`
Sets diagram for action.
Specified by:
`setDiagram` in interface `com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction`
Parameters:
`diagram` - the given diagram.
getDiagram
@CheckForNullpublic [AbstractDiagramPresentationElement](../magicdraw/uml/symbols/AbstractDiagramPresentationElement.html) getDiagram()
clone
public [SetFontAction](SetFontAction.html) clone()
Description copied from class: `[ActionsCategory](ActionsCategory.html#clone())`
Clones the category. During clone does not fire any property change events.
 Does deep clone.
Overrides:
`[clone](ActionsCategory.html#clone())` in class `[ActionsCategory](ActionsCategory.html)`
Returns:
deep clone of category.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.actions</a></div>
<h1 class="title" title="Class SetFontAction">Class SetFontAction</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">javax.swing.AbstractAction</a>
<div class="inheritance"><a href="NMAction.html" title="class in com.nomagic.actions">com.nomagic.actions.NMAction</a>
<div class="inheritance"><a href="ActionsCategory.html" title="class in com.nomagic.actions">com.nomagic.actions.ActionsCategory</a>
<div class="inheritance">com.nomagic.actions.SetFontAction</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction</code>, <code>com.nomagic.actions.ShortcutsNotCustomizable</code>, <code>com.nomagic.actions.StandaloneAction</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">SetFontAction</span>
<span class="extends-implements">extends <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a>, com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction, com.nomagic.actions.StandaloneAction, com.nomagic.actions.ShortcutsNotCustomizable</span></div>
<div class="block">Action for choosing font(size and font face).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../serialized-form.html#com.nomagic.actions.SetFontAction">Serialized Form</a></li>
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
<h3 id="fields-inherited-from-class-com.nomagic.actions.ActionsCategory">Fields inherited from class com.nomagic.actions.<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></h3>
<code><a href="ActionsCategory.html#ACTIONS_PROPERTY">ACTIONS_PROPERTY</a>, <a href="ActionsCategory.html#ADDED_ACTION_PROPERTY">ADDED_ACTION_PROPERTY</a>, <a href="ActionsCategory.html#CHANGE_ACTIONS_PROPERTY">CHANGE_ACTIONS_PROPERTY</a>, <a href="ActionsCategory.html#DISABLE_IF_EMPTY">DISABLE_IF_EMPTY</a>, <a href="ActionsCategory.html#MAX_CATEGORY_ACTIONS">MAX_CATEGORY_ACTIONS</a>, <a href="ActionsCategory.html#REMOVE_IF_EMPTY">REMOVE_IF_EMPTY</a>, <a href="ActionsCategory.html#REMOVED_ACTION_PROPERTY">REMOVED_ACTION_PROPERTY</a>, <a href="ActionsCategory.html#USE_AS_SEPARATOR_IN_UI">USE_AS_SEPARATOR_IN_UI</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.actions.NMAction">Fields inherited from class com.nomagic.actions.<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="NMAction.html#ACTION_SHORTCUTS">ACTION_SHORTCUTS</a>, <a href="NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI">BELONGS_TO_SEPARATE_GROUP_IN_UI</a>, <a href="NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI">DO_NO_SHOW_ACTION_NAME_IN_UI</a>, <a href="NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS">DO_NOT_REGISTER_ACTION_TO_COMPONENTS</a>, <a href="NMAction.html#GENERATED_ID_PREFIX">GENERATED_ID_PREFIX</a>, <a href="NMAction.html#GROUP">GROUP</a>, <a href="NMAction.html#ID">ID</a>, <a href="NMAction.html#LARGE_ICON">LARGE_ICON</a>, <a href="NMAction.html#MENU_SHORTCUT_MASK">MENU_SHORTCUT_MASK</a>, <a href="NMAction.html#TINY_ICON">TINY_ICON</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.AbstractAction">Fields inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">AbstractAction</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#changeSupport" title="class or interface in javax.swing">changeSupport</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#enabled" title="class or interface in javax.swing">enabled</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.Action">Fields inherited from interface javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#ACCELERATOR_KEY" title="class or interface in javax.swing">ACCELERATOR_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#ACTION_COMMAND_KEY" title="class or interface in javax.swing">ACTION_COMMAND_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#DEFAULT" title="class or interface in javax.swing">DEFAULT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#DISPLAYED_MNEMONIC_INDEX_KEY" title="class or interface in javax.swing">DISPLAYED_MNEMONIC_INDEX_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#LARGE_ICON_KEY" title="class or interface in javax.swing">LARGE_ICON_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#LONG_DESCRIPTION" title="class or interface in javax.swing">LONG_DESCRIPTION</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#MNEMONIC_KEY" title="class or interface in javax.swing">MNEMONIC_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#NAME" title="class or interface in javax.swing">NAME</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SELECTED_KEY" title="class or interface in javax.swing">SELECTED_KEY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SHORT_DESCRIPTION" title="class or interface in javax.swing">SHORT_DESCRIPTION</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SMALL_ICON" title="class or interface in javax.swing">SMALL_ICON</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.actions.ShortcutsNotCustomizable">Fields inherited from interface com.nomagic.actions.ShortcutsNotCustomizable</h3>
<code>SHORTCUTS_NOT_CUSTOMIZABLE</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String)">SetFontAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#changeFontFace(java.lang.String)">changeFontFace</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newFontFace)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method is called then inner action for font face name changes its value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#changeFontSize(int)">changeFontSize</a><wbr/>(int newSize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method is called then inner action for font size changes its value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SetFontAction.html" title="class in com.nomagic.actions">SetFontAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the category.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../magicdraw/uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagram()">getDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SetFontFaceAction.html" title="class in com.nomagic.actions">SetFontFaceAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSetFontFaceAction()">getSetFontFaceAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns inner font face action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SetFontSizeAction.html" title="class in com.nomagic.actions">SetFontSizeAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSetFontSizeAction()">getSetFontSizeAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns inner font size action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDiagram(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">setDiagram</a><wbr/>(<a href="../magicdraw/uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets diagram for  action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEnabled(boolean)">setEnabled</a><wbr/>(boolean val)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Enables or disables this action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSetFontFaceAction(com.nomagic.actions.SetFontFaceAction)">setSetFontFaceAction</a><wbr/>(<a href="SetFontFaceAction.html" title="class in com.nomagic.actions">SetFontFaceAction</a> fontFaceAction)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new font face inner action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSetFontSizeAction(com.nomagic.actions.SetFontSizeAction)">setSetFontSizeAction</a><wbr/>(<a href="SetFontSizeAction.html" title="class in com.nomagic.actions">SetFontSizeAction</a> fontSizeAction)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new font size inner action.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.ActionsCategory">Methods inherited from class com.nomagic.actions.<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></h3>
<code><a href="ActionsCategory.html#accept(com.nomagic.actions.ActionsVisitor)">accept</a>, <a href="ActionsCategory.html#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a>, <a href="ActionsCategory.html#addAction(com.nomagic.actions.NMAction)">addAction</a>, <a href="ActionsCategory.html#addAction(com.nomagic.actions.NMAction,int)">addAction</a>, <a href="ActionsCategory.html#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction)">addActionNearTheGiven</a>, <a href="ActionsCategory.html#addActions(java.util.List)">addActions</a>, <a href="ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)">breakActions</a>, <a href="ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean,int)">breakActions</a>, <a href="ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List)">breakActions</a>, <a href="ActionsCategory.html#breakeActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)">breakeActions</a>, <a href="ActionsCategory.html#createSeparatorCategory()">createSeparatorCategory</a>, <a href="ActionsCategory.html#forEach(java.util.function.Consumer)">forEach</a>, <a href="ActionsCategory.html#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a>, <a href="ActionsCategory.html#getAction(java.lang.String)">getAction</a>, <a href="ActionsCategory.html#getActions()">getActions</a>, <a href="ActionsCategory.html#getActionsRecursively(boolean)">getActionsRecursively</a>, <a href="ActionsCategory.html#getCategories()">getCategories</a>, <a href="ActionsCategory.html#isDisplayHeader()">isDisplayHeader</a>, <a href="ActionsCategory.html#isEmpty()">isEmpty</a>, <a href="ActionsCategory.html#isNested()">isNested</a>, <a href="ActionsCategory.html#isUseActionForDisable()">isUseActionForDisable</a>, <a href="ActionsCategory.html#removeAction(com.nomagic.actions.NMAction)">removeAction</a>, <a href="ActionsCategory.html#removeIf(java.util.function.Predicate)">removeIf</a>, <a href="ActionsCategory.html#setActions(java.util.List)">setActions</a>, <a href="ActionsCategory.html#setDisplayHeader(boolean)">setDisplayHeader</a>, <a href="ActionsCategory.html#setNested(boolean)">setNested</a>, <a href="ActionsCategory.html#setUseActionForDisable(boolean)">setUseActionForDisable</a>, <a href="ActionsCategory.html#shallowClone()">shallowClone</a>, <a href="ActionsCategory.html#size()">size</a>, <a href="ActionsCategory.html#sort()">sort</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.NMAction">Methods inherited from class com.nomagic.actions.<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="NMAction.html#addShortcut(javax.swing.KeyStroke)">addShortcut</a>, <a href="NMAction.html#addShotcut(javax.swing.KeyStroke)">addShotcut</a>, <a href="NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)">addWeakPropertyChangeListener</a>, <a href="NMAction.html#compareTo(java.lang.Object)">compareTo</a>, <a href="NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)">createMenuItem</a>, <a href="NMAction.html#equals(java.lang.Object)">equals</a>, <a href="NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="NMAction.html#getCommandKey()">getCommandKey</a>, <a href="NMAction.html#getDescription()">getDescription</a>, <a href="NMAction.html#getGroup()">getGroup</a>, <a href="NMAction.html#getIcon()">getIcon</a>, <a href="NMAction.html#getID()">getID</a>, <a href="NMAction.html#getLargeIcon()">getLargeIcon</a>, <a href="NMAction.html#getLargeOrSmallIcon()">getLargeOrSmallIcon</a>, <a href="NMAction.html#getMenuShortcutMaskAsString()">getMenuShortcutMaskAsString</a>, <a href="NMAction.html#getMnemonicKey()">getMnemonicKey</a>, <a href="NMAction.html#getName()">getName</a>, <a href="NMAction.html#getPropertyChangeListeners()">getPropertyChangeListeners</a>, <a href="NMAction.html#getShortcuts()">getShortcuts</a>, <a href="NMAction.html#getSmallIcon()">getSmallIcon</a>, <a href="NMAction.html#getSmallOrLargeIcon()">getSmallOrLargeIcon</a>, <a href="NMAction.html#getTinyIcon()">getTinyIcon</a>, <a href="NMAction.html#hashCode()">hashCode</a>, <a href="NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)">hasMenuShortcutMask</a>, <a href="NMAction.html#isIDGenerated()">isIDGenerated</a>, <a href="NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="NMAction.html#removeShortcut(javax.swing.KeyStroke)">removeShortcut</a>, <a href="NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)">removeWeakPropertyChangeListener</a>, <a href="NMAction.html#setDescription(java.lang.String)">setDescription</a>, <a href="NMAction.html#setGroup(java.lang.String)">setGroup</a>, <a href="NMAction.html#setIcon(javax.swing.Icon)">setIcon</a>, <a href="NMAction.html#setLargeIcon(javax.swing.Icon)">setLargeIcon</a>, <a href="NMAction.html#setMnemonicKey(int)">setMnemonicKey</a>, <a href="NMAction.html#setName(java.lang.String)">setName</a>, <a href="NMAction.html#setShortcuts(java.util.List)">setShortcuts</a>, <a href="NMAction.html#setSmallIcon(javax.swing.Icon)">setSmallIcon</a>, <a href="NMAction.html#setTinyIcon(javax.swing.Icon)">setTinyIcon</a>, <a href="NMAction.html#toString()">toString</a>, <a href="NMAction.html#updateState()">updateState</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.AbstractAction">Methods inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">AbstractAction</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()" title="class or interface in javax.swing">getKeys</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)" title="class or interface in javax.swing">getValue</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()" title="class or interface in javax.swing">isEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)" title="class or interface in javax.swing">putValue</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String)">
<h3>SetFontAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SetFontAction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
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
<section class="detail" id="propertyChange(java.beans.PropertyChangeEvent)">
<h3>propertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans">propertyChange</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="changeFontSize(int)">
<h3>changeFontSize</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">changeFontSize</span><wbr/><span class="parameters">(int newSize)</span></div>
<div class="block">This method is called then inner action for font size changes its value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>newSize</code> - the new font size.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="changeFontFace(java.lang.String)">
<h3>changeFontFace</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">changeFontFace</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newFontFace)</span></div>
<div class="block">This method is called then inner action for font face name changes its value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>newFontFace</code> - the name of new font face.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSetFontFaceAction(com.nomagic.actions.SetFontFaceAction)">
<h3>setSetFontFaceAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSetFontFaceAction</span><wbr/><span class="parameters">(<a href="SetFontFaceAction.html" title="class in com.nomagic.actions">SetFontFaceAction</a> fontFaceAction)</span></div>
<div class="block">Sets new font face inner action. Old font face action will be removed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fontFaceAction</code> - the new font face action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSetFontFaceAction()">
<h3>getSetFontFaceAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SetFontFaceAction.html" title="class in com.nomagic.actions">SetFontFaceAction</a></span> <span class="element-name">getSetFontFaceAction</span>()</div>
<div class="block">Returns inner font face action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>inner font face action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSetFontSizeAction(com.nomagic.actions.SetFontSizeAction)">
<h3>setSetFontSizeAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSetFontSizeAction</span><wbr/><span class="parameters">(<a href="SetFontSizeAction.html" title="class in com.nomagic.actions">SetFontSizeAction</a> fontSizeAction)</span></div>
<div class="block">Sets new font size inner action. Old font size action will be removed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fontSizeAction</code> - the new font size action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSetFontSizeAction()">
<h3>getSetFontSizeAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SetFontSizeAction.html" title="class in com.nomagic.actions">SetFontSizeAction</a></span> <span class="element-name">getSetFontSizeAction</span>()</div>
<div class="block">Returns inner font size action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>inner font size action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnabled(boolean)">
<h3>setEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnabled</span><wbr/><span class="parameters">(boolean val)</span></div>
<div class="block">Enables or disables this action. Inner font size and font face actions also will be
 enabled or disabled.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#setEnabled(boolean)" title="class or interface in javax.swing">setEnabled</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean)" title="class or interface in javax.swing">setEnabled</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">AbstractAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>val</code> - the new enable flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDiagram(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>setDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDiagram</span><wbr/><span class="parameters">(<a href="../magicdraw/uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code>com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction</code></span></div>
<div class="block">Sets diagram for  action.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setDiagram</code> in interface <code>com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction</code></dd>
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagram()">
<h3>getDiagram</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../magicdraw/uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></span> <span class="element-name">getDiagram</span>()</div>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SetFontAction.html" title="class in com.nomagic.actions">SetFontAction</a></span> <span class="element-name">clone</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="ActionsCategory.html#clone()">ActionsCategory</a></code></span></div>
<div class="block">Clones the category. During clone does not fire any property change events.
 Does deep clone.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ActionsCategory.html#clone()">clone</a></code> in class <code><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></code></dd>
<dt>Returns:</dt>
<dd>deep clone of category.</dd>
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
