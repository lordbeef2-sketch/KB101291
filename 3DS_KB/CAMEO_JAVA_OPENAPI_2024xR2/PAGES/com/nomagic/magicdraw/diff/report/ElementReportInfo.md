# JAVA OPENAPI: ElementReportInfo (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/diff/report/ElementReportInfo.html
- source_path: `com/nomagic/magicdraw/diff/report/ElementReportInfo.html`
- source_sha256: `dd1a478884c35c04bba7512734a77a9286ef50ab1cef1ee688041087e8c9a0e9`
- captured_utc: `2026-07-14T16:55:16.088018+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff.report](package-summary.html)

## Class ElementReportInfo

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.diff.report.ElementReportInfo

@OpenApiAllpublic classElementReportInfo
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains merge/diff report element information.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[ElementReportInfo](#%3Cinit%3E(java.lang.String,com.nomagic.magicdraw.diff.report.ReportType))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [ReportType](ReportType.html) reportType)`
Constructs element report info.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`int`
`[depth](#depth())()`
Gets element depth in containment tree.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getAddedTypeText](#getAddedTypeText())()`
Gets text of the added modification kind.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getElementName](#getElementName())()`
Gets name of the element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getElementType](#getElementType())()`
Gets type of the element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getID](#getID())()`
Gets element ID.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getModificationKindText](#getModificationKindText(com.nomagic.magicdraw.diff.ModificationKind))([ModificationKind](../ModificationKind.html) modificationKind)`
Gets representation text of a modification kind.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getModifiedTypeText](#getModifiedTypeText())()`
Gets text of the modified modification kind.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PropertyReportInfo](PropertyReportInfo.html)>`
`[getProperties](#getProperties())()`
Gets modified properties.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getQualifiedName](#getQualifiedName())()`
Gets element qualified name.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRemovedTypeText](#getRemovedTypeText())()`
Gets text of the removed modification kind.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSourceChangeKind](#getSourceChangeKind())()`
Gets source change kind.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTargetChangeKind](#getTargetChangeKind())()`
Gets target change kind.
`boolean`
`[isOfKind](#isOfKind(com.nomagic.magicdraw.diff.ModificationKind))([ModificationKind](../ModificationKind.html) modificationKind)`
Checks if modification is of a given type.
`void`
`[setElementName](#setElementName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementName)`
Sets name of the element.
`void`
`[setElementType](#setElementType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementType)`
Sets element type.
`void`
`[setProperties](#setProperties(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PropertyReportInfo](PropertyReportInfo.html)> properties)`
Sets modified properties.
`void`
`[setQualifiedName](#setQualifiedName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName)`
Sets element qualified name.
`void`
`[setSourceChangeKind](#setSourceChangeKind(com.nomagic.magicdraw.diff.ModificationKind))([ModificationKind](../ModificationKind.html) sourceChangeKind)`
Sets source change kind.
`void`
`[setTargetChangeKind](#setTargetChangeKind(com.nomagic.magicdraw.diff.ModificationKind))([ModificationKind](../ModificationKind.html) targetChangeKind)`
Sets target change kind.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ElementReportInfo
protected ElementReportInfo([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [ReportType](ReportType.html) reportType)
Constructs element report info.
Parameters:
`id` - id of the element.
`reportType` - type of the report.
 ============ METHOD DETAIL ========== 
Method Details
getElementName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getElementName()
Gets name of the element.
Returns:
name of the element.
setElementName
public void setElementName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementName)
Sets name of the element.
Parameters:
`elementName` - name to set.
getElementType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getElementType()
Gets type of the element.
Returns:
type of the element.
setElementType
public void setElementType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementType)
Sets element type.
Parameters:
`elementType` - sets type of the element.
getQualifiedName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getQualifiedName()
Gets element qualified name.
Returns:
element qualified name.
setQualifiedName
public void setQualifiedName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName)
Sets element qualified name.
Parameters:
`qualifiedName` - qualified name to set.
getSourceChangeKind
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSourceChangeKind()
Gets source change kind.
Returns:
source change kind.
setSourceChangeKind
public void setSourceChangeKind([ModificationKind](../ModificationKind.html) sourceChangeKind)
Sets source change kind.
Parameters:
`sourceChangeKind` - change kind to set.
getTargetChangeKind
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTargetChangeKind()
Gets target change kind.
Returns:
target change kind.
setTargetChangeKind
public void setTargetChangeKind([ModificationKind](../ModificationKind.html) targetChangeKind)
Sets target change kind.
Parameters:
`targetChangeKind` - change kind to set.
getProperties
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PropertyReportInfo](PropertyReportInfo.html)> getProperties()
Gets modified properties.
Returns:
modified properties.
setProperties
public void setProperties([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PropertyReportInfo](PropertyReportInfo.html)> properties)
Sets modified properties.
Parameters:
`properties` - properties to set.
isOfKind
public boolean isOfKind([ModificationKind](../ModificationKind.html) modificationKind)
Checks if modification is of a given type.
Parameters:
`modificationKind` - modification kind to compare with.
Returns:
true if modification is of a given type, false otherwise.
getModificationKindText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getModificationKindText([ModificationKind](../ModificationKind.html) modificationKind)
Gets representation text of a modification kind.
Parameters:
`modificationKind` - modification kind for which to get its text.
Returns:
text of a given modification kind.
getAddedTypeText
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAddedTypeText()
Gets text of the added modification kind.
Returns:
text of the added modification kind.
getModifiedTypeText
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getModifiedTypeText()
Gets text of the modified modification kind.
Returns:
text of the modified modification kind.
getRemovedTypeText
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRemovedTypeText()
Gets text of the removed modification kind.
Returns:
text of the removed modification kind.
getID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getID()
Gets element ID.
Returns:
ID of the element.
depth
public int depth()
Gets element depth in containment tree.
Returns:
element depth in containment tree.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff.report</a></div>
<h1 class="title" title="Class ElementReportInfo">Class ElementReportInfo</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.diff.report.ElementReportInfo</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ElementReportInfo</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Contains merge/diff report element information.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.magicdraw.diff.report.ReportType)">ElementReportInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a href="ReportType.html" title="enum class in com.nomagic.magicdraw.diff.report">ReportType</a> reportType)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs element report info.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#depth()">depth</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets element depth in containment tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAddedTypeText()">getAddedTypeText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets text of the added modification kind.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementName()">getElementName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets name of the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementType()">getElementType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets type of the element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets element ID.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getModificationKindText(com.nomagic.magicdraw.diff.ModificationKind)">getModificationKindText</a><wbr/>(<a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a> modificationKind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets representation text of a modification kind.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModifiedTypeText()">getModifiedTypeText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets text of the modified modification kind.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PropertyReportInfo.html" title="class in com.nomagic.magicdraw.diff.report">PropertyReportInfo</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperties()">getProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets modified properties.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getQualifiedName()">getQualifiedName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets element qualified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemovedTypeText()">getRemovedTypeText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets text of the removed modification kind.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceChangeKind()">getSourceChangeKind</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets source change kind.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetChangeKind()">getTargetChangeKind</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets target change kind.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isOfKind(com.nomagic.magicdraw.diff.ModificationKind)">isOfKind</a><wbr/>(<a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a> modificationKind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if modification is of a given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setElementName(java.lang.String)">setElementName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets name of the element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setElementType(java.lang.String)">setElementType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets element type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperties(java.util.List)">setProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PropertyReportInfo.html" title="class in com.nomagic.magicdraw.diff.report">PropertyReportInfo</a>&gt; properties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets modified properties.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setQualifiedName(java.lang.String)">setQualifiedName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets element qualified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSourceChangeKind(com.nomagic.magicdraw.diff.ModificationKind)">setSourceChangeKind</a><wbr/>(<a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a> sourceChangeKind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets source change kind.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTargetChangeKind(com.nomagic.magicdraw.diff.ModificationKind)">setTargetChangeKind</a><wbr/>(<a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a> targetChangeKind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets target change kind.</div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.magicdraw.diff.report.ReportType)">
<h3>ElementReportInfo</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">ElementReportInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a href="ReportType.html" title="enum class in com.nomagic.magicdraw.diff.report">ReportType</a> reportType)</span></div>
<div class="block">Constructs element report info.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - id of the element.</dd>
<dd><code>reportType</code> - type of the report.</dd>
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
<section class="detail" id="getElementName()">
<h3>getElementName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getElementName</span>()</div>
<div class="block">Gets name of the element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setElementName(java.lang.String)">
<h3>setElementName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setElementName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName)</span></div>
<div class="block">Sets name of the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementName</code> - name to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementType()">
<h3>getElementType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getElementType</span>()</div>
<div class="block">Gets type of the element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>type of the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setElementType(java.lang.String)">
<h3>setElementType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setElementType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementType)</span></div>
<div class="block">Sets element type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementType</code> - sets type of the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQualifiedName()">
<h3>getQualifiedName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQualifiedName</span>()</div>
<div class="block">Gets element qualified name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element qualified name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setQualifiedName(java.lang.String)">
<h3>setQualifiedName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setQualifiedName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</span></div>
<div class="block">Sets element qualified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>qualifiedName</code> - qualified name to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceChangeKind()">
<h3>getSourceChangeKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSourceChangeKind</span>()</div>
<div class="block">Gets source change kind.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>source change kind.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSourceChangeKind(com.nomagic.magicdraw.diff.ModificationKind)">
<h3>setSourceChangeKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSourceChangeKind</span><wbr/><span class="parameters">(<a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a> sourceChangeKind)</span></div>
<div class="block">Sets source change kind.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceChangeKind</code> - change kind to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetChangeKind()">
<h3>getTargetChangeKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTargetChangeKind</span>()</div>
<div class="block">Gets target change kind.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>target change kind.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTargetChangeKind(com.nomagic.magicdraw.diff.ModificationKind)">
<h3>setTargetChangeKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTargetChangeKind</span><wbr/><span class="parameters">(<a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a> targetChangeKind)</span></div>
<div class="block">Sets target change kind.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetChangeKind</code> - change kind to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperties()">
<h3>getProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PropertyReportInfo.html" title="class in com.nomagic.magicdraw.diff.report">PropertyReportInfo</a>&gt;</span> <span class="element-name">getProperties</span>()</div>
<div class="block">Gets modified properties.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>modified properties.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProperties(java.util.List)">
<h3>setProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PropertyReportInfo.html" title="class in com.nomagic.magicdraw.diff.report">PropertyReportInfo</a>&gt; properties)</span></div>
<div class="block">Sets modified properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - properties to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOfKind(com.nomagic.magicdraw.diff.ModificationKind)">
<h3>isOfKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOfKind</span><wbr/><span class="parameters">(<a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a> modificationKind)</span></div>
<div class="block">Checks if modification is of a given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modificationKind</code> - modification kind to compare with.</dd>
<dt>Returns:</dt>
<dd>true if modification is of a given type, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModificationKindText(com.nomagic.magicdraw.diff.ModificationKind)">
<h3>getModificationKindText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getModificationKindText</span><wbr/><span class="parameters">(<a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a> modificationKind)</span></div>
<div class="block">Gets representation text of a modification kind.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modificationKind</code> - modification kind for which to get its text.</dd>
<dt>Returns:</dt>
<dd>text of a given modification kind.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAddedTypeText()">
<h3>getAddedTypeText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAddedTypeText</span>()</div>
<div class="block">Gets text of the added modification kind.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>text of the added modification kind.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModifiedTypeText()">
<h3>getModifiedTypeText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getModifiedTypeText</span>()</div>
<div class="block">Gets text of the modified modification kind.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>text of the modified modification kind.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemovedTypeText()">
<h3>getRemovedTypeText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRemovedTypeText</span>()</div>
<div class="block">Gets text of the removed modification kind.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>text of the removed modification kind.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<div class="block">Gets element ID.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ID of the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="depth()">
<h3>depth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">depth</span>()</div>
<div class="block">Gets element depth in containment tree.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element depth in containment tree.</dd>
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
