# JAVA OPENAPI: Names (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Names.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Names.html`
- source_sha256: `86d2bc493fc7744154e8653f006e6caeeb7b8a153aa72b0c76ae72ba2f1e4fdc`
- captured_utc: `2026-07-14T16:44:47.899841+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Names

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Names

@OpenApiAllpublic classNames
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Element`](kerml/Element.html) names.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Names](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[escapeName](#escapeName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Escapes a name according to the KerML specification.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[escapeString](#escapeString(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string)`
Escapes special characters in a string according to KerML rules.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDeclaredNameOrEmpty](#getDeclaredNameOrEmpty(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns the declared name of the element, or an empty string if none exists.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDeclaredShortNameOrEmpty](#getDeclaredShortNameOrEmpty(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns the declared short name of the element, or an empty string if none exists.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getNameOrEmpty](#getNameOrEmpty(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns the name of the element, or an empty string if none exists.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getNameOrProvided](#getNameOrProvided(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.String))([Element](kerml/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) provided)`
Returns the element's name, or the provided fallback if the name is empty.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getQualifiedNameOrEmpty](#getQualifiedNameOrEmpty(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns the fully qualified name of the element, or an empty string
 if it has no owning namespace.
`static boolean`
`[isDeclaredNameApplicable](#isDeclaredNameApplicable(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Checks whether the element's declared name is applicable.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[unescapeString](#unescapeString(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string)`
Converts a string literal or unrestricted name with escaped characters
 into a string in which the escape sequences are replaced with the corresponding
 represented characters.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Names
public Names()
 ============ METHOD DETAIL ========== 
Method Details
escapeName
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) escapeName(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Escapes a name according to the KerML specification.
 If the name is null, empty, or already a valid identifier,
 it is returned unchanged. Otherwise, it is wrapped in quotes
 and escape sequences are applied.
Parameters:
`name` - the name to escape
Returns:
escaped name, or null if input is null
getDeclaredShortNameOrEmpty
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDeclaredShortNameOrEmpty([Element](kerml/Element.html) element)
Returns the declared short name of the element, or an empty string if none exists.
Parameters:
`element` - the element to inspect
Returns:
declared short name or empty string
getNameOrEmpty
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getNameOrEmpty([Element](kerml/Element.html) element)
Returns the name of the element, or an empty string if none exists.
Parameters:
`element` - the element to inspect
Returns:
name or empty string
getQualifiedNameOrEmpty
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getQualifiedNameOrEmpty([Element](kerml/Element.html) element)
Returns the fully qualified name of the element, or an empty string
 if it has no owning namespace.
Parameters:
`element` - the element to inspect
Returns:
qualified name or empty string
getNameOrProvided
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getNameOrProvided([Element](kerml/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) provided)
Returns the element's name, or the provided fallback if the name is empty.
Parameters:
`element` - the element to inspect
`provided` - fallback name
Returns:
name or fallback
isDeclaredNameApplicable
public static boolean isDeclaredNameApplicable([Element](kerml/Element.html) element)
Checks whether the element's declared name is applicable.
 Declared names are not applicable for root namespaces or
 non-member relationships.
Parameters:
`element` - the element to inspect
Returns:
true if declared name is applicable
getDeclaredNameOrEmpty
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDeclaredNameOrEmpty([Element](kerml/Element.html) element)
Returns the declared name of the element, or an empty string if none exists.
Parameters:
`element` - the element to inspect
Returns:
declared name or empty string
escapeString
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) escapeString([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string)
Escapes special characters in a string according to KerML rules.
Parameters:
`string` - the string to escape
Returns:
escaped string
unescapeString
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) unescapeString(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string)
Converts a string literal or unrestricted name with escaped characters
 into a string in which the escape sequences are replaced with the corresponding
 represented characters. If the input string starts with a single or double quote
 character, it is assumed to be a lexically valid unrestricted name or string literal,
 respectively. Otherwise, the input string is returned without change.
Parameters:
`string` - the string to unescape
Returns:
unescaped string, or null if input is null

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Names">Class Names</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Names</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Names</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a> names.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Names</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#escapeName(java.lang.String)">escapeName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Escapes a name according to the KerML specification.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#escapeString(java.lang.String)">escapeString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Escapes special characters in a string according to KerML rules.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDeclaredNameOrEmpty(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getDeclaredNameOrEmpty</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the declared name of the element, or an empty string if none exists.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDeclaredShortNameOrEmpty(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getDeclaredShortNameOrEmpty</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the declared short name of the element, or an empty string if none exists.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNameOrEmpty(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getNameOrEmpty</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the name of the element, or an empty string if none exists.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNameOrProvided(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.String)">getNameOrProvided</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> provided)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the element's name, or the provided fallback if the name is empty.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getQualifiedNameOrEmpty(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getQualifiedNameOrEmpty</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the fully qualified name of the element, or an empty string
 if it has no owning namespace.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDeclaredNameApplicable(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isDeclaredNameApplicable</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element's declared name is applicable.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unescapeString(java.lang.String)">unescapeString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts a string literal or unrestricted name with escaped characters
 into a string in which the escape sequences are replaced with the corresponding
 represented characters.</div>
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
<h3>Names</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Names</span>()</div>
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
<section class="detail" id="escapeName(java.lang.String)">
<h3>escapeName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">escapeName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Escapes a name according to the KerML specification.
 If the name is null, empty, or already a valid identifier,
 it is returned unchanged. Otherwise, it is wrapped in quotes
 and escape sequences are applied.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name to escape</dd>
<dt>Returns:</dt>
<dd>escaped name, or null if input is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeclaredShortNameOrEmpty(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getDeclaredShortNameOrEmpty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDeclaredShortNameOrEmpty</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns the declared short name of the element, or an empty string if none exists.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to inspect</dd>
<dt>Returns:</dt>
<dd>declared short name or empty string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNameOrEmpty(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getNameOrEmpty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getNameOrEmpty</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns the name of the element, or an empty string if none exists.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to inspect</dd>
<dt>Returns:</dt>
<dd>name or empty string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQualifiedNameOrEmpty(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getQualifiedNameOrEmpty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQualifiedNameOrEmpty</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns the fully qualified name of the element, or an empty string
 if it has no owning namespace.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to inspect</dd>
<dt>Returns:</dt>
<dd>qualified name or empty string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNameOrProvided(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.String)">
<h3>getNameOrProvided</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getNameOrProvided</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> provided)</span></div>
<div class="block">Returns the element's name, or the provided fallback if the name is empty.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to inspect</dd>
<dd><code>provided</code> - fallback name</dd>
<dt>Returns:</dt>
<dd>name or fallback</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDeclaredNameApplicable(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isDeclaredNameApplicable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDeclaredNameApplicable</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the element's declared name is applicable.
 Declared names are not applicable for root namespaces or
 non-member relationships.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to inspect</dd>
<dt>Returns:</dt>
<dd>true if declared name is applicable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeclaredNameOrEmpty(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getDeclaredNameOrEmpty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDeclaredNameOrEmpty</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns the declared name of the element, or an empty string if none exists.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to inspect</dd>
<dt>Returns:</dt>
<dd>declared name or empty string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="escapeString(java.lang.String)">
<h3>escapeString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">escapeString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</span></div>
<div class="block">Escapes special characters in a string according to KerML rules.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>string</code> - the string to escape</dd>
<dt>Returns:</dt>
<dd>escaped string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unescapeString(java.lang.String)">
<h3>unescapeString</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">unescapeString</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</span></div>
<div class="block">Converts a string literal or unrestricted name with escaped characters
 into a string in which the escape sequences are replaced with the corresponding
 represented characters. If the input string starts with a single or double quote
 character, it is assumed to be a lexically valid unrestricted name or string literal,
 respectively. Otherwise, the input string is returned without change.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>string</code> - the string to unescape</dd>
<dt>Returns:</dt>
<dd>unescaped string, or null if input is null</dd>
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
