# JAVA OPENAPI: VelocityContext (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/velocity/VelocityContext.html
- source_path: `com/nomagic/magicreport/engine/velocity/VelocityContext.html`
- source_sha256: `5ee4399d1f8cef77a99d5120166e89e2090f9fc991164f8792dbb4a2ecbb6e7b`
- captured_utc: `2026-07-14T16:46:13.443979+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.velocity](package-summary.html)

## Class VelocityContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.engine.velocity.VelocityContext

All Implemented Interfaces:
`[IContext](../IContext.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`

@OpenApiAllpublic classVelocityContext
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [IContext](../IContext.html)

Implementation of the [`IContext`](../IContext.html) interface for use. This implementation uses a
 `org.apache.velocity.VelocityContext` for data storage.
 `org.apache.velocity.VelocityContext` is not synchronized. If you need to share a Context between
 threads with simultaneous access for some reason, please create your own and extend the interface Context

Since:
Jun 11, 2007 10:50:15 PM
Version:
1.0 Jun 11, 2007
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.engine.velocity.VelocityContext)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[VelocityContext](#%3Cinit%3E())()`
Creates a new instance (with no inner context).
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[contextKeys](#contextKeys())()`
Finds all the keys of the entry in this context.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[]`
`[contextKeysArray](#contextKeysArray())()`
Finds all the keys of the entry in this context as array.
`org.apache.velocity.VelocityContext`
`[createContext](#createContext())()`
Create a velocity context from template context.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)`
Gets the value corresponding to the provided key from the context.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[put](#put(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Adds a name/value pair to the context.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[remove](#remove(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)`
Removes the value associated with the specified key from the context.
`void`
`[removeAll](#removeAll())()`
Removes all items from this context.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
VelocityContext
public VelocityContext()
Creates a new instance (with no inner context).
 ============ METHOD DETAIL ========== 
Method Details
get
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) get([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)
Gets the value corresponding to the provided key from the context.
Specified by:
`[get](../IContext.html#get(java.lang.String))` in interface `[IContext](../IContext.html)`
Parameters:
`key` - The name of the desired value.
Returns:
The value corresponding to the provided key.
remove
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) remove([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)
Removes the value associated with the specified key from the context.
Specified by:
`[remove](../IContext.html#remove(java.lang.String))` in interface `[IContext](../IContext.html)`
Parameters:
`key` - The name of the value to remove.
Returns:
The value that the key was mapped to, or null if unmapped.
put
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) put([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Adds a name/value pair to the context.
Specified by:
`[put](../IContext.html#put(java.lang.String,java.lang.Object))` in interface `[IContext](../IContext.html)`
Parameters:
`key` - The name to key the provided value with.
`value` - The corresponding value.
Returns:
The old object or null if there was no old object.
removeAll
public void removeAll()
Removes all items from this context.
Specified by:
`[removeAll](../IContext.html#removeAll())` in interface `[IContext](../IContext.html)`
contextKeys
public [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> contextKeys()
Finds all the keys of the entry in this context.
Specified by:
`[contextKeys](../IContext.html#contextKeys())` in interface `[IContext](../IContext.html)`
Returns:
an Iterator of all the key of the entry in this context.
contextKeysArray
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] contextKeysArray()
Finds all the keys of the entry in this context as array.
Specified by:
`[contextKeysArray](../IContext.html#contextKeysArray())` in interface `[IContext](../IContext.html)`
Returns:
an array of all the key of the entry in this context.
createContext
public org.apache.velocity.VelocityContext createContext()
Create a velocity context from template context.
Returns:
a velocity context

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.velocity</a></div>
<h1 class="title" title="Class VelocityContext">Class VelocityContext</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.engine.velocity.VelocityContext</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">VelocityContext</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="../IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></span></div>
<div class="block">Implementation of the <a href="../IContext.html" title="interface in com.nomagic.magicreport.engine"><code>IContext</code></a> interface for use. This implementation uses a
 <code>org.apache.velocity.VelocityContext</code> for data storage.
 <code>org.apache.velocity.VelocityContext</code> is not synchronized. If you need to share a Context between
 threads with simultaneous access for some reason, please create your own and extend the interface Context</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 11, 2007 10:50:15 PM</dd>
<dt>Version:</dt>
<dd>1.0 Jun 11, 2007</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.engine.velocity.VelocityContext">Serialized Form</a></li>
</ul>
</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">VelocityContext</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance (with no inner context).</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#contextKeys()">contextKeys</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds all the keys of the entry in this context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#contextKeysArray()">contextKeysArray</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds all the keys of the entry in this context as array.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.apache.velocity.VelocityContext</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createContext()">createContext</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create a velocity context from template context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the value corresponding to the provided key from the context.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#put(java.lang.String,java.lang.Object)">put</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a name/value pair to the context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(java.lang.String)">remove</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the value associated with the specified key from the context.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAll()">removeAll</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all items from this context.</div>
</div>
</div>
</div>
</div>
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
<h3>VelocityContext</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VelocityContext</span>()</div>
<div class="block">Creates a new instance (with no inner context).</div>
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
<section class="detail" id="get(java.lang.String)">
<h3>get</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div class="block">Gets the value corresponding to the provided key from the context.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IContext.html#get(java.lang.String)">get</a></code> in interface <code><a href="../IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></code></dd>
<dt>Parameters:</dt>
<dd><code>key</code> - The name of the desired value.</dd>
<dt>Returns:</dt>
<dd>The value corresponding to the provided key.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(java.lang.String)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">remove</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div class="block">Removes the value associated with the specified key from the context.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IContext.html#remove(java.lang.String)">remove</a></code> in interface <code><a href="../IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></code></dd>
<dt>Parameters:</dt>
<dd><code>key</code> - The name of the value to remove.</dd>
<dt>Returns:</dt>
<dd>The value that the key was mapped to, or null if unmapped.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="put(java.lang.String,java.lang.Object)">
<h3>put</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">put</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Adds a name/value pair to the context.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IContext.html#put(java.lang.String,java.lang.Object)">put</a></code> in interface <code><a href="../IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></code></dd>
<dt>Parameters:</dt>
<dd><code>key</code> - The name to key the provided value with.</dd>
<dd><code>value</code> - The corresponding value.</dd>
<dt>Returns:</dt>
<dd>The old object or null if there was no old object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAll()">
<h3>removeAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAll</span>()</div>
<div class="block">Removes all items from this context.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IContext.html#removeAll()">removeAll</a></code> in interface <code><a href="../IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="contextKeys()">
<h3>contextKeys</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">contextKeys</span>()</div>
<div class="block">Finds all the keys of the entry in this context.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IContext.html#contextKeys()">contextKeys</a></code> in interface <code><a href="../IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></code></dd>
<dt>Returns:</dt>
<dd>an Iterator of all the key of the entry in this context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="contextKeysArray()">
<h3>contextKeysArray</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">contextKeysArray</span>()</div>
<div class="block">Finds all the keys of the entry in this context as array.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IContext.html#contextKeysArray()">contextKeysArray</a></code> in interface <code><a href="../IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></code></dd>
<dt>Returns:</dt>
<dd>an array of all the key of the entry in this context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createContext()">
<h3>createContext</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.apache.velocity.VelocityContext</span> <span class="element-name">createContext</span>()</div>
<div class="block">Create a velocity context from template context.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a velocity context</dd>
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
