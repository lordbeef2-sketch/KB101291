# JAVA OPENAPI: ActionsCommandBarCreator (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/actions/ActionsCommandBarCreator.html
- source_path: `com/nomagic/actions/ActionsCommandBarCreator.html`
- source_sha256: `e5a889a3fdc427014ed4cafe31733774c2e5693af6422ae41eda21cfac7d52e5`
- captured_utc: `2026-07-14T16:57:42.224358+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.actions](package-summary.html)

## Class ActionsCommandBarCreator

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.actions.ActionsCommandBarCreator

All Implemented Interfaces:
`[ActionsVisitor](ActionsVisitor.html)`, `com.nomagic.magicdraw.ui.actions.MainActionsVisitor`

@OpenApiAllpublic abstract classActionsCommandBarCreator
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [ActionsVisitor](ActionsVisitor.html), com.nomagic.magicdraw.ui.actions.MainActionsVisitor

The abstract class for creating toolbars from actions.
 This class provides common framework for toolbar creation, but does not
 implement specific methods for buttons creation.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static interface`
`[ActionsCommandBarCreator.ButtonFactory](ActionsCommandBarCreator.ButtonFactory.html)`
Buttons factory used to create a button
`static class`
`[ActionsCommandBarCreator.FontFaceCellRenderer](ActionsCommandBarCreator.FontFaceCellRenderer.html)`
The renderer used to represent some font face name.
`static class`
`[ActionsCommandBarCreator.ListComboBox](ActionsCommandBarCreator.ListComboBox.html)`
Class for representing list action as combo box.
`static class`
`[ActionsCommandBarCreator.NMJideButtonFactory](ActionsCommandBarCreator.NMJideButtonFactory.html)`

`static class`
`[ActionsCommandBarCreator.NMJideSplitButtonFactory](ActionsCommandBarCreator.NMJideSplitButtonFactory.html)`

