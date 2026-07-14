# JAVA OPENAPI: XMLDataHandler (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/xml/XMLDataHandler.html
- source_path: `com/nomagic/magicreport/engine/xml/XMLDataHandler.html`
- source_sha256: `61d9c27244e3e813572377d4f8cec524b8f352c47ae860f2e266545ecab463ad`
- captured_utc: `2026-07-14T16:58:38.956302+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.xml](package-summary.html)

## Class XMLDataHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[org.xml.sax.helpers.DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)
com.nomagic.magicreport.engine.xml.XMLDataHandler

All Implemented Interfaces:
`[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)`, `[DTDHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/DTDHandler.html)`, `[EntityResolver](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/EntityResolver.html)`, `[ErrorHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ErrorHandler.html)`

@OpenApiAllpublic classXMLDataHandler
extends [DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)

XML Data handler.

Since:
May 23, 2008

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)`
`[writer](#writer)`
Contains writer for this handler.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[XMLDataHandler](#%3Cinit%3E(java.io.Writer))([Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) writer)`
Create SAX handler.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[characters](#characters(char%5B%5D,int,int))(char[] ch,
 int start,
 int length)`
/** Receive notification of character data inside an element.
`void`
`[endDocument](#endDocument())()`
Receive notification of the end of the document.
`void`
`[endElement](#endElement(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)`
Receive notification of the end of an element.
`void`
`[startDocument](#startDocument())()`
Receive notification of the beginning of the document.
`void`
`[startElement](#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)`
Receive notification of the start of an element.
`protected void`
`[write](#write(char))(char c)`
Write a single character.
`protected void`
`[write](#write(char%5B%5D,int,int))(char[] cbuf,
 int off,
 int len)`
Write a portion of an array of characters.
`protected void`
`[write](#write(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string)`
Write a string.
`protected void`
`[write](#write(java.lang.StringBuffer))([StringBuffer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html) buffer)`
Write a StringBuffer.
`protected void`
`[write](#write(java.lang.StringBuilder))([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) buffer)`

`protected void`
`[writeAttributes](#writeAttributes(org.xml.sax.Attributes))([Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)`
Write all attributes to writer.
`protected void`
`[writeText](#writeText(char))(char chr)`
Filter the specified character that are sensitive to XML interpreters and write into the writer.
`protected void`
`[writeText](#writeText(char%5B%5D,int,int))(char[] cbuf,
 int off,
 int len)`
Filter the specified character that are sensitive to XML interpreters and write a portion of an array of
 characters into the writer.
`protected void`
`[writeText](#writeText(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) buffer)`
Filter the specified character that are sensitive to XML interpreters and write a StringBuffer into the
 writer.
Methods inherited from class org.xml.sax.helpers.[DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)
`[endPrefixMapping](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endPrefixMapping(java.lang.String)), [error](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#error(org.xml.sax.SAXParseException)), [fatalError](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#fatalError(org.xml.sax.SAXParseException)), [ignorableWhitespace](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#ignorableWhitespace(char%5B%5D,int,int)), [notationDecl](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#notationDecl(java.lang.String,java.lang.String,java.lang.String)), [processingInstruction](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#processingInstruction(java.lang.String,java.lang.String)), [resolveEntity](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#resolveEntity(java.lang.String,java.lang.String)), [setDocumentLocator](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#setDocumentLocator(org.xml.sax.Locator)), [skippedEntity](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#skippedEntity(java.lang.String)), [startPrefixMapping](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startPrefixMapping(java.lang.String,java.lang.String)), [unparsedEntityDecl](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#unparsedEntityDecl(java.lang.String,java.lang.String,java.lang.String,java.lang.String)), [warning](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#warning(org.xml.sax.SAXParseException))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface org.xml.sax.[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)
`[declaration](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#declaration(java.lang.String,java.lang.String,java.lang.String))`

============ FIELD DETAIL =========== 
Field Details
writer
protected [Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) writer
Contains writer for this handler.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
XMLDataHandler
public XMLDataHandler([Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) writer)
Create SAX handler.
Parameters:
`writer` - output writer
 ============ METHOD DETAIL ========== 
Method Details
write
protected void write([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Write a string.
Parameters:
`string` - String to be written
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - If an I/O error occurs
write
protected void write([StringBuffer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html) buffer)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Write a StringBuffer.
Parameters:
`buffer` - StringBuffer to be written.
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - If an I/O error occurs
write
protected void write([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) buffer)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)`
write
protected void write(char c)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Write a single character.
Parameters:
`c` - int specifying a character to be written.
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - If an I/O error occurs
write
protected void write(char[] cbuf,
 int off,
 int len)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Write a portion of an array of characters.
Parameters:
`cbuf` - Array of characters
`off` - Offset from which to start writing characters
`len` - Number of characters to write
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - If an I/O error occurs
writeText
protected void writeText(char chr)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Filter the specified character that are sensitive to XML interpreters and write into the writer.
Parameters:
`chr` - int specifying a character to be written.
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - If an I/O error occurs
writeText
protected void writeText(char[] cbuf,
 int off,
 int len)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Filter the specified character that are sensitive to XML interpreters and write a portion of an array of
 characters into the writer.
Parameters:
`cbuf` - Array of characters
`off` - Offset from which to start writing characters
`len` - Number of characters to write
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - If an I/O error occurs
writeText
protected void writeText([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) buffer)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Filter the specified character that are sensitive to XML interpreters and write a StringBuffer into the
 writer.
Parameters:
`buffer` - StringBuffer
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - If an I/O error occurs
writeAttributes
protected void writeAttributes([Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Write all attributes to writer.
Parameters:
`attributes` - XML attributes
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - Any SAX exception, possibly wrapping another exception.
startDocument
public void startDocument()
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Receive notification of the beginning of the document.
 By default, write a XML document header.
Specified by:
`[startDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#startDocument())` in interface `[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)`
Overrides:
`[startDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startDocument())` in class `[DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)`
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - Any SAX exception, possibly wrapping another exception.
endDocument
public void endDocument()
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Receive notification of the end of the document.
 By default, do nothing. Application writers may override this method in a subclass to take specific actions
 at the end of a document (such as finalizing a tree or closing an output file).
Specified by:
`[endDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#endDocument())` in interface `[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)`
Overrides:
`[endDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endDocument())` in class `[DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)`
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - Any SAX exception, possibly wrapping another exception.
startElement
public void startElement([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Receive notification of the start of an element.
 By default, write a XML start tag and attributes.
Specified by:
`[startElement](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes))` in interface `[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)`
Overrides:
`[startElement](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes))` in class `[DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)`
Parameters:
`uri` - The Namespace URI, or the empty string if the element has no Namespace URI or if Namespace
 processing is not being performed.
`localName` - The local name (without prefix), or the empty string if Namespace processing is not being
 performed.
`qName` - The qualified name (with prefix), or the empty string if qualified names are not available.
`attributes` - The attributes attached to the element. If there are no attributes, it shall be an empty
 Attributes object.
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - Any SAX exception, possibly wrapping another exception.
characters
public void characters(char[] ch,
 int start,
 int length)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
/** Receive notification of character data inside an element.
 By default, write a XML text content
Specified by:
`[characters](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#characters(char%5B%5D,int,int))` in interface `[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)`
Overrides:
`[characters](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#characters(char%5B%5D,int,int))` in class `[DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)`
Parameters:
`ch` - The characters.
`start` - The start position in the character array.
`length` - The number of characters to use from the character array.
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - Any SAX exception, possibly wrapping another exception.
endElement
public void endElement([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Receive notification of the end of an element.
 By default, write a XML end tag
Specified by:
`[endElement](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#endElement(java.lang.String,java.lang.String,java.lang.String))` in interface `[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)`
Overrides:
`[endElement](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endElement(java.lang.String,java.lang.String,java.lang.String))` in class `[DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)`
Parameters:
`uri` - The Namespace URI, or the empty string if the element has no Namespace URI or if Namespace
 processing is not being performed.
`localName` - The local name (without prefix), or the empty string if Namespace processing is not being
 performed.
`qName` - The qualified name (with prefix), or the empty string if qualified names are not available.
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - Any SAX exception, possibly wrapping another exception.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.xml</a></div>
<h1 class="title" title="Class XMLDataHandler">Class XMLDataHandler</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">org.xml.sax.helpers.DefaultHandler</a>
<div class="inheritance">com.nomagic.magicreport.engine.xml.XMLDataHandler</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html" title="class or interface in org.xml.sax">ContentHandler</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/DTDHandler.html" title="class or interface in org.xml.sax">DTDHandler</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/EntityResolver.html" title="class or interface in org.xml.sax">EntityResolver</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ErrorHandler.html" title="class or interface in org.xml.sax">ErrorHandler</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">XMLDataHandler</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></span></div>
<div class="block">XML Data handler.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>May 23, 2008</dd>
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
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#writer">writer</a></code></div>
<div class="col-last even-row-color">
<div class="block">Contains writer for this handler.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.io.Writer)">XMLDataHandler</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> writer)</code></div>
<div class="col-last even-row-color">
<div class="block">Create SAX handler.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#characters(char%5B%5D,int,int)">characters</a><wbr/>(char[] ch,
 int start,
 int length)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">/** Receive notification of character data inside an element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#endDocument()">endDocument</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Receive notification of the end of the document.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#endElement(java.lang.String,java.lang.String,java.lang.String)">endElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Receive notification of the end of an element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#startDocument()">startDocument</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Receive notification of the beginning of the document.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)">startElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> attributes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Receive notification of the start of an element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(char)">write</a><wbr/>(char c)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write a single character.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(char%5B%5D,int,int)">write</a><wbr/>(char[] cbuf,
 int off,
 int len)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write a portion of an array of characters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(java.lang.String)">write</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write a string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(java.lang.StringBuffer)">write</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> buffer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write a StringBuffer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(java.lang.StringBuilder)">write</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> buffer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeAttributes(org.xml.sax.Attributes)">writeAttributes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> attributes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write all attributes to writer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeText(char)">writeText</a><wbr/>(char chr)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Filter the specified character that are sensitive to XML interpreters and write into the writer.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeText(char%5B%5D,int,int)">writeText</a><wbr/>(char[] cbuf,
 int off,
 int len)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Filter the specified character that are sensitive to XML interpreters and write a portion of an array of
 characters into the writer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeText(java.lang.CharSequence)">writeText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> buffer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Filter the specified character that are sensitive to XML interpreters and write a StringBuffer into the
 writer.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.xml.sax.helpers.DefaultHandler">Methods inherited from class org.xml.sax.helpers.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endPrefixMapping(java.lang.String)" title="class or interface in org.xml.sax.helpers">endPrefixMapping</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#error(org.xml.sax.SAXParseException)" title="class or interface in org.xml.sax.helpers">error</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#fatalError(org.xml.sax.SAXParseException)" title="class or interface in org.xml.sax.helpers">fatalError</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#ignorableWhitespace(char%5B%5D,int,int)" title="class or interface in org.xml.sax.helpers">ignorableWhitespace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#notationDecl(java.lang.String,java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">notationDecl</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#processingInstruction(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">processingInstruction</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#resolveEntity(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">resolveEntity</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#setDocumentLocator(org.xml.sax.Locator)" title="class or interface in org.xml.sax.helpers">setDocumentLocator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#skippedEntity(java.lang.String)" title="class or interface in org.xml.sax.helpers">skippedEntity</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startPrefixMapping(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">startPrefixMapping</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#unparsedEntityDecl(java.lang.String,java.lang.String,java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">unparsedEntityDecl</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#warning(org.xml.sax.SAXParseException)" title="class or interface in org.xml.sax.helpers">warning</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.xml.sax.ContentHandler">Methods inherited from interface org.xml.sax.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html" title="class or interface in org.xml.sax">ContentHandler</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#declaration(java.lang.String,java.lang.String,java.lang.String)" title="class or interface in org.xml.sax">declaration</a></code></div>
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
<section class="detail" id="writer">
<h3>writer</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></span> <span class="element-name">writer</span></div>
<div class="block">Contains writer for this handler.</div>
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
<section class="detail" id="&lt;init&gt;(java.io.Writer)">
<h3>XMLDataHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">XMLDataHandler</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> writer)</span></div>
<div class="block">Create SAX handler.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>writer</code> - output writer</dd>
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
<section class="detail" id="write(java.lang.String)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</span>
              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<div class="block">Write a string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>string</code> - String to be written</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write(java.lang.StringBuffer)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> buffer)</span>
              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<div class="block">Write a StringBuffer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>buffer</code> - StringBuffer to be written.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write(java.lang.StringBuilder)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> buffer)</span>
              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write(char)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(char c)</span>
              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<div class="block">Write a single character.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>c</code> - int specifying a character to be written.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write(char[],int,int)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(char[] cbuf,
 int off,
 int len)</span>
              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<div class="block">Write a portion of an array of characters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cbuf</code> - Array of characters</dd>
<dd><code>off</code> - Offset from which to start writing characters</dd>
<dd><code>len</code> - Number of characters to write</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeText(char)">
<h3>writeText</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">writeText</span><wbr/><span class="parameters">(char chr)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<div class="block">Filter the specified character that are sensitive to XML interpreters and write into the writer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>chr</code> - int specifying a character to be written.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeText(char[],int,int)">
<h3>writeText</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">writeText</span><wbr/><span class="parameters">(char[] cbuf,
 int off,
 int len)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<div class="block">Filter the specified character that are sensitive to XML interpreters and write a portion of an array of
 characters into the writer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cbuf</code> - Array of characters</dd>
<dd><code>off</code> - Offset from which to start writing characters</dd>
<dd><code>len</code> - Number of characters to write</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeText(java.lang.CharSequence)">
<h3>writeText</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">writeText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> buffer)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<div class="block">Filter the specified character that are sensitive to XML interpreters and write a StringBuffer into the
 writer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>buffer</code> - StringBuffer</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeAttributes(org.xml.sax.Attributes)">
<h3>writeAttributes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">writeAttributes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> attributes)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<div class="block">Write all attributes to writer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attributes</code> - XML attributes</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - Any SAX exception, possibly wrapping another exception.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="startDocument()">
<h3>startDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startDocument</span>()
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<div class="block">Receive notification of the beginning of the document.
 <p>
 By default, write a XML document header.
 </p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#startDocument()" title="class or interface in org.xml.sax">startDocument</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html" title="class or interface in org.xml.sax">ContentHandler</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startDocument()" title="class or interface in org.xml.sax.helpers">startDocument</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - Any SAX exception, possibly wrapping another exception.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="endDocument()">
<h3>endDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">endDocument</span>()
                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<div class="block">Receive notification of the end of the document.
 <p>
 By default, do nothing. Application writers may override this method in a subclass to take specific actions
 at the end of a document (such as finalizing a tree or closing an output file).
 </p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#endDocument()" title="class or interface in org.xml.sax">endDocument</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html" title="class or interface in org.xml.sax">ContentHandler</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endDocument()" title="class or interface in org.xml.sax.helpers">endDocument</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - Any SAX exception, possibly wrapping another exception.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)">
<h3>startElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> attributes)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<div class="block">Receive notification of the start of an element.
 <p>
 By default, write a XML start tag and attributes.
 </p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)" title="class or interface in org.xml.sax">startElement</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html" title="class or interface in org.xml.sax">ContentHandler</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)" title="class or interface in org.xml.sax.helpers">startElement</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></code></dd>
<dt>Parameters:</dt>
<dd><code>uri</code> - The Namespace URI, or the empty string if the element has no Namespace URI or if Namespace
           processing is not being performed.</dd>
<dd><code>localName</code> - The local name (without prefix), or the empty string if Namespace processing is not being
           performed.</dd>
<dd><code>qName</code> - The qualified name (with prefix), or the empty string if qualified names are not available.</dd>
<dd><code>attributes</code> - The attributes attached to the element. If there are no attributes, it shall be an empty
           Attributes object.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - Any SAX exception, possibly wrapping another exception.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="characters(char[],int,int)">
<h3>characters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">characters</span><wbr/><span class="parameters">(char[] ch,
 int start,
 int length)</span>
                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<div class="block">/** Receive notification of character data inside an element.
 <p>
 By default, write a XML text content
 </p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#characters(char%5B%5D,int,int)" title="class or interface in org.xml.sax">characters</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html" title="class or interface in org.xml.sax">ContentHandler</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#characters(char%5B%5D,int,int)" title="class or interface in org.xml.sax.helpers">characters</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></code></dd>
<dt>Parameters:</dt>
<dd><code>ch</code> - The characters.</dd>
<dd><code>start</code> - The start position in the character array.</dd>
<dd><code>length</code> - The number of characters to use from the character array.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - Any SAX exception, possibly wrapping another exception.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="endElement(java.lang.String,java.lang.String,java.lang.String)">
<h3>endElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">endElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName)</span>
                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<div class="block">Receive notification of the end of an element.
 <p>
 By default, write a XML end tag
 </p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#endElement(java.lang.String,java.lang.String,java.lang.String)" title="class or interface in org.xml.sax">endElement</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html" title="class or interface in org.xml.sax">ContentHandler</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endElement(java.lang.String,java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">endElement</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></code></dd>
<dt>Parameters:</dt>
<dd><code>uri</code> - The Namespace URI, or the empty string if the element has no Namespace URI or if Namespace
           processing is not being performed.</dd>
<dd><code>localName</code> - The local name (without prefix), or the empty string if Namespace processing is not being
           performed.</dd>
<dd><code>qName</code> - The qualified name (with prefix), or the empty string if qualified names are not available.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - Any SAX exception, possibly wrapping another exception.</dd>
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
