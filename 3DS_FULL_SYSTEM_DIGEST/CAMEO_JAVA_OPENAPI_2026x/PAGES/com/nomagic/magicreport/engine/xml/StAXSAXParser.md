# JAVA OPENAPI: StAXSAXParser (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/xml/StAXSAXParser.html
- source_path: `com/nomagic/magicreport/engine/xml/StAXSAXParser.html`
- source_sha256: `77c96749d3f4055c9a3371a87ed295b1e16771bdd7a40b3abfee3698f1e4eb86`
- captured_utc: `2026-07-14T16:58:38.182294+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.xml](package-summary.html)

## Class StAXSAXParser

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.engine.xml.StAXSAXParser

@OpenApiAllpublic classStAXSAXParser
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Provides a SAX interface for reading an XML document using StAX parser.

Since:
Dec 24, 2009

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[StAXSAXParser](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[parse](#parse(java.io.InputStream,org.xml.sax.helpers.DefaultHandler))([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) stream,
 [DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html) dh)`
Parse the content given InputStream as XML using the specified [`DefaultHandler`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html).
`void`
`[parse](#parse(java.io.Reader,org.xml.sax.helpers.DefaultHandler))([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) reader,
 [DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html) dh)`
Parse the content given Reader as XML using the specified [`DefaultHandler`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html).
`void`
`[parse](#parse(org.xml.sax.InputSource,org.xml.sax.helpers.DefaultHandler))([InputSource](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/InputSource.html) is,
 [DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html) dh)`
Parse the content given [`InputSource`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/InputSource.html) as XML using the specified
 [`DefaultHandler`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html).
`void`
`[setNamespaceAware](#setNamespaceAware(boolean))(boolean awareness)`
Specifies that the parser produced by this code will provide support for XML namespaces.
`void`
`[setProperty](#setProperty(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Allows the user to set specific feature/property on the underlying implementation.
`void`
`[setValidating](#setValidating(boolean))(boolean validating)`
Specifies that the parser produced by this code will validate documents as they are parsed.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
StAXSAXParser
public StAXSAXParser()
 ============ METHOD DETAIL ========== 
Method Details
setNamespaceAware
public void setNamespaceAware(boolean awareness)
Specifies that the parser produced by this code will provide support for XML namespaces. By default the
 value of this is set to `false`.
Parameters:
`awareness` - true if the parser produced by this code will provide support for XML namespaces; false
 otherwise.
setValidating
public void setValidating(boolean validating)
Specifies that the parser produced by this code will validate documents as they are parsed. By default the
 value of this is set to `false`.
Parameters:
`validating` - true if the parser produced by this code will validate documents as they are parsed; false
 otherwise.
setProperty
public void setProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)
Allows the user to set specific feature/property on the underlying implementation. The underlying
 implementation is not required to support every setting of every property in the specification and may use
 IllegalArgumentException to signal that an unsupported property may not be set with the specified value.
Parameters:
`name` - The name of the property (may not be null)
`value` - The value of the property
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if the property is not supported
parse
public void parse([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) reader,
 [DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html) dh)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html),
[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Parse the content given Reader as XML using the specified [`DefaultHandler`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html).
Parameters:
`reader` - The Reader containing the content to be parsed.
`dh` - The SAX DefaultHandler to use.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - If the `InputSource` object is `null`.
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If any IO errors occur.
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - If any SAX errors occur during processing.
See Also:
[`DocumentHandler`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/DocumentHandler.html)
parse
public void parse([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) stream,
 [DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html) dh)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html),
