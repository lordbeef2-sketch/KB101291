# JAVA OPENAPI: SysMLTextualNotationService (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/magic/sysml/textual/SysMLTextualNotationService.html
- source_path: `com/dassault_systemes/modeler/magic/sysml/textual/SysMLTextualNotationService.html`
- source_sha256: `814aaa38b45b4e6cb078fdefd1c5e3a27d7ac642eb5a93f9dea0a15c0840e6fe`
- captured_utc: `2026-07-14T16:44:50.987881+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.magic.sysml.textual](package-summary.html)

## Class SysMLTextualNotationService

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.magic.sysml.textual.SysMLTextualNotationService

@OpenApiAllpublic final classSysMLTextualNotationService
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Provides API for importing and exporting SysML textual notation
 for a given project or namespace.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SysMLTextualNotationService](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[exportTextual](#exportTextual(com.dassault_systemes.modeler.kerml.model.kerml.Namespace))([Namespace](../../../kerml/model/kerml/Namespace.html) namespace)`
Exports the textual SysML representation of the specified [`Namespace`](../../../kerml/model/kerml/Namespace.html).
`static void`
`[importTextual](#importTextual(com.dassault_systemes.modeler.foundation.project.ModelElementProject,java.lang.String))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sysmlText)`
Imports SysML textual notation into the specified project.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SysMLTextualNotationService
public SysMLTextualNotationService()
 ============ METHOD DETAIL ========== 
Method Details
exportTextual
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) exportTextual([Namespace](../../../kerml/model/kerml/Namespace.html) namespace)
Exports the textual SysML representation of the specified [`Namespace`](../../../kerml/model/kerml/Namespace.html).
 The `TextualNotationBuilder` service is looked up from the project
 that owns the given namespace. If the service is not available, an
 [`IllegalStateException`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html) is thrown.
Parameters:
`namespace` - the namespace to export to textual SysML notation;
 must belong to a [`ModelElementProject`](../../../foundation/project/ModelElementProject.html)
Returns:
the textual SysML notation corresponding to the given namespace
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if no `TextualNotationBuilder` is
 registered for the namespace's project
importTextual
public static void importTextual([ModelElementProject](../../../foundation/project/ModelElementProject.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sysmlText)
Imports SysML textual notation into the specified project.
Parameters:
`project` - the target project that will receive the imported model
`sysmlText` - the SysML textual notation to import; must not be `null`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.magic.sysml.textual</a></div>
<h1 class="title" title="Class SysMLTextualNotationService">Class SysMLTextualNotationService</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.magic.sysml.textual.SysMLTextualNotationService</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">SysMLTextualNotationService</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Provides API for importing and exporting SysML textual notation
 for a given project or namespace.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SysMLTextualNotationService</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#exportTextual(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">exportTextual</a><wbr/>(<a href="../../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> namespace)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports the textual SysML representation of the specified <a href="../../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Namespace</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#importTextual(com.dassault_systemes.modeler.foundation.project.ModelElementProject,java.lang.String)">importTextual</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sysmlText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Imports SysML textual notation into the specified project.</div>
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
<h3>SysMLTextualNotationService</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SysMLTextualNotationService</span>()</div>
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
<section class="detail" id="exportTextual(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">
<h3>exportTextual</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">exportTextual</span><wbr/><span class="parameters">(<a href="../../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> namespace)</span></div>
<div class="block">Exports the textual SysML representation of the specified <a href="../../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Namespace</code></a>.
 <p>
 The <code>TextualNotationBuilder</code> service is looked up from the project
 that owns the given namespace. If the service is not available, an
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang"><code>IllegalStateException</code></a> is thrown.
 </p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>namespace</code> - the namespace to export to textual SysML notation;
                  must belong to a <a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project"><code>ModelElementProject</code></a></dd>
<dt>Returns:</dt>
<dd>the textual SysML notation corresponding to the given namespace</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if no <code>TextualNotationBuilder</code> is
                               registered for the namespace's project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importTextual(com.dassault_systemes.modeler.foundation.project.ModelElementProject,java.lang.String)">
<h3>importTextual</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">importTextual</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sysmlText)</span></div>
<div class="block">Imports SysML textual notation into the specified project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the target project that will receive the imported model</dd>
<dd><code>sysmlText</code> - the SysML textual notation to import; must not be <code>null</code></dd>
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
