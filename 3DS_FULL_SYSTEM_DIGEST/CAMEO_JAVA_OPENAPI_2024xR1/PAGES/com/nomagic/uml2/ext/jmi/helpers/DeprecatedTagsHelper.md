# JAVA OPENAPI: DeprecatedTagsHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/jmi/helpers/DeprecatedTagsHelper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/DeprecatedTagsHelper.html`
- source_sha256: `af3de1925701ccc1bff353c04211fa00be141eec439beac1bc1603ab64b83512`
- captured_utc: `2026-07-14T16:52:40.260256+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class DeprecatedTagsHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.jmi.helpers.DeprecatedTagsHelper

Direct Known Subclasses:
`[DeprecatedStereotypesHelper](DeprecatedStereotypesHelper.html)`

@OpenApiAllpublic classDeprecatedTagsHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Utility class to work with tagged values. It has only deprecated methods for API compatibility.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DeprecatedTagsHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static void`
`[clearStereotypeProperty](#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)`
Deprecated.
use [`TagsHelper.clearStereotypeProperty(Element, Stereotype, String)`](TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))
`static void`
`[clearStereotypeProperty](#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean removeEmptyTaggedValues)`
Deprecated.
use [`TagsHelper.clearStereotypeProperty(Element, Stereotype, String, boolean)`](TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getStereotypePropertyFirst](#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)`
Deprecated.
use [`TagsHelper.getStereotypePropertyFirst(Element, Stereotype, String)`](TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getStereotypePropertyFirst](#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean calculateDerived)`
Deprecated.
use [`TagsHelper.getStereotypePropertyFirst(Element, Stereotype, String, boolean)`](TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[getStereotypePropertyValue](#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)`
Deprecated.
use [`TagsHelper.getStereotypePropertyValue(Element, Stereotype, String)`](TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[getStereotypePropertyValue](#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean calculateDerived)`
Deprecated.
use [`TagsHelper.getStereotypePropertyValue(Element, Stereotype, String, boolean)`](TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getStereotypePropertyValueAsString](#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)`
Deprecated.
use [`TagsHelper.getStereotypePropertyValueAsString(Element, Stereotype, String)`](TagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getStereotypePropertyValueAsString](#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean calculateDerived)`
Deprecated.
use [`TagsHelper.getStereotypePropertyValueAsString(Element, Stereotype, String, boolean)`](TagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DeprecatedTagsHelper
public DeprecatedTagsHelper()
 ============ METHOD DETAIL ========== 
Method Details
getStereotypePropertyValueAsString
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getStereotypePropertyValueAsString([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)
Deprecated.
use [`TagsHelper.getStereotypePropertyValueAsString(Element, Stereotype, String)`](TagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))
Gets tagged values as list of strings.
Parameters:
`element` - element with assigned stereotype
`stereotype` - stereotype name
`tagName` - name of tag definition
Returns:
values
getStereotypePropertyValueAsString
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getStereotypePropertyValueAsString([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean calculateDerived)
Deprecated.
use [`TagsHelper.getStereotypePropertyValueAsString(Element, Stereotype, String, boolean)`](TagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))
Gets tagged values as list of strings.
Parameters:
`element` - element with assigned stereotype
`stereotype` - stereotype
`tagName` - name of tag definition
`calculateDerived` - if to calculate derived property value
Returns:
values
getStereotypePropertyValue
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) getStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)
Deprecated.
use [`TagsHelper.getStereotypePropertyValue(Element, Stereotype, String)`](TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))
Gets tagged values as list.
Parameters:
`element` - element with applied stereotype
`stereotype` - stereotype
`tagName` - name of tag definition
Returns:
values
getStereotypePropertyValue
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) getStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean calculateDerived)
Deprecated.
use [`TagsHelper.getStereotypePropertyValue(Element, Stereotype, String, boolean)`](TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))
Gets stereotype property value as list
Parameters:
`element` - element with applied stereotype
`stereotype` - stereotype name
`tagName` - name of tag definition
`calculateDerived` - if to calculate derived property value
Returns:
values
clearStereotypeProperty
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void clearStereotypeProperty([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)
Deprecated.
use [`TagsHelper.clearStereotypeProperty(Element, Stereotype, String)`](TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))
Clears tagged values.
Parameters:
`element` - element
`stereotype` - stereotype name
`tagName` - name of tag definition
clearStereotypeProperty
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void clearStereotypeProperty([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean removeEmptyTaggedValues)
Deprecated.
use [`TagsHelper.clearStereotypeProperty(Element, Stereotype, String, boolean)`](TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))
Clears tagged values and removes TaggedValue if needed.
Parameters:
`element` - element
`stereotype` - stereotype name
`tagName` - name of tag definition
`removeEmptyTaggedValues` - remove all owned empty TaggedValues
getStereotypePropertyFirst
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getStereotypePropertyFirst([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)
Deprecated.
use [`TagsHelper.getStereotypePropertyFirst(Element, Stereotype, String)`](TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))
Returns first value of TaggedValue.
Parameters:
`element` - element
`stereotype` - stereotype name
`tagName` - name of tag definition
Returns:
first value of TaggedValue
getStereotypePropertyFirst
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getStereotypePropertyFirst([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean calculateDerived)
Deprecated.
use [`TagsHelper.getStereotypePropertyFirst(Element, Stereotype, String, boolean)`](TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))
Returns first value of TaggedValue.
Parameters:
`element` - element
`stereotype` - stereotype name
`tagName` - name of tag definition
`calculateDerived` - if to calculate derived value
Returns:
first value of TaggedValue

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class DeprecatedTagsHelper">Class DeprecatedTagsHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.DeprecatedTagsHelper</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="DeprecatedStereotypesHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">DeprecatedStereotypesHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DeprecatedTagsHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with tagged values. It has only deprecated methods for API compatibility.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DeprecatedTagsHelper</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">clearStereotypeProperty</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)"><code>TagsHelper.clearStereotypeProperty(Element, Stereotype, String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">clearStereotypeProperty</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean removeEmptyTaggedValues)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)"><code>TagsHelper.clearStereotypeProperty(Element, Stereotype, String, boolean)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">getStereotypePropertyFirst</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)"><code>TagsHelper.getStereotypePropertyFirst(Element, Stereotype, String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">getStereotypePropertyFirst</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean calculateDerived)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)"><code>TagsHelper.getStereotypePropertyFirst(Element, Stereotype, String, boolean)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">getStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)"><code>TagsHelper.getStereotypePropertyValue(Element, Stereotype, String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">getStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean calculateDerived)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)"><code>TagsHelper.getStereotypePropertyValue(Element, Stereotype, String, boolean)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">getStereotypePropertyValueAsString</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)"><code>TagsHelper.getStereotypePropertyValueAsString(Element, Stereotype, String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">getStereotypePropertyValueAsString</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean calculateDerived)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)"><code>TagsHelper.getStereotypePropertyValueAsString(Element, Stereotype, String, boolean)</code></a></div>
</div>
</div>
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
<h3>DeprecatedTagsHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DeprecatedTagsHelper</span>()</div>
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
<section class="detail" id="getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">
<h3>getStereotypePropertyValueAsString</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getStereotypePropertyValueAsString</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)"><code>TagsHelper.getStereotypePropertyValueAsString(Element, Stereotype, String)</code></a></div>
</div>
<div class="block">Gets tagged values as list of strings.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with assigned stereotype</dd>
<dd><code>stereotype</code> - stereotype name</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dt>Returns:</dt>
<dd>values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">
<h3>getStereotypePropertyValueAsString</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getStereotypePropertyValueAsString</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean calculateDerived)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)"><code>TagsHelper.getStereotypePropertyValueAsString(Element, Stereotype, String, boolean)</code></a></div>
</div>
<div class="block">Gets tagged values as list of strings.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with assigned stereotype</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dd><code>calculateDerived</code> - if to calculate derived property value</dd>
<dt>Returns:</dt>
<dd>values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">
<h3>getStereotypePropertyValue</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">getStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)"><code>TagsHelper.getStereotypePropertyValue(Element, Stereotype, String)</code></a></div>
</div>
<div class="block">Gets tagged values as list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dt>Returns:</dt>
<dd>values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">
<h3>getStereotypePropertyValue</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">getStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean calculateDerived)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)"><code>TagsHelper.getStereotypePropertyValue(Element, Stereotype, String, boolean)</code></a></div>
</div>
<div class="block">Gets stereotype property value as list</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - stereotype name</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dd><code>calculateDerived</code> - if to calculate derived property value</dd>
<dt>Returns:</dt>
<dd>values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">
<h3>clearStereotypeProperty</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">clearStereotypeProperty</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)"><code>TagsHelper.clearStereotypeProperty(Element, Stereotype, String)</code></a></div>
</div>
<div class="block">Clears tagged values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype name</dd>
<dd><code>tagName</code> - name of tag definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">
<h3>clearStereotypeProperty</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">clearStereotypeProperty</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean removeEmptyTaggedValues)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)"><code>TagsHelper.clearStereotypeProperty(Element, Stereotype, String, boolean)</code></a></div>
</div>
<div class="block">Clears tagged values and removes TaggedValue if needed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype name</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dd><code>removeEmptyTaggedValues</code> - remove all owned empty TaggedValues</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">
<h3>getStereotypePropertyFirst</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getStereotypePropertyFirst</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)"><code>TagsHelper.getStereotypePropertyFirst(Element, Stereotype, String)</code></a></div>
</div>
<div class="block">Returns first value of TaggedValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype name</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dt>Returns:</dt>
<dd>first value of TaggedValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">
<h3>getStereotypePropertyFirst</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getStereotypePropertyFirst</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean calculateDerived)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)"><code>TagsHelper.getStereotypePropertyFirst(Element, Stereotype, String, boolean)</code></a></div>
</div>
<div class="block">Returns first value of TaggedValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype name</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dd><code>calculateDerived</code> - if to calculate derived value</dd>
<dt>Returns:</dt>
<dd>first value of TaggedValue</dd>
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
