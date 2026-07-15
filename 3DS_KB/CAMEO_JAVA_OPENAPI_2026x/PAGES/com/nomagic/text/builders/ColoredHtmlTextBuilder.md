# JAVA OPENAPI: ColoredHtmlTextBuilder (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/text/builders/ColoredHtmlTextBuilder.html
- source_path: `com/nomagic/text/builders/ColoredHtmlTextBuilder.html`
- source_sha256: `8fb61213ad5d3f46587e651d314258099ac395f943b7367e117fd8b3779822e1`
- captured_utc: `2026-07-14T16:58:41.218327+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.text.builders](package-summary.html)

## Class ColoredHtmlTextBuilder<T extends ColoredHtmlTextBuilder>

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.text.builders.AbstractTextBuilder](AbstractTextBuilder.html)<T>
[com.nomagic.text.builders.HtmlTextBuilder](HtmlTextBuilder.html)<T>
com.nomagic.text.builders.ColoredHtmlTextBuilder<T>

All Implemented Interfaces:
`[TextBuilder](TextBuilder.html)<T>`

@OpenApiAllpublic classColoredHtmlTextBuilder<T extends ColoredHtmlTextBuilder>
extends [HtmlTextBuilder](HtmlTextBuilder.html)<T>

A builder used for html text building. Plain or rich text fragments will be transformed to html text. Colored fragments are supported.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ColoredHtmlTextBuilder](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[appendColor](#appendColor(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`

`static [ColoredHtmlTextBuilder](ColoredHtmlTextBuilder.html)`
`[createColoredHtmlTextBuilderPreferLightHtml](#createColoredHtmlTextBuilderPreferLightHtml())()`
Creates and instance of builder which outputs light html if full html was not appended.
`boolean`
`[isColorSupported](#isColorSupported())()`

`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[prependColor](#prependColor(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`

