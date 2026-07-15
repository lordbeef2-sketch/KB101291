# JAVA OPENAPI: PropertyAction (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/actions/PropertyAction.html
- source_path: `com/nomagic/magicdraw/actions/PropertyAction.html`
- source_sha256: `0ba5c1ae42b60712f917daa643110b6c254c700699cbc25bb7cbfb0f0258d615`
- captured_utc: `2026-07-14T16:55:02.814876+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.actions](package-summary.html)

## Class PropertyAction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[javax.swing.AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
[com.nomagic.actions.NMAction](../../actions/NMAction.html)
[com.nomagic.magicdraw.actions.MDAction](MDAction.html)
com.nomagic.magicdraw.actions.PropertyAction

All Implemented Interfaces:
`com.nomagic.magicdraw.actions.ShortcutSchemaAction`, `[ActionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`, `[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)`

@OpenApiAllpublic classPropertyAction
extends [MDAction](MDAction.html)
implements [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)

Action for changing assigned property value.

See Also:
[Serialized Form](../../../../serialized-form.html#com.nomagic.magicdraw.actions.PropertyAction)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MANAGER_CHANGED](#MANAGER_CHANGED)`
Fields inherited from class com.nomagic.actions.[NMAction](../../actions/NMAction.html)
`[ACTION_SHORTCUTS](../../actions/NMAction.html#ACTION_SHORTCUTS), [BELONGS_TO_SEPARATE_GROUP_IN_UI](../../actions/NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI), [DO_NO_SHOW_ACTION_NAME_IN_UI](../../actions/NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI), [DO_NOT_REGISTER_ACTION_TO_COMPONENTS](../../actions/NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS), [GENERATED_ID_PREFIX](../../actions/NMAction.html#GENERATED_ID_PREFIX), [GROUP](../../actions/NMAction.html#GROUP), [ID](../../actions/NMAction.html#ID), [LARGE_ICON](../../actions/NMAction.html#LARGE_ICON), [MENU_SHORTCUT_MASK](../../actions/NMAction.html#MENU_SHORTCUT_MASK), [TINY_ICON](../../actions/NMAction.html#TINY_ICON)`
Fields inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[changeSupport](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#changeSupport), [enabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#enabled)`
Fields inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[ACCELERATOR_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACCELERATOR_KEY), [ACTION_COMMAND_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACTION_COMMAND_KEY), [DEFAULT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DEFAULT), [DISPLAYED_MNEMONIC_INDEX_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DISPLAYED_MNEMONIC_INDEX_KEY), [LARGE_ICON_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LARGE_ICON_KEY), [LONG_DESCRIPTION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LONG_DESCRIPTION), [MNEMONIC_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#MNEMONIC_KEY), [NAME](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#NAME), [SELECTED_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SELECTED_KEY), [SHORT_DESCRIPTION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SHORT_DESCRIPTION), [SMALL_ICON](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SMALL_ICON)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PropertyAction](#%3Cinit%3E(com.nomagic.magicdraw.properties.PropertyManager,java.lang.String))([PropertyManager](../properties/PropertyManager.html) manager,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyID)`
The constructor for action with given property.
`[PropertyAction](#%3Cinit%3E(java.lang.String,com.nomagic.magicdraw.properties.PropertyManager,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 [PropertyManager](../properties/PropertyManager.html) manager,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyID)`
The constructor for action with given property.
`[PropertyAction](#%3Cinit%3E(java.lang.String,com.nomagic.magicdraw.properties.PropertyManager,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 [PropertyManager](../properties/PropertyManager.html) manager,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyID,
 boolean useShortcutSchema)`
The constructor for action with given property.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.actions.ActionsVisitor))([ActionsVisitor](../../actions/ActionsVisitor.html) visitor)`
Accepts ActionsVisitor using Visitor pattern.
`void`
`[addChangeListener](#addChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Add the listener which will be notified about the
 change of underlying property manager of this action
`void`
`[addChangeListener](#addChangeListener(java.lang.String,java.beans.PropertyChangeListener))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) property,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Add the listener which will be notified about the
 change of underlying property manager of this action
`protected void`
`[changePropertyValue](#changePropertyValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)`
Change value of a property
`protected void`
`[fireManagerChanged](#fireManagerChanged(com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](../properties/PropertyManager.html) oldManager,
 [PropertyManager](../properties/PropertyManager.html) newManager)`
Fires the notification about the property manager change
`[PropertyManager](../properties/PropertyManager.html)`
`[getManager](#getManager())()`
Get the manager.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getNewValue](#getNewValue())()`
Gets the new property value.
`[Property](../properties/Property.html)`
`[getProperty](#getProperty())()`
Returns the property.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPropertyID](#getPropertyID())()`
Get the property id.
`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)`

`void`
`[removeChangeListener](#removeChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Remove the listener from this action
`void`
`[removeChangeListener](#removeChangeListener(java.lang.String,java.beans.PropertyChangeListener))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) property,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Remove the listener from this action
`void`
`[setManager](#setManager(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](../properties/PropertyManager.html) manager)`
Set the manager.
`void`
`[setNewValue](#setNewValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)`
Sets the new property value.
`protected void`
`[setPropertyId](#setPropertyId(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Sets property id
Methods inherited from class com.nomagic.magicdraw.actions.[MDAction](MDAction.html)
`[actionPerformed](MDAction.html#actionPerformed(java.awt.event.ActionEvent)), [isUseShortcutSchema](MDAction.html#isUseShortcutSchema()), [updateState](MDAction.html#updateState())`
Methods inherited from class com.nomagic.actions.[NMAction](../../actions/NMAction.html)
`[addAction](../../actions/NMAction.html#addAction(com.nomagic.actions.NMAction)), [addPropertyChangeListener](../../actions/NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addShortcut](../../actions/NMAction.html#addShortcut(javax.swing.KeyStroke)), [addShotcut](../../actions/NMAction.html#addShotcut(javax.swing.KeyStroke)), [addWeakPropertyChangeListener](../../actions/NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [clone](../../actions/NMAction.html#clone()), [compareTo](../../actions/NMAction.html#compareTo(java.lang.Object)), [createMenuItem](../../actions/NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)), [equals](../../actions/NMAction.html#equals(java.lang.Object)), [firePropertyChange](../../actions/NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [forEach](../../actions/NMAction.html#forEach(java.util.function.Consumer)), [forEachIncludingSelf](../../actions/NMAction.html#forEachIncludingSelf(java.util.function.Consumer)), [getActions](../../actions/NMAction.html#getActions()), [getCommandKey](../../actions/NMAction.html#getCommandKey()), [getDescription](../../actions/NMAction.html#getDescription()), [getGroup](../../actions/NMAction.html#getGroup()), [getIcon](../../actions/NMAction.html#getIcon()), [getID](../../actions/NMAction.html#getID()), [getLargeIcon](../../actions/NMAction.html#getLargeIcon()), [getLargeOrSmallIcon](../../actions/NMAction.html#getLargeOrSmallIcon()), [getMenuShortcutMaskAsString](../../actions/NMAction.html#getMenuShortcutMaskAsString()), [getMnemonicKey](../../actions/NMAction.html#getMnemonicKey()), [getName](../../actions/NMAction.html#getName()), [getPropertyChangeListeners](../../actions/NMAction.html#getPropertyChangeListeners()), [getShortcuts](../../actions/NMAction.html#getShortcuts()), [getSmallIcon](../../actions/NMAction.html#getSmallIcon()), [getSmallOrLargeIcon](../../actions/NMAction.html#getSmallOrLargeIcon()), [getTinyIcon](../../actions/NMAction.html#getTinyIcon()), [hashCode](../../actions/NMAction.html#hashCode()), [hasMenuShortcutMask](../../actions/NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)), [isIDGenerated](../../actions/NMAction.html#isIDGenerated()), [removeAction](../../actions/NMAction.html#removeAction(com.nomagic.actions.NMAction)), [removeIf](../../actions/NMAction.html#removeIf(java.util.function.Predicate)), [removePropertyChangeListener](../../actions/NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [removeShortcut](../../actions/NMAction.html#removeShortcut(javax.swing.KeyStroke)), [removeWeakPropertyChangeListener](../../actions/NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [setActions](../../actions/NMAction.html#setActions(java.util.List)), [setDescription](../../actions/NMAction.html#setDescription(java.lang.String)), [setGroup](../../actions/NMAction.html#setGroup(java.lang.String)), [setIcon](../../actions/NMAction.html#setIcon(javax.swing.Icon)), [setLargeIcon](../../actions/NMAction.html#setLargeIcon(javax.swing.Icon)), [setMnemonicKey](../../actions/NMAction.html#setMnemonicKey(int)), [setName](../../actions/NMAction.html#setName(java.lang.String)), [setShortcuts](../../actions/NMAction.html#setShortcuts(java.util.List)), [setSmallIcon](../../actions/NMAction.html#setSmallIcon(javax.swing.Icon)), [setTinyIcon](../../actions/NMAction.html#setTinyIcon(javax.swing.Icon)), [shallowClone](../../actions/NMAction.html#shallowClone()), [toString](../../actions/NMAction.html#toString())`
Methods inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[getKeys](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()), [getValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)), [isEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()), [putValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)), [setEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[accept](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object))`

============ FIELD DETAIL =========== 
Field Details
MANAGER_CHANGED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MANAGER_CHANGED
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.PropertyAction.MANAGER_CHANGED)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PropertyAction
public PropertyAction([PropertyManager](../properties/PropertyManager.html) manager,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyID)
The constructor for action with given property.
Parameters:
`manager` - property manager
`propertyID` - id of the property
PropertyAction
public PropertyAction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 [PropertyManager](../properties/PropertyManager.html) manager,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyID)
The constructor for action with given property.
Parameters:
`actionID` - id of the action
`manager` - property manager
`propertyID` - id of the property
PropertyAction
public PropertyAction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 [PropertyManager](../properties/PropertyManager.html) manager,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyID,
 boolean useShortcutSchema)
The constructor for action with given property.
Parameters:
`actionID` - id of the action
`manager` - property manager
`propertyID` - id of the property
`useShortcutSchema` - use shortcuts schema for this action
 ============ METHOD DETAIL ========== 
Method Details
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
See Also:
[`PropertyChangeListener.propertyChange(java.beans.PropertyChangeEvent)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))
setNewValue
public void setNewValue([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)
Sets the new property value.
Parameters:
`newValue` - the new property value.
getNewValue
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getNewValue()
Gets the new property value.
Returns:
the new property value
getProperty
public [Property](../properties/Property.html) getProperty()
Returns the property.
Returns:
returns an assigned property
changePropertyValue
protected void changePropertyValue([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)
Change value of a property
Parameters:
`newValue` - new value
accept
public void accept([ActionsVisitor](../../actions/ActionsVisitor.html) visitor)
Description copied from class: `[NMAction](../../actions/NMAction.html#accept(com.nomagic.actions.ActionsVisitor))`
Accepts ActionsVisitor using Visitor pattern.
Overrides:
`[accept](../../actions/NMAction.html#accept(com.nomagic.actions.ActionsVisitor))` in class `[NMAction](../../actions/NMAction.html)`
Parameters:
`visitor` - visitor to accept.
getManager
public [PropertyManager](../properties/PropertyManager.html) getManager()
Get the manager.
Returns:
returns the manager
setManager
public void setManager([PropertyManager](../properties/PropertyManager.html) manager)
Set the manager.
Parameters:
`manager` - the new manager
fireManagerChanged
protected void fireManagerChanged([PropertyManager](../properties/PropertyManager.html) oldManager,
 [PropertyManager](../properties/PropertyManager.html) newManager)
Fires the notification about the property manager change
Parameters:
`oldManager` - old manager
`newManager` - new manager
getPropertyID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPropertyID()
Get the property id.
Returns:
Returns the id
setPropertyId
protected void setPropertyId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Sets property id
Parameters:
`id` - property id
addChangeListener
public void addChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Add the listener which will be notified about the
 change of underlying property manager of this action
Parameters:
`listener` - for property change notifications
addChangeListener
public void addChangeListener([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) property,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Add the listener which will be notified about the
 change of underlying property manager of this action
Parameters:
`property` - the listener will be notified only about this property changes
`listener` - for property change notifications
See Also:
[`MANAGER_CHANGED`](#MANAGER_CHANGED)
removeChangeListener
public void removeChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Remove the listener from this action
Parameters:
`listener` - to be removed
removeChangeListener
public void removeChangeListener([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) property,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Remove the listener from this action
Parameters:
`property` - the name of the property
`listener` - to be removed

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.actions</a></div>
<h1 class="title" title="Class PropertyAction">Class PropertyAction</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">javax.swing.AbstractAction</a>
<div class="inheritance"><a href="../../actions/NMAction.html" title="class in com.nomagic.actions">com.nomagic.actions.NMAction</a>
<div class="inheritance"><a href="MDAction.html" title="class in com.nomagic.magicdraw.actions">com.nomagic.magicdraw.actions.MDAction</a>
<div class="inheritance">com.nomagic.magicdraw.actions.PropertyAction</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.actions.ShortcutSchemaAction</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PropertyAction</span>
<span class="extends-implements">extends <a href="MDAction.html" title="class in com.nomagic.magicdraw.actions">MDAction</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></span></div>
<div class="block">Action for changing assigned property value.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../serialized-form.html#com.nomagic.magicdraw.actions.PropertyAction">Serialized Form</a></li>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MANAGER_CHANGED">MANAGER_CHANGED</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.actions.NMAction">Fields inherited from class com.nomagic.actions.<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="../../actions/NMAction.html#ACTION_SHORTCUTS">ACTION_SHORTCUTS</a>, <a href="../../actions/NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI">BELONGS_TO_SEPARATE_GROUP_IN_UI</a>, <a href="../../actions/NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI">DO_NO_SHOW_ACTION_NAME_IN_UI</a>, <a href="../../actions/NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS">DO_NOT_REGISTER_ACTION_TO_COMPONENTS</a>, <a href="../../actions/NMAction.html#GENERATED_ID_PREFIX">GENERATED_ID_PREFIX</a>, <a href="../../actions/NMAction.html#GROUP">GROUP</a>, <a href="../../actions/NMAction.html#ID">ID</a>, <a href="../../actions/NMAction.html#LARGE_ICON">LARGE_ICON</a>, <a href="../../actions/NMAction.html#MENU_SHORTCUT_MASK">MENU_SHORTCUT_MASK</a>, <a href="../../actions/NMAction.html#TINY_ICON">TINY_ICON</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.properties.PropertyManager,java.lang.String)">PropertyAction</a><wbr/>(<a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyID)</code></div>
<div class="col-last even-row-color">
<div class="block">The constructor for action with given property.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.magicdraw.properties.PropertyManager,java.lang.String)">PropertyAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyID)</code></div>
<div class="col-last odd-row-color">
<div class="block">The constructor for action with given property.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.magicdraw.properties.PropertyManager,java.lang.String,boolean)">PropertyAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyID,
 boolean useShortcutSchema)</code></div>
<div class="col-last even-row-color">
<div class="block">The constructor for action with given property.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.actions.ActionsVisitor)">accept</a><wbr/>(<a href="../../actions/ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts ActionsVisitor using Visitor pattern.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addChangeListener(java.beans.PropertyChangeListener)">addChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add the listener which will be notified about the
 change of underlying property manager of this action</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addChangeListener(java.lang.String,java.beans.PropertyChangeListener)">addChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add the listener which will be notified about the
 change of underlying property manager of this action</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#changePropertyValue(java.lang.Object)">changePropertyValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Change value of a property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireManagerChanged(com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.magicdraw.properties.PropertyManager)">fireManagerChanged</a><wbr/>(<a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> oldManager,
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> newManager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Fires the notification about the property manager change</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManager()">getManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNewValue()">getNewValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the new property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperty()">getProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyID()">getPropertyID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the property id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeChangeListener(java.beans.PropertyChangeListener)">removeChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove the listener from this action</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeChangeListener(java.lang.String,java.beans.PropertyChangeListener)">removeChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove the listener from this action</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setManager(com.nomagic.magicdraw.properties.PropertyManager)">setManager</a><wbr/>(<a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNewValue(java.lang.Object)">setNewValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the new property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPropertyId(java.lang.String)">setPropertyId</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets property id</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.actions.MDAction">Methods inherited from class com.nomagic.magicdraw.actions.<a href="MDAction.html" title="class in com.nomagic.magicdraw.actions">MDAction</a></h3>
<code><a href="MDAction.html#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a>, <a href="MDAction.html#isUseShortcutSchema()">isUseShortcutSchema</a>, <a href="MDAction.html#updateState()">updateState</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.NMAction">Methods inherited from class com.nomagic.actions.<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="../../actions/NMAction.html#addAction(com.nomagic.actions.NMAction)">addAction</a>, <a href="../../actions/NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../actions/NMAction.html#addShortcut(javax.swing.KeyStroke)">addShortcut</a>, <a href="../../actions/NMAction.html#addShotcut(javax.swing.KeyStroke)">addShotcut</a>, <a href="../../actions/NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)">addWeakPropertyChangeListener</a>, <a href="../../actions/NMAction.html#clone()">clone</a>, <a href="../../actions/NMAction.html#compareTo(java.lang.Object)">compareTo</a>, <a href="../../actions/NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)">createMenuItem</a>, <a href="../../actions/NMAction.html#equals(java.lang.Object)">equals</a>, <a href="../../actions/NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../actions/NMAction.html#forEach(java.util.function.Consumer)">forEach</a>, <a href="../../actions/NMAction.html#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a>, <a href="../../actions/NMAction.html#getActions()">getActions</a>, <a href="../../actions/NMAction.html#getCommandKey()">getCommandKey</a>, <a href="../../actions/NMAction.html#getDescription()">getDescription</a>, <a href="../../actions/NMAction.html#getGroup()">getGroup</a>, <a href="../../actions/NMAction.html#getIcon()">getIcon</a>, <a href="../../actions/NMAction.html#getID()">getID</a>, <a href="../../actions/NMAction.html#getLargeIcon()">getLargeIcon</a>, <a href="../../actions/NMAction.html#getLargeOrSmallIcon()">getLargeOrSmallIcon</a>, <a href="../../actions/NMAction.html#getMenuShortcutMaskAsString()">getMenuShortcutMaskAsString</a>, <a href="../../actions/NMAction.html#getMnemonicKey()">getMnemonicKey</a>, <a href="../../actions/NMAction.html#getName()">getName</a>, <a href="../../actions/NMAction.html#getPropertyChangeListeners()">getPropertyChangeListeners</a>, <a href="../../actions/NMAction.html#getShortcuts()">getShortcuts</a>, <a href="../../actions/NMAction.html#getSmallIcon()">getSmallIcon</a>, <a href="../../actions/NMAction.html#getSmallOrLargeIcon()">getSmallOrLargeIcon</a>, <a href="../../actions/NMAction.html#getTinyIcon()">getTinyIcon</a>, <a href="../../actions/NMAction.html#hashCode()">hashCode</a>, <a href="../../actions/NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)">hasMenuShortcutMask</a>, <a href="../../actions/NMAction.html#isIDGenerated()">isIDGenerated</a>, <a href="../../actions/NMAction.html#removeAction(com.nomagic.actions.NMAction)">removeAction</a>, <a href="../../actions/NMAction.html#removeIf(java.util.function.Predicate)">removeIf</a>, <a href="../../actions/NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../actions/NMAction.html#removeShortcut(javax.swing.KeyStroke)">removeShortcut</a>, <a href="../../actions/NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)">removeWeakPropertyChangeListener</a>, <a href="../../actions/NMAction.html#setActions(java.util.List)">setActions</a>, <a href="../../actions/NMAction.html#setDescription(java.lang.String)">setDescription</a>, <a href="../../actions/NMAction.html#setGroup(java.lang.String)">setGroup</a>, <a href="../../actions/NMAction.html#setIcon(javax.swing.Icon)">setIcon</a>, <a href="../../actions/NMAction.html#setLargeIcon(javax.swing.Icon)">setLargeIcon</a>, <a href="../../actions/NMAction.html#setMnemonicKey(int)">setMnemonicKey</a>, <a href="../../actions/NMAction.html#setName(java.lang.String)">setName</a>, <a href="../../actions/NMAction.html#setShortcuts(java.util.List)">setShortcuts</a>, <a href="../../actions/NMAction.html#setSmallIcon(javax.swing.Icon)">setSmallIcon</a>, <a href="../../actions/NMAction.html#setTinyIcon(javax.swing.Icon)">setTinyIcon</a>, <a href="../../actions/NMAction.html#shallowClone()">shallowClone</a>, <a href="../../actions/NMAction.html#toString()">toString</a></code></div>
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
<section class="detail" id="MANAGER_CHANGED">
<h3>MANAGER_CHANGED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MANAGER_CHANGED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.PropertyAction.MANAGER_CHANGED">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.properties.PropertyManager,java.lang.String)">
<h3>PropertyAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PropertyAction</span><wbr/><span class="parameters">(<a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyID)</span></div>
<div class="block">The constructor for action with given property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - property manager</dd>
<dd><code>propertyID</code> - id of the property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.magicdraw.properties.PropertyManager,java.lang.String)">
<h3>PropertyAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PropertyAction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyID)</span></div>
<div class="block">The constructor for action with given property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionID</code> - id of the action</dd>
<dd><code>manager</code> - property manager</dd>
<dd><code>propertyID</code> - id of the property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.magicdraw.properties.PropertyManager,java.lang.String,boolean)">
<h3>PropertyAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PropertyAction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyID,
 boolean useShortcutSchema)</span></div>
