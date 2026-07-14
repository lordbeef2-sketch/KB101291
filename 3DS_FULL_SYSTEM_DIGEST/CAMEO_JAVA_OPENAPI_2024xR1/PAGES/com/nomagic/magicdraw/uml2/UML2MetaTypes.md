# JAVA OPENAPI: UML2MetaTypes (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml2/UML2MetaTypes.html
- source_path: `com/nomagic/magicdraw/uml2/UML2MetaTypes.html`
- source_sha256: `0a1ce50bc694a9137fcca256d52bc268104328f201edeb77937961dc631288e9`
- captured_utc: `2026-07-14T16:52:16.436938+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2](package-summary.html)

## Class UML2MetaTypes

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml2.UML2MetaTypes

public classUML2MetaTypes
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static interface`
`[UML2MetaTypes.CachedResolver](UML2MetaTypes.CachedResolver.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UML2METAMODEL_NAME](#UML2METAMODEL_NAME)`
Name of UML2 metamodel
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UML2METAMODEL_PRIMITIVE_TYPES](#UML2METAMODEL_PRIMITIVE_TYPES)`
Name of primitives package in the UML2 metamodel
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UML2METAMODEL_URI](#UML2METAMODEL_URI)`
URI of UML2 metamodel, must correspond UML standard profile metamodel uri.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[UML2MetaTypes](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static <V> V`
`[callWithoutCachedResolver](#callWithoutCachedResolver(java.util.concurrent.Callable))([Callable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Callable.html)<V> callable)`
Call callable without cached resolver
`static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getClassOfMetaClass](#getClassOfMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](../../uml2/ext/magicdraw/classes/mdkernel/Class.html) metaClass)`

`static boolean`
`[hasUML2MetamodelNameAndURI](#hasUML2MetamodelNameAndURI(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model))([Model](../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html) model)`

`static boolean`
`[hasUML2MetaModelURI](#hasUML2MetaModelURI(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model))([Model](../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html) model)`

`static boolean`
`[isOfType](#isOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](../../uml2/ext/magicdraw/classes/mdkernel/Class.html) uml2MetaClass)`

`static boolean`
`[isOwnedByUML2Metamodel](#isOwnedByUML2Metamodel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](../../uml2/ext/magicdraw/classes/mdkernel/Class.html) c)`

`static boolean`
`[isUML2MetaClass](#isUML2MetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](../../uml2/ext/magicdraw/classes/mdkernel/Class.html) c)`

`static void`
`[setCachedResolver](#setCachedResolver(com.nomagic.magicdraw.uml2.UML2MetaTypes.CachedResolver))([UML2MetaTypes.CachedResolver](UML2MetaTypes.CachedResolver.html) resolver)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
UML2METAMODEL_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UML2METAMODEL_NAME
Name of UML2 metamodel
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.uml2.UML2MetaTypes.UML2METAMODEL_NAME)
UML2METAMODEL_URI
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UML2METAMODEL_URI
URI of UML2 metamodel, must correspond UML standard profile metamodel uri.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.uml2.UML2MetaTypes.UML2METAMODEL_URI)
UML2METAMODEL_PRIMITIVE_TYPES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UML2METAMODEL_PRIMITIVE_TYPES
Name of primitives package in the UML2 metamodel
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.uml2.UML2MetaTypes.UML2METAMODEL_PRIMITIVE_TYPES)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
UML2MetaTypes
public UML2MetaTypes()
 ============ METHOD DETAIL ========== 
Method Details
setCachedResolver
public static void setCachedResolver(@CheckForNull
 [UML2MetaTypes.CachedResolver](UML2MetaTypes.CachedResolver.html) resolver)
isUML2MetaClass
public static boolean isUML2MetaClass([Class](../../uml2/ext/magicdraw/classes/mdkernel/Class.html) c)
callWithoutCachedResolver
public static <V> V callWithoutCachedResolver([Callable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Callable.html)<V> callable)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Call callable without cached resolver
Type Parameters:
`V` - result type
Parameters:
`callable` - callable
Returns:
result of callable
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
isOwnedByUML2Metamodel
public static boolean isOwnedByUML2Metamodel([Class](../../uml2/ext/magicdraw/classes/mdkernel/Class.html) c)
getClassOfMetaClass
@CheckForNullpublic static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getClassOfMetaClass([Class](../../uml2/ext/magicdraw/classes/mdkernel/Class.html) metaClass)
isOfType
public static boolean isOfType([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](../../uml2/ext/magicdraw/classes/mdkernel/Class.html) uml2MetaClass)
Parameters:
`element` - any model element
Returns:
true if given class type of given element is compatible with java.lang.Class of the given metaType
hasUML2MetamodelNameAndURI
public static boolean hasUML2MetamodelNameAndURI([Model](../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html) model)
hasUML2MetaModelURI
public static boolean hasUML2MetaModelURI([Model](../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html) model)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2</a></div>
<h1 class="title" title="Class UML2MetaTypes">Class UML2MetaTypes</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml2.UML2MetaTypes</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">UML2MetaTypes</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="UML2MetaTypes.CachedResolver.html" title="interface in com.nomagic.magicdraw.uml2">UML2MetaTypes.CachedResolver</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#UML2METAMODEL_NAME">UML2METAMODEL_NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">Name of UML2 metamodel</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UML2METAMODEL_PRIMITIVE_TYPES">UML2METAMODEL_PRIMITIVE_TYPES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Name of primitives package in the UML2 metamodel</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#UML2METAMODEL_URI">UML2METAMODEL_URI</a></code></div>
<div class="col-last even-row-color">
<div class="block">URI of UML2 metamodel, must correspond UML standard profile metamodel uri.</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">UML2MetaTypes</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;V&gt; V</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#callWithoutCachedResolver(java.util.concurrent.Callable)">callWithoutCachedResolver</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent">Callable</a>&lt;V&gt; callable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Call callable without cached resolver</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassOfMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">getClassOfMetaClass</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> metaClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasUML2MetamodelNameAndURI(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model)">hasUML2MetamodelNameAndURI</a><wbr/>(<a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a> model)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasUML2MetaModelURI(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model)">hasUML2MetaModelURI</a><wbr/>(<a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a> model)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">isOfType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> uml2MetaClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOwnedByUML2Metamodel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">isOwnedByUML2Metamodel</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> c)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isUML2MetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">isUML2MetaClass</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> c)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setCachedResolver(com.nomagic.magicdraw.uml2.UML2MetaTypes.CachedResolver)">setCachedResolver</a><wbr/>(<a href="UML2MetaTypes.CachedResolver.html" title="interface in com.nomagic.magicdraw.uml2">UML2MetaTypes.CachedResolver</a> resolver)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="UML2METAMODEL_NAME">
<h3>UML2METAMODEL_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UML2METAMODEL_NAME</span></div>
<div class="block">Name of UML2 metamodel</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.uml2.UML2MetaTypes.UML2METAMODEL_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UML2METAMODEL_URI">
<h3>UML2METAMODEL_URI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UML2METAMODEL_URI</span></div>
<div class="block">URI of UML2 metamodel, must correspond UML standard profile metamodel uri.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.uml2.UML2MetaTypes.UML2METAMODEL_URI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UML2METAMODEL_PRIMITIVE_TYPES">
<h3>UML2METAMODEL_PRIMITIVE_TYPES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UML2METAMODEL_PRIMITIVE_TYPES</span></div>
<div class="block">Name of primitives package in the UML2 metamodel</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.uml2.UML2MetaTypes.UML2METAMODEL_PRIMITIVE_TYPES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
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
<section class="detail" id="&lt;init&gt;()">
<h3>UML2MetaTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">UML2MetaTypes</span>()</div>
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
<section class="detail" id="setCachedResolver(com.nomagic.magicdraw.uml2.UML2MetaTypes.CachedResolver)">
<h3>setCachedResolver</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setCachedResolver</span><wbr/><span class="parameters">(@CheckForNull
 <a href="UML2MetaTypes.CachedResolver.html" title="interface in com.nomagic.magicdraw.uml2">UML2MetaTypes.CachedResolver</a> resolver)</span></div>
</section>
</li>
<li>
<section class="detail" id="isUML2MetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>isUML2MetaClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isUML2MetaClass</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> c)</span></div>
</section>
</li>
<li>
<section class="detail" id="callWithoutCachedResolver(java.util.concurrent.Callable)">
<h3>callWithoutCachedResolver</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;V&gt;</span> <span class="return-type">V</span> <span class="element-name">callWithoutCachedResolver</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent">Callable</a>&lt;V&gt; callable)</span>
                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Call callable without cached resolver</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>V</code> - result type</dd>
<dt>Parameters:</dt>
<dd><code>callable</code> - callable</dd>
<dt>Returns:</dt>
<dd>result of callable</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOwnedByUML2Metamodel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>isOwnedByUML2Metamodel</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOwnedByUML2Metamodel</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> c)</span></div>
</section>
</li>
<li>
<section class="detail" id="getClassOfMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>getClassOfMetaClass</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getClassOfMetaClass</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> metaClass)</span></div>
</section>
</li>
<li>
<section class="detail" id="isOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>isOfType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOfType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> uml2MetaClass)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - any model element</dd>
<dt>Returns:</dt>
<dd>true if given class type of given element is compatible with java.lang.Class of the given metaType</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasUML2MetamodelNameAndURI(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model)">
<h3>hasUML2MetamodelNameAndURI</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasUML2MetamodelNameAndURI</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a> model)</span></div>
</section>
</li>
<li>
<section class="detail" id="hasUML2MetaModelURI(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model)">
<h3>hasUML2MetaModelURI</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasUML2MetaModelURI</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a> model)</span></div>
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
