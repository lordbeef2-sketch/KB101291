# JAVA OPENAPI: SimpleProgressStatus (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/task/SimpleProgressStatus.html
- source_path: `com/nomagic/task/SimpleProgressStatus.html`
- source_sha256: `8f77c5585a3f78a3ae7591d1f7ad29ca3dc5ae5d09e15fed1abc3bd0b087956e`
- captured_utc: `2026-07-14T16:56:02.750539+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.task](package-summary.html)

## Class SimpleProgressStatus

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.task.SimpleProgressStatus

All Implemented Interfaces:
`[ProgressStatus](ProgressStatus.html)`

@OpenApiAllpublic classSimpleProgressStatus
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [ProgressStatus](ProgressStatus.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SimpleProgressStatus](#%3Cinit%3E())()`

`[SimpleProgressStatus](#%3Cinit%3E(long,long,java.lang.String))(long min,
 long max,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`long`
`[getCurrent](#getCurrent())()`
Get current progress value.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
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
`[init](#init(java.lang.String,long))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 long max)`
Initialize progress.
`void`
`[init](#init(java.lang.String,long,long))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 long min,
 long max)`
Initialize progress.
`void`
`[init](#init(java.lang.String,long,long,long))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 long min,
 long max,
 long cur)`
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
`[setCurrent](#setCurrent(long))(long cur)`
Set progress current value.
`void`
`[setDescription](#setDescription(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)`
Set progress description.
`void`
`[setIndeterminate](#setIndeterminate(boolean))(boolean ind)`
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
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.task.[ProgressStatus](ProgressStatus.html)
`[cancelIfCanceled](ProgressStatus.html#cancelIfCanceled())`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SimpleProgressStatus
public SimpleProgressStatus()
SimpleProgressStatus
public SimpleProgressStatus(long min,
 long max,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)
 ============ METHOD DETAIL ========== 
Method Details
setMin
public void setMin(long min)
Description copied from interface: `[ProgressStatus](ProgressStatus.html#setMin(long))`
Set progress minimum value.
Specified by:
`[setMin](ProgressStatus.html#setMin(long))` in interface `[ProgressStatus](ProgressStatus.html)`
Parameters:
`min` - minimum value
setMax
public void setMax(long max)
Description copied from interface: `[ProgressStatus](ProgressStatus.html#setMax(long))`
Set progress maximum value.
Specified by:
`[setMax](ProgressStatus.html#setMax(long))` in interface `[ProgressStatus](ProgressStatus.html)`
Parameters:
`max` - maximum value
setCurrent
public void setCurrent(long cur)
Description copied from interface: `[ProgressStatus](ProgressStatus.html#setCurrent(long))`
Set progress current value.
Specified by:
`[setCurrent](ProgressStatus.html#setCurrent(long))` in interface `[ProgressStatus](ProgressStatus.html)`
Parameters:
`cur` - current value
getMin
public long getMin()
Description copied from interface: `[ProgressStatus](ProgressStatus.html#getMin())`
Get progress minimum value.
Specified by:
`[getMin](ProgressStatus.html#getMin())` in interface `[ProgressStatus](ProgressStatus.html)`
Returns:
minimum value
getMax
public long getMax()
Description copied from interface: `[ProgressStatus](ProgressStatus.html#getMax())`
Get progress maximum value.
Specified by:
`[getMax](ProgressStatus.html#getMax())` in interface `[ProgressStatus](ProgressStatus.html)`
Returns:
maximum value
reset
public void reset()
Description copied from interface: `[ProgressStatus](ProgressStatus.html#reset())`
Reset progress status.
Specified by:
`[reset](ProgressStatus.html#reset())` in interface `[ProgressStatus](ProgressStatus.html)`
getPercentage
public int getPercentage()
Description copied from interface: `[ProgressStatus](ProgressStatus.html#getPercentage())`
Get completed percentage.
Specified by:
`[getPercentage](ProgressStatus.html#getPercentage())` in interface `[ProgressStatus](ProgressStatus.html)`
Returns:
completed percentage
getDescription
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescription()
Description copied from interface: `[ProgressStatus](ProgressStatus.html#getDescription())`
Get progress description.
Specified by:
`[getDescription](ProgressStatus.html#getDescription())` in interface `[ProgressStatus](ProgressStatus.html)`
Returns:
progress description
setDescription
public void setDescription([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)
Description copied from interface: `[ProgressStatus](ProgressStatus.html#setDescription(java.lang.String))`
Set progress description.
Specified by:
`[setDescription](ProgressStatus.html#setDescription(java.lang.String))` in interface `[ProgressStatus](ProgressStatus.html)`
Parameters:
`description` - progress description
increase
public void increase()
Description copied from interface: `[ProgressStatus](ProgressStatus.html#increase())`
Increment progress current value.
Specified by:
`[increase](ProgressStatus.html#increase())` in interface `[ProgressStatus](ProgressStatus.html)`
getCurrent
public long getCurrent()
Description copied from interface: `[ProgressStatus](ProgressStatus.html#getCurrent())`
Get current progress value.
Specified by:
`[getCurrent](ProgressStatus.html#getCurrent())` in interface `[ProgressStatus](ProgressStatus.html)`
Returns:
current value
isCompleted
public boolean isCompleted()
Description copied from interface: `[ProgressStatus](ProgressStatus.html#isCompleted())`
Checks if progress status completed.
Specified by:
`[isCompleted](ProgressStatus.html#isCompleted())` in interface `[ProgressStatus](ProgressStatus.html)`
Returns:
`true when progress status completed`
setIndeterminate
public void setIndeterminate(boolean ind)
Description copied from interface: `[ProgressStatus](ProgressStatus.html#setIndeterminate(boolean))`
Set progress status as indeterminate.
Specified by:
`[setIndeterminate](ProgressStatus.html#setIndeterminate(boolean))` in interface `[ProgressStatus](ProgressStatus.html)`
Parameters:
`ind` - `true for progress status as indeterminate.`
isIndeterminate
public boolean isIndeterminate()
Description copied from interface: `[ProgressStatus](ProgressStatus.html#isIndeterminate())`
Checks if progress status is indeterminate,
Specified by:
`[isIndeterminate](ProgressStatus.html#isIndeterminate())` in interface `[ProgressStatus](ProgressStatus.html)`
Returns:
`true when progress status as indeterminate.`
setLocked
public void setLocked(boolean lock)
Description copied from interface: `[ProgressStatus](ProgressStatus.html#setLocked(boolean))`
Lock the progress status. Locked status does not change progress value.
Specified by:
`[setLocked](ProgressStatus.html#setLocked(boolean))` in interface `[ProgressStatus](ProgressStatus.html)`
Parameters:
`lock` - `true for progress status locking.`
isLocked
public boolean isLocked()
Description copied from interface: `[ProgressStatus](ProgressStatus.html#isLocked())`
Check if progress status is locked.
Specified by:
`[isLocked](ProgressStatus.html#isLocked())` in interface `[ProgressStatus](ProgressStatus.html)`
Returns:
`true when progress status is locked.`
init
public void init([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 long min,
 long max,
 long cur)
Description copied from interface: `[ProgressStatus](ProgressStatus.html#init(java.lang.String,long,long,long))`
Initialize progress.
Specified by:
`[init](ProgressStatus.html#init(java.lang.String,long,long,long))` in interface `[ProgressStatus](ProgressStatus.html)`
Parameters:
`description` - progress description.
`min` - minimum value.
`max` - maximum value.
`cur` - current value.
init
public void init([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 long min,
 long max)
Description copied from interface: `[ProgressStatus](ProgressStatus.html#init(java.lang.String,long,long))`
Initialize progress.
Specified by:
`[init](ProgressStatus.html#init(java.lang.String,long,long))` in interface `[ProgressStatus](ProgressStatus.html)`
Parameters:
`description` - progress description.
`min` - minimum value.
`max` - maximum value.
init
public void init([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 long max)
Description copied from interface: `[ProgressStatus](ProgressStatus.html#init(java.lang.String,long))`
Initialize progress.
Specified by:
`[init](ProgressStatus.html#init(java.lang.String,long))` in interface `[ProgressStatus](ProgressStatus.html)`
Parameters:
`description` - progress description.
`max` - maximum value.
isCancel
public boolean isCancel()
Specified by:
`[isCancel](ProgressStatus.html#isCancel())` in interface `[ProgressStatus](ProgressStatus.html)`
Returns:
true if current operation is requested to be canceled.
setCancel
public void setCancel(boolean cancel)
Description copied from interface: `[ProgressStatus](ProgressStatus.html#setCancel(boolean))`
Call this when want current operation be canceled. Actual operation can not support cancel.
Specified by:
`[setCancel](ProgressStatus.html#setCancel(boolean))` in interface `[ProgressStatus](ProgressStatus.html)`
Parameters:
`cancel` - new cancel value.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.task</a></div>
<h1 class="title" title="Class SimpleProgressStatus">Class SimpleProgressStatus</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.task.SimpleProgressStatus</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SimpleProgressStatus</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></span></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SimpleProgressStatus</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(long,long,java.lang.String)">SimpleProgressStatus</a><wbr/>(long min,
 long max,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCurrent()">getCurrent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get current progress value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescription()">getDescription</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get progress description.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMax()">getMax</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get progress maximum value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMin()">getMin</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get progress minimum value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPercentage()">getPercentage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get completed percentage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#increase()">increase</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Increment progress current value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init(java.lang.String,long)">init</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 long max)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initialize progress.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init(java.lang.String,long,long)">init</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 long min,
 long max)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initialize progress.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init(java.lang.String,long,long,long)">init</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 long min,
 long max,
 long cur)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initialize progress.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCancel()">isCancel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCompleted()">isCompleted</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if progress status completed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isIndeterminate()">isIndeterminate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if progress status is indeterminate,</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLocked()">isLocked</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if progress status is locked.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reset()">reset</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Reset progress status.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCancel(boolean)">setCancel</a><wbr/>(boolean cancel)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call this when want current operation be canceled.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCurrent(long)">setCurrent</a><wbr/>(long cur)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set progress current value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDescription(java.lang.String)">setDescription</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set progress description.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIndeterminate(boolean)">setIndeterminate</a><wbr/>(boolean ind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set progress status as indeterminate.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLocked(boolean)">setLocked</a><wbr/>(boolean lock)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Lock the progress status.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMax(long)">setMax</a><wbr/>(long max)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set progress maximum value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMin(long)">setMin</a><wbr/>(long min)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set progress minimum value.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.task.ProgressStatus">Methods inherited from interface com.nomagic.task.<a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></h3>
<code><a href="ProgressStatus.html#cancelIfCanceled()">cancelIfCanceled</a></code></div>
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
<h3>SimpleProgressStatus</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SimpleProgressStatus</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(long,long,java.lang.String)">
<h3>SimpleProgressStatus</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SimpleProgressStatus</span><wbr/><span class="parameters">(long min,
 long max,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</span></div>
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
<section class="detail" id="setMin(long)">
<h3>setMin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMin</span><wbr/><span class="parameters">(long min)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#setMin(long)">ProgressStatus</a></code></span></div>
<div class="block">Set progress minimum value.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#setMin(long)">setMin</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Parameters:</dt>
<dd><code>min</code> - minimum value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMax(long)">
<h3>setMax</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMax</span><wbr/><span class="parameters">(long max)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#setMax(long)">ProgressStatus</a></code></span></div>
<div class="block">Set progress maximum value.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#setMax(long)">setMax</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Parameters:</dt>
<dd><code>max</code> - maximum value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCurrent(long)">
<h3>setCurrent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCurrent</span><wbr/><span class="parameters">(long cur)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#setCurrent(long)">ProgressStatus</a></code></span></div>
<div class="block">Set progress current value.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#setCurrent(long)">setCurrent</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Parameters:</dt>
<dd><code>cur</code> - current value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMin()">
<h3>getMin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getMin</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#getMin()">ProgressStatus</a></code></span></div>
<div class="block">Get progress minimum value.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#getMin()">getMin</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Returns:</dt>
<dd>minimum value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMax()">
<h3>getMax</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getMax</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#getMax()">ProgressStatus</a></code></span></div>
<div class="block">Get progress maximum value.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#getMax()">getMax</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Returns:</dt>
<dd>maximum value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reset()">
<h3>reset</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reset</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#reset()">ProgressStatus</a></code></span></div>
<div class="block">Reset progress status.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#reset()">reset</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPercentage()">
<h3>getPercentage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPercentage</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#getPercentage()">ProgressStatus</a></code></span></div>
<div class="block">Get completed percentage.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#getPercentage()">getPercentage</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Returns:</dt>
<dd>completed percentage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#getDescription()">ProgressStatus</a></code></span></div>
<div class="block">Get progress description.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#getDescription()">getDescription</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Returns:</dt>
<dd>progress description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDescription(java.lang.String)">
<h3>setDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDescription</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#setDescription(java.lang.String)">ProgressStatus</a></code></span></div>
<div class="block">Set progress description.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#setDescription(java.lang.String)">setDescription</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Parameters:</dt>
<dd><code>description</code> - progress description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="increase()">
<h3>increase</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">increase</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#increase()">ProgressStatus</a></code></span></div>
<div class="block">Increment progress current value.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#increase()">increase</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCurrent()">
<h3>getCurrent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getCurrent</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#getCurrent()">ProgressStatus</a></code></span></div>
<div class="block">Get current progress value.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#getCurrent()">getCurrent</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Returns:</dt>
<dd>current value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCompleted()">
<h3>isCompleted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCompleted</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#isCompleted()">ProgressStatus</a></code></span></div>
<div class="block">Checks if progress status completed.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#isCompleted()">isCompleted</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Returns:</dt>
<dd><code>true<code></code> when progress status completed</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIndeterminate(boolean)">
<h3>setIndeterminate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIndeterminate</span><wbr/><span class="parameters">(boolean ind)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#setIndeterminate(boolean)">ProgressStatus</a></code></span></div>
<div class="block">Set progress status as indeterminate.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#setIndeterminate(boolean)">setIndeterminate</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Parameters:</dt>
<dd><code>ind</code> - <code>true<code></code> for progress status as indeterminate.</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isIndeterminate()">
<h3>isIndeterminate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isIndeterminate</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#isIndeterminate()">ProgressStatus</a></code></span></div>
<div class="block">Checks if progress status is indeterminate,</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#isIndeterminate()">isIndeterminate</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Returns:</dt>
<dd><code>true<code></code> when progress status as indeterminate.</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLocked(boolean)">
<h3>setLocked</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLocked</span><wbr/><span class="parameters">(boolean lock)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#setLocked(boolean)">ProgressStatus</a></code></span></div>
<div class="block">Lock the progress status. Locked status does not change progress value.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#setLocked(boolean)">setLocked</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Parameters:</dt>
<dd><code>lock</code> - <code>true<code></code> for progress status locking.</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLocked()">
<h3>isLocked</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLocked</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#isLocked()">ProgressStatus</a></code></span></div>
<div class="block">Check if progress status is locked.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#isLocked()">isLocked</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Returns:</dt>
<dd><code>true<code></code> when progress status is locked.</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="init(java.lang.String,long,long,long)">
<h3>init</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 long min,
 long max,
 long cur)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#init(java.lang.String,long,long,long)">ProgressStatus</a></code></span></div>
<div class="block">Initialize progress.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#init(java.lang.String,long,long,long)">init</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Parameters:</dt>
<dd><code>description</code> - progress description.</dd>
<dd><code>min</code> - minimum value.</dd>
<dd><code>max</code> - maximum value.</dd>
<dd><code>cur</code> - current value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="init(java.lang.String,long,long)">
<h3>init</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 long min,
 long max)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#init(java.lang.String,long,long)">ProgressStatus</a></code></span></div>
<div class="block">Initialize progress.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#init(java.lang.String,long,long)">init</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 long max)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#init(java.lang.String,long)">ProgressStatus</a></code></span></div>
<div class="block">Initialize progress.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#init(java.lang.String,long)">init</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Parameters:</dt>
<dd><code>description</code> - progress description.</dd>
<dd><code>max</code> - maximum value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCancel()">
<h3>isCancel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCancel</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#isCancel()">isCancel</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Returns:</dt>
<dd>true if current operation is requested to be canceled.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCancel(boolean)">
<h3>setCancel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCancel</span><wbr/><span class="parameters">(boolean cancel)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProgressStatus.html#setCancel(boolean)">ProgressStatus</a></code></span></div>
<div class="block">Call this when want current operation be canceled. Actual operation can not support cancel.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProgressStatus.html#setCancel(boolean)">setCancel</a></code> in interface <code><a href="ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></dd>
<dt>Parameters:</dt>
<dd><code>cancel</code> - new cancel value.</dd>
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
