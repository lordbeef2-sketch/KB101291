# JAVA OPENAPI: DOCXEngine.DocumentRelationshipProcess (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/velocity/DOCXEngine.DocumentRelationshipProcess.html
- source_path: `com/nomagic/magicreport/engine/velocity/DOCXEngine.DocumentRelationshipProcess.html`
- source_sha256: `46d0462a6c7f03c946a088ac2f9fd87881a680c3bd1ae076eb45afe3811eb6fb`
- captured_utc: `2026-07-14T16:46:13.056973+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.velocity](package-summary.html)

## Class DOCXEngine.DocumentRelationshipProcess

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[org.xml.sax.helpers.DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)
com.nomagic.magicreport.engine.velocity.DOCXEngine.DocumentRelationshipProcess

All Implemented Interfaces:
`[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)`, `[DTDHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/DTDHandler.html)`, `[EntityResolver](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/EntityResolver.html)`, `[ErrorHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ErrorHandler.html)`

Enclosing class:
`[DOCXEngine](DOCXEngine.html)`

public static classDOCXEngine.DocumentRelationshipProcess
extends [DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)

Handle document relationship

Since:
July 19, 2017

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DocumentRelationshipProcess](#%3Cinit%3E(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo))([DocumentInfo](../ooxml/child/docx/DocumentInfo.html) documentInfo)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[startElement](#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) namespaceURI,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)`
Receive notification of the start of an element.
`protected void`
`[writeAttributes](#writeAttributes(org.xml.sax.Attributes))([Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)`
Methods inherited from class org.xml.sax.helpers.[DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)
`[characters](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#characters(char%5B%5D,int,int)), [endDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endDocument()), [endElement](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endElement(java.lang.String,java.lang.String,java.lang.String)), [endPrefixMapping](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endPrefixMapping(java.lang.String)), [error](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#error(org.xml.sax.SAXParseException)), [fatalError](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#fatalError(org.xml.sax.SAXParseException)), [ignorableWhitespace](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#ignorableWhitespace(char%5B%5D,int,int)), [notationDecl](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#notationDecl(java.lang.String,java.lang.String,java.lang.String)), [processingInstruction](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#processingInstruction(java.lang.String,java.lang.String)), [resolveEntity](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#resolveEntity(java.lang.String,java.lang.String)), [setDocumentLocator](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#setDocumentLocator(org.xml.sax.Locator)), [skippedEntity](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#skippedEntity(java.lang.String)), [startDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startDocument()), [startPrefixMapping](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startPrefixMapping(java.lang.String,java.lang.String)), [unparsedEntityDecl](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#unparsedEntityDecl(java.lang.String,java.lang.String,java.lang.String,java.lang.String)), [warning](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#warning(org.xml.sax.SAXParseException))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface org.xml.sax.[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)
`[declaration](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#declaration(java.lang.String,java.lang.String,java.lang.String))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DocumentRelationshipProcess
public DocumentRelationshipProcess([DocumentInfo](../ooxml/child/docx/DocumentInfo.html) documentInfo)
 ============ METHOD DETAIL ========== 
Method Details
startElement
public void startElement([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) namespaceURI,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)
Receive notification of the start of an element.
Specified by:
`[startElement](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes))` in interface `[ContentHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html)`
Overrides:
`[startElement](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes))` in class `[DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html)`
Parameters:
`namespaceURI` - The Namespace URI, or the empty string if the element has no Namespace URI or if
 Namespace processing is not being performed.
`localName` - The local name (without prefix), or the empty string if Namespace processing is not
 being performed.
`qName` - The qualified name (with prefix), or the empty string if qualified names are not available.
`attributes` - The attributes attached to the element. If there are no attributes, it shall be an
 empty Attributes object.
Throws:
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - Any SAX exception, possibly wrapping another exception.
writeAttributes
protected void writeAttributes([Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.velocity</a></div>
<h1 class="title" title="Class DOCXEngine.DocumentRelationshipProcess">Class DOCXEngine.DocumentRelationshipProcess</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">org.xml.sax.helpers.DefaultHandler</a>
<div class="inheritance">com.nomagic.magicreport.engine.velocity.DOCXEngine.DocumentRelationshipProcess</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html" title="class or interface in org.xml.sax">ContentHandler</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/DTDHandler.html" title="class or interface in org.xml.sax">DTDHandler</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/EntityResolver.html" title="class or interface in org.xml.sax">EntityResolver</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ErrorHandler.html" title="class or interface in org.xml.sax">ErrorHandler</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="DOCXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">DOCXEngine.DocumentRelationshipProcess</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></span></div>
<div class="block">Handle document relationship</div>
<dl class="notes">
<dt>Since:</dt>
<dd>July 19, 2017</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">DocumentRelationshipProcess</a><wbr/>(<a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> documentInfo)</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)">startElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> namespaceURI,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> attributes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Receive notification of the start of an element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeAttributes(org.xml.sax.Attributes)">writeAttributes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> attributes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.xml.sax.helpers.DefaultHandler">Methods inherited from class org.xml.sax.helpers.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#characters(char%5B%5D,int,int)" title="class or interface in org.xml.sax.helpers">characters</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endDocument()" title="class or interface in org.xml.sax.helpers">endDocument</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endElement(java.lang.String,java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">endElement</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#endPrefixMapping(java.lang.String)" title="class or interface in org.xml.sax.helpers">endPrefixMapping</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#error(org.xml.sax.SAXParseException)" title="class or interface in org.xml.sax.helpers">error</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#fatalError(org.xml.sax.SAXParseException)" title="class or interface in org.xml.sax.helpers">fatalError</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#ignorableWhitespace(char%5B%5D,int,int)" title="class or interface in org.xml.sax.helpers">ignorableWhitespace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#notationDecl(java.lang.String,java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">notationDecl</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#processingInstruction(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">processingInstruction</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#resolveEntity(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">resolveEntity</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#setDocumentLocator(org.xml.sax.Locator)" title="class or interface in org.xml.sax.helpers">setDocumentLocator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#skippedEntity(java.lang.String)" title="class or interface in org.xml.sax.helpers">skippedEntity</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startDocument()" title="class or interface in org.xml.sax.helpers">startDocument</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startPrefixMapping(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">startPrefixMapping</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#unparsedEntityDecl(java.lang.String,java.lang.String,java.lang.String,java.lang.String)" title="class or interface in org.xml.sax.helpers">unparsedEntityDecl</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#warning(org.xml.sax.SAXParseException)" title="class or interface in org.xml.sax.helpers">warning</a></code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">
<h3>DocumentRelationshipProcess</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DocumentRelationshipProcess</span><wbr/><span class="parameters">(<a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> documentInfo)</span></div>
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
<div class="block">Receive notification of the start of an element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)" title="class or interface in org.xml.sax">startElement</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html" title="class or interface in org.xml.sax">ContentHandler</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)" title="class or interface in org.xml.sax.helpers">startElement</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a></code></dd>
<dt>Parameters:</dt>
<dd><code>namespaceURI</code> - The Namespace URI, or the empty string if the element has no Namespace URI or if
           Namespace processing is not being performed.</dd>
<dd><code>localName</code> - The local name (without prefix), or the empty string if Namespace processing is not
           being performed.</dd>
<dd><code>qName</code> - The qualified name (with prefix), or the empty string if qualified names are not available.</dd>
<dd><code>attributes</code> - The attributes attached to the element. If there are no attributes, it shall be an
           empty Attributes object.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - Any SAX exception, possibly wrapping another exception.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeAttributes(org.xml.sax.Attributes)">
<h3>writeAttributes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">writeAttributes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> attributes)</span></div>
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
