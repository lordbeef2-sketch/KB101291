# JAVA OPENAPI: ActionsMenuCreator (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/actions/ActionsMenuCreator.html
- source_path: `com/nomagic/actions/ActionsMenuCreator.html`
- source_sha256: `b6f825fc1b17c0e5abad970e6bd57b027236903e5c776b0490469c968aa8691b`
- captured_utc: `2026-07-14T16:55:00.752846+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.actions](package-summary.html)

## Class ActionsMenuCreator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.actions.ActionsMenuCreator

@OpenApiAllpublic classActionsMenuCreator
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Class for creating GUI menu items from actions.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`protected class`
`[ActionsMenuCreator.AMC_ActionsVisitor](ActionsMenuCreator.AMC_ActionsVisitor.html)`

`static class`
`[ActionsMenuCreator.CustomJMenuItem](ActionsMenuCreator.CustomJMenuItem.html)`

`class`
`[ActionsMenuCreator.MutableActionListener](ActionsMenuCreator.MutableActionListener.html)`
Class for handling ActionsCategory changes.
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ACTION](#ACTION)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CATEGORY_HEADER](#CATEGORY_HEADER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[HIDDEN_ALWAYS](#HIDDEN_ALWAYS)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[POPUP_HEADER_ITEM_NAME](#POPUP_HEADER_ITEM_NAME)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ActionsMenuCreator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[addCleanupParticipant](#addCleanupParticipant(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) participant)`

`protected void`
`[addJMenuItem](#addJMenuItem(java.awt.Component,com.nomagic.actions.NMAction))([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) item,
 [NMAction](NMAction.html) action)`
Adds menu item, according to index item will be added to end when index less than 0, or to
 specified by index position.
`final void`
`[appendMenuItems](#appendMenuItems(java.awt.Container,com.nomagic.actions.ActionsManager))([Container](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html) container,
 [ActionsManager](ActionsManager.html) manager)`
Appends menu items to given container.
`final void`
`[appendMenuItems](#appendMenuItems(javax.swing.JPopupMenu,com.nomagic.actions.ActionsManager))([JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html) popup,
 [ActionsManager](ActionsManager.html) manager)`
Appends menu items to the given pop up menu.
`final void`
`[appendMenuItems](#appendMenuItems(javax.swing.JPopupMenu,com.nomagic.actions.ActionsManager,boolean))([JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html) popup,
 [ActionsManager](ActionsManager.html) manager,
 boolean addSeparator)`
Appends menu items to given popup.
`protected [ActionsVisitor](ActionsVisitor.html)`
`[createActionsVisitor](#createActionsVisitor())()`

`final [JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html)`
`[createPopupMenu](#createPopupMenu(com.nomagic.actions.ActionsManager))([ActionsManager](ActionsManager.html) manager)`
Creates popup menu for given actions manager
`final [JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html)`
`[createPopupMenu](#createPopupMenu(com.nomagic.actions.ActionsManager,java.util.function.Supplier))([ActionsManager](ActionsManager.html) manager,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html)> factory)`
Creates popup menu for given actions manager
`com.nomagic.actions.MenuComponentFactory`
`[getFactory](#getFactory())()`
Return menu component factory
`protected void`
`[internalAppendMenuItems](#internalAppendMenuItems(java.awt.Container,com.nomagic.actions.ActionsManager))([Container](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html) container,
 [ActionsManager](ActionsManager.html) manager)`

`protected void`
`[internalAppendMenuItems](#internalAppendMenuItems(javax.swing.JPopupMenu,com.nomagic.actions.ActionsManager,boolean))([JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html) popup,
 [ActionsManager](ActionsManager.html) manager,
 boolean addSeparator)`

`static boolean`
`[isSeparatorComponent](#isSeparatorComponent(java.awt.Component))([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component)`

`void`
`[setFactory](#setFactory(com.nomagic.actions.MenuComponentFactory))(com.nomagic.actions.MenuComponentFactory factory)`
Set menu component factory
`static void`
`[setPropertiesToMenuItem](#setPropertiesToMenuItem(javax.swing.JMenuItem,com.nomagic.actions.NMAction))([JMenuItem](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html) item,
 [NMAction](NMAction.html) action)`
