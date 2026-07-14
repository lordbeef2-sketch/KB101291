# JAVA OPENAPI: BaseCustomizableDiagramAction (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/ui/diagrams/BaseCustomizableDiagramAction.html
- source_path: `com/nomagic/magicdraw/ui/diagrams/BaseCustomizableDiagramAction.html`
- source_sha256: `7c0cf237e541bf7d747b3f597753f2482775f09c13990ed02078b7714e5c1c5f`
- captured_utc: `2026-07-14T16:58:25.147146+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.diagrams](package-summary.html)

## Class BaseCustomizableDiagramAction

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[javax.swing.AbstractAction](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html)
[com.nomagic.actions.NMAction](../../../actions/NMAction.html)
[com.nomagic.actions.BaseNMStateAction](../../../actions/BaseNMStateAction.html)
[com.nomagic.actions.NMStateAction](../../../actions/NMStateAction.html)
[com.nomagic.magicdraw.actions.MDStateAction](../../actions/MDStateAction.html)
[com.dassault_systemes.modeler.magic.ui.diagrams.actions.DefaultAbstractDiagramStateAction](../../../../dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramStateAction.html)
com.dassault_systemes.modeler.magic.ui.diagrams.actions.BaseAbstractDiagramAction
com.nomagic.magicdraw.ui.actions.BaseDiagramAction
com.nomagic.magicdraw.ui.diagrams.BaseCustomizableDiagramAction

All Implemented Interfaces:
`com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction`, `com.nomagic.magicdraw.actions.ShortcutSchemaAction`, `[ActionListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)`, `[Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html)`

Direct Known Subclasses:
`[DrawShapeDiagramAction](../actions/DrawShapeDiagramAction.html)`

@OpenApiAllpublic classBaseCustomizableDiagramAction
extends com.nomagic.magicdraw.ui.actions.BaseDiagramAction

Action which can be customized in custom diagram descriptor UI.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.ui.diagrams.BaseCustomizableDiagramAction)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction`
`[customAdditionalDrawAction](#customAdditionalDrawAction)`
Fields inherited from class com.nomagic.actions.[NMStateAction](../../../actions/NMStateAction.html)
`[DISTINGUISH](../../../actions/NMStateAction.html#DISTINGUISH), [STATE](../../../actions/NMStateAction.html#STATE)`
Fields inherited from class com.nomagic.actions.[BaseNMStateAction](../../../actions/BaseNMStateAction.html)
`[GROUPED](../../../actions/BaseNMStateAction.html#GROUPED)`
Fields inherited from class com.nomagic.actions.[NMAction](../../../actions/NMAction.html)
`[ACTION_SHORTCUTS](../../../actions/NMAction.html#ACTION_SHORTCUTS), [BELONGS_TO_SEPARATE_GROUP_IN_UI](../../../actions/NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI), [DO_NO_SHOW_ACTION_NAME_IN_UI](../../../actions/NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI), [DO_NOT_REGISTER_ACTION_TO_COMPONENTS](../../../actions/NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS), [GENERATED_ID_PREFIX](../../../actions/NMAction.html#GENERATED_ID_PREFIX), [GROUP](../../../actions/NMAction.html#GROUP), [ID](../../../actions/NMAction.html#ID), [LARGE_ICON](../../../actions/NMAction.html#LARGE_ICON), [MENU_SHORTCUT_MASK](../../../actions/NMAction.html#MENU_SHORTCUT_MASK), [TINY_ICON](../../../actions/NMAction.html#TINY_ICON)`
Fields inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[changeSupport](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#changeSupport), [enabled](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#enabled)`
Fields inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html)
`[ACCELERATOR_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#ACCELERATOR_KEY), [ACTION_COMMAND_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#ACTION_COMMAND_KEY), [DEFAULT](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#DEFAULT), [DISPLAYED_MNEMONIC_INDEX_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#DISPLAYED_MNEMONIC_INDEX_KEY), [LARGE_ICON_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#LARGE_ICON_KEY), [LONG_DESCRIPTION](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#LONG_DESCRIPTION), [MNEMONIC_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#MNEMONIC_KEY), [NAME](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#NAME), [SELECTED_KEY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SELECTED_KEY), [SHORT_DESCRIPTION](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SHORT_DESCRIPTION), [SMALL_ICON](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#SMALL_ICON)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[BaseCustomizableDiagramAction](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) actionID,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) actionName,
 [KeyStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/KeyStroke.html) key)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[BaseCustomizableDiagramAction](BaseCustomizableDiagramAction.html)`
