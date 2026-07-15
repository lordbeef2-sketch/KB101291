# JAVA OPENAPI: ActionsCategory (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/actions/ActionsCategory.html
- source_path: `com/nomagic/actions/ActionsCategory.html`
- source_sha256: `97b4c40625df484870b65421e1508b7f7e58b3e7c05636b266fcaac865fbc11d`
- captured_utc: `2026-07-14T16:50:59.318911+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.actions](package-summary.html)

## Class ActionsCategory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[javax.swing.AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
[com.nomagic.actions.NMAction](NMAction.html)
com.nomagic.actions.ActionsCategory

All Implemented Interfaces:
`[ActionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`, `[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)`

Direct Known Subclasses:
`[MDActionsCategory](../magicdraw/actions/MDActionsCategory.html)`, `[MenuAction](MenuAction.html)`, `[SelectItemAction](SelectItemAction.html)`, `[SetFontAction](SetFontAction.html)`

@OpenApiAllpublic classActionsCategory
extends [NMAction](NMAction.html)

Actions category owns a list of actions.
 Actions category can represent structure of menu or toolbar, and it can be nested (represents sub menu).

See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.actions.ActionsCategory)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ACTIONS_PROPERTY](#ACTIONS_PROPERTY)`
Property Change event name fired when actions of this category were changed.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ADDED_ACTION_PROPERTY](#ADDED_ACTION_PROPERTY)`
Property Change event name fired when new action is added.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CHANGE_ACTIONS_PROPERTY](#CHANGE_ACTIONS_PROPERTY)`
Deprecated.
use [`ACTIONS_PROPERTY`](#ACTIONS_PROPERTY), [`ADDED_ACTION_PROPERTY`](#ADDED_ACTION_PROPERTY), [`REMOVED_ACTION_PROPERTY`](#REMOVED_ACTION_PROPERTY)
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DISABLE_IF_EMPTY](#DISABLE_IF_EMPTY)`
A name of property to disable the category if it has no actions.
`static final int`
`[MAX_CATEGORY_ACTIONS](#MAX_CATEGORY_ACTIONS)`
Default value limiting maximum action count in one category
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REMOVE_IF_EMPTY](#REMOVE_IF_EMPTY)`
A name of property to drop the category if it has no actions.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REMOVED_ACTION_PROPERTY](#REMOVED_ACTION_PROPERTY)`
Property Change event name fired when new action is removed.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[USE_AS_SEPARATOR_IN_UI](#USE_AS_SEPARATOR_IN_UI)`
A name of property to use this category as separator in UI even if it does not have inner actions
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
`[ActionsCategory](#%3Cinit%3E())()`
Creates actions category with no name
`[ActionsCategory](#%3Cinit%3E(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Creates actions category with given name and id.
`[ActionsCategory](#%3Cinit%3E(java.lang.String,java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int keyCode)`
Creates actions category with given id, name, and key code.
`[ActionsCategory](#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int keyCode,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`
Creates actions category with given id, name, and key code.
`[ActionsCategory](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke)`
Creates actions category with given id, name, and keystroke.
`[ActionsCategory](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`
Creates actions category with given id, name, keystroke and assigned
 group.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.actions.ActionsVisitor))([ActionsVisitor](ActionsVisitor.html) visitor)`
Accepts visitor and calls visit method of visitor.
`void`
`[actionPerformed](#actionPerformed(java.awt.event.ActionEvent))([ActionEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionEvent.html) e)`
Empty implementation.
`void`
`[addAction](#addAction(com.nomagic.actions.NMAction))([NMAction](NMAction.html) action)`
Adds the given action to the category.
`void`
`[addAction](#addAction(com.nomagic.actions.NMAction,int))([NMAction](NMAction.html) action,
 int position)`
Adds the given action at the specified position to the category.
`void`
`[addActionNearTheGiven](#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) givenID,
 boolean addAfter,
 [NMAction](NMAction.html) action)`
Adds given action near the action with the given id.
`void`
`[addActions](#addActions(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](NMAction.html)> actions)`
Adds given actions to the category.
`static void`
`[breakActions](#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean))([ActionsCategory](ActionsCategory.html) category,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](NMAction.html)> actions,
 int maxCategorySize,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) categoryName,
 boolean nested)`
Breaks given actions into subcategories of given category if the actions number exceeds maxCategorySize.
`static void`
`[breakActions](#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean,int))([ActionsCategory](ActionsCategory.html) category,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](NMAction.html)> actions,
 int maxCategorySize,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) categoryName,
 boolean nested,
 int innerCategorySize)`
Breaks category into sub categories, but it has ability to specify inner category size separately
`static void`
`[breakActions](#breakActions(com.nomagic.actions.ActionsCategory,java.util.List))([ActionsCategory](ActionsCategory.html) category,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NMAction](NMAction.html)> actions)`
Breaks given actions into subcategories of given category if the actions number exceeds predefined number.
`static void`
`[breakeActions](#breakeActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean))([ActionsCategory](ActionsCategory.html) category,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](NMAction.html)> actions,
 int maxCategorySize,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) categoryName,
 boolean nested)`
Deprecated.
use [`breakActions(ActionsCategory, java.util.List, int, String, boolean)`](#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean))
`[ActionsCategory](ActionsCategory.html)`
`[clone](#clone())()`
Clones the category.
`static [ActionsCategory](ActionsCategory.html)`
`[createSeparatorCategory](#createSeparatorCategory())()`

`void`
`[forEach](#forEach(java.util.function.Consumer))([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[NMAction](NMAction.html)> consumer)`
Performs the given consumer for each owned action.
`void`
`[forEachIncludingSelf](#forEachIncludingSelf(java.util.function.Consumer))([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[NMAction](NMAction.html)> consumer)`
Performs the given consumer for each owned action including self.
`[NMAction](NMAction.html)`
`[getAction](#getAction(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID)`
Find direct action with given ID
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NMAction](NMAction.html)>`
`[getActions](#getActions())()`
Returns the list of the owned actions.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NMAction](NMAction.html)>`
`[getActionsRecursively](#getActionsRecursively(boolean))(boolean includeCategories)`
Returns all simple actions (not ActionsCategory) recursively.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ActionsCategory](ActionsCategory.html)>`
`[getCategories](#getCategories())()`
Gets inner action categories.
`boolean`
`[isDisplayHeader](#isDisplayHeader())()`

`boolean`
`[isEmpty](#isEmpty())()`

`boolean`
`[isNested](#isNested())()`
Returns value of nested flag.
`boolean`
`[isUseActionForDisable](#isUseActionForDisable())()`
Returns value of nested flag.
`void`
`[removeAction](#removeAction(com.nomagic.actions.NMAction))([NMAction](NMAction.html) action)`
Removes the given action from the category.
`void`
`[removeIf](#removeIf(java.util.function.Predicate))([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[NMAction](NMAction.html)> filter)`
Removes all of the owned actions that satisfy the given predicate
`void`
`[setActions](#setActions(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](NMAction.html)> actions)`
Sets the list of the new actions overriding old actions.
`void`
`[setDisplayHeader](#setDisplayHeader(boolean))(boolean displayHeader)`
Display category name as header of category.
`void`
`[setNested](#setNested(boolean))(boolean nested)`
Sets new value of nested flag.
`void`
`[setUseActionForDisable](#setUseActionForDisable(boolean))(boolean use)`

`[ActionsCategory](ActionsCategory.html)`
`[shallowClone](#shallowClone())()`
Clones the category.
`int`
`[size](#size())()`
Size of category - number of inner actions.
`void`
`[sort](#sort())()`
Methods inherited from class com.nomagic.actions.[NMAction](NMAction.html)
`[addPropertyChangeListener](NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addShortcut](NMAction.html#addShortcut(javax.swing.KeyStroke)), [addShotcut](NMAction.html#addShotcut(javax.swing.KeyStroke)), [addWeakPropertyChangeListener](NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [compareTo](NMAction.html#compareTo(java.lang.Object)), [createMenuItem](NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)), [equals](NMAction.html#equals(java.lang.Object)), [firePropertyChange](NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getCommandKey](NMAction.html#getCommandKey()), [getDescription](NMAction.html#getDescription()), [getGroup](NMAction.html#getGroup()), [getIcon](NMAction.html#getIcon()), [getID](NMAction.html#getID()), [getLargeIcon](NMAction.html#getLargeIcon()), [getLargeOrSmallIcon](NMAction.html#getLargeOrSmallIcon()), [getMenuShortcutMaskAsString](NMAction.html#getMenuShortcutMaskAsString()), [getMnemonicKey](NMAction.html#getMnemonicKey()), [getName](NMAction.html#getName()), [getPropertyChangeListeners](NMAction.html#getPropertyChangeListeners()), [getShortcuts](NMAction.html#getShortcuts()), [getSmallIcon](NMAction.html#getSmallIcon()), [getSmallOrLargeIcon](NMAction.html#getSmallOrLargeIcon()), [getTinyIcon](NMAction.html#getTinyIcon()), [hashCode](NMAction.html#hashCode()), [hasMenuShortcutMask](NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)), [isIDGenerated](NMAction.html#isIDGenerated()), [removePropertyChangeListener](NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [removeShortcut](NMAction.html#removeShortcut(javax.swing.KeyStroke)), [removeWeakPropertyChangeListener](NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [setDescription](NMAction.html#setDescription(java.lang.String)), [setGroup](NMAction.html#setGroup(java.lang.String)), [setIcon](NMAction.html#setIcon(javax.swing.Icon)), [setLargeIcon](NMAction.html#setLargeIcon(javax.swing.Icon)), [setMnemonicKey](NMAction.html#setMnemonicKey(int)), [setName](NMAction.html#setName(java.lang.String)), [setShortcuts](NMAction.html#setShortcuts(java.util.List)), [setSmallIcon](NMAction.html#setSmallIcon(javax.swing.Icon)), [setTinyIcon](NMAction.html#setTinyIcon(javax.swing.Icon)), [toString](NMAction.html#toString()), [updateState](NMAction.html#updateState())`
Methods inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[getKeys](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()), [getValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)), [isEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()), [putValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)), [setEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[accept](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object))`

============ FIELD DETAIL =========== 
Field Details
USE_AS_SEPARATOR_IN_UI
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) USE_AS_SEPARATOR_IN_UI
A name of property to use this category as separator in UI even if it does not have inner actions
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.ActionsCategory.USE_AS_SEPARATOR_IN_UI)
DISABLE_IF_EMPTY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DISABLE_IF_EMPTY
A name of property to disable the category if it has no actions.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.ActionsCategory.DISABLE_IF_EMPTY)
REMOVE_IF_EMPTY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REMOVE_IF_EMPTY
A name of property to drop the category if it has no actions.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.ActionsCategory.REMOVE_IF_EMPTY)
MAX_CATEGORY_ACTIONS
public static final int MAX_CATEGORY_ACTIONS
Default value limiting maximum action count in one category
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.ActionsCategory.MAX_CATEGORY_ACTIONS)
ADDED_ACTION_PROPERTY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ADDED_ACTION_PROPERTY
Property Change event name fired when new action is added.
See Also:
[`addAction(NMAction)`](#addAction(com.nomagic.actions.NMAction))
[`addAction(NMAction, int)`](#addAction(com.nomagic.actions.NMAction,int))
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.ActionsCategory.ADDED_ACTION_PROPERTY)
REMOVED_ACTION_PROPERTY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REMOVED_ACTION_PROPERTY
Property Change event name fired when new action is removed.
See Also:
[`removeAction(NMAction)`](#removeAction(com.nomagic.actions.NMAction))
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.ActionsCategory.REMOVED_ACTION_PROPERTY)
ACTIONS_PROPERTY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ACTIONS_PROPERTY
Property Change event name fired when actions of this category were changed.
See Also:
[`setActions(List)`](#setActions(java.util.List))
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.ActionsCategory.ACTIONS_PROPERTY)
CHANGE_ACTIONS_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CHANGE_ACTIONS_PROPERTY
Deprecated.
use [`ACTIONS_PROPERTY`](#ACTIONS_PROPERTY), [`ADDED_ACTION_PROPERTY`](#ADDED_ACTION_PROPERTY), [`REMOVED_ACTION_PROPERTY`](#REMOVED_ACTION_PROPERTY)
Property Change event name fired when actions of this category were changed.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.ActionsCategory.CHANGE_ACTIONS_PROPERTY)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ActionsCategory
public ActionsCategory()
Creates actions category with no name
ActionsCategory
public ActionsCategory(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Creates actions category with given name and id.
Parameters:
`id` - the id of the category.
`name` - the name of the category.
ActionsCategory
public ActionsCategory(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke)
Creates actions category with given id, name, and keystroke.
Parameters:
`id` - the id of the category.
`name` - the name of the category.
`stroke` - keystroke used for invoking action category.
ActionsCategory
public ActionsCategory(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
Creates actions category with given id, name, keystroke and assigned
 group.
Parameters:
`id` - the id of the category.
`name` - the name of the category.
`stroke` - keystroke used for invoking action category.
`group` - the name of the related commands group.
ActionsCategory
public ActionsCategory(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int keyCode)
Creates actions category with given id, name, and key code.
Parameters:
`id` - the id of the category.
`name` - the name of the category.
`keyCode` - keystroke used for invoking action category.
ActionsCategory
public ActionsCategory(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int keyCode,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
Creates actions category with given id, name, and key code.
Parameters:
`id` - the id of the category.
`name` - the name of the category.
`keyCode` - keystroke used for invoking action category.
`group` - the name of the related commands group.
 ============ METHOD DETAIL ========== 
Method Details
createSeparatorCategory
public static [ActionsCategory](ActionsCategory.html) createSeparatorCategory()
addAction
public void addAction(@CheckForNull
 [NMAction](NMAction.html) action)
Adds the given action to the category.
 Fires [`ADDED_ACTION_PROPERTY`](#ADDED_ACTION_PROPERTY) property change event, where new value is added action.
 Fires [`CHANGE_ACTIONS_PROPERTY`](#CHANGE_ACTIONS_PROPERTY) (for backward compatibility) property change event, where old value is old actions list, new value is new actions list.
Overrides:
`[addAction](NMAction.html#addAction(com.nomagic.actions.NMAction))` in class `[NMAction](NMAction.html)`
Parameters:
`action` - the given action to add, parameter can be null.
addActions
public void addActions([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](NMAction.html)> actions)
Adds given actions to the category.
 Fires [`ACTIONS_PROPERTY`](#ACTIONS_PROPERTY) (and [`CHANGE_ACTIONS_PROPERTY`](#CHANGE_ACTIONS_PROPERTY) for backward compatibility) property change event,
 where old value is old actions list, new value is new actions list.
Parameters:
`actions` - the given actions to add, parameter can be null.
addAction
public void addAction(@CheckForNull
 [NMAction](NMAction.html) action,
 int position)
Adds the given action at the specified position to the category.
 Fires [`ADDED_ACTION_PROPERTY`](#ADDED_ACTION_PROPERTY) property change event, where new value is added action.
 Fires [`CHANGE_ACTIONS_PROPERTY`](#CHANGE_ACTIONS_PROPERTY) (for backward compatibility) property change event, where old value is old actions list, new value is new actions list.
Parameters:
`action` - the given action to add, parameter can be null.
`position` - the given position to be added.
addActionNearTheGiven
public void addActionNearTheGiven(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) givenID,
 boolean addAfter,
 @CheckForNull
 [NMAction](NMAction.html) action)
Adds given action near the action with the given id. The given action will be added into the same parent as action with givenID.
 The position of the given action will be above or below the "givenID".
Parameters:
`givenID` - the id of action to add near
`addAfter` - add after or before "givenID"
`action` - the action to add.
removeAction
public void removeAction(@CheckForNull
 [NMAction](NMAction.html) action)
Removes the given action from the category.
 Fires [`REMOVED_ACTION_PROPERTY`](#REMOVED_ACTION_PROPERTY) property change event, where old value is removed action.
 Fires [`CHANGE_ACTIONS_PROPERTY`](#CHANGE_ACTIONS_PROPERTY) (for backward compatibility) property change event, where old value is old actions list, new value is new actions list.
Overrides:
`[removeAction](NMAction.html#removeAction(com.nomagic.actions.NMAction))` in class `[NMAction](NMAction.html)`
Parameters:
`action` - the given action to remove, parameter can be null.
getActions
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NMAction](NMAction.html)> getActions()
Returns the list of the owned actions.
Overrides:
`[getActions](NMAction.html#getActions())` in class `[NMAction](NMAction.html)`
Returns:
the cloned list of the actions.
getCategories
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ActionsCategory](ActionsCategory.html)> getCategories()
Gets inner action categories.
Returns:
a list of action categories.
getActionsRecursively
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NMAction](NMAction.html)> getActionsRecursively(boolean includeCategories)
Returns all simple actions (not ActionsCategory) recursively.
Parameters:
`includeCategories` - If true, then ActionsCategories will be included in the list
Returns:
all actions recursively
setActions
public void setActions([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](NMAction.html)> actions)
Sets the list of the new actions overriding old actions.
 Fires [`ACTIONS_PROPERTY`](#ACTIONS_PROPERTY) (and [`CHANGE_ACTIONS_PROPERTY`](#CHANGE_ACTIONS_PROPERTY) for backward compatibility) property change event,
 where old value is old actions list, new value is new actions list.
Overrides:
`[setActions](NMAction.html#setActions(java.util.List))` in class `[NMAction](NMAction.html)`
Parameters:
`actions` - the new list of the actions.
removeIf
public void removeIf([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[NMAction](NMAction.html)> filter)
Description copied from class: `[NMAction](NMAction.html#removeIf(java.util.function.Predicate))`
Removes all of the owned actions that satisfy the given predicate
Overrides:
`[removeIf](NMAction.html#removeIf(java.util.function.Predicate))` in class `[NMAction](NMAction.html)`
Parameters:
`filter` - given predicate
forEach
public void forEach([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[NMAction](NMAction.html)> consumer)
Description copied from class: `[NMAction](NMAction.html#forEach(java.util.function.Consumer))`
Performs the given consumer for each owned action. Owned actions should not be added/removed inside consumer.
Overrides:
`[forEach](NMAction.html#forEach(java.util.function.Consumer))` in class `[NMAction](NMAction.html)`
Parameters:
`consumer` - the action to be performed for each NMAction
forEachIncludingSelf
public void forEachIncludingSelf([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[NMAction](NMAction.html)> consumer)
Description copied from class: `[NMAction](NMAction.html#forEachIncludingSelf(java.util.function.Consumer))`
Performs the given consumer for each owned action including self. Owned actions should not be added/removed inside consumer.
Overrides:
`[forEachIncludingSelf](NMAction.html#forEachIncludingSelf(java.util.function.Consumer))` in class `[NMAction](NMAction.html)`
Parameters:
`consumer` - the action to be performed for each NMAction
clone
public [ActionsCategory](ActionsCategory.html) clone()
Clones the category. During clone does not fire any property change events.
 Does deep clone.
Overrides:
`[clone](NMAction.html#clone())` in class `[NMAction](NMAction.html)`
Returns:
deep clone of category.
shallowClone
public [ActionsCategory](ActionsCategory.html) shallowClone()
Clones the category. During clone does not fire any property change events.
 Does deep clone.
Overrides:
`[shallowClone](NMAction.html#shallowClone())` in class `[NMAction](NMAction.html)`
Returns:
deep clone of category.
setNested
public void setNested(boolean nested)
Sets new value of nested flag.
 Flag indicates that children of this action is nested elements.
 When representing this action as menu, nested action means new sub menu.
 Not nested means group(usually separated by some menu separator).
Parameters:
`nested` - new value of nested flag.
isNested
public boolean isNested()
Returns value of nested flag.
Returns:
true if this category is nested.
See Also:
[`setNested(boolean)`](#setNested(boolean))
accept
public void accept([ActionsVisitor](ActionsVisitor.html) visitor)
Accepts visitor and calls visit method of visitor.
Overrides:
`[accept](NMAction.html#accept(com.nomagic.actions.ActionsVisitor))` in class `[NMAction](NMAction.html)`
Parameters:
`visitor` - ActionsVisitor.
actionPerformed
public void actionPerformed([ActionEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionEvent.html) e)
Empty implementation.
Specified by:
`[actionPerformed](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html#actionPerformed(java.awt.event.ActionEvent))` in interface `[ActionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html)`
Specified by:
`[actionPerformed](NMAction.html#actionPerformed(java.awt.event.ActionEvent))` in class `[NMAction](NMAction.html)`
Parameters:
`e` - event caused this action execution.
setUseActionForDisable
public void setUseActionForDisable(boolean use)
Parameters:
`use` - if true, menus created from this category will be disabled if all children are disabled.
See Also:
`useActionForDisable`
isUseActionForDisable
public boolean isUseActionForDisable()
Returns value of nested flag.
Returns:
value of mUseActionForDisable field
See Also:
[`(boolean)`](#setUseActionForDisable(boolean))
breakActions
public static void breakActions([ActionsCategory](ActionsCategory.html) category,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NMAction](NMAction.html)> actions)
Breaks given actions into subcategories of given category if the actions number exceeds predefined number.
Parameters:
`category` - category to add created inner categories
`actions` - actions to break into categories
breakeActions
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void breakeActions([ActionsCategory](ActionsCategory.html) category,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](NMAction.html)> actions,
 int maxCategorySize,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) categoryName,
 boolean nested)
Deprecated.
use [`breakActions(ActionsCategory, java.util.List, int, String, boolean)`](#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean))
breakActions
public static void breakActions([ActionsCategory](ActionsCategory.html) category,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](NMAction.html)> actions,
 int maxCategorySize,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) categoryName,
 boolean nested)
Breaks given actions into subcategories of given category if the actions number exceeds maxCategorySize.
Parameters:
`category` - category to add created inner categories
`actions` - actions to break into categories
`maxCategorySize` - max size of inner category
`categoryName` - subcategory name
`nested` - make nested subcategories
breakActions
public static void breakActions([ActionsCategory](ActionsCategory.html) category,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](NMAction.html)> actions,
 int maxCategorySize,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) categoryName,
 boolean nested,
 int innerCategorySize)
Breaks category into sub categories, but it has ability to specify inner category size separately
Parameters:
`category` - category to add created inner categories
`actions` - actions to break into categories
`maxCategorySize` - max size of inner category
`categoryName` - subcategory name
`nested` - make nested subcategories
`innerCategorySize` - maximum size of inner category
sort
public void sort()
getAction
@CheckForNullpublic [NMAction](NMAction.html) getAction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID)
Find direct action with given ID
Parameters:
`actionID` - action ID
Returns:
a list of action categories.
isEmpty
public boolean isEmpty()
Returns:
true if this category contains no actions at all
isDisplayHeader
public boolean isDisplayHeader()
Returns:
display header flag
setDisplayHeader
public void setDisplayHeader(boolean displayHeader)
Display category name as header of category. This has affect only if category is not nested
Parameters:
`displayHeader` - display header of not nested menu
size
public int size()
Size of category - number of inner actions.
Returns:
size of category

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.actions</a></div>
<h1 class="title" title="Class ActionsCategory">Class ActionsCategory</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">javax.swing.AbstractAction</a>
<div class="inheritance"><a href="NMAction.html" title="class in com.nomagic.actions">com.nomagic.actions.NMAction</a>
<div class="inheritance">com.nomagic.actions.ActionsCategory</div>
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
<dd><code><a href="../magicdraw/actions/MDActionsCategory.html" title="class in com.nomagic.magicdraw.actions">MDActionsCategory</a></code>, <code><a href="MenuAction.html" title="class in com.nomagic.actions">MenuAction</a></code>, <code><a href="SelectItemAction.html" title="class in com.nomagic.actions">SelectItemAction</a></code>, <code><a href="SetFontAction.html" title="class in com.nomagic.actions">SetFontAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ActionsCategory</span>
<span class="extends-implements">extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></span></div>
<div class="block">Actions category  owns a list of actions.
 Actions category can represent structure of menu or toolbar, and it can be nested (represents sub menu).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../serialized-form.html#com.nomagic.actions.ActionsCategory">Serialized Form</a></li>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTIONS_PROPERTY">ACTIONS_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Property Change event name fired when actions of this category were changed.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ADDED_ACTION_PROPERTY">ADDED_ACTION_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Property Change event name fired when new action is added.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CHANGE_ACTIONS_PROPERTY">CHANGE_ACTIONS_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#ACTIONS_PROPERTY"><code>ACTIONS_PROPERTY</code></a>, <a href="#ADDED_ACTION_PROPERTY"><code>ADDED_ACTION_PROPERTY</code></a>, <a href="#REMOVED_ACTION_PROPERTY"><code>REMOVED_ACTION_PROPERTY</code></a></div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DISABLE_IF_EMPTY">DISABLE_IF_EMPTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A name of property to disable the category if it has no actions.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MAX_CATEGORY_ACTIONS">MAX_CATEGORY_ACTIONS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default value limiting maximum action count in one category</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REMOVE_IF_EMPTY">REMOVE_IF_EMPTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A name of property to drop the category if it has no actions.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REMOVED_ACTION_PROPERTY">REMOVED_ACTION_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Property Change event name fired when new action is removed.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#USE_AS_SEPARATOR_IN_UI">USE_AS_SEPARATOR_IN_UI</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A name of property to use this category as separator in UI even if it does not have inner actions</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ActionsCategory</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates actions category with no name</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String)">ActionsCategory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates actions category with given name and id.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,int)">ActionsCategory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int keyCode)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates actions category with given id, name, and key code.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.String)">ActionsCategory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int keyCode,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates actions category with given id, name, and key code.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke)">ActionsCategory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates actions category with given id, name, and keystroke.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String)">ActionsCategory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates actions category with given id, name, keystroke and assigned
 group.</div>
</div>
</div>
</section>
</li>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.actions.ActionsVisitor)">accept</a><wbr/>(<a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts visitor and calls visit method of visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionEvent.html" title="class or interface in java.awt.event">ActionEvent</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Empty implementation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAction(com.nomagic.actions.NMAction)">addAction</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the given action to the category.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAction(com.nomagic.actions.NMAction,int)">addAction</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 int position)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the given action at the specified position to the category.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction)">addActionNearTheGiven</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> givenID,
 boolean addAfter,
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds given action near the action with the given id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addActions(java.util.List)">addActions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds given actions to the category.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)">breakActions</a><wbr/>(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions,
 int maxCategorySize,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> categoryName,
 boolean nested)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Breaks given actions into subcategories of given category if the actions number exceeds maxCategorySize.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean,int)">breakActions</a><wbr/>(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions,
 int maxCategorySize,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> categoryName,
 boolean nested,
 int innerCategorySize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Breaks category into sub categories, but it has ability to specify inner category size separately</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#breakActions(com.nomagic.actions.ActionsCategory,java.util.List)">breakActions</a><wbr/>(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Breaks given actions into subcategories of given category if the actions number exceeds predefined number.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#breakeActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)">breakeActions</a><wbr/>(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions,
 int maxCategorySize,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> categoryName,
 boolean nested)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)"><code>breakActions(ActionsCategory, java.util.List, int, String, boolean)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the category.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSeparatorCategory()">createSeparatorCategory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#forEach(java.util.function.Consumer)">forEach</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; consumer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs the given consumer for each owned action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; consumer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs the given consumer for each owned action including self.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAction(java.lang.String)">getAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find direct action with given ID</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActions()">getActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the list of the owned actions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActionsRecursively(boolean)">getActionsRecursively</a><wbr/>(boolean includeCategories)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all simple actions (not ActionsCategory) recursively.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCategories()">getCategories</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets inner action categories.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisplayHeader()">isDisplayHeader</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEmpty()">isEmpty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNested()">isNested</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns value of nested flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseActionForDisable()">isUseActionForDisable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns value of nested flag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAction(com.nomagic.actions.NMAction)">removeAction</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the given action from the category.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeIf(java.util.function.Predicate)">removeIf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; filter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all of the owned actions that satisfy the given predicate</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setActions(java.util.List)">setActions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the list of the new actions overriding old actions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayHeader(boolean)">setDisplayHeader</a><wbr/>(boolean displayHeader)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Display category name as header of category.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNested(boolean)">setNested</a><wbr/>(boolean nested)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new value of nested flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseActionForDisable(boolean)">setUseActionForDisable</a><wbr/>(boolean use)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#shallowClone()">shallowClone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the category.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#size()">size</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Size of category - number of inner actions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sort()">sort</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.NMAction">Methods inherited from class com.nomagic.actions.<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="NMAction.html#addShortcut(javax.swing.KeyStroke)">addShortcut</a>, <a href="NMAction.html#addShotcut(javax.swing.KeyStroke)">addShotcut</a>, <a href="NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)">addWeakPropertyChangeListener</a>, <a href="NMAction.html#compareTo(java.lang.Object)">compareTo</a>, <a href="NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)">createMenuItem</a>, <a href="NMAction.html#equals(java.lang.Object)">equals</a>, <a href="NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="NMAction.html#getCommandKey()">getCommandKey</a>, <a href="NMAction.html#getDescription()">getDescription</a>, <a href="NMAction.html#getGroup()">getGroup</a>, <a href="NMAction.html#getIcon()">getIcon</a>, <a href="NMAction.html#getID()">getID</a>, <a href="NMAction.html#getLargeIcon()">getLargeIcon</a>, <a href="NMAction.html#getLargeOrSmallIcon()">getLargeOrSmallIcon</a>, <a href="NMAction.html#getMenuShortcutMaskAsString()">getMenuShortcutMaskAsString</a>, <a href="NMAction.html#getMnemonicKey()">getMnemonicKey</a>, <a href="NMAction.html#getName()">getName</a>, <a href="NMAction.html#getPropertyChangeListeners()">getPropertyChangeListeners</a>, <a href="NMAction.html#getShortcuts()">getShortcuts</a>, <a href="NMAction.html#getSmallIcon()">getSmallIcon</a>, <a href="NMAction.html#getSmallOrLargeIcon()">getSmallOrLargeIcon</a>, <a href="NMAction.html#getTinyIcon()">getTinyIcon</a>, <a href="NMAction.html#hashCode()">hashCode</a>, <a href="NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)">hasMenuShortcutMask</a>, <a href="NMAction.html#isIDGenerated()">isIDGenerated</a>, <a href="NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="NMAction.html#removeShortcut(javax.swing.KeyStroke)">removeShortcut</a>, <a href="NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)">removeWeakPropertyChangeListener</a>, <a href="NMAction.html#setDescription(java.lang.String)">setDescription</a>, <a href="NMAction.html#setGroup(java.lang.String)">setGroup</a>, <a href="NMAction.html#setIcon(javax.swing.Icon)">setIcon</a>, <a href="NMAction.html#setLargeIcon(javax.swing.Icon)">setLargeIcon</a>, <a href="NMAction.html#setMnemonicKey(int)">setMnemonicKey</a>, <a href="NMAction.html#setName(java.lang.String)">setName</a>, <a href="NMAction.html#setShortcuts(java.util.List)">setShortcuts</a>, <a href="NMAction.html#setSmallIcon(javax.swing.Icon)">setSmallIcon</a>, <a href="NMAction.html#setTinyIcon(javax.swing.Icon)">setTinyIcon</a>, <a href="NMAction.html#toString()">toString</a>, <a href="NMAction.html#updateState()">updateState</a></code></div>
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
<section class="detail" id="USE_AS_SEPARATOR_IN_UI">
<h3>USE_AS_SEPARATOR_IN_UI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">USE_AS_SEPARATOR_IN_UI</span></div>
<div class="block">A name of property to use this category as separator in UI even if it does not have inner actions</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.ActionsCategory.USE_AS_SEPARATOR_IN_UI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DISABLE_IF_EMPTY">
<h3>DISABLE_IF_EMPTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DISABLE_IF_EMPTY</span></div>
<div class="block">A name of property to disable the category if it has no actions.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.ActionsCategory.DISABLE_IF_EMPTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REMOVE_IF_EMPTY">
<h3>REMOVE_IF_EMPTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REMOVE_IF_EMPTY</span></div>
<div class="block">A name of property to drop the category if it has no actions.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.ActionsCategory.REMOVE_IF_EMPTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MAX_CATEGORY_ACTIONS">
<h3>MAX_CATEGORY_ACTIONS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">MAX_CATEGORY_ACTIONS</span></div>
<div class="block">Default value limiting maximum action count in one category</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.ActionsCategory.MAX_CATEGORY_ACTIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ADDED_ACTION_PROPERTY">
<h3>ADDED_ACTION_PROPERTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ADDED_ACTION_PROPERTY</span></div>
<div class="block">Property Change event name fired when new action is added.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#addAction(com.nomagic.actions.NMAction)"><code>addAction(NMAction)</code></a></li>
<li><a href="#addAction(com.nomagic.actions.NMAction,int)"><code>addAction(NMAction, int)</code></a></li>
<li><a href="../../../constant-values.html#com.nomagic.actions.ActionsCategory.ADDED_ACTION_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REMOVED_ACTION_PROPERTY">
<h3>REMOVED_ACTION_PROPERTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REMOVED_ACTION_PROPERTY</span></div>
<div class="block">Property Change event name fired when new action is removed.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#removeAction(com.nomagic.actions.NMAction)"><code>removeAction(NMAction)</code></a></li>
<li><a href="../../../constant-values.html#com.nomagic.actions.ActionsCategory.REMOVED_ACTION_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTIONS_PROPERTY">
<h3>ACTIONS_PROPERTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACTIONS_PROPERTY</span></div>
<div class="block">Property Change event name fired when actions of this category were changed.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#setActions(java.util.List)"><code>setActions(List)</code></a></li>
<li><a href="../../../constant-values.html#com.nomagic.actions.ActionsCategory.ACTIONS_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CHANGE_ACTIONS_PROPERTY">
<h3>CHANGE_ACTIONS_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CHANGE_ACTIONS_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#ACTIONS_PROPERTY"><code>ACTIONS_PROPERTY</code></a>, <a href="#ADDED_ACTION_PROPERTY"><code>ADDED_ACTION_PROPERTY</code></a>, <a href="#REMOVED_ACTION_PROPERTY"><code>REMOVED_ACTION_PROPERTY</code></a></div>
</div>
<div class="block">Property Change event name fired when actions of this category were changed.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.ActionsCategory.CHANGE_ACTIONS_PROPERTY">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;()">
<h3>ActionsCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ActionsCategory</span>()</div>
<div class="block">Creates actions category with no name</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String)">
<h3>ActionsCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ActionsCategory</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Creates actions category with given name and id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the id of the category.</dd>
<dd><code>name</code> - the name of the category.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,javax.swing.KeyStroke)">
<h3>ActionsCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ActionsCategory</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke)</span></div>
<div class="block">Creates actions category with given id, name, and keystroke.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the id of the category.</dd>
<dd><code>name</code> - the name of the category.</dd>
<dd><code>stroke</code> - keystroke used for invoking action category.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String)">
<h3>ActionsCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ActionsCategory</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Creates actions category with given id, name, keystroke and assigned
 group.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the id of the category.</dd>
