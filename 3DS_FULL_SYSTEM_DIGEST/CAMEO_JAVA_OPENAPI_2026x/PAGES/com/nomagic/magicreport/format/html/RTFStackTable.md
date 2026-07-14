# JAVA OPENAPI: RTFStackTable (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/format/html/RTFStackTable.html
- source_path: `com/nomagic/magicreport/format/html/RTFStackTable.html`
- source_sha256: `68485441690e9e76f13890d0f1d339f93f8fb77c6f8e45faa055d1f3a7e241b0`
- captured_utc: `2026-07-14T16:58:39.122303+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format.html](package-summary.html)

## Class RTFStackTable

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicreport.format.html.StackTable](StackTable.html)
com.nomagic.magicreport.format.html.RTFStackTable

@OpenApiAllpublic final classRTFStackTable
extends [StackTable](StackTable.html)

Class for keeping value of tag and its position in stack or keeping value of table attribute. This class is
 used for RTF creator

Since:
Mar 5, 2012

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[RTFStackTable](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag)`
Constructor.
`[RTFStackTable](#%3Cinit%3E(java.lang.String,java.lang.StringBuilder))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) paragraphStyle)`
Constructor.
`[RTFStackTable](#%3Cinit%3E(java.lang.String,java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 int pos)`
Constructor for tag and its position.
`[RTFStackTable](#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 int pos,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] attributeValueList)`
Constructor for tag, its position and attributeList.
`[RTFStackTable](#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.String%5B%5D,java.lang.StringBuilder))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 int pos,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] attributeValueList,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) paragraphStyle)`
Constructor for tag, its position and attributeList.
`[RTFStackTable](#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.StringBuilder))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 int pos,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) paragraphStyle)`
Constructor for tag and its position.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[getParagraphStyle](#getParagraphStyle())()`
Get paragraphStyle.
`void`
`[setParagraphStyle](#setParagraphStyle(java.lang.StringBuilder))([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) paragraphStyle)`
Set paragraphStyle.
Methods inherited from class com.nomagic.magicreport.format.html.[StackTable](StackTable.html)
`[getAttributeValueList](StackTable.html#getAttributeValueList()), [getPos](StackTable.html#getPos()), [getTag](StackTable.html#getTag()), [getValue](StackTable.html#getValue()), [setAttributeValueList](StackTable.html#setAttributeValueList(java.lang.String%5B%5D)), [setPos](StackTable.html#setPos(int)), [setTag](StackTable.html#setTag(java.lang.String)), [setValue](StackTable.html#setValue(java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
RTFStackTable
public RTFStackTable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 int pos,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] attributeValueList,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) paragraphStyle)
Constructor for tag, its position and attributeList.
Parameters:
`tag` - html tag name or attribute name
`value` - attribute value
`pos` - position in stack
`attributeValueList` - Array of tag attribute
`paragraphStyle` - paragraph style (for paragraph tag such as p, div etc.)
RTFStackTable
public RTFStackTable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 int pos,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) paragraphStyle)
Constructor for tag and its position.
Parameters:
`tag` - html tag name or attribute name
`value` - attribute value
`pos` - position in stack
`paragraphStyle` - paragraph style (for paragraph tag such as p, div etc.)
RTFStackTable
public RTFStackTable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) paragraphStyle)
Constructor.
Parameters:
`tag` - attribute name of html tag
`paragraphStyle` - paragraph style (for paragraph tag such as p, div etc.)
RTFStackTable
public RTFStackTable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 int pos,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] attributeValueList)
Constructor for tag, its position and attributeList.
Parameters:
`tag` - html tag name or attribute name
`value` - attribute value
`pos` - position in stack
`attributeValueList` - Array of tag attribute
RTFStackTable
public RTFStackTable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 int pos)
Constructor for tag and its position.
Parameters:
`tag` - html tag name or attribute name
`value` - attribute value
`pos` - position in stack
RTFStackTable
public RTFStackTable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag)
Constructor.
Parameters:
`tag` - attribute name of html tag
 ============ METHOD DETAIL ========== 
Method Details
getParagraphStyle
public [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) getParagraphStyle()
Get paragraphStyle.
Returns:
paragraphStyle
setParagraphStyle
public void setParagraphStyle([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) paragraphStyle)
Set paragraphStyle.
Parameters:
`paragraphStyle` - paragraphStyle

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format.html</a></div>
<h1 class="title" title="Class RTFStackTable">Class RTFStackTable</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="StackTable.html" title="class in com.nomagic.magicreport.format.html">com.nomagic.magicreport.format.html.StackTable</a>
<div class="inheritance">com.nomagic.magicreport.format.html.RTFStackTable</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">RTFStackTable</span>
<span class="extends-implements">extends <a href="StackTable.html" title="class in com.nomagic.magicreport.format.html">StackTable</a></span></div>
<div class="block">Class for keeping value of tag and its position in stack or keeping value of table attribute. This class is
 used for RTF creator</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Mar 5, 2012</dd>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">RTFStackTable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.StringBuilder)">RTFStackTable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> paragraphStyle)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,int)">RTFStackTable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 int pos)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor for tag and its position.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.String%5B%5D)">RTFStackTable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 int pos,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] attributeValueList)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor for tag, its position and attributeList.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.String%5B%5D,java.lang.StringBuilder)">RTFStackTable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 int pos,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] attributeValueList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> paragraphStyle)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor for tag, its position and attributeList.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,int,java.lang.StringBuilder)">RTFStackTable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 int pos,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> paragraphStyle)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor for tag and its position.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParagraphStyle()">getParagraphStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get paragraphStyle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParagraphStyle(java.lang.StringBuilder)">setParagraphStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> paragraphStyle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set paragraphStyle.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.format.html.StackTable">Methods inherited from class com.nomagic.magicreport.format.html.<a href="StackTable.html" title="class in com.nomagic.magicreport.format.html">StackTable</a></h3>
<code><a href="StackTable.html#getAttributeValueList()">getAttributeValueList</a>, <a href="StackTable.html#getPos()">getPos</a>, <a href="StackTable.html#getTag()">getTag</a>, <a href="StackTable.html#getValue()">getValue</a>, <a href="StackTable.html#setAttributeValueList(java.lang.String%5B%5D)">setAttributeValueList</a>, <a href="StackTable.html#setPos(int)">setPos</a>, <a href="StackTable.html#setTag(java.lang.String)">setTag</a>, <a href="StackTable.html#setValue(java.lang.String)">setValue</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,int,java.lang.String[],java.lang.StringBuilder)">
<h3>RTFStackTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RTFStackTable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 int pos,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] attributeValueList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> paragraphStyle)</span></div>
<div class="block">Constructor for tag, its position and attributeList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - html tag name or attribute name</dd>
<dd><code>value</code> - attribute value</dd>
<dd><code>pos</code> - position in stack</dd>
<dd><code>attributeValueList</code> - Array of tag attribute</dd>
<dd><code>paragraphStyle</code> - paragraph style (for paragraph tag such as p, div etc.)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,int,java.lang.StringBuilder)">
<h3>RTFStackTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RTFStackTable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 int pos,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> paragraphStyle)</span></div>
<div class="block">Constructor for tag and its position.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - html tag name or attribute name</dd>
<dd><code>value</code> - attribute value</dd>
<dd><code>pos</code> - position in stack</dd>
<dd><code>paragraphStyle</code> - paragraph style (for paragraph tag such as p, div etc.)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.StringBuilder)">
<h3>RTFStackTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RTFStackTable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> paragraphStyle)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - attribute name of html tag</dd>
<dd><code>paragraphStyle</code> - paragraph style (for paragraph tag such as p, div etc.)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,int,java.lang.String[])">
<h3>RTFStackTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RTFStackTable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 int pos,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] attributeValueList)</span></div>
<div class="block">Constructor for tag, its position and attributeList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - html tag name or attribute name</dd>
<dd><code>value</code> - attribute value</dd>
<dd><code>pos</code> - position in stack</dd>
<dd><code>attributeValueList</code> - Array of tag attribute</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,int)">
<h3>RTFStackTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RTFStackTable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 int pos)</span></div>
<div class="block">Constructor for tag and its position.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - html tag name or attribute name</dd>
<dd><code>value</code> - attribute value</dd>
<dd><code>pos</code> - position in stack</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>RTFStackTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RTFStackTable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - attribute name of html tag</dd>
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
<section class="detail" id="getParagraphStyle()">
<h3>getParagraphStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">getParagraphStyle</span>()</div>
<div class="block">Get paragraphStyle.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>paragraphStyle</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParagraphStyle(java.lang.StringBuilder)">
<h3>setParagraphStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParagraphStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> paragraphStyle)</span></div>
<div class="block">Set paragraphStyle.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>paragraphStyle</code> - paragraphStyle</dd>
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