`[clone](#clone())()`
Clones the object.
`com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction`
`[getCustomAdditionalDrawAction](#getCustomAdditionalDrawAction())()`
Returns custom additional draw action for this action.
`com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction`
`[getDefaultAdditionalDrawAction](#getDefaultAdditionalDrawAction())()`
Returns default additional draw action for this action
`protected [ResizableIcon](../../../ui/ResizableIcon.html)`
`[getDefaultIcon](#getDefaultIcon())()`

`com.nomagic.magicdraw.ui.diagrams.IconCollection`
`[getIcons](#getIcons())()`

`[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
`[getLargeIcon](#getLargeIcon())()`
Returns the large icon of the action.
`[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
`[getSmallIcon](#getSmallIcon())()`
Returns the small icon of the action.
`[PropertyManager](../../properties/PropertyManager.html)`
`[getStyle](#getStyle())()`

`void`
`[setCustomAdditionalDrawAction](#setCustomAdditionalDrawAction(com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction))(com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction customAdditionalDrawAction)`
Set custom additional draw action for this action.
`void`
`[setDescription](#setDescription(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description)`
Sets new action description.
`void`
`[setIcons](#setIcons(com.nomagic.magicdraw.ui.diagrams.IconCollection))(com.nomagic.magicdraw.ui.diagrams.IconCollection icons)`

`void`
`[setStyle](#setStyle(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](../../properties/PropertyManager.html) style)`

`void`
`[setStyle](#setStyle(com.nomagic.magicdraw.ui.diagrams.PropertyManagerProxy))(com.nomagic.magicdraw.ui.diagrams.PropertyManagerProxy style)`
Methods inherited from class com.nomagic.magicdraw.ui.actions.BaseDiagramAction
`getDiagramActionsExecuter, getElementCreatorInfo, isAllowedToCreateSymbol`
Methods inherited from class com.dassault_systemes.modeler.magic.ui.diagrams.actions.BaseAbstractDiagramAction
`actionPerformed, getCanvas, getProject, isEnabledInRODiagram, replaceState, replaceWithSelectionActionState, setEnabledInRODiagram, updateState`
Methods inherited from class com.dassault_systemes.modeler.magic.ui.diagrams.actions.[DefaultAbstractDiagramStateAction](../../../../dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramStateAction.html)
`[getDiagram](../../../../dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramStateAction.html#getDiagram()), [getFirstSelected](../../../../dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramStateAction.html#getFirstSelected()), [getSelected](../../../../dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramStateAction.html#getSelected()), [setDiagram](../../../../dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramStateAction.html#setDiagram(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))`
Methods inherited from class com.nomagic.magicdraw.actions.[MDStateAction](../../actions/MDStateAction.html)
`[isUseShortcutSchema](../../actions/MDStateAction.html#isUseShortcutSchema())`
Methods inherited from class com.nomagic.actions.[NMStateAction](../../../actions/NMStateAction.html)
`[accept](../../../actions/NMStateAction.html#accept(com.nomagic.actions.ActionsVisitor)), [getState](../../../actions/NMStateAction.html#getState()), [isDistinguish](../../../actions/NMStateAction.html#isDistinguish()), [isStateEvent](../../../actions/NMStateAction.html#isStateEvent(java.beans.PropertyChangeEvent)), [setDistinguish](../../../actions/NMStateAction.html#setDistinguish(boolean)), [setState](../../../actions/NMStateAction.html#setState(boolean))`
Methods inherited from class com.nomagic.actions.[BaseNMStateAction](../../../actions/BaseNMStateAction.html)
`[isGrouped](../../../actions/BaseNMStateAction.html#isGrouped()), [setGrouped](../../../actions/BaseNMStateAction.html#setGrouped(boolean))`
Methods inherited from class com.nomagic.actions.[NMAction](../../../actions/NMAction.html)
`[addAction](../../../actions/NMAction.html#addAction(com.nomagic.actions.NMAction)), [addPropertyChangeListener](../../../actions/NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addShortcut](../../../actions/NMAction.html#addShortcut(javax.swing.KeyStroke)), [addShotcut](../../../actions/NMAction.html#addShotcut(javax.swing.KeyStroke)), [addWeakPropertyChangeListener](../../../actions/NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [compareTo](../../../actions/NMAction.html#compareTo(java.lang.Object)), [createMenuItem](../../../actions/NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)), [equals](../../../actions/NMAction.html#equals(java.lang.Object)), [firePropertyChange](../../../actions/NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [forEach](../../../actions/NMAction.html#forEach(java.util.function.Consumer)), [forEachIncludingSelf](../../../actions/NMAction.html#forEachIncludingSelf(java.util.function.Consumer)), [getActions](../../../actions/NMAction.html#getActions()), [getCommandKey](../../../actions/NMAction.html#getCommandKey()), [getDescription](../../../actions/NMAction.html#getDescription()), [getGroup](../../../actions/NMAction.html#getGroup()), [getIcon](../../../actions/NMAction.html#getIcon()), [getID](../../../actions/NMAction.html#getID()), [getLargeOrSmallIcon](../../../actions/NMAction.html#getLargeOrSmallIcon()), [getMenuShortcutMaskAsString](../../../actions/NMAction.html#getMenuShortcutMaskAsString()), [getMnemonicKey](../../../actions/NMAction.html#getMnemonicKey()), [getName](../../../actions/NMAction.html#getName()), [getPropertyChangeListeners](../../../actions/NMAction.html#getPropertyChangeListeners()), [getShortcuts](../../../actions/NMAction.html#getShortcuts()), [getSmallOrLargeIcon](../../../actions/NMAction.html#getSmallOrLargeIcon()), [getTinyIcon](../../../actions/NMAction.html#getTinyIcon()), [hashCode](../../../actions/NMAction.html#hashCode()), [hasMenuShortcutMask](../../../actions/NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)), [isIDGenerated](../../../actions/NMAction.html#isIDGenerated()), [removeAction](../../../actions/NMAction.html#removeAction(com.nomagic.actions.NMAction)), [removeIf](../../../actions/NMAction.html#removeIf(java.util.function.Predicate)), [removePropertyChangeListener](../../../actions/NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [removeShortcut](../../../actions/NMAction.html#removeShortcut(javax.swing.KeyStroke)), [removeWeakPropertyChangeListener](../../../actions/NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [setActions](../../../actions/NMAction.html#setActions(java.util.List)), [setGroup](../../../actions/NMAction.html#setGroup(java.lang.String)), [setIcon](../../../actions/NMAction.html#setIcon(javax.swing.Icon)), [setLargeIcon](../../../actions/NMAction.html#setLargeIcon(javax.swing.Icon)), [setMnemonicKey](../../../actions/NMAction.html#setMnemonicKey(int)), [setName](../../../actions/NMAction.html#setName(java.lang.String)), [setShortcuts](../../../actions/NMAction.html#setShortcuts(java.util.List)), [setSmallIcon](../../../actions/NMAction.html#setSmallIcon(javax.swing.Icon)), [setTinyIcon](../../../actions/NMAction.html#setTinyIcon(javax.swing.Icon)), [shallowClone](../../../actions/NMAction.html#shallowClone()), [toString](../../../actions/NMAction.html#toString())`
Methods inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[getKeys](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()), [getValue](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)), [isEnabled](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()), [putValue](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)), [setEnabled](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html)
`[accept](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object))`

