# JAVA OPENAPI: StateSubactionKind (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/sysml/StateSubactionKind.html
- source_path: `com/dassault_systemes/modeler/sysml/model/sysml/StateSubactionKind.html`
- source_sha256: `a7edc155a9ef04e3d03ed0ce61be221a8e99b5c52145b21cc57581b9892f58fc`
- captured_utc: `2026-07-14T16:45:04.807067+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model.sysml](package-summary.html)

## Class StateSubactionKind

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.util.AbstractEnumerator
com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionKind

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `org.eclipse.emf.common.util.Enumerator`

@OpenApiAllpublic classStateSubactionKind
extends org.eclipse.emf.common.util.AbstractEnumerator

A representation of the literals of the enumeration '***State Subaction Kind***',
 and utility methods for working with them.
 begin-model-doc 
A `StateSubactionKind` indicates whether the `action` of a StateSubactionMembership is an entry, do or exit action.
 end-model-doc

See Also:
[`SysMLPackage.getStateSubactionKind()`](SysMLPackage.html#getStateSubactionKind())
[Serialized Form](../../../../../../serialized-form.html#com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionKind)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [StateSubactionKind](StateSubactionKind.html)`
`[DO](#DO)`
The '***Do***' literal object.
`static final int`
`[DO_VALUE](#DO_VALUE)`
The '***Do***' literal value.
`static final [StateSubactionKind](StateSubactionKind.html)`
`[ENTRY](#ENTRY)`
The '***Entry***' literal object.
`static final int`
`[ENTRY_VALUE](#ENTRY_VALUE)`
The '***Entry***' literal value.
`static final [StateSubactionKind](StateSubactionKind.html)`
`[EXIT](#EXIT)`
The '***Exit***' literal object.
`static final int`
`[EXIT_VALUE](#EXIT_VALUE)`
The '***Exit***' literal value.
`static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[StateSubactionKind](StateSubactionKind.html)>`
`[VALUES](#VALUES)`
A public read-only list of all the '***State Subaction Kind***' enumerators.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [StateSubactionKind](StateSubactionKind.html)`
`[get](#get(int))(int value)`
Returns the '***State Subaction Kind***' literal with the specified integer value.
`static [StateSubactionKind](StateSubactionKind.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)`
Returns the '***State Subaction Kind***' literal with the specified literal value.
`static [StateSubactionKind](StateSubactionKind.html)`
`[getByName](#getByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Returns the '***State Subaction Kind***' literal with the specified name.
Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
`getLiteral, getName, getValue, toString, writeReplace`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ENTRY
public static final [StateSubactionKind](StateSubactionKind.html) ENTRY
The '***Entry***' literal object.
 begin-model-doc 
Indicates that the `action` of a `StateSubactionMembership` is an `entryAction`.
 end-model-doc
See Also:
[`ENTRY_VALUE`](#ENTRY_VALUE)
DO
public static final [StateSubactionKind](StateSubactionKind.html) DO
The '***Do***' literal object.
 begin-model-doc 
Indicates that the `action` of a `StateSubactionMembership` is a `doAction`.
 end-model-doc
See Also:
[`DO_VALUE`](#DO_VALUE)
EXIT
public static final [StateSubactionKind](StateSubactionKind.html) EXIT
The '***Exit***' literal object.
 begin-model-doc 
Indicates that the `action` of a `StateSubactionMembership` is an `exitAction`.
 end-model-doc
See Also:
[`EXIT_VALUE`](#EXIT_VALUE)
ENTRY_VALUE
public static final int ENTRY_VALUE
The '***Entry***' literal value.
 begin-model-doc 
Indicates that the `action` of a `StateSubactionMembership` is an `entryAction`.
 end-model-doc
See Also:
[`ENTRY`](#ENTRY)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionKind.ENTRY_VALUE)
DO_VALUE
public static final int DO_VALUE
The '***Do***' literal value.
 begin-model-doc 
Indicates that the `action` of a `StateSubactionMembership` is a `doAction`.
 end-model-doc
See Also:
[`DO`](#DO)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionKind.DO_VALUE)
EXIT_VALUE
public static final int EXIT_VALUE
The '***Exit***' literal value.
 begin-model-doc 
Indicates that the `action` of a `StateSubactionMembership` is an `exitAction`.
 end-model-doc
See Also:
[`EXIT`](#EXIT)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionKind.EXIT_VALUE)
VALUES
public static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[StateSubactionKind](StateSubactionKind.html)> VALUES
A public read-only list of all the '***State Subaction Kind***' enumerators.
 ============ METHOD DETAIL ========== 
Method Details
get
@CheckForNullpublic static [StateSubactionKind](StateSubactionKind.html) get([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)
Returns the '***State Subaction Kind***' literal with the specified literal value.
Parameters:
`literal` - the literal.
Returns:
the matching enumerator or `null`.
getByName
@CheckForNullpublic static [StateSubactionKind](StateSubactionKind.html) getByName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Returns the '***State Subaction Kind***' literal with the specified name.
Parameters:
`name` - the name.
Returns:
the matching enumerator or `null`.
get
@CheckForNullpublic static [StateSubactionKind](StateSubactionKind.html) get(int value)
Returns the '***State Subaction Kind***' literal with the specified integer value.
Parameters:
`value` - the integer value.
Returns:
the matching enumerator or `null`.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model.sysml</a></div>
<h1 class="title" title="Class StateSubactionKind">Class StateSubactionKind</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.util.AbstractEnumerator
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionKind</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code>org.eclipse.emf.common.util.Enumerator</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">StateSubactionKind</span>
<span class="extends-implements">extends org.eclipse.emf.common.util.AbstractEnumerator</span></div>
<div class="block">A representation of the literals of the enumeration '<em><b>State Subaction Kind</b></em>',
 and utility methods for working with them.
 <!-- begin-model-doc -->
<p>A <code>StateSubactionKind</code> indicates whether the <code>action</code> of a StateSubactionMembership is an entry, do or exit action.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="SysMLPackage.html#getStateSubactionKind()"><code>SysMLPackage.getStateSubactionKind()</code></a></li>
<li><a href="../../../../../../serialized-form.html#com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionKind">Serialized Form</a></li>
</ul>
</dd>
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
<div class="col-first even-row-color"><code>static final <a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DO">DO</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Do</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DO_VALUE">DO_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Do</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ENTRY">ENTRY</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Entry</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ENTRY_VALUE">ENTRY_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Entry</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXIT">EXIT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Exit</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EXIT_VALUE">EXIT_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Exit</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUES">VALUES</a></code></div>
<div class="col-last even-row-color">
<div class="block">A public read-only list of all the '<em><b>State Subaction Kind</b></em>' enumerators.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(int)">get</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>State Subaction Kind</b></em>' literal with the specified integer value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>State Subaction Kind</b></em>' literal with the specified literal value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getByName(java.lang.String)">getByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>State Subaction Kind</b></em>' literal with the specified name.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.AbstractEnumerator">Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator</h3>
<code>getLiteral, getName, getValue, toString, writeReplace</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="ENTRY">
<h3>ENTRY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a></span> <span class="element-name">ENTRY</span></div>
<div class="block">The '<em><b>Entry</b></em>' literal object.
 <!-- begin-model-doc -->
<p>Indicates that the <code>action</code> of a <code>StateSubactionMembership</code> is an <code>entryAction</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#ENTRY_VALUE"><code>ENTRY_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DO">
<h3>DO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a></span> <span class="element-name">DO</span></div>
<div class="block">The '<em><b>Do</b></em>' literal object.
 <!-- begin-model-doc -->
<p>Indicates that the <code>action</code> of a <code>StateSubactionMembership</code> is a <code>doAction</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#DO_VALUE"><code>DO_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXIT">
<h3>EXIT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a></span> <span class="element-name">EXIT</span></div>
<div class="block">The '<em><b>Exit</b></em>' literal object.
 <!-- begin-model-doc -->
<p>Indicates that the <code>action</code> of a <code>StateSubactionMembership</code> is an <code>exitAction</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#EXIT_VALUE"><code>EXIT_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENTRY_VALUE">
<h3>ENTRY_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ENTRY_VALUE</span></div>
<div class="block">The '<em><b>Entry</b></em>' literal value.
 <!-- begin-model-doc -->
<p>Indicates that the <code>action</code> of a <code>StateSubactionMembership</code> is an <code>entryAction</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#ENTRY"><code>ENTRY</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionKind.ENTRY_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DO_VALUE">
<h3>DO_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DO_VALUE</span></div>
<div class="block">The '<em><b>Do</b></em>' literal value.
 <!-- begin-model-doc -->
<p>Indicates that the <code>action</code> of a <code>StateSubactionMembership</code> is a <code>doAction</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#DO"><code>DO</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionKind.DO_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXIT_VALUE">
<h3>EXIT_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">EXIT_VALUE</span></div>
<div class="block">The '<em><b>Exit</b></em>' literal value.
 <!-- begin-model-doc -->
<p>Indicates that the <code>action</code> of a <code>StateSubactionMembership</code> is an <code>exitAction</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#EXIT"><code>EXIT</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionKind.EXIT_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALUES">
<h3>VALUES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a>&gt;</span> <span class="element-name">VALUES</span></div>
<div class="block">A public read-only list of all the '<em><b>State Subaction Kind</b></em>' enumerators.</div>
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
<section class="detail" id="get(java.lang.String)">
<h3>get</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</span></div>
<div class="block">Returns the '<em><b>State Subaction Kind</b></em>' literal with the specified literal value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>literal</code> - the literal.</dd>
<dt>Returns:</dt>
<dd>the matching enumerator or <code>null</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getByName(java.lang.String)">
<h3>getByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a></span> <span class="element-name">getByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the '<em><b>State Subaction Kind</b></em>' literal with the specified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name.</dd>
<dt>Returns:</dt>
<dd>the matching enumerator or <code>null</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="get(int)">
<h3>get</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Returns the '<em><b>State Subaction Kind</b></em>' literal with the specified integer value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the integer value.</dd>
<dt>Returns:</dt>
<dd>the matching enumerator or <code>null</code>.</dd>
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
