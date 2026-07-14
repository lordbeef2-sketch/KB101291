# JAVA OPENAPI: VisibilityKind (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/VisibilityKind.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/VisibilityKind.html`
- source_sha256: `e209cf8690c9d1e398428107477804d0e3f56a9843bfda7121ff2320b0ed2032`
- captured_utc: `2026-07-14T16:44:50.879882+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Class VisibilityKind

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.util.AbstractEnumerator
com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `org.eclipse.emf.common.util.Enumerator`

@OpenApiAllpublic classVisibilityKind
extends org.eclipse.emf.common.util.AbstractEnumerator

A representation of the literals of the enumeration '***Visibility Kind***',
 and utility methods for working with them.
 begin-model-doc 
`VisibilityKind` is an enumeration whose literals specify the visibility of a `Membership` of an `Element` in a `Namespace` outside of that `Namespace`. Note that "visibility" specifically restricts whether an `Element` in a `Namespace` may be referenced by name from outside the `Namespace` and only otherwise restricts access to an `Element` as provided by specific constraints in the abstract syntax (e.g., preventing the import or inheritance of private `Elements`).
 end-model-doc

See Also:
[`KerMLPackage.getVisibilityKind()`](KerMLPackage.html#getVisibilityKind())
[Serialized Form](../../../../../../serialized-form.html#com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [VisibilityKind](VisibilityKind.html)`
`[PRIVATE](#PRIVATE)`
The '***Private***' literal object.
`static final int`
`[PRIVATE_VALUE](#PRIVATE_VALUE)`
The '***Private***' literal value.
`static final [VisibilityKind](VisibilityKind.html)`
`[PROTECTED](#PROTECTED)`
The '***Protected***' literal object.
`static final int`
`[PROTECTED_VALUE](#PROTECTED_VALUE)`
The '***Protected***' literal value.
`static final [VisibilityKind](VisibilityKind.html)`
`[PUBLIC](#PUBLIC)`
The '***Public***' literal object.
`static final int`
`[PUBLIC_VALUE](#PUBLIC_VALUE)`
The '***Public***' literal value.
`static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[VisibilityKind](VisibilityKind.html)>`
`[VALUES](#VALUES)`
A public read-only list of all the '***Visibility Kind***' enumerators.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [VisibilityKind](VisibilityKind.html)`
`[get](#get(int))(int value)`
Returns the '***Visibility Kind***' literal with the specified integer value.
`static [VisibilityKind](VisibilityKind.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)`
Returns the '***Visibility Kind***' literal with the specified literal value.
`static [VisibilityKind](VisibilityKind.html)`
`[getByName](#getByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Returns the '***Visibility Kind***' literal with the specified name.
Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
`getLiteral, getName, getValue, toString, writeReplace`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
PRIVATE
public static final [VisibilityKind](VisibilityKind.html) PRIVATE
The '***Private***' literal object.
 begin-model-doc 
Indicates a `Membership` is not visible outside its owning `Namespace`.
 end-model-doc
See Also:
[`PRIVATE_VALUE`](#PRIVATE_VALUE)
PROTECTED
public static final [VisibilityKind](VisibilityKind.html) PROTECTED
The '***Protected***' literal object.
 begin-model-doc 
An intermediate level of visibility between `public` and `private`. By default, it is equivalent to `private` for the purposes of normal access to and import of `Elements` from a `Namespace`. However, other `Relationships` may be specified to include `Memberships` with `protected` visibility in the list of `memberships` for a `Namespace` (e.g., `Specialization`).
 end-model-doc
See Also:
[`PROTECTED_VALUE`](#PROTECTED_VALUE)
PUBLIC
public static final [VisibilityKind](VisibilityKind.html) PUBLIC
The '***Public***' literal object.
 begin-model-doc 
Indicates that a `Membership` is publicly visible outside its owning `Namespace`.
 end-model-doc
See Also:
[`PUBLIC_VALUE`](#PUBLIC_VALUE)
PRIVATE_VALUE
public static final int PRIVATE_VALUE
The '***Private***' literal value.
 begin-model-doc 
Indicates a `Membership` is not visible outside its owning `Namespace`.
 end-model-doc
See Also:
[`PRIVATE`](#PRIVATE)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind.PRIVATE_VALUE)
PROTECTED_VALUE
public static final int PROTECTED_VALUE
The '***Protected***' literal value.
 begin-model-doc 
An intermediate level of visibility between `public` and `private`. By default, it is equivalent to `private` for the purposes of normal access to and import of `Elements` from a `Namespace`. However, other `Relationships` may be specified to include `Memberships` with `protected` visibility in the list of `memberships` for a `Namespace` (e.g., `Specialization`).
 end-model-doc
See Also:
[`PROTECTED`](#PROTECTED)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind.PROTECTED_VALUE)
PUBLIC_VALUE
public static final int PUBLIC_VALUE
The '***Public***' literal value.
 begin-model-doc 
Indicates that a `Membership` is publicly visible outside its owning `Namespace`.
 end-model-doc
See Also:
[`PUBLIC`](#PUBLIC)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind.PUBLIC_VALUE)
VALUES
public static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[VisibilityKind](VisibilityKind.html)> VALUES
A public read-only list of all the '***Visibility Kind***' enumerators.
 ============ METHOD DETAIL ========== 
Method Details
get
@CheckForNullpublic static [VisibilityKind](VisibilityKind.html) get([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)
Returns the '***Visibility Kind***' literal with the specified literal value.
Parameters:
`literal` - the literal.
Returns:
the matching enumerator or `null`.
getByName
@CheckForNullpublic static [VisibilityKind](VisibilityKind.html) getByName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Returns the '***Visibility Kind***' literal with the specified name.
Parameters:
`name` - the name.
Returns:
the matching enumerator or `null`.
get
@CheckForNullpublic static [VisibilityKind](VisibilityKind.html) get(int value)
Returns the '***Visibility Kind***' literal with the specified integer value.
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
<h1 class="title" title="Class VisibilityKind">Class VisibilityKind</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.util.AbstractEnumerator
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code>org.eclipse.emf.common.util.Enumerator</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">VisibilityKind</span>
<span class="extends-implements">extends org.eclipse.emf.common.util.AbstractEnumerator</span></div>
<div class="block">A representation of the literals of the enumeration '<em><b>Visibility Kind</b></em>',
 and utility methods for working with them.
 <!-- begin-model-doc -->
<p><code>VisibilityKind</code> is an enumeration whose literals specify the visibility of a <code>Membership</code> of an <code>Element</code> in a <code>Namespace</code> outside of that <code>Namespace</code>. Note that "visibility" specifically restricts whether an <code>Element</code> in a <code>Namespace</code> may be referenced by name from outside the <code>Namespace</code> and only otherwise restricts access to an <code>Element</code> as provided by specific constraints in the abstract syntax (e.g., preventing the import or inheritance of private <code>Elements</code>).</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="KerMLPackage.html#getVisibilityKind()"><code>KerMLPackage.getVisibilityKind()</code></a></li>
<li><a href="../../../../../../serialized-form.html#com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind">Serialized Form</a></li>
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
<div class="col-first even-row-color"><code>static final <a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PRIVATE">PRIVATE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Private</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PRIVATE_VALUE">PRIVATE_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Private</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROTECTED">PROTECTED</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Protected</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROTECTED_VALUE">PROTECTED_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Protected</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PUBLIC">PUBLIC</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Public</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PUBLIC_VALUE">PUBLIC_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Public</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUES">VALUES</a></code></div>
<div class="col-last even-row-color">
<div class="block">A public read-only list of all the '<em><b>Visibility Kind</b></em>' enumerators.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(int)">get</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Visibility Kind</b></em>' literal with the specified integer value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Visibility Kind</b></em>' literal with the specified literal value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getByName(java.lang.String)">getByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Visibility Kind</b></em>' literal with the specified name.</div>
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
<section class="detail" id="PRIVATE">
<h3>PRIVATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></span> <span class="element-name">PRIVATE</span></div>
<div class="block">The '<em><b>Private</b></em>' literal object.
 <!-- begin-model-doc -->
<p>Indicates a <code>Membership</code> is not visible outside its owning <code>Namespace</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#PRIVATE_VALUE"><code>PRIVATE_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROTECTED">
<h3>PROTECTED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></span> <span class="element-name">PROTECTED</span></div>
<div class="block">The '<em><b>Protected</b></em>' literal object.
 <!-- begin-model-doc -->
<p>An intermediate level of visibility between <code>public</code> and <code>private</code>. By default, it is equivalent to <code>private</code> for the purposes of normal access to and import of <code>Elements</code> from a <code>Namespace</code>. However, other <code>Relationships</code> may be specified to include <code>Memberships</code> with <code>protected</code> visibility in the list of <code>memberships</code> for a <code>Namespace</code> (e.g., <code>Specialization</code>).</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#PROTECTED_VALUE"><code>PROTECTED_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PUBLIC">
<h3>PUBLIC</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></span> <span class="element-name">PUBLIC</span></div>
<div class="block">The '<em><b>Public</b></em>' literal object.
 <!-- begin-model-doc -->
<p>Indicates that a <code>Membership</code> is publicly visible outside its owning <code>Namespace</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#PUBLIC_VALUE"><code>PUBLIC_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PRIVATE_VALUE">
<h3>PRIVATE_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">PRIVATE_VALUE</span></div>
<div class="block">The '<em><b>Private</b></em>' literal value.
 <!-- begin-model-doc -->
<p>Indicates a <code>Membership</code> is not visible outside its owning <code>Namespace</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#PRIVATE"><code>PRIVATE</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind.PRIVATE_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROTECTED_VALUE">
<h3>PROTECTED_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">PROTECTED_VALUE</span></div>
<div class="block">The '<em><b>Protected</b></em>' literal value.
 <!-- begin-model-doc -->
<p>An intermediate level of visibility between <code>public</code> and <code>private</code>. By default, it is equivalent to <code>private</code> for the purposes of normal access to and import of <code>Elements</code> from a <code>Namespace</code>. However, other <code>Relationships</code> may be specified to include <code>Memberships</code> with <code>protected</code> visibility in the list of <code>memberships</code> for a <code>Namespace</code> (e.g., <code>Specialization</code>).</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#PROTECTED"><code>PROTECTED</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind.PROTECTED_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PUBLIC_VALUE">
<h3>PUBLIC_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">PUBLIC_VALUE</span></div>
<div class="block">The '<em><b>Public</b></em>' literal value.
 <!-- begin-model-doc -->
<p>Indicates that a <code>Membership</code> is publicly visible outside its owning <code>Namespace</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#PUBLIC"><code>PUBLIC</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind.PUBLIC_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALUES">
<h3>VALUES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a>&gt;</span> <span class="element-name">VALUES</span></div>
<div class="block">A public read-only list of all the '<em><b>Visibility Kind</b></em>' enumerators.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</span></div>
<div class="block">Returns the '<em><b>Visibility Kind</b></em>' literal with the specified literal value.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></span> <span class="element-name">getByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the '<em><b>Visibility Kind</b></em>' literal with the specified name.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Returns the '<em><b>Visibility Kind</b></em>' literal with the specified integer value.</div>
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
