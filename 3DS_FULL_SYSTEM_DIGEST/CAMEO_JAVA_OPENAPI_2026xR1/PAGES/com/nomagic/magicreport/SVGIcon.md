# JAVA OPENAPI: SVGIcon (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/SVGIcon.html
- source_path: `com/nomagic/magicreport/SVGIcon.html`
- source_sha256: `f8d77b5184add6214934ab82a0297e4932863a0eedf9049c4864aacf721b7ca4`
- captured_utc: `2026-07-14T16:46:11.523955+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport](package-summary.html)

## Class SVGIcon

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicreport.Image](Image.html)
com.nomagic.magicreport.SVGIcon

All Implemented Interfaces:
`[IObserverMessage](engine/IObserverMessage.html)`, `[IVariable](IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classSVGIcon
extends [Image](Image.html)

A bean represent SVG icon.

Since:
Mar 22, 2016
See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.magicreport.SVGIcon)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicreport.[Image](Image.html)
`[FIT_PAPER](Image.html#FIT_PAPER), [FORCE_ROTATE](Image.html#FORCE_ROTATE), [FORCE_ROTATE_LEFT](Image.html#FORCE_ROTATE_LEFT), [FORCE_ROTATE_RIGHT](Image.html#FORCE_ROTATE_RIGHT), [IMAGE_TYPE_ICON](Image.html#IMAGE_TYPE_ICON), [IMAGE_TYPE_IMAGE](Image.html#IMAGE_TYPE_IMAGE), [LARGE_ONLY](Image.html#LARGE_ONLY), [MAINTAIN_RATIO](Image.html#MAINTAIN_RATIO), [ROTATE_LEFT](Image.html#ROTATE_LEFT), [ROTATE_RIGHT](Image.html#ROTATE_RIGHT), [TRUE_TRANSFORM](Image.html#TRUE_TRANSFORM)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SVGIcon](#%3Cinit%3E(java.lang.String,java.awt.image.BufferedImage,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html) data,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageFormat,
 boolean disposeAfterUse)`

`[SVGIcon](#%3Cinit%3E(java.lang.String,java.io.File,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) imageFile,
 boolean disposeAfterUse)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[ensureOriginal](#ensureOriginal())()`

