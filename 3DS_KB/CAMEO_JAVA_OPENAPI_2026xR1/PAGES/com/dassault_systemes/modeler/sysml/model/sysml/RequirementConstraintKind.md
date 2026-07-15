# JAVA OPENAPI: RequirementConstraintKind (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/sysml/RequirementConstraintKind.html
- source_path: `com/dassault_systemes/modeler/sysml/model/sysml/RequirementConstraintKind.html`
- source_sha256: `4a5d70287da16b3c6dcd4bc03de4a1ff183e6248af365b2d292729f47c99bebf`
- captured_utc: `2026-07-14T16:45:04.592065+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model.sysml](package-summary.html)

## Class RequirementConstraintKind

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.util.AbstractEnumerator
com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintKind

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `org.eclipse.emf.common.util.Enumerator`

@OpenApiAllpublic classRequirementConstraintKind
extends org.eclipse.emf.common.util.AbstractEnumerator

A representation of the literals of the enumeration '***Requirement Constraint Kind***',
 and utility methods for working with them.
 begin-model-doc 
A `RequirementConstraintKind` indicates whether a `ConstraintUsage` is an assumption or a requirement in a `RequirementDefinition` or `RequirementUsage`.
 end-model-doc

See Also:
[`SysMLPackage.getRequirementConstraintKind()`](SysMLPackage.html#getRequirementConstraintKind())
[Serialized Form](../../../../../../serialized-form.html#com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintKind)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [RequirementConstraintKind](RequirementConstraintKind.html)`
`[ASSUMPTION](#ASSUMPTION)`
The '***Assumption***' literal object.
`static final int`
`[ASSUMPTION_VALUE](#ASSUMPTION_VALUE)`
The '***Assumption***' literal value.
`static final [RequirementConstraintKind](RequirementConstraintKind.html)`
`[REQUIREMENT](#REQUIREMENT)`
The '***Requirement***' literal object.
`static final int`
`[REQUIREMENT_VALUE](#REQUIREMENT_VALUE)`
The '***Requirement***' literal value.
`static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RequirementConstraintKind](RequirementConstraintKind.html)>`
`[VALUES](#VALUES)`
A public read-only list of all the '***Requirement Constraint Kind***' enumerators.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [RequirementConstraintKind](RequirementConstraintKind.html)`
`[get](#get(int))(int value)`
Returns the '***Requirement Constraint Kind***' literal with the specified integer value.
`static [RequirementConstraintKind](RequirementConstraintKind.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)`
Returns the '***Requirement Constraint Kind***' literal with the specified literal value.
`static [RequirementConstraintKind](RequirementConstraintKind.html)`
`[getByName](#getByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Returns the '***Requirement Constraint Kind***' literal with the specified name.
Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
`getLiteral, getName, getValue, toString, writeReplace`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ASSUMPTION
public static final [RequirementConstraintKind](RequirementConstraintKind.html) ASSUMPTION
The '***Assumption***' literal object.
 begin-model-doc 
Indicates that a member `ConstraintUsage` of a `RequirementDefinition` or `RequirementUsage` represents an assumption.
 end-model-doc
See Also:
[`ASSUMPTION_VALUE`](#ASSUMPTION_VALUE)
REQUIREMENT
public static final [RequirementConstraintKind](RequirementConstraintKind.html) REQUIREMENT
The '***Requirement***' literal object.
 begin-model-doc 
Indicates that a member `ConstraintUsage` of a `RequirementDefinition` or `RequirementUsage`represents an requirement.
 end-model-doc
See Also:
[`REQUIREMENT_VALUE`](#REQUIREMENT_VALUE)
ASSUMPTION_VALUE
public static final int ASSUMPTION_VALUE
The '***Assumption***' literal value.
 begin-model-doc 
Indicates that a member `ConstraintUsage` of a `RequirementDefinition` or `RequirementUsage` represents an assumption.
 end-model-doc
See Also:
[`ASSUMPTION`](#ASSUMPTION)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintKind.ASSUMPTION_VALUE)
REQUIREMENT_VALUE
public static final int REQUIREMENT_VALUE
The '***Requirement***' literal value.
 begin-model-doc 
Indicates that a member `ConstraintUsage` of a `RequirementDefinition` or `RequirementUsage`represents an requirement.
 end-model-doc
See Also:
[`REQUIREMENT`](#REQUIREMENT)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintKind.REQUIREMENT_VALUE)
VALUES
public static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RequirementConstraintKind](RequirementConstraintKind.html)> VALUES
A public read-only list of all the '***Requirement Constraint Kind***' enumerators.
 ============ METHOD DETAIL ========== 
Method Details
get
@CheckForNullpublic static [RequirementConstraintKind](RequirementConstraintKind.html) get([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)
Returns the '***Requirement Constraint Kind***' literal with the specified literal value.
Parameters:
`literal` - the literal.
Returns:
the matching enumerator or `null`.
getByName
@CheckForNullpublic static [RequirementConstraintKind](RequirementConstraintKind.html) getByName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Returns the '***Requirement Constraint Kind***' literal with the specified name.
Parameters:
`name` - the name.
Returns:
the matching enumerator or `null`.
get
@CheckForNullpublic static [RequirementConstraintKind](RequirementConstraintKind.html) get(int value)
Returns the '***Requirement Constraint Kind***' literal with the specified integer value.
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
<h1 class="title" title="Class RequirementConstraintKind">Class RequirementConstraintKind</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.util.AbstractEnumerator
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintKind</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code>org.eclipse.emf.common.util.Enumerator</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">RequirementConstraintKind</span>
<span class="extends-implements">extends org.eclipse.emf.common.util.AbstractEnumerator</span></div>
<div class="block">A representation of the literals of the enumeration '<em><b>Requirement Constraint Kind</b></em>',
 and utility methods for working with them.
 <!-- begin-model-doc -->
<p>A <code>RequirementConstraintKind</code> indicates whether a <code>ConstraintUsage</code> is an assumption or a requirement in a <code>RequirementDefinition</code> or <code>RequirementUsage</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="SysMLPackage.html#getRequirementConstraintKind()"><code>SysMLPackage.getRequirementConstraintKind()</code></a></li>
<li><a href="../../../../../../serialized-form.html#com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintKind">Serialized Form</a></li>
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
<div class="col-first even-row-color"><code>static final <a href="RequirementConstraintKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ASSUMPTION">ASSUMPTION</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Assumption</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ASSUMPTION_VALUE">ASSUMPTION_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Assumption</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="RequirementConstraintKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REQUIREMENT">REQUIREMENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Requirement</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REQUIREMENT_VALUE">REQUIREMENT_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Requirement</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="RequirementConstraintKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintKind</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUES">VALUES</a></code></div>
<div class="col-last even-row-color">
<div class="block">A public read-only list of all the '<em><b>Requirement Constraint Kind</b></em>' enumerators.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="RequirementConstraintKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(int)">get</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Requirement Constraint Kind</b></em>' literal with the specified integer value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="RequirementConstraintKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Requirement Constraint Kind</b></em>' literal with the specified literal value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="RequirementConstraintKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getByName(java.lang.String)">getByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Requirement Constraint Kind</b></em>' literal with the specified name.</div>
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
<section class="detail" id="ASSUMPTION">
<h3>ASSUMPTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="RequirementConstraintKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintKind</a></span> <span class="element-name">ASSUMPTION</span></div>
<div class="block">The '<em><b>Assumption</b></em>' literal object.
 <!-- begin-model-doc -->
<p>Indicates that a member <code>ConstraintUsage</code> of a <code>RequirementDefinition</code> or <code>RequirementUsage</code> represents an assumption.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#ASSUMPTION_VALUE"><code>ASSUMPTION_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENT">
<h3>REQUIREMENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="RequirementConstraintKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintKind</a></span> <span class="element-name">REQUIREMENT</span></div>
<div class="block">The '<em><b>Requirement</b></em>' literal object.
 <!-- begin-model-doc -->
<p>Indicates that a member <code>ConstraintUsage</code> of a <code>RequirementDefinition</code> or <code>RequirementUsage</code>represents an requirement.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#REQUIREMENT_VALUE"><code>REQUIREMENT_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ASSUMPTION_VALUE">
<h3>ASSUMPTION_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ASSUMPTION_VALUE</span></div>
<div class="block">The '<em><b>Assumption</b></em>' literal value.
 <!-- begin-model-doc -->
<p>Indicates that a member <code>ConstraintUsage</code> of a <code>RequirementDefinition</code> or <code>RequirementUsage</code> represents an assumption.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#ASSUMPTION"><code>ASSUMPTION</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintKind.ASSUMPTION_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENT_VALUE">
<h3>REQUIREMENT_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">REQUIREMENT_VALUE</span></div>
<div class="block">The '<em><b>Requirement</b></em>' literal value.
 <!-- begin-model-doc -->
<p>Indicates that a member <code>ConstraintUsage</code> of a <code>RequirementDefinition</code> or <code>RequirementUsage</code>represents an requirement.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#REQUIREMENT"><code>REQUIREMENT</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintKind.REQUIREMENT_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALUES">
<h3>VALUES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RequirementConstraintKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintKind</a>&gt;</span> <span class="element-name">VALUES</span></div>
<div class="block">A public read-only list of all the '<em><b>Requirement Constraint Kind</b></em>' enumerators.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="RequirementConstraintKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintKind</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</span></div>
<div class="block">Returns the '<em><b>Requirement Constraint Kind</b></em>' literal with the specified literal value.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="RequirementConstraintKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintKind</a></span> <span class="element-name">getByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the '<em><b>Requirement Constraint Kind</b></em>' literal with the specified name.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="RequirementConstraintKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintKind</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Returns the '<em><b>Requirement Constraint Kind</b></em>' literal with the specified integer value.</div>
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
