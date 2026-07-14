# JAVA OPENAPI: HtmlTextBuilder (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/text/builders/HtmlTextBuilder.html
- source_path: `com/nomagic/text/builders/HtmlTextBuilder.html`
- source_sha256: `834e593d87f3cabeff5d2c36a520ff17490ecd0b5a8d5458d87f855be6856a93`
- captured_utc: `2026-07-14T16:56:02.977543+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.text.builders](package-summary.html)

## Class HtmlTextBuilder<T extends HtmlTextBuilder>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.text.builders.AbstractTextBuilder](AbstractTextBuilder.html)<T>
com.nomagic.text.builders.HtmlTextBuilder<T>

All Implemented Interfaces:
`[TextBuilder](TextBuilder.html)<T>`

Direct Known Subclasses:
`[ColoredHtmlTextBuilder](ColoredHtmlTextBuilder.html)`

@OpenApiAllpublic classHtmlTextBuilder<T extends HtmlTextBuilder>
extends [AbstractTextBuilder](AbstractTextBuilder.html)<T>

A builder used for html text building. Plain or rich text fragments will be transformed to html text. Colored fragments are not supported.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[HtmlTextBuilder](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[T](HtmlTextBuilder.html)`
`[appendWithNoWrap](#appendWithNoWrap(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)`
Append text from the given builder.
`static [HtmlTextBuilder](HtmlTextBuilder.html)`
`[createHtmlTextBuilderPreferLightHtml](#createHtmlTextBuilderPreferLightHtml())()`
Creates and instance of builder which outputs light html if full html was not appended.
`protected void`
`[preferLightHtml](#preferLightHtml(com.nomagic.text.builders.HtmlTextBuilder))([HtmlTextBuilder](HtmlTextBuilder.html) builder)`

