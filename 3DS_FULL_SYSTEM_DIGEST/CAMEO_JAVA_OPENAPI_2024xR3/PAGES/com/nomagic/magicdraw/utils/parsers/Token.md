# JAVA OPENAPI: Token (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/utils/parsers/Token.html
- source_path: `com/nomagic/magicdraw/utils/parsers/Token.html`
- source_sha256: `ad0103d9436cafb7974cc6a629d3af1cbb0622a8bd504394a291f1bba549a046`
- captured_utc: `2026-07-14T16:56:08.092599+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.utils.parsers](package-summary.html)

## Class Token

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.utils.parsers.Token

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`

@OpenApiAllpublic classToken
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)

Describes the input token stream.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.utils.parsers.Token)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`int`
`[beginColumn](#beginColumn)`
The column number of the first character of this Token.
`int`
`[beginLine](#beginLine)`
The line number of the first character of this Token.
`int`
`[endColumn](#endColumn)`
The column number of the last character of this Token.
`int`
`[endLine](#endLine)`
The line number of the last character of this Token.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[image](#image)`
The string image of the token.
`int`
`[kind](#kind)`
An integer that describes the kind of this token.
`[Token](Token.html)`
`[next](#next)`
A reference to the next regular (non-special) token from the input
 stream.
`[Token](Token.html)`
`[specialToken](#specialToken)`
This field is used to access special tokens that occur prior to this
 token, but after the immediately preceding regular (non-special) token.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Token](#%3Cinit%3E())()`
No-argument constructor
`[Token](#%3Cinit%3E(int))(int kind)`
Constructs a new token for the specified Image.
`[Token](#%3Cinit%3E(int,java.lang.String))(int kind,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) image)`
Constructs a new token for the specified Image and Kind.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue())()`
An optional attribute value of the Token.
`static [Token](Token.html)`
`[newToken](#newToken(int))(int ofKind)`

`static [Token](Token.html)`
`[newToken](#newToken(int,java.lang.String))(int ofKind,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) image)`
Returns a new Token object, by default.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Returns the image.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
kind
public int kind
An integer that describes the kind of this token. This numbering
 system is determined by JavaCCParser, and a table of these numbers is
 stored in the file ...Constants.java.
beginLine
public int beginLine
The line number of the first character of this Token.
beginColumn
public int beginColumn
The column number of the first character of this Token.
endLine
public int endLine
The line number of the last character of this Token.
endColumn
public int endColumn
The column number of the last character of this Token.
image
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) image
The string image of the token.
next
public [Token](Token.html) next
A reference to the next regular (non-special) token from the input
 stream. If this is the last token from the input stream, or if the
 token manager has not read tokens beyond this one, this field is
 set to null. This is true only if this token is also a regular
 token. Otherwise, see below for a description of the contents of
 this field.
specialToken
public [Token](Token.html) specialToken
This field is used to access special tokens that occur prior to this
 token, but after the immediately preceding regular (non-special) token.
 If there are no such special tokens, this field is set to null.
 When there are more than one such special token, this field refers
 to the last of these special tokens, which in turn refers to the next
 previous special token through its specialToken field, and so on
 until the first special token (whose specialToken field is null).
 The next fields of special tokens refer to other special tokens that
 immediately follow it (without an intervening regular token). If there
 is no such token, this field is null.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Token
public Token()
No-argument constructor
Token
public Token(int kind)
Constructs a new token for the specified Image.
Token
public Token(int kind,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) image)
Constructs a new token for the specified Image and Kind.
 ============ METHOD DETAIL ========== 
Method Details
getValue
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getValue()
An optional attribute value of the Token.
 Tokens which are not used as syntactic sugar will often contain
 meaningful values that will be used later on by the compiler or
 interpreter. This attribute value is often different from the image.
 Any subclass of Token that actually wants to return a non-null value can
 override this method as appropriate.
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Returns the image.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
newToken
public static [Token](Token.html) newToken(int ofKind,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) image)
Returns a new Token object, by default. However, if you want, you
 can create and return subclass objects based on the value of ofKind.
 Simply add the cases to the switch for all those special cases.
 For example, if you have a subclass of Token called IDToken that
 you want to create if ofKind is ID, simply add something like :

 case MyParserConstants.ID : return new IDToken(ofKind, image);

 to the following switch statement. Then you can cast matchedToken
 variable to the appropriate type and use sit in your lexical actions.
newToken
public static [Token](Token.html) newToken(int ofKind)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.utils.parsers</a></div>
<h1 class="title" title="Class Token">Class Token</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.utils.parsers.Token</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Token</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></span></div>
<div class="block">Describes the input token stream.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.utils.parsers.Token">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#beginColumn">beginColumn</a></code></div>
<div class="col-last even-row-color">
<div class="block">The column number of the first character of this Token.</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#beginLine">beginLine</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The line number of the first character of this Token.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#endColumn">endColumn</a></code></div>
<div class="col-last even-row-color">
<div class="block">The column number of the last character of this Token.</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#endLine">endLine</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The line number of the last character of this Token.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#image">image</a></code></div>
<div class="col-last even-row-color">
<div class="block">The string image of the token.</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#kind">kind</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An integer that describes the kind of this token.</div>
</div>
<div class="col-first even-row-color"><code><a href="Token.html" title="class in com.nomagic.magicdraw.utils.parsers">Token</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#next">next</a></code></div>
<div class="col-last even-row-color">
<div class="block">A reference to the next regular (non-special) token from the input
 stream.</div>
