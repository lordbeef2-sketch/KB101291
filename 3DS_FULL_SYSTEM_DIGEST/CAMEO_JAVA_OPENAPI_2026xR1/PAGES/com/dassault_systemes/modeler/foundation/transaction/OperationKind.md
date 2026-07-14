# JAVA OPENAPI: OperationKind (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/foundation/transaction/OperationKind.html
- source_path: `com/dassault_systemes/modeler/foundation/transaction/OperationKind.html`
- source_sha256: `dd5302461769735eb4cf9fd4a649bda37f8af6ee5d61294d3ea009b252033451`
- captured_utc: `2026-07-14T16:44:44.747799+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.foundation.transaction](package-summary.html)

## Enum Class OperationKind

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html)<[OperationKind](OperationKind.html)>
com.dassault_systemes.modeler.foundation.transaction.OperationKind

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)<[OperationKind](OperationKind.html)>`, `[Constable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/constant/Constable.html)`

@OpenApiAllpublic enumOperationKind
extends [Enum](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html)<[OperationKind](OperationKind.html)>

Represents the kind of operation executed within a transaction.

 This enumeration is typically used in transaction listeners and other
 infrastructure components to understand the intent of a committed change.
 It allows distinguishing between generic model updates and operations
 performed through the [`Editing`](../editing/Editing.html) API, such as command execution,
 undo, and redo.
Understanding the `OperationKind` is useful when implementing
 custom validation, auditing, or integration logic that reacts differently
 depending on how the model was modified.

See Also:
[`Editing`](../editing/Editing.html)