Sets properties to given JMenuItem from given action.
`void`
`[setUseMenuListener](#setUseMenuListener(boolean))(boolean useMenuListener)`
Do we need to use [`MenuListener`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/event/MenuListener.html) on category? This flag should be set to true only if
 software is running on mac and using -Dapple.laf.useScreenMenuBar=true system property.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
HIDDEN_ALWAYS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) HIDDEN_ALWAYS
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.ActionsMenuCreator.HIDDEN_ALWAYS)
ACTION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ACTION
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.ActionsMenuCreator.ACTION)
CATEGORY_HEADER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CATEGORY_HEADER
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.ActionsMenuCreator.CATEGORY_HEADER)
POPUP_HEADER_ITEM_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) POPUP_HEADER_ITEM_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.ActionsMenuCreator.POPUP_HEADER_ITEM_NAME)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ActionsMenuCreator
public ActionsMenuCreator()
 ============ METHOD DETAIL ========== 
Method Details
createPopupMenu
public final [JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html) createPopupMenu([ActionsManager](ActionsManager.html) manager)
Creates popup menu for given actions manager
Parameters:
`manager` - manager
Returns:
popup menu
createPopupMenu
public final [JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html) createPopupMenu([ActionsManager](ActionsManager.html) manager,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html)> factory)
Creates popup menu for given actions manager
Parameters:
`manager` - manager
`factory` - new popup menu factory
Returns:
popup menu
appendMenuItems
public final void appendMenuItems([JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html) popup,
 [ActionsManager](ActionsManager.html) manager)
Appends menu items to the given pop up menu. Adds separator before new items if given pop up is not empty.
Parameters:
`popup` - where items will be appended
`manager` - manager from which actions menu items will be created
appendMenuItems
public final void appendMenuItems([JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html) popup,
 [ActionsManager](ActionsManager.html) manager,
 boolean addSeparator)
Appends menu items to given popup.
Parameters:
`popup` - where items will be appended
`manager` - manager from which actions menu items will be created
`addSeparator` - add separator after last item in the given popup or not
internalAppendMenuItems
protected void internalAppendMenuItems([JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html) popup,
 [ActionsManager](ActionsManager.html) manager,
 boolean addSeparator)
appendMenuItems
public final void appendMenuItems([Container](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html) container,
 [ActionsManager](ActionsManager.html) manager)
Appends menu items to given container.
Parameters:
`container` - container where items will be appended
`manager` - manager from which actions items will be created
createActionsVisitor
protected [ActionsVisitor](ActionsVisitor.html) createActionsVisitor()
internalAppendMenuItems
protected void internalAppendMenuItems([Container](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html) container,
 [ActionsManager](ActionsManager.html) manager)
addJMenuItem
protected void addJMenuItem([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) item,
 [NMAction](NMAction.html) action)
Adds menu item, according to index item will be added to end when index less than 0, or to
 specified by index position.
Parameters:
`item` - item to add.
`action` - action
setPropertiesToMenuItem
public static void setPropertiesToMenuItem([JMenuItem](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html) item,
 [NMAction](NMAction.html) action)
Sets properties to given JMenuItem from given action.
Parameters:
`item` - item to set properties.
`action` - for getting properties.
setUseMenuListener
public void setUseMenuListener(boolean useMenuListener)
Do we need to use [`MenuListener`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/event/MenuListener.html) on category? This flag should be set to true only if
 software is running on mac and using -Dapple.laf.useScreenMenuBar=true system property.
