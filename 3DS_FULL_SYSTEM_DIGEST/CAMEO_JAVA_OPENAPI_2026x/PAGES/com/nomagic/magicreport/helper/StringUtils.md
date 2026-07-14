# JAVA OPENAPI: StringUtils (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/helper/StringUtils.html
- source_path: `com/nomagic/magicreport/helper/StringUtils.html`
- source_sha256: `480ae863814a9bb714dc41b18995c5efa179686bdfb7f3744464addce39b77d4`
- captured_utc: `2026-07-14T16:58:39.398311+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.helper](package-summary.html)

## Class StringUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.helper.StringUtils

@OpenApiAllpublic final classStringUtils
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Contains collection of String utilities.

Since:
Jun 15, 2007

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[LINE_SEPARATOR](#LINE_SEPARATOR)`
A line separator string.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[leftTrim](#leftTrim(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input)`
Returns a copy of the string, with leading whitespace omitted.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[lPad](#lPad(java.lang.CharSequence,char,int))([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) src,
 char pad,
 int length)`
Padding a character to left of string.
`static [StringBuffer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html)`
`[replace](#replace(java.lang.CharSequence,java.lang.String,java.lang.String))([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) target,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) replacement)`
Replaces each substring of this string that matches the literal target sequence with the specified literal
 replacement sequence.
`static [StringBuffer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html)`
`[replaceAll](#replaceAll(java.lang.CharSequence,java.lang.String,java.lang.String))([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) regex,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) replacement)`
Replaces each substring of this subsequence that matches the given regular expression with the given
 replacement.
`static [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[replaceAllBuilder](#replaceAllBuilder(java.lang.CharSequence,java.lang.String,java.lang.String))([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) regex,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) replacement)`
Replaces each substring of this subsequence that matches the given regular expression with the given
 replacement.
`static [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[replaceBuilder](#replaceBuilder(java.lang.CharSequence,java.lang.String,java.lang.String))([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) target,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) replacement)`
Replaces each substring of this string that matches the literal target sequence with the specified literal
 replacement sequence.
`static [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[rightTrim](#rightTrim(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input)`
Returns a copy of the string, with trailing whitespace omitted.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[rPad](#rPad(java.lang.CharSequence,char,int))([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) src,
 char pad,
 int length)`
Padding a character to right of string.
`static [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[trim](#trim(java.lang.CharSequence))([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input)`
Returns a copy of the string, with leading whitespace and trailing whitespace are omitted.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
LINE_SEPARATOR
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) LINE_SEPARATOR
A line separator string. The line separator string is defined by the system property
 `line.separator`, and is not necessarily a single newline ('\n') character.
 ============ METHOD DETAIL ========== 
Method Details
replaceAll
public static [StringBuffer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html) replaceAll([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) regex,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) replacement)
Replaces each substring of this subsequence that matches the given regular expression with the given
 replacement.
Parameters:
`input` - The character sequence to be matched
`regex` - the regular expression to which this string is to be matched
`replacement` - The replacement string
Returns:
The StringBuffer constructed by replacing each matching subsequence by the replacement string,
 substituting captured subsequences as needed
replaceAllBuilder
public static [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) replaceAllBuilder([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) regex,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) replacement)
Replaces each substring of this subsequence that matches the given regular expression with the given
 replacement.
Parameters:
`input` - The character sequence to be matched
`regex` - the regular expression to which this string is to be matched
`replacement` - The replacement string
Returns:
The StringBuilder constructed by replacing each matching subsequence by the replacement string,
 substituting captured subsequences as needed
replace
public static [StringBuffer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html) replace([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) target,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) replacement)
Replaces each substring of this string that matches the literal target sequence with the specified literal
 replacement sequence. The replacement proceeds from the beginning of the string to the end.
Parameters:
`input` - The character sequence to be matched
`target` - The sequence of char values to be replaced
`replacement` - The replacement string
Returns:
The StringBuffer constructed by replacing each matching subsequence by the replacement string,
 substituting captured subsequences as needed