<dd><code>name</code> - the name of the category.</dd>
<dd><code>stroke</code> - keystroke used for invoking action category.</dd>
<dd><code>group</code> - the name of the related commands group.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,int)">
<h3>ActionsCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ActionsCategory</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int keyCode)</span></div>
<div class="block">Creates actions category with given id, name, and key code.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the id of the category.</dd>
<dd><code>name</code> - the name of the category.</dd>
<dd><code>keyCode</code> - keystroke used for invoking action category.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,int,java.lang.String)">
<h3>ActionsCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ActionsCategory</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int keyCode,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Creates actions category with given id, name, and key code.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the id of the category.</dd>
<dd><code>name</code> - the name of the category.</dd>
<dd><code>keyCode</code> - keystroke used for invoking action category.</dd>
<dd><code>group</code> - the name of the related commands group.</dd>
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
<section class="detail" id="createSeparatorCategory()">
<h3>createSeparatorCategory</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></span> <span class="element-name">createSeparatorCategory</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addAction(com.nomagic.actions.NMAction)">
<h3>addAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Adds the given action to the category.
 Fires <a href="#ADDED_ACTION_PROPERTY"><code>ADDED_ACTION_PROPERTY</code></a> property change event, where new value is added action.
 Fires <a href="#CHANGE_ACTIONS_PROPERTY"><code>CHANGE_ACTIONS_PROPERTY</code></a> (for backward compatibility) property change event, where old value is old actions list, new value is new actions list.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="NMAction.html#addAction(com.nomagic.actions.NMAction)">addAction</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>action</code> - the given action to add, parameter can be null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addActions(java.util.List)">
