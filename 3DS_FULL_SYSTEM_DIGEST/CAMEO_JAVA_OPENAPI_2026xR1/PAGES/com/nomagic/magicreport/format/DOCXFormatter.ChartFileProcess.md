# JAVA OPENAPI: DOCXFormatter.ChartFileProcess (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/format/DOCXFormatter.ChartFileProcess.html
- source_path: `com/nomagic/magicreport/format/DOCXFormatter.ChartFileProcess.html`
- source_sha256: `31d5cf4457e9e202a43481a0b20c937f66ed2d445b9452df0acd7125ea0c9297`
- captured_utc: `2026-07-14T16:46:13.806985+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format](package-summary.html)

## Class DOCXFormatter.ChartFileProcess

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[org.xml.sax.helpers.DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)
com.nomagic.magicreport.format.DOCXFormatter.ChartFileProcess

All Implemented Interfaces:
`[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)`, `[DTDHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/DTDHandler.html)`, `[EntityResolver](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/EntityResolver.html)`, `[ErrorHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ErrorHandler.html)`

Enclosing class:
`[DOCXFormatter](DOCXFormatter.html)`

public static classDOCXFormatter.ChartFileProcess
extends [DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ChartFileProcess](#%3Cinit%3E(int))(int chartId)`
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

`void`
`[endElement](#endElement(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)`

`[StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[getContent](#getContent())()`

`void`
`[startElement](#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) namespaceURI,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)`

`protected void`
`[writeAttributes](#writeAttributes(java.lang.String,org.xml.sax.Attributes))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)`
Methods inherited from class org.xml.sax.helpers.[DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)
`[endDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endDocument()), [endPrefixMapping](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endPrefixMapping(java.lang.String)), [error](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#error(org.xml.sax.SAXParseException)), [fatalError](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#fatalError(org.xml.sax.SAXParseException)), [ignorableWhitespace](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#ignorableWhitespace(char%5B%5D,int,int)), [notationDecl](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#notationDecl(java.lang.String,java.lang.String,java.lang.String)), [processingInstruction](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#processingInstruction(java.lang.String,java.lang.String)), [resolveEntity](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#resolveEntity(java.lang.String,java.lang.String)), [setDocumentLocator](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#setDocumentLocator(org.xml.sax.Locator)), [skippedEntity](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#skippedEntity(java.lang.String)), [startDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startDocument()), [startPrefixMapping](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startPrefixMapping(java.lang.String,java.lang.String)), [unparsedEntityDecl](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#unparsedEntityDecl(java.lang.String,java.lang.String,java.lang.String,java.lang.String)), [warning](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#warning(org.xml.sax.SAXParseException))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface org.xml.sax.[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)
`[declaration](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#declaration(java.lang.String,java.lang.String,java.lang.String))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ChartFileProcess
public ChartFileProcess(int chartId)
 ============ METHOD DETAIL ========== 
Method Details
startElement
public void startElement([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) namespaceURI,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Specified by:
`[startElement](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes))` in interface `[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)`
Overrides:
`[startElement](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes))` in class `[DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)`
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)`
writeAttributes
protected void writeAttributes([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)`
characters
public void characters(char[] ch,
 int start,
 int length)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Specified by:
`[characters](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#characters(char%5B%5D,int,int))` in interface `[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)`
Overrides:
`[characters](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#characters(char%5B%5D,int,int))` in class `[DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)`
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)`
endElement
public void endElement([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Specified by:
`[endElement](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#endElement(java.lang.String,java.lang.String,java.lang.String))` in interface `[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)`
Overrides:
`[endElement](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endElement(java.lang.String,java.lang.String,java.lang.String))` in class `[DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)`
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)`
getContent
public [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) getContent()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format</a></div>
<h1 class="title" title="Class DOCXFormatter.ChartFileProcess">Class DOCXFormatter.ChartFileProcess</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">org.xml.sax.helpers.DefaultHandler</a>
<div class="inheritance">com.nomagic.magicreport.format.DOCXFormatter.ChartFileProcess</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html" title="class or interface in org.xml.sax">ContentHandler</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/DTDHandler.html" title="class or interface in org.xml.sax">DTDHandler</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/EntityResolver.html" title="class or interface in org.xml.sax">EntityResolver</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ErrorHandler.html" title="class or interface in org.xml.sax">ErrorHandler</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="DOCXFormatter.html" title="class in com.nomagic.magicreport.format">DOCXFormatter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">DOCXFormatter.ChartFileProcess</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></span></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(int)">ChartFileProcess</a><wbr/>(int chartId)</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#characters(char%5B%5D,int,int)">characters</a><wbr/>(char[] ch,
 int start,
 int length)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#endElement(java.lang.String,java.lang.String,java.lang.String)">endElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContent()">getContent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)">startElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> namespaceURI,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> attributes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeAttributes(java.lang.String,org.xml.sax.Attributes)">writeAttributes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> attributes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.xml.sax.helpers.DefaultHandler">Methods inherited from class org.xml.sax.helpers.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endDocument()" title="class or interface in org.xml.sax.helpers">endDocument</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endPrefixMapping(java.lang.String)" title="class or interface in org.xml.sax.helpers">endPrefixMapping</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#error(org.xml.sax.SAXParseException)" title="class or interface in org.xml.sax.helpers">error</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#fatalError(org.xml.sax.SAXParseException)" title="class or interface in org.xml.sax.helpers">fatalError</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#ignorableWhitespace(char%5B%5D,int,int)" title="class or interface in org.xml.sax.helpers">ignorableWhitespace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#notationDecl(java.lang.String,java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">notationDecl</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#processingInstruction(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">processingInstruction</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#resolveEntity(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">resolveEntity</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#setDocumentLocator(org.xml.sax.Locator)" title="class or interface in org.xml.sax.helpers">setDocumentLocator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#skippedEntity(java.lang.String)" title="class or interface in org.xml.sax.helpers">skippedEntity</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startDocument()" title="class or interface in org.xml.sax.helpers">startDocument</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startPrefixMapping(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">startPrefixMapping</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#unparsedEntityDecl(java.lang.String,java.lang.String,java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">unparsedEntityDecl</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#warning(org.xml.sax.SAXParseException)" title="class or interface in org.xml.sax.helpers">warning</a></code></div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(int)">
<h3>ChartFileProcess</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ChartFileProcess</span><wbr/><span class="parameters">(int chartId)</span></div>
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
<section class="detail" id="startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)">
<h3>startElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> namespaceURI,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> attributes)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)" title="class or interface in org.xml.sax">startElement</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html" title="class or interface in org.xml.sax">ContentHandler</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)" title="class or interface in org.xml.sax.helpers">startElement</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeAttributes(java.lang.String,org.xml.sax.Attributes)">
<h3>writeAttributes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">writeAttributes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> attributes)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code></dd>
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
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#characters(char%5B%5D,int,int)" title="class or interface in org.xml.sax">characters</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html" title="class or interface in org.xml.sax">ContentHandler</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#characters(char%5B%5D,int,int)" title="class or interface in org.xml.sax.helpers">characters</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code></dd>
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
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#endElement(java.lang.String,java.lang.String,java.lang.String)" title="class or interface in org.xml.sax">endElement</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html" title="class or interface in org.xml.sax">ContentHandler</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endElement(java.lang.String,java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">endElement</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContent()">
<h3>getContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">getContent</span>()</div>
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
