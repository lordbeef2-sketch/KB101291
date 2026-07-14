# JAVA OPENAPI: CommitToBranchExecuter (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/variants/teamwork/CommitToBranchExecuter.html
- source_path: `com/nomagic/magicdraw/variants/teamwork/CommitToBranchExecuter.html`
- source_sha256: `eecb83f29f04b884d5f39708a11f06f8fed15700a83d2a1543b98f58aa1e10b8`
- captured_utc: `2026-07-14T16:52:27.712088+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.variants.teamwork](package-summary.html)

## Class CommitToBranchExecuter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.variants.teamwork.CommitToBranchExecuter

@OpenApiAllpublic abstract classCommitToBranchExecuter
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Commits the provided remote project to the selected branch (that can only be the branch of the same remote project).
 The resulting version of the branch is identical to the source project.
 Current changes to the original (source) project itself are not committed/saved.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CommitToBranchExecuter](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[addErrorMessage](#addErrorMessage(java.lang.String,java.lang.Exception))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html) e)`

`protected void`
`[clearErrorMessages](#clearErrorMessages())()`

`static [CommitToBranchExecuter](CommitToBranchExecuter.html)`
`[createExecuter](#createExecuter(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`

`abstract void`
`[findAndCommit](#findAndCommit(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String,java.util.List,boolean,boolean))([Project](../../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputBranch,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) comment,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> tags,
 boolean unlock,
 boolean retainUsageVersions)`
Finds/creates the branch automatically, and then commits the given project to that branch.
`protected static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getCommitTags](#getCommitTags(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.teamwork2.ui.dialogs.L2RModulesDlg))([Project](../../core/Project.html) project,
 com.nomagic.magicdraw.teamwork2.ui.dialogs.L2RModulesDlg<?> dialog)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getErrorMessages](#getErrorMessages())()`

`abstract void`
`[selectAndCommit](#selectAndCommit(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Shows GUI allowing user to select the branch, add commit comment and tags.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CommitToBranchExecuter
public CommitToBranchExecuter()
 ============ METHOD DETAIL ========== 
Method Details
createExecuter
@CheckForNullpublic static [CommitToBranchExecuter](CommitToBranchExecuter.html) createExecuter([Project](../../core/Project.html) project)
selectAndCommit
public abstract void selectAndCommit([Project](../../core/Project.html) project)
Shows GUI allowing user to select the branch, add commit comment and tags.
 Then should call commitToBranch()
findAndCommit
public abstract void findAndCommit([Project](../../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputBranch,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) comment,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> tags,
 boolean unlock,
 boolean retainUsageVersions)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Finds/creates the branch automatically, and then commits the given project to that branch.
 Implementation of this method should not use any user interaction/GUI
Parameters:
`project` - source to get the state from
`outputBranch` - string to find in the given project. If branch does not exit, it should be created.
`comment` - informative commit comment
`tags` - optional commit tags
`unlock` - true to unlock user's currently locked elements in the output branch
`retainUsageVersions` - true to preserve project usage versions in the output branch. Providing false will update versions from the source project
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
addErrorMessage
protected void addErrorMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 @CheckForNull
 [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html) e)
clearErrorMessages
protected void clearErrorMessages()
getErrorMessages
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getErrorMessages()
getCommitTags
protected static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getCommitTags([Project](../../core/Project.html) project,
 com.nomagic.magicdraw.teamwork2.ui.dialogs.L2RModulesDlg<?> dialog)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.variants.teamwork</a></div>
<h1 class="title" title="Class CommitToBranchExecuter">Class CommitToBranchExecuter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.variants.teamwork.CommitToBranchExecuter</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">CommitToBranchExecuter</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Commits the provided remote project to the selected branch (that can only be the branch of the same remote project).
 The resulting version of the branch is identical to the source project.
 Current changes to the original (source) project itself are not committed/saved.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CommitToBranchExecuter</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addErrorMessage(java.lang.String,java.lang.Exception)">addErrorMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearErrorMessages()">clearErrorMessages</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="CommitToBranchExecuter.html" title="class in com.nomagic.magicdraw.variants.teamwork">CommitToBranchExecuter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createExecuter(com.nomagic.magicdraw.core.Project)">createExecuter</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#findAndCommit(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String,java.util.List,boolean,boolean)">findAndCommit</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputBranch,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags,
 boolean unlock,
 boolean retainUsageVersions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Finds/creates the branch automatically, and then commits the given project to that branch.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCommitTags(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.teamwork2.ui.dialogs.L2RModulesDlg)">getCommitTags</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.magicdraw.teamwork2.ui.dialogs.L2RModulesDlg&lt;?&gt; dialog)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getErrorMessages()">getErrorMessages</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#selectAndCommit(com.nomagic.magicdraw.core.Project)">selectAndCommit</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Shows GUI allowing user to select the branch, add commit comment and tags.</div>
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
<h3>CommitToBranchExecuter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CommitToBranchExecuter</span>()</div>
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
<section class="detail" id="createExecuter(com.nomagic.magicdraw.core.Project)">
<h3>createExecuter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="CommitToBranchExecuter.html" title="class in com.nomagic.magicdraw.variants.teamwork">CommitToBranchExecuter</a></span> <span class="element-name">createExecuter</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
</section>
</li>
<li>
<section class="detail" id="selectAndCommit(com.nomagic.magicdraw.core.Project)">
<h3>selectAndCommit</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">selectAndCommit</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Shows GUI allowing user to select the branch, add commit comment and tags.
 Then should call commitToBranch()</div>
</section>
</li>
<li>
<section class="detail" id="findAndCommit(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String,java.util.List,boolean,boolean)">
<h3>findAndCommit</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">findAndCommit</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputBranch,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags,
 boolean unlock,
 boolean retainUsageVersions)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Finds/creates the branch automatically, and then commits the given project to that branch.
 Implementation of this method should not use any user interaction/GUI</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - source to get the state from</dd>
<dd><code>outputBranch</code> - string to find in the given project. If branch does not exit, it should be created.</dd>
<dd><code>comment</code> - informative commit comment</dd>
<dd><code>tags</code> - optional commit tags</dd>
<dd><code>unlock</code> - true to unlock user's currently locked elements in the output branch</dd>
<dd><code>retainUsageVersions</code> - true to preserve project usage versions in the output branch. Providing false will update versions from the source project</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addErrorMessage(java.lang.String,java.lang.Exception)">
<h3>addErrorMessage</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addErrorMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearErrorMessages()">
<h3>clearErrorMessages</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">clearErrorMessages</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getErrorMessages()">
<h3>getErrorMessages</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getErrorMessages</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCommitTags(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.teamwork2.ui.dialogs.L2RModulesDlg)">
<h3>getCommitTags</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getCommitTags</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.magicdraw.teamwork2.ui.dialogs.L2RModulesDlg&lt;?&gt; dialog)</span></div>
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
