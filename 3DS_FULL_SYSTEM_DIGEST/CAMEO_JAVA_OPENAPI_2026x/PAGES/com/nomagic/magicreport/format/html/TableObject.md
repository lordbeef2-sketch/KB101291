# JAVA OPENAPI: TableObject (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/format/html/TableObject.html
- source_path: `com/nomagic/magicreport/format/html/TableObject.html`
- source_sha256: `781f27bdac71be4529790ac9c8b1722390d41a4d05a4b3af6f1372fb7674e368`
- captured_utc: `2026-07-14T16:58:39.701312+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format.html](package-summary.html)

## Class TableObject

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.format.html.TableObject

@OpenApiAllpublic classTableObject
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

The class use for collect table tag of HTML.

Since:
Feb 04, 2013
Version:
1.0 Feb 04, 2013

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TABLE_INDEX](#TABLE_INDEX)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TABLE_MARGIN_LEFT](#TABLE_MARGIN_LEFT)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TABLE_MARGIN_RIGTH](#TABLE_MARGIN_RIGTH)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TABLE_WIDTH](#TABLE_WIDTH)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TableObject](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addBodyRowList](#addBodyRowList(com.nomagic.magicreport.format.html.RowObject))([RowObject](RowObject.html) rowObject)`

`void`
`[addHeaderRowList](#addHeaderRowList(com.nomagic.magicreport.format.html.RowObject))([RowObject](RowObject.html) rowObject)`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Attribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/javax/management/Attribute.html)>`
`[getAttributes](#getAttributes())()`
Gets attributes.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RowObject](RowObject.html)>`
`[getBodyRowList](#getBodyRowList())()`
Gets bodyRowList.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RowObject](RowObject.html)>`
`[getHeaderRowList](#getHeaderRowList())()`
Gets headerRowList.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[getTableProperties](#getTableProperties())()`
Get table properties
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getTablePropertiesValue](#getTablePropertiesValue(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)`
Remove data from tableProperties
`void`
`[removeTableProperties](#removeTableProperties(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)`
Remove data from tableProperties
`void`
`[setAttributes](#setAttributes(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Attribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/javax/management/Attribute.html)> attributes)`
Sets attributes.
`void`
`[setBodyRowList](#setBodyRowList(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RowObject](RowObject.html)> bodyRowList)`
Sets bodyRowList.
`void`
`[setHeaderRowList](#setHeaderRowList(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RowObject](RowObject.html)> headerRowList)`
Sets headerRowList.
`void`
`[setTableProperties](#setTableProperties(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> tableProperties)`
Set table properties
`void`
`[updateTableProperties](#updateTableProperties(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Update value in tableProperties
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
TABLE_INDEX
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TABLE_INDEX
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.TableObject.TABLE_INDEX)
TABLE_WIDTH
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TABLE_WIDTH
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.TableObject.TABLE_WIDTH)
TABLE_MARGIN_LEFT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TABLE_MARGIN_LEFT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.TableObject.TABLE_MARGIN_LEFT)
TABLE_MARGIN_RIGTH
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TABLE_MARGIN_RIGTH
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.TableObject.TABLE_MARGIN_RIGTH)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TableObject
public TableObject()
 ============ METHOD DETAIL ========== 
Method Details
getHeaderRowList
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RowObject](RowObject.html)> getHeaderRowList()
Gets headerRowList.
Returns:
the headerRowList
setHeaderRowList
public void setHeaderRowList([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RowObject](RowObject.html)> headerRowList)
Sets headerRowList.
Parameters:
`headerRowList` - the headerRowList to set
getBodyRowList
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RowObject](RowObject.html)> getBodyRowList()
Gets bodyRowList.
Returns:
the bodyRowList
setBodyRowList
public void setBodyRowList([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RowObject](RowObject.html)> bodyRowList)
Sets bodyRowList.
Parameters:
`bodyRowList` - the bodyRowList to set
getAttributes
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Attribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/javax/management/Attribute.html)> getAttributes()
Gets attributes.
Returns:
the attributes
setAttributes
public void setAttributes([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Attribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/javax/management/Attribute.html)> attributes)
Sets attributes.
Parameters:
`attributes` - the attributes to set
addBodyRowList
public void addBodyRowList([RowObject](RowObject.html) rowObject)
addHeaderRowList
public void addHeaderRowList([RowObject](RowObject.html) rowObject)
getTableProperties
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> getTableProperties()
Get table properties
Returns:
tableProperties
setTableProperties
public void setTableProperties([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> tableProperties)
Set table properties
Parameters:
`tableProperties` - tableProperties
updateTableProperties
public void updateTableProperties([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Update value in tableProperties
Parameters:
`key` - key
`value` - value
removeTableProperties
public void removeTableProperties([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)
Remove data from tableProperties
Parameters:
`key` - key key to remove
getTablePropertiesValue
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getTablePropertiesValue([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)
Remove data from tableProperties
Parameters:
`key` - a key to remove
Returns:
table property of specific key

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format.html</a></div>
<h1 class="title" title="Class TableObject">Class TableObject</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.format.html.TableObject</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TableObject</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The class use for collect table tag of HTML.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Feb 04, 2013</dd>
<dt>Version:</dt>
<dd>1.0 Feb 04, 2013</dd>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TABLE_INDEX">TABLE_INDEX</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TABLE_MARGIN_LEFT">TABLE_MARGIN_LEFT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TABLE_MARGIN_RIGTH">TABLE_MARGIN_RIGTH</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TABLE_WIDTH">TABLE_WIDTH</a></code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TableObject</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addBodyRowList(com.nomagic.magicreport.format.html.RowObject)">addBodyRowList</a><wbr/>(<a href="RowObject.html" title="class in com.nomagic.magicreport.format.html">RowObject</a> rowObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addHeaderRowList(com.nomagic.magicreport.format.html.RowObject)">addHeaderRowList</a><wbr/>(<a href="RowObject.html" title="class in com.nomagic.magicreport.format.html">RowObject</a> rowObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.management/javax/management/Attribute.html" title="class or interface in javax.management">Attribute</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttributes()">getAttributes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets attributes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="RowObject.html" title="class in com.nomagic.magicreport.format.html">RowObject</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBodyRowList()">getBodyRowList</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets bodyRowList.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="RowObject.html" title="class in com.nomagic.magicreport.format.html">RowObject</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHeaderRowList()">getHeaderRowList</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets headerRowList.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTableProperties()">getTableProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get table properties</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTablePropertiesValue(java.lang.String)">getTablePropertiesValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove data from tableProperties</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeTableProperties(java.lang.String)">removeTableProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove data from tableProperties</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAttributes(java.util.List)">setAttributes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.management/javax/management/Attribute.html" title="class or interface in javax.management">Attribute</a>&gt; attributes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets attributes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBodyRowList(java.util.List)">setBodyRowList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RowObject.html" title="class in com.nomagic.magicreport.format.html">RowObject</a>&gt; bodyRowList)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets bodyRowList.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHeaderRowList(java.util.List)">setHeaderRowList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RowObject.html" title="class in com.nomagic.magicreport.format.html">RowObject</a>&gt; headerRowList)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets headerRowList.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTableProperties(java.util.Map)">setTableProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; tableProperties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set table properties</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateTableProperties(java.lang.String,java.lang.Object)">updateTableProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Update value in tableProperties</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="TABLE_INDEX">
<h3>TABLE_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TABLE_INDEX</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.TableObject.TABLE_INDEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TABLE_WIDTH">
<h3>TABLE_WIDTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TABLE_WIDTH</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.TableObject.TABLE_WIDTH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TABLE_MARGIN_LEFT">
<h3>TABLE_MARGIN_LEFT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TABLE_MARGIN_LEFT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.TableObject.TABLE_MARGIN_LEFT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TABLE_MARGIN_RIGTH">
<h3>TABLE_MARGIN_RIGTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TABLE_MARGIN_RIGTH</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.TableObject.TABLE_MARGIN_RIGTH">Constant Field Values</a></li>
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
<h3>TableObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TableObject</span>()</div>
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
<section class="detail" id="getHeaderRowList()">
<h3>getHeaderRowList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RowObject.html" title="class in com.nomagic.magicreport.format.html">RowObject</a>&gt;</span> <span class="element-name">getHeaderRowList</span>()</div>
<div class="block">Gets headerRowList.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the headerRowList</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHeaderRowList(java.util.List)">
<h3>setHeaderRowList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHeaderRowList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RowObject.html" title="class in com.nomagic.magicreport.format.html">RowObject</a>&gt; headerRowList)</span></div>
<div class="block">Sets headerRowList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>headerRowList</code> - the headerRowList to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBodyRowList()">
<h3>getBodyRowList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RowObject.html" title="class in com.nomagic.magicreport.format.html">RowObject</a>&gt;</span> <span class="element-name">getBodyRowList</span>()</div>
<div class="block">Gets bodyRowList.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the bodyRowList</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBodyRowList(java.util.List)">
<h3>setBodyRowList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBodyRowList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RowObject.html" title="class in com.nomagic.magicreport.format.html">RowObject</a>&gt; bodyRowList)</span></div>
<div class="block">Sets bodyRowList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bodyRowList</code> - the bodyRowList to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttributes()">
<h3>getAttributes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.management/javax/management/Attribute.html" title="class or interface in javax.management">Attribute</a>&gt;</span> <span class="element-name">getAttributes</span>()</div>
<div class="block">Gets attributes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the attributes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAttributes(java.util.List)">
<h3>setAttributes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAttributes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.management/javax/management/Attribute.html" title="class or interface in javax.management">Attribute</a>&gt; attributes)</span></div>
<div class="block">Sets attributes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attributes</code> - the attributes to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addBodyRowList(com.nomagic.magicreport.format.html.RowObject)">
<h3>addBodyRowList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addBodyRowList</span><wbr/><span class="parameters">(<a href="RowObject.html" title="class in com.nomagic.magicreport.format.html">RowObject</a> rowObject)</span></div>
</section>
</li>
<li>
<section class="detail" id="addHeaderRowList(com.nomagic.magicreport.format.html.RowObject)">
<h3>addHeaderRowList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addHeaderRowList</span><wbr/><span class="parameters">(<a href="RowObject.html" title="class in com.nomagic.magicreport.format.html">RowObject</a> rowObject)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTableProperties()">
<h3>getTableProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getTableProperties</span>()</div>
<div class="block">Get table properties</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tableProperties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTableProperties(java.util.Map)">
<h3>setTableProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTableProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; tableProperties)</span></div>
<div class="block">Set table properties</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tableProperties</code> - tableProperties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateTableProperties(java.lang.String,java.lang.Object)">
<h3>updateTableProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateTableProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Update value in tableProperties</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - key</dd>
<dd><code>value</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeTableProperties(java.lang.String)">
<h3>removeTableProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeTableProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div class="block">Remove data from tableProperties</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - key key to remove</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTablePropertiesValue(java.lang.String)">
<h3>getTablePropertiesValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getTablePropertiesValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div class="block">Remove data from tableProperties</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - a key to remove</dd>
<dt>Returns:</dt>
<dd>table property of specific key</dd>
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
