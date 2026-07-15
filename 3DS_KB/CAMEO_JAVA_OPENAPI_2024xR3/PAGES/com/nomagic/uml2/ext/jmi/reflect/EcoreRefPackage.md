# JAVA OPENAPI: EcoreRefPackage (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/jmi/reflect/EcoreRefPackage.html
- source_path: `com/nomagic/uml2/ext/jmi/reflect/EcoreRefPackage.html`
- source_sha256: `aaeeba1c5a57b1f6509776b90d233c3c5baab45d9b2aed184728859f29171498`
- captured_utc: `2026-07-14T16:56:16.196691+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.reflect](package-summary.html)

## Class EcoreRefPackage

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
[com.nomagic.uml2.ext.jmi.reflect.AbstractRefPackage](AbstractRefPackage.html)
com.nomagic.uml2.ext.jmi.reflect.EcoreRefPackage

All Implemented Interfaces:
`com.nomagic.uml2.ext.jmi.MapOwner`, `[AbstractRefBaseObject](AbstractRefBaseObject.html)`, `com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefPackage`

public classEcoreRefPackage
extends [AbstractRefPackage](AbstractRefPackage.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
`mMetaObject, repository`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[EcoreRefPackage](#%3Cinit%3E(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository,java.lang.String))([AbstractRepository](AbstractRepository.html) repository,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addEnum](#addEnum(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),javax.jmi.reflect.RefEnum> enumInfo)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`

`javax.jmi.reflect.RefEnum`
`[refGetEnum](#refGetEnum(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) enumName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) literal)`
The refGetEnum operation returns the instance of an enumeration (i.e., an
 enumeration literal) whose value is described by the value of literalName .
Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.[AbstractRefPackage](AbstractRefPackage.html)
`[addAssociation](AbstractRefPackage.html#addAssociation(java.lang.String,javax.jmi.reflect.RefAssociation)), [addClass](AbstractRefPackage.html#addClass(java.lang.String,javax.jmi.reflect.RefClass)), [addPackage](AbstractRefPackage.html#addPackage(java.lang.String,javax.jmi.reflect.RefBaseObject)), [getMetaObjects](AbstractRefPackage.html#getMetaObjects()), [internalError](AbstractRefPackage.html#internalError(java.lang.String,javax.jmi.reflect.InvalidCallException)), [refAllAssociations](AbstractRefPackage.html#refAllAssociations()), [refAllClasses](AbstractRefPackage.html#refAllClasses()), [refAllPackages](AbstractRefPackage.html#refAllPackages()), [refAssociation](AbstractRefPackage.html#refAssociation(java.lang.String)), [refAssociation](AbstractRefPackage.html#refAssociation(javax.jmi.reflect.RefObject)), [refClass](AbstractRefPackage.html#refClass(java.lang.String)), [refClass](AbstractRefPackage.html#refClass(javax.jmi.reflect.RefObject)), [refCreateStruct](AbstractRefPackage.html#refCreateStruct(java.lang.String,java.util.List)), [refCreateStruct](AbstractRefPackage.html#refCreateStruct(javax.jmi.reflect.RefObject,java.util.List)), [refDelete](AbstractRefPackage.html#refDelete()), [refGetEnum](AbstractRefPackage.html#refGetEnum(javax.jmi.reflect.RefObject,java.lang.String)), [refPackage](AbstractRefPackage.html#refPackage(java.lang.String)), [refPackage](AbstractRefPackage.html#refPackage(javax.jmi.reflect.RefObject)), [removeClass](AbstractRefPackage.html#removeClass(com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass)), [removePackage](AbstractRefPackage.html#removePackage(javax.jmi.reflect.RefBaseObject))`
Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
`getRepository, mapClear, mapPut, mapPutAll, mapRemove, mof_getRepository, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints, setMofID, setOwner, setRefMetaObject, setRepository`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
EcoreRefPackage
public EcoreRefPackage([AbstractRepository](AbstractRepository.html) repository,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
 ============ METHOD DETAIL ========== 
Method Details
getName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
addEnum
public void addEnum([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),javax.jmi.reflect.RefEnum> enumInfo)
refGetEnum
public javax.jmi.reflect.RefEnum refGetEnum([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) enumName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) literal)
Description copied from class: `[AbstractRefPackage](AbstractRefPackage.html#refGetEnum(java.lang.String,java.lang.String))`
The refGetEnum operation returns the instance of an enumeration (i.e., an
 enumeration literal) whose value is described by the value of literalName .
 Note that the type of enumeration is defined by the meta object that owns
 the metaLiteral object. InvalidCallException is raised if the enumType
 parameter does not designate a valid enumeration. InvalidNameException is
 raised when the enumName does not denote a valid enum name. This
 refGetEnum returns the enumeration object representing the enumeration
 literal. specific analog: none. return type: RefEnum parameters:
 RefObject enumType (or String enumName ) String literalName exceptions:
 JmiException (TypeMismatchException, InvalidCallException,
 InvalidNameException, java.lang.NullPointerException)