Parameters:
`useMenuListener` - true if need to use.
getFactory
public com.nomagic.actions.MenuComponentFactory getFactory()
Return menu component factory
Returns:
factory
setFactory
public void setFactory(com.nomagic.actions.MenuComponentFactory factory)
Set menu component factory
Parameters:
`factory` - factory
isSeparatorComponent
public static boolean isSeparatorComponent(@CheckForNull
 [Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component)
addCleanupParticipant
protected void addCleanupParticipant([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) participant)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.actions</a></div>
<h1 class="title" title="Class ActionsMenuCreator">Class ActionsMenuCreator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.actions.ActionsMenuCreator</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ActionsMenuCreator</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Class for creating GUI menu items from actions.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ActionsMenuCreator.AMC_ActionsVisitor.html" title="class in com.nomagic.actions">ActionsMenuCreator.AMC_ActionsVisitor</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ActionsMenuCreator.CustomJMenuItem.html" title="class in com.nomagic.actions">ActionsMenuCreator.CustomJMenuItem</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ActionsMenuCreator.MutableActionListener.html" title="class in com.nomagic.actions">ActionsMenuCreator.MutableActionListener</a></code></div>
<div class="col-last even-row-color">
<div class="block">Class for handling ActionsCategory changes.</div>
</div>
</div>
</section>
</li>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTION">ACTION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CATEGORY_HEADER">CATEGORY_HEADER</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#HIDDEN_ALWAYS">HIDDEN_ALWAYS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#POPUP_HEADER_ITEM_NAME">POPUP_HEADER_ITEM_NAME</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ActionsMenuCreator</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCleanupParticipant(java.lang.Runnable)">addCleanupParticipant</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> participant)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addJMenuItem(java.awt.Component,com.nomagic.actions.NMAction)">addJMenuItem</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> item,
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds menu item, according to index item will be added to end when index less than 0, or to
 specified by index position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#appendMenuItems(java.awt.Container,com.nomagic.actions.ActionsManager)">appendMenuItems</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html" title="class or interface in java.awt">Container</a> container,
 <a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Appends menu items to given container.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#appendMenuItems(javax.swing.JPopupMenu,com.nomagic.actions.ActionsManager)">appendMenuItems</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a> popup,
 <a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Appends menu items to the given pop up menu.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#appendMenuItems(javax.swing.JPopupMenu,com.nomagic.actions.ActionsManager,boolean)">appendMenuItems</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a> popup,
 <a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 boolean addSeparator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Appends menu items to given popup.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActionsVisitor()">createActionsVisitor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPopupMenu(com.nomagic.actions.ActionsManager)">createPopupMenu</a><wbr/>(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates popup menu for given actions manager</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPopupMenu(com.nomagic.actions.ActionsManager,java.util.function.Supplier)">createPopupMenu</a><wbr/>(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a>&gt; factory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates popup menu for given actions manager</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.actions.MenuComponentFactory</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFactory()">getFactory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return menu component factory</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalAppendMenuItems(java.awt.Container,com.nomagic.actions.ActionsManager)">internalAppendMenuItems</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html" title="class or interface in java.awt">Container</a> container,
 <a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalAppendMenuItems(javax.swing.JPopupMenu,com.nomagic.actions.ActionsManager,boolean)">internalAppendMenuItems</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a> popup,
 <a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 boolean addSeparator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSeparatorComponent(java.awt.Component)">isSeparatorComponent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFactory(com.nomagic.actions.MenuComponentFactory)">setFactory</a><wbr/>(com.nomagic.actions.MenuComponentFactory factory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set menu component factory</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setPropertiesToMenuItem(javax.swing.JMenuItem,com.nomagic.actions.NMAction)">setPropertiesToMenuItem</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html" title="class or interface in javax.swing">JMenuItem</a> item,
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets properties to given JMenuItem from given action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseMenuListener(boolean)">setUseMenuListener</a><wbr/>(boolean useMenuListener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Do we need to use <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/event/MenuListener.html" title="class or interface in javax.swing.event"><code>MenuListener</code></a> on category? This flag should be set to true only if
 software is running on mac and using -Dapple.laf.useScreenMenuBar=true system property.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="HIDDEN_ALWAYS">
<h3>HIDDEN_ALWAYS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HIDDEN_ALWAYS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.ActionsMenuCreator.HIDDEN_ALWAYS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTION">
<h3>ACTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACTION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.ActionsMenuCreator.ACTION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CATEGORY_HEADER">
<h3>CATEGORY_HEADER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CATEGORY_HEADER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.ActionsMenuCreator.CATEGORY_HEADER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="POPUP_HEADER_ITEM_NAME">
<h3>POPUP_HEADER_ITEM_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">POPUP_HEADER_ITEM_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.ActionsMenuCreator.POPUP_HEADER_ITEM_NAME">Constant Field Values</a></li>
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
<h3>ActionsMenuCreator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ActionsMenuCreator</span>()</div>
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
<section class="detail" id="createPopupMenu(com.nomagic.actions.ActionsManager)">
<h3>createPopupMenu</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a></span> <span class="element-name">createPopupMenu</span><wbr/><span class="parameters">(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</span></div>
<div class="block">Creates popup menu for given actions manager</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - manager</dd>
<dt>Returns:</dt>
<dd>popup menu</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPopupMenu(com.nomagic.actions.ActionsManager,java.util.function.Supplier)">
<h3>createPopupMenu</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a></span> <span class="element-name">createPopupMenu</span><wbr/><span class="parameters">(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a>&gt; factory)</span></div>
<div class="block">Creates popup menu for given actions manager</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - manager</dd>
<dd><code>factory</code> - new popup menu factory</dd>
<dt>Returns:</dt>
<dd>popup menu</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendMenuItems(javax.swing.JPopupMenu,com.nomagic.actions.ActionsManager)">
<h3>appendMenuItems</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">appendMenuItems</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a> popup,
 <a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</span></div>
<div class="block">Appends menu items to the given pop up menu. Adds separator before new items if given pop up is not empty.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>popup</code> - where items will be appended</dd>
<dd><code>manager</code> - manager from which actions menu items will be created</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendMenuItems(javax.swing.JPopupMenu,com.nomagic.actions.ActionsManager,boolean)">
<h3>appendMenuItems</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">appendMenuItems</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a> popup,
 <a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 boolean addSeparator)</span></div>
<div class="block">Appends menu items to given popup.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>popup</code> - where items will be appended</dd>
<dd><code>manager</code> - manager from which actions menu items will be created</dd>
<dd><code>addSeparator</code> - add separator after last item in the given popup or not</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalAppendMenuItems(javax.swing.JPopupMenu,com.nomagic.actions.ActionsManager,boolean)">
<h3>internalAppendMenuItems</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalAppendMenuItems</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a> popup,
 <a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 boolean addSeparator)</span></div>
</section>
</li>
<li>
<section class="detail" id="appendMenuItems(java.awt.Container,com.nomagic.actions.ActionsManager)">
<h3>appendMenuItems</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">appendMenuItems</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html" title="class or interface in java.awt">Container</a> container,
 <a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</span></div>
<div class="block">Appends menu items to given container.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>container</code> - container where items will be appended</dd>
<dd><code>manager</code> - manager from which actions items will be created</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActionsVisitor()">
<h3>createActionsVisitor</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a></span> <span class="element-name">createActionsVisitor</span>()</div>
</section>
</li>
<li>
<section class="detail" id="internalAppendMenuItems(java.awt.Container,com.nomagic.actions.ActionsManager)">
<h3>internalAppendMenuItems</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalAppendMenuItems</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html" title="class or interface in java.awt">Container</a> container,
 <a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</span></div>
</section>
</li>
<li>
<section class="detail" id="addJMenuItem(java.awt.Component,com.nomagic.actions.NMAction)">
<h3>addJMenuItem</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addJMenuItem</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> item,
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Adds menu item, according to index item will be added to end when index less than 0, or to
 specified by index position.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>item</code> - item to add.</dd>
<dd><code>action</code> - action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPropertiesToMenuItem(javax.swing.JMenuItem,com.nomagic.actions.NMAction)">
<h3>setPropertiesToMenuItem</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setPropertiesToMenuItem</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html" title="class or interface in javax.swing">JMenuItem</a> item,
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Sets properties to given JMenuItem from given action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>item</code> - item to set properties.</dd>
<dd><code>action</code> - for getting properties.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseMenuListener(boolean)">
<h3>setUseMenuListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseMenuListener</span><wbr/><span class="parameters">(boolean useMenuListener)</span></div>
<div class="block">Do we need to use <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/event/MenuListener.html" title="class or interface in javax.swing.event"><code>MenuListener</code></a> on category? This flag should be set to true only if
 software is running on mac and using -Dapple.laf.useScreenMenuBar=true system property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useMenuListener</code> - true if need to use.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFactory()">
<h3>getFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.actions.MenuComponentFactory</span> <span class="element-name">getFactory</span>()</div>
<div class="block">Return menu component factory</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>factory</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFactory(com.nomagic.actions.MenuComponentFactory)">
<h3>setFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFactory</span><wbr/><span class="parameters">(com.nomagic.actions.MenuComponentFactory factory)</span></div>
<div class="block">Set menu component factory</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factory</code> - factory</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSeparatorComponent(java.awt.Component)">
<h3>isSeparatorComponent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSeparatorComponent</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component)</span></div>
</section>
</li>
<li>
<section class="detail" id="addCleanupParticipant(java.lang.Runnable)">
<h3>addCleanupParticipant</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addCleanupParticipant</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> participant)</span></div>
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
