# JAVA OPENAPI: Activities (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml2/Activities.html
- source_path: `com/nomagic/magicdraw/uml2/Activities.html`
- source_sha256: `18326bd0bcd8f20e2c875c8435212e93d575d89e79bc2fe2a1ce586b89ca964c`
- captured_utc: `2026-07-14T16:52:15.979932+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2](package-summary.html)

## Class Activities

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml2.Activities

public classActivities
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Convenience utility methods that operate on elements from Activities.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Activities](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [AcceptEventAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html)`
`[getActionForEvent](#getActionForEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event))([Event](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html) event)`

`static [Event](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html)`
`[getEventForAction](#getEventForAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction))([AcceptEventAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html) action)`
Returns an event of given action.
`static [SignalEvent](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html)`
`[getSignalEventForAction](#getSignalEventForAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction))([AcceptEventAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html) action)`
Returns a signal event of given action.
`static [Signal](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html)`
`[getSignalForAction](#getSignalForAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction))([AcceptEventAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html) action)`
Returns a signal of given action.
`static [InputPin](../../uml2/ext/magicdraw/actions/mdbasicactions/InputPin.html)`
`[getTargetPin](#getTargetPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction))([InvocationAction](../../uml2/ext/magicdraw/actions/mdbasicactions/InvocationAction.html) invocationAction)`
Returns target pin of InvocationAction type elements that can have target
`static boolean`
`[isAcceptTimeEventAction](#isAcceptTimeEventAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction))([AcceptEventAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html) acceptEventAction)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Activities
public Activities()
 ============ METHOD DETAIL ========== 
Method Details
isAcceptTimeEventAction
public static boolean isAcceptTimeEventAction([AcceptEventAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html) acceptEventAction)
getEventForAction
@CheckForNullpublic static [Event](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html) getEventForAction([AcceptEventAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html) action)
Returns an event of given action. Event is taken from trigger.
Parameters:
`action` - the given action
Returns:
an event of given action
getSignalForAction
@CheckForNullpublic static [Signal](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html) getSignalForAction([AcceptEventAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html) action)
Returns a signal of given action. Signal is taken from trigger signal event.
Parameters:
`action` - the given action
Returns:
a signal of given action
getSignalEventForAction
@CheckForNullpublic static [SignalEvent](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html) getSignalEventForAction([AcceptEventAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html) action)
Returns a signal event of given action. Signal Event is taken from trigger.
Parameters:
`action` - the given action
Returns:
a signal event of given action
getActionForEvent
@CheckForNullpublic static [AcceptEventAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html) getActionForEvent([Event](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html) event)
getTargetPin
@CheckForNullpublic static [InputPin](../../uml2/ext/magicdraw/actions/mdbasicactions/InputPin.html) getTargetPin([InvocationAction](../../uml2/ext/magicdraw/actions/mdbasicactions/InvocationAction.html) invocationAction)
Returns target pin of InvocationAction type elements that can have target
Parameters:
`invocationAction` - action to get the target pin from
Returns:
target pin of the action

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2</a></div>
<h1 class="title" title="Class Activities">Class Activities</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml2.Activities</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">Activities</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Convenience utility methods that operate on elements from Activities.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Activities</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getActionForEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event)">getActionForEvent</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> event)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEventForAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">getEventForAction</a><wbr/>(<a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an event of given action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSignalEventForAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">getSignalEventForAction</a><wbr/>(<a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a signal event of given action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSignalForAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">getSignalForAction</a><wbr/>(<a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a signal of given action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction)">getTargetPin</a><wbr/>(<a href="../../uml2/ext/magicdraw/actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a> invocationAction)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns target pin of InvocationAction type elements that can have target</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAcceptTimeEventAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">isAcceptTimeEventAction</a><wbr/>(<a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> acceptEventAction)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
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
<h3>Activities</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Activities</span>()</div>
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
<section class="detail" id="isAcceptTimeEventAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">
<h3>isAcceptTimeEventAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAcceptTimeEventAction</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> acceptEventAction)</span></div>
</section>
</li>
<li>
<section class="detail" id="getEventForAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">
<h3>getEventForAction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a></span> <span class="element-name">getEventForAction</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> action)</span></div>
<div class="block">Returns an event of given action. Event is taken from trigger.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - the given action</dd>
<dt>Returns:</dt>
<dd>an event of given action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignalForAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">
<h3>getSignalForAction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></span> <span class="element-name">getSignalForAction</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> action)</span></div>
<div class="block">Returns a signal of given action. Signal is taken from trigger signal event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - the given action</dd>
<dt>Returns:</dt>
<dd>a signal of given action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignalEventForAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">
<h3>getSignalEventForAction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a></span> <span class="element-name">getSignalEventForAction</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> action)</span></div>
<div class="block">Returns a signal event of given action. Signal Event is taken from trigger.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - the given action</dd>
<dt>Returns:</dt>
<dd>a signal event of given action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActionForEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event)">
<h3>getActionForEvent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></span> <span class="element-name">getActionForEvent</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> event)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTargetPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction)">
<h3>getTargetPin</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></span> <span class="element-name">getTargetPin</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a> invocationAction)</span></div>
<div class="block">Returns target pin of InvocationAction type elements that can have target</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>invocationAction</code> - action to get the target pin from</dd>
<dt>Returns:</dt>
<dd>target pin of the action</dd>
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