Specified by:
`refGetEnum` in interface `javax.jmi.reflect.RefPackage`
Overrides:
`[refGetEnum](AbstractRefPackage.html#refGetEnum(java.lang.String,java.lang.String))` in class `[AbstractRefPackage](AbstractRefPackage.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.reflect</a></div>
<h1 class="title" title="Class EcoreRefPackage">Class EcoreRefPackage</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
<div class="inheritance"><a href="AbstractRefPackage.html" title="class in com.nomagic.uml2.ext.jmi.reflect">com.nomagic.uml2.ext.jmi.reflect.AbstractRefPackage</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.reflect.EcoreRefPackage</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.uml2.ext.jmi.MapOwner</code>, <code><a href="AbstractRefBaseObject.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRefBaseObject</a></code>, <code>com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">EcoreRefPackage</span>
<span class="extends-implements">extends <a href="AbstractRefPackage.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRefPackage</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl">Fields inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl</h3>
<code>mMetaObject, repository</code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository,java.lang.String)">EcoreRefPackage</a><wbr/>(<a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> repository,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addEnum(java.util.Map)">addEnum</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>javax.jmi.reflect.RefEnum&gt; enumInfo)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>javax.jmi.reflect.RefEnum</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refGetEnum(java.lang.String,java.lang.String)">refGetEnum</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> enumName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The refGetEnum operation returns the instance of an enumeration (i.e., an
 enumeration literal) whose value is described by the value of literalName .</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.reflect.AbstractRefPackage">Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.<a href="AbstractRefPackage.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRefPackage</a></h3>
<code><a href="AbstractRefPackage.html#addAssociation(java.lang.String,javax.jmi.reflect.RefAssociation)">addAssociation</a>, <a href="AbstractRefPackage.html#addClass(java.lang.String,javax.jmi.reflect.RefClass)">addClass</a>, <a href="AbstractRefPackage.html#addPackage(java.lang.String,javax.jmi.reflect.RefBaseObject)">addPackage</a>, <a href="AbstractRefPackage.html#getMetaObjects()">getMetaObjects</a>, <a href="AbstractRefPackage.html#internalError(java.lang.String,javax.jmi.reflect.InvalidCallException)">internalError</a>, <a href="AbstractRefPackage.html#refAllAssociations()">refAllAssociations</a>, <a href="AbstractRefPackage.html#refAllClasses()">refAllClasses</a>, <a href="AbstractRefPackage.html#refAllPackages()">refAllPackages</a>, <a href="AbstractRefPackage.html#refAssociation(java.lang.String)">refAssociation</a>, <a href="AbstractRefPackage.html#refAssociation(javax.jmi.reflect.RefObject)">refAssociation</a>, <a href="AbstractRefPackage.html#refClass(java.lang.String)">refClass</a>, <a href="AbstractRefPackage.html#refClass(javax.jmi.reflect.RefObject)">refClass</a>, <a href="AbstractRefPackage.html#refCreateStruct(java.lang.String,java.util.List)">refCreateStruct</a>, <a href="AbstractRefPackage.html#refCreateStruct(javax.jmi.reflect.RefObject,java.util.List)">refCreateStruct</a>, <a href="AbstractRefPackage.html#refDelete()">refDelete</a>, <a href="AbstractRefPackage.html#refGetEnum(javax.jmi.reflect.RefObject,java.lang.String)">refGetEnum</a>, <a href="AbstractRefPackage.html#refPackage(java.lang.String)">refPackage</a>, <a href="AbstractRefPackage.html#refPackage(javax.jmi.reflect.RefObject)">refPackage</a>, <a href="AbstractRefPackage.html#removeClass(com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass)">removeClass</a>, <a href="AbstractRefPackage.html#removePackage(javax.jmi.reflect.RefBaseObject)">removePackage</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl">Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl</h3>
<code>getRepository, mapClear, mapPut, mapPutAll, mapRemove, mof_getRepository, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints, setMofID, setOwner, setRefMetaObject, setRepository</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefBaseObject">Methods inherited from interface javax.jmi.reflect.RefBaseObject</h3>
<code>equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints</code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository,java.lang.String)">
<h3>EcoreRefPackage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EcoreRefPackage</span><wbr/><span class="parameters">(<a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> repository,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addEnum(java.util.Map)">
<h3>addEnum</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addEnum</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>javax.jmi.reflect.RefEnum&gt; enumInfo)</span></div>
</section>
</li>
<li>
<section class="detail" id="refGetEnum(java.lang.String,java.lang.String)">
<h3>refGetEnum</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">javax.jmi.reflect.RefEnum</span> <span class="element-name">refGetEnum</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> enumName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literal)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractRefPackage.html#refGetEnum(java.lang.String,java.lang.String)">AbstractRefPackage</a></code></span></div>
<div class="block">The refGetEnum operation returns the instance of an enumeration (i.e., an
 enumeration literal) whose value is described by the value of literalName .
 Note that the type of enumeration is defined by the meta object that owns
 the metaLiteral object. InvalidCallException is raised if the enumType
 parameter does not designate a valid enumeration. InvalidNameException is
 raised when the enumName does not denote a valid enum name. This
 refGetEnum returns the enumeration object representing the enumeration
 literal. specific analog: none. return type: RefEnum parameters:
 RefObject enumType (or String enumName ) String literalName exceptions:
 JmiException (TypeMismatchException, InvalidCallException,
 InvalidNameException, java.lang.NullPointerException)</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refGetEnum</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
<dt>Overrides:</dt>
<dd><code><a href="AbstractRefPackage.html#refGetEnum(java.lang.String,java.lang.String)">refGetEnum</a></code> in class <code><a href="AbstractRefPackage.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRefPackage</a></code></dd>
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
