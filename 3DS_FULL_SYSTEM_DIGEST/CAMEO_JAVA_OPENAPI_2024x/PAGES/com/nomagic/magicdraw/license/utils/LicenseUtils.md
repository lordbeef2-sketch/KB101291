# JAVA OPENAPI: LicenseUtils (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/license/utils/LicenseUtils.html
- source_path: `com/nomagic/magicdraw/license/utils/LicenseUtils.html`
- source_sha256: `5df79dba8d7c8bc7e411e2608dc6949892792634c31645216cb347943daf9d94`
- captured_utc: `2026-07-14T16:51:23.238229+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.license.utils](package-summary.html)

## Class LicenseUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.license.utils.LicenseUtils

@OpenApiAllpublic final classLicenseUtils
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Utility class for accessing licensing information.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[LicenseUtils](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getEdition](#getEdition())()`
Get current edition.
`static boolean`
`[isArchitectEdition](#isArchitectEdition())()`
Check if Architect edition.
`static boolean`
`[isArchitectVersion](#isArchitectVersion())()`
Deprecated.
use [`isArchitectEdition()`](#isArchitectEdition())
`static boolean`
`[isDemoVersion](#isDemoVersion())()`
Check if Demo version.
`static boolean`
`[isEdition](#isEdition(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) edition)`
Check if given edition.
`static boolean`
`[isEnterpriseEdition](#isEnterpriseEdition())()`
Check if Enterprise edition.
`static boolean`
`[isEnterpriseVersion](#isEnterpriseVersion())()`
Deprecated.
use [`isEnterpriseEdition()`](#isEnterpriseEdition())
`static boolean`
`[isEvaluationVersion](#isEvaluationVersion())()`
Check if Evaluation version.
`static boolean`
`[isFloating](#isFloating())()`
Check if Floating license type.
`static boolean`
`[isHigherThanStandardEdition](#isHigherThanStandardEdition())()`
Check if "higher" than Standard edition.
`static boolean`
`[isReaderEdition](#isReaderEdition())()`
Check if Reader edition.
`static boolean`
`[isStandardEditionOrHigher](#isStandardEditionOrHigher())()`
Check if Standard edition or "higher".
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
LicenseUtils
public LicenseUtils()
 ============ METHOD DETAIL ========== 
Method Details
isReaderEdition
public static boolean isReaderEdition()
Check if Reader edition.
Returns:
true if Reader edition, otherwise - false.
isEnterpriseEdition
public static boolean isEnterpriseEdition()
Check if Enterprise edition.
Returns:
true if Enterprise edition, otherwise - false.
isArchitectEdition
public static boolean isArchitectEdition()
Check if Architect edition.
Returns:
true if Architect edition, otherwise - false.
isEdition
public static boolean isEdition([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) edition)
Check if given edition.
Parameters:
`edition` - edition to check.
Returns:
true if given edition, otherwise - false.
getEdition
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getEdition()
Get current edition.
Returns:
current edition.
isStandardEditionOrHigher
public static boolean isStandardEditionOrHigher()
Check if Standard edition or "higher".
Returns:
true if Standard edition or "higher", otherwise - false.
isHigherThanStandardEdition
public static boolean isHigherThanStandardEdition()
Check if "higher" than Standard edition.
Returns:
true if "higher" than Standard edition, otherwise - false.
isEvaluationVersion
public static boolean isEvaluationVersion()
Check if Evaluation version.
Returns:
true if Evaluation version, otherwise - false.
isDemoVersion
public static boolean isDemoVersion()
Check if Demo version.
Returns:
true if Demo version, otherwise - false.
isFloating
public static boolean isFloating()
Check if Floating license type.
Returns:
true if Floating license, otherwise - false.
isArchitectVersion
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isArchitectVersion()
Deprecated.
use [`isArchitectEdition()`](#isArchitectEdition())
isEnterpriseVersion
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isEnterpriseVersion()
Deprecated.
use [`isEnterpriseEdition()`](#isEnterpriseEdition())

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.license.utils</a></div>
<h1 class="title" title="Class LicenseUtils">Class LicenseUtils</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.license.utils.LicenseUtils</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">LicenseUtils</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class for accessing licensing information.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">LicenseUtils</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEdition()">getEdition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get current edition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isArchitectEdition()">isArchitectEdition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if Architect edition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isArchitectVersion()">isArchitectVersion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#isArchitectEdition()"><code>isArchitectEdition()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDemoVersion()">isDemoVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if Demo version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isEdition(java.lang.String)">isEdition</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> edition)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given edition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isEnterpriseEdition()">isEnterpriseEdition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if Enterprise edition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isEnterpriseVersion()">isEnterpriseVersion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#isEnterpriseEdition()"><code>isEnterpriseEdition()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isEvaluationVersion()">isEvaluationVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if Evaluation version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFloating()">isFloating</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if Floating license type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isHigherThanStandardEdition()">isHigherThanStandardEdition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if "higher" than Standard edition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isReaderEdition()">isReaderEdition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if Reader edition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStandardEditionOrHigher()">isStandardEditionOrHigher</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if Standard edition or "higher".</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>LicenseUtils</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LicenseUtils</span>()</div>
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
<section class="detail" id="isReaderEdition()">
<h3>isReaderEdition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isReaderEdition</span>()</div>
<div class="block">Check if Reader edition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if Reader edition, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEnterpriseEdition()">
<h3>isEnterpriseEdition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEnterpriseEdition</span>()</div>
<div class="block">Check if Enterprise edition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if Enterprise edition, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isArchitectEdition()">
<h3>isArchitectEdition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isArchitectEdition</span>()</div>
<div class="block">Check if Architect edition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if Architect edition, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEdition(java.lang.String)">
<h3>isEdition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEdition</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> edition)</span></div>
<div class="block">Check if given edition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>edition</code> - edition to check.</dd>
<dt>Returns:</dt>
<dd>true if given edition, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEdition()">
<h3>getEdition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEdition</span>()</div>
<div class="block">Get current edition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>current edition.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStandardEditionOrHigher()">
<h3>isStandardEditionOrHigher</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStandardEditionOrHigher</span>()</div>
<div class="block">Check if Standard edition or "higher".</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if Standard edition or "higher", otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isHigherThanStandardEdition()">
<h3>isHigherThanStandardEdition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isHigherThanStandardEdition</span>()</div>
<div class="block">Check if "higher" than Standard edition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if "higher" than Standard edition, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEvaluationVersion()">
<h3>isEvaluationVersion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEvaluationVersion</span>()</div>
<div class="block">Check if Evaluation version.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if Evaluation version, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDemoVersion()">
<h3>isDemoVersion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDemoVersion</span>()</div>
<div class="block">Check if Demo version.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if Demo version, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFloating()">
<h3>isFloating</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFloating</span>()</div>
<div class="block">Check if Floating license type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if Floating license, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isArchitectVersion()">
<h3>isArchitectVersion</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isArchitectVersion</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#isArchitectEdition()"><code>isArchitectEdition()</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="isEnterpriseVersion()">
<h3>isEnterpriseVersion</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEnterpriseVersion</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#isEnterpriseEdition()"><code>isEnterpriseEdition()</code></a></div>
</div>
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
