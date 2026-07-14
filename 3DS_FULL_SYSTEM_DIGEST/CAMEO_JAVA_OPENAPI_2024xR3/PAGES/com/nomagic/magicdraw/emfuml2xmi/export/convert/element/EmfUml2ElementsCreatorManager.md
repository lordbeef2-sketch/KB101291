# JAVA OPENAPI: EmfUml2ElementsCreatorManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/export/convert/element/EmfUml2ElementsCreatorManager.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/export/convert/element/EmfUml2ElementsCreatorManager.html`
- source_sha256: `99276dc702f315c29a1092030f98e3fcc3af8b8217746cebdd7edea11768c787`
- captured_utc: `2026-07-14T16:55:17.694035+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.export.convert.element](package-summary.html)

## Interface EmfUml2ElementsCreatorManager

All Known Implementing Classes:
`[EmfUml2ElementsCreatorManager](../../../v3/export/convert/element/EmfUml2ElementsCreatorManager.html)`, `com.nomagic.magicdraw.emfuml2xmi.export.convert.element.EmfUml2ElementsCreatorManagerImpl`

@OpenApipublic interfaceEmfUml2ElementsCreatorManager

Registers EmfElementCreators for MagicDraw UML2 model metaclasses

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[addCreator](#addCreator(java.lang.Class,com.nomagic.magicdraw.emfuml2xmi.export.convert.element.EmfElementCreator))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) mdClassType,
 [EmfElementCreator](EmfElementCreator.html) creator)`
Registers new creator.
`void`
`[removeCreator](#removeCreator(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) mdClassType)`
Removes elements creator.

============ METHOD DETAIL ========== 
Method Details
addCreator
@OpenApivoid addCreator([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) mdClassType,
 [EmfElementCreator](EmfElementCreator.html) creator)
Registers new creator.
Parameters:
`mdClassType` - MagicDraw UML2 model metaclass
`creator` - element creator
removeCreator
@OpenApivoid removeCreator([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) mdClassType)
Removes elements creator.
Parameters:
`mdClassType` - MagicDraw UML2 model metaclass

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.export.convert.element</a></div>
<h1 class="title" title="Interface EmfUml2ElementsCreatorManager">Interface EmfUml2ElementsCreatorManager</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../../../v3/export/convert/element/EmfUml2ElementsCreatorManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.export.convert.element">EmfUml2ElementsCreatorManager</a></code>, <code>com.nomagic.magicdraw.emfuml2xmi.export.convert.element.EmfUml2ElementsCreatorManagerImpl</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EmfUml2ElementsCreatorManager</span></div>
<div class="block">Registers EmfElementCreators for MagicDraw UML2 model metaclasses</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addCreator(java.lang.Class,com.nomagic.magicdraw.emfuml2xmi.export.convert.element.EmfElementCreator)">addCreator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> mdClassType,
 <a href="EmfElementCreator.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.export.convert.element">EmfElementCreator</a> creator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Registers new creator.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeCreator(java.lang.Class)">removeCreator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> mdClassType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes elements creator.</div>
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
<section class="detail" id="addCreator(java.lang.Class,com.nomagic.magicdraw.emfuml2xmi.export.convert.element.EmfElementCreator)">
<h3>addCreator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">addCreator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> mdClassType,
 <a href="EmfElementCreator.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.export.convert.element">EmfElementCreator</a> creator)</span></div>
<div class="block">Registers new creator.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mdClassType</code> - MagicDraw UML2 model metaclass</dd>
<dd><code>creator</code> - element creator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeCreator(java.lang.Class)">
<h3>removeCreator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">removeCreator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> mdClassType)</span></div>
<div class="block">Removes elements creator.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mdClassType</code> - MagicDraw UML2 model metaclass</dd>
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