<h3>addActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addActions</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
<div class="block">Adds given actions to the category.
 Fires <a href="#ACTIONS_PROPERTY"><code>ACTIONS_PROPERTY</code></a> (and <a href="#CHANGE_ACTIONS_PROPERTY"><code>CHANGE_ACTIONS_PROPERTY</code></a> for backward compatibility) property change event,
 where old value is old actions list, new value is new actions list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actions</code> - the given actions to add, parameter can be null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAction(com.nomagic.actions.NMAction,int)">
<h3>addAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 int position)</span></div>
<div class="block">Adds the given action at the specified position to the category.
 Fires <a href="#ADDED_ACTION_PROPERTY"><code>ADDED_ACTION_PROPERTY</code></a> property change event, where new value is added action.
 Fires <a href="#CHANGE_ACTIONS_PROPERTY"><code>CHANGE_ACTIONS_PROPERTY</code></a> (for backward compatibility) property change event, where old value is old actions list, new value is new actions list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - the given action to add, parameter can be null.</dd>
<dd><code>position</code> - the given position to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction)">
<h3>addActionNearTheGiven</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addActionNearTheGiven</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> givenID,
 boolean addAfter,
 @CheckForNull
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Adds given action near the action with the given id. The given action will be added into the same parent as action with givenID.
 The position of the given action will be above or below the "givenID".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>givenID</code> - the id of action to add near</dd>
