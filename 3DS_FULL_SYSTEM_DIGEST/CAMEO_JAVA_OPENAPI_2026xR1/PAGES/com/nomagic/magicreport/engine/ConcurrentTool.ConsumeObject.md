# JAVA OPENAPI: ConcurrentTool.ConsumeObject (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/ConcurrentTool.ConsumeObject.html
- source_path: `com/nomagic/magicreport/engine/ConcurrentTool.ConsumeObject.html`
- source_sha256: `6e6489e30995f990e5556d16589ba218af97f920f2a1e9e8b651500831e66a48`
- captured_utc: `2026-07-14T16:46:11.751957+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Class ConcurrentTool.ConsumeObject

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.lang.ref.Reference](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>
[java.lang.ref.WeakReference](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/WeakReference.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>
com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject

Enclosing class:
`[ConcurrentTool](ConcurrentTool.html)`

@OpenApiAllpublic static classConcurrentTool.ConsumeObject
extends [WeakReference](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/WeakReference.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>

Inner class which acts as the reference for a file pending deletion.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[ConsumeObject](#%3Cinit%3E(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)`
Create consumed object.
``
`[ConsumeObject](#%3Cinit%3E(java.lang.Object%5B%5D%5B%5D))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)[][] parameters)`
Create consumed object.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)`
Indicates whether some other object is "equal to" this one.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) parameterName)`
Return value of given parameter name.
`int`
`[hashCode](#hashCode())()`
Returns a hash code value for the object.
Methods inherited from class java.lang.ref.[Reference](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html)
`[clear](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#clear()), [clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#clone()), [enqueue](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#enqueue()), [get](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#get()), [isEnqueued](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#isEnqueued()), [reachabilityFence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#reachabilityFence(java.lang.Object)), [refersTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#refersTo(T))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ConsumeObject
protected ConsumeObject([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)
Create consumed object.
Parameters:
`obj` - object the new weak reference will refer to
ConsumeObject
public ConsumeObject([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)[][] parameters)
Create consumed object. The parameters format is [position of parameter][name,value]. 

 Example: `ConsumeObject consumeObject = new ConsumeObject(new Object[][]{{"param1","value1"},{"param2","value2"});`
Parameters:
`parameters` - two dimensions parameter for consumed object
 ============ METHOD DETAIL ========== 
Method Details
getValue
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getValue([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) parameterName)
Return value of given parameter name.
Parameters:
`parameterName` - parameter name
Returns:
parameter value
hashCode
public int hashCode()
Returns a hash code value for the object. This method is supported for the benefit of hashtables such as
 those provided by
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
a hash code value for this object.
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)
Indicates whether some other object is "equal to" this one.
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Parameters:
`obj` - the reference object with which to compare.
Returns:
`true` if this object is the same as the obj argument; `false` otherwise.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Class ConcurrentTool.ConsumeObject">Class ConcurrentTool.ConsumeObject</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html" title="class or interface in java.lang.ref">java.lang.ref.Reference</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/WeakReference.html" title="class or interface in java.lang.ref">java.lang.ref.WeakReference</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;
<div class="inheritance">com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public static class </span><span class="element-name type-name-label">ConcurrentTool.ConsumeObject</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/WeakReference.html" title="class or interface in java.lang.ref">WeakReference</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span></div>
<div class="block">Inner class which acts as the reference for a file pending deletion.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Object)">ConsumeObject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color">
<div class="block">Create consumed object.</div>
</div>
<div class="col-first odd-row-color"><code> </code></div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Object%5B%5D%5B%5D)">ConsumeObject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[][] parameters)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create consumed object.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates whether some other object is "equal to" this one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(java.lang.Object)">getValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> parameterName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return value of given parameter name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a hash code value for the object.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.ref.Reference">Methods inherited from class java.lang.ref.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html" title="class or interface in java.lang.ref">Reference</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#clear()" title="class or interface in java.lang.ref">clear</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#clone()" title="class or interface in java.lang.ref">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#enqueue()" title="class or interface in java.lang.ref">enqueue</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#get()" title="class or interface in java.lang.ref">get</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#isEnqueued()" title="class or interface in java.lang.ref">isEnqueued</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#reachabilityFence(java.lang.Object)" title="class or interface in java.lang.ref">reachabilityFence</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ref/Reference.html#refersTo(T)" title="class or interface in java.lang.ref">refersTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.Object)">
<h3>ConsumeObject</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">ConsumeObject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="block">Create consumed object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - object the new weak reference will refer to</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Object[][])">
<h3>ConsumeObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ConsumeObject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[][] parameters)</span></div>
<div class="block">Create consumed object. The parameters format is [position of parameter][name,value]. <br/>
 Example: <pre><code>
    ConsumeObject consumeObject = new ConsumeObject(new Object[][]{{"param1","value1"},{"param2","value2"});
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameters</code> - two dimensions parameter for consumed object</dd>
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
<section class="detail" id="getValue(java.lang.Object)">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> parameterName)</span></div>
<div class="block">Return value of given parameter name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameterName</code> - parameter name</dd>
<dt>Returns:</dt>
<dd>parameter value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<div class="block">Returns a hash code value for the object. This method is supported for the benefit of hashtables such as
 those provided by</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>a hash code value for this object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="block">Indicates whether some other object is "equal to" this one.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Parameters:</dt>
<dd><code>obj</code> - the reference object with which to compare.</dd>
<dt>Returns:</dt>
<dd><code>true</code> if this object is the same as the obj argument; <code>false</code> otherwise.</dd>
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
