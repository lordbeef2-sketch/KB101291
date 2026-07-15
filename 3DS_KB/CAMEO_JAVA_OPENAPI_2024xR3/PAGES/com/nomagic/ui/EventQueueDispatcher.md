# JAVA OPENAPI: EventQueueDispatcher (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/ui/EventQueueDispatcher.html
- source_path: `com/nomagic/ui/EventQueueDispatcher.html`
- source_sha256: `b87077c65bffad91466a5f2fda4cd8877b734804663f160d385e43ddae706bb9`
- captured_utc: `2026-07-14T16:56:09.785620+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Class EventQueueDispatcher

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.ui.EventQueueDispatcher

@OpenApipublic abstract classEventQueueDispatcher
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
AWT event dispatcher which dispatches events in the event queue thread until done condition is encountered.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[EventQueueDispatcher](#%3Cinit%3E())()`
Creates a `EventQueueDispatcher` and resets done condition.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected boolean`
`[customDispatchMouseEvent](#customDispatchMouseEvent(com.nomagic.ui.EventQueueDispatcher.Dispatcher,java.awt.EventQueue,java.awt.event.MouseEvent))(com.nomagic.ui.EventQueueDispatcher.Dispatcher dispatcher,
 [EventQueue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/EventQueue.html) eventQueue,
 [MouseEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html) mouseEvent)`

`protected void`
`[dispatchEvents](#dispatchEvents())()`
Dispatches AWT events until done condition is encountered.
`protected boolean`
`[dispatchEvents](#dispatchEvents(int))(int timeout)`
Dispatches AWT events until done condition is encountered or
 timeout is reached whatever happens first.
`static void`
`[disposeSequencedEvent](#disposeSequencedEvent())()`
This is required to avoid hang.
`void`
`[doneDispatching](#doneDispatching())()`
Sets done condition which causes `dispatchEvents` method to exit.
`void`
`[forceTimeout](#forceTimeout())()`
Forcefully sets timeout condition which causes `dispatchEvents` method to exit.
`final [Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[AWTEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html)>`
`[getDispatchTheseEvents](#getDispatchTheseEvents())()`

`protected boolean`
`[isDoneDispatching](#isDoneDispatching())()`
The method has to be called from event thread.
`protected void`
`[reset](#reset())()`
Resets done condition.
`final void`
`[setDispatchTheseEvents](#setDispatchTheseEvents(java.util.function.Predicate))([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[AWTEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html)> dispatchTheseEvents)`
Set verification which events needs to be dispatched.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
EventQueueDispatcher
protected EventQueueDispatcher()
Creates a `EventQueueDispatcher` and resets done condition.
 ============ METHOD DETAIL ========== 
Method Details
reset
protected void reset()
Resets done condition.
 The method has to be called from event thread.
dispatchEvents
protected void dispatchEvents()
Dispatches AWT events until done condition is encountered.
 The method has to be called from event thread.
dispatchEvents
protected boolean dispatchEvents(int timeout)
Dispatches AWT events until done condition is encountered or
 timeout is reached whatever happens first.
 The method has to be called from event thread.
Parameters:
`timeout` - the timeout or -1 if there is no timeout
Returns:
`true` if dispatching has stopped because of done condition,
 `false` if dispatching has stopped because timeout was reached.
disposeSequencedEvent
public static void disposeSequencedEvent()
This is required to avoid hang.
doneDispatching
public void doneDispatching()
Sets done condition which causes `dispatchEvents` method to exit.
forceTimeout
public void forceTimeout()
Forcefully sets timeout condition which causes `dispatchEvents` method to exit.
isDoneDispatching
protected boolean isDoneDispatching()
The method has to be called from event thread.
Returns:
`true` if done condition was encountered.
customDispatchMouseEvent
protected boolean customDispatchMouseEvent(com.nomagic.ui.EventQueueDispatcher.Dispatcher dispatcher,
 [EventQueue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/EventQueue.html) eventQueue,
 [MouseEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html) mouseEvent)
setDispatchTheseEvents
public final void setDispatchTheseEvents([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[AWTEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html)> dispatchTheseEvents)
Set verification which events needs to be dispatched. For normal UI only invocation events are dispatched.
Parameters:
`dispatchTheseEvents` - predicate to check if event needs to be dispatched
getDispatchTheseEvents
public final [Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[AWTEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html)> getDispatchTheseEvents()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Class EventQueueDispatcher">Class EventQueueDispatcher</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.ui.EventQueueDispatcher</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">EventQueueDispatcher</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">AWT event dispatcher which dispatches events in the event queue thread until done condition is encountered.</div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">EventQueueDispatcher</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a <code>EventQueueDispatcher</code> and resets done condition.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#customDispatchMouseEvent(com.nomagic.ui.EventQueueDispatcher.Dispatcher,java.awt.EventQueue,java.awt.event.MouseEvent)">customDispatchMouseEvent</a><wbr/>(com.nomagic.ui.EventQueueDispatcher.Dispatcher dispatcher,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/EventQueue.html" title="class or interface in java.awt">EventQueue</a> eventQueue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html" title="class or interface in java.awt.event">MouseEvent</a> mouseEvent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispatchEvents()">dispatchEvents</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dispatches AWT events until done condition is encountered.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispatchEvents(int)">dispatchEvents</a><wbr/>(int timeout)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dispatches AWT events until done condition is encountered or
 timeout is reached whatever happens first.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#disposeSequencedEvent()">disposeSequencedEvent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">This is required to avoid hang.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#doneDispatching()">doneDispatching</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets done condition which causes <code>dispatchEvents</code> method to exit.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#forceTimeout()">forceTimeout</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Forcefully sets timeout condition which causes <code>dispatchEvents</code> method to exit.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html" title="class or interface in java.awt">AWTEvent</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDispatchTheseEvents()">getDispatchTheseEvents</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDoneDispatching()">isDoneDispatching</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The method has to be called from event thread.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reset()">reset</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Resets done condition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDispatchTheseEvents(java.util.function.Predicate)">setDispatchTheseEvents</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html" title="class or interface in java.awt">AWTEvent</a>&gt; dispatchTheseEvents)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set verification which events needs to be dispatched.</div>
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
<h3>EventQueueDispatcher</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">EventQueueDispatcher</span>()</div>
<div class="block">Creates a <code>EventQueueDispatcher</code> and resets done condition.</div>
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
<section class="detail" id="reset()">
<h3>reset</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">reset</span>()</div>
<div class="block">Resets done condition.
 <p>The method has to be called from event thread.</p></div>
</section>
</li>
<li>
<section class="detail" id="dispatchEvents()">
<h3>dispatchEvents</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">dispatchEvents</span>()</div>
<div class="block">Dispatches AWT events until done condition is encountered.
 <p>The method has to be called from event thread.</p></div>
</section>
</li>
<li>
<section class="detail" id="dispatchEvents(int)">
<h3>dispatchEvents</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">dispatchEvents</span><wbr/><span class="parameters">(int timeout)</span></div>
<div class="block">Dispatches AWT events until done condition is encountered or
 timeout is reached whatever happens first.
 <p>The method has to be called from event thread.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>timeout</code> - the timeout or -1 if there is no timeout</dd>
<dt>Returns:</dt>
<dd><code>true</code> if dispatching has stopped because of done condition,
 <code>false</code> if dispatching has stopped because timeout was reached.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disposeSequencedEvent()">
<h3>disposeSequencedEvent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">disposeSequencedEvent</span>()</div>
<div class="block">This is required to avoid hang.</div>
</section>
</li>
<li>
<section class="detail" id="doneDispatching()">
<h3>doneDispatching</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">doneDispatching</span>()</div>
<div class="block">Sets done condition which causes <code>dispatchEvents</code> method to exit.</div>
</section>
</li>
<li>
<section class="detail" id="forceTimeout()">
<h3>forceTimeout</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">forceTimeout</span>()</div>
<div class="block">Forcefully sets timeout condition which causes <code>dispatchEvents</code> method to exit.</div>
</section>
</li>
<li>
<section class="detail" id="isDoneDispatching()">
<h3>isDoneDispatching</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isDoneDispatching</span>()</div>
<div class="block"><p>The method has to be called from event thread.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if done condition was encountered.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="customDispatchMouseEvent(com.nomagic.ui.EventQueueDispatcher.Dispatcher,java.awt.EventQueue,java.awt.event.MouseEvent)">
<h3>customDispatchMouseEvent</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">customDispatchMouseEvent</span><wbr/><span class="parameters">(com.nomagic.ui.EventQueueDispatcher.Dispatcher dispatcher,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/EventQueue.html" title="class or interface in java.awt">EventQueue</a> eventQueue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/MouseEvent.html" title="class or interface in java.awt.event">MouseEvent</a> mouseEvent)</span></div>
</section>
</li>
<li>
<section class="detail" id="setDispatchTheseEvents(java.util.function.Predicate)">
<h3>setDispatchTheseEvents</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setDispatchTheseEvents</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html" title="class or interface in java.awt">AWTEvent</a>&gt; dispatchTheseEvents)</span></div>
<div class="block">Set verification which events needs to be dispatched. For normal UI only invocation events are dispatched.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dispatchTheseEvents</code> - predicate to check if event needs to be dispatched</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDispatchTheseEvents()">
<h3>getDispatchTheseEvents</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html" title="class or interface in java.awt">AWTEvent</a>&gt;</span> <span class="element-name">getDispatchTheseEvents</span>()</div>
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
