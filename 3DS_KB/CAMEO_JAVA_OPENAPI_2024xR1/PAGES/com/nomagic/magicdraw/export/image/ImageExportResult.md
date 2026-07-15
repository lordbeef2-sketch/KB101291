# JAVA OPENAPI: ImageExportResult (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/export/image/ImageExportResult.html
- source_path: `com/nomagic/magicdraw/export/image/ImageExportResult.html`
- source_sha256: `8158b7e0f3e1338e9fee6cd810c5481bc7beadf69fe07f5a140dc0affa240130`
- captured_utc: `2026-07-14T16:51:21.911216+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.export.image](package-summary.html)

## Class ImageExportResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.export.image.ImageExportResult

@OpenApiAllpublic classImageExportResult
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Class providing image export result.

 Diagram: Diagram canvas:
 +-------------------------+
 | HEADER |
 +-------------------------+ +--------------------------+
 | | | +----------------------| <-- canvas bound for exporting when shapes are not close to border
 | +-------------+ | | | |
 | | | | | | +-------------+ |
 | | A | | | | | AA | |
 | | | | | | | | |
 | +-------------+ | | | +-------------+ |
 | | | | |
 +-------------------------+ +--------------------------+
 | FOOTER |
 +-------------------------+


 Exported image with banners:
 +--
 | +-------------+
 | | HEADER |
 | +-------------+
 | | |
 B | | C |
 | | |
 | +-------------+
 | | FOOTER |
 | +-------------+
 +--

 Exported image without banners:
 +--
 | +-------------+
 | | |
 B | | C |
 | | |
 | +-------------+
 +--

 Failed export image:
 +-
 | +----------------+
 B | | Error message |
 | +----------------+
 +-

 A - `exportedAreaRect` Start point and dimension of exported diagram area.
 In case of failed export (over time/dimension limits, error) rectangle will be empty as no part of diagram was exported
 AA - `exportedCanvasAreaRect` Start point and dimension of exported diagram canvas area.
 Shape bounds returned from `SymbolDiagramElementsLocator.getLocatedElements()` are offset from 0,0 point if no shape is close enough to border,
 this makes it harder to locate them on image without this value.
 In case of failed export (over time/dimension limits, error) rectangle will be empty as no part of diagram was exported
 B - `imageRect` Rectangle of exported image.
 Contains `imageWithoutBannersRect` and banners, or is same as `imageWithoutBannersRect` if banners are not exported
 Might also be just size of failed export image
 C - `imageWithoutBannersRect` Rectangle within exported image containing `exportedAreaRect` (same height and width, only starting coordinates are different)
 In case of failed export (over time/dimension limits, error) rectangle will be empty as it does not exist in exported image
 A and C only differs in starting coordinate since one is in diagram coordinates, other in exported image

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static enum`
`[ImageExportResult.ImageExportStatus](ImageExportResult.ImageExportStatus.html)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ImageExportResult](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getExportedAreaRect](#getExportedAreaRect())()`

`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getExportedCanvasAreaRect](#getExportedCanvasAreaRect())()`

`[ImageExportResult.ImageExportStatus](ImageExportResult.ImageExportStatus.html)`
`[getExportStatus](#getExportStatus())()`

`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getImageRect](#getImageRect())()`

`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getImageWithoutBannersRect](#getImageWithoutBannersRect())()`

`boolean`
`[isDiagramNotExported](#isDiagramNotExported())()`

`boolean`
`[isExportSuccessful](#isExportSuccessful())()`

`void`
`[setExportedAreaRect](#setExportedAreaRect(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) exportedAreaRect)`

`void`
`[setExportedCanvasAreaRect](#setExportedCanvasAreaRect(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) exportedCanvasAreaRect)`

`void`
`[setExportStatus](#setExportStatus(com.nomagic.magicdraw.export.image.ImageExportResult.ImageExportStatus))([ImageExportResult.ImageExportStatus](ImageExportResult.ImageExportStatus.html) exportStatus)`

`void`
`[setImageRect](#setImageRect(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) imageRect)`

