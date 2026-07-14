# JAVA OPENAPI: NMAction (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/actions/NMAction.html
- source_path: `com/nomagic/actions/NMAction.html`
- source_sha256: `2f6a324ae5db26e41072f45579856c61f6a06b9808931c1fd1eaf37afed2f236`
- captured_utc: `2026-07-14T16:50:59.086909+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.actions](package-summary.html)

## Class NMAction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[javax.swing.AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
com.nomagic.actions.NMAction

All Implemented Interfaces:
`[ActionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`, `[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)`

Direct Known Subclasses:
`[ActionsCategory](ActionsCategory.html)`, `[BaseNMStateAction](BaseNMStateAction.html)`, `[ColorChooseAction](ColorChooseAction.html)`, `[MDAction](../magicdraw/actions/MDAction.html)`

@OpenApiAllpublic abstract classNMAction
extends [AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
implements [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)

The class describes some abstract action.
 Any specific action must implement actionPerformed() method.
 The action has such properties: name, id,small icon,large icon,some shortcuts,mnemonic, description, group

See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.actions.NMAction)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ACTION_SHORTCUTS](#ACTION_SHORTCUTS)`
Key for storing command keys.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BELONGS_TO_SEPARATE_GROUP_IN_UI](#BELONGS_TO_SEPARATE_GROUP_IN_UI)`
A name of property to put this action into a dedicate special group.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DO_NO_SHOW_ACTION_NAME_IN_UI](#DO_NO_SHOW_ACTION_NAME_IN_UI)`
A name of property to hide action name text in create UI.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DO_NOT_REGISTER_ACTION_TO_COMPONENTS](#DO_NOT_REGISTER_ACTION_TO_COMPONENTS)`
A name of property to skip registering this action to components.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[GENERATED_ID_PREFIX](#GENERATED_ID_PREFIX)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[GROUP](#GROUP)`
Key for storing group.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ID](#ID)`
Key for storing id.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LARGE_ICON](#LARGE_ICON)`
Key for storing large icon.
`static final int`
`[MENU_SHORTCUT_MASK](#MENU_SHORTCUT_MASK)`
Menu shortcut mask used to create shortcuts.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TINY_ICON](#TINY_ICON)`
Key for storing tiny icon (smaller than small icon).
Fields inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[changeSupport](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#changeSupport), [enabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#enabled)`
Fields inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[ACCELERATOR_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACCELERATOR_KEY), [ACTION_COMMAND_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACTION_COMMAND_KEY), [DEFAULT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DEFAULT), [DISPLAYED_MNEMONIC_INDEX_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DISPLAYED_MNEMONIC_INDEX_KEY), [LARGE_ICON_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LARGE_ICON_KEY), [LONG_DESCRIPTION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LONG_DESCRIPTION), [MNEMONIC_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#MNEMONIC_KEY), [NAME](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#NAME), [SELECTED_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SELECTED_KEY), [SHORT_DESCRIPTION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SHORT_DESCRIPTION), [SMALL_ICON](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SMALL_ICON)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[NMAction](#%3Cinit%3E())()`
Constructs the action with nulls.
`[NMAction](#%3Cinit%3E(java.lang.String,java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int mnemonic)`
Constructs the action with given id, name, mnemonic key.
`[NMAction](#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int mnemonic,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`
Constructs the action with given id, name, mnemonic key and group.
`[NMAction](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke)`
Constructs the action with given id, name, keystroke.
`[NMAction](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`
Constructs the action with given id, name, keystroke and group.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.actions.ActionsVisitor))([ActionsVisitor](ActionsVisitor.html) visitor)`
Accepts ActionsVisitor using Visitor pattern.
`abstract void`
`[actionPerformed](#actionPerformed(java.awt.event.ActionEvent))([ActionEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionEvent.html) e)`
Executes given action.
`void`
`[addAction](#addAction(com.nomagic.actions.NMAction))([NMAction](NMAction.html) action)`
Adds action.
`void`
`[addPropertyChangeListener](#addPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Adds a `PropertyChangeListener` to the listener list.
`void`
`[addShortcut](#addShortcut(javax.swing.KeyStroke))([KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) key)`
Adds the shortcut to the action.
`void`
`[addShotcut](#addShotcut(javax.swing.KeyStroke))([KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) key)`
Deprecated.
type error.
`void`
`[addWeakPropertyChangeListener](#addWeakPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Adds a `PropertyChangeListener` to the weak listener list.
`[NMAction](NMAction.html)`
`[clone](#clone())()`
Clones the object.
`int`
`[compareTo](#compareTo(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`
Compares the name of the action.
`[JMenuItem](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html)`
`[createMenuItem](#createMenuItem(com.nomagic.actions.MenuComponentFactory))(com.nomagic.actions.MenuComponentFactory factory)`
Action can return preferred representation of itself as menu item.
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`
Checks if given object is equal to the current action.
`protected void`
`[firePropertyChange](#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)`
Supports reporting bound property changes.
`void`
`[forEach](#forEach(java.util.function.Consumer))([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[NMAction](NMAction.html)> consumer)`
Performs the given consumer for each owned action.
`void`
`[forEachIncludingSelf](#forEachIncludingSelf(java.util.function.Consumer))([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[NMAction](NMAction.html)> consumer)`
Performs the given consumer for each owned action including self.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NMAction](NMAction.html)>`
`[getActions](#getActions())()`
Returns the list of the actions.
`[KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html)`
`[getCommandKey](#getCommandKey())()`
Returns the shortcut of the action.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription())()`
Returns description of this action.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getGroup](#getGroup())()`
Returns the name of the related actions group.
`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getIcon](#getIcon())()`
Deprecated.
use {link #getSmallOrLargeIcon}
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getID](#getID())()`
Returns the id of the action.
`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getLargeIcon](#getLargeIcon())()`
Returns the large icon of the action.
`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getLargeOrSmallIcon](#getLargeOrSmallIcon())()`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getMenuShortcutMaskAsString](#getMenuShortcutMaskAsString())()`

`int`
`[getMnemonicKey](#getMnemonicKey())()`
Returns the mnemonic of the action.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Returns the name of the action.
`[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)[]`
`[getPropertyChangeListeners](#getPropertyChangeListeners())()`
Returns an array of all the `PropertyChangeListener`s added
 to this action with addPropertyChangeListener().
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html)>`
`[getShortcuts](#getShortcuts())()`
Returns all shortcuts of the the action.
`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getSmallIcon](#getSmallIcon())()`
Returns the small icon of the action.
`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getSmallOrLargeIcon](#getSmallOrLargeIcon())()`

`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getTinyIcon](#getTinyIcon())()`
Returns the tiny icon of the action.
`int`
`[hashCode](#hashCode())()`
Creates hashcode from id.
`static boolean`
`[hasMenuShortcutMask](#hasMenuShortcutMask(java.awt.AWTEvent))([AWTEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html) event)`
Check if event has menu shortcut mask modifier
`boolean`
`[isIDGenerated](#isIDGenerated())()`
Returns true if id was generated.
`void`
`[removeAction](#removeAction(com.nomagic.actions.NMAction))([NMAction](NMAction.html) action)`
Remove action.
`void`
`[removeIf](#removeIf(java.util.function.Predicate))([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[NMAction](NMAction.html)> filter)`
Removes all of the owned actions that satisfy the given predicate
`void`
`[removePropertyChangeListener](#removePropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Removes a `PropertyChangeListener` from the listener list.
`void`
`[removeShortcut](#removeShortcut(javax.swing.KeyStroke))([KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) key)`
Removes the shortcut from the action.
`void`
`[removeWeakPropertyChangeListener](#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Removes a `PropertyChangeListener` from the weak listener list.
`void`
`[setActions](#setActions(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](NMAction.html)> actions)`
Sets the list of the actions(do nothing here).
`void`
`[setDescription](#setDescription(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)`
Sets new action description.
`protected void`
`[setGroup](#setGroup(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`
Sets new group for this action.
`void`
`[setIcon](#setIcon(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Sets small and large icon.
`void`
`[setLargeIcon](#setLargeIcon(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Sets the large icon of the action.
`void`
`[setMnemonicKey](#setMnemonicKey(int))(int key)`
Sets the mnemonic key of the action.
`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Sets new name of action, method implemented by putting value with key Action.NAME
`void`
`[setShortcuts](#setShortcuts(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html)> shortcuts)`
Sets the shortcuts list.
`void`
`[setSmallIcon](#setSmallIcon(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Sets the small icon of the action.
`void`
`[setTinyIcon](#setTinyIcon(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Sets the tiny icon of the action.
`[NMAction](NMAction.html)`
`[shallowClone](#shallowClone())()`
Returns itself
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
toString returns the action's name.
`void`
`[updateState](#updateState())()`
Method should update action state (enabled or disabled, checked or unchecked).
Methods inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[getKeys](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()), [getValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)), [isEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()), [putValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)), [setEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[accept](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object))`

============ FIELD DETAIL =========== 
Field Details
DO_NO_SHOW_ACTION_NAME_IN_UI
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DO_NO_SHOW_ACTION_NAME_IN_UI
A name of property to hide action name text in create UI. For example buttons will not show name of this action as text
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.NMAction.DO_NO_SHOW_ACTION_NAME_IN_UI)
BELONGS_TO_SEPARATE_GROUP_IN_UI
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BELONGS_TO_SEPARATE_GROUP_IN_UI
A name of property to put this action into a dedicate special group. For example Options action can be in the right side of horizontal toolbar.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.NMAction.BELONGS_TO_SEPARATE_GROUP_IN_UI)
DO_NOT_REGISTER_ACTION_TO_COMPONENTS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DO_NOT_REGISTER_ACTION_TO_COMPONENTS
A name of property to skip registering this action to components.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.NMAction.DO_NOT_REGISTER_ACTION_TO_COMPONENTS)
ACTION_SHORTCUTS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ACTION_SHORTCUTS
Key for storing command keys.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.NMAction.ACTION_SHORTCUTS)
ID
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ID
Key for storing id.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.NMAction.ID)
LARGE_ICON
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LARGE_ICON
Key for storing large icon.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.NMAction.LARGE_ICON)
TINY_ICON
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TINY_ICON
Key for storing tiny icon (smaller than small icon).
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.NMAction.TINY_ICON)
GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) GROUP
Key for storing group.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.NMAction.GROUP)
MENU_SHORTCUT_MASK
public static final int MENU_SHORTCUT_MASK
Menu shortcut mask used to create shortcuts.
GENERATED_ID_PREFIX
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) GENERATED_ID_PREFIX
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.NMAction.GENERATED_ID_PREFIX)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
NMAction
public NMAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
Constructs the action with given id, name, keystroke and group.
Parameters:
`id` - the id of the action.
`name` - the name of the action.
`stroke` - the KeyStroke of the action.
`group` - the name of the related commands group.
NMAction
public NMAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke)
Constructs the action with given id, name, keystroke.
Parameters:
`id` - the id of the action.
`name` - the name of the action.
`stroke` - the KeyStroke of the action.
NMAction
public NMAction()
Constructs the action with nulls.
NMAction
public NMAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int mnemonic,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
Constructs the action with given id, name, mnemonic key and group.
Parameters:
`id` - the id of the action.
`name` - the name of the action.
`mnemonic` - the mnemonic key of the action
`group` - the name of the related commands group.
NMAction
public NMAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 int mnemonic)
Constructs the action with given id, name, mnemonic key.
Parameters:
`id` - the id of the action.
`name` - the name of the action.
`mnemonic` - the mnemonic key of the action
 ============ METHOD DETAIL ========== 
Method Details
setName
public void setName(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Sets new name of action, method implemented by putting value with key Action.NAME
Parameters:
`name` - name
getID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getID()
Returns the id of the action.
Returns:
the id of the action.
getCommandKey
@CheckForNullpublic [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) getCommandKey()
Returns the shortcut of the action.
Returns:
the first shortcut from all available shortcuts, null if no shortcuts are defined.
addShotcut
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void addShotcut(@CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) key)
Deprecated.
type error. Use [`addShortcut(KeyStroke)`](#addShortcut(javax.swing.KeyStroke))
Adds the shortcut to the action.
Parameters:
`key` - the given shortcut.
addShortcut
public void addShortcut(@CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) key)
Adds the shortcut to the action.
Parameters:
`key` - the given shortcut.
removeShortcut
public void removeShortcut(@CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) key)
Removes the shortcut from the action.
Parameters:
`key` - the given shortcut.
setShortcuts
public void setShortcuts(@CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html)> shortcuts)
Sets the shortcuts list.
Parameters:
`shortcuts` - the list of all shortcuts.
getShortcuts
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html)> getShortcuts()
Returns all shortcuts of the the action.
Returns:
the list of all shortcuts. List is unmodifiable.
getName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Returns the name of the action.
Returns:
the name of the action.
setMnemonicKey
public void setMnemonicKey(int key)
Sets the mnemonic key of the action.
Parameters:
`key` - the mnemonic key of the action.
getMnemonicKey
public int getMnemonicKey()
Returns the mnemonic of the action.
Returns:
the mnemonic of the action or -1 if command does not have mnemonic.
setIcon
public void setIcon(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Sets small and large icon.
Parameters:
`icon` - Icon of the action.
setSmallIcon
public void setSmallIcon(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Sets the small icon of the action.
Parameters:
`icon` - the small icon of the action.
getSmallIcon
@CheckForNullpublic [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getSmallIcon()
Returns the small icon of the action.
Returns:
the small icon of the action.
setTinyIcon
public void setTinyIcon(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Sets the tiny icon of the action.
Parameters:
`icon` - the tiny icon of the action
getTinyIcon
@CheckForNullpublic [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getTinyIcon()
Returns the tiny icon of the action.
Returns:
the tiny icon of the action.
getIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getIcon()
Deprecated.
use {link #getSmallOrLargeIcon}
setLargeIcon
public void setLargeIcon(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Sets the large icon of the action.
Parameters:
`icon` - the large icon of the action.
getLargeIcon
@CheckForNullpublic [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getLargeIcon()
Returns the large icon of the action.
Returns:
the large icon of the action.
getLargeOrSmallIcon
@CheckForNullpublic [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getLargeOrSmallIcon()
Returns:
large icon if present. If not, small one
getSmallOrLargeIcon
@CheckForNullpublic [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getSmallOrLargeIcon()
Returns:
small icon if present. If not, large one
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Checks if given object is equal to the current action.
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
true if given object is NMAction and id of the given action is the same as id of current action.
hashCode
public int hashCode()
Creates hashcode from id.
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
hash code of action.
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
toString returns the action's name.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
the name.
actionPerformed
public abstract void actionPerformed(@CheckForNull
 [ActionEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionEvent.html) e)
Executes given action.
Specified by:
`[actionPerformed](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html#actionPerformed(java.awt.event.ActionEvent))` in interface `[ActionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html)`
Parameters:
`e` - event caused execution.
compareTo
public int compareTo([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Compares the name of the action. Uses String.compareTo method.
Specified by:
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))` in interface `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`
Parameters:
`o` - the given object to compare to.
Returns:
name comparison result
clone
public [NMAction](NMAction.html) clone()
Clones the object.
 Does the deep clone.
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#clone())` in class `[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)`
Returns:
cloned object
shallowClone
public [NMAction](NMAction.html) shallowClone()
Returns itself
Returns:
itself here
accept
public void accept([ActionsVisitor](ActionsVisitor.html) visitor)
Accepts ActionsVisitor using Visitor pattern.
Parameters:
`visitor` - visitor to accept.
setDescription
public void setDescription(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)
Sets new action description.
Parameters:
`description` - action description.
getDescription
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescription()
Returns description of this action.
Returns:
action description.
setGroup
protected void setGroup(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
Sets new group for this action. Empty string will be converted to null.
Parameters:
`group` - group name.
getGroup
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getGroup()
Returns the name of the related actions group.
Returns:
the name of the related actions group.
getActions
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NMAction](NMAction.html)> getActions()
Returns the list of the actions.
Returns:
empty list here. Some derived classes may override this method.
forEach
public void forEach([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[NMAction](NMAction.html)> consumer)
Performs the given consumer for each owned action. Owned actions should not be added/removed inside consumer.
Parameters:
`consumer` - the action to be performed for each NMAction
forEachIncludingSelf
public void forEachIncludingSelf([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[NMAction](NMAction.html)> consumer)
Performs the given consumer for each owned action including self. Owned actions should not be added/removed inside consumer.
Parameters:
`consumer` - the action to be performed for each NMAction
setActions
public void setActions([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](NMAction.html)> actions)
Sets the list of the actions(do nothing here).
Parameters:
`actions` - the list of the actions.
addAction
public void addAction([NMAction](NMAction.html) action)
Adds action. Not supported here.
Parameters:
`action` - the action to add.
removeAction
public void removeAction([NMAction](NMAction.html) action)
Remove action. Not supported here.
Parameters:
`action` - the action to remove.
removeIf
public void removeIf([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[NMAction](NMAction.html)> filter)
Removes all of the owned actions that satisfy the given predicate
Parameters:
`filter` - given predicate
updateState
public void updateState()
Method should update action state (enabled or disabled, checked or unchecked).
 Method is called after other actions was executed.
 Always enable here.
addPropertyChangeListener
public void addPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Adds a `PropertyChangeListener` to the listener list.
 The listener is registered for all properties.
 A `PropertyChangeEvent` will get fired in response to setting
 a bound property, e.g. `setFont`, `setBackground`,
 or `setForeground`.
 Note that if the current component is inheriting its foreground,
 background, or font from its container, then no event will be
 fired in response to a change in the inherited property.
 This method creates advanced SwingPropertyChangeSupport which is safe to use when
 removing/adding listeners during firing property change event.
Specified by:
`[addPropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#addPropertyChangeListener(java.beans.PropertyChangeListener))` in interface `[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)`
Overrides:
`[addPropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener))` in class `[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)`
Parameters:
`listener` - The `PropertyChangeListener` to be added
See Also:
[`Action.addPropertyChangeListener(java.beans.PropertyChangeListener)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#addPropertyChangeListener(java.beans.PropertyChangeListener))
addWeakPropertyChangeListener
public void addWeakPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Adds a `PropertyChangeListener` to the weak listener list.
 The listener is registered for all properties.
 A `PropertyChangeEvent` will get fired in response to setting
 a bound property, e.g. `setFont`, `setBackground`,
 or `setForeground`.
 Note that if the current component is inheriting its foreground,
 background, or font from its container, then no event will be
 fired in response to a change in the inherited property.
 This method creates advanced SwingPropertyChangeSupport which is safe to use when
 removing/adding listeners during firing property change event.
Parameters:
`listener` - The `PropertyChangeListener` to be added
See Also:
[`Action.addPropertyChangeListener(java.beans.PropertyChangeListener)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#addPropertyChangeListener(java.beans.PropertyChangeListener))
firePropertyChange
protected void firePropertyChange([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)
Supports reporting bound property changes. This method can be called
 when a bound property has changed and it will send the appropriate
 `PropertyChangeEvent` to any registered
 `PropertyChangeListeners`.
Overrides:
`[firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))` in class `[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)`
removePropertyChangeListener
public void removePropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Removes a `PropertyChangeListener` from the listener list.
 This removes a `PropertyChangeListener` that was registered
 for all properties.
Specified by:
`[removePropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#removePropertyChangeListener(java.beans.PropertyChangeListener))` in interface `[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)`
Overrides:
`[removePropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener))` in class `[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)`
Parameters:
`listener` - the `PropertyChangeListener` to be removed
See Also:
[`Action.removePropertyChangeListener(java.beans.PropertyChangeListener)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#removePropertyChangeListener(java.beans.PropertyChangeListener))
removeWeakPropertyChangeListener
public void removeWeakPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Removes a `PropertyChangeListener` from the weak listener list.
 This removes a `PropertyChangeListener` that was registered
 for all properties.
Parameters:
`listener` - the `PropertyChangeListener` to be removed
See Also:
[`Action.removePropertyChangeListener(java.beans.PropertyChangeListener)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#removePropertyChangeListener(java.beans.PropertyChangeListener))
createMenuItem
@CheckForNullpublic [JMenuItem](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html) createMenuItem(com.nomagic.actions.MenuComponentFactory factory)
Action can return preferred representation of itself as menu item. If action returns null,
 some external menu item creation mechanism will be used.
Parameters:
`factory` - factory.
Returns:
the menu item or null.
isIDGenerated
public boolean isIDGenerated()
Returns true if id was generated.
Returns:
true if id was generated.
getPropertyChangeListeners
public [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)[] getPropertyChangeListeners()
Returns an array of all the `PropertyChangeListener`s added
 to this action with addPropertyChangeListener().
Overrides:
`[getPropertyChangeListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getPropertyChangeListeners())` in class `[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)`
Returns:
all of the `PropertyChangeListener`s added or an empty
 array if no listeners have been added
hasMenuShortcutMask
public static boolean hasMenuShortcutMask([AWTEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html) event)
Check if event has menu shortcut mask modifier
Parameters:
`event` - event
Returns:
true if event has CONTROL (or COMMAND on Mac) modifiers
getMenuShortcutMaskAsString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getMenuShortcutMaskAsString()
Returns:
representation of menu shortcut modifier. Representation can be used in various UI messages.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.actions</a></div>
<h1 class="title" title="Class NMAction">Class NMAction</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">javax.swing.AbstractAction</a>
<div class="inheritance">com.nomagic.actions.NMAction</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></code>, <code><a href="BaseNMStateAction.html" title="class in com.nomagic.actions">BaseNMStateAction</a></code>, <code><a href="ColorChooseAction.html" title="class in com.nomagic.actions">ColorChooseAction</a></code>, <code><a href="../magicdraw/actions/MDAction.html" title="class in com.nomagic.magicdraw.actions">MDAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">NMAction</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">AbstractAction</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></span></div>
<div class="block">The class describes some abstract action.
 Any specific action must implement actionPerformed() method.
 The action has such properties: name, id,small icon,large icon,some shortcuts,mnemonic, description, group</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../serialized-form.html#com.nomagic.actions.NMAction">Serialized Form</a></li>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTION_SHORTCUTS">ACTION_SHORTCUTS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for storing command keys.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BELONGS_TO_SEPARATE_GROUP_IN_UI">BELONGS_TO_SEPARATE_GROUP_IN_UI</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A name of property to put this action into a dedicate special group.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DO_NO_SHOW_ACTION_NAME_IN_UI">DO_NO_SHOW_ACTION_NAME_IN_UI</a></code></div>
<div class="col-last even-row-color">
<div class="block">A name of property to hide action name text in create UI.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DO_NOT_REGISTER_ACTION_TO_COMPONENTS">DO_NOT_REGISTER_ACTION_TO_COMPONENTS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A name of property to skip registering this action to components.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#GENERATED_ID_PREFIX">GENERATED_ID_PREFIX</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GROUP">GROUP</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for storing group.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ID">ID</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for storing id.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LARGE_ICON">LARGE_ICON</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for storing large icon.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MENU_SHORTCUT_MASK">MENU_SHORTCUT_MASK</a></code></div>
<div class="col-last even-row-color">
<div class="block">Menu shortcut mask used to create shortcuts.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TINY_ICON">TINY_ICON</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for storing tiny icon (smaller than small icon).</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">NMAction</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs the action with nulls.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,int)">NMAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int mnemonic)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs the action with given id, name, mnemonic key.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.String)">NMAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int mnemonic,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs the action with given id, name, mnemonic key and group.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke)">NMAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs the action with given id, name, keystroke.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String)">NMAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs the action with given id, name, keystroke and group.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.actions.ActionsVisitor)">accept</a><wbr/>(<a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts ActionsVisitor using Visitor pattern.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionEvent.html" title="class or interface in java.awt.event">ActionEvent</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Executes given action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAction(com.nomagic.actions.NMAction)">addAction</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a <code>PropertyChangeListener</code> to the listener list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addShortcut(javax.swing.KeyStroke)">addShortcut</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> key)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the shortcut to the action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addShotcut(javax.swing.KeyStroke)">addShotcut</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> key)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">type error.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)">addWeakPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a <code>PropertyChangeListener</code> to the weak listener  list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareTo(java.lang.Object)">compareTo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Compares the name of the action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html" title="class or interface in javax.swing">JMenuItem</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMenuItem(com.nomagic.actions.MenuComponentFactory)">createMenuItem</a><wbr/>(com.nomagic.actions.MenuComponentFactory factory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Action can return preferred representation of itself as menu item.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if given object is equal to the current action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Supports reporting bound property changes.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActions()">getActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the list of the actions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCommandKey()">getCommandKey</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the shortcut of the action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescription()">getDescription</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns description of this action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGroup()">getGroup</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the name of the related actions group.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getIcon()">getIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use {link #getSmallOrLargeIcon}</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the id of the action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLargeIcon()">getLargeIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the large icon of the action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLargeOrSmallIcon()">getLargeOrSmallIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMenuShortcutMaskAsString()">getMenuShortcutMaskAsString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMnemonicKey()">getMnemonicKey</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the mnemonic of the action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the name of the action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyChangeListeners()">getPropertyChangeListeners</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns an array of all the <code>PropertyChangeListener</code>s added
 to this action with addPropertyChangeListener().</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShortcuts()">getShortcuts</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all shortcuts of the the action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSmallIcon()">getSmallIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the small icon of the action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSmallOrLargeIcon()">getSmallOrLargeIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTinyIcon()">getTinyIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the tiny icon of the action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates hashcode from id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasMenuShortcutMask(java.awt.AWTEvent)">hasMenuShortcutMask</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html" title="class or interface in java.awt">AWTEvent</a> event)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if event has menu shortcut mask modifier</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isIDGenerated()">isIDGenerated</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if id was generated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAction(com.nomagic.actions.NMAction)">removeAction</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeIf(java.util.function.Predicate)">removeIf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; filter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all of the owned actions that satisfy the given predicate</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a <code>PropertyChangeListener</code> from the listener list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeShortcut(javax.swing.KeyStroke)">removeShortcut</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> key)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the shortcut from the action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)">removeWeakPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a <code>PropertyChangeListener</code> from the weak listener list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setActions(java.util.List)">setActions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the list of the actions(do nothing here).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDescription(java.lang.String)">setDescription</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new action description.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setGroup(java.lang.String)">setGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new group for this action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIcon(javax.swing.Icon)">setIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets small and large icon.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLargeIcon(javax.swing.Icon)">setLargeIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the large icon of the action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMnemonicKey(int)">setMnemonicKey</a><wbr/>(int key)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the mnemonic key of the action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new name of action, method implemented by putting value with key  Action.NAME</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShortcuts(java.util.List)">setShortcuts</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a>&gt; shortcuts)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the shortcuts list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSmallIcon(javax.swing.Icon)">setSmallIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the small icon of the action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTinyIcon(javax.swing.Icon)">setTinyIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the tiny icon of the action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#shallowClone()">shallowClone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns itself</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">toString returns the action's name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateState()">updateState</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method should update action state (enabled or disabled, checked or unchecked).</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="DO_NO_SHOW_ACTION_NAME_IN_UI">
<h3>DO_NO_SHOW_ACTION_NAME_IN_UI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DO_NO_SHOW_ACTION_NAME_IN_UI</span></div>
<div class="block">A name of property to hide action name text in create UI. For example buttons will not show name of this action as text</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.NMAction.DO_NO_SHOW_ACTION_NAME_IN_UI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BELONGS_TO_SEPARATE_GROUP_IN_UI">
<h3>BELONGS_TO_SEPARATE_GROUP_IN_UI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BELONGS_TO_SEPARATE_GROUP_IN_UI</span></div>
<div class="block">A name of property to put this action into a dedicate special group. For example Options action can be in the right side of horizontal toolbar.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.NMAction.BELONGS_TO_SEPARATE_GROUP_IN_UI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DO_NOT_REGISTER_ACTION_TO_COMPONENTS">
<h3>DO_NOT_REGISTER_ACTION_TO_COMPONENTS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DO_NOT_REGISTER_ACTION_TO_COMPONENTS</span></div>
<div class="block">A name of property to skip registering this action to components.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.NMAction.DO_NOT_REGISTER_ACTION_TO_COMPONENTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTION_SHORTCUTS">
<h3>ACTION_SHORTCUTS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACTION_SHORTCUTS</span></div>
<div class="block">Key for storing command keys.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.NMAction.ACTION_SHORTCUTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ID">
<h3>ID</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ID</span></div>
<div class="block">Key for storing id.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.NMAction.ID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LARGE_ICON">
<h3>LARGE_ICON</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LARGE_ICON</span></div>
<div class="block">Key for storing large icon.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.NMAction.LARGE_ICON">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TINY_ICON">
<h3>TINY_ICON</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TINY_ICON</span></div>
<div class="block">Key for storing tiny icon (smaller than small icon).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.NMAction.TINY_ICON">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GROUP">
<h3>GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">GROUP</span></div>
<div class="block">Key for storing group.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.NMAction.GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MENU_SHORTCUT_MASK">
<h3>MENU_SHORTCUT_MASK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">MENU_SHORTCUT_MASK</span></div>
<div class="block">Menu shortcut mask used to create shortcuts.</div>
</section>
</li>
<li>
<section class="detail" id="GENERATED_ID_PREFIX">
<h3>GENERATED_ID_PREFIX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">GENERATED_ID_PREFIX</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.NMAction.GENERATED_ID_PREFIX">Constant Field Values</a></li>
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
<h3>NMAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NMAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Constructs the action with given id, name, keystroke and group.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the id of the action.</dd>
<dd><code>name</code> - the name of the action.</dd>
<dd><code>stroke</code> - the KeyStroke of the action.</dd>
<dd><code>group</code> - the name of the related commands group.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,javax.swing.KeyStroke)">
<h3>NMAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NMAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke)</span></div>
<div class="block">Constructs the action with given id, name, keystroke.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the id of the action.</dd>
<dd><code>name</code> - the name of the action.</dd>
<dd><code>stroke</code> - the KeyStroke of the action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>NMAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NMAction</span>()</div>
<div class="block">Constructs the action with nulls.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,int,java.lang.String)">
<h3>NMAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NMAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int mnemonic,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Constructs the action with given id, name, mnemonic key and group.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the id of the action.</dd>
<dd><code>name</code> - the name of the action.</dd>
<dd><code>mnemonic</code> - the mnemonic key of the action</dd>
<dd><code>group</code> - the name of the related commands group.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,int)">
<h3>NMAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NMAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 int mnemonic)</span></div>
<div class="block">Constructs the action with given id, name, mnemonic key.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the id of the action.</dd>
<dd><code>name</code> - the name of the action.</dd>
<dd><code>mnemonic</code> - the mnemonic key of the action</dd>
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
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Sets new name of action, method implemented by putting value with key  Action.NAME</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<div class="block">Returns the id of the action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the id of the action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCommandKey()">
<h3>getCommandKey</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a></span> <span class="element-name">getCommandKey</span>()</div>
<div class="block">Returns the shortcut of the action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the first shortcut from all available shortcuts, null if no shortcuts are defined.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addShotcut(javax.swing.KeyStroke)">
<h3>addShotcut</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addShotcut</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> key)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">type error. Use <a href="#addShortcut(javax.swing.KeyStroke)"><code>addShortcut(KeyStroke)</code></a></div>
</div>
<div class="block">Adds the shortcut to the action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - the given shortcut.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addShortcut(javax.swing.KeyStroke)">
<h3>addShortcut</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addShortcut</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> key)</span></div>
<div class="block">Adds the shortcut to the action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - the given shortcut.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeShortcut(javax.swing.KeyStroke)">
<h3>removeShortcut</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeShortcut</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> key)</span></div>
<div class="block">Removes the shortcut from the action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - the given shortcut.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShortcuts(java.util.List)">
<h3>setShortcuts</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShortcuts</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a>&gt; shortcuts)</span></div>
<div class="block">Sets the shortcuts list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shortcuts</code> - the list of all shortcuts.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getShortcuts()">
<h3>getShortcuts</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a>&gt;</span> <span class="element-name">getShortcuts</span>()</div>
<div class="block">Returns all shortcuts of the the action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the list of all shortcuts. List is unmodifiable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Returns the name of the action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the name of the action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMnemonicKey(int)">
<h3>setMnemonicKey</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMnemonicKey</span><wbr/><span class="parameters">(int key)</span></div>
<div class="block">Sets the mnemonic key of the action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - the mnemonic key of the action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMnemonicKey()">
<h3>getMnemonicKey</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMnemonicKey</span>()</div>
<div class="block">Returns the mnemonic of the action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the mnemonic of the action or -1 if command does not have mnemonic.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIcon(javax.swing.Icon)">
<h3>setIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="block">Sets small and large icon.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - Icon of the action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSmallIcon(javax.swing.Icon)">
<h3>setSmallIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSmallIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="block">Sets the small icon of the action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - the small icon of the action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSmallIcon()">
<h3>getSmallIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getSmallIcon</span>()</div>
<div class="block">Returns the small icon of the action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the small icon of the action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTinyIcon(javax.swing.Icon)">
<h3>setTinyIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTinyIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="block">Sets the tiny icon of the action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - the tiny icon of the action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTinyIcon()">
<h3>getTinyIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getTinyIcon</span>()</div>
<div class="block">Returns the tiny icon of the action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the tiny icon of the action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon()">
<h3>getIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getIcon</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use {link #getSmallOrLargeIcon}</div>
</div>
</section>
</li>
<li>
<section class="detail" id="setLargeIcon(javax.swing.Icon)">
<h3>setLargeIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLargeIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="block">Sets the large icon of the action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - the large icon of the action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLargeIcon()">
<h3>getLargeIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getLargeIcon</span>()</div>
<div class="block">Returns the large icon of the action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the large icon of the action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLargeOrSmallIcon()">
<h3>getLargeOrSmallIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getLargeOrSmallIcon</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>large icon if present. If not, small one</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSmallOrLargeIcon()">
<h3>getSmallOrLargeIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getSmallOrLargeIcon</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>small icon if present. If not, large one</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<div class="block">Checks if given object is equal to the current action.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>true if given object is NMAction and id of the given action is the same as id of current action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<div class="block">Creates hashcode from id.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>hash code of action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">toString returns the action's name.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>the name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="actionPerformed(java.awt.event.ActionEvent)">
<h3>actionPerformed</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">actionPerformed</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionEvent.html" title="class or interface in java.awt.event">ActionEvent</a> e)</span></div>
<div class="block">Executes given action.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html#actionPerformed(java.awt.event.ActionEvent)" title="class or interface in java.awt.event">actionPerformed</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>e</code> - event caused execution.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareTo(java.lang.Object)">
<h3>compareTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">compareTo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<div class="block">Compares the name of the action. Uses String.compareTo method.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code></dd>
<dt>Parameters:</dt>
<dd><code>o</code> - the given object to compare to.</dd>
<dt>Returns:</dt>
<dd>name comparison result</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></span> <span class="element-name">clone</span>()</div>
<div class="block">Clones the object.
 Does the deep clone.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#clone()" title="class or interface in javax.swing">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">AbstractAction</a></code></dd>
