# JAVA OPENAPI: ProgressStatus (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/task/ProgressStatus.html
- source_path: `com/nomagic/task/ProgressStatus.html`
- source_sha256: `4d8dc0a4a4f4fd42778baeaada847334348a17052a0c4edf27793904ce0ce15d`
- captured_utc: `2026-07-14T16:46:16.399018+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.task](package-summary.html)

## Interface ProgressStatus

All Known Implementing Classes:
`[EmptyProgressStatus](EmptyProgressStatus.html)`, `[SimpleProgressStatus](SimpleProgressStatus.html)`

@OpenApiAllpublic interfaceProgressStatus

Progress status interface.
 Usually used when performing long task to show task progress status.
 Can be implemented in various ways, represented in GUI.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`default void`
`[cancelIfCanceled](#cancelIfCanceled())()`
Throw `CanceledException` when progress has been canceled.
`long`
`[getCurrent](#getCurrent())()`
Get current progress value.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription())()`
Get progress description.
`long`
`[getMax](#getMax())()`
Get progress maximum value.
`long`
`[getMin](#getMin())()`
Get progress minimum value.
`int`
`[getPercentage](#getPercentage())()`
Get completed percentage.
`void`
`[increase](#increase())()`
Increment progress current value.
`void`
`[init](#init(java.lang.String,long))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description,
 long max)`
Initialize progress.
`void`
`[init](#init(java.lang.String,long,long))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description,
 long min,
 long max)`
Initialize progress.
`void`
`[init](#init(java.lang.String,long,long,long))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description,
 long min,
 long max,
 long current)`
Initialize progress.
`boolean`
`[isCancel](#isCancel())()`

`boolean`
`[isCompleted](#isCompleted())()`
Checks if progress status completed.
`boolean`
`[isIndeterminate](#isIndeterminate())()`
Checks if progress status is indeterminate,
`boolean`
`[isLocked](#isLocked())()`
Check if progress status is locked.
`void`
`[reset](#reset())()`
Reset progress status.
`void`
`[setCancel](#setCancel(boolean))(boolean cancel)`
Call this when want current operation be canceled.
`void`
`[setCurrent](#setCurrent(long))(long current)`
Set progress current value.
`void`
`[setDescription](#setDescription(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description)`
Set progress description.
`void`
`[setIndeterminate](#setIndeterminate(boolean))(boolean indeterminate)`
Set progress status as indeterminate.
`void`
`[setLocked](#setLocked(boolean))(boolean lock)`
Lock the progress status.
`void`
`[setMax](#setMax(long))(long max)`
Set progress maximum value.
`void`
`[setMin](#setMin(long))(long min)`
Set progress minimum value.

============ METHOD DETAIL ========== 
Method Details
setMin
void setMin(long min)
Set progress minimum value.
Parameters:
`min` - minimum value
setMax
void setMax(long max)
Set progress maximum value.
Parameters:
`max` - maximum value
setCurrent
void setCurrent(long current)
Set progress current value.
Parameters:
`current` - current value
setDescription
void setDescription([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description)
Set progress description.
Parameters:
`description` - progress description
getPercentage
int getPercentage()
Get completed percentage.
Returns:
completed percentage
getMin
long getMin()
Get progress minimum value.
Returns:
minimum value
getMax
long getMax()
Get progress maximum value.
Returns:
maximum value
getCurrent
long getCurrent()
Get current progress value.
Returns:
current value
getDescription
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDescription()
Get progress description.
Returns:
progress description
reset
void reset()
Reset progress status.
increase
void increase()
Increment progress current value.
init
void init([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description,
 long min,
 long max,
 long current)
Initialize progress.
Parameters:
`description` - progress description.
`min` - minimum value.
`max` - maximum value.
`current` - current value.
init
void init([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description,
 long min,
 long max)
Initialize progress.
Parameters:
`description` - progress description.
`min` - minimum value.
`max` - maximum value.
init
void init([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description,
 long max)
Initialize progress.
Parameters:
`description` - progress description.
`max` - maximum value.
isCompleted
boolean isCompleted()
Checks if progress status completed.
Returns:
`true when progress status completed`
setIndeterminate
void setIndeterminate(boolean indeterminate)
Set progress status as indeterminate.
Parameters:
`indeterminate` - `true for progress status as indeterminate.`
isIndeterminate
boolean isIndeterminate()
Checks if progress status is indeterminate,
Returns:
`true when progress status as indeterminate.`
setLocked
void setLocked(boolean lock)
Lock the progress status. Locked status does not change progress value.
Parameters:
`lock` - `true for progress status locking.`
isLocked
boolean isLocked()
Check if progress status is locked.
Returns:
`true when progress status is locked.`
setCancel
void setCancel(boolean cancel)
Call this when want current operation be canceled. Actual operation can not support cancel.
Parameters:
`cancel` - new cancel value.
isCancel
boolean isCancel()
Returns:
true if current operation is requested to be canceled.
cancelIfCanceled
default void cancelIfCanceled()
Throw `CanceledException` when progress has been canceled.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.task</a></div>
<h1 class="title" title="Interface ProgressStatus">Interface ProgressStatus</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="EmptyProgressStatus.html" title="class in com.nomagic.task">EmptyProgressStatus</a></code>, <code><a href="SimpleProgressStatus.html" title="class in com.nomagic.task">SimpleProgressStatus</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ProgressStatus</span></div>
<div class="block">Progress status interface.
 Usually used when performing long task to show task progress status.
 Can be implemented in various ways, represented in GUI.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#cancelIfCanceled()">cancelIfCanceled</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Throw <code>CanceledException</code> when progress has been canceled.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCurrent()">getCurrent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get current progress value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDescription()">getDescription</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get progress description.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMax()">getMax</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get progress maximum value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMin()">getMin</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get progress minimum value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPercentage()">getPercentage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get completed percentage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#increase()">increase</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Increment progress current value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#init(java.lang.String,long)">init</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 long max)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Initialize progress.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#init(java.lang.String,long,long)">init</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 long min,
 long max)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Initialize progress.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#init(java.lang.String,long,long,long)">init</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 long min,
 long max,
 long current)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Initialize progress.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isCancel()">isCancel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isCompleted()">isCompleted</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if progress status completed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isIndeterminate()">isIndeterminate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if progress status is indeterminate,</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isLocked()">isLocked</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if progress status is locked.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#reset()">reset</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Reset progress status.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setCancel(boolean)">setCancel</a><wbr/>(boolean cancel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Call this when want current operation be canceled.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setCurrent(long)">setCurrent</a><wbr/>(long current)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set progress current value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDescription(java.lang.String)">setDescription</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set progress description.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIndeterminate(boolean)">setIndeterminate</a><wbr/>(boolean indeterminate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set progress status as indeterminate.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setLocked(boolean)">setLocked</a><wbr/>(boolean lock)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Lock the progress status.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMax(long)">setMax</a><wbr/>(long max)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set progress maximum value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMin(long)">setMin</a><wbr/>(long min)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set progress minimum value.</div>
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
<section class="detail" id="setMin(long)">
<h3>setMin</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMin</span><wbr/><span class="parameters">(long min)</span></div>
<div class="block">Set progress minimum value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>min</code> - minimum value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMax(long)">
<h3>setMax</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMax</span><wbr/><span class="parameters">(long max)</span></div>
<div class="block">Set progress maximum value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>max</code> - maximum value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCurrent(long)">
<h3>setCurrent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setCurrent</span><wbr/><span class="parameters">(long current)</span></div>
<div class="block">Set progress current value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>current</code> - current value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDescription(java.lang.String)">
<h3>setDescription</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDescription</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</span></div>
<div class="block">Set progress description.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>description</code> - progress description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPercentage()">
<h3>getPercentage</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getPercentage</span>()</div>
<div class="block">Get completed percentage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>completed percentage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMin()">
<h3>getMin</h3>
<div class="member-signature"><span class="return-type">long</span> <span class="element-name">getMin</span>()</div>
<div class="block">Get progress minimum value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>minimum value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMax()">
<h3>getMax</h3>
<div class="member-signature"><span class="return-type">long</span> <span class="element-name">getMax</span>()</div>
<div class="block">Get progress maximum value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>maximum value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCurrent()">
<h3>getCurrent</h3>
<div class="member-signature"><span class="return-type">long</span> <span class="element-name">getCurrent</span>()</div>
<div class="block">Get current progress value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>current value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span>()</div>
<div class="block">Get progress description.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>progress description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reset()">
<h3>reset</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">reset</span>()</div>
<div class="block">Reset progress status.</div>
</section>
</li>
<li>
<section class="detail" id="increase()">
<h3>increase</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">increase</span>()</div>
<div class="block">Increment progress current value.</div>
</section>
</li>
<li>
<section class="detail" id="init(java.lang.String,long,long,long)">
<h3>init</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 long min,
 long max,
 long current)</span></div>
<div class="block">Initialize progress.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>description</code> - progress description.</dd>
<dd><code>min</code> - minimum value.</dd>
<dd><code>max</code> - maximum value.</dd>
<dd><code>current</code> - current value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="init(java.lang.String,long,long)">
<h3>init</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 long min,
 long max)</span></div>
<div class="block">Initialize progress.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>description</code> - progress description.</dd>
<dd><code>min</code> - minimum value.</dd>
<dd><code>max</code> - maximum value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="init(java.lang.String,long)">
<h3>init</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 long max)</span></div>
<div class="block">Initialize progress.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>description</code> - progress description.</dd>
<dd><code>max</code> - maximum value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCompleted()">
<h3>isCompleted</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isCompleted</span>()</div>
<div class="block">Checks if progress status completed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true<code></code> when progress status completed</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIndeterminate(boolean)">
<h3>setIndeterminate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIndeterminate</span><wbr/><span class="parameters">(boolean indeterminate)</span></div>
<div class="block">Set progress status as indeterminate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>indeterminate</code> - <code>true<code></code> for progress status as indeterminate.</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isIndeterminate()">
<h3>isIndeterminate</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isIndeterminate</span>()</div>
<div class="block">Checks if progress status is indeterminate,</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true<code></code> when progress status as indeterminate.</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLocked(boolean)">
<h3>setLocked</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setLocked</span><wbr/><span class="parameters">(boolean lock)</span></div>
<div class="block">Lock the progress status. Locked status does not change progress value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lock</code> - <code>true<code></code> for progress status locking.</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLocked()">
<h3>isLocked</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isLocked</span>()</div>
<div class="block">Check if progress status is locked.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true<code></code> when progress status is locked.</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCancel(boolean)">
<h3>setCancel</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setCancel</span><wbr/><span class="parameters">(boolean cancel)</span></div>
<div class="block">Call this when want current operation be canceled. Actual operation can not support cancel.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cancel</code> - new cancel value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCancel()">
<h3>isCancel</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isCancel</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if current operation is requested to be canceled.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="cancelIfCanceled()">
<h3>cancelIfCanceled</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">cancelIfCanceled</span>()</div>
<div class="block">Throw <code>CanceledException</code> when progress has been canceled.</div>
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
