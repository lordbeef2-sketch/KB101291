# JAVA OPENAPI: DiagramComparator (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/tests/common/comparators/DiagramComparator.html
- source_path: `com/nomagic/magicdraw/tests/common/comparators/DiagramComparator.html`
- source_sha256: `fadd2850c7c77b1ca1dac4cdd34dae945c9eb19190372e1d121df5f255142b08`
- captured_utc: `2026-07-14T16:51:48.504565+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.tests.common.comparators](package-summary.html)

## Interface DiagramComparator

All Known Implementing Classes:
`[DiagramComparatorImpl](DiagramComparatorImpl.html)`

@OpenApiAllpublic interfaceDiagramComparator

Base interface for comparing diagrams.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[compareDiagrams](#compareDiagrams(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html)> diagrams1,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html)> diagrams2)`
Compare two diagram presentations.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiffInfo](#getDiffInfo())()`
Format textual information about differences found in compared diagrams.
`void`
`[saveDiffToImageFiles](#saveDiffToImageFiles(java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)`
Save graphical diagram differences to the given file or directory.

============ METHOD DETAIL ========== 
Method Details
compareDiagrams
boolean compareDiagrams([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html)> diagrams1,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html)> diagrams2)
Compare two diagram presentations.
Parameters:
`diagrams1` - first diagram to compare.
`diagrams2` - second diagram to compare.
Returns:
true if diagrams are equals.
getDiffInfo
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiffInfo()
Format textual information about differences found in compared diagrams.
Returns:
String information about differences in diagram.
saveDiffToImageFiles
void saveDiffToImageFiles([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)
Save graphical diagram differences to the given file or directory.
Parameters:
`file` - File or directory to save graphical differences to.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.tests.common.comparators</a></div>
<h1 class="title" title="Interface DiagramComparator">Interface DiagramComparator</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="DiagramComparatorImpl.html" title="class in com.nomagic.magicdraw.tests.common.comparators">DiagramComparatorImpl</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DiagramComparator</span></div>
<div class="block">Base interface for comparing diagrams.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#compareDiagrams(java.util.Collection,java.util.Collection)">compareDiagrams</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; diagrams1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; diagrams2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Compare two diagram presentations.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiffInfo()">getDiffInfo</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Format textual information about differences found in compared diagrams.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#saveDiffToImageFiles(java.io.File)">saveDiffToImageFiles</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Save graphical diagram differences to the given file or directory.</div>
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
<section class="detail" id="compareDiagrams(java.util.Collection,java.util.Collection)">
<h3>compareDiagrams</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">compareDiagrams</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; diagrams1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; diagrams2)</span></div>
<div class="block">Compare two diagram presentations.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagrams1</code> - first diagram to compare.</dd>
<dd><code>diagrams2</code> - second diagram to compare.</dd>
<dt>Returns:</dt>
<dd>true if diagrams are equals.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiffInfo()">
<h3>getDiffInfo</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiffInfo</span>()</div>
<div class="block">Format textual information about differences found in compared diagrams.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>String information about differences in diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveDiffToImageFiles(java.io.File)">
<h3>saveDiffToImageFiles</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">saveDiffToImageFiles</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Save graphical diagram differences to the given file or directory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - File or directory to save graphical differences to.</dd>
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