<dt>Returns:</dt>
<dd>cloned object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="shallowClone()">
<h3>shallowClone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></span> <span class="element-name">shallowClone</span>()</div>
<div class="block">Returns itself</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>itself here</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.actions.ActionsVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a> visitor)</span></div>
<div class="block">Accepts ActionsVisitor using Visitor pattern.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visitor</code> - visitor to accept.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDescription(java.lang.String)">
<h3>setDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDescription</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</span></div>
<div class="block">Sets new action description.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>description</code> - action description.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span>()</div>
<div class="block">Returns description of this action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>action description.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGroup(java.lang.String)">
<h3>setGroup</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setGroup</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Sets new group for this action. Empty string will be converted to null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>group</code> - group name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGroup()">
<h3>getGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getGroup</span>()</div>
<div class="block">Returns the name of the related actions group.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the name of the related actions group.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActions()">
<h3>getActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</span> <span class="element-name">getActions</span>()</div>
<div class="block">Returns the list of the actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>empty list here. Some derived classes may override this method.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="forEach(java.util.function.Consumer)">
<h3>forEach</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">forEach</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; consumer)</span></div>
<div class="block">Performs the given consumer for each owned action. Owned actions should not be added/removed inside consumer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>consumer</code> - the action to be performed for each NMAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="forEachIncludingSelf(java.util.function.Consumer)">
<h3>forEachIncludingSelf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">forEachIncludingSelf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; consumer)</span></div>
<div class="block">Performs the given consumer for each owned action including self. Owned actions should not be added/removed inside consumer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>consumer</code> - the action to be performed for each NMAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActions(java.util.List)">
<h3>setActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActions</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
<div class="block">Sets the list of the actions(do nothing here).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actions</code> - the list of the actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAction(com.nomagic.actions.NMAction)">
<h3>addAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAction</span><wbr/><span class="parameters">(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Adds action. Not supported here.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - the action to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAction(com.nomagic.actions.NMAction)">
<h3>removeAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAction</span><wbr/><span class="parameters">(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Remove action. Not supported here.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - the action to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeIf(java.util.function.Predicate)">
<h3>removeIf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeIf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; filter)</span></div>
<div class="block">Removes all of the owned actions that satisfy the given predicate</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filter</code> - given predicate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateState()">
<h3>updateState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateState</span>()</div>
<div class="block">Method should update action state (enabled or disabled, checked or unchecked).
 Method is called after other actions was executed.
 Always enable here.</div>
</section>
</li>
<li>
<section class="detail" id="addPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>addPropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Adds a <code>PropertyChangeListener</code> to the listener list.
 The listener is registered for all properties.
 <p>
 A <code>PropertyChangeEvent</code> will get fired in response to setting
 a bound property, e.g. <code>setFont</code>, <code>setBackground</code>,
 or <code>setForeground</code>.
 Note that if the current component is inheriting its foreground,
 background, or font from its container, then no event will be
 fired in response to a change in the inherited property.
 This method creates advanced SwingPropertyChangeSupport which is safe to use when
 removing/adding listeners during firing property change event.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#addPropertyChangeListener(java.beans.PropertyChangeListener)" title="class or interface in javax.swing">addPropertyChangeListener</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)" title="class or interface in javax.swing">addPropertyChangeListener</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">AbstractAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - The <code>PropertyChangeListener</code> to be added</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#addPropertyChangeListener(java.beans.PropertyChangeListener)" title="class or interface in javax.swing"><code>Action.addPropertyChangeListener(java.beans.PropertyChangeListener)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addWeakPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>addWeakPropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addWeakPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Adds a <code>PropertyChangeListener</code> to the weak listener  list.
 The listener is registered for all properties.
 <p>
 A <code>PropertyChangeEvent</code> will get fired in response to setting
 a bound property, e.g. <code>setFont</code>, <code>setBackground</code>,
 or <code>setForeground</code>.
 Note that if the current component is inheriting its foreground,
 background, or font from its container, then no event will be
 fired in response to a change in the inherited property.
 This method creates advanced SwingPropertyChangeSupport which is safe to use when
 removing/adding listeners during firing property change event.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - The <code>PropertyChangeListener</code> to be added</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#addPropertyChangeListener(java.beans.PropertyChangeListener)" title="class or interface in javax.swing"><code>Action.addPropertyChangeListener(java.beans.PropertyChangeListener)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block">Supports reporting bound property changes.  This method can be called
 when a bound property has changed and it will send the appropriate
 <code>PropertyChangeEvent</code> to any registered
 <code>PropertyChangeListeners</code>.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)" title="class or interface in javax.swing">firePropertyChange</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">AbstractAction</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>removePropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Removes a <code>PropertyChangeListener</code> from the listener list.
 This removes a <code>PropertyChangeListener</code> that was registered
 for all properties.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#removePropertyChangeListener(java.beans.PropertyChangeListener)" title="class or interface in javax.swing">removePropertyChangeListener</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)" title="class or interface in javax.swing">removePropertyChangeListener</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">AbstractAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - the <code>PropertyChangeListener</code> to be removed</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#removePropertyChangeListener(java.beans.PropertyChangeListener)" title="class or interface in javax.swing"><code>Action.removePropertyChangeListener(java.beans.PropertyChangeListener)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>removeWeakPropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeWeakPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Removes a <code>PropertyChangeListener</code> from the weak listener list.
 This removes a <code>PropertyChangeListener</code> that was registered
 for all properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the <code>PropertyChangeListener</code> to be removed</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#removePropertyChangeListener(java.beans.PropertyChangeListener)" title="class or interface in javax.swing"><code>Action.removePropertyChangeListener(java.beans.PropertyChangeListener)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMenuItem(com.nomagic.actions.MenuComponentFactory)">
