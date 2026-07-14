# JAVA OPENAPI: PlainTextBuilder (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/text/builders/PlainTextBuilder.html
- source_path: `com/nomagic/text/builders/PlainTextBuilder.html`
- source_sha256: `62d9701992887dd7ad23be369541f627195c4b310e4008ceeede712d7b4fe006`
- captured_utc: `2026-07-14T16:52:32.957158+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.text.builders](package-summary.html)

## Class PlainTextBuilder<T extends PlainTextBuilder>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.text.builders.AbstractTextBuilder](AbstractTextBuilder.html)<T>
com.nomagic.text.builders.PlainTextBuilder<T>

All Implemented Interfaces:
`[TextBuilder](TextBuilder.html)<T>`

@OpenApiAllpublic classPlainTextBuilder<T extends PlainTextBuilder>
extends [AbstractTextBuilder](AbstractTextBuilder.html)<T>

A builder used for plain text building. Any text fragments will be transformed to a plain text. Colored fragments are not supported.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PlainTextBuilder](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[compress](#compress(int))(int textLength)`
Compress current text to the given length.
`boolean`
`[isPlainTextEmpty](#isPlainTextEmpty())()`

`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toAppendableText](#toAppendableText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toPlainText](#toPlainText())()`
Methods inherited from class com.nomagic.text.builders.[AbstractTextBuilder](AbstractTextBuilder.html)
`[append](AbstractTextBuilder.html#append(java.lang.CharSequence)), [appendColor](AbstractTextBuilder.html#appendColor(java.lang.String)), [appendToText](AbstractTextBuilder.html#appendToText(java.lang.String)), [isTextAdded](AbstractTextBuilder.html#isTextAdded()), [prepend](AbstractTextBuilder.html#prepend(java.lang.CharSequence)), [prependColor](AbstractTextBuilder.html#prependColor(java.lang.String)), [prependToText](AbstractTextBuilder.html#prependToText(java.lang.String)), [replaceText](AbstractTextBuilder.html#replaceText(java.lang.String)), [setText](AbstractTextBuilder.html#setText(java.lang.CharSequence)), [textLength](AbstractTextBuilder.html#textLength()), [toString](AbstractTextBuilder.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.text.builders.[TextBuilder](TextBuilder.html)
`[append](TextBuilder.html#append(com.nomagic.text.builders.TextBuilder)), [appendWithNoWrap](TextBuilder.html#appendWithNoWrap(java.lang.CharSequence)), [appendWithSpace](TextBuilder.html#appendWithSpace(com.nomagic.text.builders.TextBuilder)), [appendWithSpace](TextBuilder.html#appendWithSpace(java.lang.CharSequence)), [isColorSupported](TextBuilder.html#isColorSupported()), [prepend](TextBuilder.html#prepend(com.nomagic.text.builders.TextBuilder)), [prependWithNoWrap](TextBuilder.html#prependWithNoWrap(java.lang.CharSequence)), [setColor](TextBuilder.html#setColor(java.awt.Color)), [setText](TextBuilder.html#setText(com.nomagic.text.builders.TextBuilder))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PlainTextBuilder
public PlainTextBuilder()
 ============ METHOD DETAIL ========== 
Method Details
toAppendableText
protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toAppendableText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Overrides:
`[toAppendableText](AbstractTextBuilder.html#toAppendableText(java.lang.String))` in class `[AbstractTextBuilder](AbstractTextBuilder.html)<[T](PlainTextBuilder.html) extends [PlainTextBuilder](PlainTextBuilder.html)>`
compress
public void compress(int textLength)
Description copied from interface: `[TextBuilder](TextBuilder.html#compress(int))`
Compress current text to the given length. This function is not supported in every implementation, so it can be ignored.
Parameters:
`textLength` - text length
toPlainText
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toPlainText()
Returns:
result string as plain text
isPlainTextEmpty
public boolean isPlainTextEmpty()
Returns:
true if text converted to a plain is empty in this builder

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.text.builders</a></div>
<h1 class="title" title="Class PlainTextBuilder">Class PlainTextBuilder&lt;T extends PlainTextBuilder&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">com.nomagic.text.builders.AbstractTextBuilder</a>&lt;T&gt;
<div class="inheritance">com.nomagic.text.builders.PlainTextBuilder&lt;T&gt;</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;T&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PlainTextBuilder&lt;T extends PlainTextBuilder&gt;</span>
<span class="extends-implements">extends <a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a>&lt;T&gt;</span></div>
<div class="block">A builder used for plain text building. Any text fragments will be transformed to a plain text. Colored fragments are not supported.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PlainTextBuilder</a>()</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compress(int)">compress</a><wbr/>(int textLength)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Compress current text to the given length.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isPlainTextEmpty()">isPlainTextEmpty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toAppendableText(java.lang.String)">toAppendableText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toPlainText()">toPlainText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.text.builders.AbstractTextBuilder">Methods inherited from class com.nomagic.text.builders.<a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a></h3>
<code><a href="AbstractTextBuilder.html#append(java.lang.CharSequence)">append</a>, <a href="AbstractTextBuilder.html#appendColor(java.lang.String)">appendColor</a>, <a href="AbstractTextBuilder.html#appendToText(java.lang.String)">appendToText</a>, <a href="AbstractTextBuilder.html#isTextAdded()">isTextAdded</a>, <a href="AbstractTextBuilder.html#prepend(java.lang.CharSequence)">prepend</a>, <a href="AbstractTextBuilder.html#prependColor(java.lang.String)">prependColor</a>, <a href="AbstractTextBuilder.html#prependToText(java.lang.String)">prependToText</a>, <a href="AbstractTextBuilder.html#replaceText(java.lang.String)">replaceText</a>, <a href="AbstractTextBuilder.html#setText(java.lang.CharSequence)">setText</a>, <a href="AbstractTextBuilder.html#textLength()">textLength</a>, <a href="AbstractTextBuilder.html#toString()">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.text.builders.TextBuilder">Methods inherited from interface com.nomagic.text.builders.<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></h3>
<code><a href="TextBuilder.html#append(com.nomagic.text.builders.TextBuilder)">append</a>, <a href="TextBuilder.html#appendWithNoWrap(java.lang.CharSequence)">appendWithNoWrap</a>, <a href="TextBuilder.html#appendWithSpace(com.nomagic.text.builders.TextBuilder)">appendWithSpace</a>, <a href="TextBuilder.html#appendWithSpace(java.lang.CharSequence)">appendWithSpace</a>, <a href="TextBuilder.html#isColorSupported()">isColorSupported</a>, <a href="TextBuilder.html#prepend(com.nomagic.text.builders.TextBuilder)">prepend</a>, <a href="TextBuilder.html#prependWithNoWrap(java.lang.CharSequence)">prependWithNoWrap</a>, <a href="TextBuilder.html#setColor(java.awt.Color)">setColor</a>, <a href="TextBuilder.html#setText(com.nomagic.text.builders.TextBuilder)">setText</a></code></div>
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
<h3>PlainTextBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PlainTextBuilder</span>()</div>
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
<dd><code><a href="AbstractTextBuilder.html#toAppendableText(java.lang.String)">toAppendableText</a></code> in class <code><a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a>&lt;<a href="PlainTextBuilder.html" title="type parameter in PlainTextBuilder">T</a> extends <a href="PlainTextBuilder.html" title="class in com.nomagic.text.builders">PlainTextBuilder</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compress(int)">
<h3>compress</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">compress</span><wbr/><span class="parameters">(int textLength)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="TextBuilder.html#compress(int)">TextBuilder</a></code></span></div>
<div class="block">Compress current text to the given length. This function is not supported in every implementation, so it can be ignored.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>textLength</code> - text length</dd>
</dl>
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
<section class="detail" id="isPlainTextEmpty()">
<h3>isPlainTextEmpty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPlainTextEmpty</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if text converted to a plain is empty in this builder</dd>
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
