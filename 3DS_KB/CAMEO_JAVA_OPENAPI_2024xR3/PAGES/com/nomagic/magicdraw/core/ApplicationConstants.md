# JAVA OPENAPI: ApplicationConstants (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/ApplicationConstants.html
- source_path: `com/nomagic/magicdraw/core/ApplicationConstants.html`
- source_sha256: `58fa8437e019096d031fc9f40aadfc47c14b0fcffeebd197a5a8c078dba60a87`
- captured_utc: `2026-07-14T16:55:11.574965+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core](package-summary.html)

## Class ApplicationConstants

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.runtime.RuntimeConstants](../../runtime/RuntimeConstants.html)
com.nomagic.magicdraw.core.ApplicationConstants

@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public classApplicationConstants
extends [RuntimeConstants](../../runtime/RuntimeConstants.html)
Deprecated.
use [`Application`](Application.html)
This class holds application specific constants.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MAGICDRAW_NAME](#MAGICDRAW_NAME)`
Deprecated.
Use [`RebrandingConfigurator.getProductName()`](../rebranding/RebrandingConfigurator.html#getProductName()) with no "UML" addition in name.
Fields inherited from class com.nomagic.runtime.[RuntimeConstants](../../runtime/RuntimeConstants.html)
`[HF](../../runtime/RuntimeConstants.html#HF), [MAGIC_DRAW_SUPPORT_URL](../../runtime/RuntimeConstants.html#MAGIC_DRAW_SUPPORT_URL), [REFRESH](../../runtime/RuntimeConstants.html#REFRESH), [REFRESH1_NUMBER](../../runtime/RuntimeConstants.html#REFRESH1_NUMBER), [REFRESH3_NUMBER](../../runtime/RuntimeConstants.html#REFRESH3_NUMBER), [SP](../../runtime/RuntimeConstants.html#SP), [VERSION](../../runtime/RuntimeConstants.html#VERSION)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getApplicationName](#getApplicationName())()`
Deprecated.
use {@link Application#runtime#getApplicationName()}
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTemplatesDirectory](#getTemplatesDirectory())()`
Deprecated.
use {@link Application#environment#getTemplatesDirectory()}
`static void`
`[setApplicationName](#setApplicationName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Deprecated.
use {@link Application#runtimeInternal#setApplicationName(String)}
Methods inherited from class com.nomagic.runtime.[RuntimeConstants](../../runtime/RuntimeConstants.html)
`[appendRefreshAndHotFixNumber](../../runtime/RuntimeConstants.html#appendRefreshAndHotFixNumber(java.lang.String)), [appendRefreshAndHotFixNumber](../../runtime/RuntimeConstants.html#appendRefreshAndHotFixNumber(java.lang.String,java.lang.String,java.lang.String)), [appendRefreshNumber](../../runtime/RuntimeConstants.html#appendRefreshNumber(java.lang.String)), [appendRefreshNumber](../../runtime/RuntimeConstants.html#appendRefreshNumber(java.lang.String,java.lang.String)), [getFullVersion](../../runtime/RuntimeConstants.html#getFullVersion()), [getFullVersionWithHotFix](../../runtime/RuntimeConstants.html#getFullVersionWithHotFix()), [getHotFixNumber](../../runtime/RuntimeConstants.html#getHotFixNumber()), [getProductHomePage](../../runtime/RuntimeConstants.html#getProductHomePage()), [getRefreshNumber](../../runtime/RuntimeConstants.html#getRefreshNumber()), [parsePatchIndex](../../runtime/RuntimeConstants.html#parsePatchIndex(java.lang.String)), [setHotFixNumber](../../runtime/RuntimeConstants.html#setHotFixNumber(java.lang.String)), [setProductHomePage](../../runtime/RuntimeConstants.html#setProductHomePage(java.lang.String)), [setRefreshNumber](../../runtime/RuntimeConstants.html#setRefreshNumber(java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
MAGICDRAW_NAME
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MAGICDRAW_NAME
Deprecated.
Use [`RebrandingConfigurator.getProductName()`](../rebranding/RebrandingConfigurator.html#getProductName()) with no "UML" addition in name. Use {@link Application#runtimeInternal#MAGICDRAW_UML} if old reference is required (usually for import).
Application name
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.ApplicationConstants.MAGICDRAW_NAME)
 ============ METHOD DETAIL ========== 
Method Details
setApplicationName
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void setApplicationName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Deprecated.
use {@link Application#runtimeInternal#setApplicationName(String)}
Set the name of the application.
Parameters:
`name` - application name
getApplicationName
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getApplicationName()
Deprecated.
use {@link Application#runtime#getApplicationName()}
Returns application name
Returns:
application name
getTemplatesDirectory
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTemplatesDirectory()
Deprecated.
use {@link Application#environment#getTemplatesDirectory()}
Gets project templates directory.
Returns:
project templates directory.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core</a></div>
<h1 class="title" title="Class ApplicationConstants">Class ApplicationConstants</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../runtime/RuntimeConstants.html" title="class in com.nomagic.runtime">com.nomagic.runtime.RuntimeConstants</a>
<div class="inheritance">com.nomagic.magicdraw.core.ApplicationConstants</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ApplicationConstants</span>
<span class="extends-implements">extends <a href="../../runtime/RuntimeConstants.html" title="class in com.nomagic.runtime">RuntimeConstants</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Application.html" title="class in com.nomagic.magicdraw.core"><code>Application</code></a></div>
</div>
<div class="block">This class holds application specific constants.</div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MAGICDRAW_NAME">MAGICDRAW_NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="../rebranding/RebrandingConfigurator.html#getProductName()"><code>RebrandingConfigurator.getProductName()</code></a> with no "UML" addition in name.</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.runtime.RuntimeConstants">Fields inherited from class com.nomagic.runtime.<a href="../../runtime/RuntimeConstants.html" title="class in com.nomagic.runtime">RuntimeConstants</a></h3>
<code><a href="../../runtime/RuntimeConstants.html#HF">HF</a>, <a href="../../runtime/RuntimeConstants.html#MAGIC_DRAW_SUPPORT_URL">MAGIC_DRAW_SUPPORT_URL</a>, <a href="../../runtime/RuntimeConstants.html#REFRESH">REFRESH</a>, <a href="../../runtime/RuntimeConstants.html#REFRESH1_NUMBER">REFRESH1_NUMBER</a>, <a href="../../runtime/RuntimeConstants.html#REFRESH3_NUMBER">REFRESH3_NUMBER</a>, <a href="../../runtime/RuntimeConstants.html#SP">SP</a>, <a href="../../runtime/RuntimeConstants.html#VERSION">VERSION</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getApplicationName()">getApplicationName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use {@link Application#runtime#getApplicationName()}</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getTemplatesDirectory()">getTemplatesDirectory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use {@link Application#environment#getTemplatesDirectory()}</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setApplicationName(java.lang.String)">setApplicationName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use {@link Application#runtimeInternal#setApplicationName(String)}</div>
</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.runtime.RuntimeConstants">Methods inherited from class com.nomagic.runtime.<a href="../../runtime/RuntimeConstants.html" title="class in com.nomagic.runtime">RuntimeConstants</a></h3>
<code><a href="../../runtime/RuntimeConstants.html#appendRefreshAndHotFixNumber(java.lang.String)">appendRefreshAndHotFixNumber</a>, <a href="../../runtime/RuntimeConstants.html#appendRefreshAndHotFixNumber(java.lang.String,java.lang.String,java.lang.String)">appendRefreshAndHotFixNumber</a>, <a href="../../runtime/RuntimeConstants.html#appendRefreshNumber(java.lang.String)">appendRefreshNumber</a>, <a href="../../runtime/RuntimeConstants.html#appendRefreshNumber(java.lang.String,java.lang.String)">appendRefreshNumber</a>, <a href="../../runtime/RuntimeConstants.html#getFullVersion()">getFullVersion</a>, <a href="../../runtime/RuntimeConstants.html#getFullVersionWithHotFix()">getFullVersionWithHotFix</a>, <a href="../../runtime/RuntimeConstants.html#getHotFixNumber()">getHotFixNumber</a>, <a href="../../runtime/RuntimeConstants.html#getProductHomePage()">getProductHomePage</a>, <a href="../../runtime/RuntimeConstants.html#getRefreshNumber()">getRefreshNumber</a>, <a href="../../runtime/RuntimeConstants.html#parsePatchIndex(java.lang.String)">parsePatchIndex</a>, <a href="../../runtime/RuntimeConstants.html#setHotFixNumber(java.lang.String)">setHotFixNumber</a>, <a href="../../runtime/RuntimeConstants.html#setProductHomePage(java.lang.String)">setProductHomePage</a>, <a href="../../runtime/RuntimeConstants.html#setRefreshNumber(java.lang.String)">setRefreshNumber</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="MAGICDRAW_NAME">
<h3>MAGICDRAW_NAME</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MAGICDRAW_NAME</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="../rebranding/RebrandingConfigurator.html#getProductName()"><code>RebrandingConfigurator.getProductName()</code></a> with no "UML" addition in name. Use {@link Application#runtimeInternal#MAGICDRAW_UML} if old reference is required (usually for import).</div>
</div>
<div class="block">Application name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.ApplicationConstants.MAGICDRAW_NAME">Constant Field Values</a></li>
</ul>
</dd>
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
<section class="detail" id="setApplicationName(java.lang.String)">
<h3>setApplicationName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setApplicationName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use {@link Application#runtimeInternal#setApplicationName(String)}</div>
</div>
<div class="block">Set the name of the application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - application name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getApplicationName()">
<h3>getApplicationName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getApplicationName</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use {@link Application#runtime#getApplicationName()}</div>
</div>
<div class="block">Returns application name</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>application name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplatesDirectory()">
<h3>getTemplatesDirectory</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTemplatesDirectory</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use {@link Application#environment#getTemplatesDirectory()}</div>
</div>
<div class="block">Gets project templates directory.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project templates directory.</dd>
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
