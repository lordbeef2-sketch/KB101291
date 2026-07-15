# JAVA OPENAPI: ProjectWindow (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/ui/ProjectWindow.html
- source_path: `com/nomagic/magicdraw/ui/ProjectWindow.html`
- source_sha256: `b32fdcd96f978bd6e610d7ac32481d667a816d2ad860f60311a5462ef0b75eb9`
- captured_utc: `2026-07-14T16:55:48.335377+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Class ProjectWindow

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.ProjectWindow

All Implemented Interfaces:
`[WindowComponent](browser/WindowComponent.html)`

@OpenApiAllpublic classProjectWindow
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [WindowComponent](browser/WindowComponent.html)

Project window is a window component associated with the project.
 To manage project windows of active project use [`ProjectWindowsManager`](ProjectWindowsManager.html) (Accessible via
 `Application.getInstance().getMainFrame().getProjectWindowsManager()`)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectWindow](#%3Cinit%3E(com.nomagic.magicdraw.ui.WindowComponentInfo,com.nomagic.magicdraw.ui.browser.WindowComponentContent))([WindowComponentInfo](WindowComponentInfo.html) info,
 [WindowComponentContent](browser/WindowComponentContent.html) content)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addProjectWindowListener](#addProjectWindowListener(com.nomagic.magicdraw.ui.ProjectWindowListener))([ProjectWindowListener](ProjectWindowListener.html) listener)`
Register given project window listener to this project window.
`final void`
`[closed](#closed())()`
The method is called when project window is closed.
`[WindowComponentContent](browser/WindowComponentContent.html)`
`[getContent](#getContent())()`
Returns this project window content.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getId](#getId())()`
Returns id of this project window.
`[WindowComponentInfo](WindowComponentInfo.html)`
`[getInfo](#getInfo())()`
Returns this project window info
`void`
`[removeProjectWindowListener](#removeProjectWindowListener(com.nomagic.magicdraw.ui.ProjectWindowListener))([ProjectWindowListener](ProjectWindowListener.html) listener)`
Unregister given project window listener from this project window.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectWindow
public ProjectWindow([WindowComponentInfo](WindowComponentInfo.html) info,
 [WindowComponentContent](browser/WindowComponentContent.html) content)
Constructor.
Parameters:
`info` - info about this project window.
`content` - contents of this project window.
 ============ METHOD DETAIL ========== 
Method Details
getInfo
public [WindowComponentInfo](WindowComponentInfo.html) getInfo()
Returns this project window info
Specified by:
`[getInfo](browser/WindowComponent.html#getInfo())` in interface `[WindowComponent](browser/WindowComponent.html)`
Returns:
component info
getId
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getId()
Returns id of this project window.
Returns:
project window id.
getContent
public [WindowComponentContent](browser/WindowComponentContent.html) getContent()
Returns this project window content.
Specified by:
`[getContent](browser/WindowComponent.html#getContent())` in interface `[WindowComponent](browser/WindowComponent.html)`
Returns:
project window content.
addProjectWindowListener
public void addProjectWindowListener([ProjectWindowListener](ProjectWindowListener.html) listener)
Register given project window listener to this project window.
Parameters:
`listener` - project window listener.
removeProjectWindowListener
public void removeProjectWindowListener([ProjectWindowListener](ProjectWindowListener.html) listener)
Unregister given project window listener from this project window.
Parameters:
`listener` - project window listener.
closed
public final void closed()
The method is called when project window is closed. Do not call this method.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Class ProjectWindow">Class ProjectWindow</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.ProjectWindow</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="browser/WindowComponent.html" title="interface in com.nomagic.magicdraw.ui.browser">WindowComponent</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProjectWindow</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="browser/WindowComponent.html" title="interface in com.nomagic.magicdraw.ui.browser">WindowComponent</a></span></div>
<div class="block">Project window is a window component associated with the project.
 To manage project windows of active project use <a href="ProjectWindowsManager.html" title="interface in com.nomagic.magicdraw.ui"><code>ProjectWindowsManager</code></a> (Accessible via
 <code>Application.getInstance().getMainFrame().getProjectWindowsManager()</code>)</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.ui.WindowComponentInfo,com.nomagic.magicdraw.ui.browser.WindowComponentContent)">ProjectWindow</a><wbr/>(<a href="WindowComponentInfo.html" title="class in com.nomagic.magicdraw.ui">WindowComponentInfo</a> info,
 <a href="browser/WindowComponentContent.html" title="interface in com.nomagic.magicdraw.ui.browser">WindowComponentContent</a> content)</code></div>
