# JAVA OPENAPI: TextTool (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/reportwizard/tools/TextTool.html
- source_path: `com/nomagic/reportwizard/tools/TextTool.html`
- source_sha256: `4d8df28649555b8782f178701a86d21eb92030775713fb1466d1f7f17dc671bc`
- captured_utc: `2026-07-14T16:58:40.003312+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools](package-summary.html)

## Class TextTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../../magicreport/engine/Tool.html)
com.nomagic.reportwizard.tools.TextTool

All Implemented Interfaces:
`[ITool](../../magicreport/engine/ITool.html)`, `[IVariable](../../magicreport/IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classTextTool
extends [Tool](../../magicreport/engine/Tool.html)

Contains utilities functions for text renderer. Recommended context name of this class is "text".

Since:
Jun 6, 2008
See Also:
[Serialized Form](../../../../serialized-form.html#com.nomagic.reportwizard.tools.TextTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../../magicreport/engine/ITool.html)
`[ITool.HTMLString](../../magicreport/engine/ITool.HTMLString.html), [ITool.RetainedString](../../magicreport/engine/ITool.RetainedString.html), [ITool.Void](../../magicreport/engine/ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../../magicreport/engine/Tool.html)
`[context](../../magicreport/engine/Tool.html#context), [properties](../../magicreport/engine/Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../../magicreport/engine/ITool.html)
`[VOID](../../magicreport/engine/ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TextTool](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[ITool.HTMLString](../../magicreport/engine/ITool.HTMLString.html)`
`[bold](#bold(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Force report to render given text in bold style.
`boolean`
`[equals](#equals(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str2)`
Compares two strings.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getPureText](#getPureText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)`
Get Pure text from html source.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getString](#getString(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str)`
Convert text from RTF into Java String.
`[ITool.HTMLString](../../magicreport/engine/ITool.HTMLString.html)`
`[html](#html(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Force report to render given text in HTML.
`[ITool.HTMLString](../../magicreport/engine/ITool.HTMLString.html)`
`[italic](#italic(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Force report to render given text in italic style.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[noLineBreak](#noLineBreak(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Remove all control characters such as U+0009 (Tab), U+000A (Line Feed) and U+000D (Carriage Return) from
 given text.
`[Double](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html)`
`[toDouble](#toDouble(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Convert the string argument to signed decimal `double`.
`[Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html)`
`[toInteger](#toInteger(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Convert the string argument to signed decimal `integer`.
`[ITool.HTMLString](../../magicreport/engine/ITool.HTMLString.html)`
`[underline](#underline(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Force report to render given text in underline style.
Methods inherited from class com.nomagic.magicreport.engine.[Tool](../../magicreport/engine/Tool.html)
`[clone](../../magicreport/engine/Tool.html#clone()), [getContext](../../magicreport/engine/Tool.html#getContext()), [getProperties](../../magicreport/engine/Tool.html#getProperties()), [getProperty](../../magicreport/engine/Tool.html#getProperty(java.lang.String)), [getProperty](../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)), [notifyObservers](../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)), [setContext](../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)), [setProperties](../../magicreport/engine/Tool.html#setProperties(java.util.Properties))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](../../magicreport/engine/ITool.html)
`[clearTool](../../magicreport/engine/ITool.html#clearTool())`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TextTool
public TextTool()
 ============ METHOD DETAIL ========== 
Method Details
noLineBreak
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) noLineBreak([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Remove all control characters such as U+0009 (Tab), U+000A (Line Feed) and U+000D (Carriage Return) from
 given text. This method will performs text filtering under category "Cc" in the Unicode specification.
Parameters:
`text` - input text
Returns:
new text
toInteger
public [Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html) toInteger([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Convert the string argument to signed decimal `integer`.
Parameters:
`text` - a `String` containing the `int` representation to be converted
Returns:
the integer value represented by the argument in decimal
toDouble
public [Double](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html) toDouble([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Convert the string argument to signed decimal `double`.
Parameters:
`text` - a `String` containing the `int` representation to be converted
Returns:
the integer value represented by the argument in decimal
italic
public [ITool.HTMLString](../../magicreport/engine/ITool.HTMLString.html) italic([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Force report to render given text in italic style.
Parameters:
`text` - input text
Returns:
HTML text in italic style.
bold
public [ITool.HTMLString](../../magicreport/engine/ITool.HTMLString.html) bold([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Force report to render given text in bold style.
Parameters:
`text` - input text
Returns:
HTML text in bold style.
underline
public [ITool.HTMLString](../../magicreport/engine/ITool.HTMLString.html) underline([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Force report to render given text in underline style.
Parameters:
`text` - input text
Returns:
HTML text in underline style.
html
public [ITool.HTMLString](../../magicreport/engine/ITool.HTMLString.html) html([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Force report to render given text in HTML.
 For example: `$text.html('<ul><li>A</li><li>B</li></ul>')`
Parameters:
`text` - input text
Returns:
HTML text.
equals
public boolean equals([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str2)
Compares two strings. The result is `true` if and only if the `str1` is represents the
 same sequence of characters as `str2`.
Parameters:
`str1` - first string
`str2` - second string
Returns:
`true` if the `String`are equal; `false` otherwise.
getString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getString([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str)
Convert text from RTF into Java String.
 For example: `#set ($str = $text.getString("bersetzer"))`
Parameters:
`str` - a RTF text.
Returns:
a Java String
getPureText
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getPureText([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)
Get Pure text from html source.
Parameters:
`source` - The given html source.
Returns:
pure text from html source.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools</a></div>
<h1 class="title" title="Class TextTool">Class TextTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance">com.nomagic.reportwizard.tools.TextTool</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../magicreport/IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TextTool</span>
<span class="extends-implements">extends <a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></span></div>
<div class="block">Contains utilities functions for text renderer. Recommended context name of this class is "text".</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 6, 2008</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../serialized-form.html#com.nomagic.reportwizard.tools.TextTool">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="../../magicreport/engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.<a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../magicreport/engine/Tool.html#context">context</a>, <a href="../../magicreport/engine/Tool.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../magicreport/engine/ITool.html#VOID">VOID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TextTool</a>()</code></div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#bold(java.lang.String)">bold</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Force report to render given text in bold style.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.String,java.lang.String)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Compares two strings.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPureText(java.lang.String)">getPureText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Pure text from html source.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getString(java.lang.String)">getString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert text from RTF into Java String.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#html(java.lang.String)">html</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Force report to render given text in HTML.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#italic(java.lang.String)">italic</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Force report to render given text in italic style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#noLineBreak(java.lang.String)">noLineBreak</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove all control characters such as U+0009 (Tab), U+000A (Line Feed) and U+000D (Carriage Return) from
 given text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toDouble(java.lang.String)">toDouble</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert the string argument to signed decimal <code>double</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toInteger(java.lang.String)">toInteger</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert the string argument to signed decimal <code>integer</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#underline(java.lang.String)">underline</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Force report to render given text in underline style.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../magicreport/engine/Tool.html#clone()">clone</a>, <a href="../../magicreport/engine/Tool.html#getContext()">getContext</a>, <a href="../../magicreport/engine/Tool.html#getProperties()">getProperties</a>, <a href="../../magicreport/engine/Tool.html#getProperty(java.lang.String)">getProperty</a>, <a href="../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)">getProperty</a>, <a href="../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../../magicreport/engine/Tool.html#setProperties(java.util.Properties)">setProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../magicreport/engine/ITool.html#clearTool()">clearTool</a></code></div>
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
<h3>TextTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TextTool</span>()</div>
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
<section class="detail" id="noLineBreak(java.lang.String)">
<h3>noLineBreak</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">noLineBreak</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Remove all control characters such as U+0009 (Tab), U+000A (Line Feed) and U+000D (Carriage Return) from
 given text. This method will performs text filtering under category "Cc" in the Unicode specification.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - input text</dd>
<dt>Returns:</dt>
<dd>new text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toInteger(java.lang.String)">
<h3>toInteger</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">toInteger</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Convert the string argument to signed decimal <code>integer</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - a <code>String</code> containing the <code>int</code> representation to be converted</dd>
<dt>Returns:</dt>
<dd>the integer value represented by the argument in decimal</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toDouble(java.lang.String)">
<h3>toDouble</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">toDouble</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Convert the string argument to signed decimal <code>double</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - a <code>String</code> containing the <code>int</code> representation to be converted</dd>
<dt>Returns:</dt>
<dd>the integer value represented by the argument in decimal</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="italic(java.lang.String)">
<h3>italic</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></span> <span class="element-name">italic</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Force report to render given text in italic style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - input text</dd>
<dt>Returns:</dt>
<dd>HTML text in italic style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="bold(java.lang.String)">
<h3>bold</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></span> <span class="element-name">bold</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Force report to render given text in bold style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - input text</dd>
<dt>Returns:</dt>
<dd>HTML text in bold style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="underline(java.lang.String)">
<h3>underline</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></span> <span class="element-name">underline</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Force report to render given text in underline style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - input text</dd>
<dt>Returns:</dt>
<dd>HTML text in underline style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="html(java.lang.String)">
<h3>html</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></span> <span class="element-name">html</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Force report to render given text in HTML.
 <p>
 For example: <code><pre>
    $text.html('&lt;ul&gt;&lt;li&gt;A&lt;/li&gt;&lt;li&gt;B&lt;/li&gt;&lt;/ul&gt;')
 </pre></code>
</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - input text</dd>
<dt>Returns:</dt>
<dd>HTML text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.String,java.lang.String)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str2)</span></div>
<div class="block">Compares two strings. The result is <code>true</code> if and only if the <code>str1</code> is represents the
 same sequence of characters as <code>str2</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>str1</code> - first string</dd>
<dd><code>str2</code> - second string</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the <code>String </code>are equal; <code>false</code> otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getString(java.lang.String)">
<h3>getString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str)</span></div>
<div class="block">Convert text from RTF into Java String.
 <p>
 For example: <code><pre>
        #set ($str = $text.getString("bersetzer"))
 </pre></code>
</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>str</code> - a RTF text.</dd>
<dt>Returns:</dt>
<dd>a Java String</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPureText(java.lang.String)">
<h3>getPureText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPureText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</span></div>
<div class="block">Get Pure text from html source.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - The given html source.</dd>
<dt>Returns:</dt>
<dd>pure text from html source.</dd>
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
