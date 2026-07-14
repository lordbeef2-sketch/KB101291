# JAVA OPENAPI: DefaultFormatter (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/format/DefaultFormatter.html
- source_path: `com/nomagic/magicreport/format/DefaultFormatter.html`
- source_sha256: `4e29fa63d1e367f4d2aa52144b511b37793ecb304f0b8cba7cdf6e611b21c60c`
- captured_utc: `2026-07-14T16:46:13.732984+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format](package-summary.html)

## Class DefaultFormatter

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.format.DefaultFormatter

All Implemented Interfaces:
`[IFormatter](IFormatter.html)`

Direct Known Subclasses:
`[DocBookFormatter](DocBookFormatter.html)`, `[DOCXFormatter](DOCXFormatter.html)`, `[HTMLFormatter](HTMLFormatter.html)`, `[LaTeXFormatter](LaTeXFormatter.html)`, `[PPTXFormatter](PPTXFormatter.html)`, `[RTFFormatter](RTFFormatter.html)`, `[TextFormatter](TextFormatter.html)`, `[XLSXFormatter](XLSXFormatter.html)`, `[XMLFormatter](XMLFormatter.html)`

@OpenApiAllpublic classDefaultFormatter
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [IFormatter](IFormatter.html)

This class provides default implementation for any output format.

Since:
Jun 11, 2007 10:49:57 PM
Version:
1.0 Jun 11, 2007

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html)`
`[properties](#properties)`
Engine properties.
`protected [StyledDocument](html/StyledDocument.html)`
`[styledDocument](#styledDocument)`
Styled document.
Fields inherited from interface com.nomagic.magicreport.format.[IFormatter](IFormatter.html)
`[DOT_PER_INCH](IFormatter.html#DOT_PER_INCH)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DefaultFormatter](#%3Cinit%3E())()`
Create a default formatter without properties.
`[DefaultFormatter](#%3Cinit%3E(java.util.Properties))([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
Create a default formatter with specific properties.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[format](#format(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Convert an Object value into default format.
`static int`
`[getImageFlag](#getImageFlag(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) autoImageOption)`
Convert auto image option from [`TemplateConstants.TEMPLATE_AUTO_IMAGE`](../engine/TemplateConstants.html#TEMPLATE_AUTO_IMAGE) into transformation flag.
`[IFormatter](IFormatter.html)`
`[getObjectFormater](#getObjectFormater(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> targetType)`
Returns the formatter for the target type class or current formatter if target type class is not registered.
`[Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html)`
`[getProperties](#getProperties())()`
Return a properties.
`void`
`[registerObjectFormatter](#registerObjectFormatter(java.lang.Class,com.nomagic.magicreport.format.IFormatter))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> targetType,
 [IFormatter](IFormatter.html) formatter)`
Register an object formatter to be used to format values of a given target class.
`void`
`[setProperties](#setProperties(java.util.Properties))([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
Passes along the properties from the template engine indicating the properties to be used in formatter.
`void`
`[setStyledDocument](#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument))([StyledDocument](html/StyledDocument.html) styledDocument)`
Set a [`StyledDocument`](html/StyledDocument.html) to be used with this formatter.
`protected void`
`[writeImage](#writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.File,boolean))([Image](../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageFormat,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) outputFile,
 boolean forceWrite)`
Write an image into output file.
`protected void`
`[writeImage](#writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.OutputStream,boolean))([Image](../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageFormat,
 [OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) outputStream,
 boolean forceWrite)`
Write an image into output stream.
`protected void`
`[writeImage](#writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.OutputStream,boolean,boolean))([Image](../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageFormat,
 [OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) outputStream,
 boolean forceWrite,
 boolean skipDPI)`
Write an image into output stream.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
properties
protected [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties
Engine properties.
styledDocument
protected [StyledDocument](html/StyledDocument.html) styledDocument
Styled document.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DefaultFormatter
public DefaultFormatter()
Create a default formatter without properties.
DefaultFormatter
public DefaultFormatter([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
Create a default formatter with specific properties.
Parameters:
`properties` - a template properties
 ============ METHOD DETAIL ========== 
Method Details
registerObjectFormatter
public void registerObjectFormatter([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> targetType,
 [IFormatter](IFormatter.html) formatter)
Register an object formatter to be used to format values of a given target class.
Specified by:
`[registerObjectFormatter](IFormatter.html#registerObjectFormatter(java.lang.Class,com.nomagic.magicreport.format.IFormatter))` in interface `[IFormatter](IFormatter.html)`
Parameters:
`targetType` - the Class object of the type to be formatted
`formatter` - the instance of object of the [`IFormatter`](IFormatter.html) class. If this is null, then any existing
 definition will be removed.
getObjectFormater
public [IFormatter](IFormatter.html) getObjectFormater([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> targetType)
Returns the formatter for the target type class or current formatter if target type class is not registered.
Specified by:
`[getObjectFormater](IFormatter.html#getObjectFormater(java.lang.Class))` in interface `[IFormatter](IFormatter.html)`
Parameters:
`targetType` - the Class object of the type to be formatted
Returns:
the instance of object of the [`IFormatter`](IFormatter.html) class.
setProperties
public void setProperties([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
Passes along the properties from the template engine indicating the properties to be used in formatter.
Parameters:
`properties` - Properties
getProperties
public [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) getProperties()
Return a properties.
Returns:
the properties
setStyledDocument
public void setStyledDocument([StyledDocument](html/StyledDocument.html) styledDocument)
Set a [`StyledDocument`](html/StyledDocument.html) to be used with this formatter.
Specified by:
`[setStyledDocument](IFormatter.html#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument))` in interface `[IFormatter](IFormatter.html)`
Parameters:
`styledDocument` - A {link StyledDocument}
writeImage
protected void writeImage([Image](../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageFormat,
 [OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) outputStream,
 boolean forceWrite)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Write an image into output stream.
Parameters:
`image` - Image
`imageFormat` - output image format
`outputStream` - output stream
`forceWrite` - force to write the image to output stream
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an error occurs during writing.
writeImage
protected void writeImage([Image](../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageFormat,
 [OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) outputStream,
 boolean forceWrite,
 boolean skipDPI)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Write an image into output stream.
Parameters:
`image` - Image
`imageFormat` - output image format
`outputStream` - output stream
`forceWrite` - force to write the image to output stream
`skipDPI` - skip change dpi metadata
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an error occurs during writing.
writeImage
protected void writeImage([Image](../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageFormat,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) outputFile,
 boolean forceWrite)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Write an image into output file.
Parameters:
`image` - Image
`imageFormat` - output image format
`outputFile` - output file
`forceWrite` - force to write the image to output stream
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an error occurs during writing.
format
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) format([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Convert an Object value into default format. This method always convert all value into String.
Specified by:
`[format](IFormatter.html#format(java.lang.Object))` in interface `[IFormatter](IFormatter.html)`
Parameters:
`value` - converting value
Returns:
object in default format.
getImageFlag
public static int getImageFlag([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) autoImageOption)
Convert auto image option from [`TemplateConstants.TEMPLATE_AUTO_IMAGE`](../engine/TemplateConstants.html#TEMPLATE_AUTO_IMAGE) into transformation flag.
Parameters:
`autoImageOption` - auto image option; (value 0, 1, 2, 3)
Returns:
transformation flag

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format</a></div>
<h1 class="title" title="Class DefaultFormatter">Class DefaultFormatter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.format.DefaultFormatter</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="DocBookFormatter.html" title="class in com.nomagic.magicreport.format">DocBookFormatter</a></code>, <code><a href="DOCXFormatter.html" title="class in com.nomagic.magicreport.format">DOCXFormatter</a></code>, <code><a href="HTMLFormatter.html" title="class in com.nomagic.magicreport.format">HTMLFormatter</a></code>, <code><a href="LaTeXFormatter.html" title="class in com.nomagic.magicreport.format">LaTeXFormatter</a></code>, <code><a href="PPTXFormatter.html" title="class in com.nomagic.magicreport.format">PPTXFormatter</a></code>, <code><a href="RTFFormatter.html" title="class in com.nomagic.magicreport.format">RTFFormatter</a></code>, <code><a href="TextFormatter.html" title="class in com.nomagic.magicreport.format">TextFormatter</a></code>, <code><a href="XLSXFormatter.html" title="class in com.nomagic.magicreport.format">XLSXFormatter</a></code>, <code><a href="XMLFormatter.html" title="class in com.nomagic.magicreport.format">XMLFormatter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DefaultFormatter</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></span></div>
<div class="block">This class provides default implementation for any output format.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 11, 2007 10:49:57 PM</dd>
<dt>Version:</dt>
<dd>1.0 Jun 11, 2007</dd>
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
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#properties">properties</a></code></div>
<div class="col-last even-row-color">
<div class="block">Engine properties.</div>
</div>
<div class="col-first odd-row-color"><code>protected <a href="html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#styledDocument">styledDocument</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Styled document.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.format.IFormatter">Fields inherited from interface com.nomagic.magicreport.format.<a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></h3>
<code><a href="IFormatter.html#DOT_PER_INCH">DOT_PER_INCH</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DefaultFormatter</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Create a default formatter without properties.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Properties)">DefaultFormatter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create a default formatter with specific properties.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#format(java.lang.Object)">format</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert an Object value into default format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageFlag(java.lang.String)">getImageFlag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> autoImageOption)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert auto image option from <a href="../engine/TemplateConstants.html#TEMPLATE_AUTO_IMAGE"><code>TemplateConstants.TEMPLATE_AUTO_IMAGE</code></a> into transformation flag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectFormater(java.lang.Class)">getObjectFormater</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; targetType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the formatter for the target type class or current formatter if target type class is not registered.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperties()">getProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a properties.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerObjectFormatter(java.lang.Class,com.nomagic.magicreport.format.IFormatter)">registerObjectFormatter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; targetType,
 <a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a> formatter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Register an object formatter to be used to format values of a given target class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperties(java.util.Properties)">setProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Passes along the properties from the template engine indicating the properties to be used in formatter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument)">setStyledDocument</a><wbr/>(<a href="html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a> styledDocument)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a <a href="html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html"><code>StyledDocument</code></a> to be used with this formatter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.File,boolean)">writeImage</a><wbr/>(<a href="../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageFormat,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> outputFile,
 boolean forceWrite)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write an image into output file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.OutputStream,boolean)">writeImage</a><wbr/>(<a href="../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageFormat,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> outputStream,
 boolean forceWrite)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write an image into output stream.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.OutputStream,boolean,boolean)">writeImage</a><wbr/>(<a href="../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageFormat,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> outputStream,
 boolean forceWrite,
 boolean skipDPI)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write an image into output stream.</div>
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
<section class="detail" id="properties">
<h3>properties</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></span> <span class="element-name">properties</span></div>
<div class="block">Engine properties.</div>
</section>
</li>
<li>
<section class="detail" id="styledDocument">
<h3>styledDocument</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a></span> <span class="element-name">styledDocument</span></div>
<div class="block">Styled document.</div>
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
<h3>DefaultFormatter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DefaultFormatter</span>()</div>
<div class="block">Create a default formatter without properties.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Properties)">
<h3>DefaultFormatter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DefaultFormatter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">Create a default formatter with specific properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - a template properties</dd>
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
<section class="detail" id="registerObjectFormatter(java.lang.Class,com.nomagic.magicreport.format.IFormatter)">
<h3>registerObjectFormatter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerObjectFormatter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; targetType,
 <a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a> formatter)</span></div>
<div class="block">Register an object formatter to be used to format values of a given target class.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IFormatter.html#registerObjectFormatter(java.lang.Class,com.nomagic.magicreport.format.IFormatter)">registerObjectFormatter</a></code> in interface <code><a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>targetType</code> - the Class object of the type to be formatted</dd>
<dd><code>formatter</code> - the instance of object of the <a href="IFormatter.html" title="interface in com.nomagic.magicreport.format"><code>IFormatter</code></a> class. If this is null, then any existing
           definition will be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectFormater(java.lang.Class)">
<h3>getObjectFormater</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></span> <span class="element-name">getObjectFormater</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; targetType)</span></div>
<div class="block">Returns the formatter for the target type class or current formatter if target type class is not registered.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IFormatter.html#getObjectFormater(java.lang.Class)">getObjectFormater</a></code> in interface <code><a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>targetType</code> - the Class object of the type to be formatted</dd>
<dt>Returns:</dt>
<dd>the instance of object of the <a href="IFormatter.html" title="interface in com.nomagic.magicreport.format"><code>IFormatter</code></a> class.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProperties(java.util.Properties)">
<h3>setProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">Passes along the properties from the template engine indicating the properties to be used in formatter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - Properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperties()">
<h3>getProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></span> <span class="element-name">getProperties</span>()</div>
<div class="block">Return a properties.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument)">
<h3>setStyledDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStyledDocument</span><wbr/><span class="parameters">(<a href="html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a> styledDocument)</span></div>
<div class="block">Set a <a href="html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html"><code>StyledDocument</code></a> to be used with this formatter.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IFormatter.html#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument)">setStyledDocument</a></code> in interface <code><a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>styledDocument</code> - A {link StyledDocument}</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.OutputStream,boolean)">
<h3>writeImage</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">writeImage</span><wbr/><span class="parameters">(<a href="../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageFormat,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> outputStream,
 boolean forceWrite)</span>
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Write an image into output stream.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - Image</dd>
<dd><code>imageFormat</code> - output image format</dd>
<dd><code>outputStream</code> - output stream</dd>
<dd><code>forceWrite</code> - force to write the image to output stream</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an error occurs during writing.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.OutputStream,boolean,boolean)">
<h3>writeImage</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">writeImage</span><wbr/><span class="parameters">(<a href="../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageFormat,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> outputStream,
 boolean forceWrite,
 boolean skipDPI)</span>
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Write an image into output stream.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - Image</dd>
<dd><code>imageFormat</code> - output image format</dd>
<dd><code>outputStream</code> - output stream</dd>
<dd><code>forceWrite</code> - force to write the image to output stream</dd>
<dd><code>skipDPI</code> - skip change dpi metadata</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an error occurs during writing.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.File,boolean)">
<h3>writeImage</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">writeImage</span><wbr/><span class="parameters">(<a href="../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageFormat,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> outputFile,
 boolean forceWrite)</span>
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Write an image into output file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - Image</dd>
<dd><code>imageFormat</code> - output image format</dd>
<dd><code>outputFile</code> - output file</dd>
<dd><code>forceWrite</code> - force to write the image to output stream</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an error occurs during writing.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="format(java.lang.Object)">
<h3>format</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">format</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Convert an Object value into default format. This method always convert all value into String.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IFormatter.html#format(java.lang.Object)">format</a></code> in interface <code><a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - converting value</dd>
<dt>Returns:</dt>
<dd>object in default format.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImageFlag(java.lang.String)">
<h3>getImageFlag</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">getImageFlag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> autoImageOption)</span></div>
<div class="block">Convert auto image option from <a href="../engine/TemplateConstants.html#TEMPLATE_AUTO_IMAGE"><code>TemplateConstants.TEMPLATE_AUTO_IMAGE</code></a> into transformation flag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>autoImageOption</code> - auto image option; (value 0, 1, 2, 3)</dd>
<dt>Returns:</dt>
<dd>transformation flag</dd>
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
