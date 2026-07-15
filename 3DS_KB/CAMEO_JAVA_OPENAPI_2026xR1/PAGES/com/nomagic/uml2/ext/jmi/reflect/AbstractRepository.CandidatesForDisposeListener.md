# JAVA OPENAPI: AbstractRepository.CandidatesForDisposeListener (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/jmi/reflect/AbstractRepository.CandidatesForDisposeListener.html
- source_path: `com/nomagic/uml2/ext/jmi/reflect/AbstractRepository.CandidatesForDisposeListener.html`
- source_sha256: `0db29b641266eea0b5a5623dfbcb9accb1377910563470f22f39770a5282df17`
- captured_utc: `2026-07-14T16:46:22.713102+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.reflect](package-summary.html)

## Interface AbstractRepository.CandidatesForDisposeListener

Enclosing class:
`[AbstractRepository](AbstractRepository.html)`

public static interfaceAbstractRepository.CandidatesForDisposeListener

Candidates for dispose listener

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[candidateAdded](#candidateAdded(javax.jmi.reflect.RefObject))(javax.jmi.reflect.RefObject candidate)`
Invoked when an object is registered as candidate to be disposed
`void`
`[candidateRemoved](#candidateRemoved(javax.jmi.reflect.RefObject))(javax.jmi.reflect.RefObject candidate)`
Invoked when an object is removed from candidates to be disposed

============ METHOD DETAIL ========== 
Method Details
candidateAdded
void candidateAdded(javax.jmi.reflect.RefObject candidate)
Invoked when an object is registered as candidate to be disposed
Parameters:
`candidate` - the object
candidateRemoved
void candidateRemoved(javax.jmi.reflect.RefObject candidate)
Invoked when an object is removed from candidates to be disposed
Parameters:
`candidate` - the object

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.reflect</a></div>
<h1 class="title" title="Interface AbstractRepository.CandidatesForDisposeListener">Interface AbstractRepository.CandidatesForDisposeListener</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static interface </span><span class="element-name type-name-label">AbstractRepository.CandidatesForDisposeListener</span></div>
<div class="block">Candidates for dispose listener</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#candidateAdded(javax.jmi.reflect.RefObject)">candidateAdded</a><wbr/>(javax.jmi.reflect.RefObject candidate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Invoked when an object is registered as candidate to be disposed</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#candidateRemoved(javax.jmi.reflect.RefObject)">candidateRemoved</a><wbr/>(javax.jmi.reflect.RefObject candidate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Invoked when an object is removed from candidates to be disposed</div>
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
<section class="detail" id="candidateAdded(javax.jmi.reflect.RefObject)">
<h3>candidateAdded</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">candidateAdded</span><wbr/><span class="parameters">(javax.jmi.reflect.RefObject candidate)</span></div>
<div class="block">Invoked when an object is registered as candidate to be disposed</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>candidate</code> - the object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="candidateRemoved(javax.jmi.reflect.RefObject)">
<h3>candidateRemoved</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">candidateRemoved</span><wbr/><span class="parameters">(javax.jmi.reflect.RefObject candidate)</span></div>
<div class="block">Invoked when an object is removed from candidates to be disposed</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>candidate</code> - the object</dd>
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
