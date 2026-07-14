# JAVA OPENAPI: AcceptActions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/AcceptActions.html
- source_path: `com/dassault_systemes/modeler/sysml/model/AcceptActions.html`
- source_sha256: `cc4e0e6630ad753fcb8f0c00b026f768d9ccd35e519b4378029817db3b39a72e`
- captured_utc: `2026-07-14T16:45:02.194032+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class AcceptActions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.AcceptActions

@OpenApiAllpublic classAcceptActions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility methods for accessing and modifying the payload and receiver
 parameters of an [`AcceptActionUsage`](sysml/AcceptActionUsage.html).

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[PAYLOAD_PARAMETER_INDEX](#PAYLOAD_PARAMETER_INDEX)`
Index of the payload input parameter.
`static final int`
`[RECEIVER_PARAMETER_INDEX](#RECEIVER_PARAMETER_INDEX)`
Index of the receiver input parameter.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AcceptActions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[addPayload](#addPayload(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,java.util.List))([AcceptActionUsage](sysml/AcceptActionUsage.html) acceptActionUsage,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Definition](sysml/Definition.html)> definitions)`
Adds the given definitions to the payload parameter of the accept action.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOrCreatePayloadParameter](#getOrCreatePayloadParameter(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage))([AcceptActionUsage](sysml/AcceptActionUsage.html) actionUsage)`
Returns the payload parameter of the accept action, creating it if necessary.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOrCreateReceiverParameter](#getOrCreateReceiverParameter(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage))([AcceptActionUsage](sysml/AcceptActionUsage.html) actionUsage)`
Returns the receiver parameter of the accept action, creating it if necessary.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOwnedPayloadParameter](#getOwnedPayloadParameter(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage))([AcceptActionUsage](sysml/AcceptActionUsage.html) actionUsage)`
Returns the owned payload parameter of the accept action, or `null`
 if it has not been created.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOwnedReceiverParameter](#getOwnedReceiverParameter(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage))([AcceptActionUsage](sysml/AcceptActionUsage.html) actionUsage)`
Returns the owned receiver parameter of the accept action, or `null`
 if it has not been created.
`static void`
`[setPayload](#setPayload(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,java.util.List))([AcceptActionUsage](sysml/AcceptActionUsage.html) actionUsage,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Definition](sysml/Definition.html)> definitions)`
Sets the payload of the accept action to the given definitions.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
PAYLOAD_PARAMETER_INDEX
public static final int PAYLOAD_PARAMETER_INDEX
Index of the payload input parameter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.AcceptActions.PAYLOAD_PARAMETER_INDEX)
RECEIVER_PARAMETER_INDEX
public static final int RECEIVER_PARAMETER_INDEX
Index of the receiver input parameter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.AcceptActions.RECEIVER_PARAMETER_INDEX)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AcceptActions
public AcceptActions()
 ============ METHOD DETAIL ========== 
Method Details
setPayload
public static void setPayload([AcceptActionUsage](sysml/AcceptActionUsage.html) actionUsage,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Definition](sysml/Definition.html)> definitions)
Sets the payload of the accept action to the given definitions.
 If a payload parameter already exists, any subsettings or existing
 value expressions are removed before assigning the new type.
 Only definition‑based payloads are supported.
Parameters:
`actionUsage` - the accept action usage
`definitions` - the definitions to assign as payload type(s)
addPayload
public static void addPayload([AcceptActionUsage](sysml/AcceptActionUsage.html) acceptActionUsage,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Definition](sysml/Definition.html)> definitions)
Adds the given definitions to the payload parameter of the accept action.
 Creates the payload parameter if it does not already exist.
Parameters:
`acceptActionUsage` - the accept action usage
`definitions` - the definitions to add as payload types
getOwnedPayloadParameter
@CheckForNullpublic static [Feature](../../kerml/model/kerml/Feature.html) getOwnedPayloadParameter([AcceptActionUsage](sysml/AcceptActionUsage.html) actionUsage)
Returns the owned payload parameter of the accept action, or `null`
 if it has not been created.
Parameters:
`actionUsage` - the accept action usage
Returns:
the owned payload parameter, or `null`
getOrCreatePayloadParameter
public static [Feature](../../kerml/model/kerml/Feature.html) getOrCreatePayloadParameter([AcceptActionUsage](sysml/AcceptActionUsage.html) actionUsage)
Returns the payload parameter of the accept action, creating it if necessary.
Parameters:
`actionUsage` - the accept action usage
Returns:
the existing or newly created payload parameter
getOwnedReceiverParameter
@CheckForNullpublic static [Feature](../../kerml/model/kerml/Feature.html) getOwnedReceiverParameter([AcceptActionUsage](sysml/AcceptActionUsage.html) actionUsage)
Returns the owned receiver parameter of the accept action, or `null`
 if it has not been created.
