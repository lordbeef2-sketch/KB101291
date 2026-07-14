# JAVA OPENAPI: ExtractReference (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/refactor/extract/ExtractReference.html
- source_path: `com/nomagic/magicdraw/uml/refactor/extract/ExtractReference.html`
- source_sha256: `3bd7feb98d71ed9570647a40c80a5eeadae7db58f64052d8aa7b65be975a7eb2`
- captured_utc: `2026-07-14T16:55:55.578460+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.refactor.extract](package-summary.html)

## Interface ExtractReference

@OpenApiAllpublic interfaceExtractReference
Represents logical model relation from the extract source to the extract target.
 In the concrete refactoring this reference can be represented as connector (composite structures),
 object flow (activities), transition (states), message (interactions).

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[setCreate](#setCreate(boolean))(boolean create)`
Flag value which indicates whether reference should be created during refactoring.
`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Sets name of the reference.
`void`
`[setType](#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([Type](../../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type)`
Sets type of the reference.

============ METHOD DETAIL ========== 
Method Details
setCreate
void setCreate(boolean create)
Flag value which indicates whether reference should be created during refactoring.
Parameters:
`create` - create flag value.
setName
void setName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Sets name of the reference.
 This name is used to name the elements which represent the reference in the model.
Parameters:
`name` - name to set.
setType
void setType([Type](../../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type)
Sets type of the reference.
 This type is used to type the elements which represent the reference in the model.
 For example, in activity extract the type is used to type activity parameters, activity parameter nodes,
 pins. In extract structure it is used to type ports.
Parameters:
`type` - type to set.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.refactor.extract</a></div>
<h1 class="title" title="Interface ExtractReference">Interface ExtractReference</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ExtractReference</span></div>
<div class="block">Represents logical model relation from the extract source to the extract target.
 In the concrete refactoring this reference can be represented as connector (composite structures),
 object flow (activities), transition (states), message (interactions).</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setCreate(boolean)">setCreate</a><wbr/>(boolean create)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Flag value which indicates whether reference should be created during refactoring.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets name of the reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">setType</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets type of the reference.</div>
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
<section class="detail" id="setCreate(boolean)">
<h3>setCreate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setCreate</span><wbr/><span class="parameters">(boolean create)</span></div>
<div class="block">Flag value which indicates whether reference should be created during refactoring.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>create</code> - create flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Sets name of the reference.
 This name is used to name the elements which represent the reference in the model.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - name to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>setType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setType</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</span></div>
<div class="block">Sets type of the reference.
 This type is used to type the elements which represent the reference in the model.
 For example, in activity extract the type is used to type activity parameters, activity parameter nodes,
 pins. In extract structure it is used to type ports.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - type to set.</dd>
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
