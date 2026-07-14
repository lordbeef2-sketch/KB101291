# JAVA OPENAPI: HtmlTextUtils (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/text/html/HtmlTextUtils.html
- source_path: `com/nomagic/text/html/HtmlTextUtils.html`
- source_sha256: `824202c43ed1a0ebf0e56dd4b6b9a2e4ad47eeaa4ba35f15f1db33297f9eddf7`
- captured_utc: `2026-07-14T16:58:41.421328+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.text.html](package-summary.html)

## Class HtmlTextUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.text.html.HtmlTextUtils

@OpenApiAllpublic classHtmlTextUtils
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
HTML text related utility methods.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[HtmlTextUtils](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[encodeHtmlCharacters](#encodeHtmlCharacters(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Encodes string characters to html characters.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[endTag](#endTag(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag)`
Create end tag for the given tag.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[escapeLongSpaces](#escapeLongSpaces(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Replaces sequece of 2 or more spaces with same amount of not breaking spaces.
`static boolean`
`[isDocTypeHtml](#isDocTypeHtml(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`

`static boolean`
`[isHtml](#isHtml(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Checks if given string is html string - starts with <html> tag
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[removeHtmlBodyPTags](#removeHtmlBodyPTags(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) htmlText)`
Extracts body from the given html text.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[removeHtmlBodyTags](#removeHtmlBodyTags(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) htmlText)`
Extracts body from the given html text
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[replaceNBSP](#replaceNBSP(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`

`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[startTag](#startTag(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag)`
Create start tag for the given tag.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toHtmlText](#toHtmlText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Convert given text to html text.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toPlainText](#toPlainText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) htmlText)`
Converts html text to plain text.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toPlainText](#toPlainText(javax.swing.text.Document))([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Document.html) doc)`
Converts document to plain text
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[wrapInHtmlBodyNewLineTags](#wrapInHtmlBodyNewLineTags(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Wrap given text in <html><body>new_line tags
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[wrapInHtmlBodyPTags](#wrapInHtmlBodyPTags(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Wrap given text in <html><body><p> tags
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[wrapInHtmlBodyTags](#wrapInHtmlBodyTags(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Wrap given text in <html><body> tags
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[wrapInHtmlLightBodyPTags](#wrapInHtmlLightBodyPTags(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Wrap given text in <html light="true"><body><p> tags
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[wrapInHtmlLightBodyTags](#wrapInHtmlLightBodyTags(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Wrap given text in <html light="true"><body> tags
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[wrapInHtmlTag](#wrapInHtmlTag(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Wrap given text with <html> tag
`static [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[wrapInHtmlTag](#wrapInHtmlTag(java.lang.StringBuilder))([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) text)`
Wrap given text with <html> tag
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
HtmlTextUtils
public HtmlTextUtils()
 ============ METHOD DETAIL ========== 
Method Details
isHtml
public static boolean isHtml(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Checks if given string is html string - starts with <html> tag
Parameters:
`text` - text
isDocTypeHtml
public static boolean isDocTypeHtml([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
removeHtmlBodyPTags
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) removeHtmlBodyPTags([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) htmlText)
Extracts body from the given html text. If body is wrapped with P tags, removes them as well.
Parameters:
`htmlText` - html text
Returns:
body text
removeHtmlBodyTags
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) removeHtmlBodyTags([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) htmlText)
Extracts body from the given html text
Parameters:
`htmlText` - html text
Returns:
body text
wrapInHtmlTag
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) wrapInHtmlTag([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Wrap given text with <html> tag
Parameters:
`text` - text
Returns:
wrapped text
wrapInHtmlTag
public static [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) wrapInHtmlTag([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) text)
Wrap given text with <html> tag
Parameters:
`text` - text
Returns:
wrapped text
wrapInHtmlBodyPTags
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) wrapInHtmlBodyPTags([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Wrap given text in <html><body><p> tags
Parameters:
`text` - text
Returns:
wrapped text
wrapInHtmlBodyNewLineTags
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) wrapInHtmlBodyNewLineTags([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Wrap given text in <html><body>new_line tags
Parameters:
`text` - text
Returns:
wrapped text
wrapInHtmlBodyTags
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) wrapInHtmlBodyTags([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Wrap given text in <html><body> tags
Parameters:
`text` - text
Returns:
wrapped text
wrapInHtmlLightBodyTags
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) wrapInHtmlLightBodyTags([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Wrap given text in <html light="true"><body> tags
Parameters:
`text` - text
Returns:
wrapped text
wrapInHtmlLightBodyPTags
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) wrapInHtmlLightBodyPTags([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Wrap given text in <html light="true"><body><p> tags
Parameters:
`text` - text
Returns:
wrapped text
startTag
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) startTag([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag)
Create start tag for the given tag.
Parameters:
`tag` - The given tag.
Returns:
tag wrapped to <tag>
endTag
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) endTag([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag)
Create end tag for the given tag.
Parameters:
`tag` - The given tag.
Returns:
tag wrapped to </tag>
toHtmlText
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toHtmlText([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Convert given text to html text. Characters are converter to html characters.
 Does nothing if text is html text already.
Parameters:
`text` - the given text
Returns:
the html text
encodeHtmlCharacters
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) encodeHtmlCharacters([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Encodes string characters to html characters. For example convert space to nbps;, < to < and etc.
Parameters:
`text` - plain text
Returns:
string with encoded characters
toPlainText
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toPlainText([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) htmlText)
Converts html text to plain text.
 Important - pass html text, not a plain text!
Parameters:
`htmlText` - html text
Returns:
plain text
toPlainText
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toPlainText([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Document.html) doc)
Converts document to plain text
Returns:
the plain text
escapeLongSpaces
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) escapeLongSpaces([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Replaces sequece of 2 or more spaces with same amount of not breaking spaces.
 Required for HTML text, which shrinks multiple spaces into single
replaceNBSP
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) replaceNBSP([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.text.html</a></div>
<h1 class="title" title="Class HtmlTextUtils">Class HtmlTextUtils</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.text.html.HtmlTextUtils</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">HtmlTextUtils</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">HTML text related utility methods.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">HtmlTextUtils</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#encodeHtmlCharacters(java.lang.String)">encodeHtmlCharacters</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Encodes string characters to html characters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#endTag(java.lang.String)">endTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create end tag for the given tag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#escapeLongSpaces(java.lang.String)">escapeLongSpaces</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replaces sequece of 2 or more spaces with same amount of not breaking spaces.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDocTypeHtml(java.lang.String)">isDocTypeHtml</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isHtml(java.lang.String)">isHtml</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given string is html string - starts with &lt;html&gt; tag</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeHtmlBodyPTags(java.lang.String)">removeHtmlBodyPTags</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> htmlText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Extracts body from the given html text.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeHtmlBodyTags(java.lang.String)">removeHtmlBodyTags</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> htmlText)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Extracts body from the given html text</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replaceNBSP(java.lang.String)">replaceNBSP</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#startTag(java.lang.String)">startTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create start tag for the given tag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toHtmlText(java.lang.String)">toHtmlText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert given text to html text.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toPlainText(java.lang.String)">toPlainText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> htmlText)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts html text to plain text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toPlainText(javax.swing.text.Document)">toPlainText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Document.html" title="class or interface in javax.swing.text">Document</a> doc)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts document to plain text</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#wrapInHtmlBodyNewLineTags(java.lang.String)">wrapInHtmlBodyNewLineTags</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Wrap given text in &lt;html&gt;&lt;body&gt;new_line tags</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#wrapInHtmlBodyPTags(java.lang.String)">wrapInHtmlBodyPTags</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Wrap given text in &lt;html&gt;&lt;body&gt;&lt;p&gt; tags</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#wrapInHtmlBodyTags(java.lang.String)">wrapInHtmlBodyTags</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Wrap given text in &lt;html&gt;&lt;body&gt; tags</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#wrapInHtmlLightBodyPTags(java.lang.String)">wrapInHtmlLightBodyPTags</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Wrap given text in &lt;html light="true"&gt;&lt;body&gt;&lt;p&gt; tags</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#wrapInHtmlLightBodyTags(java.lang.String)">wrapInHtmlLightBodyTags</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Wrap given text in &lt;html light="true"&gt;&lt;body&gt; tags</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#wrapInHtmlTag(java.lang.String)">wrapInHtmlTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Wrap given text with &lt;html&gt; tag</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#wrapInHtmlTag(java.lang.StringBuilder)">wrapInHtmlTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Wrap given text with &lt;html&gt; tag</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>HtmlTextUtils</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HtmlTextUtils</span>()</div>
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
<section class="detail" id="isHtml(java.lang.String)">
<h3>isHtml</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isHtml</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Checks if given string is html string - starts with &lt;html&gt; tag</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDocTypeHtml(java.lang.String)">
<h3>isDocTypeHtml</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDocTypeHtml</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeHtmlBodyPTags(java.lang.String)">
<h3>removeHtmlBodyPTags</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">removeHtmlBodyPTags</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> htmlText)</span></div>
<div class="block">Extracts body from the given html text. If body is wrapped with P tags, removes them as well.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>htmlText</code> - html text</dd>
<dt>Returns:</dt>
<dd>body text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeHtmlBodyTags(java.lang.String)">
<h3>removeHtmlBodyTags</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">removeHtmlBodyTags</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> htmlText)</span></div>
<div class="block">Extracts body from the given html text</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>htmlText</code> - html text</dd>
<dt>Returns:</dt>
<dd>body text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wrapInHtmlTag(java.lang.String)">
<h3>wrapInHtmlTag</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">wrapInHtmlTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Wrap given text with &lt;html&gt; tag</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text</dd>
<dt>Returns:</dt>
<dd>wrapped text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wrapInHtmlTag(java.lang.StringBuilder)">
<h3>wrapInHtmlTag</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">wrapInHtmlTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> text)</span></div>
<div class="block">Wrap given text with &lt;html&gt; tag</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text</dd>
<dt>Returns:</dt>
<dd>wrapped text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wrapInHtmlBodyPTags(java.lang.String)">
<h3>wrapInHtmlBodyPTags</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">wrapInHtmlBodyPTags</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Wrap given text in &lt;html&gt;&lt;body&gt;&lt;p&gt; tags</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text</dd>
<dt>Returns:</dt>
<dd>wrapped text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wrapInHtmlBodyNewLineTags(java.lang.String)">
<h3>wrapInHtmlBodyNewLineTags</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">wrapInHtmlBodyNewLineTags</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Wrap given text in &lt;html&gt;&lt;body&gt;new_line tags</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text</dd>
<dt>Returns:</dt>
<dd>wrapped text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wrapInHtmlBodyTags(java.lang.String)">
<h3>wrapInHtmlBodyTags</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">wrapInHtmlBodyTags</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Wrap given text in &lt;html&gt;&lt;body&gt; tags</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text</dd>
<dt>Returns:</dt>
<dd>wrapped text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wrapInHtmlLightBodyTags(java.lang.String)">
<h3>wrapInHtmlLightBodyTags</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">wrapInHtmlLightBodyTags</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Wrap given text in &lt;html light="true"&gt;&lt;body&gt; tags</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text</dd>
<dt>Returns:</dt>
<dd>wrapped text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wrapInHtmlLightBodyPTags(java.lang.String)">
<h3>wrapInHtmlLightBodyPTags</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">wrapInHtmlLightBodyPTags</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Wrap given text in &lt;html light="true"&gt;&lt;body&gt;&lt;p&gt; tags</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text</dd>
<dt>Returns:</dt>
<dd>wrapped text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="startTag(java.lang.String)">
<h3>startTag</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">startTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag)</span></div>
<div class="block">Create start tag for the given tag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - The given tag.</dd>
<dt>Returns:</dt>
<dd>tag wrapped to &lt;tag&gt;</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="endTag(java.lang.String)">
<h3>endTag</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">endTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag)</span></div>
<div class="block">Create end tag for the given tag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - The given tag.</dd>
<dt>Returns:</dt>
<dd>tag wrapped to &lt;/tag&gt;</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toHtmlText(java.lang.String)">
<h3>toHtmlText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toHtmlText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Convert given text to html text. Characters are converter to html characters.
 Does nothing if text is html text already.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - the given text</dd>
<dt>Returns:</dt>
<dd>the html text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="encodeHtmlCharacters(java.lang.String)">
<h3>encodeHtmlCharacters</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">encodeHtmlCharacters</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Encodes string characters to html characters. For example convert space to nbps;, &lt; to &amp;lt; and etc.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - plain text</dd>
<dt>Returns:</dt>
<dd>string with encoded characters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toPlainText(java.lang.String)">
<h3>toPlainText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toPlainText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> htmlText)</span></div>
<div class="block">Converts html text to plain text.
 Important - pass html text, not a plain text!</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>htmlText</code> - html text</dd>
<dt>Returns:</dt>
<dd>plain text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toPlainText(javax.swing.text.Document)">
<h3>toPlainText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toPlainText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Document.html" title="class or interface in javax.swing.text">Document</a> doc)</span></div>
<div class="block">Converts document to plain text</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the plain text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="escapeLongSpaces(java.lang.String)">
<h3>escapeLongSpaces</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">escapeLongSpaces</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Replaces sequece of 2 or more spaces with same amount of not breaking spaces.
 Required for HTML text, which shrinks multiple spaces into single</div>
</section>
</li>
<li>
<section class="detail" id="replaceNBSP(java.lang.String)">
<h3>replaceNBSP</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">replaceNBSP</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
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
