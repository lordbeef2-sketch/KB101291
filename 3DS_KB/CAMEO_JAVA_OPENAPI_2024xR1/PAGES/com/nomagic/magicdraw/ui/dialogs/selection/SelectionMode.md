# JAVA OPENAPI: SelectionMode (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/ui/dialogs/selection/SelectionMode.html
- source_path: `com/nomagic/magicdraw/ui/dialogs/selection/SelectionMode.html`
- source_sha256: `4622966c56b17a3aa27972b979ca62e7f17359928bd47c1c77ef72e4540420b0`
- captured_utc: `2026-07-14T16:52:02.958759+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dialogs.selection](package-summary.html)

## Class SelectionMode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.dialogs.selection.SelectionMode

@OpenApiAllpublic final classSelectionMode
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Describes element selection mode. Element selection can support single/multiple selection modes.
 The multiple selection mode allows to initialize selection in single mode.

See Also:
[`SINGLE_MODE`](#SINGLE_MODE)
[`MULTIPLE_MODE`](#MULTIPLE_MODE)
[`MULTIPLE_MODE_SINGLE_INITIAL`](#MULTIPLE_MODE_SINGLE_INITIAL)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [SelectionMode](SelectionMode.html)`
`[MULTIPLE_MODE](#MULTIPLE_MODE)`
Multiple selection mode (with initial multiple selection).
`static final [SelectionMode](SelectionMode.html)`
`[MULTIPLE_MODE_SINGLE_INITIAL](#MULTIPLE_MODE_SINGLE_INITIAL)`
Multiple selection mode with initial single selection mode.
`static final [SelectionMode](SelectionMode.html)`
`[SINGLE_MODE](#SINGLE_MODE)`
Single selection mode.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[isInitialSingleMode](#isInitialSingleMode())()`
Check initial selection mode.
`boolean`
`[isSingleMode](#isSingleMode())()`
Check selection mode.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
SINGLE_MODE
public static final [SelectionMode](SelectionMode.html) SINGLE_MODE
Single selection mode.
MULTIPLE_MODE
public static final [SelectionMode](SelectionMode.html) MULTIPLE_MODE
Multiple selection mode (with initial multiple selection).
MULTIPLE_MODE_SINGLE_INITIAL
public static final [SelectionMode](SelectionMode.html) MULTIPLE_MODE_SINGLE_INITIAL
Multiple selection mode with initial single selection mode.
 ============ METHOD DETAIL ========== 
Method Details
isSingleMode
public boolean isSingleMode()
Check selection mode.
Returns:
true - single selection mode, false - multiple selection mode.
isInitialSingleMode
public boolean isInitialSingleMode()
Check initial selection mode. If [`isSingleMode()`](#isSingleMode()) returns true, this method also returns true.
 Only multiple selection mode supports multiple initial selection mode.
Returns:
true - single selection mode, false - multiple selection mode.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dialogs.selection</a></div>
<h1 class="title" title="Class SelectionMode">Class SelectionMode</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dialogs.selection.SelectionMode</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">SelectionMode</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Describes element selection mode. Element selection can support single/multiple selection modes.
 The multiple selection mode allows to initialize selection in single mode.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SINGLE_MODE"><code>SINGLE_MODE</code></a></li>
<li><a href="#MULTIPLE_MODE"><code>MULTIPLE_MODE</code></a></li>
<li><a href="#MULTIPLE_MODE_SINGLE_INITIAL"><code>MULTIPLE_MODE_SINGLE_INITIAL</code></a></li>
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
<div class="col-first even-row-color"><code>static final <a href="SelectionMode.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">SelectionMode</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MULTIPLE_MODE">MULTIPLE_MODE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Multiple selection mode (with initial multiple selection).</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SelectionMode.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">SelectionMode</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MULTIPLE_MODE_SINGLE_INITIAL">MULTIPLE_MODE_SINGLE_INITIAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Multiple selection mode with initial single selection mode.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SelectionMode.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">SelectionMode</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SINGLE_MODE">SINGLE_MODE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Single selection mode.</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isInitialSingleMode()">isInitialSingleMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check initial selection mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSingleMode()">isSingleMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check selection mode.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="SINGLE_MODE">
<h3>SINGLE_MODE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SelectionMode.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">SelectionMode</a></span> <span class="element-name">SINGLE_MODE</span></div>
<div class="block">Single selection mode.</div>
</section>
</li>
<li>
<section class="detail" id="MULTIPLE_MODE">
<h3>MULTIPLE_MODE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SelectionMode.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">SelectionMode</a></span> <span class="element-name">MULTIPLE_MODE</span></div>
<div class="block">Multiple selection mode (with initial multiple selection).</div>
</section>
</li>
<li>
<section class="detail" id="MULTIPLE_MODE_SINGLE_INITIAL">
<h3>MULTIPLE_MODE_SINGLE_INITIAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SelectionMode.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">SelectionMode</a></span> <span class="element-name">MULTIPLE_MODE_SINGLE_INITIAL</span></div>
<div class="block">Multiple selection mode with initial single selection mode.</div>
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
<section class="detail" id="isSingleMode()">
<h3>isSingleMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSingleMode</span>()</div>
<div class="block">Check selection mode.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true - single selection mode, false - multiple selection mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInitialSingleMode()">
<h3>isInitialSingleMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isInitialSingleMode</span>()</div>
<div class="block">Check initial selection mode. If <a href="#isSingleMode()"><code>isSingleMode()</code></a> returns true, this method also returns true.
 Only multiple selection mode supports multiple initial selection mode.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true - single selection mode, false - multiple selection mode.</dd>
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
