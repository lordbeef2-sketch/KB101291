# JAVA OPENAPI: SelectionProvider (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/ui/SelectionProvider.html
- source_path: `com/nomagic/magicdraw/ui/SelectionProvider.html`
- source_sha256: `60fbe544af0812b0c9a1b007a3e1f0ac023f4c211f131e2638da527ffb3731f1`
- captured_utc: `2026-07-14T16:52:01.317740+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Class SelectionProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.SelectionProvider

@OpenApiAllpublic classSelectionProvider
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Selection provider to manage selected elements in browser and diagrams

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static interface`
`[SelectionProvider.Selection](SelectionProvider.Selection.html)`

`static class`
`[SelectionProvider.SelectionChangedEvent](SelectionProvider.SelectionChangedEvent.html)`
An event which indicates selection change.
`static interface`
`[SelectionProvider.SelectionChangedListener](SelectionProvider.SelectionChangedListener.html)`
Selection changed listener
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [SelectionProvider.Selection](SelectionProvider.Selection.html)`
`[selection](#selection)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SelectionProvider](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addSelectionChangedListener](#addSelectionChangedListener(com.nomagic.magicdraw.ui.SelectionProvider.SelectionChangedListener))([SelectionProvider.SelectionChangedListener](SelectionProvider.SelectionChangedListener.html) listener)`
Adds selection changed listener
`protected void`
`[fireSelectionChanged](#fireSelectionChanged(com.nomagic.magicdraw.ui.SelectionProvider.SelectionChangedEvent))([SelectionProvider.SelectionChangedEvent](SelectionProvider.SelectionChangedEvent.html) event)`

`static [SelectionProvider](SelectionProvider.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Returns selection provider
`final [BaseElement](../uml/BaseElement.html)`
`[getMainElement](#getMainElement())()`
Returns main element
`final [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)>`
`[getSelectedElements](#getSelectedElements())()`
Returns selected elements
`final [SelectionProvider.Selection](SelectionProvider.Selection.html)`
`[getSelection](#getSelection())()`

`void`
`[removeSelectionChangedListener](#removeSelectionChangedListener(com.nomagic.magicdraw.ui.SelectionProvider.SelectionChangedListener))([SelectionProvider.SelectionChangedListener](SelectionProvider.SelectionChangedListener.html) listener)`
Removes selection changed listener
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
selection
protected [SelectionProvider.Selection](SelectionProvider.Selection.html) selection
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SelectionProvider
public SelectionProvider()
 ============ METHOD DETAIL ========== 
Method Details
getInstance
public static [SelectionProvider](SelectionProvider.html) getInstance([Project](../core/Project.html) project)
Returns selection provider
Parameters:
`project` - where are selected elements
Returns:
selection provider
getSelection
public final [SelectionProvider.Selection](SelectionProvider.Selection.html) getSelection()
Returns:
active selection
getSelectedElements
public final [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> getSelectedElements()
Returns selected elements
getMainElement
@CheckForNullpublic final [BaseElement](../uml/BaseElement.html) getMainElement()
Returns main element
addSelectionChangedListener
public void addSelectionChangedListener([SelectionProvider.SelectionChangedListener](SelectionProvider.SelectionChangedListener.html) listener)
Adds selection changed listener
Parameters:
`listener` - to add
removeSelectionChangedListener
public void removeSelectionChangedListener([SelectionProvider.SelectionChangedListener](SelectionProvider.SelectionChangedListener.html) listener)
Removes selection changed listener
Parameters:
`listener` - to remove
fireSelectionChanged
protected void fireSelectionChanged([SelectionProvider.SelectionChangedEvent](SelectionProvider.SelectionChangedEvent.html) event)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Class SelectionProvider">Class SelectionProvider</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.SelectionProvider</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SelectionProvider</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Selection provider to manage selected elements in browser and diagrams</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SelectionProvider.Selection.html" title="interface in com.nomagic.magicdraw.ui">SelectionProvider.Selection</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SelectionProvider.SelectionChangedEvent.html" title="class in com.nomagic.magicdraw.ui">SelectionProvider.SelectionChangedEvent</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An event which indicates selection change.</div>
</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SelectionProvider.SelectionChangedListener.html" title="interface in com.nomagic.magicdraw.ui">SelectionProvider.SelectionChangedListener</a></code></div>
<div class="col-last even-row-color">
<div class="block">Selection changed listener</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected <a href="SelectionProvider.Selection.html" title="interface in com.nomagic.magicdraw.ui">SelectionProvider.Selection</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#selection">selection</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SelectionProvider</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSelectionChangedListener(com.nomagic.magicdraw.ui.SelectionProvider.SelectionChangedListener)">addSelectionChangedListener</a><wbr/>(<a href="SelectionProvider.SelectionChangedListener.html" title="interface in com.nomagic.magicdraw.ui">SelectionProvider.SelectionChangedListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds selection changed listener</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireSelectionChanged(com.nomagic.magicdraw.ui.SelectionProvider.SelectionChangedEvent)">fireSelectionChanged</a><wbr/>(<a href="SelectionProvider.SelectionChangedEvent.html" title="class in com.nomagic.magicdraw.ui">SelectionProvider.SelectionChangedEvent</a> event)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SelectionProvider.html" title="class in com.nomagic.magicdraw.ui">SelectionProvider</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.core.Project)">getInstance</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns selection provider</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMainElement()">getMainElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns main element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedElements()">getSelectedElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns selected elements</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="SelectionProvider.Selection.html" title="interface in com.nomagic.magicdraw.ui">SelectionProvider.Selection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelection()">getSelection</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSelectionChangedListener(com.nomagic.magicdraw.ui.SelectionProvider.SelectionChangedListener)">removeSelectionChangedListener</a><wbr/>(<a href="SelectionProvider.SelectionChangedListener.html" title="interface in com.nomagic.magicdraw.ui">SelectionProvider.SelectionChangedListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes selection changed listener</div>
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
<section class="detail" id="selection">
<h3>selection</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="SelectionProvider.Selection.html" title="interface in com.nomagic.magicdraw.ui">SelectionProvider.Selection</a></span> <span class="element-name">selection</span></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>SelectionProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SelectionProvider</span>()</div>
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
<section class="detail" id="getInstance(com.nomagic.magicdraw.core.Project)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SelectionProvider.html" title="class in com.nomagic.magicdraw.ui">SelectionProvider</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns selection provider</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - where are selected elements</dd>
<dt>Returns:</dt>
<dd>selection provider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelection()">
<h3>getSelection</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a href="SelectionProvider.Selection.html" title="interface in com.nomagic.magicdraw.ui">SelectionProvider.Selection</a></span> <span class="element-name">getSelection</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>active selection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedElements()">
<h3>getSelectedElements</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getSelectedElements</span>()</div>
<div class="block">Returns selected elements</div>
</section>
</li>
<li>
<section class="detail" id="getMainElement()">
<h3>getMainElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getMainElement</span>()</div>
<div class="block">Returns main element</div>
</section>
</li>
<li>
<section class="detail" id="addSelectionChangedListener(com.nomagic.magicdraw.ui.SelectionProvider.SelectionChangedListener)">
<h3>addSelectionChangedListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSelectionChangedListener</span><wbr/><span class="parameters">(<a href="SelectionProvider.SelectionChangedListener.html" title="interface in com.nomagic.magicdraw.ui">SelectionProvider.SelectionChangedListener</a> listener)</span></div>
<div class="block">Adds selection changed listener</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSelectionChangedListener(com.nomagic.magicdraw.ui.SelectionProvider.SelectionChangedListener)">
<h3>removeSelectionChangedListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeSelectionChangedListener</span><wbr/><span class="parameters">(<a href="SelectionProvider.SelectionChangedListener.html" title="interface in com.nomagic.magicdraw.ui">SelectionProvider.SelectionChangedListener</a> listener)</span></div>
<div class="block">Removes selection changed listener</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - to remove</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireSelectionChanged(com.nomagic.magicdraw.ui.SelectionProvider.SelectionChangedEvent)">
<h3>fireSelectionChanged</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">fireSelectionChanged</span><wbr/><span class="parameters">(<a href="SelectionProvider.SelectionChangedEvent.html" title="class in com.nomagic.magicdraw.ui">SelectionProvider.SelectionChangedEvent</a> event)</span></div>
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