`[T](HtmlTextBuilder.html)`
`[prependWithNoWrap](#prependWithNoWrap(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) plainText)`
Add text to the beginning.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[replaceSpaceToNbsp](#replaceSpaceToNbsp(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`

`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toAppendableText](#toAppendableText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toPlainText](#toPlainText())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Methods inherited from class com.nomagic.text.builders.[AbstractTextBuilder](AbstractTextBuilder.html)
`[append](AbstractTextBuilder.html#append(java.lang.CharSequence)), [appendColor](AbstractTextBuilder.html#appendColor(java.lang.String)), [appendToText](AbstractTextBuilder.html#appendToText(java.lang.String)), [isTextAdded](AbstractTextBuilder.html#isTextAdded()), [prepend](AbstractTextBuilder.html#prepend(java.lang.CharSequence)), [prependColor](AbstractTextBuilder.html#prependColor(java.lang.String)), [prependToText](AbstractTextBuilder.html#prependToText(java.lang.String)), [replaceText](AbstractTextBuilder.html#replaceText(java.lang.String)), [setText](AbstractTextBuilder.html#setText(java.lang.CharSequence)), [textLength](AbstractTextBuilder.html#textLength())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.text.builders.[TextBuilder](TextBuilder.html)
`[append](TextBuilder.html#append(com.nomagic.text.builders.TextBuilder)), [appendWithSpace](TextBuilder.html#appendWithSpace(com.nomagic.text.builders.TextBuilder)), [appendWithSpace](TextBuilder.html#appendWithSpace(java.lang.CharSequence)), [compress](TextBuilder.html#compress(int)), [isColorSupported](TextBuilder.html#isColorSupported()), [isPlainTextEmpty](TextBuilder.html#isPlainTextEmpty()), [prepend](TextBuilder.html#prepend(com.nomagic.text.builders.TextBuilder)), [setColor](TextBuilder.html#setColor(java.awt.Color)), [setText](TextBuilder.html#setText(com.nomagic.text.builders.TextBuilder))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
HtmlTextBuilder
public HtmlTextBuilder()
 ============ METHOD DETAIL ========== 
Method Details
toAppendableText
protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toAppendableText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Overrides:
`[toAppendableText](AbstractTextBuilder.html#toAppendableText(java.lang.String))` in class `[AbstractTextBuilder](AbstractTextBuilder.html)<[T](HtmlTextBuilder.html) extends [HtmlTextBuilder](HtmlTextBuilder.html)>`
prependWithNoWrap
public [T](HtmlTextBuilder.html) prependWithNoWrap([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) plainText)
Description copied from interface: `[TextBuilder](TextBuilder.html#prependWithNoWrap(java.lang.CharSequence))`
Add text to the beginning. Added text will not be wrapped if builder supports that.
Parameters:
`plainText` - text to prepend
Returns:
this builder
appendWithNoWrap
public [T](HtmlTextBuilder.html) appendWithNoWrap([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)
Description copied from interface: `[TextBuilder](TextBuilder.html#appendWithNoWrap(java.lang.CharSequence))`
Append text from the given builder. Added text will not be wrapped if builder supports that.
Parameters:
`text` - text to prepend
Returns:
this builder
replaceSpaceToNbsp
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) replaceSpaceToNbsp([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
toPlainText
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toPlainText()
Returns:
result string as plain text
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Specified by:
`[toString](TextBuilder.html#toString())` in interface `[TextBuilder](TextBuilder.html)<[T](HtmlTextBuilder.html) extends [HtmlTextBuilder](HtmlTextBuilder.html)>`
Overrides:
`[toString](AbstractTextBuilder.html#toString())` in class `[AbstractTextBuilder](AbstractTextBuilder.html)<[T](HtmlTextBuilder.html) extends [HtmlTextBuilder](HtmlTextBuilder.html)>`
Returns:
result string
createHtmlTextBuilderPreferLightHtml
public static [HtmlTextBuilder](HtmlTextBuilder.html) createHtmlTextBuilderPreferLightHtml()
Creates and instance of builder which outputs light html if full html was not appended.
Returns:
builder
preferLightHtml
protected void preferLightHtml([HtmlTextBuilder](HtmlTextBuilder.html) builder)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.text.builders</a></div>
<h1 class="title" title="Class HtmlTextBuilder">Class HtmlTextBuilder&lt;T extends HtmlTextBuilder&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">com.nomagic.text.builders.AbstractTextBuilder</a>&lt;T&gt;
<div class="inheritance">com.nomagic.text.builders.HtmlTextBuilder&lt;T&gt;</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;T&gt;</code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ColoredHtmlTextBuilder.html" title="class in com.nomagic.text.builders">ColoredHtmlTextBuilder</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">HtmlTextBuilder&lt;T extends HtmlTextBuilder&gt;</span>
<span class="extends-implements">extends <a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a>&lt;T&gt;</span></div>
<div class="block">A builder used for html text building. Plain or rich text fragments will be transformed to html text. Colored fragments are not supported.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">HtmlTextBuilder</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="HtmlTextBuilder.html" title="type parameter in HtmlTextBuilder">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#appendWithNoWrap(java.lang.CharSequence)">appendWithNoWrap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Append text from the given builder.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="HtmlTextBuilder.html" title="class in com.nomagic.text.builders">HtmlTextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createHtmlTextBuilderPreferLightHtml()">createHtmlTextBuilderPreferLightHtml</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates and instance of builder which outputs light html if full html was not appended.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#preferLightHtml(com.nomagic.text.builders.HtmlTextBuilder)">preferLightHtml</a><wbr/>(<a href="HtmlTextBuilder.html" title="class in com.nomagic.text.builders">HtmlTextBuilder</a> builder)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="HtmlTextBuilder.html" title="type parameter in HtmlTextBuilder">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prependWithNoWrap(java.lang.CharSequence)">prependWithNoWrap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> plainText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add text to the beginning.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#replaceSpaceToNbsp(java.lang.String)">replaceSpaceToNbsp</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toAppendableText(java.lang.String)">toAppendableText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toPlainText()">toPlainText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.text.builders.AbstractTextBuilder">Methods inherited from class com.nomagic.text.builders.<a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a></h3>
<code><a href="AbstractTextBuilder.html#append(java.lang.CharSequence)">append</a>, <a href="AbstractTextBuilder.html#appendColor(java.lang.String)">appendColor</a>, <a href="AbstractTextBuilder.html#appendToText(java.lang.String)">appendToText</a>, <a href="AbstractTextBuilder.html#isTextAdded()">isTextAdded</a>, <a href="AbstractTextBuilder.html#prepend(java.lang.CharSequence)">prepend</a>, <a href="AbstractTextBuilder.html#prependColor(java.lang.String)">prependColor</a>, <a href="AbstractTextBuilder.html#prependToText(java.lang.String)">prependToText</a>, <a href="AbstractTextBuilder.html#replaceText(java.lang.String)">replaceText</a>, <a href="AbstractTextBuilder.html#setText(java.lang.CharSequence)">setText</a>, <a href="AbstractTextBuilder.html#textLength()">textLength</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.text.builders.TextBuilder">Methods inherited from interface com.nomagic.text.builders.<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></h3>
<code><a href="TextBuilder.html#append(com.nomagic.text.builders.TextBuilder)">append</a>, <a href="TextBuilder.html#appendWithSpace(com.nomagic.text.builders.TextBuilder)">appendWithSpace</a>, <a href="TextBuilder.html#appendWithSpace(java.lang.CharSequence)">appendWithSpace</a>, <a href="TextBuilder.html#compress(int)">compress</a>, <a href="TextBuilder.html#isColorSupported()">isColorSupported</a>, <a href="TextBuilder.html#isPlainTextEmpty()">isPlainTextEmpty</a>, <a href="TextBuilder.html#prepend(com.nomagic.text.builders.TextBuilder)">prepend</a>, <a href="TextBuilder.html#setColor(java.awt.Color)">setColor</a>, <a href="TextBuilder.html#setText(com.nomagic.text.builders.TextBuilder)">setText</a></code></div>
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
<h3>HtmlTextBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HtmlTextBuilder</span>()</div>
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
<section class="detail" id="toAppendableText(java.lang.String)">
<h3>toAppendableText</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toAppendableText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractTextBuilder.html#toAppendableText(java.lang.String)">toAppendableText</a></code> in class <code><a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a>&lt;<a href="HtmlTextBuilder.html" title="type parameter in HtmlTextBuilder">T</a> extends <a href="HtmlTextBuilder.html" title="class in com.nomagic.text.builders">HtmlTextBuilder</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prependWithNoWrap(java.lang.CharSequence)">
<h3>prependWithNoWrap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="HtmlTextBuilder.html" title="type parameter in HtmlTextBuilder">T</a></span> <span class="element-name">prependWithNoWrap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> plainText)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="TextBuilder.html#prependWithNoWrap(java.lang.CharSequence)">TextBuilder</a></code></span></div>
<div class="block">Add text to the beginning. Added text will not be wrapped if builder supports that.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>plainText</code> - text to prepend</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendWithNoWrap(java.lang.CharSequence)">
<h3>appendWithNoWrap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="HtmlTextBuilder.html" title="type parameter in HtmlTextBuilder">T</a></span> <span class="element-name">appendWithNoWrap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="TextBuilder.html#appendWithNoWrap(java.lang.CharSequence)">TextBuilder</a></code></span></div>
<div class="block">Append text from the given builder. Added text will not be wrapped if builder supports that.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text to prepend</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="replaceSpaceToNbsp(java.lang.String)">
<h3>replaceSpaceToNbsp</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">replaceSpaceToNbsp</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
</section>
</li>
<li>
<section class="detail" id="toPlainText()">
<h3>toPlainText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toPlainText</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>result string as plain text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#toString()">toString</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="HtmlTextBuilder.html" title="type parameter in HtmlTextBuilder">T</a> extends <a href="HtmlTextBuilder.html" title="class in com.nomagic.text.builders">HtmlTextBuilder</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code><a href="AbstractTextBuilder.html#toString()">toString</a></code> in class <code><a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a>&lt;<a href="HtmlTextBuilder.html" title="type parameter in HtmlTextBuilder">T</a> extends <a href="HtmlTextBuilder.html" title="class in com.nomagic.text.builders">HtmlTextBuilder</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>result string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createHtmlTextBuilderPreferLightHtml()">
<h3>createHtmlTextBuilderPreferLightHtml</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="HtmlTextBuilder.html" title="class in com.nomagic.text.builders">HtmlTextBuilder</a></span> <span class="element-name">createHtmlTextBuilderPreferLightHtml</span>()</div>
<div class="block">Creates and instance of builder which outputs light html if full html was not appended.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="preferLightHtml(com.nomagic.text.builders.HtmlTextBuilder)">
<h3>preferLightHtml</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">preferLightHtml</span><wbr/><span class="parameters">(<a href="HtmlTextBuilder.html" title="class in com.nomagic.text.builders">HtmlTextBuilder</a> builder)</span></div>
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
