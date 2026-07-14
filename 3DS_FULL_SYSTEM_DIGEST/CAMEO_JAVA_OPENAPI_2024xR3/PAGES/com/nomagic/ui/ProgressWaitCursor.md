# JAVA OPENAPI: ProgressWaitCursor (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/ui/ProgressWaitCursor.html
- source_path: `com/nomagic/ui/ProgressWaitCursor.html`
- source_sha256: `fb262f49b5a7ae0daa84c9efb830a9aec10bd88ecafd203cda7089e043834a3b`
- captured_utc: `2026-07-14T16:56:10.038622+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Class ProgressWaitCursor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.ui.ProgressWaitCursor

@OpenApipublic classProgressWaitCursor
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Mouse wait cursor handling helper for progress monitors.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProgressWaitCursor](#%3Cinit%3E())()`
Creates a new progress wait cursor handling helper
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ProgressWaitCursor](ProgressWaitCursor.html)`
`[createProgressWaitCursorIgnoringMouseAndKeyEvents](#createProgressWaitCursorIgnoringMouseAndKeyEvents())()`
Creates instance of [`ProgressWaitCursor`](ProgressWaitCursor.html) which shows waiting mouse
 cursor and filters out all mouse and key events.
`void`
`[initializeWaitCursor](#initializeWaitCursor())()`
Initializes mouse wait cursor for all application windows
`void`
`[removeWaitCursor](#removeWaitCursor())()`
Removes mouse wait cursor and restores the original cursors for all
 application windows
`void`
`[trackCursor](#trackCursor(java.awt.Component,java.awt.event.MouseEvent,boolean))([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) progressComponent,
 [MouseEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html) mouseEvent,
 boolean waitCursorExpected)`
Tracks mouse cursor changes when mouse enters/leaves progress component.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProgressWaitCursor
public ProgressWaitCursor()
Creates a new progress wait cursor handling helper
 ============ METHOD DETAIL ========== 
Method Details
createProgressWaitCursorIgnoringMouseAndKeyEvents
public static [ProgressWaitCursor](ProgressWaitCursor.html) createProgressWaitCursorIgnoringMouseAndKeyEvents()
Creates instance of [`ProgressWaitCursor`](ProgressWaitCursor.html) which shows waiting mouse
 cursor and filters out all mouse and key events. Therefore user will not be
 able to interact with any components while [`ProgressWaitCursor`](ProgressWaitCursor.html) is
 not removed.
Returns:
instance of [`ProgressWaitCursor`](ProgressWaitCursor.html)
initializeWaitCursor
public void initializeWaitCursor()
Initializes mouse wait cursor for all application windows
removeWaitCursor
public void removeWaitCursor()
Removes mouse wait cursor and restores the original cursors for all
 application windows
trackCursor
public void trackCursor([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) progressComponent,
 [MouseEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html) mouseEvent,
 boolean waitCursorExpected)
Tracks mouse cursor changes when mouse enters/leaves progress component.
 This method is typically invoked from
 `EventQueueDispatcher.customDispatchMouseEvent()` and ensures that
 cursor changes to default cursor when mouse is over progress component or
 to wait cursor when mouse is over rest of controls/windows.
Parameters:
`progressComponent` - the progress component over which mouse cursor changes to
 default cursor
`mouseEvent` - pending mouse event
`waitCursorExpected` - `true` indicates that mouse cursor should change to wait
 cursor, `false` indicates that mouse cursor should
 change to default cursor
See Also:
[`EventQueueDispatcher.customDispatchMouseEvent(EventQueueDispatcher.Dispatcher, EventQueue, MouseEvent)`](EventQueueDispatcher.html#customDispatchMouseEvent(com.nomagic.ui.EventQueueDispatcher.Dispatcher,java.awt.EventQueue,java.awt.event.MouseEvent))

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Class ProgressWaitCursor">Class ProgressWaitCursor</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.ui.ProgressWaitCursor</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProgressWaitCursor</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Mouse wait cursor handling helper for progress monitors.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ProgressWaitCursor</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new progress wait cursor handling helper</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ProgressWaitCursor.html" title="class in com.nomagic.ui">ProgressWaitCursor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createProgressWaitCursorIgnoringMouseAndKeyEvents()">createProgressWaitCursorIgnoringMouseAndKeyEvents</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates instance of <a href="ProgressWaitCursor.html" title="class in com.nomagic.ui"><code>ProgressWaitCursor</code></a> which shows waiting mouse
 cursor and filters out all mouse and key events.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initializeWaitCursor()">initializeWaitCursor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initializes mouse wait cursor for all application windows</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeWaitCursor()">removeWaitCursor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes mouse wait cursor and restores the original cursors for all
 application windows</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#trackCursor(java.awt.Component,java.awt.event.MouseEvent,boolean)">trackCursor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> progressComponent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html" title="class or interface in java.awt.event">MouseEvent</a> mouseEvent,
 boolean waitCursorExpected)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tracks mouse cursor changes when mouse enters/leaves progress component.</div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>ProgressWaitCursor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProgressWaitCursor</span>()</div>
<div class="block">Creates a new progress wait cursor handling helper</div>
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
<section class="detail" id="createProgressWaitCursorIgnoringMouseAndKeyEvents()">
<h3>createProgressWaitCursorIgnoringMouseAndKeyEvents</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ProgressWaitCursor.html" title="class in com.nomagic.ui">ProgressWaitCursor</a></span> <span class="element-name">createProgressWaitCursorIgnoringMouseAndKeyEvents</span>()</div>
<div class="block">Creates instance of <a href="ProgressWaitCursor.html" title="class in com.nomagic.ui"><code>ProgressWaitCursor</code></a> which shows waiting mouse
 cursor and filters out all mouse and key events. Therefore user will not be
 able to interact with any components while <a href="ProgressWaitCursor.html" title="class in com.nomagic.ui"><code>ProgressWaitCursor</code></a> is
 not removed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instance of <a href="ProgressWaitCursor.html" title="class in com.nomagic.ui"><code>ProgressWaitCursor</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initializeWaitCursor()">
<h3>initializeWaitCursor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">initializeWaitCursor</span>()</div>
<div class="block">Initializes mouse wait cursor for all application windows</div>
</section>
</li>
<li>
<section class="detail" id="removeWaitCursor()">
<h3>removeWaitCursor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeWaitCursor</span>()</div>
<div class="block">Removes mouse wait cursor and restores the original cursors for all
 application windows</div>
</section>
</li>
<li>
<section class="detail" id="trackCursor(java.awt.Component,java.awt.event.MouseEvent,boolean)">
<h3>trackCursor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">trackCursor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> progressComponent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html" title="class or interface in java.awt.event">MouseEvent</a> mouseEvent,
 boolean waitCursorExpected)</span></div>
<div class="block">Tracks mouse cursor changes when mouse enters/leaves progress component.
 This method is typically invoked from
 <code>EventQueueDispatcher.customDispatchMouseEvent()</code> and ensures that
 cursor changes to default cursor when mouse is over progress component or
 to wait cursor when mouse is over rest of controls/windows.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>progressComponent</code> - the progress component over which mouse cursor changes to
            default cursor</dd>
<dd><code>mouseEvent</code> - pending mouse event</dd>
<dd><code>waitCursorExpected</code> - <code>true</code> indicates that mouse cursor should change to wait
            cursor, <code>false</code> indicates that mouse cursor should
            change to default cursor</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="EventQueueDispatcher.html#customDispatchMouseEvent(com.nomagic.ui.EventQueueDispatcher.Dispatcher,java.awt.EventQueue,java.awt.event.MouseEvent)"><code>EventQueueDispatcher.customDispatchMouseEvent(EventQueueDispatcher.Dispatcher, EventQueue, MouseEvent)</code></a></li>
</ul>
</dd>
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