<dd><code>addAfter</code> - add after or before "givenID"</dd>
<dd><code>action</code> - the action to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAction(com.nomagic.actions.NMAction)">
<h3>removeAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Removes the given action from the category.
 Fires <a href="#REMOVED_ACTION_PROPERTY"><code>REMOVED_ACTION_PROPERTY</code></a> property change event, where old value is removed action.
 Fires <a href="#CHANGE_ACTIONS_PROPERTY"><code>CHANGE_ACTIONS_PROPERTY</code></a> (for backward compatibility) property change event, where old value is old actions list, new value is new actions list.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="NMAction.html#removeAction(com.nomagic.actions.NMAction)">removeAction</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>action</code> - the given action to remove, parameter can be null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActions()">
<h3>getActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</span> <span class="element-name">getActions</span>()</div>
<div class="block">Returns the list of the owned actions.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="NMAction.html#getActions()">getActions</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Returns:</dt>
<dd>the cloned list of the actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCategories()">
<h3>getCategories</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a>&gt;</span> <span class="element-name">getCategories</span>()</div>
<div class="block">Gets inner action categories.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of action categories.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActionsRecursively(boolean)">
<h3>getActionsRecursively</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</span> <span class="element-name">getActionsRecursively</span><wbr/><span class="parameters">(boolean includeCategories)</span></div>
<div class="block">Returns all simple actions (not ActionsCategory) recursively.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>includeCategories</code> - If true, then ActionsCategories will be included in the list</dd>
<dt>Returns:</dt>
<dd>all actions recursively</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActions(java.util.List)">
<h3>setActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActions</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
<div class="block">Sets the list of the new actions overriding old actions.
 Fires <a href="#ACTIONS_PROPERTY"><code>ACTIONS_PROPERTY</code></a> (and <a href="#CHANGE_ACTIONS_PROPERTY"><code>CHANGE_ACTIONS_PROPERTY</code></a> for backward compatibility) property change event,
 where old value is old actions list, new value is new actions list.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="NMAction.html#setActions(java.util.List)">setActions</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>actions</code> - the new list of the actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeIf(java.util.function.Predicate)">