============ FIELD DETAIL =========== 
Field Details
customAdditionalDrawAction
@CheckForNullprotected com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction customAdditionalDrawAction
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
BaseCustomizableDiagramAction
public BaseCustomizableDiagramAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) actionID,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) actionName,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/KeyStroke.html) key)
 ============ METHOD DETAIL ========== 
Method Details
getIcons
public com.nomagic.magicdraw.ui.diagrams.IconCollection getIcons()
setIcons
public void setIcons(com.nomagic.magicdraw.ui.diagrams.IconCollection icons)
getLargeIcon
@CheckForNullpublic [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) getLargeIcon()
Description copied from class: `[NMAction](../../../actions/NMAction.html#getLargeIcon())`
Returns the large icon of the action.
Overrides:
`[getLargeIcon](../../../actions/NMAction.html#getLargeIcon())` in class `[NMAction](../../../actions/NMAction.html)`
Returns:
the large icon of the action.
getSmallIcon
@CheckForNullpublic [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) getSmallIcon()
Description copied from class: `[NMAction](../../../actions/NMAction.html#getSmallIcon())`
Returns the small icon of the action.
Overrides:
`[getSmallIcon](../../../actions/NMAction.html#getSmallIcon())` in class `[NMAction](../../../actions/NMAction.html)`
Returns:
the small icon of the action.
getDefaultIcon
@CheckForNullprotected [ResizableIcon](../../../ui/ResizableIcon.html) getDefaultIcon()
setDescription
public void setDescription(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description)
Description copied from class: `[NMAction](../../../actions/NMAction.html#setDescription(java.lang.String))`
Sets new action description.
Overrides:
`[setDescription](../../../actions/NMAction.html#setDescription(java.lang.String))` in class `[NMAction](../../../actions/NMAction.html)`
Parameters:
`description` - action description.
clone
public [BaseCustomizableDiagramAction](BaseCustomizableDiagramAction.html) clone()
Description copied from class: `[NMAction](../../../actions/NMAction.html#clone())`
Clones the object.
 Does the deep clone.
