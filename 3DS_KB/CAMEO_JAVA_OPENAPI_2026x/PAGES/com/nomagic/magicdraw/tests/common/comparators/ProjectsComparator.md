# JAVA OPENAPI: ProjectsComparator (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/tests/common/comparators/ProjectsComparator.html
- source_path: `com/nomagic/magicdraw/tests/common/comparators/ProjectsComparator.html`
- source_sha256: `60c404a67f2ed8ab6d89064549ce597d27949ee509c29b46a6ee1fdeb9d168d7`
- captured_utc: `2026-07-14T16:58:10.419676+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.tests.common.comparators](package-summary.html)

## Class ProjectsComparator

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.tests.common.comparators.ProjectsComparator

@OpenApiAllpublic classProjectsComparator
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Class for comparing two projects. Model and symbols comparison is supported.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectsComparator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[compare](#compare(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project))([Project](../../../core/Project.html) prj1,
 [Project](../../../core/Project.html) prj2)`
Check if two given MagicDraw projects are equals by comparing their model elements and diagrams.
`[DiagramComparator](DiagramComparator.html)`
`[getDiagramComparator](#getDiagramComparator())()`
DiagramComparator used for comparing project diagrams during projects comparison.
`[ModelComparator](ModelComparator.html)`
`[getModelComparator](#getModelComparator())()`
ModelComparator implementation used for projects comparison.
`void`
`[setDiagramComparator](#setDiagramComparator(com.nomagic.magicdraw.tests.common.comparators.DiagramComparator))([DiagramComparator](DiagramComparator.html) diagramComparator)`
Sets DiagramComparator implementation for comparing project diagrams during projects comparison.
`void`
`[setLogTextEnd](#setLogTextEnd(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Text to add before projects comparison log.
`void`
`[setModelComparator](#setModelComparator(com.nomagic.magicdraw.tests.common.comparators.ModelComparator))([ModelComparator](ModelComparator.html) comparator)`
Set implementation of ModelComparator to use for projects comparison.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectsComparator
public ProjectsComparator()
 ============ METHOD DETAIL ========== 
Method Details
compare
public boolean compare([Project](../../../core/Project.html) prj1,
 [Project](../../../core/Project.html) prj2)
Check if two given MagicDraw projects are equals by comparing their model elements and diagrams.
Parameters:
`prj1` - first MagicDraw project to compare.
`prj2` - second MagicDraw project to compare.
Returns:
true if given MagicDraw projects are equals, false otherwise.
getModelComparator
public [ModelComparator](ModelComparator.html) getModelComparator()
ModelComparator implementation used for projects comparison.
Returns:
implementation of ModelComparator used for projects comparison or null if projects compared
 using other criterion.
setModelComparator
public void setModelComparator([ModelComparator](ModelComparator.html) comparator)
Set implementation of ModelComparator to use for projects comparison.
Parameters:
`comparator` - implementation of ModelComparator to use for projects comparison.
getDiagramComparator
@CheckForNullpublic [DiagramComparator](DiagramComparator.html) getDiagramComparator()
DiagramComparator used for comparing project diagrams during projects comparison.
Returns:
implementation of DiagramComparator used for comparing diagrams or null if
 projects are compared by other criterion.
setDiagramComparator
public void setDiagramComparator(@CheckForNull
 [DiagramComparator](DiagramComparator.html) diagramComparator)
Sets DiagramComparator implementation for comparing project diagrams during projects comparison.
Parameters:
`diagramComparator` - implementation of DiagramComparator use for project diagrams comparison.
setLogTextEnd
public void setLogTextEnd(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Text to add before projects comparison log.
Parameters:
`text` - String text to add.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.tests.common.comparators</a></div>
<h1 class="title" title="Class ProjectsComparator">Class ProjectsComparator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.tests.common.comparators.ProjectsComparator</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProjectsComparator</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Class for comparing two projects. Model and symbols comparison is supported.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ProjectsComparator</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compare(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">compare</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj1,
 <a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if two given MagicDraw projects are equals by comparing their model elements and diagrams.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DiagramComparator.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">DiagramComparator</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramComparator()">getDiagramComparator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">DiagramComparator used for comparing project diagrams during projects comparison.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ModelComparator.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">ModelComparator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelComparator()">getModelComparator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">ModelComparator implementation used for projects comparison.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDiagramComparator(com.nomagic.magicdraw.tests.common.comparators.DiagramComparator)">setDiagramComparator</a><wbr/>(<a href="DiagramComparator.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">DiagramComparator</a> diagramComparator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets DiagramComparator implementation for comparing project diagrams during projects comparison.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLogTextEnd(java.lang.String)">setLogTextEnd</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Text to add before projects comparison log.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setModelComparator(com.nomagic.magicdraw.tests.common.comparators.ModelComparator)">setModelComparator</a><wbr/>(<a href="ModelComparator.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">ModelComparator</a> comparator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set implementation of ModelComparator to use for projects comparison.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ProjectsComparator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectsComparator</span>()</div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="compare(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">
<h3>compare</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">compare</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj1,
 <a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj2)</span></div>
<div class="block">Check if two given MagicDraw projects are equals by comparing their model elements and diagrams.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prj1</code> - first MagicDraw project to compare.</dd>
<dd><code>prj2</code> - second MagicDraw project to compare.</dd>
<dt>Returns:</dt>
<dd>true if given MagicDraw projects are equals, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModelComparator()">
<h3>getModelComparator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ModelComparator.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">ModelComparator</a></span> <span class="element-name">getModelComparator</span>()</div>
<div class="block">ModelComparator implementation used for projects comparison.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>implementation of ModelComparator used for projects comparison or null if projects compared
 using other criterion.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setModelComparator(com.nomagic.magicdraw.tests.common.comparators.ModelComparator)">
<h3>setModelComparator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setModelComparator</span><wbr/><span class="parameters">(<a href="ModelComparator.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">ModelComparator</a> comparator)</span></div>
<div class="block">Set implementation of ModelComparator to use for projects comparison.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>comparator</code> - implementation of ModelComparator to use for projects comparison.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramComparator()">
<h3>getDiagramComparator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="DiagramComparator.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">DiagramComparator</a></span> <span class="element-name">getDiagramComparator</span>()</div>
<div class="block">DiagramComparator used for comparing project diagrams during projects comparison.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>implementation of DiagramComparator used for comparing diagrams or null if
 projects are compared by other criterion.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDiagramComparator(com.nomagic.magicdraw.tests.common.comparators.DiagramComparator)">
<h3>setDiagramComparator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDiagramComparator</span><wbr/><span class="parameters">(@CheckForNull
 <a href="DiagramComparator.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">DiagramComparator</a> diagramComparator)</span></div>
<div class="block">Sets DiagramComparator implementation for comparing project diagrams during projects comparison.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramComparator</code> - implementation of DiagramComparator use for project diagrams comparison.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLogTextEnd(java.lang.String)">
<h3>setLogTextEnd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLogTextEnd</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Text to add before projects comparison log.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - String text to add.</dd>
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
