# JAVA OPENAPI: RTFCreator (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/format/html/RTFCreator.html
- source_path: `com/nomagic/magicreport/format/html/RTFCreator.html`
- source_sha256: `5bb0f888cd9e0ec6b6c9a04088069b6fa5bcf6c5438f30e7c865a5f94a03a4ea`
- captured_utc: `2026-07-14T16:46:14.264991+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format.html](package-summary.html)

## Class RTFCreator

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicreport.format.html.AbstractDocumentCreator](AbstractDocumentCreator.html)
com.nomagic.magicreport.format.html.RTFCreator

All Implemented Interfaces:
`[IHTMLHandler](IHTMLHandler.html)`, `[IDocumentCreator](../IDocumentCreator.html)`

@OpenApiAllpublic classRTFCreator
extends [AbstractDocumentCreator](AbstractDocumentCreator.html)
implements [IHTMLHandler](IHTMLHandler.html)

The class use for create RTF content.

Since:
May 22, 2009

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[HTML_TABLE_COLUMN_MINWIDTH_DEFAULT](#HTML_TABLE_COLUMN_MINWIDTH_DEFAULT)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[RTFCreator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addTableProperties](#addTableProperties(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) attributeName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Add tag and value of align/valign or bgcolor to stack.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[changeColorFormat](#changeColorFormat(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) color)`
Change color(3-digits RGB, 6-digits RGB and color name) to RGB format.
`void`
`[characters](#characters(char%5B%5D))(char[] data)`
Receive notification of character data inside a tag.
`void`
`[checkRowSpan](#checkRowSpan())()`
check rowspan when creator received tag td, th or tr.
`void`
`[comment](#comment(char%5B%5D))(char[] data)`
Receive notification of comment data.
`void`
`[convert](#convert(java.io.Reader,java.io.Writer))([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) reader,
 [Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) writer)`
Convert the HTML content from reader into RTF document.
`void`
`[endDocument](#endDocument())()`
The Override Method.
`void`
`[endTag](#endTag(javax.swing.text.html.HTML.Tag))([HTML.Tag](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html) tag)`
Receive notification of the end of a tag.
`double`
`[getPaperHeight](#getPaperHeight())()`
Get paper height.
`double`
`[getPaperWidth](#getPaperWidth())()`
Get paper width.
`[Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html)`
`[getProperties](#getProperties())()`
Get properties.
`void`
`[setDocumentPage](#setDocumentPage(com.nomagic.magicreport.DocumentPage))(com.nomagic.magicreport.DocumentPage page)`
set document page property.
`void`
`[setPaperHeight](#setPaperHeight(float))(float h)`
set paper height.
`void`
`[setPaperWidth](#setPaperWidth(float))(float w)`
set paper width.
`void`
`[setProperties](#setProperties(java.util.Properties))([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
Set properties.
`void`
`[startTag](#startTag(javax.swing.text.html.HTML.Tag,javax.swing.text.AttributeSet))([HTML.Tag](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html) tag,
 [AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html) attributes)`
Receive notification of the start of a tag.
Methods inherited from class com.nomagic.magicreport.format.html.[AbstractDocumentCreator](AbstractDocumentCreator.html)
`[createImageTool](AbstractDocumentCreator.html#createImageTool()), [getFormatter](AbstractDocumentCreator.html#getFormatter()), [getStyleByCSSParser](AbstractDocumentCreator.html#getStyleByCSSParser(java.lang.String)), [getStyledDocument](AbstractDocumentCreator.html#getStyledDocument()), [setFormatter](AbstractDocumentCreator.html#setFormatter(com.nomagic.magicreport.format.DefaultFormatter)), [setStyledDocument](AbstractDocumentCreator.html#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
HTML_TABLE_COLUMN_MINWIDTH_DEFAULT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) HTML_TABLE_COLUMN_MINWIDTH_DEFAULT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.RTFCreator.HTML_TABLE_COLUMN_MINWIDTH_DEFAULT)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
RTFCreator
public RTFCreator()
 ============ METHOD DETAIL ========== 
