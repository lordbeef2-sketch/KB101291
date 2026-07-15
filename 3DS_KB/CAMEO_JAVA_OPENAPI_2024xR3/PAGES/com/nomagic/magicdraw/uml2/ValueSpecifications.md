# JAVA OPENAPI: ValueSpecifications (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml2/ValueSpecifications.html
- source_path: `com/nomagic/magicdraw/uml2/ValueSpecifications.html`
- source_sha256: `2c24e9b4e02b126a9f9408a2996a5b918056d8b16bf356d94a887d0a82c46b17`
- captured_utc: `2026-07-14T16:56:06.578581+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2](package-summary.html)

## Class ValueSpecifications

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml2.ValueSpecifications

public classValueSpecifications
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Convenience static methods that operate on or return ValueSpecification elements.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ValueSpecifications](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)`
`[createValueSpecification](#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)> valueSpecificationClass,
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) valueType,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [ElementsFactory](../../uml2/impl/ElementsFactory.html) factory,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)> reuse)`
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
`static [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)`
`[createValueSpecification](#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection,boolean))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)> valueSpecificationClass,
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) valueType,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [ElementsFactory](../../uml2/impl/ElementsFactory.html) factory,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)> reuse,
 boolean ignoreValuesOfReuse)`
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
`static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[getEnumerationLiteral](#getEnumerationLiteral(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,java.lang.String))([Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) enumeration,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) literalName)`
Gets EnumerationLiteral from Enumeration by name.
`static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)>`
`[getValueSpecificationClass](#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) valueType)`
Return a meta type of ValueSpecification which should be used to store values of given type
`static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)>`
`[getValueSpecificationClass](#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object))([Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) valueType,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Return a meta type of ValueSpecification which should be used to store values of given type or value.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getValueSpecificationValue](#getValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification)`
Return value of given ValueSpecification
`static boolean`
`[isValueSpecificationClassElementValue](#isValueSpecificationClassElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) valueType)`