`static interface`
`[ActionsCommandBarCreator.SplitButtonFactory](ActionsCommandBarCreator.SplitButtonFactory.html)`
Buttons factory used to create a button
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [JComponent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JComponent.html)`
`[currentToolbar](#currentToolbar)`
The toolbar to add buttons into during the visit actions.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[ActionsCommandBarCreator](#%3Cinit%3E())()`
Creates new creator with Jide buttons factory
`protected`
`[ActionsCommandBarCreator](#%3Cinit%3E(com.nomagic.actions.ActionsCommandBarCreator.ButtonFactory))([ActionsCommandBarCreator.ButtonFactory](ActionsCommandBarCreator.ButtonFactory.html) factory)`
Creates new creator with given buttons factory
`protected`
`[ActionsCommandBarCreator](#%3Cinit%3E(com.nomagic.actions.ActionsCommandBarCreator.ButtonFactory,com.nomagic.actions.ActionsCommandBarCreator.SplitButtonFactory))([ActionsCommandBarCreator.ButtonFactory](ActionsCommandBarCreator.ButtonFactory.html) factory,
 [ActionsCommandBarCreator.SplitButtonFactory](ActionsCommandBarCreator.SplitButtonFactory.html) splitButtonFactory)`
Creates new creator with given buttons factory
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[acceptChildren](#acceptChildren(com.nomagic.actions.ActionsManager))([ActionsManager](ActionsManager.html) manager)`
For all categories in manager calls accept this visitor.
`protected void`
`[acceptChildren](#acceptChildren(com.nomagic.actions.NMAction))([NMAction](NMAction.html) parent)`
Calls accept for all actions in given action.
`protected void`
`[addFlexibleSeparator](#addFlexibleSeparator())()`
Adds a flexible separator into the current toolbar.
`protected abstract void`
`[addToCurrentToolbar](#addToCurrentToolbar(java.awt.Component))([Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) c)`

`protected void`
`[addToJideSplitButton](#addToJideSplitButton(com.nomagic.actions.ActionsCategory))([ActionsCategory](ActionsCategory.html) category)`

`protected [AbstractButton](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractButton.html)`
`[createComponent](#createComponent(com.nomagic.actions.NMAction))([NMAction](NMAction.html) action)`
Creates NMActionButton for given action.
`protected [AbstractButton](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractButton.html)`
`[createComponent](#createComponent(com.nomagic.actions.NMStateAction))([NMStateAction](NMStateAction.html) action)`
Creates MDStateActionButton from MDStateAction.
`protected [AbstractButton](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractButton.html)`
`[createComponent](#createComponent(com.nomagic.actions.NMTriStateAction))([NMTriStateAction](NMTriStateAction.html) action)`
Creates MDStateActionButton from MDTriStateAction.
`protected [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html)`
`[createComponent](#createComponent(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction))(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction action)`

`protected [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html)`
`[createComponent](#createComponent(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction))(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction category)`

`protected com.nomagic.awt.NMJideSplitButton`
`[createJideSplitButton](#createJideSplitButton(com.nomagic.actions.NMAction))([NMAction](NMAction.html) a)`

`protected void`
`[createPropertyActionComponent](#createPropertyActionComponent(com.nomagic.magicdraw.actions.PropertyAction))([PropertyAction](../magicdraw/actions/PropertyAction.html) action)`

`com.nomagic.awt.ActionIconProvider`
`[getIconProvider](#getIconProvider())()`

`void`
`[setIconProvider](#setIconProvider(com.nomagic.awt.ActionIconProvider))(com.nomagic.awt.ActionIconProvider iconProvider)`

`abstract void`
`[visit](#visit(com.nomagic.actions.ActionsCategory))([ActionsCategory](ActionsCategory.html) category)`
Visits ActionsCategory.
`void`
`[visit](#visit(com.nomagic.actions.NMAction))([NMAction](NMAction.html) action)`
Visits action.
`void`
`[visit](#visit(com.nomagic.actions.NMStateAction))([NMStateAction](NMStateAction.html) action)`
Visits NMStateAction.
`void`
`[visit](#visit(com.nomagic.actions.NMTriStateAction))([NMTriStateAction](NMTriStateAction.html) action)`
Visits NMTriStateAction
`void`
`[visit](#visit(com.nomagic.actions.SelectItemAction))([SelectItemAction](SelectItemAction.html) action)`

`void`
`[visit](#visit(com.nomagic.magicdraw.actions.PropertyAction))([PropertyAction](../magicdraw/actions/PropertyAction.html) action)`

`void`
`[visit](#visit(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction))(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction action)`

`void`
`[visit](#visit(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction))(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction category)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
currentToolbar
@CheckForNullprotected [JComponent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JComponent.html) currentToolbar
The toolbar to add buttons into during the visit actions.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ActionsCommandBarCreator
protected ActionsCommandBarCreator()
Creates new creator with Jide buttons factory
ActionsCommandBarCreator
protected ActionsCommandBarCreator([ActionsCommandBarCreator.ButtonFactory](ActionsCommandBarCreator.ButtonFactory.html) factory)
Creates new creator with given buttons factory
Parameters:
`factory` - factory
ActionsCommandBarCreator
protected ActionsCommandBarCreator([ActionsCommandBarCreator.ButtonFactory](ActionsCommandBarCreator.ButtonFactory.html) factory,
 [ActionsCommandBarCreator.SplitButtonFactory](ActionsCommandBarCreator.SplitButtonFactory.html) splitButtonFactory)
Creates new creator with given buttons factory
Parameters:
`factory` - factory
 ============ METHOD DETAIL ========== 
Method Details
acceptChildren
protected void acceptChildren([ActionsManager](ActionsManager.html) manager)
For all categories in manager calls accept this visitor.
Parameters:
`manager` - manager from which categories will be collected.
addFlexibleSeparator
protected void addFlexibleSeparator()
Adds a flexible separator into the current toolbar. It should move other buttons to the most right/bottom position
addToJideSplitButton
protected void addToJideSplitButton([ActionsCategory](ActionsCategory.html) category)
createJideSplitButton
protected com.nomagic.awt.NMJideSplitButton createJideSplitButton([NMAction](NMAction.html) a)
acceptChildren
protected void acceptChildren([NMAction](NMAction.html) parent)
Calls accept for all actions in given action.
Parameters:
`parent` - container of actions.
createComponent
protected [AbstractButton](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractButton.html) createComponent([NMAction](NMAction.html) action)
Creates NMActionButton for given action.
Parameters:
`action` - action source for button.
Returns:
created button.
createComponent
protected [AbstractButton](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractButton.html) createComponent([NMStateAction](NMStateAction.html) action)
Creates MDStateActionButton from MDStateAction.
Parameters:
`action` - source for creating button.
Returns:
created button.
createComponent
protected [AbstractButton](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractButton.html) createComponent([NMTriStateAction](NMTriStateAction.html) action)
Creates MDStateActionButton from MDTriStateAction.
Parameters:
`action` - source for creating button.
Returns:
created button.
visit
public void visit([NMAction](NMAction.html) action)
Description copied from interface: `[ActionsVisitor](ActionsVisitor.html#visit(com.nomagic.actions.NMAction))`
Visits action.
Specified by:
`[visit](ActionsVisitor.html#visit(com.nomagic.actions.NMAction))` in interface `[ActionsVisitor](ActionsVisitor.html)`
Parameters:
`action` - the action to visit.
visit
public void visit([NMStateAction](NMStateAction.html) action)
Description copied from interface: `[ActionsVisitor](ActionsVisitor.html#visit(com.nomagic.actions.NMStateAction))`
Visits NMStateAction.
Specified by:
`[visit](ActionsVisitor.html#visit(com.nomagic.actions.NMStateAction))` in interface `[ActionsVisitor](ActionsVisitor.html)`
Parameters:
`action` - the action to visit.
visit
public void visit([NMTriStateAction](NMTriStateAction.html) action)
Description copied from interface: `[ActionsVisitor](ActionsVisitor.html#visit(com.nomagic.actions.NMTriStateAction))`
Visits NMTriStateAction
Specified by:
`[visit](ActionsVisitor.html#visit(com.nomagic.actions.NMTriStateAction))` in interface `[ActionsVisitor](ActionsVisitor.html)`
Parameters:
`action` - the action to visit
visit
public abstract void visit([ActionsCategory](ActionsCategory.html) category)
Description copied from interface: `[ActionsVisitor](ActionsVisitor.html#visit(com.nomagic.actions.ActionsCategory))`
Visits ActionsCategory.
Specified by:
`[visit](ActionsVisitor.html#visit(com.nomagic.actions.ActionsCategory))` in interface `[ActionsVisitor](ActionsVisitor.html)`
Parameters:
`category` - the category to visit.
visit
public void visit([SelectItemAction](SelectItemAction.html) action)
Specified by:
`visit` in interface `com.nomagic.magicdraw.ui.actions.MainActionsVisitor`
visit
public void visit(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction action)
Specified by:
`visit` in interface `com.nomagic.magicdraw.ui.actions.MainActionsVisitor`
createComponent
protected [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) createComponent(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction action)
visit
public void visit(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction category)
Specified by:
`visit` in interface `com.nomagic.magicdraw.ui.actions.MainActionsVisitor`
createComponent
protected [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) createComponent(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction category)
visit
public void visit([PropertyAction](../magicdraw/actions/PropertyAction.html) action)
Specified by:
`visit` in interface `com.nomagic.magicdraw.ui.actions.MainActionsVisitor`
createPropertyActionComponent
protected void createPropertyActionComponent([PropertyAction](../magicdraw/actions/PropertyAction.html) action)
getIconProvider
public com.nomagic.awt.ActionIconProvider getIconProvider()
setIconProvider
public void setIconProvider(com.nomagic.awt.ActionIconProvider iconProvider)
addToCurrentToolbar
protected abstract void addToCurrentToolbar([Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) c)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.actions</a></div>
<h1 class="title" title="Class ActionsCommandBarCreator">Class ActionsCommandBarCreator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.actions.ActionsCommandBarCreator</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a></code>, <code>com.nomagic.magicdraw.ui.actions.MainActionsVisitor</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">ActionsCommandBarCreator</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a>, com.nomagic.magicdraw.ui.actions.MainActionsVisitor</span></div>
<div class="block">The abstract class for creating toolbars from actions.
 This class provides common framework for toolbar creation, but does not
 implement specific methods for buttons creation.</div>
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
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ActionsCommandBarCreator.ButtonFactory.html" title="interface in com.nomagic.actions">ActionsCommandBarCreator.ButtonFactory</a></code></div>
<div class="col-last even-row-color">
<div class="block">Buttons factory used to create a button</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ActionsCommandBarCreator.FontFaceCellRenderer.html" title="class in com.nomagic.actions">ActionsCommandBarCreator.FontFaceCellRenderer</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The renderer used to represent some font face name.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ActionsCommandBarCreator.ListComboBox.html" title="class in com.nomagic.actions">ActionsCommandBarCreator.ListComboBox</a></code></div>
<div class="col-last even-row-color">
<div class="block">Class for representing list action as combo box.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ActionsCommandBarCreator.NMJideButtonFactory.html" title="class in com.nomagic.actions">ActionsCommandBarCreator.NMJideButtonFactory</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ActionsCommandBarCreator.NMJideSplitButtonFactory.html" title="class in com.nomagic.actions">ActionsCommandBarCreator.NMJideSplitButtonFactory</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static interface </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ActionsCommandBarCreator.SplitButtonFactory.html" title="interface in com.nomagic.actions">ActionsCommandBarCreator.SplitButtonFactory</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Buttons factory used to create a button</div>
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
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JComponent.html" title="class or interface in javax.swing">JComponent</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#currentToolbar">currentToolbar</a></code></div>
<div class="col-last even-row-color">
<div class="block">The toolbar to add buttons into during the visit actions.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ActionsCommandBarCreator</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates new creator with Jide buttons factory</div>
</div>
<div class="col-first odd-row-color"><code>protected </code></div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.actions.ActionsCommandBarCreator.ButtonFactory)">ActionsCommandBarCreator</a><wbr/>(<a href="ActionsCommandBarCreator.ButtonFactory.html" title="interface in com.nomagic.actions">ActionsCommandBarCreator.ButtonFactory</a> factory)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates new creator with given buttons factory</div>
</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.actions.ActionsCommandBarCreator.ButtonFactory,com.nomagic.actions.ActionsCommandBarCreator.SplitButtonFactory)">ActionsCommandBarCreator</a><wbr/>(<a href="ActionsCommandBarCreator.ButtonFactory.html" title="interface in com.nomagic.actions">ActionsCommandBarCreator.ButtonFactory</a> factory,
 <a href="ActionsCommandBarCreator.SplitButtonFactory.html" title="interface in com.nomagic.actions">ActionsCommandBarCreator.SplitButtonFactory</a> splitButtonFactory)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates new creator with given buttons factory</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#acceptChildren(com.nomagic.actions.ActionsManager)">acceptChildren</a><wbr/>(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">For all categories in manager calls accept this visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#acceptChildren(com.nomagic.actions.NMAction)">acceptChildren</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> parent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calls accept for all actions in given action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addFlexibleSeparator()">addFlexibleSeparator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a flexible separator into the current toolbar.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addToCurrentToolbar(java.awt.Component)">addToCurrentToolbar</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> c)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addToJideSplitButton(com.nomagic.actions.ActionsCategory)">addToJideSplitButton</a><wbr/>(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createComponent(com.nomagic.actions.NMAction)">createComponent</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates NMActionButton for given action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createComponent(com.nomagic.actions.NMStateAction)">createComponent</a><wbr/>(<a href="NMStateAction.html" title="class in com.nomagic.actions">NMStateAction</a> action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates MDStateActionButton from MDStateAction.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createComponent(com.nomagic.actions.NMTriStateAction)">createComponent</a><wbr/>(<a href="NMTriStateAction.html" title="class in com.nomagic.actions">NMTriStateAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates MDStateActionButton from MDTriStateAction.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createComponent(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction)">createComponent</a><wbr/>(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createComponent(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction)">createComponent</a><wbr/>(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction category)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.awt.NMJideSplitButton</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createJideSplitButton(com.nomagic.actions.NMAction)">createJideSplitButton</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> a)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPropertyActionComponent(com.nomagic.magicdraw.actions.PropertyAction)">createPropertyActionComponent</a><wbr/>(<a href="../magicdraw/actions/PropertyAction.html" title="class in com.nomagic.magicdraw.actions">PropertyAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.awt.ActionIconProvider</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconProvider()">getIconProvider</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIconProvider(com.nomagic.awt.ActionIconProvider)">setIconProvider</a><wbr/>(com.nomagic.awt.ActionIconProvider iconProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.actions.ActionsCategory)">visit</a><wbr/>(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visits ActionsCategory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.actions.NMAction)">visit</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visits action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.actions.NMStateAction)">visit</a><wbr/>(<a href="NMStateAction.html" title="class in com.nomagic.actions">NMStateAction</a> action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visits NMStateAction.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.actions.NMTriStateAction)">visit</a><wbr/>(<a href="NMTriStateAction.html" title="class in com.nomagic.actions">NMTriStateAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visits NMTriStateAction</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.actions.SelectItemAction)">visit</a><wbr/>(<a href="SelectItemAction.html" title="class in com.nomagic.actions">SelectItemAction</a> action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.actions.PropertyAction)">visit</a><wbr/>(<a href="../magicdraw/actions/PropertyAction.html" title="class in com.nomagic.magicdraw.actions">PropertyAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction)">visit</a><wbr/>(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction)">visit</a><wbr/>(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction category)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="currentToolbar">
<h3>currentToolbar</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JComponent.html" title="class or interface in javax.swing">JComponent</a></span> <span class="element-name">currentToolbar</span></div>
<div class="block">The toolbar to add buttons into during the visit actions.</div>
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
<h3>ActionsCommandBarCreator</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">ActionsCommandBarCreator</span>()</div>
<div class="block">Creates new creator with Jide buttons factory</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.actions.ActionsCommandBarCreator.ButtonFactory)">
<h3>ActionsCommandBarCreator</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">ActionsCommandBarCreator</span><wbr/><span class="parameters">(<a href="ActionsCommandBarCreator.ButtonFactory.html" title="interface in com.nomagic.actions">ActionsCommandBarCreator.ButtonFactory</a> factory)</span></div>
<div class="block">Creates new creator with given buttons factory</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factory</code> - factory</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.actions.ActionsCommandBarCreator.ButtonFactory,com.nomagic.actions.ActionsCommandBarCreator.SplitButtonFactory)">
<h3>ActionsCommandBarCreator</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">ActionsCommandBarCreator</span><wbr/><span class="parameters">(<a href="ActionsCommandBarCreator.ButtonFactory.html" title="interface in com.nomagic.actions">ActionsCommandBarCreator.ButtonFactory</a> factory,
 <a href="ActionsCommandBarCreator.SplitButtonFactory.html" title="interface in com.nomagic.actions">ActionsCommandBarCreator.SplitButtonFactory</a> splitButtonFactory)</span></div>
