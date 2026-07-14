# JAVA OPENAPI: SymbolDrawNotification (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml/symbols/SymbolDrawNotification.html
- source_path: `com/nomagic/magicdraw/uml/symbols/SymbolDrawNotification.html`
- source_sha256: `761e8a1028f25eeab7d9eec6cef6d817fc04d6f5427188db8cfbefb12d9a9288`
- captured_utc: `2026-07-14T16:52:09.517846+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class SymbolDrawNotification

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.SymbolDrawNotification

@OpenApipublic final classSymbolDrawNotification
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

A manager for registering [`SymbolDrawListener`](SymbolDrawListener.html). These listeners are notified when some symbol is drawn in diagram.

See Also:
[`SymbolDrawListener`](SymbolDrawListener.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addSymbolDrawListener](#addSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener))([SymbolDrawListener](SymbolDrawListener.html) listener)`
Registers listener for symbols adding during draw operation.
`void`
`[addSymbolDrawListener](#addSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2))(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2 listener)`
Registers listener for symbols adding during draw operation.
`static [SymbolDrawNotification](SymbolDrawNotification.html)`
`[getSymbolDrawNotification](#getSymbolDrawNotification(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Returns a shared instance of this manager for given project.
`void`
`[removeSymbolDrawListener](#removeSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener))([SymbolDrawListener](SymbolDrawListener.html) listener)`
Unregisters listener for symbols adding during draw operation.
`void`
`[removeSymbolDrawListener](#removeSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2))(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2 listener)`
Unregisters listener for symbols adding during draw operation.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
addSymbolDrawListener
@OpenApipublic void addSymbolDrawListener([SymbolDrawListener](SymbolDrawListener.html) listener)
Registers listener for symbols adding during draw operation.
Parameters:
`listener` - the listener to register.
addSymbolDrawListener
@OpenApipublic void addSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2 listener)
Registers listener for symbols adding during draw operation.
Parameters:
`listener` - the listener to register.
removeSymbolDrawListener
@OpenApipublic void removeSymbolDrawListener([SymbolDrawListener](SymbolDrawListener.html) listener)
Unregisters listener for symbols adding during draw operation.
Parameters:
`listener` - the listener to unregister.
removeSymbolDrawListener
@OpenApipublic void removeSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2 listener)
Unregisters listener for symbols adding during draw operation.
Parameters:
`listener` - the listener to unregister.
getSymbolDrawNotification
@OpenApipublic static [SymbolDrawNotification](SymbolDrawNotification.html) getSymbolDrawNotification([Project](../../core/Project.html) project)
Returns a shared instance of this manager for given project. Every project has its own notification manager.
Parameters:
`project` - project to get manager for.
Returns:
manager.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class SymbolDrawNotification">Class SymbolDrawNotification</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.SymbolDrawNotification</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">SymbolDrawNotification</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">A manager for registering <a href="SymbolDrawListener.html" title="interface in com.nomagic.magicdraw.uml.symbols"><code>SymbolDrawListener</code></a>. These listeners are notified when some symbol is drawn in diagram.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="SymbolDrawListener.html" title="interface in com.nomagic.magicdraw.uml.symbols"><code>SymbolDrawListener</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener)">addSymbolDrawListener</a><wbr/>(<a href="SymbolDrawListener.html" title="interface in com.nomagic.magicdraw.uml.symbols">SymbolDrawListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers listener for symbols adding during draw operation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2)">addSymbolDrawListener</a><wbr/>(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2 listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers listener for symbols adding during draw operation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SymbolDrawNotification.html" title="class in com.nomagic.magicdraw.uml.symbols">SymbolDrawNotification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSymbolDrawNotification(com.nomagic.magicdraw.core.Project)">getSymbolDrawNotification</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a shared instance of this manager for given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener)">removeSymbolDrawListener</a><wbr/>(<a href="SymbolDrawListener.html" title="interface in com.nomagic.magicdraw.uml.symbols">SymbolDrawListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregisters listener for symbols adding during draw operation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2)">removeSymbolDrawListener</a><wbr/>(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2 listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregisters listener for symbols adding during draw operation.</div>
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
<section class="detail" id="addSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener)">
<h3>addSymbolDrawListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSymbolDrawListener</span><wbr/><span class="parameters">(<a href="SymbolDrawListener.html" title="interface in com.nomagic.magicdraw.uml.symbols">SymbolDrawListener</a> listener)</span></div>
<div class="block">Registers listener for symbols adding during draw operation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the listener to register.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2)">
<h3>addSymbolDrawListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSymbolDrawListener</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2 listener)</span></div>
<div class="block">Registers listener for symbols adding during draw operation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the listener to register.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener)">
<h3>removeSymbolDrawListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeSymbolDrawListener</span><wbr/><span class="parameters">(<a href="SymbolDrawListener.html" title="interface in com.nomagic.magicdraw.uml.symbols">SymbolDrawListener</a> listener)</span></div>
<div class="block">Unregisters listener for symbols adding during draw operation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the listener to unregister.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSymbolDrawListener(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2)">
<h3>removeSymbolDrawListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeSymbolDrawListener</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.SymbolDrawListener2 listener)</span></div>
<div class="block">Unregisters listener for symbols adding during draw operation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the listener to unregister.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSymbolDrawNotification(com.nomagic.magicdraw.core.Project)">
<h3>getSymbolDrawNotification</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="SymbolDrawNotification.html" title="class in com.nomagic.magicdraw.uml.symbols">SymbolDrawNotification</a></span> <span class="element-name">getSymbolDrawNotification</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns a shared instance of this manager for given project. Every project has its own notification manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to get manager for.</dd>
<dt>Returns:</dt>
<dd>manager.</dd>
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
