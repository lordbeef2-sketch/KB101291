# JAVA OPENAPI: SelectItemAction (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/actions/SelectItemAction.html
- source_path: `com/nomagic/actions/SelectItemAction.html`
- source_sha256: `cf70abd503818b9ebf70ff1c94b7635a132e82219f72025ff9b898107e08b494`
- captured_utc: `2026-07-14T16:50:58.902905+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.actions](package-summary.html)

## Class SelectItemAction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[javax.swing.AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
[com.nomagic.actions.NMAction](NMAction.html)
[com.nomagic.actions.ActionsCategory](ActionsCategory.html)
com.nomagic.actions.SelectItemAction

All Implemented Interfaces:
`[ActionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`, `[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)`

Direct Known Subclasses:
`[SetFontFaceAction](SetFontFaceAction.html)`, `[SetFontSizeAction](SetFontSizeAction.html)`

@OpenApiAllpublic classSelectItemAction
extends [ActionsCategory](ActionsCategory.html)
implements [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)

Action for selecting item from the list. List can contain any objects which
 have correct `toString()` method. When this action is represented
 as toolbar GUI component is a combo box. When this action is represented as
 menu GUI component is a sub menu. By default combo box and sub menu items
 displays only strings from list elements, but it can be changed by overriding
 `createAction(Object, String)` method which can create another
 type of actions used to display list items.
 
 Selected item can be got using `getCurrent()` method. When
 selection is changed action fires property change event with name
 `getValueName()`.

See Also:
[`createAction(Object, String)`](#createAction(java.lang.Object,java.lang.String))
[Serialized Form](../../../serialized-form.html#com.nomagic.actions.SelectItemAction)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ADDITIONAL_PROPERTY_MAX_WIDTH](#ADDITIONAL_PROPERTY_MAX_WIDTH)`
A name of additional action property for specifying max width of component.
Fields inherited from class com.nomagic.actions.[ActionsCategory](ActionsCategory.html)
`[ACTIONS_PROPERTY](ActionsCategory.html#ACTIONS_PROPERTY), [ADDED_ACTION_PROPERTY](ActionsCategory.html#ADDED_ACTION_PROPERTY), [CHANGE_ACTIONS_PROPERTY](ActionsCategory.html#CHANGE_ACTIONS_PROPERTY), [DISABLE_IF_EMPTY](ActionsCategory.html#DISABLE_IF_EMPTY), [MAX_CATEGORY_ACTIONS](ActionsCategory.html#MAX_CATEGORY_ACTIONS), [REMOVE_IF_EMPTY](ActionsCategory.html#REMOVE_IF_EMPTY), [REMOVED_ACTION_PROPERTY](ActionsCategory.html#REMOVED_ACTION_PROPERTY), [USE_AS_SEPARATOR_IN_UI](ActionsCategory.html#USE_AS_SEPARATOR_IN_UI)`
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
`[SelectItemAction](#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.String,java.util.List,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int stroke,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> items,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) valueName)`
Creates action and fills it with action for each element from list.
`[SelectItemAction](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String,java.util.List,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> items,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) valueName)`
Creates action and fills it with action for each element from list.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.actions.ActionsVisitor))([ActionsVisitor](ActionsVisitor.html) visitor)`
If given visitor is `MainActionsVisitor`, visit this action in
 different way.
`[SelectItemAction](SelectItemAction.html)`
`[clone](#clone())()`
Clones the category.
`protected [SelectionStateItem](SelectionStateItem.html)`
`[createAction](#createAction(java.lang.Object,java.lang.String))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) valueName)`
Method creates action which represents given object, and fires
 `PropertyChangeEvent` with name valueName when it is executed.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?>`
`[getItems](#getItems())()`

`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue())()`
Method returns current selection.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getValueName](#getValueName())()`
Returns property name which will be used to fire property change and to put value.
`boolean`
`[isChangeable](#isChangeable())()`
Returns true if new action item can be added.
`boolean`
`[isDisplayAsComboBox](#isDisplayAsComboBox())()`

`boolean`
`[isShowActionName](#isShowActionName())()`

`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)`
Listens for child action.
`void`
`[setChangeable](#setChangeable(boolean))(boolean val)`
Sets changeable property.
`void`
`[setDisplayAsComboBox](#setDisplayAsComboBox(boolean))(boolean displayAsComboBox)`

`void`
`[setItems](#setItems(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> items)`
Sets List value.
`void`
`[setList](#setList(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) newList)`
Deprecated.
use #setItems(java.util.List)
`void`
`[setShowActionName](#setShowActionName(boolean))(boolean showActionName)`

`void`
`[setValue](#setValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets new value of this list action.
`void`
`[updateState](#updateState())()`
Updates state for actions from actions in list.
Methods inherited from class com.nomagic.actions.[ActionsCategory](ActionsCategory.html)
`[actionPerformed](ActionsCategory.html#actionPerformed(java.awt.event.ActionEvent)), [addAction](ActionsCategory.html#addAction(com.nomagic.actions.NMAction)), [addAction](ActionsCategory.html#addAction(com.nomagic.actions.NMAction,int)), [addActionNearTheGiven](ActionsCategory.html#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction)), [addActions](ActionsCategory.html#addActions(java.util.List)), [breakActions](ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)), [breakActions](ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean,int)), [breakActions](ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List)), [breakeActions](ActionsCategory.html#breakeActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)), [createSeparatorCategory](ActionsCategory.html#createSeparatorCategory()), [forEach](ActionsCategory.html#forEach(java.util.function.Consumer)), [forEachIncludingSelf](ActionsCategory.html#forEachIncludingSelf(java.util.function.Consumer)), [getAction](ActionsCategory.html#getAction(java.lang.String)), [getActions](ActionsCategory.html#getActions()), [getActionsRecursively](ActionsCategory.html#getActionsRecursively(boolean)), [getCategories](ActionsCategory.html#getCategories()), [isDisplayHeader](ActionsCategory.html#isDisplayHeader()), [isEmpty](ActionsCategory.html#isEmpty()), [isNested](ActionsCategory.html#isNested()), [isUseActionForDisable](ActionsCategory.html#isUseActionForDisable()), [removeAction](ActionsCategory.html#removeAction(com.nomagic.actions.NMAction)), [removeIf](ActionsCategory.html#removeIf(java.util.function.Predicate)), [setActions](ActionsCategory.html#setActions(java.util.List)), [setDisplayHeader](ActionsCategory.html#setDisplayHeader(boolean)), [setNested](ActionsCategory.html#setNested(boolean)), [setUseActionForDisable](ActionsCategory.html#setUseActionForDisable(boolean)), [shallowClone](ActionsCategory.html#shallowClone()), [size](ActionsCategory.html#size()), [sort](ActionsCategory.html#sort())`
Methods inherited from class com.nomagic.actions.[NMAction](NMAction.html)
`[addPropertyChangeListener](NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addShortcut](NMAction.html#addShortcut(javax.swing.KeyStroke)), [addShotcut](NMAction.html#addShotcut(javax.swing.KeyStroke)), [addWeakPropertyChangeListener](NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [compareTo](NMAction.html#compareTo(java.lang.Object)), [createMenuItem](NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)), [equals](NMAction.html#equals(java.lang.Object)), [firePropertyChange](NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getCommandKey](NMAction.html#getCommandKey()), [getDescription](NMAction.html#getDescription()), [getGroup](NMAction.html#getGroup()), [getIcon](NMAction.html#getIcon()), [getID](NMAction.html#getID()), [getLargeIcon](NMAction.html#getLargeIcon()), [getLargeOrSmallIcon](NMAction.html#getLargeOrSmallIcon()), [getMenuShortcutMaskAsString](NMAction.html#getMenuShortcutMaskAsString()), [getMnemonicKey](NMAction.html#getMnemonicKey()), [getName](NMAction.html#getName()), [getPropertyChangeListeners](NMAction.html#getPropertyChangeListeners()), [getShortcuts](NMAction.html#getShortcuts()), [getSmallIcon](NMAction.html#getSmallIcon()), [getSmallOrLargeIcon](NMAction.html#getSmallOrLargeIcon()), [getTinyIcon](NMAction.html#getTinyIcon()), [hashCode](NMAction.html#hashCode()), [hasMenuShortcutMask](NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)), [isIDGenerated](NMAction.html#isIDGenerated()), [removePropertyChangeListener](NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [removeShortcut](NMAction.html#removeShortcut(javax.swing.KeyStroke)), [removeWeakPropertyChangeListener](NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [setDescription](NMAction.html#setDescription(java.lang.String)), [setGroup](NMAction.html#setGroup(java.lang.String)), [setIcon](NMAction.html#setIcon(javax.swing.Icon)), [setLargeIcon](NMAction.html#setLargeIcon(javax.swing.Icon)), [setMnemonicKey](NMAction.html#setMnemonicKey(int)), [setName](NMAction.html#setName(java.lang.String)), [setShortcuts](NMAction.html#setShortcuts(java.util.List)), [setSmallIcon](NMAction.html#setSmallIcon(javax.swing.Icon)), [setTinyIcon](NMAction.html#setTinyIcon(javax.swing.Icon)), [toString](NMAction.html#toString())`
Methods inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[getKeys](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()), [getValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)), [isEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()), [putValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)), [setEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[accept](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object))`

============ FIELD DETAIL =========== 
Field Details
ADDITIONAL_PROPERTY_MAX_WIDTH
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ADDITIONAL_PROPERTY_MAX_WIDTH
A name of additional action property for specifying max width of component. Toolbar creator may use that setting if needed.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.SelectItemAction.ADDITIONAL_PROPERTY_MAX_WIDTH)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SelectItemAction
public SelectItemAction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> items,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) valueName)
Creates action and fills it with action for each element from list.
Parameters:
`id` - id of action
`name` - action name
`stroke` - key stroke for action.
`group` - action group.
`items` - list of selections.
`valueName` - name of fired property when value is changed.
See Also:
[`setItems(List)`](#setItems(java.util.List))
SelectItemAction
public SelectItemAction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int stroke,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> items,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) valueName)
Creates action and fills it with action for each element from list.
Parameters:
`id` - id of action
`name` - action name
`stroke` - key stroke for action.
`group` - action group.
`items` - list selections.
`valueName` - name of fired property when value is changed.
See Also:
[`setItems(List)`](#setItems(java.util.List))
 ============ METHOD DETAIL ========== 
Method Details
setItems
public void setItems(@CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> items)
Sets List value.
 For each item from items new action will be created using createAction method.
Parameters:
`items` - items of objects from which actions will be created.
getItems
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> getItems()
setList
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void setList([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) newList)
Deprecated.
use #setItems(java.util.List)
createAction
protected [SelectionStateItem](SelectionStateItem.html) createAction([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) valueName)
Method creates action which represents given object, and fires
 `PropertyChangeEvent` with name valueName when it is executed.
Parameters:
`obj` - object from which action will be created.
`valueName` - property name which should be fired when created action is executed.
See Also:
[`SelectionStateItem`](SelectionStateItem.html)
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)
Listens for child action. Puts value got from the event with
 `getPropertyName()` using `setCurrent( method )`
 method. If children actions is state actions updates theirs state.
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
updateState
public void updateState()
Updates state for actions from actions in list.
Overrides:
`[updateState](NMAction.html#updateState())` in class `[NMAction](NMAction.html)`
See Also:
[`NMStateAction.setState(boolean)`](NMStateAction.html#setState(boolean))
clone
public [SelectItemAction](SelectItemAction.html) clone()
Description copied from class: `[ActionsCategory](ActionsCategory.html#clone())`
Clones the category. During clone does not fire any property change events.
 Does deep clone.
Overrides:
`[clone](ActionsCategory.html#clone())` in class `[ActionsCategory](ActionsCategory.html)`
Returns:
deep clone of category.
getValue
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getValue()
Method returns current selection.
Returns:
currently selected object.
isChangeable
public boolean isChangeable()
Returns true if new action item can be added.
Returns:
true if this action is changeable.
setChangeable
public void setChangeable(boolean val)
Sets changeable property.
Parameters:
`val` - new value.
setValue
public void setValue([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Sets new value of this list action.
getValueName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getValueName()
Returns property name which will be used to fire property change and to put value.
Returns:
property name.
accept
public void accept([ActionsVisitor](ActionsVisitor.html) visitor)
If given visitor is `MainActionsVisitor`, visit this action in
 different way.
Overrides:
`[accept](ActionsCategory.html#accept(com.nomagic.actions.ActionsVisitor))` in class `[ActionsCategory](ActionsCategory.html)`
Parameters:
`visitor` - the given visitor.
isShowActionName
public boolean isShowActionName()
setShowActionName
public void setShowActionName(boolean showActionName)
isDisplayAsComboBox
public boolean isDisplayAsComboBox()
setDisplayAsComboBox
public void setDisplayAsComboBox(boolean displayAsComboBox)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.actions</a></div>
<h1 class="title" title="Class SelectItemAction">Class SelectItemAction</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">javax.swing.AbstractAction</a>
<div class="inheritance"><a href="NMAction.html" title="class in com.nomagic.actions">com.nomagic.actions.NMAction</a>
<div class="inheritance"><a href="ActionsCategory.html" title="class in com.nomagic.actions">com.nomagic.actions.ActionsCategory</a>
<div class="inheritance">com.nomagic.actions.SelectItemAction</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="SetFontFaceAction.html" title="class in com.nomagic.actions">SetFontFaceAction</a></code>, <code><a href="SetFontSizeAction.html" title="class in com.nomagic.actions">SetFontSizeAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SelectItemAction</span>
<span class="extends-implements">extends <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></span></div>
<div class="block">Action for selecting item from the list. List can contain any objects which
 have correct <code>toString()</code> method. When this action is represented
 as toolbar GUI component is a combo box. When this action is represented as
 menu GUI component  is a sub menu. By default combo box and sub menu items
 displays only strings from list elements, but it can be changed by overriding
 <code>createAction(Object, String)</code> method which can create another
 type of actions used to display list items.
 <p></p>
 Selected item can be got using <code>getCurrent()</code> method. When
 selection is changed action fires property change event with name
 <code>getValueName()</code>.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#createAction(java.lang.Object,java.lang.String)"><code>createAction(Object, String)</code></a></li>
<li><a href="../../../serialized-form.html#com.nomagic.actions.SelectItemAction">Serialized Form</a></li>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ADDITIONAL_PROPERTY_MAX_WIDTH">ADDITIONAL_PROPERTY_MAX_WIDTH</a></code></div>
<div class="col-last even-row-color">
<div class="block">A name of additional action property for specifying max width of component.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.actions.ActionsCategory">Fields inherited from class com.nomagic.actions.<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></h3>
<code><a href="ActionsCategory.html#ACTIONS_PROPERTY">ACTIONS_PROPERTY</a>, <a href="ActionsCategory.html#ADDED_ACTION_PROPERTY">ADDED_ACTION_PROPERTY</a>, <a href="ActionsCategory.html#CHANGE_ACTIONS_PROPERTY">CHANGE_ACTIONS_PROPERTY</a>, <a href="ActionsCategory.html#DISABLE_IF_EMPTY">DISABLE_IF_EMPTY</a>, <a href="ActionsCategory.html#MAX_CATEGORY_ACTIONS">MAX_CATEGORY_ACTIONS</a>, <a href="ActionsCategory.html#REMOVE_IF_EMPTY">REMOVE_IF_EMPTY</a>, <a href="ActionsCategory.html#REMOVED_ACTION_PROPERTY">REMOVED_ACTION_PROPERTY</a>, <a href="ActionsCategory.html#USE_AS_SEPARATOR_IN_UI">USE_AS_SEPARATOR_IN_UI</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.String,java.util.List,java.lang.String)">SelectItemAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int stroke,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; items,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> valueName)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates action and fills it with action for each element from list.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String,java.util.List,java.lang.String)">SelectItemAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; items,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> valueName)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates action and fills it with action for each element from list.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.actions.ActionsVisitor)">accept</a><wbr/>(<a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If given visitor is <code>MainActionsVisitor</code>, visit this action in
 different way.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SelectItemAction.html" title="class in com.nomagic.actions">SelectItemAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the category.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="SelectionStateItem.html" title="class in com.nomagic.actions">SelectionStateItem</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAction(java.lang.Object,java.lang.String)">createAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> valueName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method creates action which represents given object, and fires
 <code>PropertyChangeEvent</code> with name valueName when it is executed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getItems()">getItems</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue()">getValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method returns current selection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueName()">getValueName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property name which will be used to fire property change and to put value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isChangeable()">isChangeable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if new action item can be added.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisplayAsComboBox()">isDisplayAsComboBox</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowActionName()">isShowActionName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Listens for child action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChangeable(boolean)">setChangeable</a><wbr/>(boolean val)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets changeable property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayAsComboBox(boolean)">setDisplayAsComboBox</a><wbr/>(boolean displayAsComboBox)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setItems(java.util.List)">setItems</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; items)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets List value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setList(java.util.List)">setList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> newList)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use #setItems(java.util.List)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowActionName(boolean)">setShowActionName</a><wbr/>(boolean showActionName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(java.lang.Object)">setValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new value of this list action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateState()">updateState</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates state for actions from actions in list.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.ActionsCategory">Methods inherited from class com.nomagic.actions.<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></h3>
<code><a href="ActionsCategory.html#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a>, <a href="ActionsCategory.html#addAction(com.nomagic.actions.NMAction)">addAction</a>, <a href="ActionsCategory.html#addAction(com.nomagic.actions.NMAction,int)">addAction</a>, <a href="ActionsCategory.html#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction)">addActionNearTheGiven</a>, <a href="ActionsCategory.html#addActions(java.util.List)">addActions</a>, <a href="ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)">breakActions</a>, <a href="ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean,int)">breakActions</a>, <a href="ActionsCategory.html#breakActions(com.nomagic.actions.ActionsCategory,java.util.List)">breakActions</a>, <a href="ActionsCategory.html#breakeActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)">breakeActions</a>, <a href="ActionsCategory.html#createSeparatorCategory()">createSeparatorCategory</a>, <a href="ActionsCategory.html#forEach(java.util.function.Consumer)">forEach</a>, <a href="ActionsCategory.html#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a>, <a href="ActionsCategory.html#getAction(java.lang.String)">getAction</a>, <a href="ActionsCategory.html#getActions()">getActions</a>, <a href="ActionsCategory.html#getActionsRecursively(boolean)">getActionsRecursively</a>, <a href="ActionsCategory.html#getCategories()">getCategories</a>, <a href="ActionsCategory.html#isDisplayHeader()">isDisplayHeader</a>, <a href="ActionsCategory.html#isEmpty()">isEmpty</a>, <a href="ActionsCategory.html#isNested()">isNested</a>, <a href="ActionsCategory.html#isUseActionForDisable()">isUseActionForDisable</a>, <a href="ActionsCategory.html#removeAction(com.nomagic.actions.NMAction)">removeAction</a>, <a href="ActionsCategory.html#removeIf(java.util.function.Predicate)">removeIf</a>, <a href="ActionsCategory.html#setActions(java.util.List)">setActions</a>, <a href="ActionsCategory.html#setDisplayHeader(boolean)">setDisplayHeader</a>, <a href="ActionsCategory.html#setNested(boolean)">setNested</a>, <a href="ActionsCategory.html#setUseActionForDisable(boolean)">setUseActionForDisable</a>, <a href="ActionsCategory.html#shallowClone()">shallowClone</a>, <a href="ActionsCategory.html#size()">size</a>, <a href="ActionsCategory.html#sort()">sort</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.NMAction">Methods inherited from class com.nomagic.actions.<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="NMAction.html#addShortcut(javax.swing.KeyStroke)">addShortcut</a>, <a href="NMAction.html#addShotcut(javax.swing.KeyStroke)">addShotcut</a>, <a href="NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)">addWeakPropertyChangeListener</a>, <a href="NMAction.html#compareTo(java.lang.Object)">compareTo</a>, <a href="NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)">createMenuItem</a>, <a href="NMAction.html#equals(java.lang.Object)">equals</a>, <a href="NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="NMAction.html#getCommandKey()">getCommandKey</a>, <a href="NMAction.html#getDescription()">getDescription</a>, <a href="NMAction.html#getGroup()">getGroup</a>, <a href="NMAction.html#getIcon()">getIcon</a>, <a href="NMAction.html#getID()">getID</a>, <a href="NMAction.html#getLargeIcon()">getLargeIcon</a>, <a href="NMAction.html#getLargeOrSmallIcon()">getLargeOrSmallIcon</a>, <a href="NMAction.html#getMenuShortcutMaskAsString()">getMenuShortcutMaskAsString</a>, <a href="NMAction.html#getMnemonicKey()">getMnemonicKey</a>, <a href="NMAction.html#getName()">getName</a>, <a href="NMAction.html#getPropertyChangeListeners()">getPropertyChangeListeners</a>, <a href="NMAction.html#getShortcuts()">getShortcuts</a>, <a href="NMAction.html#getSmallIcon()">getSmallIcon</a>, <a href="NMAction.html#getSmallOrLargeIcon()">getSmallOrLargeIcon</a>, <a href="NMAction.html#getTinyIcon()">getTinyIcon</a>, <a href="NMAction.html#hashCode()">hashCode</a>, <a href="NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)">hasMenuShortcutMask</a>, <a href="NMAction.html#isIDGenerated()">isIDGenerated</a>, <a href="NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="NMAction.html#removeShortcut(javax.swing.KeyStroke)">removeShortcut</a>, <a href="NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)">removeWeakPropertyChangeListener</a>, <a href="NMAction.html#setDescription(java.lang.String)">setDescription</a>, <a href="NMAction.html#setGroup(java.lang.String)">setGroup</a>, <a href="NMAction.html#setIcon(javax.swing.Icon)">setIcon</a>, <a href="NMAction.html#setLargeIcon(javax.swing.Icon)">setLargeIcon</a>, <a href="NMAction.html#setMnemonicKey(int)">setMnemonicKey</a>, <a href="NMAction.html#setName(java.lang.String)">setName</a>, <a href="NMAction.html#setShortcuts(java.util.List)">setShortcuts</a>, <a href="NMAction.html#setSmallIcon(javax.swing.Icon)">setSmallIcon</a>, <a href="NMAction.html#setTinyIcon(javax.swing.Icon)">setTinyIcon</a>, <a href="NMAction.html#toString()">toString</a></code></div>
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
<section class="detail" id="ADDITIONAL_PROPERTY_MAX_WIDTH">
<h3>ADDITIONAL_PROPERTY_MAX_WIDTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ADDITIONAL_PROPERTY_MAX_WIDTH</span></div>
<div class="block">A name of additional action property for specifying max width of component. Toolbar creator may use that setting if needed.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.SelectItemAction.ADDITIONAL_PROPERTY_MAX_WIDTH">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String,java.util.List,java.lang.String)">
<h3>SelectItemAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SelectItemAction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; items,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> valueName)</span></div>
<div class="block">Creates action and fills it with action for each element from list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - id of action</dd>
<dd><code>name</code> - action name</dd>
<dd><code>stroke</code> - key stroke for action.</dd>
<dd><code>group</code> - action group.</dd>
<dd><code>items</code> - list of selections.</dd>
<dd><code>valueName</code> - name of fired property when value is changed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#setItems(java.util.List)"><code>setItems(List)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,int,java.lang.String,java.util.List,java.lang.String)">
<h3>SelectItemAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SelectItemAction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int stroke,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; items,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> valueName)</span></div>
<div class="block">Creates action and fills it with action for each element from list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - id of action</dd>
<dd><code>name</code> - action name</dd>
<dd><code>stroke</code> - key stroke for action.</dd>
<dd><code>group</code> - action group.</dd>
<dd><code>items</code> - list selections.</dd>
<dd><code>valueName</code> - name of fired property when value is changed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#setItems(java.util.List)"><code>setItems(List)</code></a></li>
</ul>
</dd>
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
<section class="detail" id="setItems(java.util.List)">
<h3>setItems</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setItems</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; items)</span></div>
<div class="block">Sets List value.
 For each item from items new action will be created using createAction method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>items</code> - items of objects from which actions will be created.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getItems()">
