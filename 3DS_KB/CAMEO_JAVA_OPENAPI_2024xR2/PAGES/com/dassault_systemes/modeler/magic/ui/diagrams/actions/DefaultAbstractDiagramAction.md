# JAVA OPENAPI: DefaultAbstractDiagramAction (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramAction.html
- source_path: `com/dassault_systemes/modeler/magic/ui/diagrams/actions/DefaultAbstractDiagramAction.html`
- source_sha256: `0406d39d383ed81b972ff999a1157613f8dd8b59ba248dce4d15ad11d935c67f`
- captured_utc: `2026-07-14T16:55:00.733844+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.magic.ui.diagrams.actions](package-summary.html)

## Class DefaultAbstractDiagramAction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[javax.swing.AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
[com.nomagic.actions.NMAction](../../../../../../nomagic/actions/NMAction.html)
[com.nomagic.magicdraw.actions.MDAction](../../../../../../nomagic/magicdraw/actions/MDAction.html)
com.dassault_systemes.modeler.magic.ui.diagrams.actions.DefaultAbstractDiagramAction

All Implemented Interfaces:
`com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction`, `com.nomagic.magicdraw.actions.ShortcutSchemaAction`, `[ActionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`, `[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)`

Direct Known Subclasses:
`[DefaultDiagramAction](../../../../../../nomagic/magicdraw/ui/actions/DefaultDiagramAction.html)`

@OpenApiAllpublic classDefaultAbstractDiagramAction
extends [MDAction](../../../../../../nomagic/magicdraw/actions/MDAction.html)
implements com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction

The default implementation of `AbstractDiagramAction` and simple MDAction

See Also:
[Serialized Form](../../../../../../../serialized-form.html#com.dassault_systemes.modeler.magic.ui.diagrams.actions.DefaultAbstractDiagramAction)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.actions.[NMAction](../../../../../../nomagic/actions/NMAction.html)
`[ACTION_SHORTCUTS](../../../../../../nomagic/actions/NMAction.html#ACTION_SHORTCUTS), [BELONGS_TO_SEPARATE_GROUP_IN_UI](../../../../../../nomagic/actions/NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI), [DO_NO_SHOW_ACTION_NAME_IN_UI](../../../../../../nomagic/actions/NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI), [DO_NOT_REGISTER_ACTION_TO_COMPONENTS](../../../../../../nomagic/actions/NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS), [GENERATED_ID_PREFIX](../../../../../../nomagic/actions/NMAction.html#GENERATED_ID_PREFIX), [GROUP](../../../../../../nomagic/actions/NMAction.html#GROUP), [ID](../../../../../../nomagic/actions/NMAction.html#ID), [LARGE_ICON](../../../../../../nomagic/actions/NMAction.html#LARGE_ICON), [MENU_SHORTCUT_MASK](../../../../../../nomagic/actions/NMAction.html#MENU_SHORTCUT_MASK), [TINY_ICON](../../../../../../nomagic/actions/NMAction.html#TINY_ICON)`
Fields inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[changeSupport](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#changeSupport), [enabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#enabled)`
Fields inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[ACCELERATOR_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACCELERATOR_KEY), [ACTION_COMMAND_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#ACTION_COMMAND_KEY), [DEFAULT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DEFAULT), [DISPLAYED_MNEMONIC_INDEX_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#DISPLAYED_MNEMONIC_INDEX_KEY), [LARGE_ICON_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LARGE_ICON_KEY), [LONG_DESCRIPTION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#LONG_DESCRIPTION), [MNEMONIC_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#MNEMONIC_KEY), [NAME](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#NAME), [SELECTED_KEY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SELECTED_KEY), [SHORT_DESCRIPTION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SHORT_DESCRIPTION), [SMALL_ICON](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#SMALL_ICON)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DefaultAbstractDiagramAction](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionName,
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`
Constructs new action.
`[DefaultAbstractDiagramAction](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionName,
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 boolean useSchema)`
Constructs new action.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[AbstractDiagramPresentationElement](../../../../../../nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html)`
`[getDiagram](#getDiagram())()`
Returns diagram of this action.
`protected [PresentationElement](../../../../../../nomagic/magicdraw/uml/symbols/PresentationElement.html)`
`[getFirstSelected](#getFirstSelected())()`
Returns first selected presentation element in the diagram.
`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../../../../../../nomagic/magicdraw/uml/symbols/PresentationElement.html)>`
`[getSelected](#getSelected())()`
Returns list of selected presentation elements.
`void`
`[setDiagram](#setDiagram(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../../../../../../nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html) diagram)`
Sets diagram for this action.
Methods inherited from class com.nomagic.magicdraw.actions.[MDAction](../../../../../../nomagic/magicdraw/actions/MDAction.html)
`[actionPerformed](../../../../../../nomagic/magicdraw/actions/MDAction.html#actionPerformed(java.awt.event.ActionEvent)), [isUseShortcutSchema](../../../../../../nomagic/magicdraw/actions/MDAction.html#isUseShortcutSchema()), [updateState](../../../../../../nomagic/magicdraw/actions/MDAction.html#updateState())`
Methods inherited from class com.nomagic.actions.[NMAction](../../../../../../nomagic/actions/NMAction.html)
`[accept](../../../../../../nomagic/actions/NMAction.html#accept(com.nomagic.actions.ActionsVisitor)), [addAction](../../../../../../nomagic/actions/NMAction.html#addAction(com.nomagic.actions.NMAction)), [addPropertyChangeListener](../../../../../../nomagic/actions/NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addShortcut](../../../../../../nomagic/actions/NMAction.html#addShortcut(javax.swing.KeyStroke)), [addShotcut](../../../../../../nomagic/actions/NMAction.html#addShotcut(javax.swing.KeyStroke)), [addWeakPropertyChangeListener](../../../../../../nomagic/actions/NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [clone](../../../../../../nomagic/actions/NMAction.html#clone()), [compareTo](../../../../../../nomagic/actions/NMAction.html#compareTo(java.lang.Object)), [createMenuItem](../../../../../../nomagic/actions/NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)), [equals](../../../../../../nomagic/actions/NMAction.html#equals(java.lang.Object)), [firePropertyChange](../../../../../../nomagic/actions/NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [forEach](../../../../../../nomagic/actions/NMAction.html#forEach(java.util.function.Consumer)), [forEachIncludingSelf](../../../../../../nomagic/actions/NMAction.html#forEachIncludingSelf(java.util.function.Consumer)), [getActions](../../../../../../nomagic/actions/NMAction.html#getActions()), [getCommandKey](../../../../../../nomagic/actions/NMAction.html#getCommandKey()), [getDescription](../../../../../../nomagic/actions/NMAction.html#getDescription()), [getGroup](../../../../../../nomagic/actions/NMAction.html#getGroup()), [getIcon](../../../../../../nomagic/actions/NMAction.html#getIcon()), [getID](../../../../../../nomagic/actions/NMAction.html#getID()), [getLargeIcon](../../../../../../nomagic/actions/NMAction.html#getLargeIcon()), [getLargeOrSmallIcon](../../../../../../nomagic/actions/NMAction.html#getLargeOrSmallIcon()), [getMenuShortcutMaskAsString](../../../../../../nomagic/actions/NMAction.html#getMenuShortcutMaskAsString()), [getMnemonicKey](../../../../../../nomagic/actions/NMAction.html#getMnemonicKey()), [getName](../../../../../../nomagic/actions/NMAction.html#getName()), [getPropertyChangeListeners](../../../../../../nomagic/actions/NMAction.html#getPropertyChangeListeners()), [getShortcuts](../../../../../../nomagic/actions/NMAction.html#getShortcuts()), [getSmallIcon](../../../../../../nomagic/actions/NMAction.html#getSmallIcon()), [getSmallOrLargeIcon](../../../../../../nomagic/actions/NMAction.html#getSmallOrLargeIcon()), [getTinyIcon](../../../../../../nomagic/actions/NMAction.html#getTinyIcon()), [hashCode](../../../../../../nomagic/actions/NMAction.html#hashCode()), [hasMenuShortcutMask](../../../../../../nomagic/actions/NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)), [isIDGenerated](../../../../../../nomagic/actions/NMAction.html#isIDGenerated()), [removeAction](../../../../../../nomagic/actions/NMAction.html#removeAction(com.nomagic.actions.NMAction)), [removeIf](../../../../../../nomagic/actions/NMAction.html#removeIf(java.util.function.Predicate)), [removePropertyChangeListener](../../../../../../nomagic/actions/NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [removeShortcut](../../../../../../nomagic/actions/NMAction.html#removeShortcut(javax.swing.KeyStroke)), [removeWeakPropertyChangeListener](../../../../../../nomagic/actions/NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)), [setActions](../../../../../../nomagic/actions/NMAction.html#setActions(java.util.List)), [setDescription](../../../../../../nomagic/actions/NMAction.html#setDescription(java.lang.String)), [setGroup](../../../../../../nomagic/actions/NMAction.html#setGroup(java.lang.String)), [setIcon](../../../../../../nomagic/actions/NMAction.html#setIcon(javax.swing.Icon)), [setLargeIcon](../../../../../../nomagic/actions/NMAction.html#setLargeIcon(javax.swing.Icon)), [setMnemonicKey](../../../../../../nomagic/actions/NMAction.html#setMnemonicKey(int)), [setName](../../../../../../nomagic/actions/NMAction.html#setName(java.lang.String)), [setShortcuts](../../../../../../nomagic/actions/NMAction.html#setShortcuts(java.util.List)), [setSmallIcon](../../../../../../nomagic/actions/NMAction.html#setSmallIcon(javax.swing.Icon)), [setTinyIcon](../../../../../../nomagic/actions/NMAction.html#setTinyIcon(javax.swing.Icon)), [shallowClone](../../../../../../nomagic/actions/NMAction.html#shallowClone()), [toString](../../../../../../nomagic/actions/NMAction.html#toString())`
Methods inherited from class javax.swing.[AbstractAction](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html)
`[getKeys](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getKeys()), [getValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#getValue(java.lang.String)), [isEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#isEnabled()), [putValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#putValue(java.lang.String,java.lang.Object)), [setEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html#setEnabled(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.[Action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html)
`[accept](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html#accept(java.lang.Object))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DefaultAbstractDiagramAction
public DefaultAbstractDiagramAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionName,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
Constructs new action.
Parameters:
`actionID` - the action ID
`actionName` - the action name
`stroke` - the action stroke
`group` - the action group
DefaultAbstractDiagramAction
public DefaultAbstractDiagramAction(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionID,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actionName,
 @CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 boolean useSchema)
Constructs new action.
Parameters:
`actionID` - the action ID
`actionName` - the action name
`stroke` - the action stroke
`group` - the action group
 ============ METHOD DETAIL ========== 
Method Details
setDiagram
public void setDiagram(@CheckForNull
 [AbstractDiagramPresentationElement](../../../../../../nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html) diagram)
Sets diagram for this action.
Specified by:
`setDiagram` in interface `com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction`
Parameters:
`diagram` - the given diagram
getDiagram
@CheckForNullpublic [AbstractDiagramPresentationElement](../../../../../../nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html) getDiagram()
Returns diagram of this action.
 MagicDraw framework guarantee that diagram will set if this method is called from updateState() or
 actionPerformed(ActionEvent) methods.
Returns:
set diagram
getFirstSelected
@CheckForNullprotected [PresentationElement](../../../../../../nomagic/magicdraw/uml/symbols/PresentationElement.html) getFirstSelected()
Returns first selected presentation element in the diagram.
Returns:
first selected presentation element
getSelected
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../../../../../../nomagic/magicdraw/uml/symbols/PresentationElement.html)> getSelected()
Returns list of selected presentation elements.
Returns:
list of selected presentation elements. If no elements selected, empty list is returned.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.magic.ui.diagrams.actions</a></div>
<h1 class="title" title="Class DefaultAbstractDiagramAction">Class DefaultAbstractDiagramAction</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractAction.html" title="class or interface in javax.swing">javax.swing.AbstractAction</a>
<div class="inheritance"><a href="../../../../../../nomagic/actions/NMAction.html" title="class in com.nomagic.actions">com.nomagic.actions.NMAction</a>
<div class="inheritance"><a href="../../../../../../nomagic/magicdraw/actions/MDAction.html" title="class in com.nomagic.magicdraw.actions">com.nomagic.magicdraw.actions.MDAction</a>
<div class="inheritance">com.dassault_systemes.modeler.magic.ui.diagrams.actions.DefaultAbstractDiagramAction</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction</code>, <code>com.nomagic.magicdraw.actions.ShortcutSchemaAction</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/ActionListener.html" title="class or interface in java.awt.event">ActionListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../../../../../../nomagic/magicdraw/ui/actions/DefaultDiagramAction.html" title="class in com.nomagic.magicdraw.ui.actions">DefaultDiagramAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DefaultAbstractDiagramAction</span>
<span class="extends-implements">extends <a href="../../../../../../nomagic/magicdraw/actions/MDAction.html" title="class in com.nomagic.magicdraw.actions">MDAction</a>
implements com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction</span></div>
<div class="block">The default implementation of <code>AbstractDiagramAction</code> and simple MDAction</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../../serialized-form.html#com.dassault_systemes.modeler.magic.ui.diagrams.actions.DefaultAbstractDiagramAction">Serialized Form</a></li>
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
<h3 id="fields-inherited-from-class-com.nomagic.actions.NMAction">Fields inherited from class com.nomagic.actions.<a href="../../../../../../nomagic/actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="../../../../../../nomagic/actions/NMAction.html#ACTION_SHORTCUTS">ACTION_SHORTCUTS</a>, <a href="../../../../../../nomagic/actions/NMAction.html#BELONGS_TO_SEPARATE_GROUP_IN_UI">BELONGS_TO_SEPARATE_GROUP_IN_UI</a>, <a href="../../../../../../nomagic/actions/NMAction.html#DO_NO_SHOW_ACTION_NAME_IN_UI">DO_NO_SHOW_ACTION_NAME_IN_UI</a>, <a href="../../../../../../nomagic/actions/NMAction.html#DO_NOT_REGISTER_ACTION_TO_COMPONENTS">DO_NOT_REGISTER_ACTION_TO_COMPONENTS</a>, <a href="../../../../../../nomagic/actions/NMAction.html#GENERATED_ID_PREFIX">GENERATED_ID_PREFIX</a>, <a href="../../../../../../nomagic/actions/NMAction.html#GROUP">GROUP</a>, <a href="../../../../../../nomagic/actions/NMAction.html#ID">ID</a>, <a href="../../../../../../nomagic/actions/NMAction.html#LARGE_ICON">LARGE_ICON</a>, <a href="../../../../../../nomagic/actions/NMAction.html#MENU_SHORTCUT_MASK">MENU_SHORTCUT_MASK</a>, <a href="../../../../../../nomagic/actions/NMAction.html#TINY_ICON">TINY_ICON</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String)">DefaultAbstractDiagramAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs new action.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String,boolean)">DefaultAbstractDiagramAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 boolean useSchema)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs new action.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../../../nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagram()">getDiagram</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns diagram of this action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../../../../nomagic/magicdraw/uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstSelected()">getFirstSelected</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns first selected presentation element in the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../../../nomagic/magicdraw/uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelected()">getSelected</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns list of selected presentation elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDiagram(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">setDiagram</a><wbr/>(<a href="../../../../../../nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets diagram for this action.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.actions.MDAction">Methods inherited from class com.nomagic.magicdraw.actions.<a href="../../../../../../nomagic/magicdraw/actions/MDAction.html" title="class in com.nomagic.magicdraw.actions">MDAction</a></h3>
<code><a href="../../../../../../nomagic/magicdraw/actions/MDAction.html#actionPerformed(java.awt.event.ActionEvent)">actionPerformed</a>, <a href="../../../../../../nomagic/magicdraw/actions/MDAction.html#isUseShortcutSchema()">isUseShortcutSchema</a>, <a href="../../../../../../nomagic/magicdraw/actions/MDAction.html#updateState()">updateState</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.NMAction">Methods inherited from class com.nomagic.actions.<a href="../../../../../../nomagic/actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a></h3>
<code><a href="../../../../../../nomagic/actions/NMAction.html#accept(com.nomagic.actions.ActionsVisitor)">accept</a>, <a href="../../../../../../nomagic/actions/NMAction.html#addAction(com.nomagic.actions.NMAction)">addAction</a>, <a href="../../../../../../nomagic/actions/NMAction.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../../nomagic/actions/NMAction.html#addShortcut(javax.swing.KeyStroke)">addShortcut</a>, <a href="../../../../../../nomagic/actions/NMAction.html#addShotcut(javax.swing.KeyStroke)">addShotcut</a>, <a href="../../../../../../nomagic/actions/NMAction.html#addWeakPropertyChangeListener(java.beans.PropertyChangeListener)">addWeakPropertyChangeListener</a>, <a href="../../../../../../nomagic/actions/NMAction.html#clone()">clone</a>, <a href="../../../../../../nomagic/actions/NMAction.html#compareTo(java.lang.Object)">compareTo</a>, <a href="../../../../../../nomagic/actions/NMAction.html#createMenuItem(com.nomagic.actions.MenuComponentFactory)">createMenuItem</a>, <a href="../../../../../../nomagic/actions/NMAction.html#equals(java.lang.Object)">equals</a>, <a href="../../../../../../nomagic/actions/NMAction.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../../nomagic/actions/NMAction.html#forEach(java.util.function.Consumer)">forEach</a>, <a href="../../../../../../nomagic/actions/NMAction.html#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getActions()">getActions</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getCommandKey()">getCommandKey</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getDescription()">getDescription</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getGroup()">getGroup</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getIcon()">getIcon</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getID()">getID</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getLargeIcon()">getLargeIcon</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getLargeOrSmallIcon()">getLargeOrSmallIcon</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getMenuShortcutMaskAsString()">getMenuShortcutMaskAsString</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getMnemonicKey()">getMnemonicKey</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getName()">getName</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getPropertyChangeListeners()">getPropertyChangeListeners</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getShortcuts()">getShortcuts</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getSmallIcon()">getSmallIcon</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getSmallOrLargeIcon()">getSmallOrLargeIcon</a>, <a href="../../../../../../nomagic/actions/NMAction.html#getTinyIcon()">getTinyIcon</a>, <a href="../../../../../../nomagic/actions/NMAction.html#hashCode()">hashCode</a>, <a href="../../../../../../nomagic/actions/NMAction.html#hasMenuShortcutMask(java.awt.AWTEvent)">hasMenuShortcutMask</a>, <a href="../../../../../../nomagic/actions/NMAction.html#isIDGenerated()">isIDGenerated</a>, <a href="../../../../../../nomagic/actions/NMAction.html#removeAction(com.nomagic.actions.NMAction)">removeAction</a>, <a href="../../../../../../nomagic/actions/NMAction.html#removeIf(java.util.function.Predicate)">removeIf</a>, <a href="../../../../../../nomagic/actions/NMAction.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../../nomagic/actions/NMAction.html#removeShortcut(javax.swing.KeyStroke)">removeShortcut</a>, <a href="../../../../../../nomagic/actions/NMAction.html#removeWeakPropertyChangeListener(java.beans.PropertyChangeListener)">removeWeakPropertyChangeListener</a>, <a href="../../../../../../nomagic/actions/NMAction.html#setActions(java.util.List)">setActions</a>, <a href="../../../../../../nomagic/actions/NMAction.html#setDescription(java.lang.String)">setDescription</a>, <a href="../../../../../../nomagic/actions/NMAction.html#setGroup(java.lang.String)">setGroup</a>, <a href="../../../../../../nomagic/actions/NMAction.html#setIcon(javax.swing.Icon)">setIcon</a>, <a href="../../../../../../nomagic/actions/NMAction.html#setLargeIcon(javax.swing.Icon)">setLargeIcon</a>, <a href="../../../../../../nomagic/actions/NMAction.html#setMnemonicKey(int)">setMnemonicKey</a>, <a href="../../../../../../nomagic/actions/NMAction.html#setName(java.lang.String)">setName</a>, <a href="../../../../../../nomagic/actions/NMAction.html#setShortcuts(java.util.List)">setShortcuts</a>, <a href="../../../../../../nomagic/actions/NMAction.html#setSmallIcon(javax.swing.Icon)">setSmallIcon</a>, <a href="../../../../../../nomagic/actions/NMAction.html#setTinyIcon(javax.swing.Icon)">setTinyIcon</a>, <a href="../../../../../../nomagic/actions/NMAction.html#shallowClone()">shallowClone</a>, <a href="../../../../../../nomagic/actions/NMAction.html#toString()">toString</a></code></div>
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
<h3>DefaultAbstractDiagramAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DefaultAbstractDiagramAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Constructs new action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionID</code> - the action ID</dd>
<dd><code>actionName</code> - the action name</dd>
<dd><code>stroke</code> - the action stroke</dd>
<dd><code>group</code> - the action group</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,javax.swing.KeyStroke,java.lang.String,boolean)">
<h3>DefaultAbstractDiagramAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DefaultAbstractDiagramAction</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 boolean useSchema)</span></div>
<div class="block">Constructs new action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionID</code> - the action ID</dd>
<dd><code>actionName</code> - the action name</dd>
<dd><code>stroke</code> - the action stroke</dd>
<dd><code>group</code> - the action group</dd>
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
<section class="detail" id="setDiagram(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>setDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDiagram</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../../../../nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</span></div>
<div class="block">Sets diagram for this action.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setDiagram</code> in interface <code>com.dassault_systemes.modeler.magic.ui.diagrams.actions.AbstractDiagramAction</code></dd>
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagram()">
<h3>getDiagram</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../../../../nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></span> <span class="element-name">getDiagram</span>()</div>
<div class="block">Returns diagram of this action.
 MagicDraw framework guarantee that diagram will set if this method is called from updateState() or
 actionPerformed(ActionEvent) methods.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>set diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstSelected()">
<h3>getFirstSelected</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="../../../../../../nomagic/magicdraw/uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getFirstSelected</span>()</div>
<div class="block">Returns first selected presentation element in the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>first selected presentation element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelected()">
<h3>getSelected</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../../../nomagic/magicdraw/uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getSelected</span>()</div>
<div class="block">Returns list of selected presentation elements.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of selected presentation elements. If no elements selected, empty list is returned.</dd>
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
