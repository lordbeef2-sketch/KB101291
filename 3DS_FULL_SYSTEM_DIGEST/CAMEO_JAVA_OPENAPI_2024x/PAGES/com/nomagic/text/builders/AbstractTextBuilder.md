# JAVA OPENAPI: AbstractTextBuilder (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/text/builders/AbstractTextBuilder.html
- source_path: `com/nomagic/text/builders/AbstractTextBuilder.html`
- source_sha256: `2a83be60b00e3264ab98f75d02121b729130f78703a71b3eeed08c8646045ee3`
- captured_utc: `2026-07-14T16:52:32.569154+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.text.builders](package-summary.html)

## Class AbstractTextBuilder<T extends AbstractTextBuilder>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.text.builders.AbstractTextBuilder<T>

All Implemented Interfaces:
`[TextBuilder](TextBuilder.html)<T>`

Direct Known Subclasses:
`[HtmlTextBuilder](HtmlTextBuilder.html)`, `[PlainOrFullHtmlTextBuilder](PlainOrFullHtmlTextBuilder.html)`, `[PlainOrLightHtmlTextBuilder](PlainOrLightHtmlTextBuilder.html)`, `[PlainTextBuilder](PlainTextBuilder.html)`, `[RichTextBuilder](RichTextBuilder.html)`

@OpenApiAllpublic abstract classAbstractTextBuilder<T extends AbstractTextBuilder>
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [TextBuilder](TextBuilder.html)<T>

Abstract builder.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractTextBuilder](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[T](AbstractTextBuilder.html)`
`[append](#append(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)`
Append given text
`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[appendColor](#appendColor(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`

`protected final void`
`[appendToText](#appendToText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`

`boolean`
`[isTextAdded](#isTextAdded())()`

`[T](AbstractTextBuilder.html)`
`[prepend](#prepend(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)`
Add given text to the beginning.
`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[prependColor](#prependColor(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`

`protected final void`
`[prependToText](#prependToText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`

`protected final void`
`[replaceText](#replaceText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`

`void`
`[setText](#setText(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)`
Replace current text with the given one
`protected final int`
`[textLength](#textLength())()`

