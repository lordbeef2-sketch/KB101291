# JAVA OPENAPI: StereotypeByProfileCache.AbstractStereotypeWrapper (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/jmi/helpers/StereotypeByProfileCache.AbstractStereotypeWrapper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/StereotypeByProfileCache.AbstractStereotypeWrapper.html`
- source_sha256: `d19db56076cdb13a506d13588190913c713e5d5bf9f8b30602e7aced05f6f2c4`
- captured_utc: `2026-07-14T16:46:22.291096+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class StereotypeByProfileCache.AbstractStereotypeWrapper

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache.AbstractElementWrapper](StereotypeByProfileCache.AbstractElementWrapper.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>
com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache.AbstractStereotypeWrapper

Enclosing class:
`[StereotypeByProfileCache](StereotypeByProfileCache.html)`

protected static classStereotypeByProfileCache.AbstractStereotypeWrapper
extends [StereotypeByProfileCache.AbstractElementWrapper](StereotypeByProfileCache.AbstractElementWrapper.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[AbstractStereotypeWrapper](#%3Cinit%3E())()`

`protected`
`[AbstractStereotypeWrapper](#%3Cinit%3E(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache))([StereotypeByProfileCache](StereotypeByProfileCache.html) cache)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[getElement](#getElement(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache,java.lang.String))([StereotypeByProfileCache](StereotypeByProfileCache.html) cache,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`

`protected static [Property](../../magicdraw/classes/mdkernel/Property.html)`
`[getTagByName](#getTagByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)`

`protected static [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)`
`[toBoolean](#toBoolean(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)`

`protected static [Double](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html)`
`[toDouble](#toDouble(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)`

`protected static [Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html)`
`[toInteger](#toInteger(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)`

`protected static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)`
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[StereotypeByProfileCache.AbstractElementWrapper](StereotypeByProfileCache.AbstractElementWrapper.html)
`[clear](StereotypeByProfileCache.AbstractElementWrapper.html#clear()), [getElementByName](StereotypeByProfileCache.AbstractElementWrapper.html#getElementByName(java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractStereotypeWrapper
protected AbstractStereotypeWrapper()
AbstractStereotypeWrapper
protected AbstractStereotypeWrapper([StereotypeByProfileCache](StereotypeByProfileCache.html) cache)
 ============ METHOD DETAIL ========== 
Method Details
getElement
@CheckForNullprotected [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) getElement([StereotypeByProfileCache](StereotypeByProfileCache.html) cache,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Specified by:
`[getElement](StereotypeByProfileCache.AbstractElementWrapper.html#getElement(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache,java.lang.String))` in class `[StereotypeByProfileCache.AbstractElementWrapper](StereotypeByProfileCache.AbstractElementWrapper.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
getTagByName
@CheckForNullprotected static [Property](../../magicdraw/classes/mdkernel/Property.html) getTagByName(@CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)
toInteger
@CheckForNullprotected static [Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html) toInteger(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)
toBoolean
@CheckForNullprotected static [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) toBoolean(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)
toString
@CheckForNullprotected static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)
toDouble
@CheckForNullprotected static [Double](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html) toDouble(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class StereotypeByProfileCache.AbstractStereotypeWrapper">Class StereotypeByProfileCache.AbstractStereotypeWrapper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="StereotypeByProfileCache.AbstractElementWrapper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache.AbstractElementWrapper</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache.AbstractStereotypeWrapper</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="StereotypeByProfileCache.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">protected static class </span><span class="element-name type-name-label">StereotypeByProfileCache.AbstractStereotypeWrapper</span>
<span class="extends-implements">extends <a href="StereotypeByProfileCache.AbstractElementWrapper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache.AbstractElementWrapper</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AbstractStereotypeWrapper</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>protected </code></div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache)">AbstractStereotypeWrapper</a><wbr/>(<a href="StereotypeByProfileCache.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache</a> cache)</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache,java.lang.String)">getElement</a><wbr/>(<a href="StereotypeByProfileCache.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache</a> cache,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTagByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getTagByName</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toBoolean(java.lang.Object)">toBoolean</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toDouble(java.lang.Object)">toDouble</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toInteger(java.lang.Object)">toInteger</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toString(java.lang.Object)">toString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache.AbstractElementWrapper">Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.<a href="StereotypeByProfileCache.AbstractElementWrapper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache.AbstractElementWrapper</a></h3>
<code><a href="StereotypeByProfileCache.AbstractElementWrapper.html#clear()">clear</a>, <a href="StereotypeByProfileCache.AbstractElementWrapper.html#getElementByName(java.lang.String)">getElementByName</a></code></div>
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
<h3>AbstractStereotypeWrapper</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">AbstractStereotypeWrapper</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache)">
<h3>AbstractStereotypeWrapper</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">AbstractStereotypeWrapper</span><wbr/><span class="parameters">(<a href="StereotypeByProfileCache.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache</a> cache)</span></div>
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
<section class="detail" id="getElement(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache,java.lang.String)">
<h3>getElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getElement</span><wbr/><span class="parameters">(<a href="StereotypeByProfileCache.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache</a> cache,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="StereotypeByProfileCache.AbstractElementWrapper.html#getElement(com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache,java.lang.String)">getElement</a></code> in class <code><a href="StereotypeByProfileCache.AbstractElementWrapper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache.AbstractElementWrapper</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTagByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">
<h3>getTagByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getTagByName</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
</section>
</li>
<li>
<section class="detail" id="toInteger(java.lang.Object)">
<h3>toInteger</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">toInteger</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
</section>
</li>
<li>
<section class="detail" id="toBoolean(java.lang.Object)">
<h3>toBoolean</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">toBoolean</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
</section>
</li>
<li>
<section class="detail" id="toString(java.lang.Object)">
<h3>toString</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
</section>
</li>
<li>
<section class="detail" id="toDouble(java.lang.Object)">
<h3>toDouble</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">toDouble</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
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
