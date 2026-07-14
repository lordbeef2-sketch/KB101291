# JAVA OPENAPI: MergeUtil (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/merge/MergeUtil.html
- source_path: `com/nomagic/magicdraw/merge/MergeUtil.html`
- source_sha256: `4788cd654cff01ba9e1dd2a2f732438cc42833fd32171d1a16367b630c1d2af0`
- captured_utc: `2026-07-14T16:51:24.713250+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.merge](package-summary.html)

## Class MergeUtil

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.merge.CompareUtil](CompareUtil.html)
com.nomagic.magicdraw.merge.MergeUtil

@OpenApiAllpublic classMergeUtil
extends [CompareUtil](CompareUtil.html)
Allows using MagicDraw project merge to merge projects.
 See Open API manual for the usage details.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MergeUtil](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[acceptChanges](#acceptChanges(java.util.Set,java.util.Set))([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Change](Change.html)> preferredChanges,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Change](Change.html)> changes)`
Accept given changes.
`static boolean`
`[applyChanges](#applyChanges(com.nomagic.magicdraw.merge.ProjectDifference,com.nomagic.utils.ErrorHandler))([ProjectDifference](ProjectDifference.html) difference,
 [ErrorHandler](../../utils/ErrorHandler.html)<[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)> errorHandler)`