`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toAppendableText](#toAppendableText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.text.builders.[TextBuilder](TextBuilder.html)
`[append](TextBuilder.html#append(com.nomagic.text.builders.TextBuilder)), [appendWithNoWrap](TextBuilder.html#appendWithNoWrap(java.lang.CharSequence)), [appendWithSpace](TextBuilder.html#appendWithSpace(com.nomagic.text.builders.TextBuilder)), [appendWithSpace](TextBuilder.html#appendWithSpace(java.lang.CharSequence)), [compress](TextBuilder.html#compress(int)), [isColorSupported](TextBuilder.html#isColorSupported()), [isPlainTextEmpty](TextBuilder.html#isPlainTextEmpty()), [prepend](TextBuilder.html#prepend(com.nomagic.text.builders.TextBuilder)), [prependWithNoWrap](TextBuilder.html#prependWithNoWrap(java.lang.CharSequence)), [setColor](TextBuilder.html#setColor(java.awt.Color)), [setText](TextBuilder.html#setText(com.nomagic.text.builders.TextBuilder)), [toPlainText](TextBuilder.html#toPlainText())`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractTextBuilder
public AbstractTextBuilder()
 ============ METHOD DETAIL ========== 
Method Details
isTextAdded
public boolean isTextAdded()
Specified by:
`[isTextAdded](TextBuilder.html#isTextAdded())` in interface `[TextBuilder](TextBuilder.html)<[T](AbstractTextBuilder.html) extends [AbstractTextBuilder](AbstractTextBuilder.html)>`
Returns:
true if at least one text fragment was added (even if fragment is empty)
append
public [T](AbstractTextBuilder.html) append([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)
Description copied from interface: `[TextBuilder](TextBuilder.html#append(java.lang.CharSequence))`
Append given text
Specified by:
`[append](TextBuilder.html#append(java.lang.CharSequence))` in interface `[TextBuilder](TextBuilder.html)<[T](AbstractTextBuilder.html) extends [AbstractTextBuilder](AbstractTextBuilder.html)>`
Parameters:
`text` - text to append
Returns:
this builder
prepend
public [T](AbstractTextBuilder.html) prepend([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)
Description copied from interface: `[TextBuilder](TextBuilder.html#prepend(java.lang.CharSequence))`
Add given text to the beginning.
Specified by:
`[prepend](TextBuilder.html#prepend(java.lang.CharSequence))` in interface `[TextBuilder](TextBuilder.html)<[T](AbstractTextBuilder.html) extends [AbstractTextBuilder](AbstractTextBuilder.html)>`
Parameters:
`text` - text to append
Returns:
this builder
appendColor
protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) appendColor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
prependColor
protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prependColor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
setText
public void setText([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)
Description copied from interface: `[TextBuilder](TextBuilder.html#setText(java.lang.CharSequence))`
Replace current text with the given one
Specified by:
`[setText](TextBuilder.html#setText(java.lang.CharSequence))` in interface `[TextBuilder](TextBuilder.html)<[T](AbstractTextBuilder.html) extends [AbstractTextBuilder](AbstractTextBuilder.html)>`
Parameters:
`text` - text
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Specified by:
`[toString](TextBuilder.html#toString())` in interface `[TextBuilder](TextBuilder.html)<[T](AbstractTextBuilder.html) extends [AbstractTextBuilder](AbstractTextBuilder.html)>`
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
result string
appendToText
protected final void appendToText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
prependToText
protected final void prependToText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
textLength
protected final int textLength()
replaceText
protected final void replaceText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
toAppendableText
protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toAppendableText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.text.builders</a></div>
<h1 class="title" title="Class AbstractTextBuilder">Class AbstractTextBuilder&lt;T extends AbstractTextBuilder&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.text.builders.AbstractTextBuilder&lt;T&gt;</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;T&gt;</code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="HtmlTextBuilder.html" title="class in com.nomagic.text.builders">HtmlTextBuilder</a></code>, <code><a href="PlainOrFullHtmlTextBuilder.html" title="class in com.nomagic.text.builders">PlainOrFullHtmlTextBuilder</a></code>, <code><a href="PlainOrLightHtmlTextBuilder.html" title="class in com.nomagic.text.builders">PlainOrLightHtmlTextBuilder</a></code>, <code><a href="PlainTextBuilder.html" title="class in com.nomagic.text.builders">PlainTextBuilder</a></code>, <code><a href="RichTextBuilder.html" title="class in com.nomagic.text.builders">RichTextBuilder</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractTextBuilder&lt;T extends AbstractTextBuilder&gt;</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;T&gt;</span></div>
<div class="block">Abstract builder.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AbstractTextBuilder</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="AbstractTextBuilder.html" title="type parameter in AbstractTextBuilder">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#append(java.lang.CharSequence)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Append given text</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#appendColor(java.lang.String)">appendColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#appendToText(java.lang.String)">appendToText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTextAdded()">isTextAdded</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="AbstractTextBuilder.html" title="type parameter in AbstractTextBuilder">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prepend(java.lang.CharSequence)">prepend</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add given text to the beginning.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prependColor(java.lang.String)">prependColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prependToText(java.lang.String)">prependToText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#replaceText(java.lang.String)">replaceText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setText(java.lang.CharSequence)">setText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Replace current text with the given one</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#textLength()">textLength</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toAppendableText(java.lang.String)">toAppendableText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.text.builders.TextBuilder">Methods inherited from interface com.nomagic.text.builders.<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></h3>
<code><a href="TextBuilder.html#append(com.nomagic.text.builders.TextBuilder)">append</a>, <a href="TextBuilder.html#appendWithNoWrap(java.lang.CharSequence)">appendWithNoWrap</a>, <a href="TextBuilder.html#appendWithSpace(com.nomagic.text.builders.TextBuilder)">appendWithSpace</a>, <a href="TextBuilder.html#appendWithSpace(java.lang.CharSequence)">appendWithSpace</a>, <a href="TextBuilder.html#compress(int)">compress</a>, <a href="TextBuilder.html#isColorSupported()">isColorSupported</a>, <a href="TextBuilder.html#isPlainTextEmpty()">isPlainTextEmpty</a>, <a href="TextBuilder.html#prepend(com.nomagic.text.builders.TextBuilder)">prepend</a>, <a href="TextBuilder.html#prependWithNoWrap(java.lang.CharSequence)">prependWithNoWrap</a>, <a href="TextBuilder.html#setColor(java.awt.Color)">setColor</a>, <a href="TextBuilder.html#setText(com.nomagic.text.builders.TextBuilder)">setText</a>, <a href="TextBuilder.html#toPlainText()">toPlainText</a></code></div>
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
<h3>AbstractTextBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractTextBuilder</span>()</div>
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
<section class="detail" id="isTextAdded()">
<h3>isTextAdded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTextAdded</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#isTextAdded()">isTextAdded</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="AbstractTextBuilder.html" title="type parameter in AbstractTextBuilder">T</a> extends <a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>true if at least one text fragment was added (even if fragment is empty)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(java.lang.CharSequence)">
<h3>append</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="AbstractTextBuilder.html" title="type parameter in AbstractTextBuilder">T</a></span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="TextBuilder.html#append(java.lang.CharSequence)">TextBuilder</a></code></span></div>
<div class="block">Append given text</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#append(java.lang.CharSequence)">append</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="AbstractTextBuilder.html" title="type parameter in AbstractTextBuilder">T</a> extends <a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>text</code> - text to append</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prepend(java.lang.CharSequence)">
<h3>prepend</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="AbstractTextBuilder.html" title="type parameter in AbstractTextBuilder">T</a></span> <span class="element-name">prepend</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="TextBuilder.html#prepend(java.lang.CharSequence)">TextBuilder</a></code></span></div>
<div class="block">Add given text to the beginning.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#prepend(java.lang.CharSequence)">prepend</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="AbstractTextBuilder.html" title="type parameter in AbstractTextBuilder">T</a> extends <a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>text</code> - text to append</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendColor(java.lang.String)">
<h3>appendColor</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">appendColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
</section>
</li>
<li>
<section class="detail" id="prependColor(java.lang.String)">
<h3>prependColor</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">prependColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
</section>
</li>
<li>
<section class="detail" id="setText(java.lang.CharSequence)">
<h3>setText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="TextBuilder.html#setText(java.lang.CharSequence)">TextBuilder</a></code></span></div>
<div class="block">Replace current text with the given one</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#setText(java.lang.CharSequence)">setText</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="AbstractTextBuilder.html" title="type parameter in AbstractTextBuilder">T</a> extends <a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>text</code> - text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#toString()">toString</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="AbstractTextBuilder.html" title="type parameter in AbstractTextBuilder">T</a> extends <a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>result string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendToText(java.lang.String)">
<h3>appendToText</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">appendToText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
</section>
</li>
<li>
<section class="detail" id="prependToText(java.lang.String)">
<h3>prependToText</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">prependToText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
</section>
</li>
<li>
<section class="detail" id="textLength()">
<h3>textLength</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">int</span> <span class="element-name">textLength</span>()</div>
</section>
</li>
<li>
<section class="detail" id="replaceText(java.lang.String)">
<h3>replaceText</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">replaceText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
</section>
</li>
<li>
<section class="detail" id="toAppendableText(java.lang.String)">
<h3>toAppendableText</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toAppendableText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
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
