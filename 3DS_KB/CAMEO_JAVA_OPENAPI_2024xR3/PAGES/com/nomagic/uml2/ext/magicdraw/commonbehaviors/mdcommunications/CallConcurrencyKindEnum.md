# JAVA OPENAPI: CallConcurrencyKindEnum (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/magicdraw/commonbehaviors/mdcommunications/CallConcurrencyKindEnum.html
- source_path: `com/nomagic/uml2/ext/magicdraw/commonbehaviors/mdcommunications/CallConcurrencyKindEnum.html`
- source_sha256: `64561f63610b11a15663bb81364a3249c4567752ed521a12aa9c890152565bda`
- captured_utc: `2026-07-14T16:56:23.251770+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications](package-summary.html)

## Class CallConcurrencyKindEnum

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.util.AbstractEnumerator
com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallConcurrencyKindEnum

All Implemented Interfaces:
`[CallConcurrencyKind](CallConcurrencyKind.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `javax.jmi.reflect.RefEnum`, `org.eclipse.emf.common.util.Enumerator`

public final classCallConcurrencyKindEnum
extends org.eclipse.emf.common.util.AbstractEnumerator
implements [CallConcurrencyKind](CallConcurrencyKind.html)

begin-user-doc 
 A representation of the literals of the enumeration '***Call Concurrency Kind***',
 and utility methods for working with them.
 end-user-doc 
 begin-model-doc 
 CallConcurrencyKind is an Enumeration used to specify the semantics of concurrent calls to a BehavioralFeature.
 end-model-doc

See Also:
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getCallConcurrencyKindEnum()`
[Serialized Form](../../../../../../../serialized-form.html#com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallConcurrencyKindEnum)
Model:
annotation="MOF package='commonbehaviors.mdcommunications'"
Generated:

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [CallConcurrencyKind](CallConcurrencyKind.html)`
`[CONCURRENT](#CONCURRENT)`
The '***Concurrent***' literal object.
`static final int`
`[CONCURRENT_VALUE](#CONCURRENT_VALUE)`
The '***Concurrent***' literal value.
`static final [CallConcurrencyKind](CallConcurrencyKind.html)`
`[GUARDED](#GUARDED)`
The '***Guarded***' literal object.
`static final int`
`[GUARDED_VALUE](#GUARDED_VALUE)`
The '***Guarded***' literal value.
`static final [CallConcurrencyKind](CallConcurrencyKind.html)`
`[SEQUENTIAL](#SEQUENTIAL)`
The '***Sequential***' literal object.
`static final int`
`[SEQUENTIAL_VALUE](#SEQUENTIAL_VALUE)`
The '***Sequential***' literal value.
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[VALUES](#VALUES)`
A public read-only list of all the '***Call Concurrency Kind***' enumerators.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [CallConcurrencyKindEnum](CallConcurrencyKindEnum.html)`
`[get](#get(int))(int value)`
Returns the '***Call Concurrency Kind***' literal with the specified integer value.
`static [CallConcurrencyKindEnum](CallConcurrencyKindEnum.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) literal)`
Returns the '***Call Concurrency Kind***' literal with the specified literal value.
`static [CallConcurrencyKindEnum](CallConcurrencyKindEnum.html)`
`[getByName](#getByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the '***Call Concurrency Kind***' literal with the specified name.
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
SEQUENTIAL_VALUE
public static final int SEQUENTIAL_VALUE
The '***Sequential***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 No concurrency management mechanism is associated with the BehavioralFeature and, therefore, concurrency conflicts may occur. Instances that invoke a
 BehavioralFeature need to coordinate so that only one invocation to a target on any BehavioralFeature occurs at once.
 end-model-doc
See Also:
[`SEQUENTIAL`](#SEQUENTIAL)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallConcurrencyKindEnum.SEQUENTIAL_VALUE)
Model:
name="sequential"
Generated:
GUARDED_VALUE
public static final int GUARDED_VALUE
The '***Guarded***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Multiple invocations of a BehavioralFeature that overlap in time may occur to one instance, but only one is allowed to commence. The others are blocked until the
 performance of the currently executing BehavioralFeature is complete. It is the responsibility of the system designer to ensure that deadlocks do not occur due
 to simultaneous blocking.
 end-model-doc
See Also:
[`GUARDED`](#GUARDED)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallConcurrencyKindEnum.GUARDED_VALUE)
Model:
name="guarded"
Generated:
CONCURRENT_VALUE
public static final int CONCURRENT_VALUE
The '***Concurrent***' literal value.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Multiple invocations of a BehavioralFeature that overlap in time may occur to one instance and all of them may proceed concurrently.
 end-model-doc
See Also:
[`CONCURRENT`](#CONCURRENT)
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallConcurrencyKindEnum.CONCURRENT_VALUE)
Model:
name="concurrent"
Generated:
SEQUENTIAL
public static final [CallConcurrencyKind](CallConcurrencyKind.html) SEQUENTIAL
The '***Sequential***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`SEQUENTIAL_VALUE`](#SEQUENTIAL_VALUE)
Generated:
GUARDED
public static final [CallConcurrencyKind](CallConcurrencyKind.html) GUARDED
The '***Guarded***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`GUARDED_VALUE`](#GUARDED_VALUE)
Generated:
CONCURRENT
public static final [CallConcurrencyKind](CallConcurrencyKind.html) CONCURRENT
The '***Concurrent***' literal object.
 begin-user-doc 
 end-user-doc
See Also:
[`CONCURRENT_VALUE`](#CONCURRENT_VALUE)
Generated:
VALUES
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) VALUES
A public read-only list of all the '***Call Concurrency Kind***' enumerators.
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
public static [CallConcurrencyKindEnum](CallConcurrencyKindEnum.html) get([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) literal)
Returns the '***Call Concurrency Kind***' literal with the specified literal value.
 begin-user-doc 
 end-user-doc
Generated:
getByName
public static [CallConcurrencyKindEnum](CallConcurrencyKindEnum.html) getByName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Returns the '***Call Concurrency Kind***' literal with the specified name.
 begin-user-doc 
 end-user-doc
Generated:
get
public static [CallConcurrencyKindEnum](CallConcurrencyKindEnum.html) get(int value)
Returns the '***Call Concurrency Kind***' literal with the specified integer value.
 begin-user-doc 
 end-user-doc
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications</a></div>
<h1 class="title" title="Class CallConcurrencyKindEnum">Class CallConcurrencyKindEnum</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.util.AbstractEnumerator
<div class="inheritance">com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallConcurrencyKindEnum</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="CallConcurrencyKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKind</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code>javax.jmi.reflect.RefEnum</code>, <code>org.eclipse.emf.common.util.Enumerator</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">CallConcurrencyKindEnum</span>
<span class="extends-implements">extends org.eclipse.emf.common.util.AbstractEnumerator
implements <a href="CallConcurrencyKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKind</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the literals of the enumeration '<em><b>Call Concurrency Kind</b></em>',
 and utility methods for working with them.
 <!-- end-user-doc -->
<!-- begin-model-doc -->
 CallConcurrencyKind is an Enumeration used to specify the semantics of concurrent calls to a BehavioralFeature.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getCallConcurrencyKindEnum()</code></li>
<li><a href="../../../../../../../serialized-form.html#com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallConcurrencyKindEnum">Serialized Form</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='commonbehaviors.mdcommunications'"</dd>
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
<div class="col-first even-row-color"><code>static final <a href="CallConcurrencyKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONCURRENT">CONCURRENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Concurrent</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONCURRENT_VALUE">CONCURRENT_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Concurrent</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="CallConcurrencyKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#GUARDED">GUARDED</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Guarded</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GUARDED_VALUE">GUARDED_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Guarded</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="CallConcurrencyKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKind</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SEQUENTIAL">SEQUENTIAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">The '<em><b>Sequential</b></em>' literal object.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SEQUENTIAL_VALUE">SEQUENTIAL_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The '<em><b>Sequential</b></em>' literal value.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUES">VALUES</a></code></div>
<div class="col-last even-row-color">
<div class="block">A public read-only list of all the '<em><b>Call Concurrency Kind</b></em>' enumerators.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="CallConcurrencyKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(int)">get</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Call Concurrency Kind</b></em>' literal with the specified integer value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="CallConcurrencyKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKindEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Call Concurrency Kind</b></em>' literal with the specified literal value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="CallConcurrencyKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getByName(java.lang.String)">getByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the '<em><b>Call Concurrency Kind</b></em>' literal with the specified name.</div>
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
<section class="detail" id="SEQUENTIAL_VALUE">
<h3>SEQUENTIAL_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SEQUENTIAL_VALUE</span></div>
<div class="block">The '<em><b>Sequential</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 No concurrency management mechanism is associated with the BehavioralFeature and, therefore, concurrency conflicts may occur. Instances that invoke a
 BehavioralFeature need to coordinate so that only one invocation to a target on any BehavioralFeature occurs at once.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SEQUENTIAL"><code>SEQUENTIAL</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallConcurrencyKindEnum.SEQUENTIAL_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="sequential"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="GUARDED_VALUE">
<h3>GUARDED_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">GUARDED_VALUE</span></div>
<div class="block">The '<em><b>Guarded</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Multiple invocations of a BehavioralFeature that overlap in time may occur to one instance, but only one is allowed to commence. The others are blocked until the
 performance of the currently executing BehavioralFeature is complete. It is the responsibility of the system designer to ensure that deadlocks do not occur due
 to simultaneous blocking.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#GUARDED"><code>GUARDED</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallConcurrencyKindEnum.GUARDED_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="guarded"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONCURRENT_VALUE">
<h3>CONCURRENT_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">CONCURRENT_VALUE</span></div>
<div class="block">The '<em><b>Concurrent</b></em>' literal value.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Multiple invocations of a BehavioralFeature that overlap in time may occur to one instance and all of them may proceed concurrently.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#CONCURRENT"><code>CONCURRENT</code></a></li>
<li><a href="../../../../../../../constant-values.html#com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallConcurrencyKindEnum.CONCURRENT_VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>name="concurrent"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="SEQUENTIAL">
<h3>SEQUENTIAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="CallConcurrencyKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKind</a></span> <span class="element-name">SEQUENTIAL</span></div>
<div class="block">The '<em><b>Sequential</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SEQUENTIAL_VALUE"><code>SEQUENTIAL_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="GUARDED">
<h3>GUARDED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="CallConcurrencyKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKind</a></span> <span class="element-name">GUARDED</span></div>
<div class="block">The '<em><b>Guarded</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#GUARDED_VALUE"><code>GUARDED_VALUE</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONCURRENT">
<h3>CONCURRENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="CallConcurrencyKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKind</a></span> <span class="element-name">CONCURRENT</span></div>
<div class="block">The '<em><b>Concurrent</b></em>' literal object.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#CONCURRENT_VALUE"><code>CONCURRENT_VALUE</code></a></li>
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
<div class="block">A public read-only list of all the '<em><b>Call Concurrency Kind</b></em>' enumerators.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="CallConcurrencyKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKindEnum</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</span></div>
<div class="block">Returns the '<em><b>Call Concurrency Kind</b></em>' literal with the specified literal value.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="CallConcurrencyKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKindEnum</a></span> <span class="element-name">getByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the '<em><b>Call Concurrency Kind</b></em>' literal with the specified name.
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="CallConcurrencyKindEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallConcurrencyKindEnum</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Returns the '<em><b>Call Concurrency Kind</b></em>' literal with the specified integer value.
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