`void`
`[flush](#flush(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) track)`
Flush current buffered image from [`Image.getData()`](Image.html#getData()) into file stream.
`org.apache.batik.svggen.SVGGraphics2D`
`[getSvgGenerator](#getSvgGenerator())()`

`[BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html)`
`[readData](#readData())()`
Read a buffered image from this instance.
`void`
`[rotate](#rotate(boolean))(boolean clockwise)`
Rotate image in clockwise or anti-clockwise.
`void`
`[setSvgGenerator](#setSvgGenerator(org.apache.batik.svggen.SVGGraphics2D))(org.apache.batik.svggen.SVGGraphics2D svgGenerator)`
Methods inherited from class com.nomagic.magicreport.[Image](Image.html)
`[clone](Image.html#clone()), [createOriginal](Image.html#createOriginal()), [dispose](Image.html#dispose()), [equals](Image.html#equals(java.lang.Object)), [flush](Image.html#flush()), [getBounds](Image.html#getBounds()), [getData](Image.html#getData()), [getDpi](Image.html#getDpi()), [getHeight](Image.html#getHeight()), [getId](Image.html#getId()), [getImageFile](Image.html#getImageFile()), [getImageFormat](Image.html#getImageFormat()), [getImageFormatToWrite](Image.html#getImageFormatToWrite()), [getImageType](Image.html#getImageType()), [getName](Image.html#getName()), [getOriginalBounds](Image.html#getOriginalBounds()), [getOriginalHeight](Image.html#getOriginalHeight()), [getOriginalImageFile](Image.html#getOriginalImageFile()), [getOriginalImageFormat](Image.html#getOriginalImageFormat()), [getOriginalWidth](Image.html#getOriginalWidth()), [getProperties](Image.html#getProperties()), [getProperty](Image.html#getProperty(java.lang.String)), [getSize](Image.html#getSize()), [getTransformationOption](Image.html#getTransformationOption()), [getWidth](Image.html#getWidth()), [hashCode](Image.html#hashCode()), [isChanged](Image.html#isChanged()), [isDisposeAfterUse](Image.html#isDisposeAfterUse()), [isTransformWithOption](Image.html#isTransformWithOption(int)), [setChanged](Image.html#setChanged(boolean)), [setData](Image.html#setData(java.awt.image.BufferedImage)), [setDisposeAfterUse](Image.html#setDisposeAfterUse(boolean)), [setDpi](Image.html#setDpi(int)), [setHeight](Image.html#setHeight(int)), [setId](Image.html#setId(java.lang.String)), [setImageFile](Image.html#setImageFile(java.io.File)), [setImageFormat](Image.html#setImageFormat(java.lang.String)), [setImageType](Image.html#setImageType(int)), [setName](Image.html#setName(java.lang.String)), [setOriginalHeight](Image.html#setOriginalHeight(int)), [setOriginalImageFile](Image.html#setOriginalImageFile(java.io.File)), [setOriginalImageFormat](Image.html#setOriginalImageFormat(java.lang.String)), [setOriginalWidth](Image.html#setOriginalWidth(int)), [setProperties](Image.html#setProperties(java.util.Map)), [setProperty](Image.html#setProperty(java.lang.String,java.lang.Object)), [setTransformationOption](Image.html#setTransformationOption(int)), [setWidth](Image.html#setWidth(int)), [toString](Image.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SVGIcon
public SVGIcon([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) imageFile,
 boolean disposeAfterUse)
SVGIcon
public SVGIcon([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html) data,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageFormat,
 boolean disposeAfterUse)
 ============ METHOD DETAIL ========== 
Method Details
getSvgGenerator
public org.apache.batik.svggen.SVGGraphics2D getSvgGenerator()
setSvgGenerator
public void setSvgGenerator(org.apache.batik.svggen.SVGGraphics2D svgGenerator)
flush
public void flush([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) track)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Description copied from class: `[Image](Image.html#flush(java.lang.Object))`
Flush current buffered image from [`Image.getData()`](Image.html#getData()) into file stream. This method will set a new image file
 and dispose the data. The image file will be deleted when tracked object is garbage collected.
Overrides:
`[flush](Image.html#flush(java.lang.Object))` in class `[Image](Image.html)`
Parameters:
`track` - the marker object track flushed file, deleting the file when the marker instance is garbage
 collected.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - when unable to flush the data.
See Also:
[`Image.getData()`](Image.html#getData())
[`Image.getImageFile()`](Image.html#getImageFile())
[`Image.flush()`](Image.html#flush())
ensureOriginal
public void ensureOriginal()
Overrides:
`[ensureOriginal](Image.html#ensureOriginal())` in class `[Image](Image.html)`
readData
public [BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html) readData()
Description copied from class: `[Image](Image.html#readData())`
Read a buffered image from this instance. Return BufferedImage if [`Image.getData()`](Image.html#getData()) contains data or read
 from [`Image.getImageFile()`](Image.html#getImageFile()).
Overrides:
`[readData](Image.html#readData())` in class `[Image](Image.html)`
Returns:
a buffered image from [`Image.getData()`](Image.html#getData()) or [`Image.getImageFile()`](Image.html#getImageFile())
rotate
public void rotate(boolean clockwise)
Description copied from class: `[Image](Image.html#rotate(boolean))`
Rotate image in clockwise or anti-clockwise.
Overrides:
`[rotate](Image.html#rotate(boolean))` in class `[Image](Image.html)`
Parameters:
`clockwise` - true for clockwise; false for anti-clockwise

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport</a></div>
<h1 class="title" title="Class SVGIcon">Class SVGIcon</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="Image.html" title="class in com.nomagic.magicreport">com.nomagic.magicreport.Image</a>
<div class="inheritance">com.nomagic.magicreport.SVGIcon</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="engine/IObserverMessage.html" title="interface in com.nomagic.magicreport.engine">IObserverMessage</a></code>, <code><a href="IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SVGIcon</span>
<span class="extends-implements">extends <a href="Image.html" title="class in com.nomagic.magicreport">Image</a></span></div>
<div class="block">A bean represent SVG icon.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Mar 22, 2016</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../serialized-form.html#com.nomagic.magicreport.SVGIcon">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.Image">Fields inherited from class com.nomagic.magicreport.<a href="Image.html" title="class in com.nomagic.magicreport">Image</a></h3>
<code><a href="Image.html#FIT_PAPER">FIT_PAPER</a>, <a href="Image.html#FORCE_ROTATE">FORCE_ROTATE</a>, <a href="Image.html#FORCE_ROTATE_LEFT">FORCE_ROTATE_LEFT</a>, <a href="Image.html#FORCE_ROTATE_RIGHT">FORCE_ROTATE_RIGHT</a>, <a href="Image.html#IMAGE_TYPE_ICON">IMAGE_TYPE_ICON</a>, <a href="Image.html#IMAGE_TYPE_IMAGE">IMAGE_TYPE_IMAGE</a>, <a href="Image.html#LARGE_ONLY">LARGE_ONLY</a>, <a href="Image.html#MAINTAIN_RATIO">MAINTAIN_RATIO</a>, <a href="Image.html#ROTATE_LEFT">ROTATE_LEFT</a>, <a href="Image.html#ROTATE_RIGHT">ROTATE_RIGHT</a>, <a href="Image.html#TRUE_TRANSFORM">TRUE_TRANSFORM</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.awt.image.BufferedImage,java.lang.String,boolean)">SVGIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a> data,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageFormat,
 boolean disposeAfterUse)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.io.File,boolean)">SVGIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> imageFile,
 boolean disposeAfterUse)</code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ensureOriginal()">ensureOriginal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#flush(java.lang.Object)">flush</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> track)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Flush current buffered image from <a href="Image.html#getData()"><code>Image.getData()</code></a> into file stream.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.apache.batik.svggen.SVGGraphics2D</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSvgGenerator()">getSvgGenerator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readData()">readData</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read a buffered image from this instance.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#rotate(boolean)">rotate</a><wbr/>(boolean clockwise)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Rotate image in clockwise or anti-clockwise.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSvgGenerator(org.apache.batik.svggen.SVGGraphics2D)">setSvgGenerator</a><wbr/>(org.apache.batik.svggen.SVGGraphics2D svgGenerator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.Image">Methods inherited from class com.nomagic.magicreport.<a href="Image.html" title="class in com.nomagic.magicreport">Image</a></h3>
<code><a href="Image.html#clone()">clone</a>, <a href="Image.html#createOriginal()">createOriginal</a>, <a href="Image.html#dispose()">dispose</a>, <a href="Image.html#equals(java.lang.Object)">equals</a>, <a href="Image.html#flush()">flush</a>, <a href="Image.html#getBounds()">getBounds</a>, <a href="Image.html#getData()">getData</a>, <a href="Image.html#getDpi()">getDpi</a>, <a href="Image.html#getHeight()">getHeight</a>, <a href="Image.html#getId()">getId</a>, <a href="Image.html#getImageFile()">getImageFile</a>, <a href="Image.html#getImageFormat()">getImageFormat</a>, <a href="Image.html#getImageFormatToWrite()">getImageFormatToWrite</a>, <a href="Image.html#getImageType()">getImageType</a>, <a href="Image.html#getName()">getName</a>, <a href="Image.html#getOriginalBounds()">getOriginalBounds</a>, <a href="Image.html#getOriginalHeight()">getOriginalHeight</a>, <a href="Image.html#getOriginalImageFile()">getOriginalImageFile</a>, <a href="Image.html#getOriginalImageFormat()">getOriginalImageFormat</a>, <a href="Image.html#getOriginalWidth()">getOriginalWidth</a>, <a href="Image.html#getProperties()">getProperties</a>, <a href="Image.html#getProperty(java.lang.String)">getProperty</a>, <a href="Image.html#getSize()">getSize</a>, <a href="Image.html#getTransformationOption()">getTransformationOption</a>, <a href="Image.html#getWidth()">getWidth</a>, <a href="Image.html#hashCode()">hashCode</a>, <a href="Image.html#isChanged()">isChanged</a>, <a href="Image.html#isDisposeAfterUse()">isDisposeAfterUse</a>, <a href="Image.html#isTransformWithOption(int)">isTransformWithOption</a>, <a href="Image.html#setChanged(boolean)">setChanged</a>, <a href="Image.html#setData(java.awt.image.BufferedImage)">setData</a>, <a href="Image.html#setDisposeAfterUse(boolean)">setDisposeAfterUse</a>, <a href="Image.html#setDpi(int)">setDpi</a>, <a href="Image.html#setHeight(int)">setHeight</a>, <a href="Image.html#setId(java.lang.String)">setId</a>, <a href="Image.html#setImageFile(java.io.File)">setImageFile</a>, <a href="Image.html#setImageFormat(java.lang.String)">setImageFormat</a>, <a href="Image.html#setImageType(int)">setImageType</a>, <a href="Image.html#setName(java.lang.String)">setName</a>, <a href="Image.html#setOriginalHeight(int)">setOriginalHeight</a>, <a href="Image.html#setOriginalImageFile(java.io.File)">setOriginalImageFile</a>, <a href="Image.html#setOriginalImageFormat(java.lang.String)">setOriginalImageFormat</a>, <a href="Image.html#setOriginalWidth(int)">setOriginalWidth</a>, <a href="Image.html#setProperties(java.util.Map)">setProperties</a>, <a href="Image.html#setProperty(java.lang.String,java.lang.Object)">setProperty</a>, <a href="Image.html#setTransformationOption(int)">setTransformationOption</a>, <a href="Image.html#setWidth(int)">setWidth</a>, <a href="Image.html#toString()">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.io.File,boolean)">
<h3>SVGIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SVGIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> imageFile,
 boolean disposeAfterUse)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.awt.image.BufferedImage,java.lang.String,boolean)">
<h3>SVGIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SVGIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a> data,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageFormat,
 boolean disposeAfterUse)</span></div>
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
<section class="detail" id="getSvgGenerator()">
<h3>getSvgGenerator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.apache.batik.svggen.SVGGraphics2D</span> <span class="element-name">getSvgGenerator</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setSvgGenerator(org.apache.batik.svggen.SVGGraphics2D)">
<h3>setSvgGenerator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSvgGenerator</span><wbr/><span class="parameters">(org.apache.batik.svggen.SVGGraphics2D svgGenerator)</span></div>
</section>
</li>
<li>
<section class="detail" id="flush(java.lang.Object)">
<h3>flush</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">flush</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> track)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="Image.html#flush(java.lang.Object)">Image</a></code></span></div>
<div class="block">Flush current buffered image from <a href="Image.html#getData()"><code>Image.getData()</code></a> into file stream. This method will set a new image file
 and dispose the data. The image file will be deleted when tracked object is garbage collected.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Image.html#flush(java.lang.Object)">flush</a></code> in class <code><a href="Image.html" title="class in com.nomagic.magicreport">Image</a></code></dd>
