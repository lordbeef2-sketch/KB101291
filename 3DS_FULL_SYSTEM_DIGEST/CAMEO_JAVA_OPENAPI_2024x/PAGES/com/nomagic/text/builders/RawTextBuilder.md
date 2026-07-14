# JAVA OPENAPI: RawTextBuilder (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/text/builders/RawTextBuilder.html
- source_path: `com/nomagic/text/builders/RawTextBuilder.html`
- source_sha256: `4cec36355f98a8236850c5a430607a557518baf3ed017492ca8b804bc7c56da3`
- captured_utc: `2026-07-14T16:52:33.080160+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.text.builders](package-summary.html)

## Class RawTextBuilder<T extends RawTextBuilder>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.text.builders.RawTextBuilder<T>

All Implemented Interfaces:
`[TextBuilder](TextBuilder.html)<T>`

@OpenApiAllpublic classRawTextBuilder<T extends RawTextBuilder>
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [TextBuilder](TextBuilder.html)<T>

Builds a text without any transformation - input text is appended to the output text.
 Builder does not support colored fragments directly - result text does not have colors. However colors are be supported
 if [`appendTo(TextBuilder)`](#appendTo(com.nomagic.text.builders.TextBuilder)) is used and proper builder is passed.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[RawTextBuilder](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[T](RawTextBuilder.html)`
`[append](#append(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)`
Append given text
`void`
`[appendTo](#appendTo(com.nomagic.text.builders.TextBuilder))([TextBuilder](TextBuilder.html) builder)`
Appends text from this builder to the given one.
`boolean`
`[isColorSupported](#isColorSupported())()`

`boolean`
`[isTextAdded](#isTextAdded())()`