<h3>removeIf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeIf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; filter)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="NMAction.html#removeIf(java.util.function.Predicate)">NMAction</a></code></span></div>
<div class="block">Removes all of the owned actions that satisfy the given predicate</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="NMAction.html#removeIf(java.util.function.Predicate)">removeIf</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>filter</code> - given predicate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="forEach(java.util.function.Consumer)">
<h3>forEach</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">forEach</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; consumer)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="NMAction.html#forEach(java.util.function.Consumer)">NMAction</a></code></span></div>
<div class="block">Performs the given consumer for each owned action. Owned actions should not be added/removed inside consumer.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="NMAction.html#forEach(java.util.function.Consumer)">forEach</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>consumer</code> - the action to be performed for each NMAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="forEachIncludingSelf(java.util.function.Consumer)">
<h3>forEachIncludingSelf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">forEachIncludingSelf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; consumer)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="NMAction.html#forEachIncludingSelf(java.util.function.Consumer)">NMAction</a></code></span></div>
<div class="block">Performs the given consumer for each owned action including self. Owned actions should not be added/removed inside consumer.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="NMAction.html#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>consumer</code> - the action to be performed for each NMAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></span> <span class="element-name">clone</span>()</div>
<div class="block">Clones the category. During clone does not fire any property change events.
 Does deep clone.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="NMAction.html#clone()">clone</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Returns:</dt>
