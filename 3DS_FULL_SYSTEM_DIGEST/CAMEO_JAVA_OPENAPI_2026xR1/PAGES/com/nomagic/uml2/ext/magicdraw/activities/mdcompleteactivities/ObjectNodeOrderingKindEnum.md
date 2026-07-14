# JAVA OPENAPI: ObjectNodeOrderingKindEnum (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/activities/mdcompleteactivities/ObjectNodeOrderingKindEnum.html
- source_path: `com/nomagic/uml2/ext/magicdraw/activities/mdcompleteactivities/ObjectNodeOrderingKindEnum.html`
- source_sha256: `9f44eac2b31e8a777566803c2be199475ff8a9b74d97d97b01c9ca9f3abef44f`
- captured_utc: `2026-07-14T16:46:26.299150+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities](package-summary.html)

## Class ObjectNodeOrderingKindEnum

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.util.AbstractEnumerator
com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKindEnum

All Implemented Interfaces:
`[ObjectNodeOrderingKind](ObjectNodeOrderingKind.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `javax.jmi.reflect.RefEnum`, `org.eclipse.emf.common.util.Enumerator`

public final classObjectNodeOrderingKindEnum
extends org.eclipse.emf.common.util.AbstractEnumerator
implements [ObjectNodeOrderingKind](ObjectNodeOrderingKind.html)

begin-user-doc 
 A representation of the literals of the enumeration '***Object Node Ordering Kind***',
 and utility methods for working with them.
 end-user-doc 
 begin-model-doc 
 ObjectNodeOrderingKind is an enumeration indicating queuing order for offering the tokens held by an ObjectNode.
 end-model-doc

See Also:
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getObjectNodeOrderingKindEnum()`
[Serialized Form](../../../../../../../serialized-form.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKindEnum)
Model:
annotation="MOF package='activities.mdcompleteactivities'"
Generated:

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [ObjectNodeOrderingKind](ObjectNodeOrderingKind.html)`
`[FIFO](#FIFO)`
The '***FIFO***' literal object.
`static final int`
`[FIFO_VALUE](#FIFO_VALUE)`
The '***FIFO***' literal value.
`static final [ObjectNodeOrderingKind](ObjectNodeOrderingKind.html)`
`[LIFO](#LIFO)`
The '***LIFO***' literal object.
`static final int`
`[LIFO_VALUE](#LIFO_VALUE)`
The '***LIFO***' literal value.
`static final [ObjectNodeOrderingKind](ObjectNodeOrderingKind.html)`
`[ORDERED](#ORDERED)`
The '***Ordered***' literal object.
`static final int`
`[ORDERED_VALUE](#ORDERED_VALUE)`
The '***Ordered***' literal value.
`static final [ObjectNodeOrderingKind](ObjectNodeOrderingKind.html)`
`[UNORDERED](#UNORDERED)`
The '***Unordered***' literal object.
`static final int`
`[UNORDERED_VALUE](#UNORDERED_VALUE)`
The '***Unordered***' literal value.
`static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)`
`[VALUES](#VALUES)`
A public read-only list of all the '***Object Node Ordering Kind***' enumerators.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ObjectNodeOrderingKindEnum](ObjectNodeOrderingKindEnum.html)`
`[get](#get(int))(int value)`
Returns the '***Object Node Ordering Kind***' literal with the specified integer value.
`static [ObjectNodeOrderingKindEnum](ObjectNodeOrderingKindEnum.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)`
Returns the '***Object Node Ordering Kind***' literal with the specified literal value.
`static [ObjectNodeOrderingKindEnum](ObjectNodeOrderingKindEnum.html)`
`[getByName](#getByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Returns the '***Object Node Ordering Kind***' literal with the specified name.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)`
`[refTypeName](#refTypeName())()`
Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
`getLiteral, getName, getValue, toString, writeReplace`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.jmi.reflect.RefEnum
`equals, hashCode, toString`

============ FIELD DETAIL =========== 
Field Details
UNORDERED_VALUE
public static final int UNORDERED_VALUE
The '***Unordered***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates that tokens are unordered.
 end-model-doc
See Also:
[`UNORDERED`](#UNORDERED)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKindEnum.UNORDERED_VALUE)
Model:
name="unordered"
Generated:
ORDERED_VALUE
public static final int ORDERED_VALUE
The '***Ordered***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates that tokens are ordered.
 end-model-doc
See Also:
[`ORDERED`](#ORDERED)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKindEnum.ORDERED_VALUE)
Model:
name="ordered"
Generated:
LIFO_VALUE
public static final int LIFO_VALUE
The '***LIFO***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates that tokens are queued in a last in, first out manner.
 end-model-doc
See Also:
[`LIFO`](#LIFO)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKindEnum.LIFO_VALUE)
Model:
Generated:
FIFO_VALUE
public static final int FIFO_VALUE
The '***FIFO***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates that tokens are queued in a first in, first out manner.
 end-model-doc
See Also:
[`FIFO`](#FIFO)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKindEnum.FIFO_VALUE)
Model:
Generated:
UNORDERED
public static final [ObjectNodeOrderingKind](ObjectNodeOrderingKind.html) UNORDERED
The '***Unordered***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`UNORDERED_VALUE`](#UNORDERED_VALUE)
Generated:
ORDERED
public static final [ObjectNodeOrderingKind](ObjectNodeOrderingKind.html) ORDERED
The '***Ordered***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`ORDERED_VALUE`](#ORDERED_VALUE)
Generated:
LIFO
public static final [ObjectNodeOrderingKind](ObjectNodeOrderingKind.html) LIFO
The '***LIFO***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`LIFO_VALUE`](#LIFO_VALUE)
Generated:
FIFO
public static final [ObjectNodeOrderingKind](ObjectNodeOrderingKind.html) FIFO
The '***FIFO***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`FIFO_VALUE`](#FIFO_VALUE)
Generated:
VALUES
public static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) VALUES
A public read-only list of all the '***Object Node Ordering Kind***' enumerators.
 begin-user-doc 
 end-user-doc
Generated:
 ============ METHOD DETAIL ========== 
Method Details
refTypeName
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) refTypeName()
Specified by:
`refTypeName` in interface `javax.jmi.reflect.RefEnum`
get
public static [ObjectNodeOrderingKindEnum](ObjectNodeOrderingKindEnum.html) get([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)
Returns the '***Object Node Ordering Kind***' literal with the specified literal value.
 begin-user-doc 
 end-user-doc
Generated:
getByName
public static [ObjectNodeOrderingKindEnum](ObjectNodeOrderingKindEnum.html) getByName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Returns the '***Object Node Ordering Kind***' literal with the specified name.
 begin-user-doc 
 end-user-doc
Generated:
get
public static [ObjectNodeOrderingKindEnum](ObjectNodeOrderingKindEnum.html) get(int value)
Returns the '***Object Node Ordering Kind***' literal with the specified integer value.
 begin-user-doc 
 end-user-doc
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities</a></div>
<h1 class="title" title="Class ObjectNodeOrderingKindEnum">Class ObjectNodeOrderingKindEnum</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.util.AbstractEnumerator
<div class="inheritance">com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKindEnum</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code>javax.jmi.reflect.RefEnum</code>, <code>org.eclipse.emf.common.util.Enumerator</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">ObjectNodeOrderingKindEnum</span>
<span class="extends-implements">extends org.eclipse.emf.common.util.AbstractEnumerator
implements <a href="ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the literals of the enumeration '<em><b>Object Node Ordering Kind</b></em>',
 and utility methods for working with them.
 <!-- end-user-doc -->
<!-- begin-model-doc -->
 ObjectNodeOrderingKind is an enumeration indicating queuing order for offering the tokens held by an ObjectNode.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getObjectNodeOrderingKindEnum()</code></pre>
</details>
</li>
<li><a href="../../../../../../../serialized-form.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKindEnum">Serialized Form</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='activities.mdcompleteactivities'"</dd>
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
<div class="col-first even-row-color"><code>static final <a href="ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FIFO">FIFO</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>FIFO</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FIFO_VALUE">FIFO_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>FIFO</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LIFO">LIFO</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>LIFO</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LIFO_VALUE">LIFO_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>LIFO</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ORDERED">ORDERED</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Ordered</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ORDERED_VALUE">ORDERED_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Ordered</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#UNORDERED">UNORDERED</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Unordered</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UNORDERED_VALUE">UNORDERED_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Unordered</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUES">VALUES</a></code></div>
<div class="col-last even-row-color">
<div class="block">A public read-only list of all the '<em><b>Object Node Ordering Kind</b></em>' enumerators.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ObjectNodeOrderingKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(int)">get</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Object Node Ordering Kind</b></em>' literal with the specified integer value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ObjectNodeOrderingKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKindEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Object Node Ordering Kind</b></em>' literal with the specified literal value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ObjectNodeOrderingKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getByName(java.lang.String)">getByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Object Node Ordering Kind</b></em>' literal with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refTypeName()">refTypeName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.AbstractEnumerator">Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator</h3>
<code>getLiteral, getName, getValue, toString, writeReplace</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="UNORDERED_VALUE">
<h3>UNORDERED_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">UNORDERED_VALUE</span></div>
<div class="block">The '<em><b>Unordered</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates that tokens are unordered.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#UNORDERED"><code>UNORDERED</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKindEnum.UNORDERED_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="unordered"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ORDERED_VALUE">
<h3>ORDERED_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ORDERED_VALUE</span></div>
<div class="block">The '<em><b>Ordered</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates that tokens are ordered.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#ORDERED"><code>ORDERED</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKindEnum.ORDERED_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="ordered"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="LIFO_VALUE">
<h3>LIFO_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">LIFO_VALUE</span></div>
<div class="block">The '<em><b>LIFO</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates that tokens are queued in a last in, first out manner.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#LIFO"><code>LIFO</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKindEnum.LIFO_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="FIFO_VALUE">
<h3>FIFO_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">FIFO_VALUE</span></div>
<div class="block">The '<em><b>FIFO</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates that tokens are queued in a first in, first out manner.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#FIFO"><code>FIFO</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKindEnum.FIFO_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="UNORDERED">
<h3>UNORDERED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a></span> <span class="element-name">UNORDERED</span></div>
<div class="block">The '<em><b>Unordered</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#UNORDERED_VALUE"><code>UNORDERED_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ORDERED">
<h3>ORDERED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a></span> <span class="element-name">ORDERED</span></div>
<div class="block">The '<em><b>Ordered</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#ORDERED_VALUE"><code>ORDERED_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="LIFO">
<h3>LIFO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a></span> <span class="element-name">LIFO</span></div>
<div class="block">The '<em><b>LIFO</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#LIFO_VALUE"><code>LIFO_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="FIFO">
<h3>FIFO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a></span> <span class="element-name">FIFO</span></div>
<div class="block">The '<em><b>FIFO</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#FIFO_VALUE"><code>FIFO_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALUES">
<h3>VALUES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">VALUES</span></div>
<div class="block">A public read-only list of all the '<em><b>Object Node Ordering Kind</b></em>' enumerators.
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">refTypeName</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refTypeName</code> in interface <code>javax.jmi.reflect.RefEnum</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="get(java.lang.String)">
<h3>get</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ObjectNodeOrderingKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKindEnum</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</span></div>
<div class="block">Returns the '<em><b>Object Node Ordering Kind</b></em>' literal with the specified literal value.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ObjectNodeOrderingKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKindEnum</a></span> <span class="element-name">getByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the '<em><b>Object Node Ordering Kind</b></em>' literal with the specified name.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ObjectNodeOrderingKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKindEnum</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Returns the '<em><b>Object Node Ordering Kind</b></em>' literal with the specified integer value.
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
