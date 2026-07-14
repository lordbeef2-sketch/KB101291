# JAVA OPENAPI: AggregationKindEnum (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/AggregationKindEnum.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/AggregationKindEnum.html`
- source_sha256: `82c165daae6d01d050cd027c619e488418eb43a33d9a397a2721ac0fb83e4147`
- captured_utc: `2026-07-14T16:56:20.969742+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Class AggregationKindEnum

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.util.AbstractEnumerator
com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKindEnum

All Implemented Interfaces:
`[AggregationKind](AggregationKind.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `javax.jmi.reflect.RefEnum`, `org.eclipse.emf.common.util.Enumerator`

public final classAggregationKindEnum
extends org.eclipse.emf.common.util.AbstractEnumerator
implements [AggregationKind](AggregationKind.html)

begin-user-doc 
 A representation of the literals of the enumeration '***Aggregation Kind***',
 and utility methods for working with them.
 end-user-doc 
 begin-model-doc 
 AggregationKind is an Enumeration for specifying the kind of aggregation of a Property.
 end-model-doc

See Also:
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getAggregationKindEnum()`
[Serialized Form](../../../../../../../serialized-form.html#com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKindEnum)
Model:
annotation="MOF package='classes.mdkernel'"
Generated:

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [AggregationKind](AggregationKind.html)`
`[COMPOSITE](#COMPOSITE)`
The '***Composite***' literal object.
`static final int`
`[COMPOSITE_VALUE](#COMPOSITE_VALUE)`
The '***Composite***' literal value.
`static final [AggregationKind](AggregationKind.html)`
`[NONE](#NONE)`
The '***None***' literal object.
`static final int`
`[NONE_VALUE](#NONE_VALUE)`
The '***None***' literal value.
`static final [AggregationKind](AggregationKind.html)`
`[SHARED](#SHARED)`
The '***Shared***' literal object.
`static final int`
`[SHARED_VALUE](#SHARED_VALUE)`
The '***Shared***' literal value.
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[VALUES](#VALUES)`
A public read-only list of all the '***Aggregation Kind***' enumerators.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [AggregationKindEnum](AggregationKindEnum.html)`
`[get](#get(int))(int value)`
Returns the '***Aggregation Kind***' literal with the specified integer value.
`static [AggregationKindEnum](AggregationKindEnum.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) literal)`
Returns the '***Aggregation Kind***' literal with the specified literal value.
`static [AggregationKindEnum](AggregationKindEnum.html)`
`[getByName](#getByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the '***Aggregation Kind***' literal with the specified name.
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
NONE_VALUE
public static final int NONE_VALUE
The '***None***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates that the Property has no aggregation.
 end-model-doc
See Also:
[`NONE`](#NONE)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKindEnum.NONE_VALUE)
Model:
name="none"
Generated:
SHARED_VALUE
public static final int SHARED_VALUE
The '***Shared***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates that the Property has shared aggregation.
 end-model-doc
See Also:
[`SHARED`](#SHARED)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKindEnum.SHARED_VALUE)
Model:
name="shared"
Generated:
COMPOSITE_VALUE
public static final int COMPOSITE_VALUE
The '***Composite***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates that the Property is aggregated compositely, i.e., the composite object has responsibility for the existence and storage of the composed objects
 (parts).
 end-model-doc
See Also:
[`COMPOSITE`](#COMPOSITE)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKindEnum.COMPOSITE_VALUE)
Model:
name="composite"
Generated:
NONE
public static final [AggregationKind](AggregationKind.html) NONE
The '***None***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`NONE_VALUE`](#NONE_VALUE)
Generated:
SHARED
public static final [AggregationKind](AggregationKind.html) SHARED
The '***Shared***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`SHARED_VALUE`](#SHARED_VALUE)
Generated:
COMPOSITE
public static final [AggregationKind](AggregationKind.html) COMPOSITE
The '***Composite***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`COMPOSITE_VALUE`](#COMPOSITE_VALUE)
Generated:
VALUES
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) VALUES
A public read-only list of all the '***Aggregation Kind***' enumerators.
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
public static [AggregationKindEnum](AggregationKindEnum.html) get([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) literal)
Returns the '***Aggregation Kind***' literal with the specified literal value.
 begin-user-doc 
 end-user-doc
Generated:
getByName
public static [AggregationKindEnum](AggregationKindEnum.html) getByName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Returns the '***Aggregation Kind***' literal with the specified name.
 begin-user-doc 
 end-user-doc
Generated:
get
public static [AggregationKindEnum](AggregationKindEnum.html) get(int value)
Returns the '***Aggregation Kind***' literal with the specified integer value.
 begin-user-doc 
 end-user-doc
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdkernel</a></div>
<h1 class="title" title="Class AggregationKindEnum">Class AggregationKindEnum</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.util.AbstractEnumerator
<div class="inheritance">com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKindEnum</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code>javax.jmi.reflect.RefEnum</code>, <code>org.eclipse.emf.common.util.Enumerator</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">AggregationKindEnum</span>
<span class="extends-implements">extends org.eclipse.emf.common.util.AbstractEnumerator
implements <a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the literals of the enumeration '<em><b>Aggregation Kind</b></em>',
 and utility methods for working with them.
 <!-- end-user-doc -->
<!-- begin-model-doc -->
 AggregationKind is an Enumeration for specifying the kind of aggregation of a Property.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getAggregationKindEnum()</code></li>
<li><a href="../../../../../../../serialized-form.html#com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKindEnum">Serialized Form</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='classes.mdkernel'"</dd>
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
<div class="col-first even-row-color"><code>static final <a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COMPOSITE">COMPOSITE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Composite</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COMPOSITE_VALUE">COMPOSITE_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Composite</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NONE">NONE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>None</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NONE_VALUE">NONE_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>None</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHARED">SHARED</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Shared</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHARED_VALUE">SHARED_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Shared</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUES">VALUES</a></code></div>
<div class="col-last even-row-color">
<div class="block">A public read-only list of all the '<em><b>Aggregation Kind</b></em>' enumerators.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="AggregationKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(int)">get</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Aggregation Kind</b></em>' literal with the specified integer value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="AggregationKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKindEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Aggregation Kind</b></em>' literal with the specified literal value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="AggregationKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getByName(java.lang.String)">getByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Aggregation Kind</b></em>' literal with the specified name.</div>
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
<section class="detail" id="NONE_VALUE">
<h3>NONE_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">NONE_VALUE</span></div>
<div class="block">The '<em><b>None</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates that the Property has no aggregation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#NONE"><code>NONE</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKindEnum.NONE_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="none"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHARED_VALUE">
<h3>SHARED_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SHARED_VALUE</span></div>
<div class="block">The '<em><b>Shared</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates that the Property has shared aggregation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SHARED"><code>SHARED</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKindEnum.SHARED_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="shared"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="COMPOSITE_VALUE">
<h3>COMPOSITE_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">COMPOSITE_VALUE</span></div>
<div class="block">The '<em><b>Composite</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates that the Property is aggregated compositely, i.e., the composite object has responsibility for the existence and storage of the composed objects
 (parts).
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#COMPOSITE"><code>COMPOSITE</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKindEnum.COMPOSITE_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="composite"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="NONE">
<h3>NONE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a></span> <span class="element-name">NONE</span></div>
<div class="block">The '<em><b>None</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#NONE_VALUE"><code>NONE_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHARED">
<h3>SHARED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a></span> <span class="element-name">SHARED</span></div>
<div class="block">The '<em><b>Shared</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SHARED_VALUE"><code>SHARED_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="COMPOSITE">
<h3>COMPOSITE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a></span> <span class="element-name">COMPOSITE</span></div>
<div class="block">The '<em><b>Composite</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#COMPOSITE_VALUE"><code>COMPOSITE_VALUE</code></a></li>
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
<div class="block">A public read-only list of all the '<em><b>Aggregation Kind</b></em>' enumerators.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="AggregationKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKindEnum</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</span></div>
<div class="block">Returns the '<em><b>Aggregation Kind</b></em>' literal with the specified literal value.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="AggregationKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKindEnum</a></span> <span class="element-name">getByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the '<em><b>Aggregation Kind</b></em>' literal with the specified name.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="AggregationKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKindEnum</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Returns the '<em><b>Aggregation Kind</b></em>' literal with the specified integer value.
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