[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Parse the content given InputStream as XML using the specified [`DefaultHandler`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html).
Parameters:
`stream` - The InputStream containing the content to be parsed.
`dh` - The SAX DefaultHandler to use.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - If the `InputSource` object is `null`.
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If any IO errors occur.
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - If any SAX errors occur during processing.
See Also:
[`DocumentHandler`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/DocumentHandler.html)
parse
public void parse([InputSource](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/InputSource.html) is,
 [DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html) dh)
 throws [SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html),
[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Parse the content given [`InputSource`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/InputSource.html) as XML using the specified
 [`DefaultHandler`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html).
Parameters:
`is` - The InputSource containing the content to be parsed.
`dh` - The SAX DefaultHandler to use.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - If the `InputSource` object is `null`.
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If any IO errors occur.
`[SAXException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html)` - If any SAX errors occur during processing.
See Also:
[`DocumentHandler`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/DocumentHandler.html)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.xml</a></div>
<h1 class="title" title="Class StAXSAXParser">Class StAXSAXParser</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.engine.xml.StAXSAXParser</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">StAXSAXParser</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Provides a SAX interface for reading an XML document using StAX parser.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Dec 24, 2009</dd>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">StAXSAXParser</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#parse(java.io.InputStream,org.xml.sax.helpers.DefaultHandler)">parse</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> stream,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a> dh)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Parse the content given InputStream as XML using the specified <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers"><code>DefaultHandler</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#parse(java.io.Reader,org.xml.sax.helpers.DefaultHandler)">parse</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> reader,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a> dh)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Parse the content given Reader as XML using the specified <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers"><code>DefaultHandler</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#parse(org.xml.sax.InputSource,org.xml.sax.helpers.DefaultHandler)">parse</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/InputSource.html" title="class or interface in org.xml.sax">InputSource</a> is,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a> dh)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Parse the content given <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/InputSource.html" title="class or interface in org.xml.sax"><code>InputSource</code></a> as XML using the specified
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers"><code>DefaultHandler</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNamespaceAware(boolean)">setNamespaceAware</a><wbr/>(boolean awareness)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Specifies that the parser produced by this code will provide support for XML namespaces.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperty(java.lang.String,java.lang.Object)">setProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Allows the user to set specific feature/property on the underlying implementation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValidating(boolean)">setValidating</a><wbr/>(boolean validating)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Specifies that the parser produced by this code will validate documents as they are parsed.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>StAXSAXParser</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">StAXSAXParser</span>()</div>
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
<section class="detail" id="setNamespaceAware(boolean)">
<h3>setNamespaceAware</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNamespaceAware</span><wbr/><span class="parameters">(boolean awareness)</span></div>
<div class="block">Specifies that the parser produced by this code will provide support for XML namespaces. By default the
 value of this is set to <code>false</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>awareness</code> - true if the parser produced by this code will provide support for XML namespaces; false
           otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValidating(boolean)">
<h3>setValidating</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValidating</span><wbr/><span class="parameters">(boolean validating)</span></div>
<div class="block">Specifies that the parser produced by this code will validate documents as they are parsed. By default the
 value of this is set to <code>false</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>validating</code> - true if the parser produced by this code will validate documents as they are parsed; false
           otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProperty(java.lang.String,java.lang.Object)">
<h3>setProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span>
                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Allows the user to set specific feature/property on the underlying implementation. The underlying
 implementation is not required to support every setting of every property in the specification and may use
 IllegalArgumentException to signal that an unsupported property may not be set with the specified value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - The name of the property (may not be null)</dd>
<dd><code>value</code> - The value of the property</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the property is not supported</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="parse(java.io.Reader,org.xml.sax.helpers.DefaultHandler)">
<h3>parse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">parse</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> reader,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a> dh)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Parse the content given Reader as XML using the specified <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers"><code>DefaultHandler</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reader</code> - The Reader containing the content to be parsed.</dd>
<dd><code>dh</code> - The SAX DefaultHandler to use.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - If the <code>InputSource</code> object is <code>null</code>.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If any IO errors occur.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - If any SAX errors occur during processing.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/DocumentHandler.html" title="class or interface in org.xml.sax"><code>DocumentHandler</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="parse(java.io.InputStream,org.xml.sax.helpers.DefaultHandler)">
<h3>parse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">parse</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> stream,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a> dh)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Parse the content given InputStream as XML using the specified <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers"><code>DefaultHandler</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stream</code> - The InputStream containing the content to be parsed.</dd>
<dd><code>dh</code> - The SAX DefaultHandler to use.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - If the <code>InputSource</code> object is <code>null</code>.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If any IO errors occur.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - If any SAX errors occur during processing.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/DocumentHandler.html" title="class or interface in org.xml.sax"><code>DocumentHandler</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="parse(org.xml.sax.InputSource,org.xml.sax.helpers.DefaultHandler)">
<h3>parse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">parse</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/InputSource.html" title="class or interface in org.xml.sax">InputSource</a> is,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a> dh)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Parse the content given <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/InputSource.html" title="class or interface in org.xml.sax"><code>InputSource</code></a> as XML using the specified
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers"><code>DefaultHandler</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>is</code> - The InputSource containing the content to be parsed.</dd>
<dd><code>dh</code> - The SAX DefaultHandler to use.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - If the <code>InputSource</code> object is <code>null</code>.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If any IO errors occur.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXException.html" title="class or interface in org.xml.sax">SAXException</a></code> - If any SAX errors occur during processing.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/DocumentHandler.html" title="class or interface in org.xml.sax"><code>DocumentHandler</code></a></li>
</ul>
</dd>
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