Parameters:
`actionUsage` - the accept action usage
Returns:
the owned receiver parameter, or `null`
getOrCreateReceiverParameter
public static [Feature](../../kerml/model/kerml/Feature.html) getOrCreateReceiverParameter([AcceptActionUsage](sysml/AcceptActionUsage.html) actionUsage)
Returns the receiver parameter of the accept action, creating it if necessary.
Parameters:
`actionUsage` - the accept action usage
Returns:
the existing or newly created receiver parameter

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class AcceptActions">Class AcceptActions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.AcceptActions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">AcceptActions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility methods for accessing and modifying the payload and receiver
 parameters of an <a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AcceptActionUsage</code></a>.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PAYLOAD_PARAMETER_INDEX">PAYLOAD_PARAMETER_INDEX</a></code></div>
<div class="col-last even-row-color">
<div class="block">Index of the payload input parameter.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RECEIVER_PARAMETER_INDEX">RECEIVER_PARAMETER_INDEX</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Index of the receiver input parameter.</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AcceptActions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addPayload(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,java.util.List)">addPayload</a><wbr/>(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> acceptActionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a>&gt; definitions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds the given definitions to the payload parameter of the accept action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreatePayloadParameter(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage)">getOrCreatePayloadParameter</a><wbr/>(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> actionUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the payload parameter of the accept action, creating it if necessary.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateReceiverParameter(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage)">getOrCreateReceiverParameter</a><wbr/>(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> actionUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the receiver parameter of the accept action, creating it if necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedPayloadParameter(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage)">getOwnedPayloadParameter</a><wbr/>(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> actionUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned payload parameter of the accept action, or <code>null</code>
 if it has not been created.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedReceiverParameter(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage)">getOwnedReceiverParameter</a><wbr/>(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> actionUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned receiver parameter of the accept action, or <code>null</code>
 if it has not been created.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setPayload(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,java.util.List)">setPayload</a><wbr/>(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a>&gt; definitions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the payload of the accept action to the given definitions.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="PAYLOAD_PARAMETER_INDEX">
<h3>PAYLOAD_PARAMETER_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">PAYLOAD_PARAMETER_INDEX</span></div>
<div class="block">Index of the payload input parameter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.AcceptActions.PAYLOAD_PARAMETER_INDEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RECEIVER_PARAMETER_INDEX">
<h3>RECEIVER_PARAMETER_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">RECEIVER_PARAMETER_INDEX</span></div>
<div class="block">Index of the receiver input parameter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.AcceptActions.RECEIVER_PARAMETER_INDEX">Constant Field Values</a></li>
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
<h3>AcceptActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AcceptActions</span>()</div>
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
<section class="detail" id="setPayload(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,java.util.List)">
<h3>setPayload</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setPayload</span><wbr/><span class="parameters">(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a>&gt; definitions)</span></div>
<div class="block">Sets the payload of the accept action to the given definitions.
 <p>
 If a payload parameter already exists, any subsettings or existing
 value expressions are removed before assigning the new type.
 Only definition‑based payloads are supported.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the accept action usage</dd>
<dd><code>definitions</code> - the definitions to assign as payload type(s)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPayload(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,java.util.List)">
<h3>addPayload</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addPayload</span><wbr/><span class="parameters">(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> acceptActionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a>&gt; definitions)</span></div>
<div class="block">Adds the given definitions to the payload parameter of the accept action.
 Creates the payload parameter if it does not already exist.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>acceptActionUsage</code> - the accept action usage</dd>
<dd><code>definitions</code> - the definitions to add as payload types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedPayloadParameter(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage)">
<h3>getOwnedPayloadParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOwnedPayloadParameter</span><wbr/><span class="parameters">(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> actionUsage)</span></div>
<div class="block">Returns the owned payload parameter of the accept action, or <code>null</code>
 if it has not been created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the accept action usage</dd>
<dt>Returns:</dt>
<dd>the owned payload parameter, or <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreatePayloadParameter(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage)">
<h3>getOrCreatePayloadParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreatePayloadParameter</span><wbr/><span class="parameters">(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> actionUsage)</span></div>
<div class="block">Returns the payload parameter of the accept action, creating it if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the accept action usage</dd>
<dt>Returns:</dt>
<dd>the existing or newly created payload parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedReceiverParameter(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage)">
<h3>getOwnedReceiverParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOwnedReceiverParameter</span><wbr/><span class="parameters">(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> actionUsage)</span></div>
<div class="block">Returns the owned receiver parameter of the accept action, or <code>null</code>
 if it has not been created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the accept action usage</dd>
<dt>Returns:</dt>
<dd>the owned receiver parameter, or <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateReceiverParameter(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage)">
<h3>getOrCreateReceiverParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreateReceiverParameter</span><wbr/><span class="parameters">(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> actionUsage)</span></div>
<div class="block">Returns the receiver parameter of the accept action, creating it if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the accept action usage</dd>
<dt>Returns:</dt>
<dd>the existing or newly created receiver parameter</dd>
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
