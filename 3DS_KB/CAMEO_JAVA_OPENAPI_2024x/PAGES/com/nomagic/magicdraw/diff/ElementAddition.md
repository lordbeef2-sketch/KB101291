# JAVA OPENAPI: ElementAddition (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/diff/ElementAddition.html
- source_path: `com/nomagic/magicdraw/diff/ElementAddition.html`
- source_sha256: `8d52866c176aa43b55c42131538b0de4fa29ff2d4d9c4ccc1cfbc39899b781bd`
- captured_utc: `2026-07-14T16:51:17.325151+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface ElementAddition

All Superinterfaces:
`[Difference](Difference.html)`, `[DifferenceLocation](DifferenceLocation.html)`, `[ElementDifference](ElementDifference.html)`

@OpenApiAllpublic interfaceElementAdditionextends [ElementDifference](ElementDifference.html)

Difference when new element is created in contributor project. Together with
 [`ElementAddition`](ElementAddition.html) there must be found more differences to fill up created element with data.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getAppliedStereotypes](#getAppliedStereotypes())()`

`long`
`[getContributorVersion](#getContributorVersion())()`

`[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getElementType](#getElementType())()`
Returns created element type.
`[UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html)`
`[getESIElementID](#getESIElementID())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLocalID](#getLocalID())()`

`boolean`
`[isModelRoot](#isModelRoot())()`

`boolean`
`[isNew](#isNew())()`
Checks if added element is persisted into the project.
Methods inherited from interface com.nomagic.magicdraw.diff.[DifferenceLocation](DifferenceLocation.html)
`[getModuleURI](DifferenceLocation.html#getModuleURI())`
Methods inherited from interface com.nomagic.magicdraw.diff.[ElementDifference](ElementDifference.html)
`[getElementID](ElementDifference.html#getElementID())`

============ METHOD DETAIL ========== 
Method Details
getElementType
[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getElementType()
Returns created element type.
Returns:
created element type.
getLocalID
@CheckForNull[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLocalID()
isModelRoot
boolean isModelRoot()
getContributorVersion
long getContributorVersion()
getESIElementID
[UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html) getESIElementID()
isNew
boolean isNew()
Checks if added element is persisted into the project.
Returns:
`true` when added element is not persisted into the project.
getAppliedStereotypes
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getAppliedStereotypes()
Returns:
applied stereotype ids

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface ElementAddition">Interface ElementAddition</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code>, <code><a href="DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></code>, <code><a href="ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ElementAddition</span><span class="extends-implements">
extends <a href="ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></span></div>
<div class="block">Difference when new element is created in contributor project. Together with
 <a href="ElementAddition.html" title="interface in com.nomagic.magicdraw.diff"><code>ElementAddition</code></a> there must be found more differences to fill up created element with data.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAppliedStereotypes()">getAppliedStereotypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getContributorVersion()">getContributorVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElementType()">getElementType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns created element type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getESIElementID()">getESIElementID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLocalID()">getLocalID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isModelRoot()">isModelRoot</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isNew()">isNew</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if added element is persisted into the project.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.DifferenceLocation">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></h3>
<code><a href="DifferenceLocation.html#getModuleURI()">getModuleURI</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.ElementDifference">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></h3>
<code><a href="ElementDifference.html#getElementID()">getElementID</a></code></div>
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
<section class="detail" id="getElementType()">
<h3>getElementType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getElementType</span>()</div>
<div class="block">Returns created element type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created element type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocalID()">
<h3>getLocalID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLocalID</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isModelRoot()">
<h3>isModelRoot</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isModelRoot</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getContributorVersion()">
<h3>getContributorVersion</h3>
<div class="member-signature"><span class="return-type">long</span> <span class="element-name">getContributorVersion</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getESIElementID()">
<h3>getESIElementID</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a></span> <span class="element-name">getESIElementID</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isNew()">
<h3>isNew</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isNew</span>()</div>
<div class="block">Checks if added element is persisted into the project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> when added element is not persisted into the project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAppliedStereotypes()">
<h3>getAppliedStereotypes</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAppliedStereotypes</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>applied stereotype ids</dd>
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
