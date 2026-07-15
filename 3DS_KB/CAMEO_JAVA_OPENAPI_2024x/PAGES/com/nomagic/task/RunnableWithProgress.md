# JAVA OPENAPI: RunnableWithProgress (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/task/RunnableWithProgress.html
- source_path: `com/nomagic/task/RunnableWithProgress.html`
- source_sha256: `f80f5271342fc013a46ee82d382a414d4849ccb68c95dce4fbd2771d7b3fe812`
- captured_utc: `2026-07-14T16:52:32.539156+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.task](package-summary.html)

## Interface RunnableWithProgress

@OpenApiAllpublic interfaceRunnableWithProgress
Runnable for executing code with progress status. 

// create runnable
 RunnableWithProgress runnable = new RunnableWithProgress()
 {
 public void run(ProgressStatus progressStatus)
 {
 int max = Integer.MAX_VALUE;
 progressStatus.init("Counting...", 0, max);
 for (int i = 0; i < max; ++i)
 {
 if (progressStatus.isCancel())
 {
 // cancel clicked
 return;
 }
 progressStatus.increase();
 }
 }
 };
 // run with progress
 ProgressStatusRunner.runWithProgressStatus(runnable, "My progress", true, 0);

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[run](#run(com.nomagic.task.ProgressStatus))([ProgressStatus](ProgressStatus.html) progressStatus)`
Performs task with progress status.

============ METHOD DETAIL ========== 
Method Details
run
void run([ProgressStatus](ProgressStatus.html) progressStatus)
Performs task with progress status.
 The method should (initialize and) update the progress status to reflect the actual task progress.
Parameters:
`progressStatus` - progress
See Also:
[`ProgressStatus`](ProgressStatus.html)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.task</a></div>
<h1 class="title" title="Interface RunnableWithProgress">Interface RunnableWithProgress</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">RunnableWithProgress</span></div>
<div class="block">Runnable for executing code with progress status.<br/>
<pre>

        // create runnable
        RunnableWithProgress runnable = new RunnableWithProgress()
    {
                public void run(ProgressStatus progressStatus)
        {
                        int max = Integer.MAX_VALUE;
                        progressStatus.init("Counting...", 0, max);
                        for (int i = 0; i &lt; max; ++i)
            {
                                if (progressStatus.isCancel())
                {
                                        // cancel clicked
                                        return;
                }
                                progressStatus.increase();
            }
        }
    };
        // run with progress
        ProgressStatusRunner.runWithProgressStatus(runnable, "My progress", true, 0);
 </pre></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#run(com.nomagic.task.ProgressStatus)">run</a><wbr/>(<a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Performs task with progress status.</div>
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
<section class="detail" id="run(com.nomagic.task.ProgressStatus)">
<h3>run</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">run</span><wbr/><span class="parameters">(<a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</span></div>
<div class="block">Performs task with progress status.
 The method should (initialize and) update the progress status to reflect the actual task progress.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>progressStatus</code> - progress</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="ProgressStatus.html" title="interface in com.nomagic.task"><code>ProgressStatus</code></a></li>
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
