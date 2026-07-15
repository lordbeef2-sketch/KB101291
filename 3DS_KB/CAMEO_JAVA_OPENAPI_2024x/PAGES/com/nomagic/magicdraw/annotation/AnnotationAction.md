# JAVA OPENAPI: AnnotationAction (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/annotation/AnnotationAction.html
- source_path: `com/nomagic/magicdraw/annotation/AnnotationAction.html`
- source_sha256: `b8ca5f4c123ebbaa4af179e39e6bea05f3c21a0052dc81a78cd499de1535cf70`
- captured_utc: `2026-07-14T16:51:00.346926+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.annotation](package-summary.html)

## Interface AnnotationAction

@OpenApiAllpublic interfaceAnnotationAction
Annotation actions supporting multiple targets should implement this interface. Otherwise this action will not be
 available in browser for recursive execution or in validation results window for multiple selection.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[canExecute](#canExecute(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Annotation](Annotation.html)> annotations)`
Checks if possible to execute action together on all specified annotations.
`void`
`[execute](#execute(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Annotation](Annotation.html)> annotations)`
Executes action on specified target annotations.

============ METHOD DETAIL ========== 
Method Details
execute
void execute([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Annotation](Annotation.html)> annotations)
Executes action on specified target annotations. This method will be invoked with such annotations
 that have the action.
Parameters:
`annotations` - action targets
canExecute
boolean canExecute([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Annotation](Annotation.html)> annotations)
Checks if possible to execute action together on all specified annotations.
Parameters:
`annotations` - target annotations
Returns:
true if action can be executed with specified annotations

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.annotation</a></div>
<h1 class="title" title="Interface AnnotationAction">Interface AnnotationAction</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">AnnotationAction</span></div>
<div class="block">Annotation actions supporting multiple targets should implement this interface. Otherwise this action will not be
 available in browser for recursive execution or in validation results window for multiple selection.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canExecute(java.util.Collection)">canExecute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; annotations)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if possible to execute action together on all specified annotations.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(java.util.Collection)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; annotations)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Executes action on specified target annotations.</div>
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
<section class="detail" id="execute(java.util.Collection)">
<h3>execute</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; annotations)</span></div>
<div class="block">Executes action on specified target annotations. This method will be invoked with such annotations
 that have the action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotations</code> - action targets</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canExecute(java.util.Collection)">
<h3>canExecute</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canExecute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; annotations)</span></div>
<div class="block">Checks if possible to execute action together on all specified annotations.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotations</code> - target annotations</dd>
<dt>Returns:</dt>
<dd>true if action can be executed with specified annotations</dd>
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
