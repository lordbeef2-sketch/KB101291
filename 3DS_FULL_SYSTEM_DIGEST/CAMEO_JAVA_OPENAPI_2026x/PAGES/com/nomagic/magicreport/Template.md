# JAVA OPENAPI: Template (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/Template.html
- source_path: `com/nomagic/magicreport/Template.html`
- source_sha256: `a9a1c6af9410ad37ff35726f1a4e262db143c9b5a67a479b090367cbd5758c25`
- captured_utc: `2026-07-14T16:58:36.022270+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport](package-summary.html)

## Class Template

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.Template

All Implemented Interfaces:
`[IObserverMessage](engine/IObserverMessage.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`

Direct Known Subclasses:
`[ODFTemplate](ODFTemplate.html)`, `[OOXMLTemplate](OOXMLTemplate.html)`

@OpenApiAllpublic classTemplate
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [IObserverMessage](engine/IObserverMessage.html)

This class is used for representing template and controlling template operations.

Since:
Jun 11, 2007 11:52:45 PM
Version:
1.0 Jun 11, 2007
See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.magicreport.Template)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Template](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[finalizeOutput](#finalizeOutput())()`
Finalize the output before terminate this object.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Return a name of template.
`[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
`[getReader](#getReader())()`
Return Reader that contains the template.
`long`
`[getSize](#getSize())()`
Return a size of template.
`[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)`
`[getWriter](#getWriter())()`
Return Writer that contains the output.
`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Set a name of template.
`void`
`[setReader](#setReader(java.io.Reader))([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) reader)`
Set Reader that contains the template.
`void`
`[setSize](#setSize(long))(long templateSize)`
Set a size of template.
`void`
`[setWriter](#setWriter(java.io.Writer))([Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) writer)`
Set Writer that contains the output.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Template
public Template()
 ============ METHOD DETAIL ========== 
Method Details
getName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName()
Return a name of template.
Specified by:
`[getName](engine/IObserverMessage.html#getName())` in interface `[IObserverMessage](engine/IObserverMessage.html)`
Returns:
the name of template
setName
public void setName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Set a name of template.
Parameters:
`name` - the name to set
getReader
public [Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) getReader()
Return Reader that contains the template.
Returns:
Reader that contains the template.
setReader
public void setReader([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) reader)
Set Reader that contains the template.
Parameters:
`reader` - Reader that contains the template.
getWriter
public [Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) getWriter()
Return Writer that contains the output.
Returns:
Reader that contains the template.
setWriter
public void setWriter([Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) writer)
Set Writer that contains the output.
Parameters:
`writer` - Writer that contains the output.
getSize
public long getSize()
Return a size of template.
Returns:
the template size
setSize
public void setSize(long templateSize)
Set a size of template.
Parameters:
`templateSize` - the template size to set
finalizeOutput
public void finalizeOutput()
Finalize the output before terminate this object.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport</a></div>
<h1 class="title" title="Class Template">Class Template</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.Template</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="engine/IObserverMessage.html" title="interface in com.nomagic.magicreport.engine">IObserverMessage</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ODFTemplate.html" title="class in com.nomagic.magicreport">ODFTemplate</a></code>, <code><a href="OOXMLTemplate.html" title="class in com.nomagic.magicreport">OOXMLTemplate</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Template</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="engine/IObserverMessage.html" title="interface in com.nomagic.magicreport.engine">IObserverMessage</a></span></div>
<div class="block">This class is used for representing template and controlling template operations.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 11, 2007 11:52:45 PM</dd>
<dt>Version:</dt>
<dd>1.0 Jun 11, 2007</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../serialized-form.html#com.nomagic.magicreport.Template">Serialized Form</a></li>
</ul>
</dd>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Template</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#finalizeOutput()">finalizeOutput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finalize the output before terminate this object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a name of template.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReader()">getReader</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return Reader that contains the template.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSize()">getSize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a size of template.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWriter()">getWriter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return Writer that contains the output.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a name of template.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setReader(java.io.Reader)">setReader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> reader)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Reader that contains the template.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSize(long)">setSize</a><wbr/>(long templateSize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a size of template.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWriter(java.io.Writer)">setWriter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> writer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Writer that contains the output.</div>
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
<h3>Template</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Template</span>()</div>
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
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Return a name of template.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="engine/IObserverMessage.html#getName()">getName</a></code> in interface <code><a href="engine/IObserverMessage.html" title="interface in com.nomagic.magicreport.engine">IObserverMessage</a></code></dd>
<dt>Returns:</dt>
<dd>the name of template</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Set a name of template.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReader()">
<h3>getReader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></span> <span class="element-name">getReader</span>()</div>
<div class="block">Return Reader that contains the template.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Reader that contains the template.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReader(java.io.Reader)">
<h3>setReader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setReader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> reader)</span></div>
<div class="block">Set Reader that contains the template.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reader</code> - Reader that contains the template.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWriter()">
<h3>getWriter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></span> <span class="element-name">getWriter</span>()</div>
<div class="block">Return Writer that contains the output.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Reader that contains the template.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWriter(java.io.Writer)">
<h3>setWriter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setWriter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> writer)</span></div>
<div class="block">Set Writer that contains the output.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>writer</code> - Writer that contains the output.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSize()">
<h3>getSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getSize</span>()</div>
<div class="block">Return a size of template.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the template size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSize(long)">
<h3>setSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSize</span><wbr/><span class="parameters">(long templateSize)</span></div>
<div class="block">Set a size of template.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateSize</code> - the template size to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="finalizeOutput()">
<h3>finalizeOutput</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">finalizeOutput</span>()</div>
<div class="block">Finalize the output before terminate this object.</div>
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
