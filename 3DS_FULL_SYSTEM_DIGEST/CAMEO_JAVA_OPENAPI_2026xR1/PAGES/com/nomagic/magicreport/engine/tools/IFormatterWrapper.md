# JAVA OPENAPI: IFormatterWrapper (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/tools/IFormatterWrapper.html
- source_path: `com/nomagic/magicreport/engine/tools/IFormatterWrapper.html`
- source_sha256: `ff9271c2a9fc3169806905a59d1ccfec5e1a8db405dbeec6d39c18f5188e45f8`
- captured_utc: `2026-07-14T16:46:12.739972+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.tools](package-summary.html)

## Interface IFormatterWrapper

@OpenApiAllpublic interfaceIFormatterWrapper

A wrapper for MagicReport formatter. This wrapper allow you to call internal method.

Since:
Feb 10, 2011

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBounds](#getBounds(com.nomagic.magicreport.engine.ITool.RetainedString))([ITool.RetainedString](../ITool.RetainedString.html) imageContent)`
Return the image bounds from image content.
`[Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getPaperBounds](#getPaperBounds(int))(int dpi)`
Return the size of paper bounds in pixel.
`[Image](../../Image.html)`
`[rotateImage](#rotateImage(com.nomagic.magicreport.Image,int))([Image](../../Image.html) image,
 int degrees)`
Rotates an image by a specific angle.
`[Image](../../Image.html)`
`[rotateImage](#rotateImage(com.nomagic.magicreport.Image,int,boolean))([Image](../../Image.html) image,
 int degrees,
 boolean bestQualityOrVecter)`
Rotates an image by a specific angle.
`[Image](../../Image.html)`
`[scale](#scale(com.nomagic.magicreport.Image,double,double))([Image](../../Image.html) image,
 double sx,
 double sy)`
Return the content of transformed image.

============ METHOD DETAIL ========== 
Method Details
rotateImage
[Image](../../Image.html) rotateImage([Image](../../Image.html) image,
 int degrees,
 boolean bestQualityOrVecter)
Rotates an image by a specific angle.
Parameters:
`image` - the image to be rotated
`degrees` - the angle of rotation can be positive or negative
`bestQualityOrVecter` - to check best quality or vector image
Returns:
the rotated image
rotateImage
[Image](../../Image.html) rotateImage([Image](../../Image.html) image,
 int degrees)
Rotates an image by a specific angle.
Parameters:
`image` - the image to be rotated
`degrees` - the angle of rotation can be positive or negative
Returns:
the rotated image
scale
[Image](../../Image.html) scale([Image](../../Image.html) image,
 double sx,
 double sy)
Return the content of transformed image. Subsequent rendering is resized according to the specified scaling
 factors relative to the previous scaling.
Parameters:
`image` - report image
`sx` - the amount by which X coordinates in subsequent rendering operations are multiplied relative to
 previous rendering operations.
`sy` - the amount by which Y coordinates in subsequent rendering operations are multiplied relative to
 previous rendering operations.
Returns:
the image after scaling transformation in content format
getBounds
[Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) getBounds([ITool.RetainedString](../ITool.RetainedString.html) imageContent)
Return the image bounds from image content.
Parameters:
`imageContent` - content of image
Returns:
the image bounds
getPaperBounds
[Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) getPaperBounds(int dpi)
Return the size of paper bounds in pixel.
Parameters:
`dpi` - DPI value
Returns:
the size of paper bounds.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.tools</a></div>
<h1 class="title" title="Interface IFormatterWrapper">Interface IFormatterWrapper</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IFormatterWrapper</span></div>
<div class="block">A wrapper for MagicReport formatter. This wrapper allow you to call internal method.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Feb 10, 2011</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBounds(com.nomagic.magicreport.engine.ITool.RetainedString)">getBounds</a><wbr/>(<a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a> imageContent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the image bounds from image content.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPaperBounds(int)">getPaperBounds</a><wbr/>(int dpi)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the size of paper bounds in pixel.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#rotateImage(com.nomagic.magicreport.Image,int)">rotateImage</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int degrees)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Rotates an image by a specific angle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#rotateImage(com.nomagic.magicreport.Image,int,boolean)">rotateImage</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int degrees,
 boolean bestQualityOrVecter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Rotates an image by a specific angle.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#scale(com.nomagic.magicreport.Image,double,double)">scale</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 double sx,
 double sy)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the content of transformed image.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="rotateImage(com.nomagic.magicreport.Image,int,boolean)">
<h3>rotateImage</h3>
<div class="member-signature"><span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">rotateImage</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int degrees,
 boolean bestQualityOrVecter)</span></div>
<div class="block">Rotates an image by a specific angle.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - the image to be rotated</dd>
<dd><code>degrees</code> - the angle of rotation can be positive or negative</dd>
<dd><code>bestQualityOrVecter</code> - to check best quality or vector image</dd>
<dt>Returns:</dt>
<dd>the rotated image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="rotateImage(com.nomagic.magicreport.Image,int)">
<h3>rotateImage</h3>
<div class="member-signature"><span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">rotateImage</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int degrees)</span></div>
<div class="block">Rotates an image by a specific angle.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - the image to be rotated</dd>
<dd><code>degrees</code> - the angle of rotation can be positive or negative</dd>
<dt>Returns:</dt>
<dd>the rotated image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scale(com.nomagic.magicreport.Image,double,double)">
<h3>scale</h3>
<div class="member-signature"><span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">scale</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 double sx,
 double sy)</span></div>
<div class="block">Return the content of transformed image. Subsequent rendering is resized according to the specified scaling
 factors relative to the previous scaling.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - report image</dd>
<dd><code>sx</code> - the amount by which X coordinates in subsequent rendering operations are multiplied relative to
           previous rendering operations.</dd>
<dd><code>sy</code> - the amount by which Y coordinates in subsequent rendering operations are multiplied relative to
           previous rendering operations.</dd>
<dt>Returns:</dt>
<dd>the image after scaling transformation in content format</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBounds(com.nomagic.magicreport.engine.ITool.RetainedString)">
<h3>getBounds</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBounds</span><wbr/><span class="parameters">(<a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a> imageContent)</span></div>
<div class="block">Return the image bounds from image content.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>imageContent</code> - content of image</dd>
<dt>Returns:</dt>
<dd>the image bounds</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPaperBounds(int)">
<h3>getPaperBounds</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getPaperBounds</span><wbr/><span class="parameters">(int dpi)</span></div>
<div class="block">Return the size of paper bounds in pixel.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dpi</code> - DPI value</dd>
<dt>Returns:</dt>
<dd>the size of paper bounds.</dd>
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
