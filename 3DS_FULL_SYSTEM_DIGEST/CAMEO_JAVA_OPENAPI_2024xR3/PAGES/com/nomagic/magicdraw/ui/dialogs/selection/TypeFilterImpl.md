# JAVA OPENAPI: TypeFilterImpl (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/dialogs/selection/TypeFilterImpl.html
- source_path: `com/nomagic/magicdraw/ui/dialogs/selection/TypeFilterImpl.html`
- source_sha256: `808b817b87bc7bfb3ec3971d9f0cae0336f2219bf99494cd1097dbd5d27af770`
- captured_utc: `2026-07-14T16:55:52.180422+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dialogs.selection](package-summary.html)

## Class TypeFilterImpl

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.dialogs.selection.TypeFilterImpl

All Implemented Interfaces:
`[TypeFilter](TypeFilter.html)`, `com.nomagic.magicdraw.ui.ElementFilter`

@OpenApiAllpublic classTypeFilterImpl
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [TypeFilter](TypeFilter.html)

Default [`TypeFilter`](TypeFilter.html) implementation.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TypeFilterImpl](#%3Cinit%3E())()`
Constructor.
`[TypeFilterImpl](#%3Cinit%3E(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> types)`
Constructor.
`[TypeFilterImpl](#%3Cinit%3E(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) all,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) restricted)`
An utility constructor for compatibility with old approach when all and restricted types were used.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`final boolean`
`[accept](#accept(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../uml/BaseElement.html) obj)`
Tests element to satisfy filter condition.
`boolean`
`[accept](#accept(com.nomagic.magicdraw.uml.BaseElement,boolean))([BaseElement](../../../uml/BaseElement.html) baseElement,
 boolean checkType)`
Tests element to satisfy filter condition.
`protected boolean`
`[acceptByType](#acceptByType(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> types,
 [BaseElement](../../../uml/BaseElement.html) baseElement)`
Test for acceptable element type.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?>`
`[getTypes](#getTypes())()`
Get the acceptable element types.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TypeFilterImpl
public TypeFilterImpl()
Constructor.
 Any element will be accepted
TypeFilterImpl
public TypeFilterImpl(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> types)
Constructor.
Parameters:
`types` - acceptable types. Can be null.
TypeFilterImpl
public TypeFilterImpl(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) all,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) restricted)
An utility constructor for compatibility with old approach when all and restricted types were used.
 It uses "restricted" types if they are not null, otherwise "all" types are used.
Parameters:
`all` - all types
`restricted` - restricted types.
 ============ METHOD DETAIL ========== 
Method Details
getTypes
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> getTypes()
Description copied from interface: `[TypeFilter](TypeFilter.html#getTypes())`
Get the acceptable element types.
Specified by:
`[getTypes](TypeFilter.html#getTypes())` in interface `[TypeFilter](TypeFilter.html)`
Returns:
acceptable element types. If null - all element types are accepted.
accept
public final boolean accept([BaseElement](../../../uml/BaseElement.html) obj)
Description copied from interface: `com.nomagic.magicdraw.ui.ElementFilter`
Tests element to satisfy filter condition.
Specified by:
`accept` in interface `com.nomagic.magicdraw.ui.ElementFilter`
Parameters:
`obj` - element.
Returns:
true if obj satisfies filter condition otherwise false.
accept
public boolean accept([BaseElement](../../../uml/BaseElement.html) baseElement,
 boolean checkType)
Description copied from interface: `[TypeFilter](TypeFilter.html#accept(com.nomagic.magicdraw.uml.BaseElement,boolean))`
Tests element to satisfy filter condition.
Specified by:
`[accept](TypeFilter.html#accept(com.nomagic.magicdraw.uml.BaseElement,boolean))` in interface `[TypeFilter](TypeFilter.html)`
Parameters:
`baseElement` - element.
`checkType` - check object type
Returns:
true if obj satisfies filter condition otherwise false.
acceptByType
protected boolean acceptByType(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> types,
 [BaseElement](../../../uml/BaseElement.html) baseElement)
Test for acceptable element type.
Parameters:
`types` - acceptable types. Null means ANY type
`baseElement` - element to be tested. Can not be null.
Returns:
true if tested element is acceptable.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dialogs.selection</a></div>
<h1 class="title" title="Class TypeFilterImpl">Class TypeFilterImpl</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dialogs.selection.TypeFilterImpl</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a></code>, <code>com.nomagic.magicdraw.ui.ElementFilter</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TypeFilterImpl</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a></span></div>
<div class="block">Default <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection"><code>TypeFilter</code></a> implementation.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TypeFilterImpl</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection)">TypeFilterImpl</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; types)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.util.Collection)">TypeFilterImpl</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> all,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted)</code></div>
<div class="col-last even-row-color">
<div class="block">An utility constructor for compatibility with old approach when all and restricted types were used.</div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.BaseElement)">accept</a><wbr/>(<a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tests element to satisfy filter condition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.BaseElement,boolean)">accept</a><wbr/>(<a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement,
 boolean checkType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tests element to satisfy filter condition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#acceptByType(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">acceptByType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; types,
 <a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Test for acceptable element type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypes()">getTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the acceptable element types.</div>
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
<h3>TypeFilterImpl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TypeFilterImpl</span>()</div>
<div class="block">Constructor.
 Any element will be accepted</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection)">
<h3>TypeFilterImpl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TypeFilterImpl</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; types)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>types</code> - acceptable types. Can be null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.util.Collection)">
<h3>TypeFilterImpl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TypeFilterImpl</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> all,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted)</span></div>
<div class="block">An utility constructor for compatibility with old approach when all and restricted types were used.
 It uses "restricted" types if they are not null, otherwise "all" types are used.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>all</code> - all types</dd>
<dd><code>restricted</code> - restricted types.</dd>
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
<section class="detail" id="getTypes()">
<h3>getTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</span> <span class="element-name">getTypes</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="TypeFilter.html#getTypes()">TypeFilter</a></code></span></div>
<div class="block">Get the acceptable element types.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TypeFilter.html#getTypes()">getTypes</a></code> in interface <code><a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a></code></dd>
<dt>Returns:</dt>
<dd>acceptable element types. If null - all element types are accepted.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.BaseElement)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.ui.ElementFilter</code></span></div>
<div class="block">Tests element to satisfy filter condition.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>accept</code> in interface <code>com.nomagic.magicdraw.ui.ElementFilter</code></dd>
<dt>Parameters:</dt>
<dd><code>obj</code> - element.</dd>
<dt>Returns:</dt>
<dd>true if obj satisfies filter condition otherwise false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.BaseElement,boolean)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement,
 boolean checkType)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="TypeFilter.html#accept(com.nomagic.magicdraw.uml.BaseElement,boolean)">TypeFilter</a></code></span></div>
<div class="block">Tests element to satisfy filter condition.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="TypeFilter.html#accept(com.nomagic.magicdraw.uml.BaseElement,boolean)">accept</a></code> in interface <code><a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>baseElement</code> - element.</dd>
<dd><code>checkType</code> - check object type</dd>
<dt>Returns:</dt>
<dd>true if obj satisfies filter condition otherwise false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="acceptByType(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">
<h3>acceptByType</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">acceptByType</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; types,
 <a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</span></div>
<div class="block">Test for acceptable element type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>types</code> - acceptable types. Null means ANY type</dd>
<dd><code>baseElement</code> - element to be tested. Can not be null.</dd>
<dt>Returns:</dt>
<dd>true if tested element is acceptable.</dd>
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
