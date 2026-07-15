# JAVA OPENAPI: SerialFieldTag (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/reportwizard/tools/doc/javadoc/SerialFieldTag.html
- source_path: `com/nomagic/reportwizard/tools/doc/javadoc/SerialFieldTag.html`
- source_sha256: `2e3e2fc2092baef49e9083e64beaafbb3ca8e0b6587b0bd15dfe8e05870a7cc1`
- captured_utc: `2026-07-14T16:58:40.262316+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.doc.javadoc](package-summary.html)

## Class SerialFieldTag

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.reportwizard.tools.doc.javadoc.TagImpl](TagImpl.html)
com.nomagic.reportwizard.tools.doc.javadoc.SerialFieldTag

All Implemented Interfaces:
`[Tag](../Tag.html)`

@OpenApiAllpublic classSerialFieldTag
extends [TagImpl](TagImpl.html)

Represents a @serialField tag.

Since:
Sep 3, 2008

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SerialFieldTag](#%3Cinit%3E(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) kind,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Create a serial field tag.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[ITool.HTMLString](../../../../magicreport/engine/ITool.HTMLString.html)`
`[getFieldDescription](#getFieldDescription())()`
Return the field comment.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getFieldName](#getFieldName())()`
Return the serializable field name.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getFieldType](#getFieldType())()`
Return the field type string.
`[ITool.HTMLString](../../../../magicreport/engine/ITool.HTMLString.html)`
`[getText](#getText())()`
Return the text of this tag.
Methods inherited from class com.nomagic.reportwizard.tools.doc.javadoc.[TagImpl](TagImpl.html)
`[getInlineTags](TagImpl.html#getInlineTags()), [getKind](TagImpl.html#getKind()), [getRawText](TagImpl.html#getRawText()), [toString](TagImpl.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SerialFieldTag
public SerialFieldTag([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) kind,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Create a serial field tag.
Parameters:
`kind` - the kind of tag that this Tag represents
`text` - the text of this tag
 ============ METHOD DETAIL ========== 
Method Details
getFieldName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getFieldName()
Return the serializable field name.
Returns:
the serializable field name
getFieldDescription
public [ITool.HTMLString](../../../../magicreport/engine/ITool.HTMLString.html) getFieldDescription()
Return the field comment.
Returns:
the field comment
getFieldType
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getFieldType()
Return the field type string.
Returns:
the field type string
getText
public [ITool.HTMLString](../../../../magicreport/engine/ITool.HTMLString.html) getText()
Return the text of this tag.
Specified by:
`[getText](../Tag.html#getText())` in interface `[Tag](../Tag.html)`
Overrides:
`[getText](TagImpl.html#getText())` in class `[TagImpl](TagImpl.html)`
Returns:
the text of this tag

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.doc.javadoc</a></div>
<h1 class="title" title="Class SerialFieldTag">Class SerialFieldTag</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="TagImpl.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">com.nomagic.reportwizard.tools.doc.javadoc.TagImpl</a>
<div class="inheritance">com.nomagic.reportwizard.tools.doc.javadoc.SerialFieldTag</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SerialFieldTag</span>
<span class="extends-implements">extends <a href="TagImpl.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">TagImpl</a></span></div>
<div class="block">Represents a @serialField tag.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Sep 3, 2008</dd>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String)">SerialFieldTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> kind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color">
<div class="block">Create a serial field tag.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFieldDescription()">getFieldDescription</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the field comment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFieldName()">getFieldName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the serializable field name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFieldType()">getFieldType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the field type string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the text of this tag.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.reportwizard.tools.doc.javadoc.TagImpl">Methods inherited from class com.nomagic.reportwizard.tools.doc.javadoc.<a href="TagImpl.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">TagImpl</a></h3>
<code><a href="TagImpl.html#getInlineTags()">getInlineTags</a>, <a href="TagImpl.html#getKind()">getKind</a>, <a href="TagImpl.html#getRawText()">getRawText</a>, <a href="TagImpl.html#toString()">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String)">
<h3>SerialFieldTag</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SerialFieldTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> kind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Create a serial field tag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>kind</code> - the kind of tag that this Tag represents</dd>
<dd><code>text</code> - the text of this tag</dd>
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
<section class="detail" id="getFieldName()">
<h3>getFieldName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFieldName</span>()</div>
<div class="block">Return the serializable field name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the serializable field name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFieldDescription()">
<h3>getFieldDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></span> <span class="element-name">getFieldDescription</span>()</div>
<div class="block">Return the field comment.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the field comment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFieldType()">
<h3>getFieldType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFieldType</span>()</div>
<div class="block">Return the field type string.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the field type string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getText()">
<h3>getText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></span> <span class="element-name">getText</span>()</div>
<div class="block">Return the text of this tag.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../Tag.html#getText()">getText</a></code> in interface <code><a href="../Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="TagImpl.html#getText()">getText</a></code> in class <code><a href="TagImpl.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">TagImpl</a></code></dd>
<dt>Returns:</dt>
<dd>the text of this tag</dd>
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
