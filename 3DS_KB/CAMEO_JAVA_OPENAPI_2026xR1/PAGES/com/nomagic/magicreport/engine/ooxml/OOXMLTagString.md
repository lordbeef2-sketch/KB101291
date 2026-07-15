# JAVA OPENAPI: OOXMLTagString (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/ooxml/OOXMLTagString.html
- source_path: `com/nomagic/magicreport/engine/ooxml/OOXMLTagString.html`
- source_sha256: `df611a84fb2b28136c6066279ba35049178a8f97d01c66449e0d461195460a50`
- captured_utc: `2026-07-14T16:46:12.207963+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.ooxml](package-summary.html)

## Class OOXMLTagString

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.engine.ooxml.OOXMLTagString

All Implemented Interfaces:
`[IVariable](../../IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`

@OpenApiAllpublic classOOXMLTagString
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html), [IVariable](../../IVariable.html)

String in OOXML format.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.engine.ooxml.OOXMLTagString)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[OOXMLTagString](#%3Cinit%3E(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) charSequence)`
Constructs a retained string that contains the same characters as the specified CharSequence.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`char`
`[charAt](#charAt(int))(int index)`
Returns the `char` value at the specified index.
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) anObject)`
Compares this HTMLString to the specified object.
`int`
`[hashCode](#hashCode())()`
Returns a hash code for this HTMLString.
`int`
`[length](#length())()`
Returns the length of this character sequence.
`[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[subSequence](#subSequence(int,int))(int start,
 int end)`
Returns a new `CharSequence` that is a subsequence of this sequence.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Returns a string containing the characters in this sequence in the same order as this sequence.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.lang.[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)
`[chars](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#chars()), [codePoints](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#codePoints()), [isEmpty](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#isEmpty())`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
OOXMLTagString
public OOXMLTagString([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) charSequence)
Constructs a retained string that contains the same characters as the specified CharSequence.
Parameters:
`charSequence` - the sequence to copy.
 ============ METHOD DETAIL ========== 
Method Details
charAt
public char charAt(int index)
Returns the `char` value at the specified index. An index ranges from zero to
 length() - 1. The first `char` value of the sequence is at index zero, the next at
 index one, and so on, as for array indexing.
 If the `char` value specified by the index is a [surrogate](Character.html#unicode), the surrogate value is returned.
Specified by:
`[charAt](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#charAt(int))` in interface `[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
Parameters:
`index` - the index of the `char` value to be returned
Returns:
the specified `char` value
Throws:
`[IndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IndexOutOfBoundsException.html)` - if the index argument is negative or not less than
 length()
See Also:
[`CharSequence.charAt(int)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#charAt(int))
length
public int length()
Returns the length of this character sequence. The length is the number of 16-bit `char`s in
 the sequence.
Specified by:
`[length](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#length())` in interface `[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
Returns:
the number of `char`s in this sequence
See Also:
[`CharSequence.length()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#length())
subSequence
public [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) subSequence(int start,
 int end)
Returns a new `CharSequence` that is a subsequence of this sequence. The subsequence starts
 with the `char` value at the specified index and ends with the `char` value at
 index end - 1. The length (in `char`s) of the returned sequence is
 end - start, so if start == end then an empty sequence is returned.
Specified by:
`[subSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#subSequence(int,int))` in interface `[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
Parameters:
`start` - the start index, inclusive
`end` - the end index, exclusive
Returns:
the specified subsequence
Throws:
`[IndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IndexOutOfBoundsException.html)` - if start or end are negative, if end is
 greater than length(), or if start is greater than end
See Also:
[`CharSequence.subSequence(int, int)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#subSequence(int,int))
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Returns a string containing the characters in this sequence in the same order as this sequence. The
 length of the string will be the length of this sequence.
Specified by:
`[toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#toString())` in interface `[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
a string consisting of exactly this sequence of characters
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) anObject)
Compares this HTMLString to the specified object. The result is `true` if and only if the argument
 is not `null` and is a `HTMLString` object that represents the same sequence of characters as
 this object.
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Parameters:
`anObject` - The object to compare this `HTMLString` against
Returns:
`true` if the given object represents a `HTMLString` equivalent to this HTMLString,
 `false` otherwise
hashCode
public int hashCode()
Returns a hash code for this HTMLString.
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
a hash code value for this object.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.ooxml</a></div>
<h1 class="title" title="Class OOXMLTagString">Class OOXMLTagString</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.engine.ooxml.OOXMLTagString</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">OOXMLTagString</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a>, <a href="../../IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></span></div>
<div class="block">String in OOXML format.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.engine.ooxml.OOXMLTagString">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.CharSequence)">OOXMLTagString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> charSequence)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a retained string that contains the same characters as the specified CharSequence.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>char</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#charAt(int)">charAt</a><wbr/>(int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the <code>char</code> value at the specified index.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> anObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Compares this HTMLString to the specified object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a hash code for this HTMLString.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#length()">length</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the length of this character sequence.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#subSequence(int,int)">subSequence</a><wbr/>(int start,
 int end)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a new <code>CharSequence</code> that is a subsequence of this sequence.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a string containing the characters in this sequence in the same order as this sequence.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.CharSequence">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#chars()" title="class or interface in java.lang">chars</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#codePoints()" title="class or interface in java.lang">codePoints</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#isEmpty()" title="class or interface in java.lang">isEmpty</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.CharSequence)">
<h3>OOXMLTagString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OOXMLTagString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> charSequence)</span></div>
<div class="block">Constructs a retained string that contains the same characters as the specified CharSequence.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>charSequence</code> - the sequence to copy.</dd>
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
<section class="detail" id="charAt(int)">
<h3>charAt</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">char</span> <span class="element-name">charAt</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block">Returns the <code>char</code> value at the specified index. An index ranges from zero to
 <tt>length() - 1</tt>. The first <code>char</code> value of the sequence is at index zero, the next at
 index one, and so on, as for array indexing.
 <p>
 If the <code>char</code> value specified by the index is a <a href="Character.html#unicode">surrogate</a>, the surrogate value is returned.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#charAt(int)" title="class or interface in java.lang">charAt</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></dd>
<dt>Parameters:</dt>
<dd><code>index</code> - the index of the <code>char</code> value to be returned</dd>
<dt>Returns:</dt>
<dd>the specified <code>char</code> value</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IndexOutOfBoundsException.html" title="class or interface in java.lang">IndexOutOfBoundsException</a></code> - if the <tt>index</tt> argument is negative or not less than
            <tt>length()</tt></dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#charAt(int)" title="class or interface in java.lang"><code>CharSequence.charAt(int)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="length()">
<h3>length</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">length</span>()</div>
<div class="block">Returns the length of this character sequence. The length is the number of 16-bit <code>char</code>s in
 the sequence.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#length()" title="class or interface in java.lang">length</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></dd>
<dt>Returns:</dt>
<dd>the number of <code>char</code>s in this sequence</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#length()" title="class or interface in java.lang"><code>CharSequence.length()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="subSequence(int,int)">
<h3>subSequence</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">subSequence</span><wbr/><span class="parameters">(int start,
 int end)</span></div>
<div class="block">Returns a new <code>CharSequence</code> that is a subsequence of this sequence. The subsequence starts
 with the <code>char</code> value at the specified index and ends with the <code>char</code> value at
 index <tt>end - 1</tt>. The length (in <code>char</code>s) of the returned sequence is
 <tt>end - start</tt>, so if <tt>start == end</tt> then an empty sequence is returned.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#subSequence(int,int)" title="class or interface in java.lang">subSequence</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></dd>
<dt>Parameters:</dt>
<dd><code>start</code> - the start index, inclusive</dd>
<dd><code>end</code> - the end index, exclusive</dd>
<dt>Returns:</dt>
<dd>the specified subsequence</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IndexOutOfBoundsException.html" title="class or interface in java.lang">IndexOutOfBoundsException</a></code> - if <tt>start</tt> or <tt>end</tt> are negative, if <tt>end</tt> is
            greater than <tt>length()</tt>, or if <tt>start</tt> is greater than <tt>end</tt></dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#subSequence(int,int)" title="class or interface in java.lang"><code>CharSequence.subSequence(int, int)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Returns a string containing the characters in this sequence in the same order as this sequence. The
 length of the string will be the length of this sequence.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html#toString()" title="class or interface in java.lang">toString</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>a string consisting of exactly this sequence of characters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> anObject)</span></div>
<div class="block">Compares this HTMLString to the specified object. The result is <code>true</code> if and only if the argument
 is not <code>null</code> and is a <code>HTMLString</code> object that represents the same sequence of characters as
 this object.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Parameters:</dt>
<dd><code>anObject</code> - The object to compare this <code>HTMLString</code> against</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the given object represents a <code>HTMLString</code> equivalent to this HTMLString,
         <code>false</code> otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<div class="block">Returns a hash code for this HTMLString.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>a hash code value for this object.</dd>
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
