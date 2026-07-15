# JAVA OPENAPI: IInvalidReferenceHandler (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/IInvalidReferenceHandler.html
- source_path: `com/nomagic/magicreport/engine/IInvalidReferenceHandler.html`
- source_sha256: `fa41dcbfa0d5259d70af94353fd46be7ffdf09954deeabd905a764b1298616e4`
- captured_utc: `2026-07-14T16:58:37.133283+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Interface IInvalidReferenceHandler

@OpenApiAllpublic interfaceIInvalidReferenceHandler
This interface is used for handling reference tags, that does not include in the API of the object , which is
 put into the context of velocity.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[invalidMethod](#invalidMethod(java.lang.String,java.lang.Object,java.lang.String,java.util.Properties))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
Handle reference method and return the proper value.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[invalidProperty](#invalidProperty(java.lang.String,java.lang.Object,java.lang.String,java.util.Properties))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) property,
 [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
Invoke when getter method of `object` is not defined.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[invalidReference](#invalidReference(java.lang.String,java.lang.Object,java.lang.String,java.util.Properties))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) property,
 [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
Handle reference tag and return the proper value.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[methodException](#methodException(java.lang.Class,java.lang.String,java.lang.Exception,java.util.Properties))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e,
 [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
Handler a method call exception.

============ METHOD DETAIL ========== 
Method Details
methodException
[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) methodException([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e,
 [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
Handler a method call exception.
Parameters:
`clazz` - the class of the object the method is being applied to
`method` - the method
`e` - the thrown exception
`properties` - the engine properties
Returns:
return value
invalidProperty
[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) invalidProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) property,
 [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
Invoke when getter method of `object` is not defined.
Parameters:
`reference` - string with complete reference
`object` - the object referred to, or null if not found
`property` - the property name from the reference
`properties` - the engine properties
Returns:
return value
invalidReference
[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) invalidReference([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) property,
 [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
Handle reference tag and return the proper value.
Parameters:
`reference` - string with complete reference
`object` - the object referred to, or null if not found
`property` - the property name from the reference
`properties` - the engine properties
Returns:
return value
invalidMethod
[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) invalidMethod([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
Handle reference method and return the proper value.
Parameters:
`reference` - string with complete reference
`object` - the object referred to, or null if not found
`method` - the property name from the reference
`properties` - the engine properties
Returns:
return value

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Interface IInvalidReferenceHandler">Interface IInvalidReferenceHandler</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IInvalidReferenceHandler</span></div>
<div class="block">This interface is used for handling reference tags, that does not include in the API of the object , which is
 put into the context of velocity.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#invalidMethod(java.lang.String,java.lang.Object,java.lang.String,java.util.Properties)">invalidMethod</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Handle reference method and return the proper value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#invalidProperty(java.lang.String,java.lang.Object,java.lang.String,java.util.Properties)">invalidProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Invoke when getter method of <code>object</code> is not defined.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#invalidReference(java.lang.String,java.lang.Object,java.lang.String,java.util.Properties)">invalidReference</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Handle reference tag and return the proper value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#methodException(java.lang.Class,java.lang.String,java.lang.Exception,java.util.Properties)">methodException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Handler a method call exception.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="methodException(java.lang.Class,java.lang.String,java.lang.Exception,java.util.Properties)">
<h3>methodException</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">methodException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">Handler a method call exception.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - the class of the object the method is being applied to</dd>
<dd><code>method</code> - the method</dd>
<dd><code>e</code> - the thrown exception</dd>
<dd><code>properties</code> - the engine properties</dd>
<dt>Returns:</dt>
<dd>return value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invalidProperty(java.lang.String,java.lang.Object,java.lang.String,java.util.Properties)">
<h3>invalidProperty</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">invalidProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">Invoke when getter method of <code>object</code> is not defined.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reference</code> - string with complete reference</dd>
<dd><code>object</code> - the object referred to, or null if not found</dd>
<dd><code>property</code> - the property name from the reference</dd>
<dd><code>properties</code> - the engine properties</dd>
<dt>Returns:</dt>
<dd>return value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invalidReference(java.lang.String,java.lang.Object,java.lang.String,java.util.Properties)">
<h3>invalidReference</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">invalidReference</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">Handle reference tag and return the proper value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reference</code> - string with complete reference</dd>
<dd><code>object</code> - the object referred to, or null if not found</dd>
<dd><code>property</code> - the property name from the reference</dd>
<dd><code>properties</code> - the engine properties</dd>
<dt>Returns:</dt>
<dd>return value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invalidMethod(java.lang.String,java.lang.Object,java.lang.String,java.util.Properties)">
<h3>invalidMethod</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">invalidMethod</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">Handle reference method and return the proper value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reference</code> - string with complete reference</dd>
<dd><code>object</code> - the object referred to, or null if not found</dd>
<dd><code>method</code> - the property name from the reference</dd>
<dd><code>properties</code> - the engine properties</dd>
<dt>Returns:</dt>
<dd>return value</dd>
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
