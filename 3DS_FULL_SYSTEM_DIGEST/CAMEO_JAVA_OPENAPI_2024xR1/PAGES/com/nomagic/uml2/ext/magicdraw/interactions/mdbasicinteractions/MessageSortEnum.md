# JAVA OPENAPI: MessageSortEnum (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageSortEnum.html
- source_path: `com/nomagic/uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageSortEnum.html`
- source_sha256: `c43721207ba5c15a7526142f8337725f54c5c5f3f5493aa4ce053744905a0472`
- captured_utc: `2026-07-14T16:53:01.295507+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions](package-summary.html)

## Class MessageSortEnum

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.util.AbstractEnumerator
com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum

All Implemented Interfaces:
`[MessageSort](MessageSort.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `javax.jmi.reflect.RefEnum`, `org.eclipse.emf.common.util.Enumerator`

public final classMessageSortEnum
extends org.eclipse.emf.common.util.AbstractEnumerator
implements [MessageSort](MessageSort.html)

begin-user-doc 
 A representation of the literals of the enumeration '***Message Sort***',
 and utility methods for working with them.
 end-user-doc 
 begin-model-doc 
 This is an enumerated type that identifies the type of communication action that was used to generate the Message.
 end-model-doc

See Also:
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getMessageSortEnum()`
[Serialized Form](../../../../../../../serialized-form.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum)
Model:
annotation="MOF package='interactions.mdbasicinteractions'"
Generated:

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[ASYNCH_CALL_VALUE](#ASYNCH_CALL_VALUE)`
The '***Asynch Call***' literal value.
`static final int`
`[ASYNCH_SIGNAL_VALUE](#ASYNCH_SIGNAL_VALUE)`
The '***Asynch Signal***' literal value.
`static final [MessageSort](MessageSort.html)`
`[ASYNCHCALL](#ASYNCHCALL)`
The '***Asynch Call***' literal object.
`static final [MessageSort](MessageSort.html)`
`[ASYNCHSIGNAL](#ASYNCHSIGNAL)`
The '***Asynch Signal***' literal object.
`static final int`
`[CREATE_MESSAGE_VALUE](#CREATE_MESSAGE_VALUE)`
The '***Create Message***' literal value.
`static final [MessageSort](MessageSort.html)`
`[CREATEMESSAGE](#CREATEMESSAGE)`
The '***Create Message***' literal object.
`static final int`
`[DELETE_MESSAGE_VALUE](#DELETE_MESSAGE_VALUE)`
The '***Delete Message***' literal value.
`static final [MessageSort](MessageSort.html)`
`[DELETEMESSAGE](#DELETEMESSAGE)`
The '***Delete Message***' literal object.
`static final [MessageSort](MessageSort.html)`
`[REPLY](#REPLY)`
The '***Reply***' literal object.
`static final int`
`[REPLY_VALUE](#REPLY_VALUE)`
The '***Reply***' literal value.
`static final int`
`[SYNCH_CALL_VALUE](#SYNCH_CALL_VALUE)`
The '***Synch Call***' literal value.
`static final [MessageSort](MessageSort.html)`
`[SYNCHCALL](#SYNCHCALL)`
The '***Synch Call***' literal object.
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[VALUES](#VALUES)`
A public read-only list of all the '***Message Sort***' enumerators.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [MessageSortEnum](MessageSortEnum.html)`
`[get](#get(int))(int value)`
Returns the '***Message Sort***' literal with the specified integer value.
`static [MessageSortEnum](MessageSortEnum.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) literal)`
Returns the '***Message Sort***' literal with the specified literal value.
`static [MessageSortEnum](MessageSortEnum.html)`
`[getByName](#getByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the '***Message Sort***' literal with the specified name.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[refTypeName](#refTypeName())()`
Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
`getLiteral, getName, getValue, toString, writeReplace`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.jmi.reflect.RefEnum
`equals, hashCode, toString`

============ FIELD DETAIL =========== 
Field Details
SYNCH_CALL_VALUE
public static final int SYNCH_CALL_VALUE
The '***Synch Call***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The message was generated by a synchronous call to an operation.
 end-model-doc
See Also:
[`SYNCHCALL`](#SYNCHCALL)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum.SYNCH_CALL_VALUE)
Model:
name="synchCall"
Generated:
ASYNCH_CALL_VALUE
public static final int ASYNCH_CALL_VALUE
The '***Asynch Call***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The message was generated by an asynchronous call to an operation; i.e., a CallAction with isSynchronous = false.
 end-model-doc
See Also:
[`ASYNCHCALL`](#ASYNCHCALL)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum.ASYNCH_CALL_VALUE)
Model:
name="asynchCall"
Generated:
ASYNCH_SIGNAL_VALUE
public static final int ASYNCH_SIGNAL_VALUE
The '***Asynch Signal***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The message was generated by an asynchronous send action.
 end-model-doc
See Also:
[`ASYNCHSIGNAL`](#ASYNCHSIGNAL)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum.ASYNCH_SIGNAL_VALUE)
Model:
name="asynchSignal"
Generated:
CREATE_MESSAGE_VALUE
public static final int CREATE_MESSAGE_VALUE
The '***Create Message***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The message designating the creation of another lifeline object.
 end-model-doc
See Also:
[`CREATEMESSAGE`](#CREATEMESSAGE)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum.CREATE_MESSAGE_VALUE)
Model:
name="createMessage"
Generated:
DELETE_MESSAGE_VALUE
public static final int DELETE_MESSAGE_VALUE
The '***Delete Message***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The message designating the termination of another lifeline.
 end-model-doc
See Also:
[`DELETEMESSAGE`](#DELETEMESSAGE)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum.DELETE_MESSAGE_VALUE)
Model:
name="deleteMessage"
Generated:
REPLY_VALUE
public static final int REPLY_VALUE
The '***Reply***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The message is a reply message to an operation call.
 end-model-doc
See Also:
[`REPLY`](#REPLY)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum.REPLY_VALUE)
Model:
name="reply"
Generated:
SYNCHCALL
public static final [MessageSort](MessageSort.html) SYNCHCALL
The '***Synch Call***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`SYNCH_CALL_VALUE`](#SYNCH_CALL_VALUE)
Generated:
ASYNCHCALL
public static final [MessageSort](MessageSort.html) ASYNCHCALL
The '***Asynch Call***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`ASYNCH_CALL_VALUE`](#ASYNCH_CALL_VALUE)
Generated:
ASYNCHSIGNAL
public static final [MessageSort](MessageSort.html) ASYNCHSIGNAL
The '***Asynch Signal***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`ASYNCH_SIGNAL_VALUE`](#ASYNCH_SIGNAL_VALUE)
Generated:
CREATEMESSAGE
public static final [MessageSort](MessageSort.html) CREATEMESSAGE
The '***Create Message***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`CREATE_MESSAGE_VALUE`](#CREATE_MESSAGE_VALUE)
Generated:
DELETEMESSAGE
public static final [MessageSort](MessageSort.html) DELETEMESSAGE
The '***Delete Message***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`DELETE_MESSAGE_VALUE`](#DELETE_MESSAGE_VALUE)
Generated:
REPLY
public static final [MessageSort](MessageSort.html) REPLY
The '***Reply***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`REPLY_VALUE`](#REPLY_VALUE)
Generated:
VALUES
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) VALUES
A public read-only list of all the '***Message Sort***' enumerators.
 begin-user-doc 
 end-user-doc
Generated:
 ============ METHOD DETAIL ========== 
Method Details
refTypeName
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) refTypeName()
Specified by:
`refTypeName` in interface `javax.jmi.reflect.RefEnum`
get
public static [MessageSortEnum](MessageSortEnum.html) get([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) literal)
Returns the '***Message Sort***' literal with the specified literal value.
 begin-user-doc 
 end-user-doc
Generated:
getByName
public static [MessageSortEnum](MessageSortEnum.html) getByName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Returns the '***Message Sort***' literal with the specified name.
 begin-user-doc 
 end-user-doc
Generated:
get
public static [MessageSortEnum](MessageSortEnum.html) get(int value)
Returns the '***Message Sort***' literal with the specified integer value.
 begin-user-doc 
 end-user-doc
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions</a></div>
<h1 class="title" title="Class MessageSortEnum">Class MessageSortEnum</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.util.AbstractEnumerator
<div class="inheritance">com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code>javax.jmi.reflect.RefEnum</code>, <code>org.eclipse.emf.common.util.Enumerator</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MessageSortEnum</span>
<span class="extends-implements">extends org.eclipse.emf.common.util.AbstractEnumerator
implements <a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the literals of the enumeration '<em><b>Message Sort</b></em>',
 and utility methods for working with them.
 <!-- end-user-doc -->
<!-- begin-model-doc -->
 This is an enumerated type that identifies the type of communication action that was used to generate the Message.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getMessageSortEnum()</code></li>
<li><a href="../../../../../../../serialized-form.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum">Serialized Form</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='interactions.mdbasicinteractions'"</dd>
<dt>Generated:</dt>
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
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ASYNCH_CALL_VALUE">ASYNCH_CALL_VALUE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Asynch Call</b></em>' literal value.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ASYNCH_SIGNAL_VALUE">ASYNCH_SIGNAL_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Asynch Signal</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ASYNCHCALL">ASYNCHCALL</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Asynch Call</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ASYNCHSIGNAL">ASYNCHSIGNAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Asynch Signal</b></em>' literal object.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CREATE_MESSAGE_VALUE">CREATE_MESSAGE_VALUE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Create Message</b></em>' literal value.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CREATEMESSAGE">CREATEMESSAGE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Create Message</b></em>' literal object.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DELETE_MESSAGE_VALUE">DELETE_MESSAGE_VALUE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Delete Message</b></em>' literal value.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DELETEMESSAGE">DELETEMESSAGE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Delete Message</b></em>' literal object.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REPLY">REPLY</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Reply</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REPLY_VALUE">REPLY_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Reply</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SYNCH_CALL_VALUE">SYNCH_CALL_VALUE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Synch Call</b></em>' literal value.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SYNCHCALL">SYNCHCALL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Synch Call</b></em>' literal object.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUES">VALUES</a></code></div>
<div class="col-last even-row-color">
<div class="block">A public read-only list of all the '<em><b>Message Sort</b></em>' enumerators.</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="MessageSortEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSortEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(int)">get</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Message Sort</b></em>' literal with the specified integer value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="MessageSortEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSortEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Message Sort</b></em>' literal with the specified literal value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="MessageSortEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSortEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getByName(java.lang.String)">getByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Message Sort</b></em>' literal with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refTypeName()">refTypeName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.AbstractEnumerator">Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator</h3>
<code>getLiteral, getName, getValue, toString, writeReplace</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefEnum">Methods inherited from interface javax.jmi.reflect.RefEnum</h3>
<code>equals, hashCode, toString</code></div>
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
<section class="detail" id="SYNCH_CALL_VALUE">
<h3>SYNCH_CALL_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SYNCH_CALL_VALUE</span></div>
<div class="block">The '<em><b>Synch Call</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The message was generated by a synchronous call to an operation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SYNCHCALL"><code>SYNCHCALL</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum.SYNCH_CALL_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="synchCall"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ASYNCH_CALL_VALUE">
<h3>ASYNCH_CALL_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ASYNCH_CALL_VALUE</span></div>
<div class="block">The '<em><b>Asynch Call</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The message was generated by an asynchronous call to an operation; i.e., a CallAction with isSynchronous = false.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#ASYNCHCALL"><code>ASYNCHCALL</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum.ASYNCH_CALL_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="asynchCall"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ASYNCH_SIGNAL_VALUE">
<h3>ASYNCH_SIGNAL_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ASYNCH_SIGNAL_VALUE</span></div>
<div class="block">The '<em><b>Asynch Signal</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The message was generated by an asynchronous send action.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#ASYNCHSIGNAL"><code>ASYNCHSIGNAL</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum.ASYNCH_SIGNAL_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="asynchSignal"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="CREATE_MESSAGE_VALUE">
<h3>CREATE_MESSAGE_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">CREATE_MESSAGE_VALUE</span></div>
<div class="block">The '<em><b>Create Message</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The message designating the creation of another lifeline object.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#CREATEMESSAGE"><code>CREATEMESSAGE</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum.CREATE_MESSAGE_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="createMessage"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="DELETE_MESSAGE_VALUE">
<h3>DELETE_MESSAGE_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DELETE_MESSAGE_VALUE</span></div>
<div class="block">The '<em><b>Delete Message</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The message designating the termination of another lifeline.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#DELETEMESSAGE"><code>DELETEMESSAGE</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum.DELETE_MESSAGE_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="deleteMessage"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="REPLY_VALUE">
<h3>REPLY_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">REPLY_VALUE</span></div>
<div class="block">The '<em><b>Reply</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The message is a reply message to an operation call.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#REPLY"><code>REPLY</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSortEnum.REPLY_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="reply"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="SYNCHCALL">
<h3>SYNCHCALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></span> <span class="element-name">SYNCHCALL</span></div>
<div class="block">The '<em><b>Synch Call</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SYNCH_CALL_VALUE"><code>SYNCH_CALL_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ASYNCHCALL">
<h3>ASYNCHCALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></span> <span class="element-name">ASYNCHCALL</span></div>
<div class="block">The '<em><b>Asynch Call</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#ASYNCH_CALL_VALUE"><code>ASYNCH_CALL_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ASYNCHSIGNAL">
<h3>ASYNCHSIGNAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></span> <span class="element-name">ASYNCHSIGNAL</span></div>
<div class="block">The '<em><b>Asynch Signal</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#ASYNCH_SIGNAL_VALUE"><code>ASYNCH_SIGNAL_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="CREATEMESSAGE">
<h3>CREATEMESSAGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></span> <span class="element-name">CREATEMESSAGE</span></div>
<div class="block">The '<em><b>Create Message</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#CREATE_MESSAGE_VALUE"><code>CREATE_MESSAGE_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="DELETEMESSAGE">
<h3>DELETEMESSAGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></span> <span class="element-name">DELETEMESSAGE</span></div>
<div class="block">The '<em><b>Delete Message</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#DELETE_MESSAGE_VALUE"><code>DELETE_MESSAGE_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="REPLY">
<h3>REPLY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></span> <span class="element-name">REPLY</span></div>
<div class="block">The '<em><b>Reply</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#REPLY_VALUE"><code>REPLY_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALUES">
<h3>VALUES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">VALUES</span></div>
<div class="block">A public read-only list of all the '<em><b>Message Sort</b></em>' enumerators.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Generated:</dt>
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
<section class="detail" id="refTypeName()">
<h3>refTypeName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">refTypeName</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refTypeName</code> in interface <code>javax.jmi.reflect.RefEnum</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="get(java.lang.String)">
<h3>get</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="MessageSortEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSortEnum</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</span></div>
<div class="block">Returns the '<em><b>Message Sort</b></em>' literal with the specified literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getByName(java.lang.String)">
<h3>getByName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="MessageSortEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSortEnum</a></span> <span class="element-name">getByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the '<em><b>Message Sort</b></em>' literal with the specified name.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get(int)">
<h3>get</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="MessageSortEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSortEnum</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Returns the '<em><b>Message Sort</b></em>' literal with the specified integer value.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Generated:</dt>
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