<div class="block">Creates new creator with given buttons factory</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factory</code> - factory</dd>
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
<section class="detail" id="acceptChildren(com.nomagic.actions.ActionsManager)">
<h3>acceptChildren</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">acceptChildren</span><wbr/><span class="parameters">(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</span></div>
<div class="block">For all categories in manager calls accept this visitor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - manager from which categories will be collected.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addFlexibleSeparator()">
<h3>addFlexibleSeparator</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addFlexibleSeparator</span>()</div>
<div class="block">Adds a flexible separator into the current toolbar. It should move other buttons to the most right/bottom position</div>
</section>
</li>
<li>
<section class="detail" id="addToJideSplitButton(com.nomagic.actions.ActionsCategory)">
<h3>addToJideSplitButton</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addToJideSplitButton</span><wbr/><span class="parameters">(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</span></div>
</section>
</li>
<li>
<section class="detail" id="createJideSplitButton(com.nomagic.actions.NMAction)">
<h3>createJideSplitButton</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.awt.NMJideSplitButton</span> <span class="element-name">createJideSplitButton</span><wbr/><span class="parameters">(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> a)</span></div>
</section>
</li>
<li>
<section class="detail" id="acceptChildren(com.nomagic.actions.NMAction)">
<h3>acceptChildren</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">acceptChildren</span><wbr/><span class="parameters">(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> parent)</span></div>
<div class="block">Calls accept for all actions in given action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - container of actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComponent(com.nomagic.actions.NMAction)">
<h3>createComponent</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></span> <span class="element-name">createComponent</span><wbr/><span class="parameters">(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Creates NMActionButton for given action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - action source for button.</dd>
<dt>Returns:</dt>
<dd>created button.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComponent(com.nomagic.actions.NMStateAction)">
<h3>createComponent</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></span> <span class="element-name">createComponent</span><wbr/><span class="parameters">(<a href="NMStateAction.html" title="class in com.nomagic.actions">NMStateAction</a> action)</span></div>
<div class="block">Creates MDStateActionButton from MDStateAction.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - source for creating button.</dd>
<dt>Returns:</dt>
<dd>created button.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComponent(com.nomagic.actions.NMTriStateAction)">
<h3>createComponent</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></span> <span class="element-name">createComponent</span><wbr/><span class="parameters">(<a href="NMTriStateAction.html" title="class in com.nomagic.actions">NMTriStateAction</a> action)</span></div>
<div class="block">Creates MDStateActionButton from MDTriStateAction.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - source for creating button.</dd>
<dt>Returns:</dt>
<dd>created button.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.actions.NMAction)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ActionsVisitor.html#visit(com.nomagic.actions.NMAction)">ActionsVisitor</a></code></span></div>
<div class="block">Visits action.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ActionsVisitor.html#visit(com.nomagic.actions.NMAction)">visit</a></code> in interface <code><a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a></code></dd>
<dt>Parameters:</dt>
<dd><code>action</code> - the action to visit.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.actions.NMStateAction)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="NMStateAction.html" title="class in com.nomagic.actions">NMStateAction</a> action)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ActionsVisitor.html#visit(com.nomagic.actions.NMStateAction)">ActionsVisitor</a></code></span></div>
<div class="block">Visits NMStateAction.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ActionsVisitor.html#visit(com.nomagic.actions.NMStateAction)">visit</a></code> in interface <code><a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a></code></dd>
<dt>Parameters:</dt>
<dd><code>action</code> - the action to visit.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.actions.NMTriStateAction)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="NMTriStateAction.html" title="class in com.nomagic.actions">NMTriStateAction</a> action)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ActionsVisitor.html#visit(com.nomagic.actions.NMTriStateAction)">ActionsVisitor</a></code></span></div>
<div class="block">Visits NMTriStateAction</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ActionsVisitor.html#visit(com.nomagic.actions.NMTriStateAction)">visit</a></code> in interface <code><a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a></code></dd>
<dt>Parameters:</dt>
<dd><code>action</code> - the action to visit</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.actions.ActionsCategory)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ActionsVisitor.html#visit(com.nomagic.actions.ActionsCategory)">ActionsVisitor</a></code></span></div>
<div class="block">Visits ActionsCategory.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ActionsVisitor.html#visit(com.nomagic.actions.ActionsCategory)">visit</a></code> in interface <code><a href="ActionsVisitor.html" title="interface in com.nomagic.actions">ActionsVisitor</a></code></dd>
<dt>Parameters:</dt>
<dd><code>category</code> - the category to visit.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.actions.SelectItemAction)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="SelectItemAction.html" title="class in com.nomagic.actions">SelectItemAction</a> action)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>visit</code> in interface <code>com.nomagic.magicdraw.ui.actions.MainActionsVisitor</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction action)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>visit</code> in interface <code>com.nomagic.magicdraw.ui.actions.MainActionsVisitor</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComponent(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction)">
<h3>createComponent</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></span> <span class="element-name">createComponent</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.actions.ChangeFontAction action)</span></div>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction category)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>visit</code> in interface <code>com.nomagic.magicdraw.ui.actions.MainActionsVisitor</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComponent(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction)">
<h3>createComponent</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></span> <span class="element-name">createComponent</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.actions.ChangeZoomAction category)</span></div>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.actions.PropertyAction)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="../magicdraw/actions/PropertyAction.html" title="class in com.nomagic.magicdraw.actions">PropertyAction</a> action)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>visit</code> in interface <code>com.nomagic.magicdraw.ui.actions.MainActionsVisitor</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPropertyActionComponent(com.nomagic.magicdraw.actions.PropertyAction)">
<h3>createPropertyActionComponent</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createPropertyActionComponent</span><wbr/><span class="parameters">(<a href="../magicdraw/actions/PropertyAction.html" title="class in com.nomagic.magicdraw.actions">PropertyAction</a> action)</span></div>
</section>
</li>
<li>
<section class="detail" id="getIconProvider()">
<h3>getIconProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.awt.ActionIconProvider</span> <span class="element-name">getIconProvider</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setIconProvider(com.nomagic.awt.ActionIconProvider)">
<h3>setIconProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIconProvider</span><wbr/><span class="parameters">(com.nomagic.awt.ActionIconProvider iconProvider)</span></div>
</section>
</li>
<li>
<section class="detail" id="addToCurrentToolbar(java.awt.Component)">
<h3>addToCurrentToolbar</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">void</span> <span class="element-name">addToCurrentToolbar</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> c)</span></div>
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