replaceBuilder
public static [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) replaceBuilder([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) target,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) replacement)
Replaces each substring of this string that matches the literal target sequence with the specified literal
 replacement sequence. The replacement proceeds from the beginning of the string to the end.
Parameters:
`input` - The character sequence to be matched
`target` - The sequence of char values to be replaced
`replacement` - The replacement string
Returns:
The StringBuilder constructed by replacing each matching subsequence by the replacement string,
 substituting captured subsequences as needed
leftTrim
public static [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) leftTrim([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input)
Returns a copy of the string, with leading whitespace omitted. This method may be used to trim whitespace
 from the beginning of a string.
Parameters:
`input` - string to be trim.
Returns:
A copy of this string with leading white space removed, or this string if it has no leading white
 space
rightTrim
public static [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) rightTrim([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input)
Returns a copy of the string, with trailing whitespace omitted. This method may be used to trim whitespace
 from the end of a string.
Parameters:
`input` - string to be trim.
Returns:
A copy of this string with trailing white space removed, or this string if it has no trailing white
 space
trim
public static [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) trim([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) input)
Returns a copy of the string, with leading whitespace and trailing whitespace are omitted.
Parameters:
`input` - string to be trim.
Returns:
A copy of this string with leading whitespace trailing white space removed, or this string if it has
 no leading whitespace and trailing white space
lPad
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) lPad([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) src,
 char pad,
 int length)
Padding a character to left of string.
Parameters:
`src` - String to padding
`pad` - Pad character
`length` - Final length of string
Returns:
new string
rPad
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) rPad([CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) src,
 char pad,
 int length)
Padding a character to right of string.
Parameters:
`src` - String to padding
`pad` - Pad character
`length` - Final length of string
Returns:
new string

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.helper</a></div>
<h1 class="title" title="Class StringUtils">Class StringUtils</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.helper.StringUtils</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">StringUtils</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Contains collection of String utilities.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 15, 2007</dd>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LINE_SEPARATOR">LINE_SEPARATOR</a></code></div>
<div class="col-last even-row-color">
<div class="block">A line separator string.</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#leftTrim(java.lang.CharSequence)">leftTrim</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a copy of the string, with leading whitespace omitted.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lPad(java.lang.CharSequence,char,int)">lPad</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> src,
 char pad,
 int length)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Padding a character to left of string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replace(java.lang.CharSequence,java.lang.String,java.lang.String)">replace</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> replacement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replaces each substring of this string that matches the literal target sequence with the specified literal
 replacement sequence.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replaceAll(java.lang.CharSequence,java.lang.String,java.lang.String)">replaceAll</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> regex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> replacement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replaces each substring of this subsequence that matches the given regular expression with the given
 replacement.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replaceAllBuilder(java.lang.CharSequence,java.lang.String,java.lang.String)">replaceAllBuilder</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> regex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> replacement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replaces each substring of this subsequence that matches the given regular expression with the given
 replacement.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replaceBuilder(java.lang.CharSequence,java.lang.String,java.lang.String)">replaceBuilder</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> replacement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replaces each substring of this string that matches the literal target sequence with the specified literal
 replacement sequence.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#rightTrim(java.lang.CharSequence)">rightTrim</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a copy of the string, with trailing whitespace omitted.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#rPad(java.lang.CharSequence,char,int)">rPad</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> src,
 char pad,
 int length)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Padding a character to right of string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#trim(java.lang.CharSequence)">trim</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a copy of the string, with leading whitespace and trailing whitespace are omitted.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="LINE_SEPARATOR">
<h3>LINE_SEPARATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LINE_SEPARATOR</span></div>
<div class="block">A line separator string. The line separator string is defined by the system property
 <code>line.separator</code>, and is not necessarily a single newline ('\n') character.</div>
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
<section class="detail" id="replaceAll(java.lang.CharSequence,java.lang.String,java.lang.String)">
<h3>replaceAll</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a></span> <span class="element-name">replaceAll</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> regex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> replacement)</span></div>
<div class="block">Replaces each substring of this subsequence that matches the given regular expression with the given
 replacement.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - The character sequence to be matched</dd>
