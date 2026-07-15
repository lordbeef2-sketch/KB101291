# JAVA OPENAPI: IFormatter (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/format/IFormatter.html
- source_path: `com/nomagic/magicreport/format/IFormatter.html`
- source_sha256: `6509ef35e7c882f621e4f5290fd9259a040b991e1adc5077fb7e3305d145cb39`
- captured_utc: `2026-07-14T16:46:13.741984+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format](package-summary.html)

## Interface IFormatter

All Known Implementing Classes:
`[DefaultFormatter](DefaultFormatter.html)`, `[DocBookFormatter](DocBookFormatter.html)`, `[DOCXFormatter](DOCXFormatter.html)`, `[HTMLFormatter](HTMLFormatter.html)`, `[LaTeXFormatter](LaTeXFormatter.html)`, `[PPTXFormatter](PPTXFormatter.html)`, `[RTFFormatter](RTFFormatter.html)`, `[TextFormatter](TextFormatter.html)`, `[XLSXFormatter](XLSXFormatter.html)`, `[XMLFormatter](XMLFormatter.html)`

@OpenApiAllpublic interfaceIFormatter

This interface provides support for object layout, common formats for numeric, string, date/time and data.

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
`static final int`
`[DOT_PER_INCH](#DOT_PER_INCH)`
Default dot per inch value.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[format](#format(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Convert an Object value into desire format.
`[IFormatter](IFormatter.html)`
`[getObjectFormater](#getObjectFormater(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> targetType)`
Returns the formatter for the target type class or current formatter if target type class is not registered.
`void`
`[registerObjectFormatter](#registerObjectFormatter(java.lang.Class,com.nomagic.magicreport.format.IFormatter))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> targetType,
 [IFormatter](IFormatter.html) formatter)`
Register an object formatter to be used to format values of a given target class.
`void`
`[setStyledDocument](#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument))([StyledDocument](html/StyledDocument.html) styledDocument)`
Set a [`StyledDocument`](html/StyledDocument.html) to be used with this formatter.

============ FIELD DETAIL =========== 
Field Details
DOT_PER_INCH
static final int DOT_PER_INCH
Default dot per inch value.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.format.IFormatter.DOT_PER_INCH)
 ============ METHOD DETAIL ========== 
Method Details
format
[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) format([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Convert an Object value into desire format.
Parameters:
`value` - Object value
Returns:
formatted object
registerObjectFormatter
void registerObjectFormatter([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> targetType,
 [IFormatter](IFormatter.html) formatter)
Register an object formatter to be used to format values of a given target class.
Parameters:
`targetType` - the Class object of the type to be formatted
`formatter` - the instance of object of the [`IFormatter`](IFormatter.html) class. If this is null, then any existing
 definition will be removed.
getObjectFormater
[IFormatter](IFormatter.html) getObjectFormater([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> targetType)
Returns the formatter for the target type class or current formatter if target type class is not registered.
Parameters:
`targetType` - the Class object of the type to be formatted
Returns:
the instance of object of the [`IFormatter`](IFormatter.html) class.
setStyledDocument
void setStyledDocument([StyledDocument](html/StyledDocument.html) styledDocument)
Set a [`StyledDocument`](html/StyledDocument.html) to be used with this formatter.
Parameters:
`styledDocument` - A {link StyledDocument}

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format</a></div>
<h1 class="title" title="Interface IFormatter">Interface IFormatter</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="DefaultFormatter.html" title="class in com.nomagic.magicreport.format">DefaultFormatter</a></code>, <code><a href="DocBookFormatter.html" title="class in com.nomagic.magicreport.format">DocBookFormatter</a></code>, <code><a href="DOCXFormatter.html" title="class in com.nomagic.magicreport.format">DOCXFormatter</a></code>, <code><a href="HTMLFormatter.html" title="class in com.nomagic.magicreport.format">HTMLFormatter</a></code>, <code><a href="LaTeXFormatter.html" title="class in com.nomagic.magicreport.format">LaTeXFormatter</a></code>, <code><a href="PPTXFormatter.html" title="class in com.nomagic.magicreport.format">PPTXFormatter</a></code>, <code><a href="RTFFormatter.html" title="class in com.nomagic.magicreport.format">RTFFormatter</a></code>, <code><a href="TextFormatter.html" title="class in com.nomagic.magicreport.format">TextFormatter</a></code>, <code><a href="XLSXFormatter.html" title="class in com.nomagic.magicreport.format">XLSXFormatter</a></code>, <code><a href="XMLFormatter.html" title="class in com.nomagic.magicreport.format">XMLFormatter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IFormatter</span></div>
<div class="block">This interface provides support for object layout, common formats for numeric, string, date/time and data.</div>
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
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOT_PER_INCH">DOT_PER_INCH</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default dot per inch value.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#format(java.lang.Object)">format</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Convert an Object value into desire format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getObjectFormater(java.lang.Class)">getObjectFormater</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; targetType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the formatter for the target type class or current formatter if target type class is not registered.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#registerObjectFormatter(java.lang.Class,com.nomagic.magicreport.format.IFormatter)">registerObjectFormatter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; targetType,
 <a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a> formatter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Register an object formatter to be used to format values of a given target class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument)">setStyledDocument</a><wbr/>(<a href="html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a> styledDocument)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set a <a href="html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html"><code>StyledDocument</code></a> to be used with this formatter.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="DOT_PER_INCH">
<h3>DOT_PER_INCH</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DOT_PER_INCH</span></div>
<div class="block">Default dot per inch value.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.format.IFormatter.DOT_PER_INCH">Constant Field Values</a></li>
</ul>
</dd>
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
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">format</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Convert an Object value into desire format.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - Object value</dd>
<dt>Returns:</dt>
<dd>formatted object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerObjectFormatter(java.lang.Class,com.nomagic.magicreport.format.IFormatter)">
<h3>registerObjectFormatter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">registerObjectFormatter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; targetType,
 <a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a> formatter)</span></div>
<div class="block">Register an object formatter to be used to format values of a given target class.</div>
<dl class="notes">
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
<div class="member-signature"><span class="return-type"><a href="IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></span> <span class="element-name">getObjectFormater</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; targetType)</span></div>
<div class="block">Returns the formatter for the target type class or current formatter if target type class is not registered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetType</code> - the Class object of the type to be formatted</dd>
<dt>Returns:</dt>
<dd>the instance of object of the <a href="IFormatter.html" title="interface in com.nomagic.magicreport.format"><code>IFormatter</code></a> class.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument)">
<h3>setStyledDocument</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setStyledDocument</span><wbr/><span class="parameters">(<a href="html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a> styledDocument)</span></div>
<div class="block">Set a <a href="html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html"><code>StyledDocument</code></a> to be used with this formatter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>styledDocument</code> - A {link StyledDocument}</dd>
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
