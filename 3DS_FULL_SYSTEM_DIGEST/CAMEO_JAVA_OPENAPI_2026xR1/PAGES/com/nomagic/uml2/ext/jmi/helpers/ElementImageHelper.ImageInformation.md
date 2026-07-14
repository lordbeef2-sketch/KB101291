# JAVA OPENAPI: ElementImageHelper.ImageInformation (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/jmi/helpers/ElementImageHelper.ImageInformation.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/ElementImageHelper.ImageInformation.html`
- source_sha256: `77f5e6601797018da7b0545304a9dae4c00a4863b891abb60d6f4e979c7e16cf`
- captured_utc: `2026-07-14T16:46:21.451086+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class ElementImageHelper.ImageInformation

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.model.ModelElementImages.AbstractElementImageInformation
com.nomagic.uml2.ext.jmi.helpers.ElementImageHelper.ImageInformation

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.model.ModelElementImages.ElementImageInformation`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

Enclosing class:
`[ElementImageHelper](ElementImageHelper.html)`

@OpenApiAllpublic static classElementImageHelper.ImageInformation
extends com.dassault_systemes.modeler.foundation.model.ModelElementImages.AbstractElementImageInformation

Structure, which contains information of image: content, format and location.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ImageInformation](#%3Cinit%3E())()`
Sets content, format and image to nulls.
`[ImageInformation](#%3Cinit%3E(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) format)`
Initializes content, format of image.
`[ImageInformation](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) format,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) location)`
Initializes content, format and location of image.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[clone](#clone())()`

`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getContent](#getContent())()`

`int`
`[hashCode](#hashCode())()`

`void`
`[setContent](#setContent(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)`
Sets content of image.
Methods inherited from class com.dassault_systemes.modeler.foundation.model.ModelElementImages.AbstractElementImageInformation
`getFormat, getLocation, setFormat, setLocation`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ImageInformation
public ImageInformation(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) format,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) location)
Initializes content, format and location of image.
Parameters:
`content` - content of image. Use [`Utilities.toString(byte[])`](../../../../utils/Utilities.html#toString(byte%5B%5D)) to convert bytes to a string
`format` - format of image(like gif, png and etc)
`location` - location of image
See Also:
[`Utilities.toString(byte[])`](../../../../utils/Utilities.html#toString(byte%5B%5D))
ImageInformation
public ImageInformation([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) format)
Initializes content, format of image.
Parameters:
`content` - content of image. Use [`Utilities.toString(byte[])`](../../../../utils/Utilities.html#toString(byte%5B%5D)) to convert bytes to a string.
`format` - format of image(like gif, png and etc).
See Also:
[`Utilities.toString(byte[])`](../../../../utils/Utilities.html#toString(byte%5B%5D))
ImageInformation
public ImageInformation()
Sets content, format and image to nulls.
 ============ METHOD DETAIL ========== 
Method Details
setContent
public void setContent(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)
Description copied from interface: `com.dassault_systemes.modeler.foundation.model.ModelElementImages.ElementImageInformation`
Sets content of image. Use [`CameoUtilities.toString(byte[])`](../../../../utils/CameoUtilities.html#toString(byte%5B%5D)) to convert bytes to a string.
Parameters:
`content` - content of image
getContent
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getContent()
Returns:
gets content of image
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)
Overrides:
`equals` in class `com.dassault_systemes.modeler.foundation.model.ModelElementImages.AbstractElementImageInformation`
hashCode
public int hashCode()
Overrides:
`hashCode` in class `com.dassault_systemes.modeler.foundation.model.ModelElementImages.AbstractElementImageInformation`
clone
protected [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) clone()
Overrides:
`clone` in class `com.dassault_systemes.modeler.foundation.model.ModelElementImages.AbstractElementImageInformation`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class ElementImageHelper.ImageInformation">Class ElementImageHelper.ImageInformation</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.model.ModelElementImages.AbstractElementImageInformation
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.ElementImageHelper.ImageInformation</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.model.ModelElementImages.ElementImageInformation</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="ElementImageHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public static class </span><span class="element-name type-name-label">ElementImageHelper.ImageInformation</span>
<span class="extends-implements">extends com.dassault_systemes.modeler.foundation.model.ModelElementImages.AbstractElementImageInformation</span></div>
<div class="block">Structure, which contains information of image: content, format and location.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ImageInformation</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Sets content, format and image to nulls.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String)">ImageInformation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format)</code></div>
<div class="col-last odd-row-color">
<div class="block">Initializes content, format of image.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String)">ImageInformation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</code></div>
<div class="col-last even-row-color">
<div class="block">Initializes content, format and location of image.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContent()">getContent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setContent(java.lang.String)">setContent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets content of image.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElementImages.AbstractElementImageInformation">Methods inherited from class com.dassault_systemes.modeler.foundation.model.ModelElementImages.AbstractElementImageInformation</h3>
<code>getFormat, getLocation, setFormat, setLocation</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String)">
<h3>ImageInformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ImageInformation</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</span></div>
<div class="block">Initializes content, format and location of image.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>content</code> - content of image. Use <a href="../../../../utils/Utilities.html#toString(byte%5B%5D)"><code>Utilities.toString(byte[])</code></a> to convert bytes to a string</dd>
<dd><code>format</code> - format of image(like gif, png and etc)</dd>
<dd><code>location</code> - location of image</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../utils/Utilities.html#toString(byte%5B%5D)"><code>Utilities.toString(byte[])</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String)">
<h3>ImageInformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ImageInformation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format)</span></div>
<div class="block">Initializes content, format of image.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>content</code> - content of image. Use <a href="../../../../utils/Utilities.html#toString(byte%5B%5D)"><code>Utilities.toString(byte[])</code></a> to convert bytes to a string.</dd>
<dd><code>format</code> - format of image(like gif, png and etc).</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../utils/Utilities.html#toString(byte%5B%5D)"><code>Utilities.toString(byte[])</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ImageInformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ImageInformation</span>()</div>
<div class="block">Sets content, format and image to nulls.</div>
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
<section class="detail" id="setContent(java.lang.String)">
<h3>setContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setContent</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code>com.dassault_systemes.modeler.foundation.model.ModelElementImages.ElementImageInformation</code></span></div>
<div class="block">Sets content of image. Use <a href="../../../../utils/CameoUtilities.html#toString(byte%5B%5D)"><code>CameoUtilities.toString(byte[])</code></a> to convert bytes to a string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>content</code> - content of image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContent()">
<h3>getContent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getContent</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>gets content of image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>equals</code> in class <code>com.dassault_systemes.modeler.foundation.model.ModelElementImages.AbstractElementImageInformation</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>hashCode</code> in class <code>com.dassault_systemes.modeler.foundation.model.ModelElementImages.AbstractElementImageInformation</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>clone</code> in class <code>com.dassault_systemes.modeler.foundation.model.ModelElementImages.AbstractElementImageInformation</code></dd>
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