`static void`
`[setIntervalValueParser](#setIntervalValueParser(java.util.function.Function))([Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[Interval](../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> intervalParser)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ValueSpecifications
public ValueSpecifications()
 ============ METHOD DETAIL ========== 
Method Details
setIntervalValueParser
public static void setIntervalValueParser(@CheckForNull
 [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[Interval](../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> intervalParser)
getValueSpecificationValue
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getValueSpecificationValue(@CheckForNull
 [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification)
Return value of given ValueSpecification
Parameters:
`valueSpecification` - value specification
Returns:
value
createValueSpecification
@CheckForNullpublic static [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) createValueSpecification(@CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)> valueSpecificationClass,
 @CheckForNull
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) valueType,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [ElementsFactory](../../uml2/impl/ElementsFactory.html) factory,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)> reuse)
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
Parameters:
`valueSpecificationClass` - meta type of value specification
`value` - value value of ValueSpecification
`factory` - factory
`reuse` - a collection of possible value specifications to reuse
Returns:
specification
createValueSpecification
@CheckForNullpublic static [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) createValueSpecification(@CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)> valueSpecificationClass,
 @CheckForNull
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) valueType,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [ElementsFactory](../../uml2/impl/ElementsFactory.html) factory,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)> reuse,
 boolean ignoreValuesOfReuse)
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
Parameters:
`valueSpecificationClass` - meta type of value specification
`value` - value value of ValueSpecification
`factory` - factory
`reuse` - a collection of possible value specifications to reuse
`ignoreValuesOfReuse` - if false, checks is value if reuse candidate is suitable, not only the meta type. If true, checks just a metatype and overwrites the value
Returns:
specification
getEnumerationLiteral
@CheckForNullpublic static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) getEnumerationLiteral([Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) enumeration,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) literalName)
Gets EnumerationLiteral from Enumeration by name.
Parameters:
`enumeration` - enumeration which literals will be searched.
`literalName` - name of the EnumerationLiteral.
Returns:
EnumerationLiteral from Enumeration by name.
getValueSpecificationClass
public static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)> getValueSpecificationClass(@CheckForNull
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) valueType,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Return a meta type of ValueSpecification which should be used to store values of given type or value. If valueType is null, value is used to define a meta type of value specification.
Parameters:
`valueType` - value type
Returns:
meta type of value specification
getValueSpecificationClass
public static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)> getValueSpecificationClass(@CheckForNull
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) valueType)
Return a meta type of ValueSpecification which should be used to store values of given type
Parameters:
`valueType` - value type
Returns:
meta type of value specification
isValueSpecificationClassElementValue
public static boolean isValueSpecificationClassElementValue(@CheckForNull
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) valueType)
Parameters:
`valueType` - value type
Returns:
true if ValueSpecification for given type should be ElementValue

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2</a></div>
<h1 class="title" title="Class ValueSpecifications">Class ValueSpecifications</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml2.ValueSpecifications</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">ValueSpecifications</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Convenience static methods that operate on or return ValueSpecification elements.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ValueSpecifications</a>()</code></div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)">createValueSpecification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; valueSpecificationClass,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="../../uml2/impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> factory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection,boolean)">createValueSpecification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; valueSpecificationClass,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="../../uml2/impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> factory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse,
 boolean ignoreValuesOfReuse)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEnumerationLiteral(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,java.lang.String)">getEnumerationLiteral</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> enumeration,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literalName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets EnumerationLiteral from Enumeration by name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">getValueSpecificationClass</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a meta type of ValueSpecification which should be used to store values of given type</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)">getValueSpecificationClass</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a meta type of ValueSpecification which should be used to store values of given type or value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">getValueSpecificationValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return value of given ValueSpecification</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isValueSpecificationClassElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">isValueSpecificationClassElementValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setIntervalValueParser(java.util.function.Function)">setIntervalValueParser</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; intervalParser)</code></div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ValueSpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValueSpecifications</span>()</div>
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
<section class="detail" id="setIntervalValueParser(java.util.function.Function)">
<h3>setIntervalValueParser</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setIntervalValueParser</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; intervalParser)</span></div>
</section>
</li>
<li>
<section class="detail" id="getValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>getValueSpecificationValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValueSpecificationValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification)</span></div>
<div class="block">Return value of given ValueSpecification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueSpecification</code> - value specification</dd>
<dt>Returns:</dt>
<dd>value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)">
<h3>createValueSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">createValueSpecification</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; valueSpecificationClass,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="../../uml2/impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> factory,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse)</span></div>
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueSpecificationClass</code> - meta type of value specification</dd>
<dd><code>value</code> - value value of ValueSpecification</dd>
<dd><code>factory</code> - factory</dd>
<dd><code>reuse</code> - a collection of possible value specifications to reuse</dd>
<dt>Returns:</dt>
<dd>specification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection,boolean)">
<h3>createValueSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">createValueSpecification</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; valueSpecificationClass,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="../../uml2/impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> factory,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse,
 boolean ignoreValuesOfReuse)</span></div>
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueSpecificationClass</code> - meta type of value specification</dd>
<dd><code>value</code> - value value of ValueSpecification</dd>
<dd><code>factory</code> - factory</dd>
<dd><code>reuse</code> - a collection of possible value specifications to reuse</dd>
<dd><code>ignoreValuesOfReuse</code> - if false, checks is value if reuse candidate is suitable, not only the meta type. If true, checks just a metatype and overwrites the value</dd>
<dt>Returns:</dt>
<dd>specification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnumerationLiteral(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,java.lang.String)">
<h3>getEnumerationLiteral</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">getEnumerationLiteral</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> enumeration,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> literalName)</span></div>
<div class="block">Gets EnumerationLiteral from Enumeration by name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enumeration</code> - enumeration which literals will be searched.</dd>
<dd><code>literalName</code> - name of the EnumerationLiteral.</dd>
<dt>Returns:</dt>
<dd>EnumerationLiteral from Enumeration by name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)">
<h3>getValueSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt;</span> <span class="element-name">getValueSpecificationClass</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Return a meta type of ValueSpecification which should be used to store values of given type or value. If valueType is null, value is used to define a meta type of value specification.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueType</code> - value type</dd>
<dt>Returns:</dt>
<dd>meta type of value specification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>getValueSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt;</span> <span class="element-name">getValueSpecificationClass</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType)</span></div>
<div class="block">Return a meta type of ValueSpecification which should be used to store values of given type</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueType</code> - value type</dd>
<dt>Returns:</dt>
<dd>meta type of value specification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isValueSpecificationClassElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>isValueSpecificationClassElementValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isValueSpecificationClassElementValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueType</code> - value type</dd>
<dt>Returns:</dt>
<dd>true if ValueSpecification for given type should be ElementValue</dd>
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
