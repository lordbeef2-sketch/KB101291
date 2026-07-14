# JAVA OPENAPI: IdleJobService (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/job/IdleJobService.html
- source_path: `com/nomagic/magicdraw/job/IdleJobService.html`
- source_sha256: `ff22da77e48f16801fdca150af6ee87fa4ee4e4c6d01a86dff1e6be442a6f296`
- captured_utc: `2026-07-14T16:51:23.247229+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.job](package-summary.html)

## Class IdleJobService

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.job.IdleJobService

@OpenApiAllpublic final classIdleJobService
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Idle job service allows to add jobs which can be executed when application is idle.
 Application decides when it is the most appropriate to execute the job without
 getting application into an inconsistent state.
 Example usage:
 Job job = new Job()
 {
 public boolean needsExecute()
 {
 return true;
 }

 public void execute(ProgressStatus progressStatus) throws Exception
 {
 // Do necessary work in the session.
 }

 public void finished()
 {
 // Cleanup after job is finished.
 }

 public String getName()
 {
 return "My Job";
 }
 };

 IdleJobService.getInstance().addJob(job);

 // Remove the job when it is no longer necessary.
 IdleJobService.getInstance().removeJob(job);

 For more information please refer to the JobExample in the examples directory.

See Also:
[`Job`](Job.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addJob](#addJob(com.nomagic.magicdraw.job.Job))([Job](Job.html) job)`
Adds a job to the service to run every two seconds
 If the same job was added previously, it will be first canceled and then re-added
 Method is thread safe.
`void`
`[addJob](#addJob(com.nomagic.magicdraw.job.Job,long,int,boolean))([Job](Job.html) job,
 long interval,
 int sessionCompletionDelay,
 boolean onIdle)`
Adds a job to the service to repeatedly run on the given interval
 If the same job was added previously, it will be canceled and re-added
`static [IdleJobService](IdleJobService.html)`
`[getInstance](#getInstance())()`
Gets the singleton job service.
`void`
`[removeJob](#removeJob(com.nomagic.magicdraw.job.Job))([Job](Job.html) job)`
Removes job from the service.
`void`
`[runJob](#runJob(com.nomagic.magicdraw.job.Job))([Job](Job.html) job)`
Immediately runs the job, without checking if it needs to run
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
public static [IdleJobService](IdleJobService.html) getInstance()
Gets the singleton job service.
Returns:
job service.
addJob
public void addJob([Job](Job.html) job)
Adds a job to the service to run every two seconds
 If the same job was added previously, it will be first canceled and then re-added
 Method is thread safe.
Parameters:
`job` - to add to the service.
addJob
public void addJob([Job](Job.html) job,
 long interval,
 int sessionCompletionDelay,
 boolean onIdle)
Adds a job to the service to repeatedly run on the given interval
 If the same job was added previously, it will be canceled and re-added
Parameters:
`job` - a job to execute
`interval` - duration between two executions of the same interval seconds.
`sessionCompletionDelay` - how many seconds must past from the last session close. See [`SessionManager`](../openapi/uml/SessionManager.html)
`onIdle` - only execute this job when MagicDraw is idle for the provided interval of seconds
 Method is thread safe.
removeJob
public void removeJob([Job](Job.html) job)
Removes job from the service.
 Method is thread safe.