<dd>deep clone of category.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="shallowClone()">
<h3>shallowClone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></span> <span class="element-name">shallowClone</span>()</div>
<div class="block">Clones the category. During clone does not fire any property change events.
 Does deep clone.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="NMAction.html#shallowClone()">shallowClone</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Returns:</dt>
<dd>deep clone of category.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNested(boolean)">
<h3>setNested</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNested</span><wbr/><span class="parameters">(boolean nested)</span></div>
<div class="block">Sets new value of nested flag.
 Flag indicates that children of this action is nested elements.
 When representing this action as menu, nested action means new sub menu.
 Not nested means group(usually separated by some menu separator).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>nested</code> - new value of nested flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNested()">
<h3>isNested</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNested</span>()</div>
<div class="block">Returns value of nested flag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this category is nested.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#setNested(boolean)"><code>setNested(boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.actions.ActionsVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a> visitor)</span></div>
<div class="block">Accepts visitor and calls visit method of visitor.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="NMAction.html#accept(com.nomagic.actions.ActionsVisitor)">accept</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - ActionsVisitor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="actionPerformed(java.awt.event.ActionEvent)">
<h3>actionPerformed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">actionPerformed</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionEvent.html" title="class or interface in java.awt.event">ActionEvent</a> e)</span></div>
<div class="block">Empty implementation.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html#actionPerformed(java.awt.event.ActionEvent)" title="class or interface in java.awt.event">actionPerformed</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="NMAction.html#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a></code> in class <code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>e</code> - event caused this action execution.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseActionForDisable(boolean)">
<h3>setUseActionForDisable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseActionForDisable</span><wbr/><span class="parameters">(boolean use)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>use</code> - if true, menus created from this category will be disabled if all children are disabled.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><code>useActionForDisable</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseActionForDisable()">
<h3>isUseActionForDisable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseActionForDisable</span>()</div>
<div class="block">Returns value of nested flag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value of mUseActionForDisable field</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#setUseActionForDisable(boolean)"><code>(boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="breakActions(com.nomagic.actions.ActionsCategory,java.util.List)">
<h3>breakActions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">breakActions</span><wbr/><span class="parameters">(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
<div class="block">Breaks given actions into subcategories of given category if the actions number exceeds predefined number.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - category to add created inner categories</dd>
<dd><code>actions</code> - actions to break into categories</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="breakeActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)">
<h3>breakeActions</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">breakeActions</span><wbr/><span class="parameters">(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions,
 int maxCategorySize,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> categoryName,
 boolean nested)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)"><code>breakActions(ActionsCategory, java.util.List, int, String, boolean)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean)">
