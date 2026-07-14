# JAVA OPENAPI: ModelElementProject (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/foundation/project/ModelElementProject.html
- source_path: `com/dassault_systemes/modeler/foundation/project/ModelElementProject.html`
- source_sha256: `421d58e1e7645276fbdca4dbe1d1f521bbf97b13c4df7efbee7151e416cc76bb`
- captured_utc: `2026-07-14T16:44:44.627798+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.foundation.project](package-summary.html)

## Interface ModelElementProject

All Superinterfaces:
`com.dassault_systemes.modeler.foundation.model.ModelElementRegistry`

All Known Implementing Classes:
`com.dassault_systemes.modeler.foundation.project.ModelElementProjectImpl`, `[Project](../../../../nomagic/magicdraw/core/Project.html)`

@OpenApipublic interfaceModelElementProjectextends com.dassault_systemes.modeler.foundation.model.ModelElementRegistry

A container of [`BaseElement`](../../../../nomagic/magicdraw/uml/BaseElement.html) and services for these elements.

========== METHOD SUMMARY =========== 
Method Summary
Static Methods
Modifier and Type
Method
Description
`static [ModelElementProject](ModelElementProject.html)`
`[getProject](#getProject(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../nomagic/magicdraw/uml/BaseElement.html) element)`
Returns the project that contains the given element.
`static [ModelElementProject](ModelElementProject.html)`
`[getProject](#getProject(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../../../../nomagic/magicdraw/uml/BaseElement.html)> elements)`
Returns the project for the given elements.
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElementRegistry
`addElementByID, getElementByID, isDisposed, isEMFProxiesSupported, isPreloadProject, removeElementByID`

============ METHOD DETAIL ========== 
Method Details
getProject
@OpenApistatic [ModelElementProject](ModelElementProject.html) getProject([BaseElement](../../../../nomagic/magicdraw/uml/BaseElement.html) element)
Returns the project that contains the given element.
Parameters:
`element` - the element
Returns:
the project, or `null` if not available
See Also:
`ProjectProvider`
getProject
@OpenApistatic [ModelElementProject](ModelElementProject.html) getProject(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../../../../nomagic/magicdraw/uml/BaseElement.html)> elements)
Returns the project for the given elements.

 If the collection is not empty, the project of the first element is returned.
Parameters:
`elements` - collection of elements
Returns:
the project, or `null` if the collection is `null` or empty

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.foundation.project</a></div>
<h1 class="title" title="Interface ModelElementProject">Interface ModelElementProject</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.model.ModelElementRegistry</code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.ModelElementProjectImpl</code>, <code><a href="../../../../nomagic/magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ModelElementProject</span><span class="extends-implements">
extends com.dassault_systemes.modeler.foundation.model.ModelElementRegistry</span></div>
<div class="block">A container of <a href="../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml"><code>BaseElement</code></a> and services for these elements.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div class="caption"><span>Static Methods</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a href="ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getProject(com.nomagic.magicdraw.uml.BaseElement)">getProject</a><wbr/>(<a href="../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Returns the project that contains the given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a href="ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getProject(java.util.Collection)">getProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Returns the project for the given elements.</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElementRegistry">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElementRegistry</h3>
<code>addElementByID, getElementByID, isDisposed, isEMFProxiesSupported, isPreloadProject, removeElementByID</code></div>
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
<section class="detail" id="getProject(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">static</span> <span class="return-type"><a href="ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a></span> <span class="element-name">getProject</span><wbr/><span class="parameters">(<a href="../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns the project that contains the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>the project, or <code>null</code> if not available</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><code>ProjectProvider</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject(java.util.Collection)">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">static</span> <span class="return-type"><a href="ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a></span> <span class="element-name">getProject</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elements)</span></div>
<div class="block">Returns the project for the given elements.

 <p>If the collection is not empty, the project of the first element is returned.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - collection of elements</dd>
<dt>Returns:</dt>
<dd>the project, or <code>null</code> if the collection is <code>null</code> or empty</dd>
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
