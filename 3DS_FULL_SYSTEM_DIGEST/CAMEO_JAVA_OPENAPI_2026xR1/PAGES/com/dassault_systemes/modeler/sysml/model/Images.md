# JAVA OPENAPI: Images (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Images.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Images.html`
- source_sha256: `9d8a4bd9a20a8782cdd1c8108134b72851c5f2fc19d9ffbaabf1495a526b24ab`
- captured_utc: `2026-07-14T16:45:02.619036+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Images

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Images

@OpenApiAllpublic classImages
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with Image elements

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ENCODING_BASE64](#ENCODING_BASE64)`
Encoding identifier for Base64‑encoded image content.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ENCODING_IDENTITY](#ENCODING_IDENTITY)`
Encoding identifier for raw (identity) image content.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TYPE_IMAGE_GIF](#TYPE_IMAGE_GIF)`
MIME type for GIF images.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TYPE_IMAGE_JPEG](#TYPE_IMAGE_JPEG)`
MIME type for JPEG images.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TYPE_IMAGE_PNG](#TYPE_IMAGE_PNG)`
MIME type for PNG images.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TYPE_IMAGE_SVG](#TYPE_IMAGE_SVG)`
Canonical MIME type for SVG images.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TYPE_IMAGE_SVG_XML](#TYPE_IMAGE_SVG_XML)`
MIME type for SVG images expressed as XML.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Images](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ResizableIcon](../../../../nomagic/ui/ResizableIcon.html)`
`[createIcon](#createIcon(java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) encoding,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) location)`
Creates a Swing icon from the given encoded image data.
`static [AttributeDefinition](sysml/AttributeDefinition.html)`
`[createImage](#createImage(com.dassault_systemes.modeler.foundation.project.ModelElementProject,java.lang.String,java.lang.String,java.lang.String))([ModelElementProject](../../foundation/project/ModelElementProject.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) encoding,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)`
Creates a new image attribute definition under the given project and
 initializes its metadata fields.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getContentAsBase64](#getContentAsBase64(byte%5B%5D))(byte[] content)`
Encodes raw bytes into a Base64 string.
`static [ResizableIcon](../../../../nomagic/ui/ResizableIcon.html)`
`[getIcon](#getIcon(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) element)`
Returns a Swing icon for the given image element, if possible.
`static boolean`
`[isImage](#isImage(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Checks whether the given element represents an image using the default
 image metadata library.
`static void`
`[setImageAttributes](#setImageAttributes(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.String,java.lang.String,java.lang.String))([Type](../../kerml/model/kerml/Type.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) encoding,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)`
Sets the metadata attributes (type, encoding, content) on the given image element.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ENCODING_BASE64
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ENCODING_BASE64
Encoding identifier for Base64‑encoded image content.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.ENCODING_BASE64)
ENCODING_IDENTITY
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ENCODING_IDENTITY
Encoding identifier for raw (identity) image content.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.ENCODING_IDENTITY)
TYPE_IMAGE_PNG
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TYPE_IMAGE_PNG
MIME type for PNG images.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.TYPE_IMAGE_PNG)
TYPE_IMAGE_JPEG
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TYPE_IMAGE_JPEG
MIME type for JPEG images.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.TYPE_IMAGE_JPEG)
TYPE_IMAGE_GIF
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TYPE_IMAGE_GIF
MIME type for GIF images.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.TYPE_IMAGE_GIF)
TYPE_IMAGE_SVG_XML
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TYPE_IMAGE_SVG_XML
MIME type for SVG images expressed as XML.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.TYPE_IMAGE_SVG_XML)
TYPE_IMAGE_SVG
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TYPE_IMAGE_SVG
Canonical MIME type for SVG images.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.TYPE_IMAGE_SVG)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Images
public Images()
 ============ METHOD DETAIL ========== 
Method Details
createImage
public static [AttributeDefinition](sysml/AttributeDefinition.html) createImage([ModelElementProject](../../foundation/project/ModelElementProject.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) encoding,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)
Creates a new image attribute definition under the given project and
 initializes its metadata fields.
Parameters:
`project` - the project in which the image is created
`type` - MIME type of the image
`encoding` - encoding of the image content (base64 or identity)
`content` - encoded image content
Returns:
the created image attribute definition
setImageAttributes
public static void setImageAttributes([Type](../../kerml/model/kerml/Type.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) encoding,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)
Sets the metadata attributes (type, encoding, content) on the given image element.
Parameters:
`image` - the image element
`type` - MIME type
`encoding` - encoding format
`content` - encoded content
isImage
public static boolean isImage([Element](../../kerml/model/kerml/Element.html) element)
Checks whether the given element represents an image using the default
 image metadata library.
