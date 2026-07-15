# JAVA OPENAPI: TriggerKind (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/sysml/TriggerKind.html
- source_path: `com/dassault_systemes/modeler/sysml/model/sysml/TriggerKind.html`
- source_sha256: `6c50380323c6658fff85da7768b8a8a8d05dd55448f6341ba8ac9f3ebaf9cc72`
- captured_utc: `2026-07-14T16:45:05.113071+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model.sysml](package-summary.html)

## Class TriggerKind

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.util.AbstractEnumerator
com.dassault_systemes.modeler.sysml.model.sysml.TriggerKind

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `org.eclipse.emf.common.util.Enumerator`

@OpenApiAllpublic classTriggerKind
extends org.eclipse.emf.common.util.AbstractEnumerator

A representation of the literals of the enumeration '***Trigger Kind***',
 and utility methods for working with them.
 begin-model-doc 
`TriggerKind` enumerates the kinds of triggers that can be represented by a `TriggerInvocationExpression`.
 end-model-doc

See Also:
[`SysMLPackage.getTriggerKind()`](SysMLPackage.html#getTriggerKind())
[Serialized Form](../../../../../../serialized-form.html#com.dassault_systemes.modeler.sysml.model.sysml.TriggerKind)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [TriggerKind](TriggerKind.html)`
`[AFTER](#AFTER)`
The '***After***' literal object.
`static final int`
`[AFTER_VALUE](#AFTER_VALUE)`
The '***After***' literal value.
`static final [TriggerKind](TriggerKind.html)`
`[AT](#AT)`
The '***At***' literal object.
`static final int`
`[AT_VALUE](#AT_VALUE)`
The '***At***' literal value.
`static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[TriggerKind](TriggerKind.html)>`
`[VALUES](#VALUES)`
A public read-only list of all the '***Trigger Kind***' enumerators.
`static final [TriggerKind](TriggerKind.html)`
`[WHEN](#WHEN)`
The '***When***' literal object.
`static final int`
`[WHEN_VALUE](#WHEN_VALUE)`
The '***When***' literal value.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [TriggerKind](TriggerKind.html)`
`[get](#get(int))(int value)`
Returns the '***Trigger Kind***' literal with the specified integer value.
`static [TriggerKind](TriggerKind.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)`
Returns the '***Trigger Kind***' literal with the specified literal value.
`static [TriggerKind](TriggerKind.html)`
`[getByName](#getByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Returns the '***Trigger Kind***' literal with the specified name.
Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
`getLiteral, getName, getValue, toString, writeReplace`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
WHEN
public static final [TriggerKind](TriggerKind.html) WHEN
The '***When***' literal object.
 begin-model-doc 
Indicates a *change trigger*, corresponding to the *`TriggerWhen`* `Function` from the *`Triggers`* model in the Kernel Semantic Library.
 end-model-doc
See Also:
[`WHEN_VALUE`](#WHEN_VALUE)
AT
public static final [TriggerKind](TriggerKind.html) AT
The '***At***' literal object.
 begin-model-doc 
Indicates an *absolute time trigger*, corresponding to the *`TriggerAt`* `Function` from the *`Triggers`* model in the Kernel Semantic Library.
 end-model-doc
See Also:
[`AT_VALUE`](#AT_VALUE)
AFTER
public static final [TriggerKind](TriggerKind.html) AFTER
The '***After***' literal object.
 begin-model-doc 
Indicates a *relative time trigger*, corresponding to the *`TriggerAfter`* `Function` from the *`Triggers`* model in the `Kernel Semantic Library.`
 end-model-doc
See Also:
[`AFTER_VALUE`](#AFTER_VALUE)
WHEN_VALUE
public static final int WHEN_VALUE
The '***When***' literal value.
 begin-model-doc 
Indicates a *change trigger*, corresponding to the *`TriggerWhen`* `Function` from the *`Triggers`* model in the Kernel Semantic Library.
 end-model-doc
See Also:
[`WHEN`](#WHEN)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.TriggerKind.WHEN_VALUE)
AT_VALUE
public static final int AT_VALUE
The '***At***' literal value.
 begin-model-doc 
Indicates an *absolute time trigger*, corresponding to the *`TriggerAt`* `Function` from the *`Triggers`* model in the Kernel Semantic Library.
 end-model-doc
See Also:
[`AT`](#AT)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.TriggerKind.AT_VALUE)
AFTER_VALUE
public static final int AFTER_VALUE
The '***After***' literal value.
 begin-model-doc 
Indicates a *relative time trigger*, corresponding to the *`TriggerAfter`* `Function` from the *`Triggers`* model in the `Kernel Semantic Library.`
 end-model-doc
See Also:
[`AFTER`](#AFTER)
[Constant Field Values](../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.TriggerKind.AFTER_VALUE)
VALUES
public static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[TriggerKind](TriggerKind.html)> VALUES
A public read-only list of all the '***Trigger Kind***' enumerators.
 ============ METHOD DETAIL ========== 
Method Details
get
@CheckForNullpublic static [TriggerKind](TriggerKind.html) get([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)
Returns the '***Trigger Kind***' literal with the specified literal value.
Parameters:
`literal` - the literal.
Returns:
the matching enumerator or `null`.
getByName
@CheckForNullpublic static [TriggerKind](TriggerKind.html) getByName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Returns the '***Trigger Kind***' literal with the specified name.
Parameters:
`name` - the name.
Returns:
the matching enumerator or `null`.
get
@CheckForNullpublic static [TriggerKind](TriggerKind.html) get(int value)
Returns the '***Trigger Kind***' literal with the specified integer value.
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
<h1 class="title" title="Class TriggerKind">Class TriggerKind</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.util.AbstractEnumerator
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.sysml.TriggerKind</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code>org.eclipse.emf.common.util.Enumerator</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TriggerKind</span>
<span class="extends-implements">extends org.eclipse.emf.common.util.AbstractEnumerator</span></div>
<div class="block">A representation of the literals of the enumeration '<em><b>Trigger Kind</b></em>',
 and utility methods for working with them.
 <!-- begin-model-doc -->
<p><code>TriggerKind</code> enumerates the kinds of triggers that can be represented by a <code>TriggerInvocationExpression</code>.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="SysMLPackage.html#getTriggerKind()"><code>SysMLPackage.getTriggerKind()</code></a></li>
<li><a href="../../../../../../serialized-form.html#com.dassault_systemes.modeler.sysml.model.sysml.TriggerKind">Serialized Form</a></li>
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
<div class="col-first even-row-color"><code>static final <a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#AFTER">AFTER</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>After</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#AFTER_VALUE">AFTER_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>After</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#AT">AT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>At</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#AT_VALUE">AT_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>At</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUES">VALUES</a></code></div>
<div class="col-last even-row-color">
<div class="block">A public read-only list of all the '<em><b>Trigger Kind</b></em>' enumerators.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#WHEN">WHEN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>When</b></em>' literal object.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#WHEN_VALUE">WHEN_VALUE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>When</b></em>' literal value.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(int)">get</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Trigger Kind</b></em>' literal with the specified integer value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Trigger Kind</b></em>' literal with the specified literal value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getByName(java.lang.String)">getByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Trigger Kind</b></em>' literal with the specified name.</div>
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
<section class="detail" id="WHEN">
<h3>WHEN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></span> <span class="element-name">WHEN</span></div>
<div class="block">The '<em><b>When</b></em>' literal object.
 <!-- begin-model-doc -->
<p>Indicates a <em>change trigger</em>, corresponding to the <em><code>TriggerWhen</code></em> <code>Function</code> from the <em><code>Triggers</code></em> model in the Kernel Semantic Library.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#WHEN_VALUE"><code>WHEN_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AT">
<h3>AT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></span> <span class="element-name">AT</span></div>
<div class="block">The '<em><b>At</b></em>' literal object.
 <!-- begin-model-doc -->
<p>Indicates an <em>absolute time trigger</em>, corresponding to the <em><code>TriggerAt</code></em> <code>Function</code> from the <em><code>Triggers</code></em> model in the Kernel Semantic Library.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#AT_VALUE"><code>AT_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AFTER">
<h3>AFTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></span> <span class="element-name">AFTER</span></div>
<div class="block">The '<em><b>After</b></em>' literal object.
 <!-- begin-model-doc -->
<p>Indicates a <em>relative time trigger</em>, corresponding to the <em><code>TriggerAfter</code></em> <code>Function</code> from the <em><code>Triggers</code></em> model in the <code>Kernel Semantic Library.</code></p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#AFTER_VALUE"><code>AFTER_VALUE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="WHEN_VALUE">
<h3>WHEN_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">WHEN_VALUE</span></div>
<div class="block">The '<em><b>When</b></em>' literal value.
 <!-- begin-model-doc -->
<p>Indicates a <em>change trigger</em>, corresponding to the <em><code>TriggerWhen</code></em> <code>Function</code> from the <em><code>Triggers</code></em> model in the Kernel Semantic Library.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#WHEN"><code>WHEN</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.TriggerKind.WHEN_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AT_VALUE">
<h3>AT_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">AT_VALUE</span></div>
<div class="block">The '<em><b>At</b></em>' literal value.
 <!-- begin-model-doc -->
<p>Indicates an <em>absolute time trigger</em>, corresponding to the <em><code>TriggerAt</code></em> <code>Function</code> from the <em><code>Triggers</code></em> model in the Kernel Semantic Library.</p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#AT"><code>AT</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.TriggerKind.AT_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AFTER_VALUE">
<h3>AFTER_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">AFTER_VALUE</span></div>
<div class="block">The '<em><b>After</b></em>' literal value.
 <!-- begin-model-doc -->
<p>Indicates a <em>relative time trigger</em>, corresponding to the <em><code>TriggerAfter</code></em> <code>Function</code> from the <em><code>Triggers</code></em> model in the <code>Kernel Semantic Library.</code></p>
<!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#AFTER"><code>AFTER</code></a></li>
<li><a href="../../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.sysml.TriggerKind.AFTER_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALUES">
<h3>VALUES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a>&gt;</span> <span class="element-name">VALUES</span></div>
<div class="block">A public read-only list of all the '<em><b>Trigger Kind</b></em>' enumerators.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</span></div>
<div class="block">Returns the '<em><b>Trigger Kind</b></em>' literal with the specified literal value.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></span> <span class="element-name">getByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the '<em><b>Trigger Kind</b></em>' literal with the specified name.</div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Returns the '<em><b>Trigger Kind</b></em>' literal with the specified integer value.</div>
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
