# JAVA OPENAPI: TransitionKindEnum (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/TransitionKindEnum.html
- source_path: `com/nomagic/uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/TransitionKindEnum.html`
- source_sha256: `4e32d019f82ee82e21c9fe72d595c4a8bf86d0872164a2be92679bb3ad236db6`
- captured_utc: `2026-07-14T16:58:57.673512+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines](package-summary.html)

## Class TransitionKindEnum

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.util.AbstractEnumerator
com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKindEnum

All Implemented Interfaces:
`[TransitionKind](TransitionKind.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `javax.jmi.reflect.RefEnum`, `org.eclipse.emf.common.util.Enumerator`

public final classTransitionKindEnum
extends org.eclipse.emf.common.util.AbstractEnumerator
implements [TransitionKind](TransitionKind.html)

begin-user-doc 
 A representation of the literals of the enumeration '***Transition Kind***',
 and utility methods for working with them.
 end-user-doc 
 begin-model-doc 
 TransitionKind is an Enumeration type used to differentiate the various kinds of Transitions.
 end-model-doc

See Also:
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getTransitionKindEnum()`
[Serialized Form](../../../../../../../serialized-form.html#com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKindEnum)
Model:
annotation="MOF package='statemachines.mdbehaviorstatemachines'"
Generated:

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [TransitionKind](TransitionKind.html)`
`[EXTERNAL](#EXTERNAL)`
The '***External***' literal object.
`static final int`
`[EXTERNAL_VALUE](#EXTERNAL_VALUE)`
The '***External***' literal value.
`static final [TransitionKind](TransitionKind.html)`
`[INTERNAL](#INTERNAL)`
The '***Internal***' literal object.
`static final int`
`[INTERNAL_VALUE](#INTERNAL_VALUE)`
The '***Internal***' literal value.
`static final [TransitionKind](TransitionKind.html)`
`[LOCAL](#LOCAL)`
The '***Local***' literal object.
`static final int`
`[LOCAL_VALUE](#LOCAL_VALUE)`
The '***Local***' literal value.
`static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)`
`[VALUES](#VALUES)`
A public read-only list of all the '***Transition Kind***' enumerators.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [TransitionKindEnum](TransitionKindEnum.html)`
`[get](#get(int))(int value)`
Returns the '***Transition Kind***' literal with the specified integer value.
`static [TransitionKindEnum](TransitionKindEnum.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)`
Returns the '***Transition Kind***' literal with the specified literal value.
`static [TransitionKindEnum](TransitionKindEnum.html)`
`[getByName](#getByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Returns the '***Transition Kind***' literal with the specified name.
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
INTERNAL_VALUE
public static final int INTERNAL_VALUE
The '***Internal***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Implies that the Transition, if triggered, occurs without exiting or entering the source State (i.e., it does not cause a state change). This means that the
 entry or exit condition of the source State will not be invoked. An internal Transition can be taken even if the SateMachine is in one or more Regions nested
 within the associated State.
 end-model-doc
See Also:
[`INTERNAL`](#INTERNAL)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKindEnum.INTERNAL_VALUE)
Model:
name="internal"
Generated:
LOCAL_VALUE
public static final int LOCAL_VALUE
The '***Local***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Implies that the Transition, if triggered, will not exit the composite (source) State, but it will exit and re-enter any state within the composite State that is
 in the current state configuration.
 end-model-doc
See Also:
[`LOCAL`](#LOCAL)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKindEnum.LOCAL_VALUE)
Model:
name="local"
Generated:
EXTERNAL_VALUE
public static final int EXTERNAL_VALUE
The '***External***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Implies that the Transition, if triggered, will exit the composite (source) State.
 end-model-doc
See Also:
[`EXTERNAL`](#EXTERNAL)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKindEnum.EXTERNAL_VALUE)
Model:
name="external"
Generated:
INTERNAL
public static final [TransitionKind](TransitionKind.html) INTERNAL
The '***Internal***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`INTERNAL_VALUE`](#INTERNAL_VALUE)
Generated:
LOCAL
public static final [TransitionKind](TransitionKind.html) LOCAL
The '***Local***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`LOCAL_VALUE`](#LOCAL_VALUE)
Generated:
EXTERNAL
public static final [TransitionKind](TransitionKind.html) EXTERNAL
The '***External***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`EXTERNAL_VALUE`](#EXTERNAL_VALUE)
Generated:
VALUES
public static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) VALUES
A public read-only list of all the '***Transition Kind***' enumerators.
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
public static [TransitionKindEnum](TransitionKindEnum.html) get([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) literal)
Returns the '***Transition Kind***' literal with the specified literal value.
 begin-user-doc 
 end-user-doc
Generated:
getByName
public static [TransitionKindEnum](TransitionKindEnum.html) getByName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Returns the '***Transition Kind***' literal with the specified name.
 begin-user-doc 
 end-user-doc
Generated:
get
public static [TransitionKindEnum](TransitionKindEnum.html) get(int value)
Returns the '***Transition Kind***' literal with the specified integer value.
 begin-user-doc 
 end-user-doc
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines</a></div>
<h1 class="title" title="Class TransitionKindEnum">Class TransitionKindEnum</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.util.AbstractEnumerator
<div class="inheritance">com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKindEnum</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKind</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code>javax.jmi.reflect.RefEnum</code>, <code>org.eclipse.emf.common.util.Enumerator</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">TransitionKindEnum</span>
<span class="extends-implements">extends org.eclipse.emf.common.util.AbstractEnumerator
implements <a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKind</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the literals of the enumeration '<em><b>Transition Kind</b></em>',
 and utility methods for working with them.
 <!-- end-user-doc -->
<!-- begin-model-doc -->
 TransitionKind is an Enumeration type used to differentiate the various kinds of Transitions.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getTransitionKindEnum()</code></pre>
</details>
</li>
<li><a href="../../../../../../../serialized-form.html#com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKindEnum">Serialized Form</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='statemachines.mdbehaviorstatemachines'"</dd>
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
<div class="col-first even-row-color"><code>static final <a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXTERNAL">EXTERNAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>External</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EXTERNAL_VALUE">EXTERNAL_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>External</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INTERNAL">INTERNAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Internal</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INTERNAL_VALUE">INTERNAL_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Internal</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOCAL">LOCAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Local</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOCAL_VALUE">LOCAL_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Local</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUES">VALUES</a></code></div>
<div class="col-last even-row-color">
<div class="block">A public read-only list of all the '<em><b>Transition Kind</b></em>' enumerators.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TransitionKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(int)">get</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Transition Kind</b></em>' literal with the specified integer value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TransitionKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKindEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Transition Kind</b></em>' literal with the specified literal value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TransitionKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getByName(java.lang.String)">getByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Transition Kind</b></em>' literal with the specified name.</div>
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
<section class="detail" id="INTERNAL_VALUE">
<h3>INTERNAL_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">INTERNAL_VALUE</span></div>
<div class="block">The '<em><b>Internal</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Implies that the Transition, if triggered, occurs without exiting or entering the source State (i.e., it does not cause a state change). This means that the
 entry or exit condition of the source State will not be invoked. An internal Transition can be taken even if the SateMachine is in one or more Regions nested
 within the associated State.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#INTERNAL"><code>INTERNAL</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKindEnum.INTERNAL_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="internal"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCAL_VALUE">
<h3>LOCAL_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">LOCAL_VALUE</span></div>
<div class="block">The '<em><b>Local</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Implies that the Transition, if triggered, will not exit the composite (source) State, but it will exit and re-enter any state within the composite State that is
 in the current state configuration.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#LOCAL"><code>LOCAL</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKindEnum.LOCAL_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="local"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXTERNAL_VALUE">
<h3>EXTERNAL_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">EXTERNAL_VALUE</span></div>
<div class="block">The '<em><b>External</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Implies that the Transition, if triggered, will exit the composite (source) State.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#EXTERNAL"><code>EXTERNAL</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKindEnum.EXTERNAL_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="external"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="INTERNAL">
<h3>INTERNAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKind</a></span> <span class="element-name">INTERNAL</span></div>
<div class="block">The '<em><b>Internal</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#INTERNAL_VALUE"><code>INTERNAL_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCAL">
<h3>LOCAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKind</a></span> <span class="element-name">LOCAL</span></div>
<div class="block">The '<em><b>Local</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#LOCAL_VALUE"><code>LOCAL_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXTERNAL">
<h3>EXTERNAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKind</a></span> <span class="element-name">EXTERNAL</span></div>
<div class="block">The '<em><b>External</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#EXTERNAL_VALUE"><code>EXTERNAL_VALUE</code></a></li>
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
<div class="block">A public read-only list of all the '<em><b>Transition Kind</b></em>' enumerators.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="TransitionKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKindEnum</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</span></div>
<div class="block">Returns the '<em><b>Transition Kind</b></em>' literal with the specified literal value.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="TransitionKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKindEnum</a></span> <span class="element-name">getByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the '<em><b>Transition Kind</b></em>' literal with the specified name.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="TransitionKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKindEnum</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Returns the '<em><b>Transition Kind</b></em>' literal with the specified integer value.
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
