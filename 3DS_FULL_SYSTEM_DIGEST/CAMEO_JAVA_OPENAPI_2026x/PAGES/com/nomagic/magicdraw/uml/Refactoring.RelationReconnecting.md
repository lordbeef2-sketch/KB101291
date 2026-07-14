# JAVA OPENAPI: Refactoring.RelationReconnecting (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/uml/Refactoring.RelationReconnecting.html
- source_path: `com/nomagic/magicdraw/uml/Refactoring.RelationReconnecting.html`
- source_sha256: `c9f477bd692057fa0b1f60bb9adf46e76f1c6657a061b8ea466ab0da39c5bb5d`
- captured_utc: `2026-07-14T16:58:27.788176+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class Refactoring.RelationReconnecting

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.Refactoring.RelationReconnecting

Enclosing class:
`[Refactoring](Refactoring.html)`

@OpenApiAllpublic static final classRefactoring.RelationReconnecting
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Reconnects one relation so that it skips selected part of the model.
 Useful when removing elements from model.
 For detailed explanation see description of

reconnectRelationForSelection(java.util.List<com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element>, boolean)

method.
 An example how to reconnect relations:

````java
// A list of elements that specifies consistent part of the model
 // i.e. model elements of selected presentation elements in a diagram.
 List
 targetElements = ...;

 // Relationship reconnecting should be wrapped with session create/close calls.
 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Reconnect relation");

 // Decide if incoming or outgoing relation should be reconnected.
 boolean incoming = ...;

 // Reconnect relation.
 Element relation = Refactoring.RelationReconnecting.reconnectRelationForSelection(targetElements, incoming);

 // Check result for null to see if any relation was reconnected.
 if (relation != null)
 {
     // relation was reconnected
 }

 // Close the session.
 sessionManager.closeSession();
````

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[RelationReconnecting](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[reconnectRelationForSelection](#reconnectRelationForSelection(java.util.List,boolean))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> targetElements,
 boolean incoming)`
Reconnects one relation so that it skips selected part of the model.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
RelationReconnecting
public RelationReconnecting()
 ============ METHOD DETAIL ========== 
Method Details
reconnectRelationForSelection
@CheckForNullpublic static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) reconnectRelationForSelection([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> targetElements,
 boolean incoming)
 throws [ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html),
[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)
Reconnects one relation so that it skips selected part of the model.
 Updates paths of reconnected relation to preserve previous form.
 Exactly one incoming relation and exactly one outgoing relation must exist for the given selection,
 or [`IllegalArgumentException`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html) exception will be thrown.
 These two relations may or may not be included in the selection.
Incoming relation is a relation element that starts from a client element that **is not** among targeted elements, but
 targets a supplier element that **is** in the list of targeted elements.
 Outgoing relation is a relation element that targets supplier element that **is not** among targeted elements, but
 starts from a client element that **is** among targeted elements.
Setting `incoming = true` will change supplier point of the incoming relation to the supplier point of the outgoing relation.
 Setting `incoming = false` will change client point of the outgoing relation to the client point of the incoming relation.
Parameters:
`targetElements` - list of elements that specifies selected part of the model
`incoming` - should incoming or outgoing relation be reconnected
Returns:
reconnected relation or null, if no changes where made
Throws:
`[ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)` - when any of provided elements is read-only
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - when list of elements is empty or when count of incoming/outgoing relations is not one.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class Refactoring.RelationReconnecting">Class Refactoring.RelationReconnecting</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.Refactoring.RelationReconnecting</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="Refactoring.html" title="class in com.nomagic.magicdraw.uml">Refactoring</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public static final class </span><span class="element-name type-name-label">Refactoring.RelationReconnecting</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Reconnects one relation so that it skips selected part of the model.
 Useful when removing elements from model.
 For detailed explanation see description of <a href="#reconnectRelationForSelection(java.util.List,boolean)"><code>reconnectRelationForSelection(java.util.List&lt;com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element&gt;, boolean)</code></a> method.
 An example how to reconnect relations:
 <pre>
 // A list of elements that specifies consistent part of the model
 // i.e. model elements of selected presentation elements in a diagram.
 List<element> targetElements = ...;

 // Relationship reconnecting should be wrapped with session create/close calls.
 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Reconnect relation");

 // Decide if incoming or outgoing relation should be reconnected.
 boolean incoming = ...;

 // Reconnect relation.
 Element relation = Refactoring.RelationReconnecting.reconnectRelationForSelection(targetElements, incoming);

 // Check result for null to see if any relation was reconnected.
 if (relation != null)
 {
     // relation was reconnected
 }

 // Close the session.
 sessionManager.closeSession();
 </element></pre></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">RelationReconnecting</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#reconnectRelationForSelection(java.util.List,boolean)">reconnectRelationForSelection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; targetElements,
 boolean incoming)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Reconnects one relation so that it skips selected part of the model.</div>
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
<h3>RelationReconnecting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RelationReconnecting</span>()</div>
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
<section class="detail" id="reconnectRelationForSelection(java.util.List,boolean)">
<h3>reconnectRelationForSelection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">reconnectRelationForSelection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; targetElements,
 boolean incoming)</span>
                                             throws <span class="exceptions"><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block"><p>Reconnects one relation so that it skips selected part of the model.
 Updates paths of reconnected relation to preserve previous form.
 Exactly one incoming relation and exactly one outgoing relation must exist for the given selection,
 or <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> exception will be thrown.
 These two relations may or may not be included in the selection.</p>
<p>
<p>Incoming relation is a relation element that starts from a client element that <b>is not</b> among targeted elements, but
 targets a supplier element that <b>is</b> in the list of targeted elements.
 Outgoing relation is a relation element that targets supplier element that <b>is not</b> among targeted elements, but
 starts from a client element that <b>is</b> among targeted elements.</p>
<p>
 Setting <code>incoming = true</code> will change supplier point of the incoming relation to the supplier point of the outgoing relation.
 Setting <code>incoming = false</code> will change client point of the outgoing relation to the client point of the incoming relation.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetElements</code> - list of elements that specifies selected part of the model</dd>
<dd><code>incoming</code> - should incoming or outgoing relation be reconnected</dd>
<dt>Returns:</dt>
<dd>reconnected relation or null, if no changes where made</dd>
<dt>Throws:</dt>
<dd><code><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - when any of provided elements is read-only</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - when list of elements is empty or when count of incoming/outgoing relations is not one.</dd>
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
