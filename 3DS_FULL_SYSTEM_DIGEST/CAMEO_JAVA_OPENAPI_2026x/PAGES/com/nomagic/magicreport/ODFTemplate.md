# JAVA OPENAPI: ODFTemplate (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/ODFTemplate.html
- source_path: `com/nomagic/magicreport/ODFTemplate.html`
- source_sha256: `986340e3030db87ea941bb022fce5c40f66382f3787cbd727708f279a145a652`
- captured_utc: `2026-07-14T16:58:35.947268+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport](package-summary.html)

## Class ODFTemplate

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicreport.Template](Template.html)
com.nomagic.magicreport.ODFTemplate

All Implemented Interfaces:
`[IObserverMessage](engine/IObserverMessage.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`

@OpenApiAllpublic classODFTemplate
extends [Template](Template.html)

ODFTemplate use for handling the ODF document. Open Document Format (ODF) is differ from other existing
 template. ODF consists of many contents and resources but all of files are zipped into single file. This class
 will unzip the template file at the beginning process and zip template at ending process.

Since:
Mar 28, 2008 1:48:19 PM
See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.magicreport.ODFTemplate)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ODFTemplate](#%3Cinit%3E())()`
Create ODF template.
`[ODFTemplate](#%3Cinit%3E(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input)`
Create ODF template.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[finalizeOutput](#finalizeOutput())()`
Finalize the output before terminate this object.
`[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[getTemplateFile](#getTemplateFile())()`
Return template file.
Methods inherited from class com.nomagic.magicreport.[Template](Template.html)
`[getName](Template.html#getName()), [getReader](Template.html#getReader()), [getSize](Template.html#getSize()), [getWriter](Template.html#getWriter()), [setName](Template.html#setName(java.lang.String)), [setReader](Template.html#setReader(java.io.Reader)), [setSize](Template.html#setSize(long)), [setWriter](Template.html#setWriter(java.io.Writer))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ODFTemplate
public ODFTemplate()
Create ODF template.
ODFTemplate
public ODFTemplate([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input)
Create ODF template.
Parameters:
`input` - template file.
 ============ METHOD DETAIL ========== 
Method Details
getTemplateFile
public [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) getTemplateFile()
Return template file.
Returns:
the template file
finalizeOutput
public void finalizeOutput()
Finalize the output before terminate this object.
Overrides:
`[finalizeOutput](Template.html#finalizeOutput())` in class `[Template](Template.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport</a></div>
<h1 class="title" title="Class ODFTemplate">Class ODFTemplate</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="Template.html" title="class in com.nomagic.magicreport">com.nomagic.magicreport.Template</a>
<div class="inheritance">com.nomagic.magicreport.ODFTemplate</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="engine/IObserverMessage.html" title="interface in com.nomagic.magicreport.engine">IObserverMessage</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ODFTemplate</span>
<span class="extends-implements">extends <a href="Template.html" title="class in com.nomagic.magicreport">Template</a></span></div>
<div class="block">ODFTemplate use for handling the ODF document. Open Document Format (ODF) is differ from other existing
 template. ODF consists of many contents and resources but all of files are zipped into single file. This class
 will unzip the template file at the beginning process and zip template at ending process.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Mar 28, 2008 1:48:19 PM</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../serialized-form.html#com.nomagic.magicreport.ODFTemplate">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ODFTemplate</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Create ODF template.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.io.File)">ODFTemplate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create ODF template.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#finalizeOutput()">finalizeOutput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finalize the output before terminate this object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateFile()">getTemplateFile</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return template file.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.Template">Methods inherited from class com.nomagic.magicreport.<a href="Template.html" title="class in com.nomagic.magicreport">Template</a></h3>
<code><a href="Template.html#getName()">getName</a>, <a href="Template.html#getReader()">getReader</a>, <a href="Template.html#getSize()">getSize</a>, <a href="Template.html#getWriter()">getWriter</a>, <a href="Template.html#setName(java.lang.String)">setName</a>, <a href="Template.html#setReader(java.io.Reader)">setReader</a>, <a href="Template.html#setSize(long)">setSize</a>, <a href="Template.html#setWriter(java.io.Writer)">setWriter</a></code></div>
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
<h3>ODFTemplate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ODFTemplate</span>()</div>
<div class="block">Create ODF template.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.io.File)">
<h3>ODFTemplate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ODFTemplate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input)</span></div>
<div class="block">Create ODF template.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - template file.</dd>
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
<section class="detail" id="getTemplateFile()">
<h3>getTemplateFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getTemplateFile</span>()</div>
<div class="block">Return template file.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the template file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="finalizeOutput()">
<h3>finalizeOutput</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">finalizeOutput</span>()</div>
<div class="block">Finalize the output before terminate this object.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Template.html#finalizeOutput()">finalizeOutput</a></code> in class <code><a href="Template.html" title="class in com.nomagic.magicreport">Template</a></code></dd>
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
