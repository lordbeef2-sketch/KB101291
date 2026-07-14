# JAVA OPENAPI: TreeNodeAdornmentManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/browser/TreeNodeAdornmentManager.html
- source_path: `com/nomagic/magicdraw/ui/browser/TreeNodeAdornmentManager.html`
- source_sha256: `a0361b4de346762c2030c6ec475e5c9010773cbcbafb360bf1042f75d9416d9d`
- captured_utc: `2026-07-14T16:55:51.433414+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.browser](package-summary.html)

## Class TreeNodeAdornmentManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.browser.TreeNodeAdornmentManager

@OpenApiAllpublic final classTreeNodeAdornmentManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Tree node adornment manager provides registers [`IconAdornment`](../IconAdornment.html), [`NodeIconAdornment`](../NodeIconAdornment.html), [`TextAdornment`](TextAdornment.html), and [`NodeTextAdornment`](NodeTextAdornment.html).

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addIconAdornment](#addIconAdornment(com.nomagic.magicdraw.ui.IconAdornment))([IconAdornment](../IconAdornment.html) adornment)`
Add icon adornment.
`void`
`[addNodeIconAdornment](#addNodeIconAdornment(com.nomagic.magicdraw.ui.NodeIconAdornment))([NodeIconAdornment](../NodeIconAdornment.html) adornment)`
Add node icon adornment.
`void`
`[addNodeTextAdornment](#addNodeTextAdornment(com.nomagic.magicdraw.ui.browser.NodeTextAdornment))([NodeTextAdornment](NodeTextAdornment.html) adornment)`
Add node text adornment.
`void`
`[addTextAdornment](#addTextAdornment(com.nomagic.magicdraw.ui.browser.TextAdornment))([TextAdornment](TextAdornment.html) adornment)`
Add text adornment.
`static [TreeNodeAdornmentManager](TreeNodeAdornmentManager.html)`
`[getInstance](#getInstance())()`
Get singleton instance.
`void`
`[removeIconAdornment](#removeIconAdornment(com.nomagic.magicdraw.ui.IconAdornment))([IconAdornment](../IconAdornment.html) adornment)`
Remove registered icon adornment.
`void`
`[removeNodeIconAdornment](#removeNodeIconAdornment(com.nomagic.magicdraw.ui.NodeIconAdornment))([NodeIconAdornment](../NodeIconAdornment.html) adornment)`
Remove registered node icon adornment.
`void`
`[removeTextAdornment](#removeTextAdornment(com.nomagic.magicdraw.ui.browser.NodeTextAdornment))([NodeTextAdornment](NodeTextAdornment.html) adornment)`
Remove registered node text adornment.
`void`
`[removeTextAdornment](#removeTextAdornment(com.nomagic.magicdraw.ui.browser.TextAdornment))([TextAdornment](TextAdornment.html) adornment)`
Remove registered text adornment.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
public static [TreeNodeAdornmentManager](TreeNodeAdornmentManager.html) getInstance()
Get singleton instance.
Returns:
instance.
addIconAdornment
public void addIconAdornment([IconAdornment](../IconAdornment.html) adornment)
Add icon adornment.
Parameters:
`adornment` - icon adornment to register.
removeIconAdornment
public void removeIconAdornment([IconAdornment](../IconAdornment.html) adornment)
Remove registered icon adornment.
Parameters:
`adornment` - icon adornment to remove.
addNodeIconAdornment
public void addNodeIconAdornment([NodeIconAdornment](../NodeIconAdornment.html) adornment)
Add node icon adornment.
Parameters:
`adornment` - icon adornment to register
removeNodeIconAdornment
public void removeNodeIconAdornment([NodeIconAdornment](../NodeIconAdornment.html) adornment)
Remove registered node icon adornment.
Parameters:
`adornment` - icon adornment to remove.
addTextAdornment
public void addTextAdornment([TextAdornment](TextAdornment.html) adornment)
Add text adornment.
Parameters:
`adornment` - text adornment to register.
removeTextAdornment
public void removeTextAdornment([TextAdornment](TextAdornment.html) adornment)
Remove registered text adornment.
Parameters:
`adornment` - text adornment to remove.
addNodeTextAdornment
public void addNodeTextAdornment([NodeTextAdornment](NodeTextAdornment.html) adornment)
Add node text adornment.
Parameters:
`adornment` - text adornment to register
removeTextAdornment
public void removeTextAdornment([NodeTextAdornment](NodeTextAdornment.html) adornment)
Remove registered node text adornment.
Parameters:
`adornment` - text adornment to remove

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.browser</a></div>
<h1 class="title" title="Class TreeNodeAdornmentManager">Class TreeNodeAdornmentManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.browser.TreeNodeAdornmentManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">TreeNodeAdornmentManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Tree node adornment manager provides registers <a href="../IconAdornment.html" title="interface in com.nomagic.magicdraw.ui"><code>IconAdornment</code></a>, <a href="../NodeIconAdornment.html" title="interface in com.nomagic.magicdraw.ui"><code>NodeIconAdornment</code></a>, <a href="TextAdornment.html" title="interface in com.nomagic.magicdraw.ui.browser"><code>TextAdornment</code></a>, and <a href="NodeTextAdornment.html" title="interface in com.nomagic.magicdraw.ui.browser"><code>NodeTextAdornment</code></a>.</div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addIconAdornment(com.nomagic.magicdraw.ui.IconAdornment)">addIconAdornment</a><wbr/>(<a href="../IconAdornment.html" title="interface in com.nomagic.magicdraw.ui">IconAdornment</a> adornment)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add icon adornment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addNodeIconAdornment(com.nomagic.magicdraw.ui.NodeIconAdornment)">addNodeIconAdornment</a><wbr/>(<a href="../NodeIconAdornment.html" title="interface in com.nomagic.magicdraw.ui">NodeIconAdornment</a> adornment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add node icon adornment.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addNodeTextAdornment(com.nomagic.magicdraw.ui.browser.NodeTextAdornment)">addNodeTextAdornment</a><wbr/>(<a href="NodeTextAdornment.html" title="interface in com.nomagic.magicdraw.ui.browser">NodeTextAdornment</a> adornment)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add node text adornment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addTextAdornment(com.nomagic.magicdraw.ui.browser.TextAdornment)">addTextAdornment</a><wbr/>(<a href="TextAdornment.html" title="interface in com.nomagic.magicdraw.ui.browser">TextAdornment</a> adornment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add text adornment.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TreeNodeAdornmentManager.html" title="class in com.nomagic.magicdraw.ui.browser">TreeNodeAdornmentManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get singleton instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeIconAdornment(com.nomagic.magicdraw.ui.IconAdornment)">removeIconAdornment</a><wbr/>(<a href="../IconAdornment.html" title="interface in com.nomagic.magicdraw.ui">IconAdornment</a> adornment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove registered icon adornment.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeNodeIconAdornment(com.nomagic.magicdraw.ui.NodeIconAdornment)">removeNodeIconAdornment</a><wbr/>(<a href="../NodeIconAdornment.html" title="interface in com.nomagic.magicdraw.ui">NodeIconAdornment</a> adornment)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove registered node icon adornment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeTextAdornment(com.nomagic.magicdraw.ui.browser.NodeTextAdornment)">removeTextAdornment</a><wbr/>(<a href="NodeTextAdornment.html" title="interface in com.nomagic.magicdraw.ui.browser">NodeTextAdornment</a> adornment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove registered node text adornment.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeTextAdornment(com.nomagic.magicdraw.ui.browser.TextAdornment)">removeTextAdornment</a><wbr/>(<a href="TextAdornment.html" title="interface in com.nomagic.magicdraw.ui.browser">TextAdornment</a> adornment)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove registered text adornment.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="TreeNodeAdornmentManager.html" title="class in com.nomagic.magicdraw.ui.browser">TreeNodeAdornmentManager</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Get singleton instance.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addIconAdornment(com.nomagic.magicdraw.ui.IconAdornment)">
<h3>addIconAdornment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addIconAdornment</span><wbr/><span class="parameters">(<a href="../IconAdornment.html" title="interface in com.nomagic.magicdraw.ui">IconAdornment</a> adornment)</span></div>
<div class="block">Add icon adornment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>adornment</code> - icon adornment to register.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeIconAdornment(com.nomagic.magicdraw.ui.IconAdornment)">
<h3>removeIconAdornment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeIconAdornment</span><wbr/><span class="parameters">(<a href="../IconAdornment.html" title="interface in com.nomagic.magicdraw.ui">IconAdornment</a> adornment)</span></div>
<div class="block">Remove registered icon adornment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>adornment</code> - icon adornment to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addNodeIconAdornment(com.nomagic.magicdraw.ui.NodeIconAdornment)">
<h3>addNodeIconAdornment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addNodeIconAdornment</span><wbr/><span class="parameters">(<a href="../NodeIconAdornment.html" title="interface in com.nomagic.magicdraw.ui">NodeIconAdornment</a> adornment)</span></div>
<div class="block">Add node icon adornment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>adornment</code> - icon adornment to register</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeNodeIconAdornment(com.nomagic.magicdraw.ui.NodeIconAdornment)">
<h3>removeNodeIconAdornment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeNodeIconAdornment</span><wbr/><span class="parameters">(<a href="../NodeIconAdornment.html" title="interface in com.nomagic.magicdraw.ui">NodeIconAdornment</a> adornment)</span></div>
<div class="block">Remove registered node icon adornment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>adornment</code> - icon adornment to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addTextAdornment(com.nomagic.magicdraw.ui.browser.TextAdornment)">
<h3>addTextAdornment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addTextAdornment</span><wbr/><span class="parameters">(<a href="TextAdornment.html" title="interface in com.nomagic.magicdraw.ui.browser">TextAdornment</a> adornment)</span></div>
<div class="block">Add text adornment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>adornment</code> - text adornment to register.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeTextAdornment(com.nomagic.magicdraw.ui.browser.TextAdornment)">
<h3>removeTextAdornment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeTextAdornment</span><wbr/><span class="parameters">(<a href="TextAdornment.html" title="interface in com.nomagic.magicdraw.ui.browser">TextAdornment</a> adornment)</span></div>
<div class="block">Remove registered text adornment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>adornment</code> - text adornment to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addNodeTextAdornment(com.nomagic.magicdraw.ui.browser.NodeTextAdornment)">
<h3>addNodeTextAdornment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addNodeTextAdornment</span><wbr/><span class="parameters">(<a href="NodeTextAdornment.html" title="interface in com.nomagic.magicdraw.ui.browser">NodeTextAdornment</a> adornment)</span></div>
<div class="block">Add node text adornment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>adornment</code> - text adornment to register</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeTextAdornment(com.nomagic.magicdraw.ui.browser.NodeTextAdornment)">
<h3>removeTextAdornment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeTextAdornment</span><wbr/><span class="parameters">(<a href="NodeTextAdornment.html" title="interface in com.nomagic.magicdraw.ui.browser">NodeTextAdornment</a> adornment)</span></div>
<div class="block">Remove registered node text adornment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>adornment</code> - text adornment to remove</dd>
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
