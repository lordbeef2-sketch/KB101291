# JAVA OPENAPI: MagicDrawProgressStatusRunner (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/ui/MagicDrawProgressStatusRunner.html
- source_path: `com/nomagic/magicdraw/ui/MagicDrawProgressStatusRunner.html`
- source_sha256: `d0e6799db2a2da5c543224a33e96ef4dc3cefd84b20513882971f203cdc2289e`
- captured_utc: `2026-07-14T16:52:00.921732+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Class MagicDrawProgressStatusRunner

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.MagicDrawProgressStatusRunner

@OpenApiAllpublic classMagicDrawProgressStatusRunner
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Runs MagicDraw related task with progress status.

See Also:
[`RunnableWithProgress`](../../task/RunnableWithProgress.html)
[`ProgressStatus`](../../task/ProgressStatus.html)
[`ProgressStatusRunner`](../../ui/ProgressStatusRunner.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MagicDrawProgressStatusRunner](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[runWithProgressStatus](#runWithProgressStatus(com.nomagic.magicdraw.core.Project,com.nomagic.task.RunnableWithProgress,java.lang.String,boolean,int))([Project](../core/Project.html) project,
 [RunnableWithProgress](../../task/RunnableWithProgress.html) runnable,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 boolean allowCancel,
 int millisToShow)`
Executes runnable with progress status.
`static void`
`[runWithProgressStatus](#runWithProgressStatus(com.nomagic.task.RunnableWithProgress,java.lang.String,boolean,int))([RunnableWithProgress](../../task/RunnableWithProgress.html) runnable,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 boolean allowCancel,
 int millisToShow)`
Executes runnable with progress status.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MagicDrawProgressStatusRunner
public MagicDrawProgressStatusRunner()
 ============ METHOD DETAIL ========== 
Method Details
runWithProgressStatus
public static void runWithProgressStatus([RunnableWithProgress](../../task/RunnableWithProgress.html) runnable,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 boolean allowCancel,
 int millisToShow)
Executes runnable with progress status.
 **MagicDraw UI environment is locked (not updated) during execution, it is updated when task finishes.**
 All runtime exceptions from runnable are thrown from this method.
Parameters:
`runnable` - runnable actually performing the task
`description` - title of progress bar
`allowCancel` - true if cancel should be enabled
`millisToShow` - amount of time before progress is displayed. Pass 0 if progress should be displayed without delay
See Also:
[`RunnableWithProgress`](../../task/RunnableWithProgress.html)
[`ProgressStatus`](../../task/ProgressStatus.html)
runWithProgressStatus
public static void runWithProgressStatus([Project](../core/Project.html) project,
 [RunnableWithProgress](../../task/RunnableWithProgress.html) runnable,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 boolean allowCancel,
 int millisToShow)
Executes runnable with progress status.
 **MagicDraw UI environment is locked (not updated) during execution, diagrams in the given project are not repainted. Everything is updated when task finishes.**
 All runtime exceptions from runnable are thrown from this method.
Parameters:
`project` - active project
`runnable` - runnable actually performing the task
`description` - title of progress bar
`allowCancel` - true if cancel should be enabled
`millisToShow` - amount of time before progress is displayed. Pass 0 if progress should be displayed without delay
See Also:
[`RunnableWithProgress`](../../task/RunnableWithProgress.html)
[`ProgressStatus`](../../task/ProgressStatus.html)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Class MagicDrawProgressStatusRunner">Class MagicDrawProgressStatusRunner</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.MagicDrawProgressStatusRunner</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MagicDrawProgressStatusRunner</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Runs MagicDraw related task with progress status.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../task/RunnableWithProgress.html" title="interface in com.nomagic.task"><code>RunnableWithProgress</code></a></li>
<li><a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task"><code>ProgressStatus</code></a></li>
<li><a href="../../ui/ProgressStatusRunner.html" title="class in com.nomagic.ui"><code>ProgressStatusRunner</code></a></li>
</ul>
</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MagicDrawProgressStatusRunner</a>()</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#runWithProgressStatus(com.nomagic.magicdraw.core.Project,com.nomagic.task.RunnableWithProgress,java.lang.String,boolean,int)">runWithProgressStatus</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../task/RunnableWithProgress.html" title="interface in com.nomagic.task">RunnableWithProgress</a> runnable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 boolean allowCancel,
 int millisToShow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes runnable with progress status.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#runWithProgressStatus(com.nomagic.task.RunnableWithProgress,java.lang.String,boolean,int)">runWithProgressStatus</a><wbr/>(<a href="../../task/RunnableWithProgress.html" title="interface in com.nomagic.task">RunnableWithProgress</a> runnable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 boolean allowCancel,
 int millisToShow)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes runnable with progress status.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>MagicDrawProgressStatusRunner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MagicDrawProgressStatusRunner</span>()</div>
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
<section class="detail" id="runWithProgressStatus(com.nomagic.task.RunnableWithProgress,java.lang.String,boolean,int)">
<h3>runWithProgressStatus</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">runWithProgressStatus</span><wbr/><span class="parameters">(<a href="../../task/RunnableWithProgress.html" title="interface in com.nomagic.task">RunnableWithProgress</a> runnable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 boolean allowCancel,
 int millisToShow)</span></div>
<div class="block">Executes runnable with progress status.
 <strong>MagicDraw UI environment is locked (not updated) during execution, it is updated when task finishes.</strong>
 All runtime exceptions from runnable are thrown from this method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runnable</code> - runnable actually performing the task</dd>
<dd><code>description</code> - title of progress bar</dd>
<dd><code>allowCancel</code> - true if cancel should be enabled</dd>
<dd><code>millisToShow</code> - amount of time before progress is displayed. Pass 0 if progress should be displayed without delay</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../task/RunnableWithProgress.html" title="interface in com.nomagic.task"><code>RunnableWithProgress</code></a></li>
<li><a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task"><code>ProgressStatus</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="runWithProgressStatus(com.nomagic.magicdraw.core.Project,com.nomagic.task.RunnableWithProgress,java.lang.String,boolean,int)">
<h3>runWithProgressStatus</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">runWithProgressStatus</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../task/RunnableWithProgress.html" title="interface in com.nomagic.task">RunnableWithProgress</a> runnable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 boolean allowCancel,
 int millisToShow)</span></div>
<div class="block">Executes runnable with progress status.
 <strong>MagicDraw UI environment is locked (not updated) during execution, diagrams in the given project are not repainted. Everything is updated when task finishes.</strong>
 All runtime exceptions from runnable are thrown from this method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - active project</dd>
<dd><code>runnable</code> - runnable actually performing the task</dd>
<dd><code>description</code> - title of progress bar</dd>
<dd><code>allowCancel</code> - true if cancel should be enabled</dd>
<dd><code>millisToShow</code> - amount of time before progress is displayed. Pass 0 if progress should be displayed without delay</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../task/RunnableWithProgress.html" title="interface in com.nomagic.task"><code>RunnableWithProgress</code></a></li>
<li><a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task"><code>ProgressStatus</code></a></li>
</ul>
</dd>
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
