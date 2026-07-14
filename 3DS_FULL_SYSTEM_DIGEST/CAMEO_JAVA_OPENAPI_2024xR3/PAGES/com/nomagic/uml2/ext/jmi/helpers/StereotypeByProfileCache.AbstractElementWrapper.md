# JAVA OPENAPI: StereotypeByProfileCache.AbstractElementWrapper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/jmi/helpers/StereotypeByProfileCache.AbstractElementWrapper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/StereotypeByProfileCache.AbstractElementWrapper.html`
- source_sha256: `f041d367e4b3f987f7fab5d1e4f8ec9e0efff392fc7c243597b835281a31668b`
- captured_utc: `2026-07-14T16:56:15.831686+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class StereotypeByProfileCache.AbstractElementWrapper<ELEMENT extends [Element](../../magicdraw/classes/mdkernel/Element.html)>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache.AbstractElementWrapper<ELEMENT>

Direct Known Subclasses:
`[StereotypeByProfileCache.AbstractEnumerationWrapper](StereotypeByProfileCache.AbstractEnumerationWrapper.html)`, `[StereotypeByProfileCache.AbstractStereotypeWrapper](StereotypeByProfileCache.AbstractStereotypeWrapper.html)`

Enclosing class:
[StereotypeByProfileCache](StereotypeByProfileCache.html)

protected abstract static classStereotypeByProfileCache.AbstractElementWrapper<ELEMENT extends [Element](../../magicdraw/classes/mdkernel/Element.html)>
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[AbstractElementWrapper](#%3Cinit%3E(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache))([StereotypeByProfileCache](StereotypeByProfileCache.html) cache)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[clear](#clear())()`

`protected abstract [ELEMENT](StereotypeByProfileCache.AbstractElementWrapper.html)`
`[getElement](#getElement(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache,java.lang.String))([StereotypeByProfileCache](StereotypeByProfileCache.html) cache,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`

`protected [ELEMENT](StereotypeByProfileCache.AbstractElementWrapper.html)`
`[getElementByName](#getElementByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractElementWrapper
protected AbstractElementWrapper([StereotypeByProfileCache](StereotypeByProfileCache.html) cache)
 ============ METHOD DETAIL ========== 
Method Details
getElementByName
@CheckForNullprotected [ELEMENT](StereotypeByProfileCache.AbstractElementWrapper.html) getElementByName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
getElement
protected abstract [ELEMENT](StereotypeByProfileCache.AbstractElementWrapper.html) getElement([StereotypeByProfileCache](StereotypeByProfileCache.html) cache,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
clear
protected void clear()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class StereotypeByProfileCache.AbstractElementWrapper">Class StereotypeByProfileCache.AbstractElementWrapper&lt;ELEMENT extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache.AbstractElementWrapper&lt;ELEMENT&gt;</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="StereotypeByProfileCache.AbstractEnumerationWrapper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache.AbstractEnumerationWrapper</a></code>, <code><a href="StereotypeByProfileCache.AbstractStereotypeWrapper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache.AbstractStereotypeWrapper</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="StereotypeByProfileCache.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">protected abstract static class </span><span class="element-name type-name-label">StereotypeByProfileCache.AbstractElementWrapper&lt;ELEMENT extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache)">AbstractElementWrapper</a><wbr/>(<a href="StereotypeByProfileCache.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache</a> cache)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clear()">clear</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract <a href="StereotypeByProfileCache.AbstractElementWrapper.html" title="type parameter in StereotypeByProfileCache.AbstractElementWrapper">ELEMENT</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElement(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache,java.lang.String)">getElement</a><wbr/>(<a href="StereotypeByProfileCache.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache</a> cache,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="StereotypeByProfileCache.AbstractElementWrapper.html" title="type parameter in StereotypeByProfileCache.AbstractElementWrapper">ELEMENT</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementByName(java.lang.String)">getElementByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache)">
<h3>AbstractElementWrapper</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">AbstractElementWrapper</span><wbr/><span class="parameters">(<a href="StereotypeByProfileCache.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache</a> cache)</span></div>
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
<section class="detail" id="getElementByName(java.lang.String)">
<h3>getElementByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="StereotypeByProfileCache.AbstractElementWrapper.html" title="type parameter in StereotypeByProfileCache.AbstractElementWrapper">ELEMENT</a></span> <span class="element-name">getElementByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
</section>
</li>
<li>
<section class="detail" id="getElement(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache,java.lang.String)">
<h3>getElement</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type"><a href="StereotypeByProfileCache.AbstractElementWrapper.html" title="type parameter in StereotypeByProfileCache.AbstractElementWrapper">ELEMENT</a></span> <span class="element-name">getElement</span><wbr/><span class="parameters">(<a href="StereotypeByProfileCache.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache</a> cache,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
</section>
</li>
<li>
<section class="detail" id="clear()">
<h3>clear</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">clear</span>()</div>
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