`[T](ColoredHtmlTextBuilder.html)`
`[setColor](#setColor(java.awt.Color))([Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html) color)`
Set the color of the text which will be added later.
`void`
`[setText](#setText(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) text)`
Replace current text with the given one
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Methods inherited from class com.nomagic.text.builders.[HtmlTextBuilder](HtmlTextBuilder.html)
`[appendWithNoWrap](HtmlTextBuilder.html#appendWithNoWrap(java.lang.CharSequence)), [createHtmlTextBuilderPreferLightHtml](HtmlTextBuilder.html#createHtmlTextBuilderPreferLightHtml()), [preferLightHtml](HtmlTextBuilder.html#preferLightHtml(com.nomagic.text.builders.HtmlTextBuilder)), [prependWithNoWrap](HtmlTextBuilder.html#prependWithNoWrap(java.lang.CharSequence)), [replaceSpaceToNbsp](HtmlTextBuilder.html#replaceSpaceToNbsp(java.lang.String)), [toAppendableText](HtmlTextBuilder.html#toAppendableText(java.lang.String)), [toPlainText](HtmlTextBuilder.html#toPlainText())`
Methods inherited from class com.nomagic.text.builders.[AbstractTextBuilder](AbstractTextBuilder.html)
`[append](AbstractTextBuilder.html#append(java.lang.CharSequence)), [appendToText](AbstractTextBuilder.html#appendToText(java.lang.String)), [isTextAdded](AbstractTextBuilder.html#isTextAdded()), [prepend](AbstractTextBuilder.html#prepend(java.lang.CharSequence)), [prependToText](AbstractTextBuilder.html#prependToText(java.lang.String)), [replaceText](AbstractTextBuilder.html#replaceText(java.lang.String)), [textLength](AbstractTextBuilder.html#textLength())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.text.builders.[TextBuilder](TextBuilder.html)
`[append](TextBuilder.html#append(com.nomagic.text.builders.TextBuilder)), [appendWithSpace](TextBuilder.html#appendWithSpace(com.nomagic.text.builders.TextBuilder)), [appendWithSpace](TextBuilder.html#appendWithSpace(java.lang.CharSequence)), [compress](TextBuilder.html#compress(int)), [isPlainTextEmpty](TextBuilder.html#isPlainTextEmpty()), [prepend](TextBuilder.html#prepend(com.nomagic.text.builders.TextBuilder)), [setText](TextBuilder.html#setText(com.nomagic.text.builders.TextBuilder))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ColoredHtmlTextBuilder
public ColoredHtmlTextBuilder()
 ============ METHOD DETAIL ========== 
Method Details
setColor
public [T](ColoredHtmlTextBuilder.html) setColor(@CheckForNull
 [Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html) color)
Description copied from interface: `[TextBuilder](TextBuilder.html#setColor(java.awt.Color))`
Set the color of the text which will be added later. Not every implementation supports that, so color can be ignored.
Parameters:
`color` - color to set. Null is used to reset previously set color
Returns:
this builder
appendColor
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) appendColor([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Overrides:
`[appendColor](AbstractTextBuilder.html#appendColor(java.lang.String))` in class `[AbstractTextBuilder](AbstractTextBuilder.html)<[T](ColoredHtmlTextBuilder.html) extends [ColoredHtmlTextBuilder](ColoredHtmlTextBuilder.html)>`
prependColor
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) prependColor([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Overrides:
`[prependColor](AbstractTextBuilder.html#prependColor(java.lang.String))` in class `[AbstractTextBuilder](AbstractTextBuilder.html)<[T](ColoredHtmlTextBuilder.html) extends [ColoredHtmlTextBuilder](ColoredHtmlTextBuilder.html)>`
setText
public void setText([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) text)
Description copied from interface: `[TextBuilder](TextBuilder.html#setText(java.lang.CharSequence))`
Replace current text with the given one
Specified by:
`[setText](TextBuilder.html#setText(java.lang.CharSequence))` in interface `[TextBuilder](TextBuilder.html)<[T](ColoredHtmlTextBuilder.html) extends [ColoredHtmlTextBuilder](ColoredHtmlTextBuilder.html)>`
Overrides:
`[setText](AbstractTextBuilder.html#setText(java.lang.CharSequence))` in class `[AbstractTextBuilder](AbstractTextBuilder.html)<[T](ColoredHtmlTextBuilder.html) extends [ColoredHtmlTextBuilder](ColoredHtmlTextBuilder.html)>`
Parameters:
`text` - text
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Specified by:
`[toString](TextBuilder.html#toString())` in interface `[TextBuilder](TextBuilder.html)<[T](ColoredHtmlTextBuilder.html) extends [ColoredHtmlTextBuilder](ColoredHtmlTextBuilder.html)>`
Overrides:
`[toString](HtmlTextBuilder.html#toString())` in class `[HtmlTextBuilder](HtmlTextBuilder.html)<[T](ColoredHtmlTextBuilder.html) extends [ColoredHtmlTextBuilder](ColoredHtmlTextBuilder.html)>`
Returns:
result string
isColorSupported
public boolean isColorSupported()
Returns:
true if builder supports color
createColoredHtmlTextBuilderPreferLightHtml
public static [ColoredHtmlTextBuilder](ColoredHtmlTextBuilder.html) createColoredHtmlTextBuilderPreferLightHtml()
Creates and instance of builder which outputs light html if full html was not appended.
Returns:
builder

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.text.builders</a></div>
<h1 class="title" title="Class ColoredHtmlTextBuilder">Class ColoredHtmlTextBuilder&lt;T extends ColoredHtmlTextBuilder&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">com.nomagic.text.builders.AbstractTextBuilder</a>&lt;T&gt;
<div class="inheritance"><a href="HtmlTextBuilder.html" title="class in com.nomagic.text.builders">com.nomagic.text.builders.HtmlTextBuilder</a>&lt;T&gt;
<div class="inheritance">com.nomagic.text.builders.ColoredHtmlTextBuilder&lt;T&gt;</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;T&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ColoredHtmlTextBuilder&lt;T extends ColoredHtmlTextBuilder&gt;</span>
<span class="extends-implements">extends <a href="HtmlTextBuilder.html" title="class in com.nomagic.text.builders">HtmlTextBuilder</a>&lt;T&gt;</span></div>
<div class="block">A builder used for html text building. Plain or rich text fragments will be transformed to html text. Colored fragments are supported.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ColoredHtmlTextBuilder</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#appendColor(java.lang.String)">appendColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ColoredHtmlTextBuilder.html" title="class in com.nomagic.text.builders">ColoredHtmlTextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createColoredHtmlTextBuilderPreferLightHtml()">createColoredHtmlTextBuilderPreferLightHtml</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates and instance of builder which outputs light html if full html was not appended.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isColorSupported()">isColorSupported</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prependColor(java.lang.String)">prependColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ColoredHtmlTextBuilder.html" title="type parameter in ColoredHtmlTextBuilder">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColor(java.awt.Color)">setColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the color of the text which will be added later.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setText(java.lang.CharSequence)">setText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Replace current text with the given one</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.text.builders.HtmlTextBuilder">Methods inherited from class com.nomagic.text.builders.<a href="HtmlTextBuilder.html" title="class in com.nomagic.text.builders">HtmlTextBuilder</a></h3>
<code><a href="HtmlTextBuilder.html#appendWithNoWrap(java.lang.CharSequence)">appendWithNoWrap</a>, <a href="HtmlTextBuilder.html#createHtmlTextBuilderPreferLightHtml()">createHtmlTextBuilderPreferLightHtml</a>, <a href="HtmlTextBuilder.html#preferLightHtml(com.nomagic.text.builders.HtmlTextBuilder)">preferLightHtml</a>, <a href="HtmlTextBuilder.html#prependWithNoWrap(java.lang.CharSequence)">prependWithNoWrap</a>, <a href="HtmlTextBuilder.html#replaceSpaceToNbsp(java.lang.String)">replaceSpaceToNbsp</a>, <a href="HtmlTextBuilder.html#toAppendableText(java.lang.String)">toAppendableText</a>, <a href="HtmlTextBuilder.html#toPlainText()">toPlainText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.text.builders.AbstractTextBuilder">Methods inherited from class com.nomagic.text.builders.<a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a></h3>
<code><a href="AbstractTextBuilder.html#append(java.lang.CharSequence)">append</a>, <a href="AbstractTextBuilder.html#appendToText(java.lang.String)">appendToText</a>, <a href="AbstractTextBuilder.html#isTextAdded()">isTextAdded</a>, <a href="AbstractTextBuilder.html#prepend(java.lang.CharSequence)">prepend</a>, <a href="AbstractTextBuilder.html#prependToText(java.lang.String)">prependToText</a>, <a href="AbstractTextBuilder.html#replaceText(java.lang.String)">replaceText</a>, <a href="AbstractTextBuilder.html#textLength()">textLength</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.text.builders.TextBuilder">Methods inherited from interface com.nomagic.text.builders.<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></h3>
<code><a href="TextBuilder.html#append(com.nomagic.text.builders.TextBuilder)">append</a>, <a href="TextBuilder.html#appendWithSpace(com.nomagic.text.builders.TextBuilder)">appendWithSpace</a>, <a href="TextBuilder.html#appendWithSpace(java.lang.CharSequence)">appendWithSpace</a>, <a href="TextBuilder.html#compress(int)">compress</a>, <a href="TextBuilder.html#isPlainTextEmpty()">isPlainTextEmpty</a>, <a href="TextBuilder.html#prepend(com.nomagic.text.builders.TextBuilder)">prepend</a>, <a href="TextBuilder.html#setText(com.nomagic.text.builders.TextBuilder)">setText</a></code></div>
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
<h3>ColoredHtmlTextBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ColoredHtmlTextBuilder</span>()</div>
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
<section class="detail" id="setColor(java.awt.Color)">
<h3>setColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ColoredHtmlTextBuilder.html" title="type parameter in ColoredHtmlTextBuilder">T</a></span> <span class="element-name">setColor</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="TextBuilder.html#setColor(java.awt.Color)">TextBuilder</a></code></span></div>
<div class="block">Set the color of the text which will be added later. Not every implementation supports that, so color can be ignored.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>color</code> - color to set. Null is used to reset previously set color</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendColor(java.lang.String)">
<h3>appendColor</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">appendColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractTextBuilder.html#appendColor(java.lang.String)">appendColor</a></code> in class <code><a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a>&lt;<a href="ColoredHtmlTextBuilder.html" title="type parameter in ColoredHtmlTextBuilder">T</a> extends <a href="ColoredHtmlTextBuilder.html" title="class in com.nomagic.text.builders">ColoredHtmlTextBuilder</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prependColor(java.lang.String)">
<h3>prependColor</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">prependColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractTextBuilder.html#prependColor(java.lang.String)">prependColor</a></code> in class <code><a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a>&lt;<a href="ColoredHtmlTextBuilder.html" title="type parameter in ColoredHtmlTextBuilder">T</a> extends <a href="ColoredHtmlTextBuilder.html" title="class in com.nomagic.text.builders">ColoredHtmlTextBuilder</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setText(java.lang.CharSequence)">
<h3>setText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="TextBuilder.html#setText(java.lang.CharSequence)">TextBuilder</a></code></span></div>
<div class="block">Replace current text with the given one</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#setText(java.lang.CharSequence)">setText</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="ColoredHtmlTextBuilder.html" title="type parameter in ColoredHtmlTextBuilder">T</a> extends <a href="ColoredHtmlTextBuilder.html" title="class in com.nomagic.text.builders">ColoredHtmlTextBuilder</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code><a href="AbstractTextBuilder.html#setText(java.lang.CharSequence)">setText</a></code> in class <code><a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a>&lt;<a href="ColoredHtmlTextBuilder.html" title="type parameter in ColoredHtmlTextBuilder">T</a> extends <a href="ColoredHtmlTextBuilder.html" title="class in com.nomagic.text.builders">ColoredHtmlTextBuilder</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>text</code> - text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#toString()">toString</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="ColoredHtmlTextBuilder.html" title="type parameter in ColoredHtmlTextBuilder">T</a> extends <a href="ColoredHtmlTextBuilder.html" title="class in com.nomagic.text.builders">ColoredHtmlTextBuilder</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code><a href="HtmlTextBuilder.html#toString()">toString</a></code> in class <code><a href="HtmlTextBuilder.html" title="class in com.nomagic.text.builders">HtmlTextBuilder</a>&lt;<a href="ColoredHtmlTextBuilder.html" title="type parameter in ColoredHtmlTextBuilder">T</a> extends <a href="ColoredHtmlTextBuilder.html" title="class in com.nomagic.text.builders">ColoredHtmlTextBuilder</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>result string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isColorSupported()">
<h3>isColorSupported</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isColorSupported</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if builder supports color</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createColoredHtmlTextBuilderPreferLightHtml()">
<h3>createColoredHtmlTextBuilderPreferLightHtml</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ColoredHtmlTextBuilder.html" title="class in com.nomagic.text.builders">ColoredHtmlTextBuilder</a></span> <span class="element-name">createColoredHtmlTextBuilderPreferLightHtml</span>()</div>
<div class="block">Creates and instance of builder which outputs light html if full html was not appended.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>builder</dd>
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