</div>
<div class="col-first odd-row-color"><code><a href="Token.html" title="class in com.nomagic.magicdraw.utils.parsers">Token</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#specialToken">specialToken</a></code></div>
<div class="col-last odd-row-color">
<div class="block">This field is used to access special tokens that occur prior to this
 token, but after the immediately preceding regular (non-special) token.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Token</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">No-argument constructor</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(int)">Token</a><wbr/>(int kind)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new token for the specified Image.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(int,java.lang.String)">Token</a><wbr/>(int kind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> image)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new token for the specified Image and Kind.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue()">getValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">An optional attribute value of the Token.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Token.html" title="class in com.nomagic.magicdraw.utils.parsers">Token</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#newToken(int)">newToken</a><wbr/>(int ofKind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Token.html" title="class in com.nomagic.magicdraw.utils.parsers">Token</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#newToken(int,java.lang.String)">newToken</a><wbr/>(int ofKind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> image)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a new Token object, by default.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the image.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="kind">
<h3>kind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">kind</span></div>
<div class="block">An integer that describes the kind of this token.  This numbering
 system is determined by JavaCCParser, and a table of these numbers is
 stored in the file ...Constants.java.</div>
</section>
</li>
<li>
<section class="detail" id="beginLine">
<h3>beginLine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">beginLine</span></div>
<div class="block">The line number of the first character of this Token.</div>
</section>
</li>
<li>
<section class="detail" id="beginColumn">
<h3>beginColumn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">beginColumn</span></div>
<div class="block">The column number of the first character of this Token.</div>
</section>
</li>
<li>
<section class="detail" id="endLine">
<h3>endLine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">endLine</span></div>
<div class="block">The line number of the last character of this Token.</div>
</section>
</li>
<li>
<section class="detail" id="endColumn">
<h3>endColumn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">endColumn</span></div>
<div class="block">The column number of the last character of this Token.</div>
</section>
</li>
<li>
<section class="detail" id="image">
<h3>image</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">image</span></div>
<div class="block">The string image of the token.</div>
</section>
</li>
<li>
<section class="detail" id="next">
<h3>next</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="Token.html" title="class in com.nomagic.magicdraw.utils.parsers">Token</a></span> <span class="element-name">next</span></div>
<div class="block">A reference to the next regular (non-special) token from the input
 stream.  If this is the last token from the input stream, or if the
 token manager has not read tokens beyond this one, this field is
 set to null.  This is true only if this token is also a regular
 token.  Otherwise, see below for a description of the contents of
 this field.</div>
</section>
</li>
<li>
<section class="detail" id="specialToken">
<h3>specialToken</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="Token.html" title="class in com.nomagic.magicdraw.utils.parsers">Token</a></span> <span class="element-name">specialToken</span></div>
<div class="block">This field is used to access special tokens that occur prior to this
 token, but after the immediately preceding regular (non-special) token.
 If there are no such special tokens, this field is set to null.
 When there are more than one such special token, this field refers
 to the last of these special tokens, which in turn refers to the next
 previous special token through its specialToken field, and so on
 until the first special token (whose specialToken field is null).
 The next fields of special tokens refer to other special tokens that
 immediately follow it (without an intervening regular token).  If there
 is no such token, this field is null.</div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>Token</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Token</span>()</div>
<div class="block">No-argument constructor</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(int)">
<h3>Token</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Token</span><wbr/><span class="parameters">(int kind)</span></div>
<div class="block">Constructs a new token for the specified Image.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(int,java.lang.String)">
<h3>Token</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Token</span><wbr/><span class="parameters">(int kind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> image)</span></div>
<div class="block">Constructs a new token for the specified Image and Kind.</div>
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
<section class="detail" id="getValue()">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span>()</div>
<div class="block">An optional attribute value of the Token.
 Tokens which are not used as syntactic sugar will often contain
 meaningful values that will be used later on by the compiler or
 interpreter. This attribute value is often different from the image.
 Any subclass of Token that actually wants to return a non-null value can
 override this method as appropriate.</div>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Returns the image.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="newToken(int,java.lang.String)">
<h3>newToken</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Token.html" title="class in com.nomagic.magicdraw.utils.parsers">Token</a></span> <span class="element-name">newToken</span><wbr/><span class="parameters">(int ofKind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> image)</span></div>
<div class="block">Returns a new Token object, by default. However, if you want, you
 can create and return subclass objects based on the value of ofKind.
 Simply add the cases to the switch for all those special cases.
 For example, if you have a subclass of Token called IDToken that
 you want to create if ofKind is ID, simply add something like :

    case MyParserConstants.ID : return new IDToken(ofKind, image);

 to the following switch statement. Then you can cast matchedToken
 variable to the appropriate type and use sit in your lexical actions.</div>
</section>
</li>
<li>
<section class="detail" id="newToken(int)">
<h3>newToken</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Token.html" title="class in com.nomagic.magicdraw.utils.parsers">Token</a></span> <span class="element-name">newToken</span><wbr/><span class="parameters">(int ofKind)</span></div>
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
