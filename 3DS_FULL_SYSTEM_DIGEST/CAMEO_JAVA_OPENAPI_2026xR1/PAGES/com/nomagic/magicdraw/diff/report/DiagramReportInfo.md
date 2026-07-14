# JAVA OPENAPI: DiagramReportInfo (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/diff/report/DiagramReportInfo.html
- source_path: `com/nomagic/magicdraw/diff/report/DiagramReportInfo.html`
- source_sha256: `989e301282e74b37f5c6c7a7544c7d28abb7c4dad1d49a8ce7eb24dfe14e2b55`
- captured_utc: `2026-07-14T16:45:33.733451+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff.report](package-summary.html)

## Class DiagramReportInfo

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.diff.report.DiagramReportInfo

@OpenApiAllpublic classDiagramReportInfo
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Contains merge/diff report diagram information.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramReportInfo](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[DiagramData](../DiagramData.html)`
`[getAncestorDiagramData](#getAncestorDiagramData())()`
Gets ancestor diagram data.
`[Image](../../../magicreport/Image.html)`
`[getAncestorDiagramImage](#getAncestorDiagramImage())()`
Gets ancestor diagram image.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getCreatedBy](#getCreatedBy())()`
Gets author which created the diagram.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getCreationDate](#getCreationDate())()`
Gets diagram creation date.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDiagramElementID](#getDiagramElementID())()`
Gets diagram element id.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDiagramID](#getDiagramID())()`
Gets diagram presentation element id.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDiagramName](#getDiagramName())()`
Gets name of the diagram.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDiagramType](#getDiagramType())()`
Gets type of the diagram.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getModificationDate](#getModificationDate())()`
Gets last diagram modification date.
`[ModificationKind](../ModificationKind.html)`
`[getModificationKind](#getModificationKind())()`
Gets diagram modification kind.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getModifiedBy](#getModifiedBy())()`
Gets author which last modified the diagram.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getNoAncestorImage](#getNoAncestorImage())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getNoSourceImage](#getNoSourceImage())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getNoTargetImage](#getNoTargetImage())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getQualifiedName](#getQualifiedName())()`
Gets diagram qualified name.
`[DiagramData](../DiagramData.html)`
`[getSourceDiagramData](#getSourceDiagramData())()`
Gets source diagram data.
`[Image](../../../magicreport/Image.html)`
`[getSourceDiagramImage](#getSourceDiagramImage())()`
Gets source diagram image.
`[DiagramData](../DiagramData.html)`
`[getTargetDiagramData](#getTargetDiagramData())()`
Gets target diagram data.
`[Image](../../../magicreport/Image.html)`
`[getTargetDiagramImage](#getTargetDiagramImage())()`
Gets target diagram image.
`void`
`[setAncestorDiagramData](#setAncestorDiagramData(com.nomagic.magicdraw.diff.DiagramData))([DiagramData](../DiagramData.html) ancestorDiagramData)`
Sets ancestor diagram data.
`void`
`[setAncestorDiagramImage](#setAncestorDiagramImage(com.nomagic.magicreport.Image))([Image](../../../magicreport/Image.html) ancestorDiagramImage)`
Sets ancestor diagram image.
`void`
`[setModificationKind](#setModificationKind(com.nomagic.magicdraw.diff.ModificationKind))([ModificationKind](../ModificationKind.html) modificationKind)`
Sets diagram modification kind.
`protected void`
`[setNoAncestorImageText](#setNoAncestorImageText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) noAncestorImageText)`

`protected void`
`[setNoSourceImageText](#setNoSourceImageText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) noSourceImageText)`

`protected void`
`[setNoTargetImageText](#setNoTargetImageText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) noTargetImageText)`

`void`
`[setSourceDiagramData](#setSourceDiagramData(com.nomagic.magicdraw.diff.DiagramData))([DiagramData](../DiagramData.html) sourceDiagramData)`
Sets source diagram data.
`void`
`[setSourceDiagramImage](#setSourceDiagramImage(com.nomagic.magicreport.Image))([Image](../../../magicreport/Image.html) sourceDiagramImage)`
Sets source diagram image.
`void`
`[setTargetDiagramData](#setTargetDiagramData(com.nomagic.magicdraw.diff.DiagramData))([DiagramData](../DiagramData.html) targetDiagramData)`
Sets target diagram data.
`void`
`[setTargetDiagramImage](#setTargetDiagramImage(com.nomagic.magicreport.Image))([Image](../../../magicreport/Image.html) targetDiagramImage)`
Sets target diagram image.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramReportInfo
public DiagramReportInfo()
 ============ METHOD DETAIL ========== 
Method Details
getDiagramName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDiagramName()
Gets name of the diagram.
Returns:
name of the diagram.
getQualifiedName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getQualifiedName()
Gets diagram qualified name.
Returns:
diagram qualified name.
getDiagramType
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDiagramType()
Gets type of the diagram.
Returns:
type of the diagram.
getAncestorDiagramImage
public [Image](../../../magicreport/Image.html) getAncestorDiagramImage()
Gets ancestor diagram image.
Returns:
ancestor diagram image.
setAncestorDiagramImage
public void setAncestorDiagramImage([Image](../../../magicreport/Image.html) ancestorDiagramImage)
Sets ancestor diagram image.
Parameters:
`ancestorDiagramImage` - image to set.
getTargetDiagramImage
public [Image](../../../magicreport/Image.html) getTargetDiagramImage()
Gets target diagram image.
Returns:
target diagram image.
setTargetDiagramImage
public void setTargetDiagramImage([Image](../../../magicreport/Image.html) targetDiagramImage)
Sets target diagram image.
Parameters:
`targetDiagramImage` - image to set.
getSourceDiagramImage
public [Image](../../../magicreport/Image.html) getSourceDiagramImage()
Gets source diagram image.
Returns:
source diagram image.
setSourceDiagramImage
public void setSourceDiagramImage([Image](../../../magicreport/Image.html) sourceDiagramImage)
Sets source diagram image.
Parameters:
`sourceDiagramImage` - image to set.
setAncestorDiagramData
public void setAncestorDiagramData([DiagramData](../DiagramData.html) ancestorDiagramData)
Sets ancestor diagram data.
Parameters:
`ancestorDiagramData` - data to set.
setTargetDiagramData
public void setTargetDiagramData([DiagramData](../DiagramData.html) targetDiagramData)
Sets target diagram data.
Parameters:
`targetDiagramData` - data to set.
setSourceDiagramData
public void setSourceDiagramData([DiagramData](../DiagramData.html) sourceDiagramData)
Sets source diagram data.
Parameters:
`sourceDiagramData` - data to set.
getDiagramID
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDiagramID()
Gets diagram presentation element id.
Returns:
diagram presentation element id.
getDiagramElementID
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDiagramElementID()
Gets diagram element id.
Returns:
diagram element id.
getAncestorDiagramData
public [DiagramData](../DiagramData.html) getAncestorDiagramData()
Gets ancestor diagram data.
Returns:
ancestor diagram data.
getTargetDiagramData
public [DiagramData](../DiagramData.html) getTargetDiagramData()
Gets target diagram data.
Returns:
target diagram data.
getSourceDiagramData
public [DiagramData](../DiagramData.html) getSourceDiagramData()
Gets source diagram data.
Returns:
source diagram data.
getCreatedBy
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getCreatedBy()
Gets author which created the diagram.
Returns:
author which created the diagram.
getCreationDate
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getCreationDate()
Gets diagram creation date.
Returns:
diagram creation date.
getModifiedBy
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getModifiedBy()
Gets author which last modified the diagram.
Returns:
author which last modified the diagram.
getModificationDate
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getModificationDate()
Gets last diagram modification date.
Returns:
last diagram modification date.
getModificationKind
public [ModificationKind](../ModificationKind.html) getModificationKind()
Gets diagram modification kind.
Returns:
diagram modification kind.
setModificationKind
public void setModificationKind([ModificationKind](../ModificationKind.html) modificationKind)
Sets diagram modification kind.
Parameters:
`modificationKind` - modification kind to set.
getNoAncestorImage
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getNoAncestorImage()
getNoSourceImage
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getNoSourceImage()
getNoTargetImage
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getNoTargetImage()
setNoSourceImageText
protected void setNoSourceImageText([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) noSourceImageText)
setNoTargetImageText
protected void setNoTargetImageText([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) noTargetImageText)
setNoAncestorImageText
protected void setNoAncestorImageText([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) noAncestorImageText)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff.report</a></div>
<h1 class="title" title="Class DiagramReportInfo">Class DiagramReportInfo</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.diff.report.DiagramReportInfo</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramReportInfo</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Contains merge/diff report diagram information.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DiagramReportInfo</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAncestorDiagramData()">getAncestorDiagramData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets ancestor diagram data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../magicreport/Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAncestorDiagramImage()">getAncestorDiagramImage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets ancestor diagram image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreatedBy()">getCreatedBy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets author which created the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreationDate()">getCreationDate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets diagram creation date.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramElementID()">getDiagramElementID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets diagram element id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramID()">getDiagramID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets diagram presentation element id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramName()">getDiagramName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets name of the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramType()">getDiagramType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets type of the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModificationDate()">getModificationDate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets last diagram modification date.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModificationKind()">getModificationKind</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets diagram modification kind.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModifiedBy()">getModifiedBy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets author which last modified the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNoAncestorImage()">getNoAncestorImage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNoSourceImage()">getNoSourceImage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNoTargetImage()">getNoTargetImage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getQualifiedName()">getQualifiedName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets diagram qualified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceDiagramData()">getSourceDiagramData</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets source diagram data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../magicreport/Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceDiagramImage()">getSourceDiagramImage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets source diagram image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetDiagramData()">getTargetDiagramData</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets target diagram data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../magicreport/Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetDiagramImage()">getTargetDiagramImage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets target diagram image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAncestorDiagramData(com.nomagic.magicdraw.diff.DiagramData)">setAncestorDiagramData</a><wbr/>(<a href="../DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a> ancestorDiagramData)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets ancestor diagram data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAncestorDiagramImage(com.nomagic.magicreport.Image)">setAncestorDiagramImage</a><wbr/>(<a href="../../../magicreport/Image.html" title="class in com.nomagic.magicreport">Image</a> ancestorDiagramImage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets ancestor diagram image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setModificationKind(com.nomagic.magicdraw.diff.ModificationKind)">setModificationKind</a><wbr/>(<a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a> modificationKind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets diagram modification kind.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNoAncestorImageText(java.lang.String)">setNoAncestorImageText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noAncestorImageText)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNoSourceImageText(java.lang.String)">setNoSourceImageText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noSourceImageText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNoTargetImageText(java.lang.String)">setNoTargetImageText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noTargetImageText)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSourceDiagramData(com.nomagic.magicdraw.diff.DiagramData)">setSourceDiagramData</a><wbr/>(<a href="../DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a> sourceDiagramData)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets source diagram data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSourceDiagramImage(com.nomagic.magicreport.Image)">setSourceDiagramImage</a><wbr/>(<a href="../../../magicreport/Image.html" title="class in com.nomagic.magicreport">Image</a> sourceDiagramImage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets source diagram image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTargetDiagramData(com.nomagic.magicdraw.diff.DiagramData)">setTargetDiagramData</a><wbr/>(<a href="../DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a> targetDiagramData)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets target diagram data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTargetDiagramImage(com.nomagic.magicreport.Image)">setTargetDiagramImage</a><wbr/>(<a href="../../../magicreport/Image.html" title="class in com.nomagic.magicreport">Image</a> targetDiagramImage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets target diagram image.</div>
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
<h3>DiagramReportInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramReportInfo</span>()</div>
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
<section class="detail" id="getDiagramName()">
<h3>getDiagramName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramName</span>()</div>
<div class="block">Gets name of the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of the diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQualifiedName()">
<h3>getQualifiedName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQualifiedName</span>()</div>
<div class="block">Gets diagram qualified name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram qualified name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramType()">
<h3>getDiagramType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramType</span>()</div>
<div class="block">Gets type of the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>type of the diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAncestorDiagramImage()">
<h3>getAncestorDiagramImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../magicreport/Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">getAncestorDiagramImage</span>()</div>
<div class="block">Gets ancestor diagram image.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ancestor diagram image.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAncestorDiagramImage(com.nomagic.magicreport.Image)">
<h3>setAncestorDiagramImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAncestorDiagramImage</span><wbr/><span class="parameters">(<a href="../../../magicreport/Image.html" title="class in com.nomagic.magicreport">Image</a> ancestorDiagramImage)</span></div>
<div class="block">Sets ancestor diagram image.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ancestorDiagramImage</code> - image to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetDiagramImage()">
<h3>getTargetDiagramImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../magicreport/Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">getTargetDiagramImage</span>()</div>
<div class="block">Gets target diagram image.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>target diagram image.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTargetDiagramImage(com.nomagic.magicreport.Image)">
<h3>setTargetDiagramImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTargetDiagramImage</span><wbr/><span class="parameters">(<a href="../../../magicreport/Image.html" title="class in com.nomagic.magicreport">Image</a> targetDiagramImage)</span></div>
<div class="block">Sets target diagram image.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetDiagramImage</code> - image to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceDiagramImage()">
<h3>getSourceDiagramImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../magicreport/Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">getSourceDiagramImage</span>()</div>
<div class="block">Gets source diagram image.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>source diagram image.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSourceDiagramImage(com.nomagic.magicreport.Image)">
<h3>setSourceDiagramImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSourceDiagramImage</span><wbr/><span class="parameters">(<a href="../../../magicreport/Image.html" title="class in com.nomagic.magicreport">Image</a> sourceDiagramImage)</span></div>
<div class="block">Sets source diagram image.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceDiagramImage</code> - image to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAncestorDiagramData(com.nomagic.magicdraw.diff.DiagramData)">
<h3>setAncestorDiagramData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAncestorDiagramData</span><wbr/><span class="parameters">(<a href="../DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a> ancestorDiagramData)</span></div>
<div class="block">Sets ancestor diagram data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ancestorDiagramData</code> - data to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTargetDiagramData(com.nomagic.magicdraw.diff.DiagramData)">
<h3>setTargetDiagramData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTargetDiagramData</span><wbr/><span class="parameters">(<a href="../DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a> targetDiagramData)</span></div>
<div class="block">Sets target diagram data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetDiagramData</code> - data to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSourceDiagramData(com.nomagic.magicdraw.diff.DiagramData)">
<h3>setSourceDiagramData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSourceDiagramData</span><wbr/><span class="parameters">(<a href="../DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a> sourceDiagramData)</span></div>
<div class="block">Sets source diagram data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceDiagramData</code> - data to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramID()">
<h3>getDiagramID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramID</span>()</div>
<div class="block">Gets diagram presentation element id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram presentation element id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramElementID()">
<h3>getDiagramElementID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramElementID</span>()</div>
<div class="block">Gets diagram element id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram element id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAncestorDiagramData()">
<h3>getAncestorDiagramData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a></span> <span class="element-name">getAncestorDiagramData</span>()</div>
<div class="block">Gets ancestor diagram data.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ancestor diagram data.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetDiagramData()">
<h3>getTargetDiagramData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a></span> <span class="element-name">getTargetDiagramData</span>()</div>
<div class="block">Gets target diagram data.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>target diagram data.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceDiagramData()">
<h3>getSourceDiagramData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a></span> <span class="element-name">getSourceDiagramData</span>()</div>
<div class="block">Gets source diagram data.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>source diagram data.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreatedBy()">
<h3>getCreatedBy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCreatedBy</span>()</div>
<div class="block">Gets author which created the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>author which created the diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreationDate()">
<h3>getCreationDate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCreationDate</span>()</div>
<div class="block">Gets diagram creation date.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram creation date.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModifiedBy()">
<h3>getModifiedBy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getModifiedBy</span>()</div>
<div class="block">Gets author which last modified the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>author which last modified the diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModificationDate()">
<h3>getModificationDate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getModificationDate</span>()</div>
<div class="block">Gets last diagram modification date.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>last diagram modification date.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModificationKind()">
<h3>getModificationKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a></span> <span class="element-name">getModificationKind</span>()</div>
<div class="block">Gets diagram modification kind.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram modification kind.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setModificationKind(com.nomagic.magicdraw.diff.ModificationKind)">
<h3>setModificationKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setModificationKind</span><wbr/><span class="parameters">(<a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a> modificationKind)</span></div>
<div class="block">Sets diagram modification kind.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modificationKind</code> - modification kind to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNoAncestorImage()">
<h3>getNoAncestorImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getNoAncestorImage</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNoSourceImage()">
<h3>getNoSourceImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getNoSourceImage</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNoTargetImage()">
<h3>getNoTargetImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getNoTargetImage</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setNoSourceImageText(java.lang.String)">
<h3>setNoSourceImageText</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setNoSourceImageText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noSourceImageText)</span></div>
</section>
</li>
<li>
<section class="detail" id="setNoTargetImageText(java.lang.String)">
<h3>setNoTargetImageText</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setNoTargetImageText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noTargetImageText)</span></div>
</section>
</li>
<li>
<section class="detail" id="setNoAncestorImageText(java.lang.String)">
<h3>setNoAncestorImageText</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setNoAncestorImageText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noAncestorImageText)</span></div>
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