Method Details
convert
public void convert([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) reader,
 [Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) writer)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Convert the HTML content from reader into RTF document.
Specified by:
`[convert](../IDocumentCreator.html#convert(java.io.Reader,java.io.Writer))` in interface `[IDocumentCreator](../IDocumentCreator.html)`
Parameters:
`reader` - the reader containing HTML source.
`writer` - the writer containing RTF document.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If any IO errors occur.
comment
public void comment(char[] data)
Receive notification of comment data.
Specified by:
`[comment](IHTMLHandler.html#comment(char%5B%5D))` in interface `[IHTMLHandler](IHTMLHandler.html)`
Parameters:
`data` - An array holding the characters in the comment.
startTag
public void startTag([HTML.Tag](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html) tag,
 [AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html) attributes)
Receive notification of the start of a tag.
Specified by:
`[startTag](IHTMLHandler.html#startTag(javax.swing.text.html.HTML.Tag,javax.swing.text.AttributeSet))` in interface `[IHTMLHandler](IHTMLHandler.html)`
Parameters:
`tag` - HTML tag
`attributes` - The attributes attached to the tag. If there are no attributes, it shall be an empty
 Attributes object.
endTag
public void endTag([HTML.Tag](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html) tag)
Receive notification of the end of a tag.
Specified by:
`[endTag](IHTMLHandler.html#endTag(javax.swing.text.html.HTML.Tag))` in interface `[IHTMLHandler](IHTMLHandler.html)`
Parameters:
`tag` - HTML tag
characters
public void characters(char[] data)
Receive notification of character data inside a tag.
Specified by:
`[characters](IHTMLHandler.html#characters(char%5B%5D))` in interface `[IHTMLHandler](IHTMLHandler.html)`
Parameters:
`data` - The characters.
addTableProperties
public void addTableProperties([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) attributeName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Add tag and value of align/valign or bgcolor to stack.
Parameters:
`tagName` - tagName
`attributeName` - attributeName
`value` - value
setPaperHeight
public void setPaperHeight(float h)
set paper height.
Specified by:
`[setPaperHeight](../IDocumentCreator.html#setPaperHeight(float))` in interface `[IDocumentCreator](../IDocumentCreator.html)`
Parameters:
`h` - paper height.
See Also:
[`IDocumentCreator.setPaperHeight(float)`](../IDocumentCreator.html#setPaperHeight(float))
getPaperHeight
public double getPaperHeight()
Get paper height.
Returns:
paper height
setPaperWidth
public void setPaperWidth(float w)
set paper width.
Specified by:
`[setPaperWidth](../IDocumentCreator.html#setPaperWidth(float))` in interface `[IDocumentCreator](../IDocumentCreator.html)`
Parameters:
`w` - paper width.
See Also:
[`IDocumentCreator.setPaperWidth(float)`](../IDocumentCreator.html#setPaperWidth(float))
getPaperWidth
public double getPaperWidth()
Get paper width.
Returns:
paper width
setProperties
public void setProperties([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
Set properties.
Specified by:
`[setProperties](../IDocumentCreator.html#setProperties(java.util.Properties))` in interface `[IDocumentCreator](../IDocumentCreator.html)`
Parameters:
`properties` - properties
getProperties
public [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) getProperties()
Get properties.
Returns:
properties
checkRowSpan
public void checkRowSpan()
check rowspan when creator received tag td, th or tr.
endDocument
public void endDocument()
The Override Method.
Specified by:
`[endDocument](IHTMLHandler.html#endDocument())` in interface `[IHTMLHandler](IHTMLHandler.html)`
See Also:
[`IHTMLHandler.endDocument()`](IHTMLHandler.html#endDocument())
changeColorFormat
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) changeColorFormat([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) color)
Change color(3-digits RGB, 6-digits RGB and color name) to RGB format.
Parameters:
`color` - color format
Returns:
RGB format and return empty String when invalid color format.
setDocumentPage
public void setDocumentPage(com.nomagic.magicreport.DocumentPage page)
Description copied from interface: `[IDocumentCreator](../IDocumentCreator.html#setDocumentPage(com.nomagic.magicreport.DocumentPage))`
set document page property.
Specified by:
`[setDocumentPage](../IDocumentCreator.html#setDocumentPage(com.nomagic.magicreport.DocumentPage))` in interface `[IDocumentCreator](../IDocumentCreator.html)`
Parameters:
`page` - page property.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format.html</a></div>
<h1 class="title" title="Class RTFCreator">Class RTFCreator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="AbstractDocumentCreator.html" title="class in com.nomagic.magicreport.format.html">com.nomagic.magicreport.format.html.AbstractDocumentCreator</a>
<div class="inheritance">com.nomagic.magicreport.format.html.RTFCreator</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="IHTMLHandler.html" title="interface in com.nomagic.magicreport.format.html">IHTMLHandler</a></code>, <code><a href="../IDocumentCreator.html" title="interface in com.nomagic.magicreport.format">IDocumentCreator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">RTFCreator</span>
<span class="extends-implements">extends <a href="AbstractDocumentCreator.html" title="class in com.nomagic.magicreport.format.html">AbstractDocumentCreator</a>
implements <a href="IHTMLHandler.html" title="interface in com.nomagic.magicreport.format.html">IHTMLHandler</a></span></div>
<div class="block">The class use for create RTF content.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>May 22, 2009</dd>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#HTML_TABLE_COLUMN_MINWIDTH_DEFAULT">HTML_TABLE_COLUMN_MINWIDTH_DEFAULT</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">RTFCreator</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addTableProperties(java.lang.String,java.lang.String,java.lang.String)">addTableProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> attributeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add tag and value of align/valign or bgcolor to stack.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#changeColorFormat(java.lang.String)">changeColorFormat</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> color)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Change color(3-digits RGB, 6-digits RGB and color name) to RGB format.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#characters(char%5B%5D)">characters</a><wbr/>(char[] data)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Receive notification of character data inside a tag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkRowSpan()">checkRowSpan</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">check rowspan when creator received tag td, th or tr.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#comment(char%5B%5D)">comment</a><wbr/>(char[] data)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Receive notification of comment data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#convert(java.io.Reader,java.io.Writer)">convert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> reader,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> writer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert the HTML content from reader into RTF document.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#endDocument()">endDocument</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The Override Method.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#endTag(javax.swing.text.html.HTML.Tag)">endTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html" title="class or interface in javax.swing.text.html">HTML.Tag</a> tag)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Receive notification of the end of a tag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPaperHeight()">getPaperHeight</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get paper height.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPaperWidth()">getPaperWidth</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get paper width.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperties()">getProperties</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDocumentPage(com.nomagic.magicreport.DocumentPage)">setDocumentPage</a><wbr/>(com.nomagic.magicreport.DocumentPage page)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">set document page property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPaperHeight(float)">setPaperHeight</a><wbr/>(float h)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">set paper height.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPaperWidth(float)">setPaperWidth</a><wbr/>(float w)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">set paper width.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperties(java.util.Properties)">setProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#startTag(javax.swing.text.html.HTML.Tag,javax.swing.text.AttributeSet)">startTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html" title="class or interface in javax.swing.text.html">HTML.Tag</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a> attributes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Receive notification of the start of a tag.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.format.html.AbstractDocumentCreator">Methods inherited from class com.nomagic.magicreport.format.html.<a href="AbstractDocumentCreator.html" title="class in com.nomagic.magicreport.format.html">AbstractDocumentCreator</a></h3>
<code><a href="AbstractDocumentCreator.html#createImageTool()">createImageTool</a>, <a href="AbstractDocumentCreator.html#getFormatter()">getFormatter</a>, <a href="AbstractDocumentCreator.html#getStyleByCSSParser(java.lang.String)">getStyleByCSSParser</a>, <a href="AbstractDocumentCreator.html#getStyledDocument()">getStyledDocument</a>, <a href="AbstractDocumentCreator.html#setFormatter(com.nomagic.magicreport.format.DefaultFormatter)">setFormatter</a>, <a href="AbstractDocumentCreator.html#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument)">setStyledDocument</a></code></div>
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
<section class="detail" id="HTML_TABLE_COLUMN_MINWIDTH_DEFAULT">
<h3>HTML_TABLE_COLUMN_MINWIDTH_DEFAULT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HTML_TABLE_COLUMN_MINWIDTH_DEFAULT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.RTFCreator.HTML_TABLE_COLUMN_MINWIDTH_DEFAULT">Constant Field Values</a></li>
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
<h3>RTFCreator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RTFCreator</span>()</div>
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
<section class="detail" id="convert(java.io.Reader,java.io.Writer)">
<h3>convert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">convert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> reader,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> writer)</span>
             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Convert the HTML content from reader into RTF document.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IDocumentCreator.html#convert(java.io.Reader,java.io.Writer)">convert</a></code> in interface <code><a href="../IDocumentCreator.html" title="interface in com.nomagic.magicreport.format">IDocumentCreator</a></code></dd>
<dt>Parameters:</dt>
<dd><code>reader</code> - the reader containing HTML source.</dd>
<dd><code>writer</code> - the writer containing RTF document.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If any IO errors occur.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="comment(char[])">
<h3>comment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">comment</span><wbr/><span class="parameters">(char[] data)</span></div>
<div class="block">Receive notification of comment data.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IHTMLHandler.html#comment(char%5B%5D)">comment</a></code> in interface <code><a href="IHTMLHandler.html" title="interface in com.nomagic.magicreport.format.html">IHTMLHandler</a></code></dd>
<dt>Parameters:</dt>
<dd><code>data</code> - An array holding the characters in the comment.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="startTag(javax.swing.text.html.HTML.Tag,javax.swing.text.AttributeSet)">
<h3>startTag</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html" title="class or interface in javax.swing.text.html">HTML.Tag</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a> attributes)</span></div>
<div class="block">Receive notification of the start of a tag.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IHTMLHandler.html#startTag(javax.swing.text.html.HTML.Tag,javax.swing.text.AttributeSet)">startTag</a></code> in interface <code><a href="IHTMLHandler.html" title="interface in com.nomagic.magicreport.format.html">IHTMLHandler</a></code></dd>
<dt>Parameters:</dt>
<dd><code>tag</code> - HTML tag</dd>
<dd><code>attributes</code> - The attributes attached to the tag. If there are no attributes, it shall be an empty
           Attributes object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="endTag(javax.swing.text.html.HTML.Tag)">
<h3>endTag</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">endTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html" title="class or interface in javax.swing.text.html">HTML.Tag</a> tag)</span></div>
<div class="block">Receive notification of the end of a tag.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IHTMLHandler.html#endTag(javax.swing.text.html.HTML.Tag)">endTag</a></code> in interface <code><a href="IHTMLHandler.html" title="interface in com.nomagic.magicreport.format.html">IHTMLHandler</a></code></dd>
<dt>Parameters:</dt>
<dd><code>tag</code> - HTML tag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="characters(char[])">
<h3>characters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">characters</span><wbr/><span class="parameters">(char[] data)</span></div>
<div class="block">Receive notification of character data inside a tag.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IHTMLHandler.html#characters(char%5B%5D)">characters</a></code> in interface <code><a href="IHTMLHandler.html" title="interface in com.nomagic.magicreport.format.html">IHTMLHandler</a></code></dd>
<dt>Parameters:</dt>
<dd><code>data</code> - The characters.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addTableProperties(java.lang.String,java.lang.String,java.lang.String)">
<h3>addTableProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addTableProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> attributeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Add tag and value of align/valign or bgcolor to stack.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tagName</code> - tagName</dd>
<dd><code>attributeName</code> - attributeName</dd>
<dd><code>value</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPaperHeight(float)">
<h3>setPaperHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPaperHeight</span><wbr/><span class="parameters">(float h)</span></div>
<div class="block">set paper height.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IDocumentCreator.html#setPaperHeight(float)">setPaperHeight</a></code> in interface <code><a href="../IDocumentCreator.html" title="interface in com.nomagic.magicreport.format">IDocumentCreator</a></code></dd>
<dt>Parameters:</dt>
<dd><code>h</code> - paper height.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../IDocumentCreator.html#setPaperHeight(float)"><code>IDocumentCreator.setPaperHeight(float)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPaperHeight()">
<h3>getPaperHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getPaperHeight</span>()</div>
<div class="block">Get paper height.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>paper height</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPaperWidth(float)">
<h3>setPaperWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPaperWidth</span><wbr/><span class="parameters">(float w)</span></div>
<div class="block">set paper width.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IDocumentCreator.html#setPaperWidth(float)">setPaperWidth</a></code> in interface <code><a href="../IDocumentCreator.html" title="interface in com.nomagic.magicreport.format">IDocumentCreator</a></code></dd>
<dt>Parameters:</dt>
<dd><code>w</code> - paper width.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../IDocumentCreator.html#setPaperWidth(float)"><code>IDocumentCreator.setPaperWidth(float)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPaperWidth()">
<h3>getPaperWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getPaperWidth</span>()</div>
<div class="block">Get paper width.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>paper width</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProperties(java.util.Properties)">
<h3>setProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">Set properties.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IDocumentCreator.html#setProperties(java.util.Properties)">setProperties</a></code> in interface <code><a href="../IDocumentCreator.html" title="interface in com.nomagic.magicreport.format">IDocumentCreator</a></code></dd>
<dt>Parameters:</dt>
<dd><code>properties</code> - properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperties()">
<h3>getProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></span> <span class="element-name">getProperties</span>()</div>
<div class="block">Get properties.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkRowSpan()">
<h3>checkRowSpan</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">checkRowSpan</span>()</div>
<div class="block">check rowspan when creator received tag td, th or tr.</div>
</section>
</li>
<li>
<section class="detail" id="endDocument()">
<h3>endDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">endDocument</span>()</div>
<div class="block">The Override Method.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IHTMLHandler.html#endDocument()">endDocument</a></code> in interface <code><a href="IHTMLHandler.html" title="interface in com.nomagic.magicreport.format.html">IHTMLHandler</a></code></dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="IHTMLHandler.html#endDocument()"><code>IHTMLHandler.endDocument()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="changeColorFormat(java.lang.String)">
<h3>changeColorFormat</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">changeColorFormat</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> color)</span></div>
<div class="block">Change color(3-digits RGB, 6-digits RGB and color name) to RGB format.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>color</code> - color format</dd>
<dt>Returns:</dt>
<dd>RGB format and return empty String when invalid color format.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDocumentPage(com.nomagic.magicreport.DocumentPage)">
<h3>setDocumentPage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDocumentPage</span><wbr/><span class="parameters">(com.nomagic.magicreport.DocumentPage page)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="../IDocumentCreator.html#setDocumentPage(com.nomagic.magicreport.DocumentPage)">IDocumentCreator</a></code></span></div>
<div class="block">set document page property.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IDocumentCreator.html#setDocumentPage(com.nomagic.magicreport.DocumentPage)">setDocumentPage</a></code> in interface <code><a href="../IDocumentCreator.html" title="interface in com.nomagic.magicreport.format">IDocumentCreator</a></code></dd>
<dt>Parameters:</dt>
<dd><code>page</code> - page property.</dd>
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
