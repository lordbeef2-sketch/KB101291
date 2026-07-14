# JAVA OPENAPI: TypeMapProfile (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/modeltransformations/TypeMapProfile.html
- source_path: `com/nomagic/magicdraw/modeltransformations/TypeMapProfile.html`
- source_sha256: `8a79046cb0a1c55b47882a734bd1883987a1e96b37e6fdb439b091593eb2d257`
- captured_utc: `2026-07-14T16:55:25.940127+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.modeltransformations](package-summary.html)

## Class TypeMapProfile

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.modeltransformations.TypeMapProfile

@OpenApipublic classTypeMapProfile
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
TypeMapProfile - class for type mapping.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final com.nomagic.magicdraw.modeltransformations.TypeMapProfile.TypeModifier`
`[EMPTY_TYPE_MODIFIER](#EMPTY_TYPE_MODIFIER)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TypeMapProfile](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) mp)`
Constructor
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDocumentation](#getDocumentation())()`
Returns type map documentation
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getErrorMessage](#getErrorMessage())()`
Returns error message for broken type map
`com.nomagic.magicdraw.modeltransformations.TypeMapProfile.Type`
`[getMappedType](#getMappedType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original)`
Returns mapped type
`[TableModel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/table/TableModel.html)`
`[getTransformationTypeTableModel](#getTransformationTypeTableModel())()`
Returns transformation type table model
`[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)`
`[getTypeMapModelPackage](#getTypeMapModelPackage())()`
Returns model package of type map
`boolean`
`[isBroken](#isBroken())()`
Is type map broken
`boolean`
`[isDefault](#isDefault(com.nomagic.magicdraw.modeltransformations.TypeMapProfile.TypeMap))(com.nomagic.magicdraw.modeltransformations.TypeMapProfile.TypeMap typeMap)`

`boolean`
`[isForwardMapping](#isForwardMapping())()`
Is forward mapping set
`boolean`
`[isForwardMappingBroken](#isForwardMappingBroken())()`

`boolean`
`[isMappingValid](#isMappingValid(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mapped)`
Checks if type mapping is valid.
`boolean`
`[isReverseMappingBroken](#isReverseMappingBroken())()`

`void`
`[setForwardMapping](#setForwardMapping(boolean))(boolean forward)`
Sets forward mapping
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Returns type map name
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
EMPTY_TYPE_MODIFIER
public static final com.nomagic.magicdraw.modeltransformations.TypeMapProfile.TypeModifier EMPTY_TYPE_MODIFIER
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TypeMapProfile
public TypeMapProfile(@CheckForNull
 [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) mp)
Constructor
Parameters:
`mp` - profile package
 ============ METHOD DETAIL ========== 
Method Details
isDefault
public boolean isDefault(@CheckForNull
 com.nomagic.magicdraw.modeltransformations.TypeMapProfile.TypeMap typeMap)
getTransformationTypeTableModel
public [TableModel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/table/TableModel.html) getTransformationTypeTableModel()
Returns transformation type table model
Returns:
transformation type table model
getDocumentation
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDocumentation()
Returns type map documentation
Returns:
documentation
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Returns type map name
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
name
getTypeMapModelPackage
@CheckForNullpublic [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) getTypeMapModelPackage()
Returns model package of type map
Returns:
model package of type map
isForwardMapping
public boolean isForwardMapping()
Is forward mapping set
Returns:
true for forward mapping, false for reverse
isBroken
public boolean isBroken()
Is type map broken
Returns:
true if broken
isForwardMappingBroken
public boolean isForwardMappingBroken()
isReverseMappingBroken
public boolean isReverseMappingBroken()
getErrorMessage
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getErrorMessage()
Returns error message for broken type map
Returns:
error message
setForwardMapping
public void setForwardMapping(boolean forward)
Sets forward mapping
Parameters:
`forward` - true for forward mapping, false for reverse
getMappedType
public com.nomagic.magicdraw.modeltransformations.TypeMapProfile.Type getMappedType([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original)
Returns mapped type
Parameters:
`original` - original type, null for EmptySourceType/EmptyDestinationType
Returns:
mapped (default) type for original type. If there is no maping return original element. Return null for EmtyTypes.
isMappingValid
public boolean isMappingValid([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mapped)
Checks if type mapping is valid. This check should check generalizations/specifications.
Parameters:
`original` - original type
`mapped` - mapped type
Returns:
true if mapped type conforms to original type

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.modeltransformations</a></div>
<h1 class="title" title="Class TypeMapProfile">Class TypeMapProfile</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.modeltransformations.TypeMapProfile</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TypeMapProfile</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">TypeMapProfile - class for type mapping.</div>
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
<div class="col-first even-row-color"><code>static final com.nomagic.magicdraw.modeltransformations.TypeMapProfile.TypeModifier</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EMPTY_TYPE_MODIFIER">EMPTY_TYPE_MODIFIER</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">TypeMapProfile</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> mp)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocumentation()">getDocumentation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns type map documentation</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getErrorMessage()">getErrorMessage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns error message for broken type map</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.modeltransformations.TypeMapProfile.Type</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMappedType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getMappedType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns mapped type</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/table/TableModel.html" title="class or interface in javax.swing.table">TableModel</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransformationTypeTableModel()">getTransformationTypeTableModel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns transformation type table model</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeMapModelPackage()">getTypeMapModelPackage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model package of type map</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isBroken()">isBroken</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Is type map broken</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDefault(com.nomagic.magicdraw.modeltransformations.TypeMapProfile.TypeMap)">isDefault</a><wbr/>(com.nomagic.magicdraw.modeltransformations.TypeMapProfile.TypeMap typeMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isForwardMapping()">isForwardMapping</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Is forward mapping set</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isForwardMappingBroken()">isForwardMappingBroken</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMappingValid(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isMappingValid</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mapped)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if type mapping is valid.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isReverseMappingBroken()">isReverseMappingBroken</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setForwardMapping(boolean)">setForwardMapping</a><wbr/>(boolean forward)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets forward mapping</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns type map name</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="EMPTY_TYPE_MODIFIER">
<h3>EMPTY_TYPE_MODIFIER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">com.nomagic.magicdraw.modeltransformations.TypeMapProfile.TypeModifier</span> <span class="element-name">EMPTY_TYPE_MODIFIER</span></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>TypeMapProfile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TypeMapProfile</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> mp)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mp</code> - profile package</dd>
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
<section class="detail" id="isDefault(com.nomagic.magicdraw.modeltransformations.TypeMapProfile.TypeMap)">
<h3>isDefault</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDefault</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.magicdraw.modeltransformations.TypeMapProfile.TypeMap typeMap)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTransformationTypeTableModel()">
<h3>getTransformationTypeTableModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/table/TableModel.html" title="class or interface in javax.swing.table">TableModel</a></span> <span class="element-name">getTransformationTypeTableModel</span>()</div>
<div class="block">Returns transformation type table model</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>transformation type table model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDocumentation()">
<h3>getDocumentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDocumentation</span>()</div>
<div class="block">Returns type map documentation</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>documentation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Returns type map name</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypeMapModelPackage()">
<h3>getTypeMapModelPackage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">getTypeMapModelPackage</span>()</div>
<div class="block">Returns model package of type map</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>model package of type map</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isForwardMapping()">
<h3>isForwardMapping</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isForwardMapping</span>()</div>
<div class="block">Is forward mapping set</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true for forward mapping, false for reverse</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isBroken()">
<h3>isBroken</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBroken</span>()</div>
<div class="block">Is type map broken</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if broken</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isForwardMappingBroken()">
<h3>isForwardMappingBroken</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isForwardMappingBroken</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isReverseMappingBroken()">
<h3>isReverseMappingBroken</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isReverseMappingBroken</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getErrorMessage()">
<h3>getErrorMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getErrorMessage</span>()</div>
<div class="block">Returns error message for broken type map</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>error message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setForwardMapping(boolean)">
<h3>setForwardMapping</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setForwardMapping</span><wbr/><span class="parameters">(boolean forward)</span></div>
<div class="block">Sets forward mapping</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>forward</code> - true for forward mapping, false for reverse</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMappedType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getMappedType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.modeltransformations.TypeMapProfile.Type</span> <span class="element-name">getMappedType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original)</span></div>
<div class="block">Returns mapped type</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>original</code> - original type, null for EmptySourceType/EmptyDestinationType</dd>
<dt>Returns:</dt>
<dd>mapped (default) type for original type. If there is no maping return original element. Return null for EmtyTypes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMappingValid(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isMappingValid</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMappingValid</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mapped)</span></div>
<div class="block">Checks if type mapping is valid. This check should check generalizations/specifications.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>original</code> - original type</dd>
<dd><code>mapped</code> - mapped type</dd>
<dt>Returns:</dt>
<dd>true if mapped type conforms to original type</dd>
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