<div class="block">The constructor for action with given property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionID</code> - id of the action</dd>
<dd><code>manager</code> - property manager</dd>
<dd><code>propertyID</code> - id of the property</dd>
<dd><code>useShortcutSchema</code> - use shortcuts schema for this action</dd>
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
<section class="detail" id="propertyChange(java.beans.PropertyChangeEvent)">
<h3>propertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans">propertyChange</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans"><code>PropertyChangeListener.propertyChange(java.beans.PropertyChangeEvent)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNewValue(java.lang.Object)">
<h3>setNewValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNewValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block">Sets the new property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>newValue</code> - the new property value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNewValue()">
<h3>getNewValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getNewValue</span>()</div>
<div class="block">Gets the new property value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new property value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperty()">
<h3>getProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span> <span class="element-name">getProperty</span>()</div>
<div class="block">Returns the property.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>returns an assigned property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="changePropertyValue(java.lang.Object)">
<h3>changePropertyValue</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">changePropertyValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block">Change value of a property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>newValue</code> - new value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.actions.ActionsVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../../actions/ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a> visitor)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../../actions/NMAction.html#accept(com.nomagic.actions.ActionsVisitor)">NMAction</a></code></span></div>
<div class="block">Accepts ActionsVisitor using Visitor pattern.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../actions/NMAction.html#accept(com.nomagic.actions.ActionsVisitor)">accept</a></code> in class <code><a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - visitor to accept.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManager()">
<h3>getManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getManager</span>()</div>
<div class="block">Get the manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>returns the manager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setManager(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>setManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManager</span><wbr/><span class="parameters">(<a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</span></div>
<div class="block">Set the manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - the new manager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireManagerChanged(com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.magicdraw.properties.PropertyManager)">
<h3>fireManagerChanged</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">fireManagerChanged</span><wbr/><span class="parameters">(<a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> oldManager,
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> newManager)</span></div>
<div class="block">Fires the notification about the property manager change</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>oldManager</code> - old manager</dd>
<dd><code>newManager</code> - new manager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyID()">
<h3>getPropertyID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPropertyID</span>()</div>
<div class="block">Get the property id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Returns the id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPropertyId(java.lang.String)">
<h3>setPropertyId</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setPropertyId</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Sets property id</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - property id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addChangeListener(java.beans.PropertyChangeListener)">
<h3>addChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Add the listener which will be notified about the
 change of underlying property manager of this action</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - for property change notifications</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addChangeListener(java.lang.String,java.beans.PropertyChangeListener)">
<h3>addChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Add the listener which will be notified about the
 change of underlying property manager of this action</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - the listener will be notified only about this property changes</dd>
<dd><code>listener</code> - for property change notifications</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#MANAGER_CHANGED"><code>MANAGER_CHANGED</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeChangeListener(java.beans.PropertyChangeListener)">
<h3>removeChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Remove the listener from this action</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - to be removed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeChangeListener(java.lang.String,java.beans.PropertyChangeListener)">
<h3>removeChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Remove the listener from this action</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - the name of the property</dd>
<dd><code>listener</code> - to be removed</dd>
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
