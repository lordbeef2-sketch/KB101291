# JAVA OPENAPI: UUIDGenerator (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/helper/UUIDGenerator.html
- source_path: `com/nomagic/magicreport/helper/UUIDGenerator.html`
- source_sha256: `41a0e64e28e741153ad38693f7f71b85962bcb19389e13a19df59f8d8f6a105b`
- captured_utc: `2026-07-14T16:46:14.440992+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.helper](package-summary.html)

## Class UUIDGenerator

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.helper.UUIDGenerator

@OpenApiAllpublic final classUUIDGenerator
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Create universal unique id.
 Magic Draw element id consists of :
 
 `"_" + ApplicationConstants.VERSION + ApplicationConstants.PATCH_NUMBER + "_" + System.currentTimeMillis() + "_" +
 Math.round(Math.random() * 1000000) + "_" + count++;`
 
 There is a very less change that element id is not unique.
 Method [`getUUID()`](#getUUID()) provides an always unique value for any purpose.
 Method [`createId(String)`](#createId(java.lang.String)) provides an utility method to convert any string value e.g. Magic Draw element
 id; into always unique 33 characters length value.

Since:
Jul 24, 2007

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createId](#createId(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Sometime element id in MagicDraw is not capable in other application e.g.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getUUID](#getUUID())()`
An immutable universally unique identifier (UUID).
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toHex](#toHex(byte%5B%5D))(byte[] data)`
Convert array of bytes into string representation of the unsigned integer in base 16.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
createId
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createId([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Sometime element id in MagicDraw is not capable in other application e.g. id length is too long. This method
 provides an utility to convert any string value into unique 33 characters length value.
Parameters:
`id` - original string value
Returns:
an unique 33 characters long value.
getUUID
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getUUID()
An immutable universally unique identifier (UUID). A UUID represents a 128-bit value.
 For more information including algorithms used to create UUIDs, see the [Internet-Draft UUIDs and GUIDs](http://www.ietf.org/internet-drafts/draft-mealling-uuid-urn-03.txt)
 or the standards body definition at [ISO/IEC 11578:1996.](http://www.iso.ch/cate/d2229.html)
Returns:
128-bit universally unique identifier (UUID)
toHex
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toHex(byte[] data)
Convert array of bytes into string representation of the unsigned integer in base 16.
Parameters:
`data` - array of bytes to be converted to a string.
Returns:
the string in hexadecimal (base 16).

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.helper</a></div>
<h1 class="title" title="Class UUIDGenerator">Class UUIDGenerator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.helper.UUIDGenerator</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">UUIDGenerator</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Create universal unique id.
 <p>
 Magic Draw element id consists of :
 
 <pre>
 <code>
   "_" + ApplicationConstants.VERSION + ApplicationConstants.PATCH_NUMBER + "_" + System.currentTimeMillis() + "_" +
   Math.round(Math.random() * 1000000) + "_" + count++;
 </code>
 </pre>
 
 There is a very less change that element id is not unique.
 <p>
 Method <a href="#getUUID()"><code>getUUID()</code></a> provides an always unique value for any purpose.
 <p>
 Method <a href="#createId(java.lang.String)"><code>createId(String)</code></a> provides an utility method to convert any string value e.g. Magic Draw element
 id; into always unique 33 characters length value.</p></p></p></div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jul 24, 2007</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createId(java.lang.String)">createId</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sometime element id in MagicDraw is not capable in other application e.g.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getUUID()">getUUID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">An immutable universally unique identifier (UUID).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toHex(byte%5B%5D)">toHex</a><wbr/>(byte[] data)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert array of bytes into string representation of the unsigned integer in base 16.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="createId(java.lang.String)">
<h3>createId</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createId</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Sometime element id in MagicDraw is not capable in other application e.g. id length is too long. This method
 provides an utility to convert any string value into unique 33 characters length value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - original string value</dd>
<dt>Returns:</dt>
<dd>an unique 33 characters long value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUUID()">
<h3>getUUID</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUUID</span>()</div>
<div class="block">An immutable universally unique identifier (UUID). A UUID represents a 128-bit value.
 <p>
 For more information including algorithms used to create UUIDs, see the <a href="http://www.ietf.org/internet-drafts/draft-mealling-uuid-urn-03.txt">Internet-Draft UUIDs and GUIDs</a>
 or the standards body definition at <a href="http://www.iso.ch/cate/d2229.html">ISO/IEC 11578:1996.</a></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>128-bit universally unique identifier (UUID)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toHex(byte[])">
<h3>toHex</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toHex</span><wbr/><span class="parameters">(byte[] data)</span></div>
<div class="block">Convert array of bytes into string representation of the unsigned integer in base 16.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>data</code> - array of bytes to be converted to a string.</dd>
<dt>Returns:</dt>
<dd>the string in hexadecimal (base 16).</dd>
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