Overrides:
`clone` in class `com.nomagic.magicdraw.ui.actions.BaseDiagramAction`
Returns:
cloned object
getStyle
@CheckForNullpublic [PropertyManager](../../properties/PropertyManager.html) getStyle()
setStyle
public void setStyle(@CheckForNull
 [PropertyManager](../../properties/PropertyManager.html) style)
setStyle
public void setStyle(@CheckForNull
 com.nomagic.magicdraw.ui.diagrams.PropertyManagerProxy style)
getCustomAdditionalDrawAction
@CheckForNullpublic com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction getCustomAdditionalDrawAction()
Returns custom additional draw action for this action.
Returns:
additional draw action
getDefaultAdditionalDrawAction
@CheckForNullpublic com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction getDefaultAdditionalDrawAction()
Returns default additional draw action for this action
Returns:
default additional draw action
setCustomAdditionalDrawAction
public void setCustomAdditionalDrawAction(@CheckForNull
 com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction customAdditionalDrawAction)
Set custom additional draw action for this action. This draw action will be used if not null.
Parameters:
`customAdditionalDrawAction` - custom additional draw action

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.diagrams</a></div>
<h1 class="title" title="Class BaseCustomizableDiagramAction">Class BaseCustomizableDiagramAction</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">javax.swing.AbstractAction</a>
<div class="inheritance"><a href="../../../actions/NMAction.html" title="class in com.nomagic.actions">com.nomagic.actions.NMAction</a>
<div class="inheritance"><a href="../../../actions/BaseNMStateAction.html" title="class in com.nomagic.actions">com.nomagic.actions.BaseNMStateAction</a>
<div class="inheritance"><a href="../../../actions/NMStateAction.html" title="class in com.nomagic.actions">com.nomagic.actions.NMStateAction</a>
<div class="inheritance"><a href="../../actions/MDStateAction.html" title="class in com.nomagic.magicdraw.actions">com.nomagic.magicdraw.actions.MDStateAction</a>
<div class="inheritance"><a href="../../../../dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramStateAction.html" title="class in com.dassault_systemes.modeler.magic.ui.diagrams.actions">com.dassault_systemes.modeler.magic.ui.diagrams.actions.DefaultAbstractDiagramStateAction</a>
<div class="inheritance">com.dassault_systemes.modeler.magic.ui.diagrams.actions.BaseAbstractDiagramAction
<div class="inheritance">com.nomagic.magicdraw.ui.actions.BaseDiagramAction
<div class="inheritance">com.nomagic.magicdraw.ui.diagrams.BaseCustomizableDiagramAction</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction</code>, <code>com.nomagic.magicdraw.actions.ShortcutSchemaAction</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../actions/DrawShapeDiagramAction.html" title="class in com.nomagic.magicdraw.ui.actions">DrawShapeDiagramAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">BaseCustomizableDiagramAction</span>
<span class="extends-implements">extends com.nomagic.magicdraw.ui.actions.BaseDiagramAction</span></div>
<div class="block">Action which can be customized in custom diagram descriptor UI.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.ui.diagrams.BaseCustomizableDiagramAction">Serialized Form</a></li>
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
<div class="col-first even-row-color"><code>protected com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#customAdditionalDrawAction">customAdditionalDrawAction</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.actions.NMStateAction">Fields inherited from class com.nomagic.actions.<a href="../../../actions/NMStateAction.html" title="class in com.nomagic.actions">NMStateAction</a></h3>
<code><a href="../../../actions/NMStateAction.html#DISTINGUISH">DISTINGUISH</a>, <a href="../../../actions/NMStateAction.html#STATE">STATE</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.actions.BaseNMStateAction">Fields inherited from class com.nomagic.actions.<a href="../../../actions/BaseNMStateAction.html" title="class in com.nomagic.actions">BaseNMStateAction</a></h3>
<code><a href="../../../actions/BaseNMStateAction.html#GROUPED">GROUPED</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.actions.NMAction">Fields inherited from class com.nomagic.actions.<a href="../../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="../../../actions/NMAction.html#ACTION_SHORTCUTS">ACTION_SHORTCUTS</a>, <a href="../../../actions/NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI">BELONGS_TO_SEPARATE_GROUP_IN_UI</a>, <a href="../../../actions/NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI">DO_NO_SHOW_ACTION_NAME_IN_UI</a>, <a href="../../../actions/NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS">DO_NOT_REGISTER_ACTION_TO_COMPONENTS</a>, <a href="../../../actions/NMAction.html#GENERATED_ID_PREFIX">GENERATED_ID_PREFIX</a>, <a href="../../../actions/NMAction.html#GROUP">GROUP</a>, <a href="../../../actions/NMAction.html#ID">ID</a>, <a href="../../../actions/NMAction.html#LARGE_ICON">LARGE_ICON</a>, <a href="../../../actions/NMAction.html#MENU_SHORTCUT_MASK">MENU_SHORTCUT_MASK</a>, <a href="../../../actions/NMAction.html#TINY_ICON">TINY_ICON</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke)">BaseCustomizableDiagramAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> key)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BaseCustomizableDiagramAction.html" title="class in com.nomagic.magicdraw.ui.diagrams">BaseCustomizableDiagramAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomAdditionalDrawAction()">getCustomAdditionalDrawAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns custom additional draw action for this action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultAdditionalDrawAction()">getDefaultAdditionalDrawAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns default additional draw action for this action</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultIcon()">getDefaultIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.diagrams.IconCollection</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcons()">getIcons</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLargeIcon()">getLargeIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the large icon of the action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSmallIcon()">getSmallIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the small icon of the action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyle()">getStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCustomAdditionalDrawAction(com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction)">setCustomAdditionalDrawAction</a><wbr/>(com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction customAdditionalDrawAction)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set custom additional draw action for this action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDescription(java.lang.String)">setDescription</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new action description.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIcons(com.nomagic.magicdraw.ui.diagrams.IconCollection)">setIcons</a><wbr/>(com.nomagic.magicdraw.ui.diagrams.IconCollection icons)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStyle(com.nomagic.magicdraw.properties.PropertyManager)">setStyle</a><wbr/>(<a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> style)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStyle(com.nomagic.magicdraw.ui.diagrams.PropertyManagerProxy)">setStyle</a><wbr/>(com.nomagic.magicdraw.ui.diagrams.PropertyManagerProxy style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.ui.actions.BaseDiagramAction">Methods inherited from class com.nomagic.magicdraw.ui.actions.BaseDiagramAction</h3>
<code>getDiagramActionsExecuter, getElementCreatorInfo, isAllowedToCreateSymbol</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.magic.ui.diagrams.actions.BaseAbstractDiagramAction">Methods inherited from class com.dassault_systemes.modeler.magic.ui.diagrams.actions.BaseAbstractDiagramAction</h3>
<code>actionPerformed, getCanvas, getProject, isEnabledInRODiagram, replaceState, replaceWithSelectionActionState, setEnabledInRODiagram, updateState</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.magic.ui.diagrams.actions.DefaultAbstractDiagramStateAction">Methods inherited from class com.dassault_systemes.modeler.magic.ui.diagrams.actions.<a href="../../../../dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramStateAction.html" title="class in com.dassault_systemes.modeler.magic.ui.diagrams.actions">DefaultAbstractDiagramStateAction</a></h3>
<code><a href="../../../../dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramStateAction.html#getDiagram()">getDiagram</a>, <a href="../../../../dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramStateAction.html#getFirstSelected()">getFirstSelected</a>, <a href="../../../../dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramStateAction.html#getSelected()">getSelected</a>, <a href="../../../../dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramStateAction.html#setDiagram(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">setDiagram</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.actions.MDStateAction">Methods inherited from class com.nomagic.magicdraw.actions.<a href="../../actions/MDStateAction.html" title="class in com.nomagic.magicdraw.actions">MDStateAction</a></h3>
<code><a href="../../actions/MDStateAction.html#isUseShortcutSchema()">isUseShortcutSchema</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.NMStateAction">Methods inherited from class com.nomagic.actions.<a href="../../../actions/NMStateAction.html" title="class in com.nomagic.actions">NMStateAction</a></h3>
<code><a href="../../../actions/NMStateAction.html#accept(com.nomagic.actions.ActionsVisitor)">accept</a>, <a href="../../../actions/NMStateAction.html#getState()">getState</a>, <a href="../../../actions/NMStateAction.html#isDistinguish()">isDistinguish</a>, <a href="../../../actions/NMStateAction.html#isStateEvent(java.beans.PropertyChangeEvent)">isStateEvent</a>, <a href="../../../actions/NMStateAction.html#setDistinguish(boolean)">setDistinguish</a>, <a href="../../../actions/NMStateAction.html#setState(boolean)">setState</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.BaseNMStateAction">Methods inherited from class com.nomagic.actions.<a href="../../../actions/BaseNMStateAction.html" title="class in com.nomagic.actions">BaseNMStateAction</a></h3>
<code><a href="../../../actions/BaseNMStateAction.html#isGrouped()">isGrouped</a>, <a href="../../../actions/BaseNMStateAction.html#setGrouped(boolean)">setGrouped</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.NMAction">Methods inherited from class com.nomagic.actions.<a href="../../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="../../../actions/NMAction.html#addAction(com.nomagic.actions.NMAction)">addAction</a>, <a href="../../../actions/NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../actions/NMAction.html#addShortcut(javax.swing.KeyStroke)">addShortcut</a>, <a href="../../../actions/NMAction.html#addShotcut(javax.swing.KeyStroke)">addShotcut</a>, <a href="../../../actions/NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)">addWeakPropertyChangeListener</a>, <a href="../../../actions/NMAction.html#compareTo(java.lang.Object)">compareTo</a>, <a href="../../../actions/NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)">createMenuItem</a>, <a href="../../../actions/NMAction.html#equals(java.lang.Object)">equals</a>, <a href="../../../actions/NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../actions/NMAction.html#forEach(java.util.function.Consumer)">forEach</a>, <a href="../../../actions/NMAction.html#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a>, <a href="../../../actions/NMAction.html#getActions()">getActions</a>, <a href="../../../actions/NMAction.html#getCommandKey()">getCommandKey</a>, <a href="../../../actions/NMAction.html#getDescription()">getDescription</a>, <a href="../../../actions/NMAction.html#getGroup()">getGroup</a>, <a href="../../../actions/NMAction.html#getIcon()">getIcon</a>, <a href="../../../actions/NMAction.html#getID()">getID</a>, <a href="../../../actions/NMAction.html#getLargeOrSmallIcon()">getLargeOrSmallIcon</a>, <a href="../../../actions/NMAction.html#getMenuShortcutMaskAsString()">getMenuShortcutMaskAsString</a>, <a href="../../../actions/NMAction.html#getMnemonicKey()">getMnemonicKey</a>, <a href="../../../actions/NMAction.html#getName()">getName</a>, <a href="../../../actions/NMAction.html#getPropertyChangeListeners()">getPropertyChangeListeners</a>, <a href="../../../actions/NMAction.html#getShortcuts()">getShortcuts</a>, <a href="../../../actions/NMAction.html#getSmallOrLargeIcon()">getSmallOrLargeIcon</a>, <a href="../../../actions/NMAction.html#getTinyIcon()">getTinyIcon</a>, <a href="../../../actions/NMAction.html#hashCode()">hashCode</a>, <a href="../../../actions/NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)">hasMenuShortcutMask</a>, <a href="../../../actions/NMAction.html#isIDGenerated()">isIDGenerated</a>, <a href="../../../actions/NMAction.html#removeAction(com.nomagic.actions.NMAction)">removeAction</a>, <a href="../../../actions/NMAction.html#removeIf(java.util.function.Predicate)">removeIf</a>, <a href="../../../actions/NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../actions/NMAction.html#removeShortcut(javax.swing.KeyStroke)">removeShortcut</a>, <a href="../../../actions/NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)">removeWeakPropertyChangeListener</a>, <a href="../../../actions/NMAction.html#setActions(java.util.List)">setActions</a>, <a href="../../../actions/NMAction.html#setGroup(java.lang.String)">setGroup</a>, <a href="../../../actions/NMAction.html#setIcon(javax.swing.Icon)">setIcon</a>, <a href="../../../actions/NMAction.html#setLargeIcon(javax.swing.Icon)">setLargeIcon</a>, <a href="../../../actions/NMAction.html#setMnemonicKey(int)">setMnemonicKey</a>, <a href="../../../actions/NMAction.html#setName(java.lang.String)">setName</a>, <a href="../../../actions/NMAction.html#setShortcuts(java.util.List)">setShortcuts</a>, <a href="../../../actions/NMAction.html#setSmallIcon(javax.swing.Icon)">setSmallIcon</a>, <a href="../../../actions/NMAction.html#setTinyIcon(javax.swing.Icon)">setTinyIcon</a>, <a href="../../../actions/NMAction.html#shallowClone()">shallowClone</a>, <a href="../../../actions/NMAction.html#toString()">toString</a></code></div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="customAdditionalDrawAction">
<h3>customAdditionalDrawAction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction</span> <span class="element-name">customAdditionalDrawAction</span></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,javax.swing.KeyStroke)">
<h3>BaseCustomizableDiagramAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BaseCustomizableDiagramAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> key)</span></div>
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
<section class="detail" id="getIcons()">
<h3>getIcons</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.diagrams.IconCollection</span> <span class="element-name">getIcons</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setIcons(com.nomagic.magicdraw.ui.diagrams.IconCollection)">
<h3>setIcons</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIcons</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.diagrams.IconCollection icons)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLargeIcon()">
<h3>getLargeIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getLargeIcon</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="../../../actions/NMAction.html#getLargeIcon()">NMAction</a></code></span></div>
<div class="block">Returns the large icon of the action.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../../actions/NMAction.html#getLargeIcon()">getLargeIcon</a></code> in class <code><a href="../../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Returns:</dt>
<dd>the large icon of the action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSmallIcon()">
<h3>getSmallIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getSmallIcon</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="../../../actions/NMAction.html#getSmallIcon()">NMAction</a></code></span></div>
<div class="block">Returns the small icon of the action.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../../actions/NMAction.html#getSmallIcon()">getSmallIcon</a></code> in class <code><a href="../../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Returns:</dt>
<dd>the small icon of the action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultIcon()">
<h3>getDefaultIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getDefaultIcon</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDescription(java.lang.String)">
<h3>setDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDescription</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="../../../actions/NMAction.html#setDescription(java.lang.String)">NMAction</a></code></span></div>
<div class="block">Sets new action description.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../../actions/NMAction.html#setDescription(java.lang.String)">setDescription</a></code> in class <code><a href="../../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></dd>
<dt>Parameters:</dt>
<dd><code>description</code> - action description.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BaseCustomizableDiagramAction.html" title="class in com.nomagic.magicdraw.ui.diagrams">BaseCustomizableDiagramAction</a></span> <span class="element-name">clone</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="../../../actions/NMAction.html#clone()">NMAction</a></code></span></div>
<div class="block">Clones the object.
 Does the deep clone.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>clone</code> in class <code>com.nomagic.magicdraw.ui.actions.BaseDiagramAction</code></dd>
