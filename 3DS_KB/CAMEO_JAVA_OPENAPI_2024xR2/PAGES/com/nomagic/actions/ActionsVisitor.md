# JAVA OPENAPI: ActionsVisitor (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/actions/ActionsVisitor.html
- source_path: `com/nomagic/actions/ActionsVisitor.html`
- source_sha256: `59b85f35e7714b5b2940c1512b0f2b4b394fe148c48ebb5048b6197ce20a0c47`
- captured_utc: `2026-07-14T16:55:00.370841+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.actions](package-summary.html)

## Interface ActionsVisitor

All Known Implementing Classes:
`[ActionsCommandBarCreator](ActionsCommandBarCreator.html)`, `[ActionsMenuCreator.AMC_ActionsVisitor](ActionsMenuCreator.AMC_ActionsVisitor.html)`

@OpenApiAllpublic interfaceActionsVisitor

Interface for visiting Actions. This interface is used to implement Visitor pattern.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[visit](#visit(com.nomagic.actions.ActionsCategory))([ActionsCategory](ActionsCategory.html) category)`
Visits ActionsCategory.
`void`
`[visit](#visit(com.nomagic.actions.NMAction))([NMAction](NMAction.html) action)`
Visits action.
`void`
`[visit](#visit(com.nomagic.actions.NMStateAction))([NMStateAction](NMStateAction.html) action)`
Visits NMStateAction.
`void`
`[visit](#visit(com.nomagic.actions.NMTriStateAction))([NMTriStateAction](NMTriStateAction.html) action)`
Visits NMTriStateAction

============ METHOD DETAIL ========== 
Method Details
visit
void visit([NMAction](NMAction.html) action)
Visits action.
Parameters:
`action` - the action to visit.
visit
void visit([NMStateAction](NMStateAction.html) action)
Visits NMStateAction.
Parameters:
`action` - the action to visit.
visit
void visit([NMTriStateAction](NMTriStateAction.html) action)
Visits NMTriStateAction
Parameters:
`action` - the action to visit
visit
void visit([ActionsCategory](ActionsCategory.html) category)
Visits ActionsCategory.
Parameters:
`category` - the category to visit.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.actions</a></div>
<h1 class="title" title="Interface ActionsVisitor">Interface ActionsVisitor</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="ActionsCommandBarCreator.html" title="class in com.nomagic.actions">ActionsCommandBarCreator</a></code>, <code><a href="ActionsMenuCreator.AMC_ActionsVisitor.html" title="class in com.nomagic.actions">ActionsMenuCreator.AMC_ActionsVisitor</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ActionsVisitor</span></div>
<div class="block">Interface for visiting Actions. This interface is used to implement Visitor pattern.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.actions.ActionsCategory)">visit</a><wbr/>(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visits ActionsCategory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.actions.NMAction)">visit</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visits action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.actions.NMStateAction)">visit</a><wbr/>(<a href="NMStateAction.html" title="class in com.nomagic.actions">NMStateAction</a> action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visits NMStateAction.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.actions.NMTriStateAction)">visit</a><wbr/>(<a href="NMTriStateAction.html" title="class in com.nomagic.actions">NMTriStateAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visits NMTriStateAction</div>
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
<section class="detail" id="visit(com.nomagic.actions.NMAction)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Visits action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - the action to visit.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.actions.NMStateAction)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="NMStateAction.html" title="class in com.nomagic.actions">NMStateAction</a> action)</span></div>
<div class="block">Visits NMStateAction.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - the action to visit.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.actions.NMTriStateAction)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="NMTriStateAction.html" title="class in com.nomagic.actions">NMTriStateAction</a> action)</span></div>
<div class="block">Visits NMTriStateAction</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - the action to visit</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.actions.ActionsCategory)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</span></div>
<div class="block">Visits ActionsCategory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - the category to visit.</dd>
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
