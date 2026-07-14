# JAVA OPENAPI: InvalidModelHandler (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/transaction/InvalidModelHandler.html
- source_path: `com/nomagic/uml2/transaction/InvalidModelHandler.html`
- source_sha256: `064947153b903b7a8a462d430ddf983c05465122349429032e1719e14cf26f36`
- captured_utc: `2026-07-14T16:58:57.975514+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.transaction](package-summary.html)

## Interface InvalidModelHandler

public interfaceInvalidModelHandler
Fixes invalid model. All fixes must be done in transaction.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static enum`
`[InvalidModelHandler.Result](InvalidModelHandler.Result.html)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[InvalidModelHandler.Result](InvalidModelHandler.Result.html)`
`[handleInvalidElements](#handleInvalidElements(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModelValidationResult](ModelValidationResult.html)> elements)`
Fixes given validation problems.

============ METHOD DETAIL ========== 
Method Details
handleInvalidElements
[InvalidModelHandler.Result](InvalidModelHandler.Result.html) handleInvalidElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModelValidationResult](ModelValidationResult.html)> elements)
Fixes given validation problems.
Parameters:
`elements` -
Returns:
result of fixing. If fixing was done by modifying model Result.FIXED should be
 return. If undo must be done Result.ROLLBACK_TRANSACTION must be return, in case of
 failure Result.UNABLE_TO_FIX must be return.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.transaction</a></div>
<h1 class="title" title="Interface InvalidModelHandler">Interface InvalidModelHandler</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">InvalidModelHandler</span></div>
<div class="block">Fixes invalid model. All fixes must be done in transaction.</div>
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
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="InvalidModelHandler.Result.html" title="enum class in com.nomagic.uml2.transaction">InvalidModelHandler.Result</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="InvalidModelHandler.Result.html" title="enum class in com.nomagic.uml2.transaction">InvalidModelHandler.Result</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#handleInvalidElements(java.util.Collection)">handleInvalidElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModelValidationResult.html" title="class in com.nomagic.uml2.transaction">ModelValidationResult</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Fixes given validation problems.</div>
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
<section class="detail" id="handleInvalidElements(java.util.Collection)">
<h3>handleInvalidElements</h3>
<div class="member-signature"><span class="return-type"><a href="InvalidModelHandler.Result.html" title="enum class in com.nomagic.uml2.transaction">InvalidModelHandler.Result</a></span> <span class="element-name">handleInvalidElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModelValidationResult.html" title="class in com.nomagic.uml2.transaction">ModelValidationResult</a>&gt; elements)</span></div>
<div class="block">Fixes given validation problems.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - </dd>
<dt>Returns:</dt>
<dd>result of fixing. If fixing was done by modifying model Result.FIXED should be
         return. If undo must be done Result.ROLLBACK_TRANSACTION must be return, in case of
         failure Result.UNABLE_TO_FIX must be return.</dd>
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
