# JAVA OPENAPI: SaveParticipant (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/core/SaveParticipant.html
- source_path: `com/nomagic/magicdraw/core/SaveParticipant.html`
- source_sha256: `2c59d9697218194b19e18495991e3fd66ac0acf70e223e95b8e5b17e0b97f8d0`
- captured_utc: `2026-07-14T16:51:14.876121+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core](package-summary.html)

## Interface SaveParticipant

@OpenApiAllpublic interfaceSaveParticipant
Interface declares functionality for save process participant.
 Save participant can do some custom actions before and after project saving procedure.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`void`
`[doAfterSave](#doAfterSave(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](Project.html) project,
 [ProjectDescriptor](project/ProjectDescriptor.html) descriptor)`
Describes any actions to do after project saving.
`void`
`[doBeforeSave](#doBeforeSave(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](Project.html) project,
 [ProjectDescriptor](project/ProjectDescriptor.html) descriptor)`
Describes any actions to do before project saving.
`default boolean`
`[isReadyForCommit](#isReadyForCommit(com.nomagic.ci.persistence.IProject,java.lang.String))(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) comment)`
Indicates ability to commit project.
`boolean`
`[isReadyForSave](#isReadyForSave(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](Project.html) project,
 [ProjectDescriptor](project/ProjectDescriptor.html) descriptor)`
Indicates ability to save project.

============ METHOD DETAIL ========== 
Method Details
isReadyForSave
boolean isReadyForSave([Project](Project.html) project,
 [ProjectDescriptor](project/ProjectDescriptor.html) descriptor)
Indicates ability to save project.
 Save mechanism checks this status of all save participants.
 Project will not be saved if some of save participants are not ready.
Parameters:
`project` - the project prepared for saving.
`descriptor` - the project location descriptor.
Returns:
false if project can't be saved.
doBeforeSave
void doBeforeSave([Project](Project.html) project,
 [ProjectDescriptor](project/ProjectDescriptor.html) descriptor)
Describes any actions to do before project saving.
 Will be executed only if isReadyForSave() returns true.
Parameters:
`project` - the project prepared for saving.
`descriptor` - the project location descriptor.
doAfterSave
void doAfterSave([Project](Project.html) project,
 [ProjectDescriptor](project/ProjectDescriptor.html) descriptor)
Describes any actions to do after project saving.
 Will be executed only if project was saved successfully.
Parameters:
`project` - the project.
`descriptor` - the project location descriptor.
isReadyForCommit
default boolean isReadyForCommit(com.nomagic.ci.persistence.IProject project,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) comment)
Indicates ability to commit project.
 Save mechanism checks this status of all save participants.
 Project will not be committed if some of save participants are not ready.
Parameters:
`project` - the project prepared for saving.
`comment` - commit comment
Returns:
false if project can't be committed.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core</a></div>
<h1 class="title" title="Interface SaveParticipant">Interface SaveParticipant</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">SaveParticipant</span></div>
<div class="block">Interface declares functionality for save process participant.
 Save participant can do some custom actions before and after project saving procedure.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#doAfterSave(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">doAfterSave</a><wbr/>(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Describes any actions to do after project saving.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#doBeforeSave(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">doBeforeSave</a><wbr/>(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Describes any actions to do before project saving.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isReadyForCommit(com.nomagic.ci.persistence.IProject,java.lang.String)">isReadyForCommit</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Indicates ability to commit project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isReadyForSave(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">isReadyForSave</a><wbr/>(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates ability to save project.</div>
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
<section class="detail" id="isReadyForSave(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>isReadyForSave</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isReadyForSave</span><wbr/><span class="parameters">(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</span></div>
<div class="block">Indicates ability to save project.
 Save mechanism checks this status of all save participants.
 Project will not be saved if some of save participants are not ready.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project prepared for saving.</dd>
<dd><code>descriptor</code> - the project location descriptor.</dd>
<dt>Returns:</dt>
<dd>false if project can't be saved.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="doBeforeSave(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>doBeforeSave</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">doBeforeSave</span><wbr/><span class="parameters">(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</span></div>
<div class="block">Describes any actions to do before project saving.
 Will be executed only if isReadyForSave() returns true.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project prepared for saving.</dd>
<dd><code>descriptor</code> - the project location descriptor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="doAfterSave(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>doAfterSave</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">doAfterSave</span><wbr/><span class="parameters">(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</span></div>
<div class="block">Describes any actions to do after project saving.
 Will be executed only if project was saved successfully.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project.</dd>
<dd><code>descriptor</code> - the project location descriptor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReadyForCommit(com.nomagic.ci.persistence.IProject,java.lang.String)">
<h3>isReadyForCommit</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isReadyForCommit</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment)</span></div>
<div class="block">Indicates ability to commit project.
 Save mechanism checks this status of all save participants.
 Project will not be committed if some of save participants are not ready.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project prepared for saving.</dd>
<dd><code>comment</code> - commit comment</dd>
<dt>Returns:</dt>
<dd>false if project can't be committed.</dd>
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
