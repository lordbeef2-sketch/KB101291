# JAVA OPENAPI: Interactions (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/uml2/Interactions.html
- source_path: `com/nomagic/magicdraw/uml2/Interactions.html`
- source_sha256: `ad2f3191e3b0b340ed5353b1e9d18f950b7b843b8a6e009f18e7d291947575e2`
- captured_utc: `2026-07-14T16:58:33.360240+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2](package-summary.html)

## Class Interactions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml2.Interactions

public classInteractions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Convenient static methods to work with Interactions elements.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Interactions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html)`
`[getMessageSubstitute](#getMessageSubstitute(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Returns message substitute for given message or the given message, if no substitution found.
`static [Operation](../../uml2/ext/magicdraw/classes/mdkernel/Operation.html)`
`[getOperationOfCallMessage](#getOperationOfCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Gets the operation of call message.
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getReceiveElement](#getReceiveElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Gets the receive element.
`static [ConnectableElement](../../uml2/ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html)`
`[getRemovableConnectableElement](#getRemovableConnectableElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline))([Lifeline](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline)`
Check if the represents can be removed along with lifeline.
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getSendElement](#getSendElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Return send event holder of the given message.
`static [Signal](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html)`
`[getSignalOfMessage](#getSignalOfMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Gets the signal of message.
`static boolean`
`[isCallMessage](#isCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Indicates if message is a call message.
`static boolean`
`[isCreateMessage](#isCreateMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) msg)`
Checks if is creates the message.
`static boolean`
`[isDestroyMessage](#isDestroyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) msg)`
Checks if is destroy message.
`static boolean`
`[isFoundMessage](#isFoundMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Indicates if given message is a found message.
`static boolean`
`[isLostMessage](#isLostMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Indicates if given message is a lost message.
`static boolean`
`[isReplyMessage](#isReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Indicates if this message is a reply message.
`static boolean`
`[isSendMessage](#isSendMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Checks if is send message.
`static boolean`
`[isSynchMessage](#isSynchMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) msg)`
Checks if is synch message.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Interactions
public Interactions()
 ============ METHOD DETAIL ========== 
Method Details
getReceiveElement
@CheckForNullpublic static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getReceiveElement([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)
Gets the receive element.
Parameters:
`message` - the message
Returns:
the receive element
getSendElement
@CheckForNullpublic static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getSendElement([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)
Return send event holder of the given message.
 It can be:
 covered lifeline
 gate owner (Interaction, CombinedFragment, InteractionUse)
Parameters:
`message` - Given message, which will be analysed
Returns:
One of Lifeline, Interaction, CombinedFragment, InteractionUse.
 Can return null, if message has no send event
getRemovableConnectableElement
@CheckForNullpublic static [ConnectableElement](../../uml2/ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html) getRemovableConnectableElement([Lifeline](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline)
Check if the represents can be removed along with lifeline.
Parameters:
`lifeline` - lifeline
Returns:
connectible element that should be disposed
getSignalOfMessage
@CheckForNullpublic static [Signal](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html) getSignalOfMessage([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)
Gets the signal of message.
Parameters:
`message` - the message
Returns:
the signal of message
isSendMessage
public static boolean isSendMessage([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)
Checks if is send message.
Parameters:
`message` - the message
Returns:
true, if is send message
isLostMessage
public static boolean isLostMessage([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)
Indicates if given message is a lost message.
Parameters:
`message` - message to check.
Returns:
true if given message is a lost message, false otherwise.
isFoundMessage
public static boolean isFoundMessage([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)
Indicates if given message is a found message.
Parameters:
`message` - message to check.
Returns:
true if given message is a found message, false otherwise.
isSynchMessage
public static boolean isSynchMessage([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) msg)
Checks if is synch message.
Parameters:
`msg` - the msg
Returns:
true, if is synch message
isDestroyMessage
public static boolean isDestroyMessage([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) msg)
Checks if is destroy message.
Parameters:
`msg` - the msg
Returns:
true, if is destroy message
isReplyMessage
public static boolean isReplyMessage([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)
Indicates if this message is a reply message.
Parameters:
`message` - - message to check.
Returns:
true if this is a reply message, false otherwise.
isCallMessage
public static boolean isCallMessage([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)
Indicates if message is a call message.
Parameters:
`message` - - message to check.
Returns:
true if this message is a call message, false otherwise.
isCreateMessage
public static boolean isCreateMessage([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) msg)
Checks if is creates the message.
Parameters:
`msg` - the msg
Returns:
true, if is creates the message
getMessageSubstitute
public static [Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) getMessageSubstitute([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)
Returns message substitute for given message or the given message, if no substitution found. Message substitution
 is message found by the formal gate.
Parameters:
`message` - message, for which substitution will be searched
Returns:
given message if no substitution found
getOperationOfCallMessage
@CheckForNullpublic static [Operation](../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) getOperationOfCallMessage([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)
Gets the operation of call message.
Parameters:
`message` - the message
Returns:
the operation of call message

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2</a></div>
<h1 class="title" title="Class Interactions">Class Interactions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml2.Interactions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">Interactions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Convenient static methods to work with Interactions elements.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Interactions</a>()</code></div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessageSubstitute(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getMessageSubstitute</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns message substitute for given message or the given message, if no substitution found.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOperationOfCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getOperationOfCallMessage</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the operation of call message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReceiveElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getReceiveElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the receive element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemovableConnectableElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">getRemovableConnectableElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if the represents can be removed along with lifeline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSendElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getSendElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return send event holder of the given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSignalOfMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getSignalOfMessage</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the signal of message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isCallMessage</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if message is a call message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isCreateMessage</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> msg)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if is creates the message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDestroyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isDestroyMessage</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> msg)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if is destroy message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFoundMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isFoundMessage</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if given message is a found message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isLostMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isLostMessage</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if given message is a lost message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isReplyMessage</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if this message is a reply message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSendMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isSendMessage</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if is send message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSynchMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isSynchMessage</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> msg)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if is synch message.</div>
</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>Interactions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Interactions</span>()</div>
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
<section class="detail" id="getReceiveElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getReceiveElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getReceiveElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Gets the receive element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dt>Returns:</dt>
<dd>the receive element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSendElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getSendElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getSendElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Return send event holder of the given message.
 <p>It can be:
 <ul>
<li> covered lifeline
 <li> gate owner (Interaction, CombinedFragment, InteractionUse)</li></li></ul></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - Given message, which will be analysed</dd>
<dt>Returns:</dt>
<dd>One of Lifeline, Interaction, CombinedFragment, InteractionUse.
 Can return null, if message has no send event</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemovableConnectableElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">
<h3>getRemovableConnectableElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></span> <span class="element-name">getRemovableConnectableElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline)</span></div>
<div class="block">Check if the represents can be removed along with lifeline.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lifeline</code> - lifeline</dd>
<dt>Returns:</dt>
<dd>connectible element that should be disposed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignalOfMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getSignalOfMessage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></span> <span class="element-name">getSignalOfMessage</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Gets the signal of message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dt>Returns:</dt>
<dd>the signal of message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSendMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isSendMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSendMessage</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Checks if is send message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dt>Returns:</dt>
<dd>true, if is send message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLostMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isLostMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isLostMessage</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Indicates if given message is a lost message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message to check.</dd>
<dt>Returns:</dt>
<dd>true if given message is a lost message, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFoundMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isFoundMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFoundMessage</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Indicates if given message is a found message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message to check.</dd>
<dt>Returns:</dt>
<dd>true if given message is a found message, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSynchMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isSynchMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSynchMessage</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> msg)</span></div>
<div class="block">Checks if is synch message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>msg</code> - the msg</dd>
<dt>Returns:</dt>
<dd>true, if is synch message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDestroyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isDestroyMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDestroyMessage</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> msg)</span></div>
<div class="block">Checks if is destroy message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>msg</code> - the msg</dd>
<dt>Returns:</dt>
<dd>true, if is destroy message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isReplyMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isReplyMessage</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Indicates if this message is a reply message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - - message to check.</dd>
<dt>Returns:</dt>
<dd>true if this is a reply message, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isCallMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCallMessage</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Indicates if message is a call message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - - message to check.</dd>
<dt>Returns:</dt>
<dd>true if this message is a call message, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreateMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isCreateMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCreateMessage</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> msg)</span></div>
<div class="block">Checks if is creates the message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>msg</code> - the msg</dd>
<dt>Returns:</dt>
<dd>true, if is creates the message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMessageSubstitute(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getMessageSubstitute</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></span> <span class="element-name">getMessageSubstitute</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Returns message substitute for given message or the given message, if no substitution found. Message substitution
 is message found by the formal gate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message, for which substitution will be searched</dd>
<dt>Returns:</dt>
<dd>given message if no substitution found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOperationOfCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getOperationOfCallMessage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></span> <span class="element-name">getOperationOfCallMessage</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Gets the operation of call message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dt>Returns:</dt>
<dd>the operation of call message</dd>
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
