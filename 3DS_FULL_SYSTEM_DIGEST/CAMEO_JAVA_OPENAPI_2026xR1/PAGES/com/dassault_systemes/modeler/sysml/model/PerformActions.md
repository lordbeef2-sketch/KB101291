# JAVA OPENAPI: PerformActions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/PerformActions.html
- source_path: `com/dassault_systemes/modeler/sysml/model/PerformActions.html`
- source_sha256: `15fa6647f2933d38e99b93e1eae5b1d9a0792783cd2a8c99f8c7fa87256a7bde`
- captured_utc: `2026-07-14T16:45:02.503036+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class PerformActions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.PerformActions

@OpenApiAllpublic classPerformActions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class providing helper methods for creating, retrieving, and managing
 [`PerformActionUsage`](sysml/PerformActionUsage.html) elements that associate a performer with an action.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PerformActions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [PerformActionUsage](sysml/PerformActionUsage.html)`
`[addActionToPerformer](#addActionToPerformer(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type))([ActionUsage](sysml/ActionUsage.html) actionUsage,
 [Feature](../../kerml/model/kerml/Feature.html) performer,
 [Feature](../../kerml/model/kerml/Feature.html) oldPerformer,
 [Type](../../kerml/model/kerml/Type.html) actionsContext)`
Ensures that the given performer has a [`PerformActionUsage`](sysml/PerformActionUsage.html) referencing
 the specified action.
`static void`
`[disposePerformActionUsage](#disposePerformActionUsage(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage))([Feature](../../kerml/model/kerml/Feature.html) performer,
 [ActionUsage](sysml/ActionUsage.html) actionUsage)`
Disposes the perform action usage associated with the given performer and action,
 if it exists and can be deleted.
`static [PerformActionUsage](sysml/PerformActionUsage.html)`
`[getOrCreateOwnedPerformActionUsageTypedBy](#getOrCreateOwnedPerformActionUsageTypedBy(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type,boolean))([Type](../../kerml/model/kerml/Type.html) owner,
 [Type](../../kerml/model/kerml/Type.html) type,
 boolean create)`
Returns a perform action usage owned by the given type and typed by the
 specified type, creating one if requested and none exists.
`static [PerformActionUsage](sysml/PerformActionUsage.html)`
`[getPurePerformActionUsageInPerformer](#getPurePerformActionUsageInPerformer(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage))([Feature](../../kerml/model/kerml/Feature.html) performer,
 [ActionUsage](sysml/ActionUsage.html) performedAction)`
Returns the perform action usage owned by the performer that references
 the given action, if any.
