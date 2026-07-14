# JAVA OPENAPI: FeatureDirectionKind (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/FeatureDirectionKind.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/FeatureDirectionKind.html`
- source_sha256: `0ce3bf428d3ae8822be3346ad789691fb2fb21625f393cd0cd044b683db49395`
- captured_utc: `2026-07-14T16:44:48.896855+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Class FeatureDirectionKind

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.util.AbstractEnumerator
com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `org.eclipse.emf.common.util.Enumerator`

@OpenApiAllpublic classFeatureDirectionKind
extends org.eclipse.emf.common.util.AbstractEnumerator

A representation of the literals of the enumeration '***Feature Direction Kind***',
 and utility methods for working with them.
 begin-model-doc 
`FeatureDirectionKind` enumerates the possible kinds of `direction` that a `Feature` may be given as a member of a `Type`.
 end-model-doc

See Also:
[`KerMLPackage.getFeatureDirectionKind()`](KerMLPackage.html#getFeatureDirectionKind())
[Serialized Form](../../../../../../serialized-form.html#com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [FeatureDirectionKind](FeatureDirectionKind.html)`
`[IN](#IN)`
The '***In***' literal object.
`static final int`
`[IN_VALUE](#IN_VALUE)`
The '***In***' literal value.
`static final [FeatureDirectionKind](FeatureDirectionKind.html)`
`[INOUT](#INOUT)`
The '***Inout***' literal object.
`static final int`
`[INOUT_VALUE](#INOUT_VALUE)`
The '***Inout***' literal value.
`static final [FeatureDirectionKind](FeatureDirectionKind.html)`
`[OUT](#OUT)`
The '***Out***' literal object.
`static final int`
`[OUT_VALUE](#OUT_VALUE)`
The '***Out***' literal value.
`static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureDirectionKind](FeatureDirectionKind.html)>`
`[VALUES](#VALUES)`
A public read-only list of all the '***Feature Direction Kind***' enumerators.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [FeatureDirectionKind](FeatureDirectionKind.html)`
`[get](#get(int))(int value)`
Returns the '***Feature Direction Kind***' literal with the specified integer value.
`static [FeatureDirectionKind](FeatureDirectionKind.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)`
Returns the '***Feature Direction Kind***' literal with the specified literal value.
`static [FeatureDirectionKind](FeatureDirectionKind.html)`
`[getByName](#getByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Returns the '***Feature Direction Kind***' literal with the specified name.
Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
`getLiteral, getName, getValue, toString, writeReplace`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
IN
public static final [FeatureDirectionKind](FeatureDirectionKind.html) IN
The '***In***' literal object.
 begin-model-doc 
Values of the `Feature` on each instance of its domain are determined externally to that instance and used internally.
 end-model-doc
See Also:
[`IN_VALUE`](#IN_VALUE)
INOUT
public static final [FeatureDirectionKind](FeatureDirectionKind.html) INOUT
The '***Inout***' literal object.
 begin-model-doc 
Values of the `Feature` on each instance are determined either as *in* or *out* directions, or both.
 end-model-doc
See Also:
[`INOUT_VALUE`](#INOUT_VALUE)
OUT
public static final [FeatureDirectionKind](FeatureDirectionKind.html) OUT
The '***Out***' literal object.
 begin-model-doc 
Values of the `Feature` on each instance of its domain are determined internally to that instance and used externally.
 end-model-doc
See Also:
[`OUT_VALUE`](#OUT_VALUE)
IN_VALUE
public static final int IN_VALUE
The '***In***' literal value.
 begin-model-doc 
Values of the `Feature` on each instance of its domain are determined externally to that instance and used internally.
 end-model-doc
See Also:
[`IN`](#IN)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind.IN_VALUE)
INOUT_VALUE
public static final int INOUT_VALUE
The '***Inout***' literal value.
 begin-model-doc 
Values of the `Feature` on each instance are determined either as *in* or *out* directions, or both.
 end-model-doc
See Also:
[`INOUT`](#INOUT)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind.INOUT_VALUE)
OUT_VALUE
public static final int OUT_VALUE
The '***Out***' literal value.
 begin-model-doc 
Values of the `Feature` on each instance of its domain are determined internally to that instance and used externally.
 end-model-doc
See Also:
[`OUT`](#OUT)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind.OUT_VALUE)
VALUES
public static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureDirectionKind](FeatureDirectionKind.html)> VALUES
A public read-only list of all the '***Feature Direction Kind***' enumerators.
 ============ METHOD DETAIL ========== 
Method Details
get
@CheckForNullpublic static [FeatureDirectionKind](FeatureDirectionKind.html) get([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)
Returns the '***Feature Direction Kind***' literal with the specified literal value.
Parameters:
`literal` - the literal.
Returns:
the matching enumerator or `null`.
getByName
@CheckForNullpublic static [FeatureDirectionKind](FeatureDirectionKind.html) getByName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Returns the '***Feature Direction Kind***' literal with the specified name.
Parameters:
`name` - the name.
Returns:
the matching enumerator or `null`.
get
@CheckForNullpublic static [FeatureDirectionKind](FeatureDirectionKind.html) get(int value)
Returns the '***Feature Direction Kind***' literal with the specified integer value.
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Class FeatureDirectionKind">Class FeatureDirectionKind</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.util.AbstractEnumerator
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code>org.eclipse.emf.common.util.Enumerator</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">FeatureDirectionKind</span>
<span class="extends-implements">extends org.eclipse.emf.common.util.AbstractEnumerator</span></div>
<div class="block">A representation of the literals of the enumeration '<em><b>Feature Direction Kind</b></em>',
 and utility methods for working with them.
 <!-- begin-model-doc -->
<p><code>FeatureDirectionKind</code> enumerates the possible kinds of <code>direction</code> that a <code>Feature</code> may be given as a member of a <code>Type</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="KerMLPackage.html#getFeatureDirectionKind()"><code>KerMLPackage.getFeatureDirectionKind()</code></a></li>
<li><a href="../../../../../../serialized-form.html#com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind">Serialized Form</a></li>
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
<div class="col-first even-row-color"><code>static final <a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#IN">IN</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>In</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IN_VALUE">IN_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>In</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INOUT">INOUT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Inout</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INOUT_VALUE">INOUT_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Inout</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OUT">OUT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Out</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#OUT_VALUE">OUT_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Out</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUES">VALUES</a></code></div>
<div class="col-last even-row-color">
<div class="block">A public read-only list of all the '<em><b>Feature Direction Kind</b></em>' enumerators.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(int)">get</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Feature Direction Kind</b></em>' literal with the specified integer value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Feature Direction Kind</b></em>' literal with the specified literal value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getByName(java.lang.String)">getByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Feature Direction Kind</b></em>' literal with the specified name.</div>
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
<section class="detail" id="IN">
<h3>IN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">IN</span></div>
<div class="block">The '<em><b>In</b></em>' literal object.
 <!-- begin-model-doc -->
<p>Values of the <code>Feature</code> on each instance of its domain are determined externally to that instance and used internally.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#IN_VALUE"><code>IN_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INOUT">
<h3>INOUT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">INOUT</span></div>
<div class="block">The '<em><b>Inout</b></em>' literal object.
 <!-- begin-model-doc -->
<p>Values of the <code>Feature</code> on each instance are determined either as <em>in</em> or <em>out</em> directions, or both.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#INOUT_VALUE"><code>INOUT_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OUT">
<h3>OUT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">OUT</span></div>
<div class="block">The '<em><b>Out</b></em>' literal object.
 <!-- begin-model-doc -->
<p>Values of the <code>Feature</code> on each instance of its domain are determined internally to that instance and used externally.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#OUT_VALUE"><code>OUT_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IN_VALUE">
<h3>IN_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">IN_VALUE</span></div>
<div class="block">The '<em><b>In</b></em>' literal value.
 <!-- begin-model-doc -->
<p>Values of the <code>Feature</code> on each instance of its domain are determined externally to that instance and used internally.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#IN"><code>IN</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind.IN_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INOUT_VALUE">
<h3>INOUT_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">INOUT_VALUE</span></div>
<div class="block">The '<em><b>Inout</b></em>' literal value.
 <!-- begin-model-doc -->
<p>Values of the <code>Feature</code> on each instance are determined either as <em>in</em> or <em>out</em> directions, or both.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#INOUT"><code>INOUT</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind.INOUT_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OUT_VALUE">
<h3>OUT_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">OUT_VALUE</span></div>
<div class="block">The '<em><b>Out</b></em>' literal value.
 <!-- begin-model-doc -->
<p>Values of the <code>Feature</code> on each instance of its domain are determined internally to that instance and used externally.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#OUT"><code>OUT</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind.OUT_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALUES">
<h3>VALUES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a>&gt;</span> <span class="element-name">VALUES</span></div>
<div class="block">A public read-only list of all the '<em><b>Feature Direction Kind</b></em>' enumerators.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</span></div>
<div class="block">Returns the '<em><b>Feature Direction Kind</b></em>' literal with the specified literal value.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">getByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the '<em><b>Feature Direction Kind</b></em>' literal with the specified name.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Returns the '<em><b>Feature Direction Kind</b></em>' literal with the specified integer value.</div>
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