Parameters:
`job` - rule to remove
runJob
public void runJob([Job](Job.html) job)
Immediately runs the job, without checking if it needs to run
Parameters:
`job` - job that was previously added to the this service

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.job</a></div>
<h1 class="title" title="Class IdleJobService">Class IdleJobService</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.job.IdleJobService</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">IdleJobService</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Idle job service allows to add jobs which can be executed when application is idle.
 <p>
 Application decides when it is the most appropriate to execute the job without
 getting application into an inconsistent state.
 <p>
 Example usage:
 <pre>
 Job job = new Job()
 {
     public boolean needsExecute()
     {
         return true;
     }

     public void execute(ProgressStatus progressStatus) throws Exception
     {
         // Do necessary work in the session.
     }

     public void finished()
     {
         // Cleanup after job is finished.
     }

     public String getName()
     {
         return "My Job";
     }
 };

 IdleJobService.getInstance().addJob(job);

 // Remove the job when it is no longer necessary.
 IdleJobService.getInstance().removeJob(job);

 For more information please refer to the JobExample in the examples directory.
 </pre></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="Job.html" title="interface in com.nomagic.magicdraw.job"><code>Job</code></a></li>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addJob(com.nomagic.magicdraw.job.Job)">addJob</a><wbr/>(<a href="Job.html" title="interface in com.nomagic.magicdraw.job">Job</a> job)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a job to the service to run every two seconds
 If the same job was added previously, it will be first canceled and then re-added
 Method is thread safe.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addJob(com.nomagic.magicdraw.job.Job,long,int,boolean)">addJob</a><wbr/>(<a href="Job.html" title="interface in com.nomagic.magicdraw.job">Job</a> job,
 long interval,
 int sessionCompletionDelay,
 boolean onIdle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a job to the service to repeatedly run on the given interval
 If the same job was added previously, it will be canceled and re-added</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="IdleJobService.html" title="class in com.nomagic.magicdraw.job">IdleJobService</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the singleton job service.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeJob(com.nomagic.magicdraw.job.Job)">removeJob</a><wbr/>(<a href="Job.html" title="interface in com.nomagic.magicdraw.job">Job</a> job)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes job from the service.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#runJob(com.nomagic.magicdraw.job.Job)">runJob</a><wbr/>(<a href="Job.html" title="interface in com.nomagic.magicdraw.job">Job</a> job)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Immediately runs the job, without checking if it needs to run</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="IdleJobService.html" title="class in com.nomagic.magicdraw.job">IdleJobService</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Gets the singleton job service.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>job service.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addJob(com.nomagic.magicdraw.job.Job)">
<h3>addJob</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addJob</span><wbr/><span class="parameters">(<a href="Job.html" title="interface in com.nomagic.magicdraw.job">Job</a> job)</span></div>
<div class="block">Adds a job to the service to run every two seconds
 If the same job was added previously, it will be first canceled and then re-added
 Method is thread safe.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>job</code> - to add to the service.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addJob(com.nomagic.magicdraw.job.Job,long,int,boolean)">
<h3>addJob</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addJob</span><wbr/><span class="parameters">(<a href="Job.html" title="interface in com.nomagic.magicdraw.job">Job</a> job,
 long interval,
 int sessionCompletionDelay,
 boolean onIdle)</span></div>
<div class="block">Adds a job to the service to repeatedly run on the given interval
 If the same job was added previously, it will be canceled and re-added</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>job</code> - a job to execute</dd>
<dd><code>interval</code> - duration between two executions of the same interval seconds.</dd>
<dd><code>sessionCompletionDelay</code> - how many seconds must past from the last session close. See <a href="../openapi/uml/SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>SessionManager</code></a></dd>
<dd><code>onIdle</code> - only execute this job when MagicDraw is idle for the provided interval of seconds
                               Method is thread safe.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeJob(com.nomagic.magicdraw.job.Job)">
<h3>removeJob</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeJob</span><wbr/><span class="parameters">(<a href="Job.html" title="interface in com.nomagic.magicdraw.job">Job</a> job)</span></div>
<div class="block">Removes job from the service.
 Method is thread safe.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>job</code> - rule to remove</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="runJob(com.nomagic.magicdraw.job.Job)">
<h3>runJob</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">runJob</span><wbr/><span class="parameters">(<a href="Job.html" title="interface in com.nomagic.magicdraw.job">Job</a> job)</span></div>
<div class="block">Immediately runs the job, without checking if it needs to run</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>job</code> - job that was previously added to the this service</dd>
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
