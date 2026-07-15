# JAVA OPENAPI: XMLFormatter (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/format/XMLFormatter.html
- source_path: `com/nomagic/magicreport/format/XMLFormatter.html`
- source_sha256: `024f6b8063b6a962bca439689c51eaebe63659fdef5e50e4ac3f3e63ac2e2055`
- captured_utc: `2026-07-14T16:58:38.588298+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format](package-summary.html)

## Class XMLFormatter

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicreport.format.DefaultFormatter](DefaultFormatter.html)
com.nomagic.magicreport.format.XMLFormatter

All Implemented Interfaces:
`[IFormatter](IFormatter.html)`

@OpenApiAllpublic classXMLFormatter
extends [DefaultFormatter](DefaultFormatter.html)

This class provides implementation for XML format output. Extend from DefaultFormatter, this class provide
 additional support for BufferedImage.

Since:
Jun 20, 2008

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicreport.format.[DefaultFormatter](DefaultFormatter.html)
`[properties](DefaultFormatter.html#properties), [styledDocument](DefaultFormatter.html#styledDocument)`
Fields inherited from interface com.nomagic.magicreport.format.[IFormatter](IFormatter.html)
`[DOT_PER_INCH](IFormatter.html#DOT_PER_INCH)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[XMLFormatter](#%3Cinit%3E(java.util.Properties))([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
Create a HTML formatter with specific properties.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[format](#format(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Convert an Object value into HTML format.
Methods inherited from class com.nomagic.magicreport.format.[DefaultFormatter](DefaultFormatter.html)
`[getImageFlag](DefaultFormatter.html#getImageFlag(java.lang.String)), [getObjectFormater](DefaultFormatter.html#getObjectFormater(java.lang.Class)), [getProperties](DefaultFormatter.html#getProperties()), [registerObjectFormatter](DefaultFormatter.html#registerObjectFormatter(java.lang.Class,com.nomagic.magicreport.format.IFormatter)), [setProperties](DefaultFormatter.html#setProperties(java.util.Properties)), [setStyledDocument](DefaultFormatter.html#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument)), [writeImage](DefaultFormatter.html#writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.File,boolean)), [writeImage](DefaultFormatter.html#writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.OutputStream,boolean)), [writeImage](DefaultFormatter.html#writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.OutputStream,boolean,boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
XMLFormatter
public XMLFormatter([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
Create a HTML formatter with specific properties.
Parameters:
`properties` - template properties
 ============ METHOD DETAIL ========== 
Method Details
format
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) format([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Convert an Object value into HTML format.
Specified by:
`[format](IFormatter.html#format(java.lang.Object))` in interface `[IFormatter](IFormatter.html)`
Overrides:
`[format](DefaultFormatter.html#format(java.lang.Object))` in class `[DefaultFormatter](DefaultFormatter.html)`
Parameters:
`value` - converting value
Returns:
object in default format.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format</a></div>
<h1 class="title" title="Class XMLFormatter">Class XMLFormatter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="DefaultFormatter.html" title="class in com.nomagic.magicreport.format">com.nomagic.magicreport.format.DefaultFormatter</a>
<div class="inheritance">com.nomagic.magicreport.format.XMLFormatter</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">XMLFormatter</span>
<span class="extends-implements">extends <a href="DefaultFormatter.html" title="class in com.nomagic.magicreport.format">DefaultFormatter</a></span></div>
<div class="block">This class provides implementation for XML format output. Extend from DefaultFormatter, this class provide
 additional support for BufferedImage.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 20, 2008</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.format.DefaultFormatter">Fields inherited from class com.nomagic.magicreport.format.<a href="DefaultFormatter.html" title="class in com.nomagic.magicreport.format">DefaultFormatter</a></h3>
<code><a href="DefaultFormatter.html#properties">properties</a>, <a href="DefaultFormatter.html#styledDocument">styledDocument</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Properties)">XMLFormatter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last even-row-color">
<div class="block">Create a HTML formatter with specific properties.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#format(java.lang.Object)">format</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert an Object value into HTML format.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.format.DefaultFormatter">Methods inherited from class com.nomagic.magicreport.format.<a href="DefaultFormatter.html" title="class in com.nomagic.magicreport.format">DefaultFormatter</a></h3>
<code><a href="DefaultFormatter.html#getImageFlag(java.lang.String)">getImageFlag</a>, <a href="DefaultFormatter.html#getObjectFormater(java.lang.Class)">getObjectFormater</a>, <a href="DefaultFormatter.html#getProperties()">getProperties</a>, <a href="DefaultFormatter.html#registerObjectFormatter(java.lang.Class,com.nomagic.magicreport.format.IFormatter)">registerObjectFormatter</a>, <a href="DefaultFormatter.html#setProperties(java.util.Properties)">setProperties</a>, <a href="DefaultFormatter.html#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument)">setStyledDocument</a>, <a href="DefaultFormatter.html#writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.File,boolean)">writeImage</a>, <a href="DefaultFormatter.html#writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.OutputStream,boolean)">writeImage</a>, <a href="DefaultFormatter.html#writeImage(com.nomagic.magicreport.Image,java.lang.String,java.io.OutputStream,boolean,boolean)">writeImage</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.util.Properties)">
<h3>XMLFormatter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">XMLFormatter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">Create a HTML formatter with specific properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - template properties</dd>
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
<section class="detail" id="format(java.lang.Object)">
<h3>format</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">format</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Convert an Object value into HTML format.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IFormatter.html#format(java.lang.Object)">format</a></code> in interface <code><a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="DefaultFormatter.html#format(java.lang.Object)">format</a></code> in class <code><a href="DefaultFormatter.html" title="class in com.nomagic.magicreport.format">DefaultFormatter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - converting value</dd>
<dt>Returns:</dt>
<dd>object in default format.</dd>
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
