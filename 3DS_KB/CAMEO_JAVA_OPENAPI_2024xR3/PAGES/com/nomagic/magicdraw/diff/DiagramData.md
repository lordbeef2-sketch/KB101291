# JAVA OPENAPI: DiagramData (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/diff/DiagramData.html
- source_path: `com/nomagic/magicdraw/diff/DiagramData.html`
- source_sha256: `f806dbd9627d5021dfd102791208c9e8e1aecaf0f313ba4420447f98d9e6fa38`
- captured_utc: `2026-07-14T16:55:15.782013+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface DiagramData

@OpenApipublic interfaceDiagramData
Information used to create new diagram presentation element with all inner elements.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[getBackground](#getBackground())()`
Returns background color of the diagram.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getCreatedBy](#getCreatedBy())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getCreationDate](#getCreationDate())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramElementID](#getDiagramElementID())()`
ID of diagram element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramName](#getDiagramName())()`
Returns diagram name of the diagram.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramPresentationElementID](#getDiagramPresentationElementID())()`
Returns diagram presentation element's ID.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramQualifiedName](#getDiagramQualifiedName())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramType](#getDiagramType())()`
Diagram type
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLabel](#getLabel())()`
Returns representation text of the diagram.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getModificationDate](#getModificationDate())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getModifiedBy](#getModifiedBy())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPreviewPath](#getPreviewPath())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getProjectFileName](#getProjectFileName())()`
Returns project file name.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRealDiagramElementID](#getRealDiagramElementID())()`

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[SymbolData](symbols/SymbolData.html)>`
`[getSymbolData](#getSymbolData())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUMLDiagramType](#getUMLDiagramType())()`
UML diagramType
`default boolean`
`[isProxyElement](#isProxyElement())()`

`boolean`
`[isSymbolDiagram](#isSymbolDiagram())()`

============ METHOD DETAIL ========== 
Method Details
getDiagramPresentationElementID
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramPresentationElementID()
Returns diagram presentation element's ID.
Returns:
presentation element id.
getDiagramElementID
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramElementID()
ID of diagram element.
Returns:
diagram element id.
getDiagramType
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramType()
Diagram type
Returns:
diagram type
getUMLDiagramType
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUMLDiagramType()
UML diagramType
Returns:
uml diagram type.
getPreviewPath
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPreviewPath()
Returns:
absolute path to exported diagram image (png format). Can be null if export could not
 be done.
getProjectFileName
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getProjectFileName()
Returns project file name.
Returns:
project file name.
getDiagramName
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramName()
Returns diagram name of the diagram.
Returns:
diagram name.
getBackground
[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) getBackground()
Returns background color of the diagram.
Returns:
background color.
getSymbolData
@OpenApi[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[SymbolData](symbols/SymbolData.html)> getSymbolData()
getLabel
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLabel()
Returns representation text of the diagram.
Returns:
representation text
isSymbolDiagram
boolean isSymbolDiagram()
Returns:
`true` when current diagram is symbol diagram (symbols
 can be drawn in it), otherwise - `false`
getRealDiagramElementID
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRealDiagramElementID()
Returns:
real diagram's element id
getDiagramQualifiedName
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramQualifiedName()
Returns:
qualified name of the diagram
getModifiedBy
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getModifiedBy()
Returns:
modified by
getModificationDate
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getModificationDate()
Returns:
modification date
getCreatedBy
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getCreatedBy()
Returns:
created by
getCreationDate
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getCreationDate()
Returns:
creation date
isProxyElement
default boolean isProxyElement()
Returns:
is diagram proxy element

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface DiagramData">Interface DiagramData</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DiagramData</span></div>
<div class="block">Information used to create new diagram presentation element with all inner elements.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBackground()">getBackground</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns background color of the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCreatedBy()">getCreatedBy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCreationDate()">getCreationDate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramElementID()">getDiagramElementID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">ID of diagram element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramName()">getDiagramName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns diagram name of the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramPresentationElementID()">getDiagramPresentationElementID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns diagram presentation element's ID.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramQualifiedName()">getDiagramQualifiedName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramType()">getDiagramType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Diagram type</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLabel()">getLabel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns representation text of the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getModificationDate()">getModificationDate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getModifiedBy()">getModifiedBy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPreviewPath()">getPreviewPath</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectFileName()">getProjectFileName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns project file name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRealDiagramElementID()">getRealDiagramElementID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="symbols/SymbolData.html" title="class in com.nomagic.magicdraw.diff.symbols">SymbolData</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSymbolData()">getSymbolData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUMLDiagramType()">getUMLDiagramType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">UML diagramType</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isProxyElement()">isProxyElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSymbolDiagram()">isSymbolDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
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
<section class="detail" id="getDiagramPresentationElementID()">
<h3>getDiagramPresentationElementID</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramPresentationElementID</span>()</div>
<div class="block">Returns diagram presentation element's ID.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>presentation element id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramElementID()">
<h3>getDiagramElementID</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramElementID</span>()</div>
<div class="block">ID of diagram element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram element id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramType()">
<h3>getDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramType</span>()</div>
<div class="block">Diagram type</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUMLDiagramType()">
<h3>getUMLDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUMLDiagramType</span>()</div>
<div class="block">UML diagramType</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>uml diagram type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreviewPath()">
<h3>getPreviewPath</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPreviewPath</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>absolute path to exported diagram image (png format). Can be null if export could not
         be done.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectFileName()">
<h3>getProjectFileName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProjectFileName</span>()</div>
<div class="block">Returns project file name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project file name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramName()">
<h3>getDiagramName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramName</span>()</div>
<div class="block">Returns diagram name of the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBackground()">
<h3>getBackground</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">getBackground</span>()</div>
<div class="block">Returns background color of the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>background color.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSymbolData()">
<h3>getSymbolData</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="symbols/SymbolData.html" title="class in com.nomagic.magicdraw.diff.symbols">SymbolData</a>&gt;</span> <span class="element-name">getSymbolData</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLabel()">
<h3>getLabel</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLabel</span>()</div>
<div class="block">Returns representation text of the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>representation text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSymbolDiagram()">
<h3>isSymbolDiagram</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isSymbolDiagram</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> when current diagram is symbol diagram (symbols
         can be drawn in it), otherwise - <code>false</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRealDiagramElementID()">
<h3>getRealDiagramElementID</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRealDiagramElementID</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>real diagram's element id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramQualifiedName()">
<h3>getDiagramQualifiedName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramQualifiedName</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>qualified name of the diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModifiedBy()">
<h3>getModifiedBy</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getModifiedBy</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>modified by</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModificationDate()">
<h3>getModificationDate</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getModificationDate</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>modification date</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreatedBy()">
<h3>getCreatedBy</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCreatedBy</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created by</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreationDate()">
<h3>getCreationDate</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCreationDate</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>creation date</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isProxyElement()">
<h3>isProxyElement</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isProxyElement</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>is diagram proxy element</dd>
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
