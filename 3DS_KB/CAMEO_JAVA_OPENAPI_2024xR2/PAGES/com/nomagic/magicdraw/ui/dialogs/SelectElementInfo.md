# JAVA OPENAPI: SelectElementInfo (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/ui/dialogs/SelectElementInfo.html
- source_path: `com/nomagic/magicdraw/ui/dialogs/SelectElementInfo.html`
- source_sha256: `d90875784211fc7f268781b90bd7130469b21d2e38293aeb46aa77cf8b56d986`
- captured_utc: `2026-07-14T16:55:49.686397+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dialogs](package-summary.html)

## Class SelectElementInfo

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.dialogs.SelectElementInfo

@OpenApipublic classSelectElementInfo
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Info class for controling selection UI in element selection dialog.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`boolean`
`[allowLoad](#allowLoad)`
Deprecated.
not used anymore.
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[root](#root)`
Root element of selection UI
`boolean`
`[showDiagrams](#showDiagrams)`
Show diagrams nodes and allow to choose presentation elements in selection UI
`boolean`
`[showNone](#showNone)`
Show NONE node
`boolean`
`[showRelationships](#showRelationships)`
Deprecated.
not used anymore.
`boolean`
`[sortable](#sortable)`
Should result of selection in UI be "sortable"
`static final int`
`[SUGGESTION_LIST_ALWAYS](#SUGGESTION_LIST_ALWAYS)`
Deprecated.
not used anymore
`static final int`
`[SUGGESTION_LIST_NEVER](#SUGGESTION_LIST_NEVER)`
Deprecated.
not used anymore
`static final int`
`[SUGGESTION_LIST_ON_DEMAND](#SUGGESTION_LIST_ON_DEMAND)`
Deprecated.
not used anymore
`int`
`[suggestionList](#suggestionList)`
Deprecated.
not used anymore.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SelectElementInfo](#%3Cinit%3E(boolean,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))(boolean showNone,
 boolean showDiagrams,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 boolean sortable)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
SUGGESTION_LIST_NEVER
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final int SUGGESTION_LIST_NEVER
Deprecated.
not used anymore
Never show element suggestion list.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.SelectElementInfo.SUGGESTION_LIST_NEVER)
SUGGESTION_LIST_ALWAYS
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final int SUGGESTION_LIST_ALWAYS
Deprecated.
not used anymore
Always show element suggestion list.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.SelectElementInfo.SUGGESTION_LIST_ALWAYS)
SUGGESTION_LIST_ON_DEMAND
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final int SUGGESTION_LIST_ON_DEMAND
Deprecated.
not used anymore
Show suggestion list only if suggested elements are Types
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.SelectElementInfo.SUGGESTION_LIST_ON_DEMAND)
showNone
@OpenApipublic boolean showNone
Show NONE node
showDiagrams
@OpenApipublic boolean showDiagrams
Show diagrams nodes and allow to choose presentation elements in selection UI
showRelationships
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public boolean showRelationships
Deprecated.
not used anymore. Now relationships are shown on demand
Show model relationships in selection UI
allowLoad
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public boolean allowLoad
Deprecated.
not used anymore. Now modules are allowed to load if needed
Allow to load not loaded modules in UI
suggestionList
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public int suggestionList
Deprecated.
not used anymore. Suggestion list is shown always in selection UI
Suggestion list display mode
See Also:
[`SUGGESTION_LIST_ALWAYS`](#SUGGESTION_LIST_ALWAYS)
[`SUGGESTION_LIST_NEVER`](#SUGGESTION_LIST_NEVER)
[`SUGGESTION_LIST_ON_DEMAND`](#SUGGESTION_LIST_ON_DEMAND)
root
@OpenApipublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root
Root element of selection UI
sortable
@OpenApipublic boolean sortable
Should result of selection in UI be "sortable"
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SelectElementInfo
@OpenApipublic SelectElementInfo(boolean showNone,
 boolean showDiagrams,
 @CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 boolean sortable)
Constructor.
Parameters:
`showNone` - [`showNone`](#showNone) value.
`showDiagrams` - [`showDiagrams`](#showDiagrams) value.
`root` - [`root`](#root) value.
`sortable` - [`sortable`](#sortable) value.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dialogs</a></div>
<h1 class="title" title="Class SelectElementInfo">Class SelectElementInfo</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dialogs.SelectElementInfo</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SelectElementInfo</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Info class for controling selection UI in element selection dialog.</div>
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
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#allowLoad">allowLoad</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore.</div>
</div>
</div>
<div class="col-first odd-row-color"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#root">root</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Root element of selection UI</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#showDiagrams">showDiagrams</a></code></div>
<div class="col-last even-row-color">
<div class="block">Show diagrams nodes and allow to choose presentation elements in selection UI</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#showNone">showNone</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Show NONE node</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#showRelationships">showRelationships</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore.</div>
</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#sortable">sortable</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Should result of selection in UI be "sortable"</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SUGGESTION_LIST_ALWAYS">SUGGESTION_LIST_ALWAYS</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SUGGESTION_LIST_NEVER">SUGGESTION_LIST_NEVER</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SUGGESTION_LIST_ON_DEMAND">SUGGESTION_LIST_ON_DEMAND</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore</div>
</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#suggestionList">suggestionList</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore.</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(boolean,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">SelectElementInfo</a><wbr/>(boolean showNone,
 boolean showDiagrams,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 boolean sortable)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
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
<section class="detail" id="SUGGESTION_LIST_NEVER">
<h3>SUGGESTION_LIST_NEVER</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SUGGESTION_LIST_NEVER</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore</div>
</div>
<div class="block">Never show element suggestion list.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.SelectElementInfo.SUGGESTION_LIST_NEVER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SUGGESTION_LIST_ALWAYS">
<h3>SUGGESTION_LIST_ALWAYS</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SUGGESTION_LIST_ALWAYS</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore</div>
</div>
<div class="block">Always show element suggestion list.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.SelectElementInfo.SUGGESTION_LIST_ALWAYS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SUGGESTION_LIST_ON_DEMAND">
<h3>SUGGESTION_LIST_ON_DEMAND</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SUGGESTION_LIST_ON_DEMAND</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore</div>
</div>
<div class="block">Show suggestion list only if suggested elements are Types</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.SelectElementInfo.SUGGESTION_LIST_ON_DEMAND">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showNone">
<h3>showNone</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showNone</span></div>
<div class="block">Show NONE node</div>
</section>
</li>
<li>
<section class="detail" id="showDiagrams">
<h3>showDiagrams</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showDiagrams</span></div>
<div class="block">Show diagrams nodes and allow to choose presentation elements in selection UI</div>
</section>
</li>
<li>
<section class="detail" id="showRelationships">
<h3>showRelationships</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showRelationships</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore. Now relationships are shown on demand</div>
</div>
<div class="block">Show model relationships in selection UI</div>
</section>
</li>
<li>
<section class="detail" id="allowLoad">
<h3>allowLoad</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">allowLoad</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore. Now modules are allowed to load if needed</div>
</div>
<div class="block">Allow to load not loaded modules in UI</div>
</section>
</li>
<li>
<section class="detail" id="suggestionList">
<h3>suggestionList</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">suggestionList</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore. Suggestion list is shown always in selection UI</div>
</div>
<div class="block">Suggestion list display mode</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SUGGESTION_LIST_ALWAYS"><code>SUGGESTION_LIST_ALWAYS</code></a></li>
<li><a href="#SUGGESTION_LIST_NEVER"><code>SUGGESTION_LIST_NEVER</code></a></li>
<li><a href="#SUGGESTION_LIST_ON_DEMAND"><code>SUGGESTION_LIST_ON_DEMAND</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="root">
<h3>root</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">root</span></div>
<div class="block">Root element of selection UI</div>
</section>
</li>
<li>
<section class="detail" id="sortable">
<h3>sortable</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">sortable</span></div>
<div class="block">Should result of selection in UI be "sortable"</div>
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
<section class="detail" id="&lt;init&gt;(boolean,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>SelectElementInfo</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">SelectElementInfo</span><wbr/><span class="parameters">(boolean showNone,
 boolean showDiagrams,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 boolean sortable)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showNone</code> - <a href="#showNone"><code>showNone</code></a> value.</dd>
<dd><code>showDiagrams</code> - <a href="#showDiagrams"><code>showDiagrams</code></a> value.</dd>
<dd><code>root</code> - <a href="#root"><code>root</code></a> value.</dd>
<dd><code>sortable</code> - <a href="#sortable"><code>sortable</code></a> value.</dd>
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