`[T](RawTextBuilder.html)`
`[prepend](#prepend(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)`
Add given text to the beginning.
`[T](RawTextBuilder.html)`
`[setColor](#setColor(java.awt.Color))([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)`
Set color of the text which will be added later.
`void`
`[setText](#setText(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)`
Replace current text with the given one
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toPlainText](#toPlainText())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.text.builders.[TextBuilder](TextBuilder.html)
`[append](TextBuilder.html#append(com.nomagic.text.builders.TextBuilder)), [appendWithNoWrap](TextBuilder.html#appendWithNoWrap(java.lang.CharSequence)), [appendWithSpace](TextBuilder.html#appendWithSpace(com.nomagic.text.builders.TextBuilder)), [appendWithSpace](TextBuilder.html#appendWithSpace(java.lang.CharSequence)), [compress](TextBuilder.html#compress(int)), [isPlainTextEmpty](TextBuilder.html#isPlainTextEmpty()), [prepend](TextBuilder.html#prepend(com.nomagic.text.builders.TextBuilder)), [prependWithNoWrap](TextBuilder.html#prependWithNoWrap(java.lang.CharSequence)), [setText](TextBuilder.html#setText(com.nomagic.text.builders.TextBuilder))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
RawTextBuilder
public RawTextBuilder()
 ============ METHOD DETAIL ========== 
Method Details
append
public [T](RawTextBuilder.html) append([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)
Description copied from interface: `[TextBuilder](TextBuilder.html#append(java.lang.CharSequence))`
Append given text
Specified by:
`[append](TextBuilder.html#append(java.lang.CharSequence))` in interface `[TextBuilder](TextBuilder.html)<[T](RawTextBuilder.html) extends [RawTextBuilder](RawTextBuilder.html)>`
Parameters:
`text` - text to append
Returns:
this builder
prepend
public [T](RawTextBuilder.html) prepend([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)
Description copied from interface: `[TextBuilder](TextBuilder.html#prepend(java.lang.CharSequence))`
Add given text to the beginning.
Specified by:
`[prepend](TextBuilder.html#prepend(java.lang.CharSequence))` in interface `[TextBuilder](TextBuilder.html)<[T](RawTextBuilder.html) extends [RawTextBuilder](RawTextBuilder.html)>`
Parameters:
`text` - text to append
Returns:
this builder
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Specified by:
`[toString](TextBuilder.html#toString())` in interface `[TextBuilder](TextBuilder.html)<[T](RawTextBuilder.html) extends [RawTextBuilder](RawTextBuilder.html)>`
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
result string
setText
public void setText([CharSequence](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html) text)
Description copied from interface: `[TextBuilder](TextBuilder.html#setText(java.lang.CharSequence))`
Replace current text with the given one
Specified by:
`[setText](TextBuilder.html#setText(java.lang.CharSequence))` in interface `[TextBuilder](TextBuilder.html)<[T](RawTextBuilder.html) extends [RawTextBuilder](RawTextBuilder.html)>`
Parameters:
`text` - text
toPlainText
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toPlainText()
Specified by:
`[toPlainText](TextBuilder.html#toPlainText())` in interface `[TextBuilder](TextBuilder.html)<[T](RawTextBuilder.html) extends [RawTextBuilder](RawTextBuilder.html)>`
Returns:
result string as plain text
setColor
public [T](RawTextBuilder.html) setColor(@CheckForNull
 [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)
Description copied from interface: `[TextBuilder](TextBuilder.html#setColor(java.awt.Color))`
Set color of the text which will be added later. Not every implementation supports that, so color can be ignored.
Specified by:
`[setColor](TextBuilder.html#setColor(java.awt.Color))` in interface `[TextBuilder](TextBuilder.html)<[T](RawTextBuilder.html) extends [RawTextBuilder](RawTextBuilder.html)>`
Parameters:
`color` - color to set. Null is used to reset previously set color
Returns:
this builder
isColorSupported
public boolean isColorSupported()
Specified by:
`[isColorSupported](TextBuilder.html#isColorSupported())` in interface `[TextBuilder](TextBuilder.html)<[T](RawTextBuilder.html) extends [RawTextBuilder](RawTextBuilder.html)>`
Returns:
true if builder supports color
appendTo
public void appendTo([TextBuilder](TextBuilder.html) builder)
Appends text from this builder to the given one.
Parameters:
`builder` - given builder
isTextAdded
public boolean isTextAdded()
Specified by:
`[isTextAdded](TextBuilder.html#isTextAdded())` in interface `[TextBuilder](TextBuilder.html)<[T](RawTextBuilder.html) extends [RawTextBuilder](RawTextBuilder.html)>`
Returns:
true if at least one text fragment was added (even if fragment is empty)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.text.builders</a></div>
<h1 class="title" title="Class RawTextBuilder">Class RawTextBuilder&lt;T extends RawTextBuilder&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.text.builders.RawTextBuilder&lt;T&gt;</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;T&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">RawTextBuilder&lt;T extends RawTextBuilder&gt;</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;T&gt;</span></div>
<div class="block">Builds a text without any transformation - input text is appended to the output text.
 Builder does not support colored fragments directly - result text does not have colors. However colors are be supported
 if <a href="#appendTo(com.nomagic.text.builders.TextBuilder)"><code>appendTo(TextBuilder)</code></a> is used and proper builder is passed.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">RawTextBuilder</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#append(java.lang.CharSequence)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Append given text</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#appendTo(com.nomagic.text.builders.TextBuilder)">appendTo</a><wbr/>(<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> builder)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Appends text from this builder to the given one.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isColorSupported()">isColorSupported</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTextAdded()">isTextAdded</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prepend(java.lang.CharSequence)">prepend</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add given text to the beginning.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColor(java.awt.Color)">setColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set color of the text which will be added later.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setText(java.lang.CharSequence)">setText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Replace current text with the given one</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toPlainText()">toPlainText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.text.builders.TextBuilder">Methods inherited from interface com.nomagic.text.builders.<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></h3>
<code><a href="TextBuilder.html#append(com.nomagic.text.builders.TextBuilder)">append</a>, <a href="TextBuilder.html#appendWithNoWrap(java.lang.CharSequence)">appendWithNoWrap</a>, <a href="TextBuilder.html#appendWithSpace(com.nomagic.text.builders.TextBuilder)">appendWithSpace</a>, <a href="TextBuilder.html#appendWithSpace(java.lang.CharSequence)">appendWithSpace</a>, <a href="TextBuilder.html#compress(int)">compress</a>, <a href="TextBuilder.html#isPlainTextEmpty()">isPlainTextEmpty</a>, <a href="TextBuilder.html#prepend(com.nomagic.text.builders.TextBuilder)">prepend</a>, <a href="TextBuilder.html#prependWithNoWrap(java.lang.CharSequence)">prependWithNoWrap</a>, <a href="TextBuilder.html#setText(com.nomagic.text.builders.TextBuilder)">setText</a></code></div>
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
<h3>RawTextBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RawTextBuilder</span>()</div>
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
<section class="detail" id="append(java.lang.CharSequence)">
<h3>append</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a></span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="TextBuilder.html#append(java.lang.CharSequence)">TextBuilder</a></code></span></div>
<div class="block">Append given text</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#append(java.lang.CharSequence)">append</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a> extends <a href="RawTextBuilder.html" title="class in com.nomagic.text.builders">RawTextBuilder</a>&gt;</code></dd>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a></span> <span class="element-name">prepend</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> text)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="TextBuilder.html#prepend(java.lang.CharSequence)">TextBuilder</a></code></span></div>
<div class="block">Add given text to the beginning.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#prepend(java.lang.CharSequence)">prepend</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a> extends <a href="RawTextBuilder.html" title="class in com.nomagic.text.builders">RawTextBuilder</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>text</code> - text to append</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#toString()">toString</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a> extends <a href="RawTextBuilder.html" title="class in com.nomagic.text.builders">RawTextBuilder</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>result string</dd>
</dl>
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
<dd><code><a href="TextBuilder.html#setText(java.lang.CharSequence)">setText</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a> extends <a href="RawTextBuilder.html" title="class in com.nomagic.text.builders">RawTextBuilder</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>text</code> - text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toPlainText()">
<h3>toPlainText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toPlainText</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#toPlainText()">toPlainText</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a> extends <a href="RawTextBuilder.html" title="class in com.nomagic.text.builders">RawTextBuilder</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>result string as plain text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setColor(java.awt.Color)">
<h3>setColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a></span> <span class="element-name">setColor</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="TextBuilder.html#setColor(java.awt.Color)">TextBuilder</a></code></span></div>
<div class="block">Set color of the text which will be added later. Not every implementation supports that, so color can be ignored.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#setColor(java.awt.Color)">setColor</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a> extends <a href="RawTextBuilder.html" title="class in com.nomagic.text.builders">RawTextBuilder</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>color</code> - color to set. Null is used to reset previously set color</dd>
<dt>Returns:</dt>
<dd>this builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isColorSupported()">
<h3>isColorSupported</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isColorSupported</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#isColorSupported()">isColorSupported</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a> extends <a href="RawTextBuilder.html" title="class in com.nomagic.text.builders">RawTextBuilder</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>true if builder supports color</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendTo(com.nomagic.text.builders.TextBuilder)">
<h3>appendTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">appendTo</span><wbr/><span class="parameters">(<a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> builder)</span></div>
<div class="block">Appends text from this builder to the given one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>builder</code> - given builder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTextAdded()">
<h3>isTextAdded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTextAdded</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TextBuilder.html#isTextAdded()">isTextAdded</a></code> in interface <code><a href="TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&lt;<a href="RawTextBuilder.html" title="type parameter in RawTextBuilder">T</a> extends <a href="RawTextBuilder.html" title="class in com.nomagic.text.builders">RawTextBuilder</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>true if at least one text fragment was added (even if fragment is empty)</dd>
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
