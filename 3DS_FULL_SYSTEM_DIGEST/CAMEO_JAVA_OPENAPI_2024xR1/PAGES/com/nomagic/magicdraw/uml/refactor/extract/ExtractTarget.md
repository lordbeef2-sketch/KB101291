# JAVA OPENAPI: ExtractTarget (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml/refactor/extract/ExtractTarget.html
- source_path: `com/nomagic/magicdraw/uml/refactor/extract/ExtractTarget.html`
- source_sha256: `8205fbef75e82b9f8cb6a33f17a6f4c6fcbe9198409b74623318fed64aa47fef`
- captured_utc: `2026-07-14T16:52:08.808835+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.refactor.extract](package-summary.html)

## Interface ExtractTarget

@OpenApiAllpublic interfaceExtractTarget

Controls extract refactoring result: target diagram type, target namespace,
 references from extract source to the target.

See Also:
[`ExtractManager`](ExtractManager.html)
[`ExtractSource`](ExtractSource.html)
[`Refactoring.Extracting`](../../Refactoring.Extracting.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getAllowedTargetDiagramTypes](#getAllowedTargetDiagramTypes())()`
Gets allowed target diagram types for extract refactoring.
`[DiagramPresentationElement](../../symbols/DiagramPresentationElement.html)`
`[getDiagram](#getDiagram())()`
Gets target diagram which was created during refactoring.
`[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElement](#getElement())()`
Gets element which was created in the extract refactor target after refactoring.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [ExtractReference](ExtractReference.html)>`
`[getReferences](#getReferences())()`
Gets source to target references.
`void`
`[setElementName](#setElementName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementName)`
Sets name of the refactored target element.
`void`
`[setTargetDiagramType](#setTargetDiagramType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) targetDiagramType)`
Sets type of diagram to create the target diagram.
`void`
`[setTargetNamespace](#setTargetNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([Namespace](../../../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) targetNamespace)`
Sets namespace in which target elements have to be created.

============ METHOD DETAIL ========== 
Method Details
setTargetDiagramType
void setTargetDiagramType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) targetDiagramType)
Sets type of diagram to create the target diagram.
 Target diagram type must be among allowed target diagram types for a specific extract refactoring.
 If target diagram type is not among allowed types, [`IllegalArgumentException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) is thrown.
Parameters:
`targetDiagramType` - target diagram type to set.
getAllowedTargetDiagramTypes
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getAllowedTargetDiagramTypes()
Gets allowed target diagram types for extract refactoring.
Returns:
allowed target diagram types.
setTargetNamespace
void setTargetNamespace([Namespace](../../../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) targetNamespace)
Sets namespace in which target elements have to be created.
Parameters:
`targetNamespace` - namespace for target elements.
getReferences
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [ExtractReference](ExtractReference.html)> getReferences()
Gets source to target references.
 Reference represents logical model relation from the extract source to the extract target.
 In the concrete refactoring this reference can be represented as connector (composite structures),
 object flow (activities), transition (states), message (interactions).
Returns:
source to target references.
setElementName
void setElementName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementName)
Sets name of the refactored target element.
Parameters:
`elementName` - refactored element name.
getElement
[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElement()
Gets element which was created in the extract refactor target after refactoring.
Returns:
target refactored element if called after refactoring, null if called before refactoring.
getDiagram
[DiagramPresentationElement](../../symbols/DiagramPresentationElement.html) getDiagram()
Gets target diagram which was created during refactoring.
Returns:
target diagram.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.refactor.extract</a></div>
<h1 class="title" title="Interface ExtractTarget">Interface ExtractTarget</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ExtractTarget</span></div>
<div class="block">Controls extract refactoring result: target diagram type, target namespace,
 references from extract source to the target.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="ExtractManager.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract"><code>ExtractManager</code></a></li>
<li><a href="ExtractSource.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract"><code>ExtractSource</code></a></li>
<li><a href="../../Refactoring.Extracting.html" title="class in com.nomagic.magicdraw.uml"><code>Refactoring.Extracting</code></a></li>
</ul>
</dd>
</dl>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAllowedTargetDiagramTypes()">getAllowedTargetDiagramTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets allowed target diagram types for extract refactoring.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagram()">getDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets target diagram which was created during refactoring.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets element which was created in the extract refactor target after refactoring.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="ExtractReference.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract">ExtractReference</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getReferences()">getReferences</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets source to target references.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setElementName(java.lang.String)">setElementName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets name of the refactored target element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTargetDiagramType(java.lang.String)">setTargetDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetDiagramType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets type of diagram to create the target diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTargetNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setTargetNamespace</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> targetNamespace)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets namespace in which target elements have to be created.</div>
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
<section class="detail" id="setTargetDiagramType(java.lang.String)">
<h3>setTargetDiagramType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTargetDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetDiagramType)</span></div>
<div class="block">Sets type of diagram to create the target diagram.
 Target diagram type must be among allowed target diagram types for a specific extract refactoring.
 If target diagram type is not among allowed types, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> is thrown.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetDiagramType</code> - target diagram type to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllowedTargetDiagramTypes()">
<h3>getAllowedTargetDiagramTypes</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAllowedTargetDiagramTypes</span>()</div>
<div class="block">Gets allowed target diagram types for extract refactoring.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>allowed target diagram types.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTargetNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>setTargetNamespace</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTargetNamespace</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> targetNamespace)</span></div>
<div class="block">Sets namespace in which target elements have to be created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetNamespace</code> - namespace for target elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReferences()">
<h3>getReferences</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="ExtractReference.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract">ExtractReference</a>&gt;</span> <span class="element-name">getReferences</span>()</div>
<div class="block">Gets source to target references.
 Reference represents logical model relation from the extract source to the extract target.
 In the concrete refactoring this reference can be represented as connector (composite structures),
 object flow (activities), transition (states), message (interactions).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>source to target references.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setElementName(java.lang.String)">
<h3>setElementName</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setElementName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName)</span></div>
<div class="block">Sets name of the refactored target element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementName</code> - refactored element name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElement</span>()</div>
<div class="block">Gets element which was created in the extract refactor target after refactoring.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>target refactored element if called after refactoring, null if called before refactoring.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagram()">
<h3>getDiagram</h3>
<div class="member-signature"><span class="return-type"><a href="../../symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></span> <span class="element-name">getDiagram</span>()</div>
<div class="block">Gets target diagram which was created during refactoring.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>target diagram.</dd>
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