<h3>createMenuItem</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html" title="class or interface in javax.swing">JMenuItem</a></span> <span class="element-name">createMenuItem</span><wbr/><span class="parameters">(com.nomagic.actions.MenuComponentFactory factory)</span></div>
<div class="block">Action can return preferred representation of itself as menu item. If action returns null,
 some external menu item creation mechanism will be used.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factory</code> - factory.</dd>
<dt>Returns:</dt>
<dd>the menu item or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isIDGenerated()">
<h3>isIDGenerated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isIDGenerated</span>()</div>
<div class="block">Returns true if id was generated.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if id was generated.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyChangeListeners()">
<h3>getPropertyChangeListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a>[]</span> <span class="element-name">getPropertyChangeListeners</span>()</div>
<div class="block">Returns an array of all the <code>PropertyChangeListener</code>s added
 to this action with addPropertyChangeListener().</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getPropertyChangeListeners()" title="class or interface in javax.swing">getPropertyChangeListeners</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">AbstractAction</a></code></dd>
<dt>Returns:</dt>
<dd>all of the <code>PropertyChangeListener</code>s added or an empty
 array if no listeners have been added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasMenuShortcutMask(java.awt.AWTEvent)">
<h3>hasMenuShortcutMask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasMenuShortcutMask</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html" title="class or interface in java.awt">AWTEvent</a> event)</span></div>
<div class="block">Check if event has menu shortcut mask modifier</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>event</code> - event</dd>
<dt>Returns:</dt>
<dd>true if event has CONTROL (or COMMAND on Mac) modifiers</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMenuShortcutMaskAsString()">
<h3>getMenuShortcutMaskAsString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMenuShortcutMaskAsString</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>representation of menu shortcut modifier. Representation can be used in various UI messages.</dd>
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