<div class="col-last even-row-color">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProjectWindowListener(com.nomagic.magicdraw.ui.ProjectWindowListener)">addProjectWindowListener</a><wbr/>(<a href="ProjectWindowListener.html" title="interface in com.nomagic.magicdraw.ui">ProjectWindowListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Register given project window listener to this project window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closed()">closed</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The method is called when project window is closed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="browser/WindowComponentContent.html" title="interface in com.nomagic.magicdraw.ui.browser">WindowComponentContent</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContent()">getContent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns this project window content.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getId()">getId</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns id of this project window.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="WindowComponentInfo.html" title="class in com.nomagic.magicdraw.ui">WindowComponentInfo</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInfo()">getInfo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns this project window info</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProjectWindowListener(com.nomagic.magicdraw.ui.ProjectWindowListener)">removeProjectWindowListener</a><wbr/>(<a href="ProjectWindowListener.html" title="interface in com.nomagic.magicdraw.ui">ProjectWindowListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregister given project window listener from this project window.</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.ui.WindowComponentInfo,com.nomagic.magicdraw.ui.browser.WindowComponentContent)">
<h3>ProjectWindow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectWindow</span><wbr/><span class="parameters">(<a href="WindowComponentInfo.html" title="class in com.nomagic.magicdraw.ui">WindowComponentInfo</a> info,
 <a href="browser/WindowComponentContent.html" title="interface in com.nomagic.magicdraw.ui.browser">WindowComponentContent</a> content)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>info</code> - info about this project window.</dd>
<dd><code>content</code> - contents of this project window.</dd>
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
<section class="detail" id="getInfo()">
<h3>getInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="WindowComponentInfo.html" title="class in com.nomagic.magicdraw.ui">WindowComponentInfo</a></span> <span class="element-name">getInfo</span>()</div>
<div class="block">Returns this project window info</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="browser/WindowComponent.html#getInfo()">getInfo</a></code> in interface <code><a href="browser/WindowComponent.html" title="interface in com.nomagic.magicdraw.ui.browser">WindowComponent</a></code></dd>
<dt>Returns:</dt>
<dd>component info</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getId()">
<h3>getId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()</div>
<div class="block">Returns id of this project window.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project window id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContent()">
<h3>getContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="browser/WindowComponentContent.html" title="interface in com.nomagic.magicdraw.ui.browser">WindowComponentContent</a></span> <span class="element-name">getContent</span>()</div>
<div class="block">Returns this project window content.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="browser/WindowComponent.html#getContent()">getContent</a></code> in interface <code><a href="browser/WindowComponent.html" title="interface in com.nomagic.magicdraw.ui.browser">WindowComponent</a></code></dd>
<dt>Returns:</dt>
<dd>project window content.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProjectWindowListener(com.nomagic.magicdraw.ui.ProjectWindowListener)">
<h3>addProjectWindowListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addProjectWindowListener</span><wbr/><span class="parameters">(<a href="ProjectWindowListener.html" title="interface in com.nomagic.magicdraw.ui">ProjectWindowListener</a> listener)</span></div>
<div class="block">Register given project window listener to this project window.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - project window listener.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeProjectWindowListener(com.nomagic.magicdraw.ui.ProjectWindowListener)">
<h3>removeProjectWindowListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeProjectWindowListener</span><wbr/><span class="parameters">(<a href="ProjectWindowListener.html" title="interface in com.nomagic.magicdraw.ui">ProjectWindowListener</a> listener)</span></div>
<div class="block">Unregister given project window listener from this project window.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - project window listener.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="closed()">
<h3>closed</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">closed</span>()</div>
<div class="block">The method is called when project window is closed. Do not call this method.</div>
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
