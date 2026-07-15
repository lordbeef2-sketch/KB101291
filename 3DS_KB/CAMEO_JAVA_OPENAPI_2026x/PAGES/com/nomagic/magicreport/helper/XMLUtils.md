# JAVA OPENAPI: XMLUtils (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/helper/XMLUtils.html
- source_path: `com/nomagic/magicreport/helper/XMLUtils.html`
- source_sha256: `354a1ad6c8319a15522c6de626e5fb08525aa674a7eccd0c2333f6f462a5c125`
- captured_utc: `2026-07-14T16:58:39.424310+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.helper](package-summary.html)

## Class XMLUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.helper.XMLUtils

@OpenApiAllpublic final classXMLUtils
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Provides utilities for XML.

Since:
Jan 10, 2006 5:27:40 PM

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[filter](#filter(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) value)`
Filter the specified string for characters that are sensitive to HTML interpreters, returning the string
 with these characters replaced by the corresponding character entities.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[filterExcludeLineBreak](#filterExcludeLineBreak(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Same as [`filter(CharSequence)`](#filter(java.lang.CharSequence)) but exclude line break.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[filterIncludeCustomLineBreak](#filterIncludeCustomLineBreak(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) lineBreakReplacement)`
Same as [`filter(CharSequence)`](#filter(java.lang.CharSequence)) but replace linebreak with lineBreakReplacement
`static [NodeList](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html)`
`[getElementsByTagName](#getElementsByTagName(org.w3c.dom.Element,java.lang.String))([Element](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)`
Returns a List over the direct children of the given element with the given tag name.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[htmlPlainText](#htmlPlainText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) xmlContent)`
Strip all tag element and convert all special characters to plain text.
`static void`
`[skipBOM](#skipBOM(java.io.InputStream))([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) inputStream)`
Skip the BOM character.
`static void`
`[skipBOM](#skipBOM(java.io.Reader))([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) reader)`
Skip the BOM character.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[xmlPlainText](#xmlPlainText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) xmlContent)`
Strip all tag element and convert all special characters to plain text.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
filter
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) filter([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) value)
Filter the specified string for characters that are sensitive to HTML interpreters, returning the string
 with these characters replaced by the corresponding character entities.
Parameters:
`value` - The string to be filtered and returned
Returns:
string after filtered
filterExcludeLineBreak
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) filterExcludeLineBreak([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Same as [`filter(CharSequence)`](#filter(java.lang.CharSequence)) but exclude line break. e.g. \r and \n
Parameters:
`value` - The string to be filtered and returned
Returns:
string after filtered
filterIncludeCustomLineBreak
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) filterIncludeCustomLineBreak([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) lineBreakReplacement)
Same as [`filter(CharSequence)`](#filter(java.lang.CharSequence)) but replace linebreak with lineBreakReplacement
Parameters:
`value` - The string to be filtered and returned
`lineBreakReplacement` - string to replace the linebreak
Returns:
string after filtered
htmlPlainText
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) htmlPlainText([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) xmlContent)
Strip all tag element and convert all special characters to plain text.
Parameters:
`xmlContent` - the xml content
Returns:
plain text.
xmlPlainText
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) xmlPlainText([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) xmlContent)
Strip all tag element and convert all special characters to plain text.
Parameters:
`xmlContent` - the xml content
Returns:
plain text.
getElementsByTagName
public static [NodeList](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html) getElementsByTagName([Element](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)
Returns a List over the direct children of the given element with the given tag name.
 [`Element.getElementsByTagName(String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html#getElementsByTagName(java.lang.String)) gives the corresponding elements in the whole
 descendance. This method return only direct descendance of element.
Parameters:
`element` - The parent element
`tagName` - The name of the desired child
Returns:
A List of children or zero length of List if children element is not found.
skipBOM
public static void skipBOM([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) reader)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Skip the BOM character. Some XML may contains a byte-order mark (BOM). The XML parser will get the error if
 XML contains BOM character. This method also remove or mark skip byte when reader contain BOM.
 The BOM is the Unicode character at code point U+FEFF ("zero-width no-break space") when that character is
 used to denote the endianness of a string of UCS/Unicode characters encoded in UTF-16 or UTF-32.
Parameters:
`reader` - Reader
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If the stream does not support mark(), or reset()
skipBOM
public static void skipBOM([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) inputStream)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Skip the BOM character. Some XML may contains a byte-order mark (BOM). The XML parser will get the error if
 XML contains BOM character. This method also remove or mark skip byte when reader contain BOM.
 The BOM is the Unicode character at code point U+FEFF ("zero-width no-break space") when that character is
 used to denote the endianness of a string of UCS/Unicode characters encoded in UTF-16 or UTF-32.
Parameters:
`inputStream` - InputStream
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If the stream does not support mark(), or reset()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.helper</a></div>
<h1 class="title" title="Class XMLUtils">Class XMLUtils</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.helper.XMLUtils</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">XMLUtils</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Provides utilities for XML.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jan 10, 2006 5:27:40 PM</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#filter(java.lang.CharSequence)">filter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Filter the specified string for characters that are sensitive to HTML interpreters, returning the string
 with these characters replaced by the corresponding character entities.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#filterExcludeLineBreak(java.lang.String)">filterExcludeLineBreak</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Same as <a href="#filter(java.lang.CharSequence)"><code>filter(CharSequence)</code></a> but exclude line break.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#filterIncludeCustomLineBreak(java.lang.String,java.lang.String)">filterIncludeCustomLineBreak</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lineBreakReplacement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Same as <a href="#filter(java.lang.CharSequence)"><code>filter(CharSequence)</code></a> but replace linebreak with lineBreakReplacement</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html" title="class or interface in org.w3c.dom">NodeList</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsByTagName(org.w3c.dom.Element,java.lang.String)">getElementsByTagName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html" title="class or interface in org.w3c.dom">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a List over the direct children of the given element with the given tag name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#htmlPlainText(java.lang.String)">htmlPlainText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> xmlContent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Strip all tag element and convert all special characters to plain text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#skipBOM(java.io.InputStream)">skipBOM</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> inputStream)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Skip the BOM character.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#skipBOM(java.io.Reader)">skipBOM</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> reader)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Skip the BOM character.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#xmlPlainText(java.lang.String)">xmlPlainText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> xmlContent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Strip all tag element and convert all special characters to plain text.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="filter(java.lang.CharSequence)">
<h3>filter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">filter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> value)</span></div>
<div class="block">Filter the specified string for characters that are sensitive to HTML interpreters, returning the string
 with these characters replaced by the corresponding character entities.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - The string to be filtered and returned</dd>
<dt>Returns:</dt>
<dd>string after filtered</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filterExcludeLineBreak(java.lang.String)">
<h3>filterExcludeLineBreak</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">filterExcludeLineBreak</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Same as <a href="#filter(java.lang.CharSequence)"><code>filter(CharSequence)</code></a> but exclude line break. e.g. \r and \n</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - The string to be filtered and returned</dd>
<dt>Returns:</dt>
<dd>string after filtered</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filterIncludeCustomLineBreak(java.lang.String,java.lang.String)">
<h3>filterIncludeCustomLineBreak</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">filterIncludeCustomLineBreak</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lineBreakReplacement)</span></div>
<div class="block">Same as <a href="#filter(java.lang.CharSequence)"><code>filter(CharSequence)</code></a> but replace linebreak with lineBreakReplacement</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - The string to be filtered and returned</dd>
<dd><code>lineBreakReplacement</code> - string to replace the linebreak</dd>
<dt>Returns:</dt>
<dd>string after filtered</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="htmlPlainText(java.lang.String)">
<h3>htmlPlainText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">htmlPlainText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> xmlContent)</span></div>
<div class="block">Strip all tag element and convert all special characters to plain text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>xmlContent</code> - the xml content</dd>
<dt>Returns:</dt>
<dd>plain text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="xmlPlainText(java.lang.String)">
<h3>xmlPlainText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">xmlPlainText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> xmlContent)</span></div>
<div class="block">Strip all tag element and convert all special characters to plain text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>xmlContent</code> - the xml content</dd>
<dt>Returns:</dt>
<dd>plain text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementsByTagName(org.w3c.dom.Element,java.lang.String)">
<h3>getElementsByTagName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html" title="class or interface in org.w3c.dom">NodeList</a></span> <span class="element-name">getElementsByTagName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html" title="class or interface in org.w3c.dom">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Returns a List over the direct children of the given element with the given tag name.
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html#getElementsByTagName(java.lang.String)" title="class or interface in org.w3c.dom"><code>Element.getElementsByTagName(String)</code></a> gives the corresponding elements in the whole
 descendance. This method return only direct descendance of element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - The parent element</dd>
<dd><code>tagName</code> - The name of the desired child</dd>
<dt>Returns:</dt>
<dd>A List of children or zero length of List if children element is not found.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="skipBOM(java.io.Reader)">
<h3>skipBOM</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">skipBOM</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> reader)</span>
                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Skip the BOM character. Some XML may contains a byte-order mark (BOM). The XML parser will get the error if
 XML contains BOM character. This method also remove or mark skip byte when reader contain BOM.
 <p>
 The BOM is the Unicode character at code point U+FEFF ("zero-width no-break space") when that character is
 used to denote the endianness of a string of UCS/Unicode characters encoded in UTF-16 or UTF-32.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reader</code> - Reader</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If the stream does not support mark(), or reset()</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="skipBOM(java.io.InputStream)">
<h3>skipBOM</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">skipBOM</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> inputStream)</span>
                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Skip the BOM character. Some XML may contains a byte-order mark (BOM). The XML parser will get the error if
 XML contains BOM character. This method also remove or mark skip byte when reader contain BOM.
 <p>
 The BOM is the Unicode character at code point U+FEFF ("zero-width no-break space") when that character is
 used to denote the endianness of a string of UCS/Unicode characters encoded in UTF-16 or UTF-32.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inputStream</code> - InputStream</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If the stream does not support mark(), or reset()</dd>
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
