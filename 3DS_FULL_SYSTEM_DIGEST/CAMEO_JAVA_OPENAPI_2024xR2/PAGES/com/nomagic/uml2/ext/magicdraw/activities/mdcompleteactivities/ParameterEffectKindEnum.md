# JAVA OPENAPI: ParameterEffectKindEnum (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/uml2/ext/magicdraw/activities/mdcompleteactivities/ParameterEffectKindEnum.html
- source_path: `com/nomagic/uml2/ext/magicdraw/activities/mdcompleteactivities/ParameterEffectKindEnum.html`
- source_sha256: `b79b35bb580cbf496701807f382d2df8e40b607f2e22e62eceb83979c7b3a2a2`
- captured_utc: `2026-07-14T16:56:13.399658+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities](package-summary.html)

## Class ParameterEffectKindEnum

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.util.AbstractEnumerator
com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKindEnum

All Implemented Interfaces:
`[ParameterEffectKind](ParameterEffectKind.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `javax.jmi.reflect.RefEnum`, `org.eclipse.emf.common.util.Enumerator`

public final classParameterEffectKindEnum
extends org.eclipse.emf.common.util.AbstractEnumerator
implements [ParameterEffectKind](ParameterEffectKind.html)

begin-user-doc 
 A representation of the literals of the enumeration '***Parameter Effect Kind***',
 and utility methods for working with them.
 end-user-doc 
 begin-model-doc 
 ParameterEffectKind is an Enumeration that indicates the effect of a Behavior on values passed in or out of its parameters.
 end-model-doc

See Also:
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getParameterEffectKindEnum()`
[Serialized Form](../../../../../../../serialized-form.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKindEnum)
Model:
annotation="MOF package='activities.mdcompleteactivities'"
Generated:

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [ParameterEffectKind](ParameterEffectKind.html)`
`[CREATE](#CREATE)`
The '***Create***' literal object.
`static final int`
`[CREATE_VALUE](#CREATE_VALUE)`
The '***Create***' literal value.
`static final [ParameterEffectKind](ParameterEffectKind.html)`
`[DELETE](#DELETE)`
The '***Delete***' literal object.
`static final int`
`[DELETE_VALUE](#DELETE_VALUE)`
The '***Delete***' literal value.
`static final [ParameterEffectKind](ParameterEffectKind.html)`
`[READ](#READ)`
The '***Read***' literal object.
`static final int`
`[READ_VALUE](#READ_VALUE)`
The '***Read***' literal value.
`static final [ParameterEffectKind](ParameterEffectKind.html)`
`[UPDATE](#UPDATE)`
The '***Update***' literal object.
`static final int`
`[UPDATE_VALUE](#UPDATE_VALUE)`
The '***Update***' literal value.
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[VALUES](#VALUES)`
A public read-only list of all the '***Parameter Effect Kind***' enumerators.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ParameterEffectKindEnum](ParameterEffectKindEnum.html)`
`[get](#get(int))(int value)`
Returns the '***Parameter Effect Kind***' literal with the specified integer value.
`static [ParameterEffectKindEnum](ParameterEffectKindEnum.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) literal)`
Returns the '***Parameter Effect Kind***' literal with the specified literal value.
`static [ParameterEffectKindEnum](ParameterEffectKindEnum.html)`
`[getByName](#getByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the '***Parameter Effect Kind***' literal with the specified name.
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
CREATE_VALUE
public static final int CREATE_VALUE
The '***Create***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates that the behavior creates values.
 end-model-doc
See Also:
[`CREATE`](#CREATE)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKindEnum.CREATE_VALUE)
Model:
name="create"
Generated:
READ_VALUE
public static final int READ_VALUE
The '***Read***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates objects that are values of the parameter have values of their properties, or links in which they participate, or their classifiers retrieved during
 executions of the behavior.
 end-model-doc
See Also:
[`READ`](#READ)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKindEnum.READ_VALUE)
Model:
name="read"
Generated:
UPDATE_VALUE
public static final int UPDATE_VALUE
The '***Update***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates objects that are values of the parameter have values of their properties, or links in which they participate, or their classification changed during
 executions of the behavior.
 end-model-doc
See Also:
[`UPDATE`](#UPDATE)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKindEnum.UPDATE_VALUE)
Model:
name="update"
Generated:
DELETE_VALUE
public static final int DELETE_VALUE
The '***Delete***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates objects that are values of the parameter do not exist after executions of the behavior are finished.
 end-model-doc
See Also:
[`DELETE`](#DELETE)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKindEnum.DELETE_VALUE)
Model:
name="delete"
Generated:
CREATE
public static final [ParameterEffectKind](ParameterEffectKind.html) CREATE
The '***Create***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`CREATE_VALUE`](#CREATE_VALUE)
Generated:
READ
public static final [ParameterEffectKind](ParameterEffectKind.html) READ
The '***Read***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`READ_VALUE`](#READ_VALUE)
Generated:
UPDATE
public static final [ParameterEffectKind](ParameterEffectKind.html) UPDATE
The '***Update***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`UPDATE_VALUE`](#UPDATE_VALUE)
Generated:
DELETE
public static final [ParameterEffectKind](ParameterEffectKind.html) DELETE
The '***Delete***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`DELETE_VALUE`](#DELETE_VALUE)
Generated:
VALUES
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) VALUES
A public read-only list of all the '***Parameter Effect Kind***' enumerators.
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
public static [ParameterEffectKindEnum](ParameterEffectKindEnum.html) get([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) literal)
Returns the '***Parameter Effect Kind***' literal with the specified literal value.
 begin-user-doc 
 end-user-doc
Generated:
getByName
public static [ParameterEffectKindEnum](ParameterEffectKindEnum.html) getByName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Returns the '***Parameter Effect Kind***' literal with the specified name.
 begin-user-doc 
 end-user-doc
Generated:
get
public static [ParameterEffectKindEnum](ParameterEffectKindEnum.html) get(int value)
Returns the '***Parameter Effect Kind***' literal with the specified integer value.
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
<h1 class="title" title="Class ParameterEffectKindEnum">Class ParameterEffectKindEnum</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.util.AbstractEnumerator
<div class="inheritance">com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKindEnum</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code>javax.jmi.reflect.RefEnum</code>, <code>org.eclipse.emf.common.util.Enumerator</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">ParameterEffectKindEnum</span>
<span class="extends-implements">extends org.eclipse.emf.common.util.AbstractEnumerator
implements <a href="ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the literals of the enumeration '<em><b>Parameter Effect Kind</b></em>',
 and utility methods for working with them.
 <!-- end-user-doc -->
<!-- begin-model-doc -->
 ParameterEffectKind is an Enumeration that indicates the effect of a Behavior on values passed in or out of its parameters.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getParameterEffectKindEnum()</code></li>
<li><a href="../../../../../../../serialized-form.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKindEnum">Serialized Form</a></li>
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
<div class="col-first even-row-color"><code>static final <a href="ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CREATE">CREATE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Create</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CREATE_VALUE">CREATE_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Create</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DELETE">DELETE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Delete</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DELETE_VALUE">DELETE_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Delete</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#READ">READ</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Read</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#READ_VALUE">READ_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Read</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#UPDATE">UPDATE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Update</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UPDATE_VALUE">UPDATE_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Update</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUES">VALUES</a></code></div>
<div class="col-last even-row-color">
<div class="block">A public read-only list of all the '<em><b>Parameter Effect Kind</b></em>' enumerators.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ParameterEffectKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(int)">get</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Parameter Effect Kind</b></em>' literal with the specified integer value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ParameterEffectKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKindEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Parameter Effect Kind</b></em>' literal with the specified literal value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ParameterEffectKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getByName(java.lang.String)">getByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Parameter Effect Kind</b></em>' literal with the specified name.</div>
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
<section class="detail" id="CREATE_VALUE">
<h3>CREATE_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">CREATE_VALUE</span></div>
<div class="block">The '<em><b>Create</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates that the behavior creates values.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#CREATE"><code>CREATE</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKindEnum.CREATE_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="create"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="READ_VALUE">
<h3>READ_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">READ_VALUE</span></div>
<div class="block">The '<em><b>Read</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates objects that are values of the parameter have values of their properties, or links in which they participate, or their classifiers retrieved during
 executions of the behavior.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#READ"><code>READ</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKindEnum.READ_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="read"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="UPDATE_VALUE">
<h3>UPDATE_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">UPDATE_VALUE</span></div>
<div class="block">The '<em><b>Update</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates objects that are values of the parameter have values of their properties, or links in which they participate, or their classification changed during
 executions of the behavior.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#UPDATE"><code>UPDATE</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKindEnum.UPDATE_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="update"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="DELETE_VALUE">
<h3>DELETE_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DELETE_VALUE</span></div>
<div class="block">The '<em><b>Delete</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates objects that are values of the parameter do not exist after executions of the behavior are finished.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#DELETE"><code>DELETE</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKindEnum.DELETE_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="delete"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="CREATE">
<h3>CREATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a></span> <span class="element-name">CREATE</span></div>
<div class="block">The '<em><b>Create</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#CREATE_VALUE"><code>CREATE_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="READ">
<h3>READ</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a></span> <span class="element-name">READ</span></div>
<div class="block">The '<em><b>Read</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#READ_VALUE"><code>READ_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="UPDATE">
<h3>UPDATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a></span> <span class="element-name">UPDATE</span></div>
<div class="block">The '<em><b>Update</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#UPDATE_VALUE"><code>UPDATE_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="DELETE">
<h3>DELETE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a></span> <span class="element-name">DELETE</span></div>
<div class="block">The '<em><b>Delete</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#DELETE_VALUE"><code>DELETE_VALUE</code></a></li>
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
<div class="block">A public read-only list of all the '<em><b>Parameter Effect Kind</b></em>' enumerators.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ParameterEffectKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKindEnum</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</span></div>
<div class="block">Returns the '<em><b>Parameter Effect Kind</b></em>' literal with the specified literal value.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ParameterEffectKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKindEnum</a></span> <span class="element-name">getByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the '<em><b>Parameter Effect Kind</b></em>' literal with the specified name.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ParameterEffectKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKindEnum</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Returns the '<em><b>Parameter Effect Kind</b></em>' literal with the specified integer value.
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