`void`
`[setImageWithoutBannersRect](#setImageWithoutBannersRect(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) imageWithoutBannersRect)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ImageExportResult
public ImageExportResult()
 ============ METHOD DETAIL ========== 
Method Details
isExportSuccessful
public boolean isExportSuccessful()
isDiagramNotExported
public boolean isDiagramNotExported()
Returns:
true if diagram was not exported due to exceeding limits or some error
getExportStatus
public [ImageExportResult.ImageExportStatus](ImageExportResult.ImageExportStatus.html) getExportStatus()
setExportStatus
public void setExportStatus([ImageExportResult.ImageExportStatus](ImageExportResult.ImageExportStatus.html) exportStatus)
getExportedAreaRect
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getExportedAreaRect()
setExportedAreaRect
public void setExportedAreaRect([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) exportedAreaRect)
getExportedCanvasAreaRect
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getExportedCanvasAreaRect()
setExportedCanvasAreaRect
public void setExportedCanvasAreaRect([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) exportedCanvasAreaRect)
getImageWithoutBannersRect
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getImageWithoutBannersRect()
setImageWithoutBannersRect
public void setImageWithoutBannersRect([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) imageWithoutBannersRect)
getImageRect
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getImageRect()
setImageRect
public void setImageRect([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) imageRect)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.export.image</a></div>
<h1 class="title" title="Class ImageExportResult">Class ImageExportResult</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.export.image.ImageExportResult</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ImageExportResult</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Class providing image export result.

 <pre>
 Diagram:                         Diagram canvas:
   +-------------------------+
   |  HEADER                 |
   +-------------------------+   +--------------------------+
   |                         |   |   +----------------------| &lt;-- canvas bound for exporting when shapes are not close to border
   |       +-------------+   |   |   |                      |
   |       |             |   |   |   |    +-------------+   |
   |       |      A      |   |   |   |    |     AA      |   |
   |       |             |   |   |   |    |             |   |
   |       +-------------+   |   |   |    +-------------+   |
   |                         |   |   |                      |
   +-------------------------+   +--------------------------+
   |  FOOTER                 |
   +-------------------------+


 Exported image with banners:
       +--
       |    +-------------+
       |    |  HEADER     |
       |    +-------------+
       |    |             |
    B  |    |      C      |
       |    |             |
       |    +-------------+
       |    |  FOOTER     |
       |    +-------------+
       +--

 Exported image without banners:
       +--
       |    +-------------+
       |    |             |
    B  |    |      C      |
       |    |             |
       |    +-------------+
       +--

 Failed export image:
       +-
       |    +----------------+
     B |    | Error message  |
       |    +----------------+
       +-

 A - <code>exportedAreaRect</code> Start point and dimension of exported diagram area.
            In case of failed export (over time/dimension limits, error) rectangle will be empty as no part of diagram was exported
 AA - <code>exportedCanvasAreaRect</code> Start point and dimension of exported diagram canvas area.
            Shape bounds returned from <code>SymbolDiagramElementsLocator.getLocatedElements()</code> are offset from 0,0 point if no shape is close enough to border,
            this makes it harder to locate them on image without this value.
            In case of failed export (over time/dimension limits, error) rectangle will be empty as no part of diagram was exported
 B - <code>imageRect</code> Rectangle of exported image.
            Contains <code>imageWithoutBannersRect</code> and banners, or is same as <code>imageWithoutBannersRect</code> if banners are not exported
            Might also be just size of failed export image
 C - <code>imageWithoutBannersRect</code> Rectangle within exported image containing <code>exportedAreaRect</code> (same height and width, only starting coordinates are different)
            In case of failed export (over time/dimension limits, error) rectangle will be empty as it does not exist in exported image
 A and C only differs in starting coordinate since one is in diagram coordinates, other in exported image
 </pre></div>
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
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ImageExportResult.ImageExportStatus.html" title="enum class in com.nomagic.magicdraw.export.image">ImageExportResult.ImageExportStatus</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ImageExportResult</a>()</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExportedAreaRect()">getExportedAreaRect</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExportedCanvasAreaRect()">getExportedCanvasAreaRect</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ImageExportResult.ImageExportStatus.html" title="enum class in com.nomagic.magicdraw.export.image">ImageExportResult.ImageExportStatus</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExportStatus()">getExportStatus</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageRect()">getImageRect</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageWithoutBannersRect()">getImageWithoutBannersRect</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDiagramNotExported()">isDiagramNotExported</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isExportSuccessful()">isExportSuccessful</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExportedAreaRect(java.awt.Rectangle)">setExportedAreaRect</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> exportedAreaRect)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExportedCanvasAreaRect(java.awt.Rectangle)">setExportedCanvasAreaRect</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> exportedCanvasAreaRect)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExportStatus(com.nomagic.magicdraw.export.image.ImageExportResult.ImageExportStatus)">setExportStatus</a><wbr/>(<a href="ImageExportResult.ImageExportStatus.html" title="enum class in com.nomagic.magicdraw.export.image">ImageExportResult.ImageExportStatus</a> exportStatus)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setImageRect(java.awt.Rectangle)">setImageRect</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> imageRect)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setImageWithoutBannersRect(java.awt.Rectangle)">setImageWithoutBannersRect</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> imageWithoutBannersRect)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<h3>ImageExportResult</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ImageExportResult</span>()</div>
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
<section class="detail" id="isExportSuccessful()">
<h3>isExportSuccessful</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExportSuccessful</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isDiagramNotExported()">
<h3>isDiagramNotExported</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDiagramNotExported</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if diagram was not exported due to exceeding limits or some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExportStatus()">
<h3>getExportStatus</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ImageExportResult.ImageExportStatus.html" title="enum class in com.nomagic.magicdraw.export.image">ImageExportResult.ImageExportStatus</a></span> <span class="element-name">getExportStatus</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setExportStatus(com.nomagic.magicdraw.export.image.ImageExportResult.ImageExportStatus)">
<h3>setExportStatus</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExportStatus</span><wbr/><span class="parameters">(<a href="ImageExportResult.ImageExportStatus.html" title="enum class in com.nomagic.magicdraw.export.image">ImageExportResult.ImageExportStatus</a> exportStatus)</span></div>
</section>
</li>
<li>
<section class="detail" id="getExportedAreaRect()">
<h3>getExportedAreaRect</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getExportedAreaRect</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setExportedAreaRect(java.awt.Rectangle)">
<h3>setExportedAreaRect</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExportedAreaRect</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> exportedAreaRect)</span></div>
</section>
</li>
<li>
<section class="detail" id="getExportedCanvasAreaRect()">
<h3>getExportedCanvasAreaRect</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getExportedCanvasAreaRect</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setExportedCanvasAreaRect(java.awt.Rectangle)">
<h3>setExportedCanvasAreaRect</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExportedCanvasAreaRect</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> exportedCanvasAreaRect)</span></div>
</section>
</li>
<li>
<section class="detail" id="getImageWithoutBannersRect()">
<h3>getImageWithoutBannersRect</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getImageWithoutBannersRect</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setImageWithoutBannersRect(java.awt.Rectangle)">
<h3>setImageWithoutBannersRect</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImageWithoutBannersRect</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> imageWithoutBannersRect)</span></div>
</section>
</li>
<li>
<section class="detail" id="getImageRect()">
<h3>getImageRect</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getImageRect</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setImageRect(java.awt.Rectangle)">
<h3>setImageRect</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImageRect</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> imageRect)</span></div>
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