<h3>getItems</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt;</span> <span class="element-name">getItems</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setList(java.util.List)">
<h3>setList</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> newList)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use #setItems(java.util.List)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="createAction(java.lang.Object,java.lang.String)">
<h3>createAction</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="SelectionStateItem.html" title="class in com.nomagic.actions">SelectionStateItem</a></span> <span class="element-name">createAction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> valueName)</span></div>
<div class="block">Method creates action which represents given object, and fires
 <code>PropertyChangeEvent</code> with name valueName when it is executed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - object from which action will be created.</dd>
<dd><code>valueName</code> - property name which should be fired when created action is executed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="SelectionStateItem.html" title="class in com.nomagic.actions"><code>SelectionStateItem</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="propertyChange(java.beans.PropertyChangeEvent)">
<h3>propertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</span></div>
<div class="block">Listens for child action. Puts value got from the event with
 <code>getPropertyName()</code> using <code>setCurrent( method )</code>
 method. If children actions is state actions updates theirs state.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans">propertyChange</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateState()">
<h3>updateState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateState</span>()</div>
<div class="block">Updates state for actions from actions in list.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="NMAction.html#updateState()">updateState</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="NMStateAction.html#setState(boolean)"><code>NMStateAction.setState(boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SelectItemAction.html" title="class in com.nomagic.actions">SelectItemAction</a></span> <span class="element-name">clone</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="ActionsCategory.html#clone()">ActionsCategory</a></code></span></div>
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
<li>
<section class="detail" id="getValue()">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span>()</div>
<div class="block">Method returns current selection.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>currently selected object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isChangeable()">
<h3>isChangeable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isChangeable</span>()</div>
<div class="block">Returns true if new action item can be added.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this action is changeable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChangeable(boolean)">
<h3>setChangeable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChangeable</span><wbr/><span class="parameters">(boolean val)</span></div>
<div class="block">Sets changeable property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>val</code> - new value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets new value of this list action.</div>
</section>
</li>
<li>
<section class="detail" id="getValueName()">
<h3>getValueName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValueName</span>()</div>
<div class="block">Returns property name which will be used to fire property change and to put value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.actions.ActionsVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a> visitor)</span></div>
<div class="block">If given visitor is <code>MainActionsVisitor</code>, visit this action in
 different way.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ActionsCategory.html#accept(com.nomagic.actions.ActionsVisitor)">accept</a></code> in class <code><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - the given visitor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowActionName()">
<h3>isShowActionName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowActionName</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setShowActionName(boolean)">
<h3>setShowActionName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowActionName</span><wbr/><span class="parameters">(boolean showActionName)</span></div>
</section>
</li>
<li>
<section class="detail" id="isDisplayAsComboBox()">
<h3>isDisplayAsComboBox</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisplayAsComboBox</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDisplayAsComboBox(boolean)">
<h3>setDisplayAsComboBox</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisplayAsComboBox</span><wbr/><span class="parameters">(boolean displayAsComboBox)</span></div>
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