=========== ENUM CONSTANT SUMMARY =========== 
Enum Constant Summary
Enum Constants
Enum Constant
Description
`[EDITING_BACK_OR_FORWARD](#EDITING_BACK_OR_FORWARD)`
Operation representing navigation in the command history:
 [`Editing.undo()`](../editing/Editing.html#undo()) or [`Editing.redo()`](../editing/Editing.html#redo()).
`[EDITING_EXECUTE](#EDITING_EXECUTE)`
Operation executed via [`Editing.execute(String, Runnable)`](../editing/Editing.html#execute(java.lang.String,java.lang.Runnable)).
`[OTHER](#OTHER)`
Any operation that is not performed through the [`Editing`](../editing/Editing.html) API.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [OperationKind](OperationKind.html)`
`[valueOf](#valueOf(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Returns the enum constant of this class with the specified name.
`static [OperationKind](OperationKind.html)[]`
`[values](#values())()`
Returns an array containing the constants of this enum class, in
the order they are declared.
Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ ENUM CONSTANT DETAIL =========== 
Enum Constant Details
OTHER
public static final [OperationKind](OperationKind.html) OTHER
Any operation that is not performed through the [`Editing`](../editing/Editing.html) API.

 This includes low-level or programmatic changes where no explicit
 [`Editing`](../editing/Editing.html) command is used.
EDITING_EXECUTE
public static final [OperationKind](OperationKind.html) EDITING_EXECUTE
Operation executed via [`Editing.execute(String, Runnable)`](../editing/Editing.html#execute(java.lang.String,java.lang.Runnable)).

 Represents standard command execution wrapped in a transaction.
 These operations participate in the command history and support undo/redo.
EDITING_BACK_OR_FORWARD
public static final [OperationKind](OperationKind.html) EDITING_BACK_OR_FORWARD
Operation representing navigation in the command history:
 [`Editing.undo()`](../editing/Editing.html#undo()) or [`Editing.redo()`](../editing/Editing.html#redo()).

 This indicates that the transaction was triggered by reverting
 or reapplying previously executed commands.
 ============ METHOD DETAIL ========== 
Method Details
values
public static [OperationKind](OperationKind.html)[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.
Returns:
an array containing the constants of this enum class, in the order they are declared
valueOf
public static [OperationKind](OperationKind.html) valueOf([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Returns the enum constant of this class with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this class. (Extraneous whitespace characters are 
not permitted.)
Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if this enum class has no constant with the specified name
`[NullPointerException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html)` - if the argument is null

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.foundation.transaction</a></div>
<h1 class="title" title="Enum Class OperationKind">Enum Class OperationKind</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="OperationKind.html" title="enum class in com.dassault_systemes.modeler.foundation.transaction">OperationKind</a>&gt;
<div class="inheritance">com.dassault_systemes.modeler.foundation.transaction.OperationKind</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="OperationKind.html" title="enum class in com.dassault_systemes.modeler.foundation.transaction">OperationKind</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public enum </span><span class="element-name type-name-label">OperationKind</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="OperationKind.html" title="enum class in com.dassault_systemes.modeler.foundation.transaction">OperationKind</a>&gt;</span></div>
<div class="block">Represents the kind of operation executed within a transaction.

 <p>This enumeration is typically used in transaction listeners and other
 infrastructure components to understand the intent of a committed change.
 It allows distinguishing between generic model updates and operations
 performed through the <a href="../editing/Editing.html" title="interface in com.dassault_systemes.modeler.foundation.editing"><code>Editing</code></a> API, such as command execution,
 undo, and redo.</p>
<p>Understanding the <code>OperationKind</code> is useful when implementing
 custom validation, auditing, or integration logic that reacts differently
 depending on how the model was modified.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../editing/Editing.html" title="interface in com.dassault_systemes.modeler.foundation.editing"><code>Editing</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section class="constants-summary" id="enum-constant-summary">
<h2>Enum Constant Summary</h2>
<div class="caption"><span>Enum Constants</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Enum Constant</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#EDITING_BACK_OR_FORWARD">EDITING_BACK_OR_FORWARD</a></code></div>
<div class="col-last even-row-color">
<div class="block">Operation representing navigation in the command history:
 <a href="../editing/Editing.html#undo()"><code>Editing.undo()</code></a> or <a href="../editing/Editing.html#redo()"><code>Editing.redo()</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#EDITING_EXECUTE">EDITING_EXECUTE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Operation executed via <a href="../editing/Editing.html#execute(java.lang.String,java.lang.Runnable)"><code>Editing.execute(String, Runnable)</code></a>.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#OTHER">OTHER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Any operation that is not performed through the <a href="../editing/Editing.html" title="interface in com.dassault_systemes.modeler.foundation.editing"><code>Editing</code></a> API.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="OperationKind.html" title="enum class in com.dassault_systemes.modeler.foundation.transaction">OperationKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="OperationKind.html" title="enum class in com.dassault_systemes.modeler.foundation.transaction">OperationKind</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#values()">values</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section class="constant-details" id="enum-constant-detail">
<h2>Enum Constant Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="OTHER">
<h3>OTHER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="OperationKind.html" title="enum class in com.dassault_systemes.modeler.foundation.transaction">OperationKind</a></span> <span class="element-name">OTHER</span></div>
<div class="block">Any operation that is not performed through the <a href="../editing/Editing.html" title="interface in com.dassault_systemes.modeler.foundation.editing"><code>Editing</code></a> API.

 <p>This includes low-level or programmatic changes where no explicit
 <a href="../editing/Editing.html" title="interface in com.dassault_systemes.modeler.foundation.editing"><code>Editing</code></a> command is used.</p></div>
</section>
</li>
<li>
<section class="detail" id="EDITING_EXECUTE">
<h3>EDITING_EXECUTE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="OperationKind.html" title="enum class in com.dassault_systemes.modeler.foundation.transaction">OperationKind</a></span> <span class="element-name">EDITING_EXECUTE</span></div>
<div class="block">Operation executed via <a href="../editing/Editing.html#execute(java.lang.String,java.lang.Runnable)"><code>Editing.execute(String, Runnable)</code></a>.

 <p>Represents standard command execution wrapped in a transaction.
 These operations participate in the command history and support undo/redo.</p></div>
</section>
</li>
<li>
<section class="detail" id="EDITING_BACK_OR_FORWARD">
<h3>EDITING_BACK_OR_FORWARD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="OperationKind.html" title="enum class in com.dassault_systemes.modeler.foundation.transaction">OperationKind</a></span> <span class="element-name">EDITING_BACK_OR_FORWARD</span></div>
<div class="block">Operation representing navigation in the command history:
 <a href="../editing/Editing.html#undo()"><code>Editing.undo()</code></a> or <a href="../editing/Editing.html#redo()"><code>Editing.redo()</code></a>.

 <p>This indicates that the transaction was triggered by reverting
 or reapplying previously executed commands.</p></div>
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
<section class="detail" id="values()">
<h3>values</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="OperationKind.html" title="enum class in com.dassault_systemes.modeler.foundation.transaction">OperationKind</a>[]</span> <span class="element-name">values</span>()</div>
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="OperationKind.html" title="enum class in com.dassault_systemes.modeler.foundation.transaction">OperationKind</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
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
