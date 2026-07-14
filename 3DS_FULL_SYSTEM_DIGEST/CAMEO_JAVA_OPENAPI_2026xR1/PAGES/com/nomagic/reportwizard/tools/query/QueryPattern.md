# JAVA OPENAPI: QueryPattern (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/reportwizard/tools/query/QueryPattern.html
- source_path: `com/nomagic/reportwizard/tools/query/QueryPattern.html`
- source_sha256: `c5db3129166f612b938c00d7bef96002a9221f61fcb6daab0fc6c5caef39e84a`
- captured_utc: `2026-07-14T16:46:15.974014+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.query](package-summary.html)

## Class QueryPattern

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.reportwizard.tools.query.QueryPattern

@OpenApiAllpublic classQueryPattern
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Class for handler query pattern.

Since:
Jan 29, 2013

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[QueryPattern](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addAttribute](#addAttribute(com.nomagic.reportwizard.tools.query.QueryAttribute))([QueryAttribute](QueryAttribute.html) queryAttr)`
Add attribute condition for the element.
`void`
`[addAttribute](#addAttribute(java.lang.String,java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) attrName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) attrValue,
 int matchingType)`
Add attribute condition for the element.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[formatToCamelCase](#formatToCamelCase(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string)`
Convert text to camel-case.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[QueryAttribute](QueryAttribute.html)>`
`[getAttributeList](#getAttributeList())()`
Return element's attribute list.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getId](#getId())()`
Return element id.
`[QueryAttribute](QueryAttribute.html)`
`[getLastAttribute](#getLastAttribute())()`
Get a last attribute form attribute list.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getQueryPatternString](#getQueryPatternString())()`
Return query pattern.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getType](#getType())()`
Return element type.
`boolean`
`[isAllType](#isAllType())()`
Return true if element type is specific by *.
`boolean`
`[isNoChild](#isNoChild())()`
Return true if :empty is set to element.
`boolean`
`[isOnlyChildElement](#isOnlyChildElement())()`
Return true if query by child element .
`void`
`[setAllType](#setAllType(boolean))(boolean allType)`
Set true if element type is specific by *.
`void`
`[setAttributeList](#setAttributeList(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[QueryAttribute](QueryAttribute.html)> attributeList)`
Set element's attribute list.
`void`
`[setId](#setId(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Set element id.
`void`
`[setNoChild](#setNoChild(boolean))(boolean noChild)`
Set true if :empty is set to element.
`void`
`[setOnlyChildElement](#setOnlyChildElement(boolean))(boolean isOnlyChild)`
Set true if query by child element.
`void`
`[setType](#setType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)`
Set element type.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
QueryPattern
public QueryPattern()
 ============ METHOD DETAIL ========== 
Method Details
getType
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getType()
Return element type.
Returns:
element type
setType
public void setType([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)
Set element type.
Parameters:
`type` - element type
isAllType
public boolean isAllType()
Return true if element type is specific by *.
Returns:
true if element type is specific by * (all type), otherwise false
setAllType
public void setAllType(boolean allType)
Set true if element type is specific by *.
Parameters:
`allType` - true if element type is specific by *. otherwise false
getId
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getId()
Return element id.
Returns:
element id
setId
public void setId([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Set element id.
Parameters:
`id` - element id
isNoChild
public boolean isNoChild()
Return true if :empty is set to element.
Returns:
true if :empty is set to element, otherwise false
setNoChild
public void setNoChild(boolean noChild)
Set true if :empty is set to element.
Parameters:
`noChild` - true if :empty is set to element, otherwise false
getAttributeList
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[QueryAttribute](QueryAttribute.html)> getAttributeList()
Return element's attribute list.
Returns:
element's attribute list
setAttributeList
public void setAttributeList([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[QueryAttribute](QueryAttribute.html)> attributeList)
Set element's attribute list.
Parameters:
`attributeList` - element's attribute list
isOnlyChildElement
public boolean isOnlyChildElement()
Return true if query by child element .
Returns:
true if query element by child element, otherwise false
setOnlyChildElement
public void setOnlyChildElement(boolean isOnlyChild)
Set true if query by child element.
Parameters:
`isOnlyChild` - true if query by child element, otherwise false
formatToCamelCase
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) formatToCamelCase([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string)
Convert text to camel-case.
Parameters:
`string` - original string
Returns:
string in camel-case format
addAttribute
public void addAttribute([QueryAttribute](QueryAttribute.html) queryAttr)
Add attribute condition for the element.
Parameters:
`queryAttr` - a QueryAttribute
addAttribute
public void addAttribute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) attrName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) attrValue,
 int matchingType)
Add attribute condition for the element.
Parameters:
`attrName` - an attribute name
`attrValue` - an attribute value
`matchingType` - an attribute matching type
getLastAttribute
public [QueryAttribute](QueryAttribute.html) getLastAttribute()
Get a last attribute form attribute list.
Returns:
a last attribute
getQueryPatternString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getQueryPatternString()
Return query pattern.
Returns:
query pattern

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.query</a></div>
<h1 class="title" title="Class QueryPattern">Class QueryPattern</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.reportwizard.tools.query.QueryPattern</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">QueryPattern</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Class for handler query pattern.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jan 29, 2013</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">QueryPattern</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAttribute(com.nomagic.reportwizard.tools.query.QueryAttribute)">addAttribute</a><wbr/>(<a href="QueryAttribute.html" title="class in com.nomagic.reportwizard.tools.query">QueryAttribute</a> queryAttr)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add attribute condition for the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAttribute(java.lang.String,java.lang.String,int)">addAttribute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> attrName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> attrValue,
 int matchingType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add attribute condition for the element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#formatToCamelCase(java.lang.String)">formatToCamelCase</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert text to camel-case.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="QueryAttribute.html" title="class in com.nomagic.reportwizard.tools.query">QueryAttribute</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttributeList()">getAttributeList</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return element's attribute list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getId()">getId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return element id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="QueryAttribute.html" title="class in com.nomagic.reportwizard.tools.query">QueryAttribute</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastAttribute()">getLastAttribute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get a last attribute form attribute list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getQueryPatternString()">getQueryPatternString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return query pattern.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return element type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAllType()">isAllType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return true if element type is specific by *.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNoChild()">isNoChild</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return true if :empty is set to element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isOnlyChildElement()">isOnlyChildElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return true if query by child element .</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAllType(boolean)">setAllType</a><wbr/>(boolean allType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set true if element type is specific by *.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAttributeList(java.util.List)">setAttributeList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="QueryAttribute.html" title="class in com.nomagic.reportwizard.tools.query">QueryAttribute</a>&gt; attributeList)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set element's attribute list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setId(java.lang.String)">setId</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set element id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNoChild(boolean)">setNoChild</a><wbr/>(boolean noChild)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set true if :empty is set to element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOnlyChildElement(boolean)">setOnlyChildElement</a><wbr/>(boolean isOnlyChild)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set true if query by child element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setType(java.lang.String)">setType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set element type.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>QueryPattern</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">QueryPattern</span>()</div>
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
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getType</span>()</div>
<div class="block">Return element type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setType(java.lang.String)">
<h3>setType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Set element type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - element type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAllType()">
<h3>isAllType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAllType</span>()</div>
<div class="block">Return true if element type is specific by *.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if element type is specific by * (all type), otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAllType(boolean)">
<h3>setAllType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAllType</span><wbr/><span class="parameters">(boolean allType)</span></div>
<div class="block">Set true if element type is specific by *.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>allType</code> - true if element type is specific by *. otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getId()">
<h3>getId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()</div>
<div class="block">Return element id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setId(java.lang.String)">
<h3>setId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setId</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Set element id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - element id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNoChild()">
<h3>isNoChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNoChild</span>()</div>
<div class="block">Return true if :empty is set to element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if :empty is set to element, otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNoChild(boolean)">
<h3>setNoChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNoChild</span><wbr/><span class="parameters">(boolean noChild)</span></div>
<div class="block">Set true if :empty is set to element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>noChild</code> - true if :empty is set to element, otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttributeList()">
<h3>getAttributeList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="QueryAttribute.html" title="class in com.nomagic.reportwizard.tools.query">QueryAttribute</a>&gt;</span> <span class="element-name">getAttributeList</span>()</div>
<div class="block">Return element's attribute list.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element's attribute list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAttributeList(java.util.List)">
<h3>setAttributeList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAttributeList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="QueryAttribute.html" title="class in com.nomagic.reportwizard.tools.query">QueryAttribute</a>&gt; attributeList)</span></div>
<div class="block">Set element's attribute list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attributeList</code> - element's attribute list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOnlyChildElement()">
<h3>isOnlyChildElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOnlyChildElement</span>()</div>
<div class="block">Return true if query by child element .</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if query element by child element, otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOnlyChildElement(boolean)">
<h3>setOnlyChildElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOnlyChildElement</span><wbr/><span class="parameters">(boolean isOnlyChild)</span></div>
<div class="block">Set true if query by child element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>isOnlyChild</code> - true if query by child element, otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="formatToCamelCase(java.lang.String)">
<h3>formatToCamelCase</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">formatToCamelCase</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</span></div>
<div class="block">Convert text to camel-case.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>string</code> - original string</dd>
<dt>Returns:</dt>
<dd>string in camel-case format</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAttribute(com.nomagic.reportwizard.tools.query.QueryAttribute)">
<h3>addAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAttribute</span><wbr/><span class="parameters">(<a href="QueryAttribute.html" title="class in com.nomagic.reportwizard.tools.query">QueryAttribute</a> queryAttr)</span></div>
<div class="block">Add attribute condition for the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>queryAttr</code> - a QueryAttribute</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAttribute(java.lang.String,java.lang.String,int)">
<h3>addAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAttribute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> attrName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> attrValue,
 int matchingType)</span></div>
<div class="block">Add attribute condition for the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attrName</code> - an attribute name</dd>
<dd><code>attrValue</code> - an attribute value</dd>
<dd><code>matchingType</code> - an attribute matching type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastAttribute()">
<h3>getLastAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="QueryAttribute.html" title="class in com.nomagic.reportwizard.tools.query">QueryAttribute</a></span> <span class="element-name">getLastAttribute</span>()</div>
<div class="block">Get a last attribute form attribute list.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a last attribute</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQueryPatternString()">
<h3>getQueryPatternString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQueryPatternString</span>()</div>
<div class="block">Return query pattern.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>query pattern</dd>
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
