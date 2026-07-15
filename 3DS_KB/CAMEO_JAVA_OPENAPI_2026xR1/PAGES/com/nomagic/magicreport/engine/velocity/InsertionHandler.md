# JAVA OPENAPI: InsertionHandler (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/velocity/InsertionHandler.html
- source_path: `com/nomagic/magicreport/engine/velocity/InsertionHandler.html`
- source_sha256: `c1fc73190abe74bb38c5d59074b019624b2b78f49802d6d06b20fd831e5c04ab`
- captured_utc: `2026-07-14T16:46:13.239977+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.velocity](package-summary.html)

## Class InsertionHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.engine.velocity.InsertionHandler

All Implemented Interfaces:
`[IReferenceInsertionHandler](../IReferenceInsertionHandler.html)`

@OpenApiAllpublic classInsertionHandler
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [IReferenceInsertionHandler](../IReferenceInsertionHandler.html)

Reference 'Stream insertion' event handler. Called with object that will be inserted into stream by following
 this logic:

````java
if (value==null) return reference;
    else return 
IFormatter.format(Object)
;
````

Please return an Object that will toString() nicely :)

Since:
Jun 19, 2007

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [ITemplateEngine](../ITemplateEngine.html)`
`[engine](#engine)`
Reference to template engine.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[InsertionHandler](#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine))([ITemplateEngine](../ITemplateEngine.html) engine)`
Create an handler with [`DefaultFormatter`](../../format/DefaultFormatter.html).
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`protected [IFormatter](../../format/IFormatter.html)`
`[createFormatter](#createFormatter(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<[ITemplateEngine](../ITemplateEngine.html)> engineClass)`
Deprecated.
the formatter is no longer determined by Class [`ITemplateEngine`](../ITemplateEngine.html).
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[referenceInsert](#referenceInsert(java.lang.String,java.lang.Object,java.util.Properties))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
A call-back which is executed during Velocity merge before a reference value is inserted into the output
 stream.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
engine
protected [ITemplateEngine](../ITemplateEngine.html) engine
Reference to template engine.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
InsertionHandler
public InsertionHandler([ITemplateEngine](../ITemplateEngine.html) engine)
Create an handler with [`DefaultFormatter`](../../format/DefaultFormatter.html).
Parameters:
`engine` - owner engine
 ============ METHOD DETAIL ========== 
Method Details
createFormatter
protected [IFormatter](../../format/IFormatter.html) createFormatter([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<[ITemplateEngine](../ITemplateEngine.html)> engineClass)
Deprecated.
the formatter is no longer determined by Class [`ITemplateEngine`](../ITemplateEngine.html). It will be created directly
 from [`ITemplateEngine.getFormatter()`](../ITemplateEngine.html#getFormatter()).
Determine and create the formatter base on template engine.
Parameters:
`engineClass` - the template engine
Returns:
the formatter
referenceInsert
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) referenceInsert([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
A call-back which is executed during Velocity merge before a reference value is inserted into the output
 stream. All registered ReferenceInsertionEventHandlers are called in sequence. If no
 ReferenceInsertionEventHandlers are are registered then reference value is inserted into the output stream
 as is.
Specified by:
`[referenceInsert](../IReferenceInsertionHandler.html#referenceInsert(java.lang.String,java.lang.Object,java.util.Properties))` in interface `[IReferenceInsertionHandler](../IReferenceInsertionHandler.html)`
Parameters:
`reference` - Reference from template about to be inserted.
`value` - Value about to be inserted (after its `toString()` method is called).
`properties` - the engine properties
Returns:
Object on which `toString()` should be called for output.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.velocity</a></div>
<h1 class="title" title="Class InsertionHandler">Class InsertionHandler</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.engine.velocity.InsertionHandler</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine">IReferenceInsertionHandler</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">InsertionHandler</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="../IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine">IReferenceInsertionHandler</a></span></div>
<div class="block">Reference 'Stream insertion' event handler. Called with object that will be inserted into stream by following
 this logic:
 <br/>
<pre>
    if (value==null) return reference;
    else return <a href="../../format/IFormatter.html#format(java.lang.Object)"><code>IFormatter.format(Object)</code></a>;
 </pre>
 
 Please return an Object that will toString() nicely :)</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 19, 2007</dd>
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
<div class="col-first even-row-color"><code>protected <a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#engine">engine</a></code></div>
<div class="col-last even-row-color">
<div class="block">Reference to template engine.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine)">InsertionHandler</a><wbr/>(<a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> engine)</code></div>
<div class="col-last even-row-color">
<div class="block">Create an handler with <a href="../../format/DefaultFormatter.html" title="class in com.nomagic.magicreport.format"><code>DefaultFormatter</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a href="../../format/IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createFormatter(java.lang.Class)">createFormatter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;<a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a>&gt; engineClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">the formatter is no longer determined by Class <a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine"><code>ITemplateEngine</code></a>.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#referenceInsert(java.lang.String,java.lang.Object,java.util.Properties)">referenceInsert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A call-back which is executed during Velocity merge before a reference value is inserted into the output
 stream.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="engine">
<h3>engine</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></span> <span class="element-name">engine</span></div>
<div class="block">Reference to template engine.</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.ITemplateEngine)">
<h3>InsertionHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">InsertionHandler</span><wbr/><span class="parameters">(<a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> engine)</span></div>
<div class="block">Create an handler with <a href="../../format/DefaultFormatter.html" title="class in com.nomagic.magicreport.format"><code>DefaultFormatter</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>engine</code> - owner engine</dd>
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
<section class="detail" id="createFormatter(java.lang.Class)">
<h3>createFormatter</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../format/IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></span> <span class="element-name">createFormatter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;<a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a>&gt; engineClass)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">the formatter is no longer determined by Class <a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine"><code>ITemplateEngine</code></a>. It will be created directly
             from <a href="../ITemplateEngine.html#getFormatter()"><code>ITemplateEngine.getFormatter()</code></a>.</div>
</div>
<div class="block">Determine and create the formatter base on template engine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>engineClass</code> - the template engine</dd>
<dt>Returns:</dt>
<dd>the formatter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="referenceInsert(java.lang.String,java.lang.Object,java.util.Properties)">
<h3>referenceInsert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">referenceInsert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">A call-back which is executed during Velocity merge before a reference value is inserted into the output
 stream. All registered ReferenceInsertionEventHandlers are called in sequence. If no
 ReferenceInsertionEventHandlers are are registered then reference value is inserted into the output stream
 as is.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IReferenceInsertionHandler.html#referenceInsert(java.lang.String,java.lang.Object,java.util.Properties)">referenceInsert</a></code> in interface <code><a href="../IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine">IReferenceInsertionHandler</a></code></dd>
<dt>Parameters:</dt>
<dd><code>reference</code> - Reference from template about to be inserted.</dd>
<dd><code>value</code> - Value about to be inserted (after its <code>toString()</code> method is called).</dd>
<dd><code>properties</code> - the engine properties</dd>
<dt>Returns:</dt>
<dd>Object on which <code>toString()</code> should be called for output.</dd>
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
