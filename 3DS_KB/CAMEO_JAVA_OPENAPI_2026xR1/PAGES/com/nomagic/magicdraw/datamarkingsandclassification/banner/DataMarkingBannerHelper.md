# JAVA OPENAPI: DataMarkingBannerHelper (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/datamarkingsandclassification/banner/DataMarkingBannerHelper.html
- source_path: `com/nomagic/magicdraw/datamarkingsandclassification/banner/DataMarkingBannerHelper.html`
- source_sha256: `152287227f0382ec6bde3aee87d85b1a77ed91ac1186e6a5f6022c2de73fcda7`
- captured_utc: `2026-07-14T16:45:31.779426+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.datamarkingsandclassification.banner](package-summary.html)

## Class DataMarkingBannerHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.datamarkingsandclassification.banner.DataMarkingBannerHelper

@OpenApiAllpublic classDataMarkingBannerHelper
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Provides API for updating and creating Data Marking banners.
[`updateBannerWithStatus(Project, String, ProgressStatus, boolean, DiagramPresentationElement...)`](#updateBannerWithStatus(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.task.ProgressStatus,boolean,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement...))
 Updates banners in same way as UI action. Also shows same notification.
[`updateBanner(ProgressStatus, boolean, DiagramPresentationElement...)`](#updateBanner(com.nomagic.task.ProgressStatus,boolean,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement...))
 Updates banner and returns [`BannerUpdateResult`](BannerUpdateResult.html) which allows handling of update results like showing of notification in a custom way.
 Does not start session.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DataMarkingBannerHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [BannerUpdateResult](BannerUpdateResult.html)`
`[updateBanner](#updateBanner(com.nomagic.task.ProgressStatus,boolean,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement...))([ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean skipDiagramsWithoutBanners,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html)... diagramPresentationElements)`
Function to create or update diagram data markings banner.
`static void`
`[updateBannerWithStatus](#updateBannerWithStatus(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.task.ProgressStatus,boolean,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement...))([Project](../../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean skipDiagramsWithoutBanners,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html)... diagramPresentationElements)`
Function to create or update diagram data markings banner.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DataMarkingBannerHelper
public DataMarkingBannerHelper()
 ============ METHOD DETAIL ========== 
Method Details
updateBannerWithStatus
public static void updateBannerWithStatus([Project](../../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean skipDiagramsWithoutBanners,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html)... diagramPresentationElements)
Function to create or update diagram data markings banner. This is same function as used from UI and will show same notification.
Parameters:
`project` - project
`sessionName` - name for session
`status` - progress status. Can be null.
`skipDiagramsWithoutBanners` - if true will skip diagrams without banners making it only update banners that already exists.
`diagramPresentationElements` - diagram presentation elements to update data marking banners of.
updateBanner
public static [BannerUpdateResult](BannerUpdateResult.html) updateBanner(@CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean skipDiagramsWithoutBanners,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html)... diagramPresentationElements)
Function to create or update diagram data markings banner.
 Does not create session.
Parameters:
`status` - progress status. Can be null.
`skipDiagramsWithoutBanners` - if true will skip diagrams without banners making it only update banners that already exists.
`diagramPresentationElements` - diagram presentation elements to update data marking banners of.
Returns:
returns [`BannerUpdateResult`](BannerUpdateResult.html) for further processing like showing custom notification.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.datamarkingsandclassification.banner</a></div>
<h1 class="title" title="Class DataMarkingBannerHelper">Class DataMarkingBannerHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.datamarkingsandclassification.banner.DataMarkingBannerHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DataMarkingBannerHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>
 Provides API for updating and creating Data Marking banners.
 </p>
<p>
<a href="#updateBannerWithStatus(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.task.ProgressStatus,boolean,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement...)"><code>updateBannerWithStatus(Project, String, ProgressStatus, boolean, DiagramPresentationElement...)</code></a>
 Updates banners in same way as UI action. Also shows same notification.
 </p>
<p>
<a href="#updateBanner(com.nomagic.task.ProgressStatus,boolean,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement...)"><code>updateBanner(ProgressStatus, boolean, DiagramPresentationElement...)</code></a>
 Updates banner and returns <a href="BannerUpdateResult.html" title="class in com.nomagic.magicdraw.datamarkingsandclassification.banner"><code>BannerUpdateResult</code></a> which allows handling of update results like showing of notification in a custom way.
 Does not start session.
 </p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DataMarkingBannerHelper</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="BannerUpdateResult.html" title="class in com.nomagic.magicdraw.datamarkingsandclassification.banner">BannerUpdateResult</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#updateBanner(com.nomagic.task.ProgressStatus,boolean,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement...)">updateBanner</a><wbr/>(<a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean skipDiagramsWithoutBanners,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>... diagramPresentationElements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Function to create or update diagram data markings banner.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#updateBannerWithStatus(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.task.ProgressStatus,boolean,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement...)">updateBannerWithStatus</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean skipDiagramsWithoutBanners,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>... diagramPresentationElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Function to create or update diagram data markings banner.</div>
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
<h3>DataMarkingBannerHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DataMarkingBannerHelper</span>()</div>
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
<section class="detail" id="updateBannerWithStatus(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.task.ProgressStatus,boolean,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement...)">
<h3>updateBannerWithStatus</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">updateBannerWithStatus</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean skipDiagramsWithoutBanners,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>... diagramPresentationElements)</span></div>
<div class="block">Function to create or update diagram data markings banner. This is same function as used from UI and will show same notification.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>sessionName</code> - name for session</dd>
<dd><code>status</code> - progress status. Can be null.</dd>
<dd><code>skipDiagramsWithoutBanners</code> - if true will skip diagrams without banners making it only update banners that already exists.</dd>
<dd><code>diagramPresentationElements</code> - diagram presentation elements to update data marking banners of.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateBanner(com.nomagic.task.ProgressStatus,boolean,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement...)">
<h3>updateBanner</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="BannerUpdateResult.html" title="class in com.nomagic.magicdraw.datamarkingsandclassification.banner">BannerUpdateResult</a></span> <span class="element-name">updateBanner</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean skipDiagramsWithoutBanners,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>... diagramPresentationElements)</span></div>
<div class="block">Function to create or update diagram data markings banner.
 Does not create session.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>status</code> - progress status. Can be null.</dd>
<dd><code>skipDiagramsWithoutBanners</code> - if true will skip diagrams without banners making it only update banners that already exists.</dd>
<dd><code>diagramPresentationElements</code> - diagram presentation elements to update data marking banners of.</dd>
<dt>Returns:</dt>
<dd>returns <a href="BannerUpdateResult.html" title="class in com.nomagic.magicdraw.datamarkingsandclassification.banner"><code>BannerUpdateResult</code></a> for further processing like showing custom notification.</dd>
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