<dt>Parameters:</dt>
<dd><code>track</code> - the marker object track flushed file, deleting the file when the marker instance is garbage
           collected.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - when unable to flush the data.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="Image.html#getData()"><code>Image.getData()</code></a></li>
<li><a href="Image.html#getImageFile()"><code>Image.getImageFile()</code></a></li>
<li><a href="Image.html#flush()"><code>Image.flush()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ensureOriginal()">
<h3>ensureOriginal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">ensureOriginal</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Image.html#ensureOriginal()">ensureOriginal</a></code> in class <code><a href="Image.html" title="class in com.nomagic.magicreport">Image</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readData()">
<h3>readData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></span> <span class="element-name">readData</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="Image.html#readData()">Image</a></code></span></div>
<div class="block">Read a buffered image from this instance. Return BufferedImage if <a href="Image.html#getData()"><code>Image.getData()</code></a> contains data or read
 from <a href="Image.html#getImageFile()"><code>Image.getImageFile()</code></a>.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Image.html#readData()">readData</a></code> in class <code><a href="Image.html" title="class in com.nomagic.magicreport">Image</a></code></dd>
<dt>Returns:</dt>
<dd>a buffered image from <a href="Image.html#getData()"><code>Image.getData()</code></a> or <a href="Image.html#getImageFile()"><code>Image.getImageFile()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="rotate(boolean)">
<h3>rotate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">rotate</span><wbr/><span class="parameters">(boolean clockwise)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="Image.html#rotate(boolean)">Image</a></code></span></div>
<div class="block">Rotate image in clockwise or anti-clockwise.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Image.html#rotate(boolean)">rotate</a></code> in class <code><a href="Image.html" title="class in com.nomagic.magicreport">Image</a></code></dd>
<dt>Parameters:</dt>
<dd><code>clockwise</code> - true for clockwise; false for anti-clockwise</dd>
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