`static boolean`
`[isPerformableAction](#isPerformableAction(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Checks whether the element is an action that can be performed.
`static boolean`
`[isPurePerformActionUsage](#isPurePerformActionUsage(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Checks whether the element is a pure perform action usage, meaning its
 EClass matches the SysML perform action usage definition exactly.
`static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[PerformActionUsage](sysml/PerformActionUsage.html)>`
`[streamOfPurePerformActionUsageInPerformer](#streamOfPurePerformActionUsageInPerformer(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) performer)`
Returns a stream of perform action usages owned by the performer.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PerformActions
public PerformActions()
 ============ METHOD DETAIL ========== 
Method Details
addActionToPerformer
public static [PerformActionUsage](sysml/PerformActionUsage.html) addActionToPerformer([ActionUsage](sysml/ActionUsage.html) actionUsage,
 [Feature](../../kerml/model/kerml/Feature.html) performer,
 @CheckForNull
 [Feature](../../kerml/model/kerml/Feature.html) oldPerformer,
 @CheckForNull
 [Type](../../kerml/model/kerml/Type.html) actionsContext)
Ensures that the given performer has a [`PerformActionUsage`](sysml/PerformActionUsage.html) referencing
 the specified action. If an existing perform action usage is found, it is reused.
 Otherwise, a new one is created or migrated from the old performer.

 If the perform action usage is newly associated with the performer, its
 referenced action is updated accordingly.
Parameters:
`actionUsage` - the action being performed
`performer` - the performer feature
`oldPerformer` - previous performer, if any
`actionsContext` - optional context used to determine reference structure
Returns:
the perform action usage associated with the performer
disposePerformActionUsage
public static void disposePerformActionUsage([Feature](../../kerml/model/kerml/Feature.html) performer,
 [ActionUsage](sysml/ActionUsage.html) actionUsage)
Disposes the perform action usage associated with the given performer and action,
 if it exists and can be deleted.
Parameters:
`performer` - the performer feature
`actionUsage` - the performed action
getPurePerformActionUsageInPerformer
@CheckForNullpublic static [PerformActionUsage](sysml/PerformActionUsage.html) getPurePerformActionUsageInPerformer([Feature](../../kerml/model/kerml/Feature.html) performer,
 [ActionUsage](sysml/ActionUsage.html) performedAction)
Returns the perform action usage owned by the performer that references
 the given action, if any.
Parameters:
`performer` - the performer feature
`performedAction` - the action being performed
Returns:
perform action usage, or null if none exists
streamOfPurePerformActionUsageInPerformer
public static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[PerformActionUsage](sysml/PerformActionUsage.html)> streamOfPurePerformActionUsageInPerformer([Feature](../../kerml/model/kerml/Feature.html) performer)
Returns a stream of perform action usages owned by the performer.
Parameters:
`performer` - the performer feature
Returns:
stream of perform action usages
isPurePerformActionUsage
public static boolean isPurePerformActionUsage([Element](../../kerml/model/kerml/Element.html) element)
Checks whether the element is a pure perform action usage, meaning its
 EClass matches the SysML perform action usage definition exactly.
Parameters:
`element` - the element
Returns:
true if pure perform action usage
isPerformableAction
public static boolean isPerformableAction(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Checks whether the element is an action that can be performed.
 Control occurrences cannot be performed.
Parameters:
`element` - the element
Returns:
true if the element is a performable action
getOrCreateOwnedPerformActionUsageTypedBy
@CheckForNullpublic static [PerformActionUsage](sysml/PerformActionUsage.html) getOrCreateOwnedPerformActionUsageTypedBy([Type](../../kerml/model/kerml/Type.html) owner,
 [Type](../../kerml/model/kerml/Type.html) type,
 boolean create)
Returns a perform action usage owned by the given type and typed by the
 specified type, creating one if requested and none exists.
Parameters:
`owner` - the owning type
`type` - the type to match
`create` - whether to create a new perform action usage if missing
Returns:
perform action usage, or null if none exists and creation is disabled

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class PerformActions">Class PerformActions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.PerformActions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PerformActions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class providing helper methods for creating, retrieving, and managing
 <a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PerformActionUsage</code></a> elements that associate a performer with an action.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PerformActions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addActionToPerformer(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">addActionToPerformer</a><wbr/>(<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> actionUsage,
 <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> performer,
 <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> oldPerformer,
 <a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> actionsContext)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Ensures that the given performer has a <a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PerformActionUsage</code></a> referencing
 the specified action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#disposePerformActionUsage(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage)">disposePerformActionUsage</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> performer,
 <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> actionUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Disposes the perform action usage associated with the given performer and action,
 if it exists and can be deleted.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateOwnedPerformActionUsageTypedBy(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type,boolean)">getOrCreateOwnedPerformActionUsageTypedBy</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> owner,
 <a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 boolean create)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a perform action usage owned by the given type and typed by the
 specified type, creating one if requested and none exists.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPurePerformActionUsageInPerformer(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage)">getPurePerformActionUsageInPerformer</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> performer,
 <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> performedAction)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the perform action usage owned by the performer that references
 the given action, if any.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPerformableAction(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isPerformableAction</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is an action that can be performed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPurePerformActionUsage(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isPurePerformActionUsage</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is a pure perform action usage, meaning its
 EClass matches the SysML perform action usage definition exactly.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#streamOfPurePerformActionUsageInPerformer(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">streamOfPurePerformActionUsageInPerformer</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> performer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a stream of perform action usages owned by the performer.</div>
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
<h3>PerformActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PerformActions</span>()</div>
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
<section class="detail" id="addActionToPerformer(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>addActionToPerformer</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a></span> <span class="element-name">addActionToPerformer</span><wbr/><span class="parameters">(<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> actionUsage,
 <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> performer,
 @CheckForNull
 <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> oldPerformer,
 @CheckForNull
 <a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> actionsContext)</span></div>
<div class="block">Ensures that the given performer has a <a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PerformActionUsage</code></a> referencing
 the specified action. If an existing perform action usage is found, it is reused.
 Otherwise, a new one is created or migrated from the old performer.

 <p>If the perform action usage is newly associated with the performer, its
 referenced action is updated accordingly.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the action being performed</dd>
<dd><code>performer</code> - the performer feature</dd>
<dd><code>oldPerformer</code> - previous performer, if any</dd>
<dd><code>actionsContext</code> - optional context used to determine reference structure</dd>
<dt>Returns:</dt>
<dd>the perform action usage associated with the performer</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disposePerformActionUsage(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage)">
<h3>disposePerformActionUsage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">disposePerformActionUsage</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> performer,
 <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> actionUsage)</span></div>
<div class="block">Disposes the perform action usage associated with the given performer and action,
 if it exists and can be deleted.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>performer</code> - the performer feature</dd>
<dd><code>actionUsage</code> - the performed action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPurePerformActionUsageInPerformer(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage)">
<h3>getPurePerformActionUsageInPerformer</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a></span> <span class="element-name">getPurePerformActionUsageInPerformer</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> performer,
 <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> performedAction)</span></div>
<div class="block">Returns the perform action usage owned by the performer that references
 the given action, if any.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>performer</code> - the performer feature</dd>
<dd><code>performedAction</code> - the action being performed</dd>
<dt>Returns:</dt>
<dd>perform action usage, or null if none exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="streamOfPurePerformActionUsageInPerformer(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>streamOfPurePerformActionUsageInPerformer</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a>&gt;</span> <span class="element-name">streamOfPurePerformActionUsageInPerformer</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> performer)</span></div>
<div class="block">Returns a stream of perform action usages owned by the performer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>performer</code> - the performer feature</dd>
<dt>Returns:</dt>
<dd>stream of perform action usages</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPurePerformActionUsage(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isPurePerformActionUsage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPurePerformActionUsage</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the element is a pure perform action usage, meaning its
 EClass matches the SysML perform action usage definition exactly.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>true if pure perform action usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPerformableAction(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isPerformableAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPerformableAction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the element is an action that can be performed.
 Control occurrences cannot be performed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>true if the element is a performable action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateOwnedPerformActionUsageTypedBy(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type,boolean)">
<h3>getOrCreateOwnedPerformActionUsageTypedBy</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a></span> <span class="element-name">getOrCreateOwnedPerformActionUsageTypedBy</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> owner,
 <a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 boolean create)</span></div>
<div class="block">Returns a perform action usage owned by the given type and typed by the
 specified type, creating one if requested and none exists.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - the owning type</dd>
<dd><code>type</code> - the type to match</dd>
<dd><code>create</code> - whether to create a new perform action usage if missing</dd>
<dt>Returns:</dt>
<dd>perform action usage, or null if none exists and creation is disabled</dd>
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
