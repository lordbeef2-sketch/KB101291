# JAVA OPENAPI: PortionKind (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/sysml/PortionKind.html
- source_path: `com/dassault_systemes/modeler/sysml/model/sysml/PortionKind.html`
- source_sha256: `7e3a9f225b32868e6510262da4d3b3478a25b94a6fed81dcf06bbdca9cc2a37a`
- captured_utc: `2026-07-14T16:45:04.538064+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model.sysml](package-summary.html)

## Class PortionKind

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.util.AbstractEnumerator
com.dassault_systemes.modeler.sysml.model.sysml.PortionKind

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `org.eclipse.emf.common.util.Enumerator`

@OpenApiAllpublic classPortionKind
extends org.eclipse.emf.common.util.AbstractEnumerator

A representation of the literals of the enumeration '***Portion Kind***',
 and utility methods for working with them.
 begin-model-doc 
`PortionKind` is an enumeration of the specific kinds of `*Occurrence*` portions that can be represented by an `OccurrenceUsage`.
 end-model-doc

See Also:
[`SysMLPackage.getPortionKind()`](SysMLPackage.html#getPortionKind())
[Serialized Form](../../../../../../serialized-form.html#com.dassault_systemes.modeler.sysml.model.sysml.PortionKind)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [PortionKind](PortionKind.html)`
`[SNAPSHOT](#SNAPSHOT)`
The '***Snapshot***' literal object.
`static final int`
`[SNAPSHOT_VALUE](#SNAPSHOT_VALUE)`
The '***Snapshot***' literal value.
`static final [PortionKind](PortionKind.html)`
`[TIMESLICE](#TIMESLICE)`
The '***Timeslice***' literal object.
`static final int`
`[TIMESLICE_VALUE](#TIMESLICE_VALUE)`
The '***Timeslice***' literal value.
`static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PortionKind](PortionKind.html)>`
`[VALUES](#VALUES)`
A public read-only list of all the '***Portion Kind***' enumerators.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [PortionKind](PortionKind.html)`
`[get](#get(int))(int value)`
Returns the '***Portion Kind***' literal with the specified integer value.
`static [PortionKind](PortionKind.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)`
Returns the '***Portion Kind***' literal with the specified literal value.
`static [PortionKind](PortionKind.html)`
`[getByName](#getByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Returns the '***Portion Kind***' literal with the specified name.
Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
`getLiteral, getName, getValue, toString, writeReplace`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
TIMESLICE
public static final [PortionKind](PortionKind.html) TIMESLICE
The '***Timeslice***' literal object.
 begin-model-doc 
A time slice of an `Occurrence` (a portion over time).
 end-model-doc
See Also:
[`TIMESLICE_VALUE`](#TIMESLICE_VALUE)
SNAPSHOT
public static final [PortionKind](PortionKind.html) SNAPSHOT
The '***Snapshot***' literal object.
 begin-model-doc 
A snapshot of an `Occurrence` (a time slice with zero duration).
 end-model-doc
See Also:
[`SNAPSHOT_VALUE`](#SNAPSHOT_VALUE)
TIMESLICE_VALUE
public static final int TIMESLICE_VALUE
The '***Timeslice***' literal value.
 begin-model-doc 
A time slice of an `Occurrence` (a portion over time).
 end-model-doc
See Also:
[`TIMESLICE`](#TIMESLICE)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.PortionKind.TIMESLICE_VALUE)
SNAPSHOT_VALUE
public static final int SNAPSHOT_VALUE
The '***Snapshot***' literal value.
 begin-model-doc 
A snapshot of an `Occurrence` (a time slice with zero duration).
 end-model-doc
See Also:
[`SNAPSHOT`](#SNAPSHOT)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.PortionKind.SNAPSHOT_VALUE)
VALUES
public static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PortionKind](PortionKind.html)> VALUES
A public read-only list of all the '***Portion Kind***' enumerators.
 ============ METHOD DETAIL ========== 
Method Details
get
@CheckForNullpublic static [PortionKind](PortionKind.html) get([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)
Returns the '***Portion Kind***' literal with the specified literal value.
Parameters:
`literal` - the literal.
Returns:
the matching enumerator or `null`.
getByName
@CheckForNullpublic static [PortionKind](PortionKind.html) getByName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Returns the '***Portion Kind***' literal with the specified name.
Parameters:
`name` - the name.
Returns:
the matching enumerator or `null`.
get
@CheckForNullpublic static [PortionKind](PortionKind.html) get(int value)
Returns the '***Portion Kind***' literal with the specified integer value.
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
<h1 class="title" title="Class PortionKind">Class PortionKind</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.util.AbstractEnumerator
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.sysml.PortionKind</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code>org.eclipse.emf.common.util.Enumerator</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PortionKind</span>
<span class="extends-implements">extends org.eclipse.emf.common.util.AbstractEnumerator</span></div>
<div class="block">A representation of the literals of the enumeration '<em><b>Portion Kind</b></em>',
 and utility methods for working with them.
 <!-- begin-model-doc -->
<p><code>PortionKind</code> is an enumeration of the specific kinds of <code><em>Occurrence</em></code> portions that can be represented by an <code>OccurrenceUsage</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="SysMLPackage.html#getPortionKind()"><code>SysMLPackage.getPortionKind()</code></a></li>
<li><a href="../../../../../../serialized-form.html#com.dassault_systemes.modeler.sysml.model.sysml.PortionKind">Serialized Form</a></li>
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
<div class="col-first even-row-color"><code>static final <a href="PortionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">PortionKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SNAPSHOT">SNAPSHOT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Snapshot</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SNAPSHOT_VALUE">SNAPSHOT_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Snapshot</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="PortionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">PortionKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TIMESLICE">TIMESLICE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Timeslice</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TIMESLICE_VALUE">TIMESLICE_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Timeslice</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="PortionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">PortionKind</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUES">VALUES</a></code></div>
<div class="col-last even-row-color">
<div class="block">A public read-only list of all the '<em><b>Portion Kind</b></em>' enumerators.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="PortionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">PortionKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(int)">get</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Portion Kind</b></em>' literal with the specified integer value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="PortionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">PortionKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Portion Kind</b></em>' literal with the specified literal value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="PortionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">PortionKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getByName(java.lang.String)">getByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Portion Kind</b></em>' literal with the specified name.</div>
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
<section class="detail" id="TIMESLICE">
<h3>TIMESLICE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="PortionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">PortionKind</a></span> <span class="element-name">TIMESLICE</span></div>
<div class="block">The '<em><b>Timeslice</b></em>' literal object.
 <!-- begin-model-doc -->
<p>A time slice of an <code>Occurrence</code> (a portion over time).</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#TIMESLICE_VALUE"><code>TIMESLICE_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SNAPSHOT">
<h3>SNAPSHOT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="PortionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">PortionKind</a></span> <span class="element-name">SNAPSHOT</span></div>
<div class="block">The '<em><b>Snapshot</b></em>' literal object.
 <!-- begin-model-doc -->
<p>A snapshot of an <code>Occurrence</code> (a time slice with zero duration).</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#SNAPSHOT_VALUE"><code>SNAPSHOT_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TIMESLICE_VALUE">
<h3>TIMESLICE_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">TIMESLICE_VALUE</span></div>
<div class="block">The '<em><b>Timeslice</b></em>' literal value.
 <!-- begin-model-doc -->
<p>A time slice of an <code>Occurrence</code> (a portion over time).</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#TIMESLICE"><code>TIMESLICE</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.PortionKind.TIMESLICE_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SNAPSHOT_VALUE">
<h3>SNAPSHOT_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SNAPSHOT_VALUE</span></div>
<div class="block">The '<em><b>Snapshot</b></em>' literal value.
 <!-- begin-model-doc -->
<p>A snapshot of an <code>Occurrence</code> (a time slice with zero duration).</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#SNAPSHOT"><code>SNAPSHOT</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.PortionKind.SNAPSHOT_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALUES">
<h3>VALUES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PortionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">PortionKind</a>&gt;</span> <span class="element-name">VALUES</span></div>
<div class="block">A public read-only list of all the '<em><b>Portion Kind</b></em>' enumerators.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="PortionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">PortionKind</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</span></div>
<div class="block">Returns the '<em><b>Portion Kind</b></em>' literal with the specified literal value.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="PortionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">PortionKind</a></span> <span class="element-name">getByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the '<em><b>Portion Kind</b></em>' literal with the specified name.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="PortionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">PortionKind</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Returns the '<em><b>Portion Kind</b></em>' literal with the specified integer value.</div>
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