Parameters:
`element` - the element to check
Returns:
true if the element is an image
getIcon
@CheckForNullpublic static [ResizableIcon](../../../../nomagic/ui/ResizableIcon.html) getIcon([Type](../../kerml/model/kerml/Type.html) element)
Returns a Swing icon for the given image element, if possible.
Parameters:
`element` - the image element
Returns:
a resizable icon, or null if the image cannot be decoded
createIcon
@CheckForNullpublic static [ResizableIcon](../../../../nomagic/ui/ResizableIcon.html) createIcon(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) encoding,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) location)
Creates a Swing icon from the given encoded image data.
Parameters:
`encoding` - encoding format (base64 or identity)
`content` - encoded content
`type` - MIME type
`location` - optional location hint
Returns:
a resizable icon, or null if decoding fails
getContentAsBase64
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getContentAsBase64(byte[] content)
Encodes raw bytes into a Base64 string.
Parameters:
`content` - raw bytes
Returns:
Base64-encoded string

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Images">Class Images</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Images</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Images</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with Image elements</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ENCODING_BASE64">ENCODING_BASE64</a></code></div>
<div class="col-last even-row-color">
<div class="block">Encoding identifier for Base64‑encoded image content.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ENCODING_IDENTITY">ENCODING_IDENTITY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Encoding identifier for raw (identity) image content.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TYPE_IMAGE_GIF">TYPE_IMAGE_GIF</a></code></div>
<div class="col-last even-row-color">
<div class="block">MIME type for GIF images.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TYPE_IMAGE_JPEG">TYPE_IMAGE_JPEG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">MIME type for JPEG images.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TYPE_IMAGE_PNG">TYPE_IMAGE_PNG</a></code></div>
<div class="col-last even-row-color">
<div class="block">MIME type for PNG images.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TYPE_IMAGE_SVG">TYPE_IMAGE_SVG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Canonical MIME type for SVG images.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TYPE_IMAGE_SVG_XML">TYPE_IMAGE_SVG_XML</a></code></div>
<div class="col-last even-row-color">
<div class="block">MIME type for SVG images expressed as XML.</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Images</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../../nomagic/ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createIcon(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">createIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> encoding,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a Swing icon from the given encoded image data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createImage(com.dassault_systemes.modeler.foundation.project.ModelElementProject,java.lang.String,java.lang.String,java.lang.String)">createImage</a><wbr/>(<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> encoding,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a new image attribute definition under the given project and
 initializes its metadata fields.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getContentAsBase64(byte%5B%5D)">getContentAsBase64</a><wbr/>(byte[] content)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Encodes raw bytes into a Base64 string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../../nomagic/ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getIcon</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a Swing icon for the given image element, if possible.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isImage(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isImage</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given element represents an image using the default
 image metadata library.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setImageAttributes(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.String,java.lang.String,java.lang.String)">setImageAttributes</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> encoding,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the metadata attributes (type, encoding, content) on the given image element.</div>
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
<section class="detail" id="ENCODING_BASE64">
<h3>ENCODING_BASE64</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ENCODING_BASE64</span></div>
<div class="block">Encoding identifier for Base64‑encoded image content.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.ENCODING_BASE64">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENCODING_IDENTITY">
<h3>ENCODING_IDENTITY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ENCODING_IDENTITY</span></div>
<div class="block">Encoding identifier for raw (identity) image content.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.ENCODING_IDENTITY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE_IMAGE_PNG">
<h3>TYPE_IMAGE_PNG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TYPE_IMAGE_PNG</span></div>
<div class="block">MIME type for PNG images.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.TYPE_IMAGE_PNG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE_IMAGE_JPEG">
<h3>TYPE_IMAGE_JPEG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TYPE_IMAGE_JPEG</span></div>
<div class="block">MIME type for JPEG images.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.TYPE_IMAGE_JPEG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE_IMAGE_GIF">
<h3>TYPE_IMAGE_GIF</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TYPE_IMAGE_GIF</span></div>
<div class="block">MIME type for GIF images.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.TYPE_IMAGE_GIF">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE_IMAGE_SVG_XML">
<h3>TYPE_IMAGE_SVG_XML</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TYPE_IMAGE_SVG_XML</span></div>
<div class="block">MIME type for SVG images expressed as XML.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.TYPE_IMAGE_SVG_XML">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE_IMAGE_SVG">
<h3>TYPE_IMAGE_SVG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TYPE_IMAGE_SVG</span></div>
<div class="block">Canonical MIME type for SVG images.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.Images.TYPE_IMAGE_SVG">Constant Field Values</a></li>
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
<h3>Images</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Images</span>()</div>
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
<section class="detail" id="createImage(com.dassault_systemes.modeler.foundation.project.ModelElementProject,java.lang.String,java.lang.String,java.lang.String)">
<h3>createImage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeDefinition</a></span> <span class="element-name">createImage</span><wbr/><span class="parameters">(<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> encoding,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content)</span></div>
<div class="block">Creates a new image attribute definition under the given project and
 initializes its metadata fields.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project in which the image is created</dd>
<dd><code>type</code> - MIME type of the image</dd>
<dd><code>encoding</code> - encoding of the image content (base64 or identity)</dd>
<dd><code>content</code> - encoded image content</dd>
<dt>Returns:</dt>
<dd>the created image attribute definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setImageAttributes(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.String,java.lang.String,java.lang.String)">
<h3>setImageAttributes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setImageAttributes</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> encoding,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content)</span></div>
<div class="block">Sets the metadata attributes (type, encoding, content) on the given image element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - the image element</dd>
<dd><code>type</code> - MIME type</dd>
<dd><code>encoding</code> - encoding format</dd>
<dd><code>content</code> - encoded content</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isImage(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isImage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isImage</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the given element represents an image using the default
 image metadata library.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd>true if the element is an image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../../../nomagic/ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element)</span></div>
<div class="block">Returns a Swing icon for the given image element, if possible.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the image element</dd>
<dt>Returns:</dt>
<dd>a resizable icon, or null if the image cannot be decoded</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIcon(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>createIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../../../nomagic/ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">createIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> encoding,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</span></div>
<div class="block">Creates a Swing icon from the given encoded image data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>encoding</code> - encoding format (base64 or identity)</dd>
<dd><code>content</code> - encoded content</dd>
<dd><code>type</code> - MIME type</dd>
<dd><code>location</code> - optional location hint</dd>
<dt>Returns:</dt>
<dd>a resizable icon, or null if decoding fails</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContentAsBase64(byte[])">
<h3>getContentAsBase64</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getContentAsBase64</span><wbr/><span class="parameters">(byte[] content)</span></div>
<div class="block">Encodes raw bytes into a Base64 string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>content</code> - raw bytes</dd>
<dt>Returns:</dt>
<dd>Base64-encoded string</dd>
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