<dd><code>regex</code> - the regular expression to which this string is to be matched</dd>
<dd><code>replacement</code> - The replacement string</dd>
<dt>Returns:</dt>
<dd>The StringBuffer constructed by replacing each matching subsequence by the replacement string,
         substituting captured subsequences as needed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="replaceAllBuilder(java.lang.CharSequence,java.lang.String,java.lang.String)">
<h3>replaceAllBuilder</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">replaceAllBuilder</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> regex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> replacement)</span></div>
<div class="block">Replaces each substring of this subsequence that matches the given regular expression with the given
 replacement.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - The character sequence to be matched</dd>
<dd><code>regex</code> - the regular expression to which this string is to be matched</dd>
<dd><code>replacement</code> - The replacement string</dd>
<dt>Returns:</dt>
<dd>The StringBuilder constructed by replacing each matching subsequence by the replacement string,
         substituting captured subsequences as needed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="replace(java.lang.CharSequence,java.lang.String,java.lang.String)">
<h3>replace</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a></span> <span class="element-name">replace</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> replacement)</span></div>
<div class="block">Replaces each substring of this string that matches the literal target sequence with the specified literal
 replacement sequence. The replacement proceeds from the beginning of the string to the end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - The character sequence to be matched</dd>
<dd><code>target</code> - The sequence of char values to be replaced</dd>
<dd><code>replacement</code> - The replacement string</dd>
<dt>Returns:</dt>
<dd>The StringBuffer constructed by replacing each matching subsequence by the replacement string,
         substituting captured subsequences as needed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="replaceBuilder(java.lang.CharSequence,java.lang.String,java.lang.String)">
<h3>replaceBuilder</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">replaceBuilder</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> replacement)</span></div>
<div class="block">Replaces each substring of this string that matches the literal target sequence with the specified literal
 replacement sequence. The replacement proceeds from the beginning of the string to the end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - The character sequence to be matched</dd>
<dd><code>target</code> - The sequence of char values to be replaced</dd>
<dd><code>replacement</code> - The replacement string</dd>
<dt>Returns:</dt>
<dd>The StringBuilder constructed by replacing each matching subsequence by the replacement string,
         substituting captured subsequences as needed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="leftTrim(java.lang.CharSequence)">
<h3>leftTrim</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">leftTrim</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input)</span></div>
<div class="block">Returns a copy of the string, with leading whitespace omitted. This method may be used to trim whitespace
 from the beginning of a string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - string to be trim.</dd>
<dt>Returns:</dt>
<dd>A copy of this string with leading white space removed, or this string if it has no leading white
         space</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="rightTrim(java.lang.CharSequence)">
<h3>rightTrim</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">rightTrim</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input)</span></div>
<div class="block">Returns a copy of the string, with trailing whitespace omitted. This method may be used to trim whitespace
 from the end of a string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - string to be trim.</dd>
<dt>Returns:</dt>
<dd>A copy of this string with trailing white space removed, or this string if it has no trailing white
         space</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="trim(java.lang.CharSequence)">
<h3>trim</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">trim</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> input)</span></div>
<div class="block">Returns a copy of the string, with leading whitespace and trailing whitespace are omitted.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - string to be trim.</dd>
<dt>Returns:</dt>
<dd>A copy of this string with leading whitespace trailing white space removed, or this string if it has
         no leading whitespace and trailing white space</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lPad(java.lang.CharSequence,char,int)">
<h3>lPad</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">lPad</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> src,
 char pad,
 int length)</span></div>
<div class="block">Padding a character to left of string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>src</code> - String to padding</dd>
<dd><code>pad</code> - Pad character</dd>
<dd><code>length</code> - Final length of string</dd>
<dt>Returns:</dt>
<dd>new string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="rPad(java.lang.CharSequence,char,int)">
<h3>rPad</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">rPad</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a> src,
 char pad,
 int length)</span></div>
<div class="block">Padding a character to right of string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>src</code> - String to padding</dd>
<dd><code>pad</code> - Pad character</dd>
<dd><code>length</code> - Final length of string</dd>
<dt>Returns:</dt>
<dd>new string</dd>
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
