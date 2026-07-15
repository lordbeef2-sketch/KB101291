# JAVA OPENAPI: TextBuilder (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/text/builders/TextBuilder.html
- source_path: `com/nomagic/text/builders/TextBuilder.html`
- source_sha256: `3ebe7f73ab8b66598665df4adfbb761dbfa6f3c4420a12f69593353952f9ec3d`
- captured_utc: `2026-07-14T16:56:09.570616+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.text.builders](package-summary.html)

## Interface TextBuilder<T extends TextBuilder>

All Known Implementing Classes:
`[AbstractTextBuilder](AbstractTextBuilder.html)`, `[ColoredHtmlTextBuilder](ColoredHtmlTextBuilder.html)`, `[ColoredRichTextBuilder](ColoredRichTextBuilder.html)`, `[HtmlTextBuilder](HtmlTextBuilder.html)`, `[PlainOrFullHtmlTextBuilder](PlainOrFullHtmlTextBuilder.html)`, `[PlainOrLightHtmlTextBuilder](PlainOrLightHtmlTextBuilder.html)`, `[PlainTextBuilder](PlainTextBuilder.html)`, `[RawTextBuilder](RawTextBuilder.html)`, `[RichTextBuilder](RichTextBuilder.html)`

@OpenApiAllpublic interfaceTextBuilder<T extends TextBuilder>

A utility used for building plain or rich texts with possibly colored fragments.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`default [T](TextBuilder.html)`
`[append](#append(com.nomagic.text.builders.TextBuilder))([TextBuilder](TextBuilder.html) builder)`
Append text from given builder
`[T](TextBuilder.html)`
`[append](#append(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)`
Append given text
`default [T](TextBuilder.html)`
`[appendWithNoWrap](#appendWithNoWrap(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)`
Append text from the given builder.
`default [T](TextBuilder.html)`
`[appendWithSpace](#appendWithSpace(com.nomagic.text.builders.TextBuilder))([TextBuilder](TextBuilder.html) builder)`
Append given text.
`default [T](TextBuilder.html)`
`[appendWithSpace](#appendWithSpace(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)`
Append given text.
`default void`
`[compress](#compress(int))(int textLength)`
Compress current text to the given length.
`default boolean`
`[isColorSupported](#isColorSupported())()`

`default boolean`
`[isPlainTextEmpty](#isPlainTextEmpty())()`

`boolean`
`[isTextAdded](#isTextAdded())()`

`default [T](TextBuilder.html)`
`[prepend](#prepend(com.nomagic.text.builders.TextBuilder))([TextBuilder](TextBuilder.html) builder)`
Add text to the beginning from the given builder.
`[T](TextBuilder.html)`
`[prepend](#prepend(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)`
Add given text to the beginning.
`default [T](TextBuilder.html)`
`[prependWithNoWrap](#prependWithNoWrap(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)`
Add text to the beginning.
`default [T](TextBuilder.html)`
`[setColor](#setColor(java.awt.Color))([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)`
Set the color of the text which will be added later.
`default [T](TextBuilder.html)`
`[setText](#setText(com.nomagic.text.builders.TextBuilder))([TextBuilder](TextBuilder.html) builder)`
Replaces current text with the one from the given builder
`void`
`[setText](#setText(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)`
Replace current text with the given one
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toPlainText](#toPlainText())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`

============ METHOD DETAIL ========== 
Method Details
append
default [T](TextBuilder.html) append([TextBuilder](TextBuilder.html) builder)
Append text from given builder
Parameters:
`builder` - builder
Returns:
this builder
prepend
default [T](TextBuilder.html) prepend([TextBuilder](TextBuilder.html) builder)
Add text to the beginning from the given builder.
Parameters:
`builder` - builder
Returns:
this builder
prependWithNoWrap
default [T](TextBuilder.html) prependWithNoWrap([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)
Add text to the beginning. Added text will not be wrapped if builder supports that.
Parameters:
`text` - text to prepend
Returns:
this builder
appendWithNoWrap
default [T](TextBuilder.html) appendWithNoWrap([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)
Append text from the given builder. Added text will not be wrapped if builder supports that.
Parameters:
`text` - text to prepend
Returns:
this builder
setText
default [T](TextBuilder.html) setText([TextBuilder](TextBuilder.html) builder)
Replaces current text with the one from the given builder
Parameters:
`builder` - builder
Returns:
this builder
append
[T](TextBuilder.html) append([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)
Append given text
Parameters:
`text` - text to append
Returns:
this builder
appendWithSpace
default [T](TextBuilder.html) appendWithSpace([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)
Append given text. Prepend space before given text if build has text added already.
Parameters:
`text` - text to append
Returns:
this builder
appendWithSpace
default [T](TextBuilder.html) appendWithSpace([TextBuilder](TextBuilder.html) builder)
Append given text. Prepend space before given text if build has text added already.
Parameters:
`builder` - text to append
Returns:
this builder
prepend
[T](TextBuilder.html) prepend([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)
Add given text to the beginning.
Parameters:
`text` - text to append
Returns:
this builder
setColor
default [T](TextBuilder.html) setColor(@CheckForNull
 [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)
Set the color of the text which will be added later. Not every implementation supports that, so color can be ignored.
Parameters:
`color` - color to set. Null is used to reset previously set color
Returns:
this builder
toString
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
result string
toPlainText
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toPlainText()
Returns:
result string as plain text
isPlainTextEmpty
default boolean isPlainTextEmpty()
Returns:
true, if a text converted to a plain is empty in this builder
setText
void setText([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)
Replace current text with the given one
Parameters:
`text` - text
compress
default void compress(int textLength)
Compress current text to the given length. This function is not supported in every implementation, so it can be ignored.
Parameters:
`textLength` - text length
isTextAdded
boolean isTextAdded()
Returns:
true if at least one text fragment was added (even if fragment is empty)
isColorSupported
default boolean isColorSupported()
Returns:
true if builder supports color

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.text.builders</a></div>
<h1 class="title" title="Interface TextBuilder">Interface TextBuilder&lt;T extends TextBuilder&gt;</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="AbstractTextBuilder.html" title="class in com.nomagic.text.builders">AbstractTextBuilder</a></code>, <code><a href="ColoredHtmlTextBuilder.html" title="class in com.nomagic.text.builders">ColoredHtmlTextBuilder</a></code>, <code><a href="ColoredRichTextBuilder.html" title="class in com.nomagic.text.builders">ColoredRichTextBuilder</a></code>, <code><a href="HtmlTextBuilder.html" title="class in com.nomagic.text.builders">HtmlTextBuilder</a></code>, <code><a href="PlainOrFullHtmlTextBuilder.html" title="class in com.nomagic.text.builders">PlainOrFullHtmlTextBuilder</a></code>, <code><a href="PlainOrLightHtmlTextBuilder.html" title="class in com.nomagic.text.builders">PlainOrLightHtmlTextBuilder</a></code>, <code><a href="PlainTextBuilder.html" title="class in com.nomagic.text.builders">PlainTextBuilder</a></code>, <code><a href="RawTextBuilder.html" title="class in com.nomagic.text.builders">RawTextBuilder</a></code>, <code><a href="RichTextBuilder.html" title="class in com.nomagic.text.builders">RichTextBuilder</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">TextBuilder&lt;T extends TextBuilder&gt;</span></div>
<div class="block">A utility used for building plain or rich texts with possibly colored fragments.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#append(com.nomagic.text.builders.TextBuilder)">append</a><wbr/>(<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> builder)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Append text from given builder</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#append(java.lang.CharSequence)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Append given text</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#appendWithNoWrap(java.lang.CharSequence)">appendWithNoWrap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Append text from the given builder.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#appendWithSpace(com.nomagic.text.builders.TextBuilder)">appendWithSpace</a><wbr/>(<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> builder)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Append given text.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#appendWithSpace(java.lang.CharSequence)">appendWithSpace</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Append given text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#compress(int)">compress</a><wbr/>(int textLength)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Compress current text to the given length.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isColorSupported()">isColorSupported</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isPlainTextEmpty()">isPlainTextEmpty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isTextAdded()">isTextAdded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#prepend(com.nomagic.text.builders.TextBuilder)">prepend</a><wbr/>(<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> builder)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Add text to the beginning from the given builder.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#prepend(java.lang.CharSequence)">prepend</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Add given text to the beginning.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#prependWithNoWrap(java.lang.CharSequence)">prependWithNoWrap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Add text to the beginning.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#setColor(java.awt.Color)">setColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Set the color of the text which will be added later.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#setText(com.nomagic.text.builders.TextBuilder)">setText</a><wbr/>(<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> builder)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Replaces current text with the one from the given builder</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setText(java.lang.CharSequence)">setText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Replace current text with the given one</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#toPlainText()">toPlainText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="append(com.nomagic.text.builders.TextBuilder)">
<h3>append</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></span> <span class="element-name">append</span><wbr/><span class="parameters">(<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> builder)</span></div>
<div class="block">Append text from given builder</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>builder</code> - builder</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prepend(com.nomagic.text.builders.TextBuilder)">
<h3>prepend</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></span> <span class="element-name">prepend</span><wbr/><span class="parameters">(<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> builder)</span></div>
<div class="block">Add text to the beginning from the given builder.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>builder</code> - builder</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prependWithNoWrap(java.lang.CharSequence)">
<h3>prependWithNoWrap</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></span> <span class="element-name">prependWithNoWrap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</span></div>
<div class="block">Add text to the beginning. Added text will not be wrapped if builder supports that.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text to prepend</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendWithNoWrap(java.lang.CharSequence)">
<h3>appendWithNoWrap</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></span> <span class="element-name">appendWithNoWrap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</span></div>
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
<section class="detail" id="setText(com.nomagic.text.builders.TextBuilder)">
<h3>setText</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></span> <span class="element-name">setText</span><wbr/><span class="parameters">(<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> builder)</span></div>
<div class="block">Replaces current text with the one from the given builder</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>builder</code> - builder</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(java.lang.CharSequence)">
<h3>append</h3>
<div class="member-signature"><span class="return-type"><a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</span></div>
<div class="block">Append given text</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text to append</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendWithSpace(java.lang.CharSequence)">
<h3>appendWithSpace</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></span> <span class="element-name">appendWithSpace</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</span></div>
<div class="block">Append given text. Prepend space before given text if build has text added already.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text to append</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendWithSpace(com.nomagic.text.builders.TextBuilder)">
<h3>appendWithSpace</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></span> <span class="element-name">appendWithSpace</span><wbr/><span class="parameters">(<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> builder)</span></div>
<div class="block">Append given text. Prepend space before given text if build has text added already.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>builder</code> - text to append</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prepend(java.lang.CharSequence)">
<h3>prepend</h3>
<div class="member-signature"><span class="return-type"><a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></span> <span class="element-name">prepend</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</span></div>
<div class="block">Add given text to the beginning.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text to append</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setColor(java.awt.Color)">
<h3>setColor</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="TextBuilder.html" title="type parameter in TextBuilder">T</a></span> <span class="element-name">setColor</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</span></div>
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
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>result string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toPlainText()">
<h3>toPlainText</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toPlainText</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>result string as plain text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPlainTextEmpty()">
<h3>isPlainTextEmpty</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isPlainTextEmpty</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if a text converted to a plain is empty in this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setText(java.lang.CharSequence)">
<h3>setText</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</span></div>
<div class="block">Replace current text with the given one</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compress(int)">
<h3>compress</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">compress</span><wbr/><span class="parameters">(int textLength)</span></div>
<div class="block">Compress current text to the given length. This function is not supported in every implementation, so it can be ignored.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>textLength</code> - text length</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTextAdded()">
<h3>isTextAdded</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isTextAdded</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if at least one text fragment was added (even if fragment is empty)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isColorSupported()">
<h3>isColorSupported</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isColorSupported</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if builder supports color</dd>
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
