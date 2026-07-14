# JAVA OPENAPI: States (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/States.html
- source_path: `com/dassault_systemes/modeler/sysml/model/States.html`
- source_sha256: `83893c3276b5ae65f00bbca7f36dea8347c05a8ee2471e93ec5fbcf4b654d3ed`
- captured_utc: `2026-07-14T16:45:02.668038+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class States

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.States

@OpenApiAllpublic classStates
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class providing helper methods for working with [`StateDefinition`](sysml/StateDefinition.html) or [`StateUsage`](sysml/StateUsage.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[States](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ActionUsage](sysml/ActionUsage.html)`
`[getOwnedStateSubaction](#getOwnedStateSubaction(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionKind))([Type](../../kerml/model/kerml/Type.html) owner,
 [StateSubactionKind](sysml/StateSubactionKind.html) kind)`
Returns the state subaction of the given kind owned by the type, if any.
`static boolean`
`[isDoAction](#isDoAction(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership))([FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)`
Checks whether the membership represents a DO subaction.
`static boolean`
`[isEntryAction](#isEntryAction(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership))([FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)`
Checks whether the membership represents an ENTRY subaction.
`static boolean`
`[isEntryDoExitAction](#isEntryDoExitAction(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership))([FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)`
Checks whether the membership represents an ENTRY, DO, or EXIT state subaction.
`static boolean`
`[isExhibitStateUsage](#isExhibitStateUsage(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the given EClass represents an [`ExhibitStateUsage`](sysml/ExhibitStateUsage.html).
`static boolean`
`[isExitAction](#isExitAction(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership))([FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)`
Checks whether the membership represents an EXIT subaction.
`static boolean`
`[isParallel](#isParallel(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Checks whether the given type represents a parallel state.
`static boolean`
`[isStateSubaction](#isStateSubaction(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Checks whether the given feature is a state subaction.
`static boolean`
`[isStateUsageOrDefinition](#isStateUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Checks whether the given element is a [`StateUsage`](sysml/StateUsage.html) or [`StateDefinition`](sysml/StateDefinition.html).
`static boolean`
`[isStateUsageOrDefinition](#isStateUsageOrDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the given EClass represents a [`StateUsage`](sysml/StateUsage.html)
 or [`StateDefinition`](sysml/StateDefinition.html).
`static [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)`
`[isSubstateUsageParallel](#isSubstateUsageParallel(com.dassault_systemes.modeler.sysml.model.sysml.StateUsage))([StateUsage](sysml/StateUsage.html) stateUsage)`
Determines whether the given state usage is a substate of a parallel state.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
States
public States()
 ============ METHOD DETAIL ========== 
Method Details
isStateUsageOrDefinition
public static boolean isStateUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Checks whether the given element is a [`StateUsage`](sysml/StateUsage.html) or [`StateDefinition`](sysml/StateDefinition.html).
Parameters:
`element` - the element to check
Returns:
true if the element is a state usage or definition
isStateUsageOrDefinition
public static boolean isStateUsageOrDefinition(org.eclipse.emf.ecore.EClass eClass)
Checks whether the given EClass represents a [`StateUsage`](sysml/StateUsage.html)
 or [`StateDefinition`](sysml/StateDefinition.html).
Parameters:
`eClass` - the class to check
Returns:
true if the class is a state usage or definition
isExhibitStateUsage
public static boolean isExhibitStateUsage(org.eclipse.emf.ecore.EClass eClass)
Checks whether the given EClass represents an [`ExhibitStateUsage`](sysml/ExhibitStateUsage.html).
Parameters:
`eClass` - the class to check
Returns:
true if the class is an exhibit state usage
getOwnedStateSubaction
@CheckForNullpublic static [ActionUsage](sysml/ActionUsage.html) getOwnedStateSubaction([Type](../../kerml/model/kerml/Type.html) owner,
 [StateSubactionKind](sysml/StateSubactionKind.html) kind)
Returns the state subaction of the given kind owned by the type, if any.
Parameters:
`owner` - the owning type
`kind` - the subaction kind (ENTRY, DO, EXIT)
Returns:
the subaction action usage, or null if none exists
isEntryDoExitAction
public static boolean isEntryDoExitAction(@CheckForNull
 [FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)
Checks whether the membership represents an ENTRY, DO, or EXIT state subaction.
Parameters:
`membership` - the membership
Returns:
true if the membership is an entry/do/exit subaction
isEntryAction
public static boolean isEntryAction(@CheckForNull
 [FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)
Checks whether the membership represents an ENTRY subaction.
Parameters:
`membership` - the membership
Returns:
true if ENTRY
isDoAction
public static boolean isDoAction(@CheckForNull
 [FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)
Checks whether the membership represents a DO subaction.
Parameters:
`membership` - the membership
Returns:
true if DO
isExitAction
public static boolean isExitAction(@CheckForNull
 [FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)
Checks whether the membership represents an EXIT subaction.
Parameters:
`membership` - the membership
Returns:
true if EXIT
isStateSubaction
public static boolean isStateSubaction([Feature](../../kerml/model/kerml/Feature.html) feature)
Checks whether the given feature is a state subaction.
Parameters:
`feature` - the feature
Returns:
true if the feature is an action usage owned by a state subaction membership
isParallel
public static boolean isParallel([Type](../../kerml/model/kerml/Type.html) type)
Checks whether the given type represents a parallel state.
Parameters:
`type` - the type
Returns:
true if the type is a parallel state
isSubstateUsageParallel
@CheckForNullpublic static [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isSubstateUsageParallel([StateUsage](sysml/StateUsage.html) stateUsage)
Determines whether the given state usage is a substate of a parallel state.
Parameters:
`stateUsage` - the state usage
Returns:
true/false if parallelism can be determined, or null if not a substate usage

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class States">Class States</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.States</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">States</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class providing helper methods for working with <a href="sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateDefinition</code></a> or <a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateUsage</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">States</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedStateSubaction(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionKind)">getOwnedStateSubaction</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> owner,
 <a href="sysml/StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a> kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the state subaction of the given kind owned by the type, if any.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDoAction(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">isDoAction</a><wbr/>(<a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the membership represents a DO subaction.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isEntryAction(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">isEntryAction</a><wbr/>(<a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the membership represents an ENTRY subaction.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isEntryDoExitAction(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">isEntryDoExitAction</a><wbr/>(<a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the membership represents an ENTRY, DO, or EXIT state subaction.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isExhibitStateUsage(org.eclipse.emf.ecore.EClass)">isExhibitStateUsage</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given EClass represents an <a href="sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ExhibitStateUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isExitAction(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">isExitAction</a><wbr/>(<a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the membership represents an EXIT subaction.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isParallel(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isParallel</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given type represents a parallel state.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStateSubaction(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isStateSubaction</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given feature is a state subaction.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStateUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isStateUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given element is a <a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateUsage</code></a> or <a href="sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStateUsageOrDefinition(org.eclipse.emf.ecore.EClass)">isStateUsageOrDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given EClass represents a <a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateUsage</code></a>
 or <a href="sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSubstateUsageParallel(com.dassault_systemes.modeler.sysml.model.sysml.StateUsage)">isSubstateUsageParallel</a><wbr/>(<a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a> stateUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Determines whether the given state usage is a substate of a parallel state.</div>
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
<h3>States</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">States</span>()</div>
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
<section class="detail" id="isStateUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isStateUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStateUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the given element is a <a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateUsage</code></a> or <a href="sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd>true if the element is a state usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStateUsageOrDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isStateUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStateUsageOrDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the given EClass represents a <a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateUsage</code></a>
 or <a href="sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if the class is a state usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExhibitStateUsage(org.eclipse.emf.ecore.EClass)">
<h3>isExhibitStateUsage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isExhibitStateUsage</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the given EClass represents an <a href="sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ExhibitStateUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if the class is an exhibit state usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedStateSubaction(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionKind)">
<h3>getOwnedStateSubaction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></span> <span class="element-name">getOwnedStateSubaction</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> owner,
 <a href="sysml/StateSubactionKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionKind</a> kind)</span></div>
<div class="block">Returns the state subaction of the given kind owned by the type, if any.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - the owning type</dd>
<dd><code>kind</code> - the subaction kind (ENTRY, DO, EXIT)</dd>
<dt>Returns:</dt>
<dd>the subaction action usage, or null if none exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEntryDoExitAction(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">
<h3>isEntryDoExitAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEntryDoExitAction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</span></div>
<div class="block">Checks whether the membership represents an ENTRY, DO, or EXIT state subaction.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the membership</dd>
<dt>Returns:</dt>
<dd>true if the membership is an entry/do/exit subaction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEntryAction(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">
<h3>isEntryAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEntryAction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</span></div>
<div class="block">Checks whether the membership represents an ENTRY subaction.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the membership</dd>
<dt>Returns:</dt>
<dd>true if ENTRY</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDoAction(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">
<h3>isDoAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDoAction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</span></div>
<div class="block">Checks whether the membership represents a DO subaction.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the membership</dd>
<dt>Returns:</dt>
<dd>true if DO</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExitAction(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">
<h3>isExitAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isExitAction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</span></div>
<div class="block">Checks whether the membership represents an EXIT subaction.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the membership</dd>
<dt>Returns:</dt>
<dd>true if EXIT</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStateSubaction(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isStateSubaction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStateSubaction</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the given feature is a state subaction.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if the feature is an action usage owned by a state subaction membership</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParallel(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isParallel</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isParallel</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Checks whether the given type represents a parallel state.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>true if the type is a parallel state</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSubstateUsageParallel(com.dassault_systemes.modeler.sysml.model.sysml.StateUsage)">
<h3>isSubstateUsageParallel</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isSubstateUsageParallel</span><wbr/><span class="parameters">(<a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a> stateUsage)</span></div>
<div class="block">Determines whether the given state usage is a substate of a parallel state.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stateUsage</code> - the state usage</dd>
<dt>Returns:</dt>
<dd>true/false if parallelism can be determined, or null if not a substate usage</dd>
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