Apply project difference changes.
`static void`
`[callInEsiIDSupport](#callInEsiIDSupport(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) runnable)`
Executes runnable where [`getID(BaseElement)`](#getID(com.nomagic.magicdraw.uml.BaseElement)) uses twc
 server element id when comparing elements.
`static [ProjectDescriptor](../core/project/ProjectDescriptor.html)`
`[createRemoteAncestorDescriptorForMerge](#createRemoteAncestorDescriptorForMerge(com.nomagic.magicdraw.core.Project,long,boolean))([Project](../core/Project.html) targetProject,
 long mergeFrom,
 boolean lock)`
Creates remote ancestor descriptor for merge.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getAllIDS](#getAllIDS(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Get element IDs of all elements in given project.
`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Change](Change.html)>`
`[getConflictingChanges](#getConflictingChanges(java.util.Set))([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Change](Change.html)> changes)`
Filter only changes that has conflicts.
`static [BaseElement](../uml/BaseElement.html)`
`[getElementByID](#getElementByID(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Return element from project with given simple or derived id.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getID](#getID(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) be)`
Returns element ID, or project id combination with element id for TWC elements.
`static boolean`
`[merge](#merge(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.merge.ConflictResolution,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization))([Project](../core/Project.html) targetProject,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) source,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) ancestor,
 [ConflictResolution](ConflictResolution.html) conflictResolution,
 [ErrorHandler](../../utils/ErrorHandler.html)<[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)> errorHandler,
 [Optimization](Optimization.html) optimization)`
Merge projects.
`static void`
`[registerCreatedElement](#registerCreatedElement(java.lang.String,com.nomagic.uml2.ext.magicdraw.base.ModelObject))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) compositeID,
 [ModelObject](../../uml2/ext/magicdraw/base/ModelObject.html) element)`
Register created element by composite id.
`static void`
`[resetCompositeIDSupport](#resetCompositeIDSupport())()`
Reset known composite id support.
`static void`
`[resetCompositeIDSupportCreatedElements](#resetCompositeIDSupportCreatedElements())()`
Reset known created elements.
`static void`
`[setChangeState](#setChangeState(com.nomagic.magicdraw.merge.Change,com.nomagic.magicdraw.merge.ChangeState))([Change](Change.html) change,
 [ChangeState](ChangeState.html) state)`
Set change state.
`static boolean`
`[showMergeGUI](#showMergeGUI(com.nomagic.magicdraw.merge.ProjectDifference))([ProjectDifference](ProjectDifference.html) projectDifference)`
Show merge GUI.
Methods inherited from class com.nomagic.magicdraw.merge.[CompareUtil](CompareUtil.html)
`[compareProjects](CompareUtil.html#compareProjects(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization)), [getDifference](CompareUtil.html#getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization)), [getDifference](CompareUtil.html#getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization,java.util.Set)), [restore](CompareUtil.html#restore(com.nomagic.magicdraw.merge.ProjectDifference)), [showDifferenceGUI](CompareUtil.html#showDifferenceGUI(com.nomagic.magicdraw.merge.ProjectDifference))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MergeUtil
public MergeUtil()
 ============ METHOD DETAIL ========== 
Method Details
acceptChanges
public static void acceptChanges([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Change](Change.html)> preferredChanges,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Change](Change.html)> changes)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)
Accept given changes. If change from `changes` conflicts with change from `preferredChanges`, it is rejected.
 The result is - all `preferredChanges` are accepted, and only not conflicting `changes` are accepted.
Parameters:
`preferredChanges` - accept all these changes.
`changes` - accept only not conflicting changes.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if merge is not available
showMergeGUI
public static boolean showMergeGUI([ProjectDifference](ProjectDifference.html) projectDifference)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)
Show merge GUI.
Parameters:
`projectDifference` - project difference.
Returns:
true proceed merging, false - cancel merging.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if merge is not available
applyChanges
public static boolean applyChanges([ProjectDifference](ProjectDifference.html) difference,
 [ErrorHandler](../../utils/ErrorHandler.html)<[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)> errorHandler)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)
Apply project difference changes.
Parameters:
`difference` - project difference.
`errorHandler` - invoked if error occurs.
Returns:
true if changes applied, otherwise - false.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if merge is not available,
 if changes applied on not latest teamwork project version,
 or trying to merge local project with teamwork project.
getConflictingChanges
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Change](Change.html)> getConflictingChanges([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Change](Change.html)> changes)
Filter only changes that has conflicts.
Parameters:
`changes` - changes to filter.
Returns:
conflicting changes.
setChangeState
public static void setChangeState([Change](Change.html) change,
 [ChangeState](ChangeState.html) state)
Set change state. Dependent, required and conflicting changes states are also modified (if modification is required).
Parameters:
`change` - change to modify state.
`state` - new change state.
merge
public static boolean merge([Project](../core/Project.html) targetProject,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) source,
 @CheckForNull
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) ancestor,
 @CheckForNull
 [ConflictResolution](ConflictResolution.html) conflictResolution,
 [ErrorHandler](../../utils/ErrorHandler.html)<[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)> errorHandler,
 [Optimization](Optimization.html) optimization)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)
Merge projects.
Parameters:
`targetProject` - target project.
`source` - source project descriptor.
`ancestor` - ancestor project descriptor. Pass value only for 3-way merge (`null` for 2-way merge).
`conflictResolution` - define conflict resolution. Used only in 3-way merge. `null` is treated as [`ConflictResolution.TARGET_PREFERRED`](ConflictResolution.html#TARGET_PREFERRED).
`errorHandler` - invoked if error occurs. Allows to perform custom action.
`optimization` - optimization option.
Returns:
`true` if project merged, otherwise `false`.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if merge is not available,
 if changes applied on not latest teamwork project version,
 or trying to merge local project with teamwork project.
getID
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getID([BaseElement](../uml/BaseElement.html) be)
Returns element ID, or project id combination with element id for TWC elements.
Parameters:
`be` - base element
Returns:
element ID
getElementByID
@CheckForNullpublic static [BaseElement](../uml/BaseElement.html) getElementByID([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Return element from project with given simple or derived id. For esi project checks project for found element - if there are more than one project with same local id.
Parameters:
`project` - project
`id` - simple or derived id
Returns:
element or null
getAllIDS
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getAllIDS([Project](../core/Project.html) project)
Get element IDs of all elements in given project.
Parameters:
`project` - project
Returns:
element IDs
resetCompositeIDSupportCreatedElements
public static void resetCompositeIDSupportCreatedElements()
Reset known created elements.
See Also:
[`registerCreatedElement(String, ModelObject)`](#registerCreatedElement(java.lang.String,com.nomagic.uml2.ext.magicdraw.base.ModelObject))
resetCompositeIDSupport
public static void resetCompositeIDSupport()
Reset known composite id support.
callInEsiIDSupport
public static void callInEsiIDSupport([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) runnable)
Executes runnable where [`getID(BaseElement)`](#getID(com.nomagic.magicdraw.uml.BaseElement)) uses twc
 server element id when comparing elements.
Parameters:
`runnable` - runnable to execute
registerCreatedElement
public static void registerCreatedElement([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) compositeID,
 [ModelObject](../../uml2/ext/magicdraw/base/ModelObject.html) element)
Register created element by composite id. Composite id may contain information that element is in module,
 but in ancestor such module is still not used. When element is registered it can be found by provided composite id.
Parameters:
`compositeID` - composite id.
`element` - created element.
createRemoteAncestorDescriptorForMerge
@CheckForNullpublic static [ProjectDescriptor](../core/project/ProjectDescriptor.html) createRemoteAncestorDescriptorForMerge([Project](../core/Project.html) targetProject,
 long mergeFrom,
 boolean lock)
Creates remote ancestor descriptor for merge.
Parameters:
`targetProject` - target project.
`mergeFrom` - source version.
`lock` - should decomposition lock be taken.
Returns:
created descriptor or null.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.merge</a></div>
<h1 class="title" title="Class MergeUtil">Class MergeUtil</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="CompareUtil.html" title="class in com.nomagic.magicdraw.merge">com.nomagic.magicdraw.merge.CompareUtil</a>
<div class="inheritance">com.nomagic.magicdraw.merge.MergeUtil</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MergeUtil</span>
<span class="extends-implements">extends <a href="CompareUtil.html" title="class in com.nomagic.magicdraw.merge">CompareUtil</a></span></div>
<div class="block">Allows using MagicDraw project merge to merge projects.
 See Open API manual for the usage details.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MergeUtil</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#acceptChanges(java.util.Set,java.util.Set)">acceptChanges</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt; preferredChanges,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt; changes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Accept given changes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#applyChanges(com.nomagic.magicdraw.merge.ProjectDifference,com.nomagic.utils.ErrorHandler)">applyChanges</a><wbr/>(<a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a> difference,
 <a href="../../utils/ErrorHandler.html" title="interface in com.nomagic.utils">ErrorHandler</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a>&gt; errorHandler)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Apply project difference changes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#callInEsiIDSupport(java.lang.Runnable)">callInEsiIDSupport</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes runnable where <a href="#getID(com.nomagic.magicdraw.uml.BaseElement)"><code>getID(BaseElement)</code></a> uses twc
 server element id when comparing elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createRemoteAncestorDescriptorForMerge(com.nomagic.magicdraw.core.Project,long,boolean)">createRemoteAncestorDescriptorForMerge</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> targetProject,
 long mergeFrom,
 boolean lock)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates remote ancestor descriptor for merge.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllIDS(com.nomagic.magicdraw.core.Project)">getAllIDS</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get element IDs of all elements in given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getConflictingChanges(java.util.Set)">getConflictingChanges</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt; changes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Filter only changes that has conflicts.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementByID(com.nomagic.magicdraw.core.Project,java.lang.String)">getElementByID</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return element from project with given simple or derived id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getID(com.nomagic.magicdraw.uml.BaseElement)">getID</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> be)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns element ID, or project id combination with element id for TWC elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#merge(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.merge.ConflictResolution,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization)">merge</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> targetProject,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> source,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> ancestor,
 <a href="ConflictResolution.html" title="enum class in com.nomagic.magicdraw.merge">ConflictResolution</a> conflictResolution,
 <a href="../../utils/ErrorHandler.html" title="interface in com.nomagic.utils">ErrorHandler</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a>&gt; errorHandler,
 <a href="Optimization.html" title="enum class in com.nomagic.magicdraw.merge">Optimization</a> optimization)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Merge projects.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#registerCreatedElement(java.lang.String,com.nomagic.uml2.ext.magicdraw.base.ModelObject)">registerCreatedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> compositeID,
 <a href="../../uml2/ext/magicdraw/base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Register created element by composite id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#resetCompositeIDSupport()">resetCompositeIDSupport</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Reset known composite id support.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#resetCompositeIDSupportCreatedElements()">resetCompositeIDSupportCreatedElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Reset known created elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setChangeState(com.nomagic.magicdraw.merge.Change,com.nomagic.magicdraw.merge.ChangeState)">setChangeState</a><wbr/>(<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a> change,
 <a href="ChangeState.html" title="enum class in com.nomagic.magicdraw.merge">ChangeState</a> state)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set change state.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#showMergeGUI(com.nomagic.magicdraw.merge.ProjectDifference)">showMergeGUI</a><wbr/>(<a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a> projectDifference)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Show merge GUI.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.merge.CompareUtil">Methods inherited from class com.nomagic.magicdraw.merge.<a href="CompareUtil.html" title="class in com.nomagic.magicdraw.merge">CompareUtil</a></h3>
<code><a href="CompareUtil.html#compareProjects(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization)">compareProjects</a>, <a href="CompareUtil.html#getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization)">getDifference</a>, <a href="CompareUtil.html#getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization,java.util.Set)">getDifference</a>, <a href="CompareUtil.html#restore(com.nomagic.magicdraw.merge.ProjectDifference)">restore</a>, <a href="CompareUtil.html#showDifferenceGUI(com.nomagic.magicdraw.merge.ProjectDifference)">showDifferenceGUI</a></code></div>
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
<h3>MergeUtil</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MergeUtil</span>()</div>
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
<section class="detail" id="acceptChanges(java.util.Set,java.util.Set)">
<h3>acceptChanges</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">acceptChanges</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt; preferredChanges,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt; changes)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Accept given changes. If change from <code>changes</code> conflicts with change from <code>preferredChanges</code>, it is rejected.
 The result is - all <code>preferredChanges</code> are accepted, and only not conflicting <code>changes</code> are accepted.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>preferredChanges</code> - accept all these changes.</dd>
<dd><code>changes</code> - accept only not conflicting changes.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if merge is not available</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showMergeGUI(com.nomagic.magicdraw.merge.ProjectDifference)">
<h3>showMergeGUI</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">showMergeGUI</span><wbr/><span class="parameters">(<a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a> projectDifference)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Show merge GUI.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectDifference</code> - project difference.</dd>
<dt>Returns:</dt>
<dd>true proceed merging, false - cancel merging.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if merge is not available</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="applyChanges(com.nomagic.magicdraw.merge.ProjectDifference,com.nomagic.utils.ErrorHandler)">
<h3>applyChanges</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">applyChanges</span><wbr/><span class="parameters">(<a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a> difference,
 <a href="../../utils/ErrorHandler.html" title="interface in com.nomagic.utils">ErrorHandler</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a>&gt; errorHandler)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Apply project difference changes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>difference</code> - project difference.</dd>
<dd><code>errorHandler</code> - invoked if error occurs.</dd>
<dt>Returns:</dt>
<dd>true if changes applied, otherwise - false.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if merge is not available,
                               if changes applied on not latest teamwork project version,
                               or trying to merge local project with teamwork project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConflictingChanges(java.util.Set)">
<h3>getConflictingChanges</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt;</span> <span class="element-name">getConflictingChanges</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt; changes)</span></div>
<div class="block">Filter only changes that has conflicts.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>changes</code> - changes to filter.</dd>
<dt>Returns:</dt>
<dd>conflicting changes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChangeState(com.nomagic.magicdraw.merge.Change,com.nomagic.magicdraw.merge.ChangeState)">
<h3>setChangeState</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setChangeState</span><wbr/><span class="parameters">(<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a> change,
 <a href="ChangeState.html" title="enum class in com.nomagic.magicdraw.merge">ChangeState</a> state)</span></div>
<div class="block">Set change state. Dependent, required and conflicting changes states are also modified (if modification is required).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>change</code> - change to modify state.</dd>
<dd><code>state</code> - new change state.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="merge(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.merge.ConflictResolution,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization)">
<h3>merge</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">merge</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> targetProject,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> source,
 @CheckForNull
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> ancestor,
 @CheckForNull
 <a href="ConflictResolution.html" title="enum class in com.nomagic.magicdraw.merge">ConflictResolution</a> conflictResolution,
 <a href="../../utils/ErrorHandler.html" title="interface in com.nomagic.utils">ErrorHandler</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a>&gt; errorHandler,
 <a href="Optimization.html" title="enum class in com.nomagic.magicdraw.merge">Optimization</a> optimization)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Merge projects.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetProject</code> - target project.</dd>
<dd><code>source</code> - source project descriptor.</dd>
<dd><code>ancestor</code> - ancestor project descriptor. Pass value only for 3-way merge (<code>null</code> for 2-way merge).</dd>
<dd><code>conflictResolution</code> - define conflict resolution. Used only in 3-way merge. <code>null</code> is treated as <a href="ConflictResolution.html#TARGET_PREFERRED"><code>ConflictResolution.TARGET_PREFERRED</code></a>.</dd>
<dd><code>errorHandler</code> - invoked if error occurs. Allows to perform custom action.</dd>
<dd><code>optimization</code> - optimization option.</dd>
<dt>Returns:</dt>
<dd><code>true</code> if project merged, otherwise <code>false</code>.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if merge is not available,
                               if changes applied on not latest teamwork project version,
                               or trying to merge local project with teamwork project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getID(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getID</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> be)</span></div>
<div class="block">Returns element ID, or project id combination with element id for TWC elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>be</code> - base element</dd>
<dt>Returns:</dt>
<dd>element ID</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementByID(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>getElementByID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getElementByID</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Return element from project with given simple or derived id. For esi project checks project for found element - if there are more than one project with same local id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>id</code> - simple or derived id</dd>
<dt>Returns:</dt>
<dd>element or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllIDS(com.nomagic.magicdraw.core.Project)">
<h3>getAllIDS</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAllIDS</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Get element IDs of all elements in given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>element IDs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetCompositeIDSupportCreatedElements()">
<h3>resetCompositeIDSupportCreatedElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetCompositeIDSupportCreatedElements</span>()</div>
<div class="block">Reset known created elements.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#registerCreatedElement(java.lang.String,com.nomagic.uml2.ext.magicdraw.base.ModelObject)"><code>registerCreatedElement(String, ModelObject)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetCompositeIDSupport()">
<h3>resetCompositeIDSupport</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetCompositeIDSupport</span>()</div>
<div class="block">Reset known composite id support.</div>
</section>
</li>
<li>
<section class="detail" id="callInEsiIDSupport(java.lang.Runnable)">
<h3>callInEsiIDSupport</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">callInEsiIDSupport</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</span></div>
<div class="block">Executes runnable where <a href="#getID(com.nomagic.magicdraw.uml.BaseElement)"><code>getID(BaseElement)</code></a> uses twc
 server element id when comparing elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runnable</code> - runnable to execute</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerCreatedElement(java.lang.String,com.nomagic.uml2.ext.magicdraw.base.ModelObject)">
<h3>registerCreatedElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">registerCreatedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> compositeID,
 <a href="../../uml2/ext/magicdraw/base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a> element)</span></div>
<div class="block">Register created element by composite id. Composite id may contain information that element is in module,
 but in ancestor such module is still not used. When element is registered it can be found by provided composite id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>compositeID</code> - composite id.</dd>
<dd><code>element</code> - created element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRemoteAncestorDescriptorForMerge(com.nomagic.magicdraw.core.Project,long,boolean)">
<h3>createRemoteAncestorDescriptorForMerge</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">createRemoteAncestorDescriptorForMerge</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> targetProject,
 long mergeFrom,
 boolean lock)</span></div>
<div class="block">Creates remote ancestor descriptor for merge.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetProject</code> - target project.</dd>
<dd><code>mergeFrom</code> - source version.</dd>
<dd><code>lock</code> - should decomposition lock be taken.</dd>
<dt>Returns:</dt>
<dd>created descriptor or null.</dd>
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