<h3>breakActions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">breakActions</span><wbr/><span class="parameters">(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions,
 int maxCategorySize,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> categoryName,
 boolean nested)</span></div>
<div class="block">Breaks given actions into subcategories of given category if the actions number exceeds maxCategorySize.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - category to add created inner categories</dd>
<dd><code>actions</code> - actions to break into categories</dd>
<dd><code>maxCategorySize</code> - max size of inner category</dd>
<dd><code>categoryName</code> - subcategory name</dd>
<dd><code>nested</code> - make nested subcategories</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="breakActions(com.nomagic.actions.ActionsCategory,java.util.List,int,java.lang.String,boolean,int)">
<h3>breakActions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">breakActions</span><wbr/><span class="parameters">(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions,
 int maxCategorySize,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> categoryName,
 boolean nested,
 int innerCategorySize)</span></div>
<div class="block">Breaks category into sub categories, but it has ability to specify inner category size separately</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - category to add created inner categories</dd>
<dd><code>actions</code> - actions to break into categories</dd>
<dd><code>maxCategorySize</code> - max size of inner category</dd>
<dd><code>categoryName</code> - subcategory name</dd>
<dd><code>nested</code> - make nested subcategories</dd>
<dd><code>innerCategorySize</code> - maximum size of inner category</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sort()">
<h3>sort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sort</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAction(java.lang.String)">
<h3>getAction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></span> <span class="element-name">getAction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID)</span></div>
<div class="block">Find direct action with given ID</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionID</code> - action ID</dd>
<dt>Returns:</dt>
<dd>a list of action categories.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEmpty()">
<h3>isEmpty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEmpty</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this category contains no actions at all</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDisplayHeader()">
<h3>isDisplayHeader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisplayHeader</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>display header flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisplayHeader(boolean)">
<h3>setDisplayHeader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisplayHeader</span><wbr/><span class="parameters">(boolean displayHeader)</span></div>
<div class="block">Display category name as header of category. This has affect only if category is not nested</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>displayHeader</code> - display header of not nested menu</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="size()">
<h3>size</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">size</span>()</div>
<div class="block">Size of category - number of inner actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>size of category</dd>
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