<dt>Returns:</dt>
<dd>cloned object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStyle()">
<h3>getStyle</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getStyle</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setStyle(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>setStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStyle</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> style)</span></div>
</section>
</li>
<li>
<section class="detail" id="setStyle(com.nomagic.magicdraw.ui.diagrams.PropertyManagerProxy)">
<h3>setStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStyle</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.magicdraw.ui.diagrams.PropertyManagerProxy style)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCustomAdditionalDrawAction()">
<h3>getCustomAdditionalDrawAction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction</span> <span class="element-name">getCustomAdditionalDrawAction</span>()</div>
<div class="block">Returns custom additional draw action for this action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>additional draw action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultAdditionalDrawAction()">
<h3>getDefaultAdditionalDrawAction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction</span> <span class="element-name">getDefaultAdditionalDrawAction</span>()</div>
<div class="block">Returns default additional draw action for this action</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>default additional draw action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCustomAdditionalDrawAction(com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction)">
<h3>setCustomAdditionalDrawAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomAdditionalDrawAction</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.magicdraw.uml.symbols.manipulators.drawactions.AdditionalDrawAction customAdditionalDrawAction)</span></div>
<div class="block">Set custom additional draw action for this action. This draw action will be used if not null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>customAdditionalDrawAction</code> - custom additional draw action</dd>
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
