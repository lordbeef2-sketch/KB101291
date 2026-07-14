# JAVA OPENAPI: WindowComponentInfo (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/WindowComponentInfo.html
- source_path: `com/nomagic/magicdraw/ui/WindowComponentInfo.html`
- source_sha256: `e717c7bb4b8ae07b9d0acfcd1f78d786abe823c120f912ada5885b11dd5e57e1`
- captured_utc: `2026-07-14T16:55:50.947407+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Class WindowComponentInfo

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.WindowComponentInfo

@OpenApiAllpublic classWindowComponentInfo
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Stores information about window component - id, name, icon and etc.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[WindowComponentInfo](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,javax.swing.Icon,int,int,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tabTitle,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 int side,
 int state,
 boolean removeOnHide)`
Constructor.
`[WindowComponentInfo](#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.Icon,int,int,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 int side,
 int state,
 boolean removeOnHide)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getIcon](#getIcon())()`
Returns icon of the window component.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getId](#getId())()`
Returns id of the window component.
`int`
`[getIndex](#getIndex())()`
Returns the window component index in the JIDE interface style.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getInitialFloatingBounds](#getInitialFloatingBounds())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Returns name (title) of the window component.
`int`
`[getSide](#getSide())()`
Returns the window component side in the JIDE interface style.
`int`
`[getState](#getState())()`
Returns the window component initial docking state in the JIDE interface style.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTabTitle](#getTabTitle())()`
Returns window's tab's title.
`boolean`
`[isAutohidable](#isAutohidable())()`

`boolean`
`[isDockable](#isDockable())()`

`boolean`
`[isFloatable](#isFloatable())()`

`boolean`
`[isMaximizable](#isMaximizable())()`

`boolean`
`[isRearrangable](#isRearrangable())()`

`boolean`
`[isRemoveOnHide](#isRemoveOnHide())()`
Returns if the window component should be removed on hide.
`boolean`
`[isShowTitleBar](#isShowTitleBar())()`

`void`
`[setAutohidable](#setAutohidable(boolean))(boolean autohidable)`

`void`
`[setDockable](#setDockable(boolean))(boolean dockable)`
Set dockable initial state of the window
`void`
`[setFloatable](#setFloatable(boolean))(boolean floatable)`

`void`
`[setIcon](#setIcon(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Set icon for the window.
`void`
`[setId](#setId(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Set id for the window component.
`void`
`[setIndex](#setIndex(int))(int index)`
Set the window component initial docking index in JIDE interface style.
`void`
`[setInitialFloatingBounds](#setInitialFloatingBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) initialFloatingBounds)`
Sets initial bounds for floating window.
`void`
`[setMaximizable](#setMaximizable(boolean))(boolean maximizable)`

`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Set name (title) for the window component.
`void`
`[setRearrangable](#setRearrangable(boolean))(boolean rearrangable)`

`void`
`[setRemoveOnHide](#setRemoveOnHide(boolean))(boolean removeOnHide)`
Set if remove the window component on
`void`
`[setShowTitleBar](#setShowTitleBar(boolean))(boolean showTitleBar)`

`void`
`[setSide](#setSide(int))(int side)`
Set the window component side in JIDE interface style.
`void`
`[setState](#setState(int))(int state)`
Set the window component initial docking state in JIDE interface style.
`void`
`[setTabTitle](#setTabTitle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tabTitle)`
Sets title of window's tab.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
WindowComponentInfo
public WindowComponentInfo([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 int side,
 int state,
 boolean removeOnHide)
Constructor.
Parameters:
`id` - id of the window component.
`name` - name (title) of the window.
`icon` - icon of the window.
`side` - indicates the side to place the window component in the JIDE interface style.
`state` - indicates the docking state of the window component in the JIDE interface style.
`removeOnHide` - true if the window should be removed on hide, false if it should be just hide.
See Also:
[`WindowsManager.SIDE_EAST`](WindowsManager.html#SIDE_EAST)
[`WindowsManager.SIDE_NORTH`](WindowsManager.html#SIDE_NORTH)
[`WindowsManager.SIDE_SOUTH`](WindowsManager.html#SIDE_SOUTH)
[`WindowsManager.SIDE_WEST`](WindowsManager.html#SIDE_WEST)
[`WindowsManager.STATE_DOCKED`](WindowsManager.html#STATE_DOCKED)
[`WindowsManager.STATE_FLOATING`](WindowsManager.html#STATE_FLOATING)
[`WindowsManager.STATE_AUTOHIDE`](WindowsManager.html#STATE_AUTOHIDE)
[`WindowsManager.STATE_HIDDEN`](WindowsManager.html#STATE_HIDDEN)
WindowComponentInfo
public WindowComponentInfo([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tabTitle,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 int side,
 int state,
 boolean removeOnHide)
Constructor.
Parameters:
`id` - id of the window component.
`tabTitle` - the title of window's tab.
`name` - name (title) of the window.
`icon` - icon of the window.
`side` - indicates the side to place the window component in the JIDE interface style.
`state` - indicates the docking state of the window component in the JIDE interface style.
`removeOnHide` - true if the window should be removed on hide, false if it should be just hide.
See Also:
[`WindowsManager.SIDE_EAST`](WindowsManager.html#SIDE_EAST)
[`WindowsManager.SIDE_NORTH`](WindowsManager.html#SIDE_NORTH)
[`WindowsManager.SIDE_SOUTH`](WindowsManager.html#SIDE_SOUTH)
[`WindowsManager.SIDE_WEST`](WindowsManager.html#SIDE_WEST)
[`WindowsManager.STATE_DOCKED`](WindowsManager.html#STATE_DOCKED)
[`WindowsManager.STATE_FLOATING`](WindowsManager.html#STATE_FLOATING)
[`WindowsManager.STATE_AUTOHIDE`](WindowsManager.html#STATE_AUTOHIDE)
[`WindowsManager.STATE_HIDDEN`](WindowsManager.html#STATE_HIDDEN)
 ============ METHOD DETAIL ========== 
Method Details
getId
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getId()
Returns id of the window component.
Returns:
id of the component.
getTabTitle
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTabTitle()
Returns window's tab's title.
Returns:
tab's title.
getName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Returns name (title) of the window component.
Returns:
title of the window.
getIcon
@CheckForNullpublic [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getIcon()
Returns icon of the window component.
Returns:
icon of the window.
getSide
public int getSide()
Returns the window component side in the JIDE interface style.
Returns:
side constant.
getState
public int getState()
Returns the window component initial docking state in the JIDE interface style.
Returns:
side constant.
isRemoveOnHide
public boolean isRemoveOnHide()
Returns if the window component should be removed on hide.
Returns:
true if window is removed on hide, otherwise - false.
setIcon
public void setIcon(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Set icon for the window.
Parameters:
`icon` - window component icon.
setId
public void setId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Set id for the window component.
Parameters:
`id` - id
setTabTitle
public void setTabTitle([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tabTitle)
Sets title of window's tab.
Parameters:
`tabTitle` - tab's title
setName
public void setName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Set name (title) for the window component.
Parameters:
`name` - name
setRemoveOnHide
public void setRemoveOnHide(boolean removeOnHide)
Set if remove the window component on
Parameters:
`removeOnHide` - remove on hide
setSide
public void setSide(int side)
Set the window component side in JIDE interface style.
Parameters:
`side` - side
setState
public void setState(int state)
Set the window component initial docking state in JIDE interface style.
Parameters:
`state` - state
getIndex
public int getIndex()
Returns the window component index in the JIDE interface style.
Returns:
index
setIndex
public void setIndex(int index)
Set the window component initial docking index in JIDE interface style.
Parameters:
`index` - index
isDockable
public boolean isDockable()
Returns:
true if window is dockable
setDockable
public void setDockable(boolean dockable)
Set dockable initial state of the window
Parameters:
`dockable` - true if window is dockable
getInitialFloatingBounds
@CheckForNullpublic [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getInitialFloatingBounds()
Returns:
initial bounds for floating window or null if default must be used.
setInitialFloatingBounds
public void setInitialFloatingBounds(@CheckForNull
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) initialFloatingBounds)
Sets initial bounds for floating window. Default bounds will be used if not specified.
Parameters:
`initialFloatingBounds` - bounds
isShowTitleBar
public boolean isShowTitleBar()
setShowTitleBar
public void setShowTitleBar(boolean showTitleBar)
isRearrangable
public boolean isRearrangable()
setRearrangable
public void setRearrangable(boolean rearrangable)
isFloatable
public boolean isFloatable()
setFloatable
public void setFloatable(boolean floatable)
isAutohidable
public boolean isAutohidable()
setAutohidable
public void setAutohidable(boolean autohidable)
isMaximizable
public boolean isMaximizable()
setMaximizable
public void setMaximizable(boolean maximizable)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Class WindowComponentInfo">Class WindowComponentInfo</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.WindowComponentInfo</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">WindowComponentInfo</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Stores information about window component - id, name, icon and etc.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,javax.swing.Icon,int,int,boolean)">WindowComponentInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tabTitle,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 int side,
 int state,
 boolean removeOnHide)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,javax.swing.Icon,int,int,boolean)">WindowComponentInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 int side,
 int state,
 boolean removeOnHide)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon()">getIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns icon of the window component.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getId()">getId</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns id of the window component.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIndex()">getIndex</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the window component index in the JIDE interface style.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInitialFloatingBounds()">getInitialFloatingBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns name (title) of the window component.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSide()">getSide</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the window component side in the JIDE interface style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getState()">getState</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the window component initial docking state in the JIDE interface style.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTabTitle()">getTabTitle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns window's tab's title.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutohidable()">isAutohidable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDockable()">isDockable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFloatable()">isFloatable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMaximizable()">isMaximizable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRearrangable()">isRearrangable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemoveOnHide()">isRemoveOnHide</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns if the window component should be removed on hide.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowTitleBar()">isShowTitleBar</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutohidable(boolean)">setAutohidable</a><wbr/>(boolean autohidable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDockable(boolean)">setDockable</a><wbr/>(boolean dockable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set dockable initial state of the window</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFloatable(boolean)">setFloatable</a><wbr/>(boolean floatable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIcon(javax.swing.Icon)">setIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set icon for the window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setId(java.lang.String)">setId</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set id for the window component.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIndex(int)">setIndex</a><wbr/>(int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the window component initial docking index in JIDE interface style.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInitialFloatingBounds(java.awt.Rectangle)">setInitialFloatingBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> initialFloatingBounds)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets initial bounds for floating window.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMaximizable(boolean)">setMaximizable</a><wbr/>(boolean maximizable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set name (title) for the window component.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRearrangable(boolean)">setRearrangable</a><wbr/>(boolean rearrangable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRemoveOnHide(boolean)">setRemoveOnHide</a><wbr/>(boolean removeOnHide)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if remove the window component on</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowTitleBar(boolean)">setShowTitleBar</a><wbr/>(boolean showTitleBar)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSide(int)">setSide</a><wbr/>(int side)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the window component side in JIDE interface style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setState(int)">setState</a><wbr/>(int state)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the window component initial docking state in JIDE interface style.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTabTitle(java.lang.String)">setTabTitle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tabTitle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets title of window's tab.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,javax.swing.Icon,int,int,boolean)">
<h3>WindowComponentInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">WindowComponentInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 int side,
 int state,
 boolean removeOnHide)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - id of the window component.</dd>
<dd><code>name</code> - name (title) of the window.</dd>
<dd><code>icon</code> - icon of the window.</dd>
<dd><code>side</code> - indicates the side to place the window component in the JIDE interface style.</dd>
<dd><code>state</code> - indicates the docking state of the window component in the JIDE interface style.</dd>
<dd><code>removeOnHide</code> - true if the window should be removed on hide, false if it should be just hide.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="WindowsManager.html#SIDE_EAST"><code>WindowsManager.SIDE_EAST</code></a></li>
<li><a href="WindowsManager.html#SIDE_NORTH"><code>WindowsManager.SIDE_NORTH</code></a></li>
<li><a href="WindowsManager.html#SIDE_SOUTH"><code>WindowsManager.SIDE_SOUTH</code></a></li>
<li><a href="WindowsManager.html#SIDE_WEST"><code>WindowsManager.SIDE_WEST</code></a></li>
<li><a href="WindowsManager.html#STATE_DOCKED"><code>WindowsManager.STATE_DOCKED</code></a></li>
<li><a href="WindowsManager.html#STATE_FLOATING"><code>WindowsManager.STATE_FLOATING</code></a></li>
<li><a href="WindowsManager.html#STATE_AUTOHIDE"><code>WindowsManager.STATE_AUTOHIDE</code></a></li>
<li><a href="WindowsManager.html#STATE_HIDDEN"><code>WindowsManager.STATE_HIDDEN</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,javax.swing.Icon,int,int,boolean)">
<h3>WindowComponentInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">WindowComponentInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tabTitle,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 int side,
 int state,
 boolean removeOnHide)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - id of the window component.</dd>
<dd><code>tabTitle</code> - the title of window's tab.</dd>
<dd><code>name</code> - name (title) of the window.</dd>
<dd><code>icon</code> - icon of the window.</dd>
<dd><code>side</code> - indicates the side to place the window component in the JIDE interface style.</dd>
<dd><code>state</code> - indicates the docking state of the window component in the JIDE interface style.</dd>
<dd><code>removeOnHide</code> - true if the window should be removed on hide, false if it should be just hide.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="WindowsManager.html#SIDE_EAST"><code>WindowsManager.SIDE_EAST</code></a></li>
<li><a href="WindowsManager.html#SIDE_NORTH"><code>WindowsManager.SIDE_NORTH</code></a></li>
<li><a href="WindowsManager.html#SIDE_SOUTH"><code>WindowsManager.SIDE_SOUTH</code></a></li>
<li><a href="WindowsManager.html#SIDE_WEST"><code>WindowsManager.SIDE_WEST</code></a></li>
<li><a href="WindowsManager.html#STATE_DOCKED"><code>WindowsManager.STATE_DOCKED</code></a></li>
<li><a href="WindowsManager.html#STATE_FLOATING"><code>WindowsManager.STATE_FLOATING</code></a></li>
<li><a href="WindowsManager.html#STATE_AUTOHIDE"><code>WindowsManager.STATE_AUTOHIDE</code></a></li>
<li><a href="WindowsManager.html#STATE_HIDDEN"><code>WindowsManager.STATE_HIDDEN</code></a></li>
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
<section class="detail" id="getId()">
<h3>getId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()</div>
<div class="block">Returns id of the window component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>id of the component.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTabTitle()">
<h3>getTabTitle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTabTitle</span>()</div>
<div class="block">Returns window's tab's title.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tab's title.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Returns name (title) of the window component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>title of the window.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon()">
<h3>getIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getIcon</span>()</div>
<div class="block">Returns icon of the window component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>icon of the window.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSide()">
<h3>getSide</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSide</span>()</div>
<div class="block">Returns the window component side in the JIDE interface style.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>side constant.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getState()">
<h3>getState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getState</span>()</div>
<div class="block">Returns the window component initial docking state in the JIDE interface style.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>side constant.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRemoveOnHide()">
<h3>isRemoveOnHide</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRemoveOnHide</span>()</div>
<div class="block">Returns if the window component should be removed on hide.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if window is removed on hide, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIcon(javax.swing.Icon)">
<h3>setIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="block">Set icon for the window.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - window component icon.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setId(java.lang.String)">
<h3>setId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setId</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Set id for the window component.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTabTitle(java.lang.String)">
<h3>setTabTitle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTabTitle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tabTitle)</span></div>
<div class="block">Sets title of window's tab.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tabTitle</code> - tab's title</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Set name (title) for the window component.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRemoveOnHide(boolean)">
<h3>setRemoveOnHide</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRemoveOnHide</span><wbr/><span class="parameters">(boolean removeOnHide)</span></div>
<div class="block">Set if remove the window component on</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>removeOnHide</code> - remove on hide</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSide(int)">
<h3>setSide</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSide</span><wbr/><span class="parameters">(int side)</span></div>
<div class="block">Set the window component side in JIDE interface style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>side</code> - side</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setState(int)">
<h3>setState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setState</span><wbr/><span class="parameters">(int state)</span></div>
<div class="block">Set the window component initial docking state in JIDE interface style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>state</code> - state</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIndex()">
<h3>getIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getIndex</span>()</div>
<div class="block">Returns the window component index in the JIDE interface style.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>index</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIndex(int)">
<h3>setIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIndex</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block">Set the window component initial docking index in JIDE interface style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - index</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDockable()">
<h3>isDockable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDockable</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if window is dockable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDockable(boolean)">
<h3>setDockable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDockable</span><wbr/><span class="parameters">(boolean dockable)</span></div>
<div class="block">Set dockable initial state of the window</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dockable</code> - true if window is dockable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInitialFloatingBounds()">
<h3>getInitialFloatingBounds</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getInitialFloatingBounds</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>initial bounds for floating window or null if default must be used.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInitialFloatingBounds(java.awt.Rectangle)">
<h3>setInitialFloatingBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInitialFloatingBounds</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> initialFloatingBounds)</span></div>
<div class="block">Sets initial bounds for floating window. Default bounds will be used if not specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>initialFloatingBounds</code> - bounds</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowTitleBar()">
<h3>isShowTitleBar</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowTitleBar</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setShowTitleBar(boolean)">
<h3>setShowTitleBar</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowTitleBar</span><wbr/><span class="parameters">(boolean showTitleBar)</span></div>
</section>
</li>
<li>
<section class="detail" id="isRearrangable()">
<h3>isRearrangable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRearrangable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setRearrangable(boolean)">
<h3>setRearrangable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRearrangable</span><wbr/><span class="parameters">(boolean rearrangable)</span></div>
</section>
</li>
<li>
<section class="detail" id="isFloatable()">
<h3>isFloatable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFloatable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setFloatable(boolean)">
<h3>setFloatable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFloatable</span><wbr/><span class="parameters">(boolean floatable)</span></div>
</section>
</li>
<li>
<section class="detail" id="isAutohidable()">
<h3>isAutohidable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAutohidable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setAutohidable(boolean)">
<h3>setAutohidable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutohidable</span><wbr/><span class="parameters">(boolean autohidable)</span></div>
</section>
</li>
<li>
<section class="detail" id="isMaximizable()">
<h3>isMaximizable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMaximizable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setMaximizable(boolean)">
<h3>setMaximizable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMaximizable</span><wbr/><span class="parameters">(boolean maximizable)</span></div>
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
