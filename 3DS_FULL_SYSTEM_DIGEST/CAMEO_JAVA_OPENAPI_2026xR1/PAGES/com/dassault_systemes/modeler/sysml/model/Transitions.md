# JAVA OPENAPI: Transitions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Transitions.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Transitions.html`
- source_sha256: `c42a9a3b4f4044e26a5a2d20279cb30816824094c95d14c6692c431f91042196`
- captured_utc: `2026-07-14T16:45:02.711037+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Transitions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Transitions

@OpenApiAllpublic final classTransitions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class providing helper methods for working with [`TransitionUsage`](sysml/TransitionUsage.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static enum`
`[Transitions.TransitionUsageKind](Transitions.TransitionUsageKind.html)`
Enumeration of transition usage kinds.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Transitions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [AcceptActionUsage](sysml/AcceptActionUsage.html)`
`[createTriggerAction](#createTriggerAction(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,java.util.List))([TransitionUsage](sysml/TransitionUsage.html) transitionUsage,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Definition](sysml/Definition.html)> definitions)`
Creates a trigger action for the transition usage with the given payload definitions.
`static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[ActionUsage](sysml/ActionUsage.html)>`
`[getEffectActions](#getEffectActions(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage))([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)`
Returns all effect actions of the transition usage.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOrCreatePayloadParameter](#getOrCreatePayloadParameter(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage))([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)`
Returns the payload parameter of the transition usage, creating it if necessary.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOrCreateSourceParameter](#getOrCreateSourceParameter(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage))([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)`
Returns the source parameter of the transition usage, creating it if necessary.
`static [Succession](../../kerml/model/kerml/Succession.html)`
`[getOrCreateSuccession](#getOrCreateSuccession(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage))([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)`
Returns the succession of the transition usage, creating one if necessary.
`static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Expression](../../kerml/model/kerml/Expression.html)>`
`[getOwnedGuardExpressions](#getOwnedGuardExpressions(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage))([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)`
Returns all guard expressions owned by the transition usage.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOwnedPayloadParameter](#getOwnedPayloadParameter(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage))([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)`
Returns the owned payload parameter of the transition usage.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOwnedSourceParameter](#getOwnedSourceParameter(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage))([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)`
Returns the owned source parameter of the transition usage.
`static [Membership](../../kerml/model/kerml/Membership.html)`
`[getSourceMembership](#getSourceMembership(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage))([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)`
Returns the source membership of the transition usage.
`static [Transitions.TransitionUsageKind](Transitions.TransitionUsageKind.html)`
`[getTransitionUsageKind](#getTransitionUsageKind(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage))([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)`
Determines the kind of transition usage based on its owning type and source.
`static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[AcceptActionUsage](sysml/AcceptActionUsage.html)>`
`[getTriggerActions](#getTriggerActions(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage))([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)`
Returns all trigger actions of the transition usage.
`static void`
`[setOwnedGuardExpression](#setOwnedGuardExpression(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,com.dassault_systemes.modeler.kerml.model.kerml.Expression))([TransitionUsage](sysml/TransitionUsage.html) transitionUsage,
 [Expression](../../kerml/model/kerml/Expression.html) guard)`
Sets the guard expression of the transition usage.
`static boolean`
`[setSourceChain](#setSourceChain(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,com.dassault_systemes.modeler.kerml.model.kerml.Succession,java.util.List))([TransitionUsage](sysml/TransitionUsage.html) transitionUsage,
 [Succession](../../kerml/model/kerml/Succession.html) succession,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](../../kerml/model/kerml/Feature.html)> chain)`
Store passed chain in the [`TransitionUsage`](sysml/TransitionUsage.html).source [`Membership`](../../kerml/model/kerml/Membership.html).
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Transitions
public Transitions()
 ============ METHOD DETAIL ========== 
Method Details
getOwnedGuardExpressions
public static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Expression](../../kerml/model/kerml/Expression.html)> getOwnedGuardExpressions([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)
Returns all guard expressions owned by the transition usage.
Parameters:
`transitionUsage` - the transition usage
Returns:
stream of guard expressions
setOwnedGuardExpression
public static void setOwnedGuardExpression([TransitionUsage](sysml/TransitionUsage.html) transitionUsage,
 [Expression](../../kerml/model/kerml/Expression.html) guard)
Sets the guard expression of the transition usage. If a guard membership
 does not yet exist, one is created. If an existing guard is replaced,
 the old guard is disposed.
Parameters:
`transitionUsage` - the transition usage
`guard` - the new guard expression
getEffectActions
public static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[ActionUsage](sysml/ActionUsage.html)> getEffectActions([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)
Returns all effect actions of the transition usage.
Parameters:
`transitionUsage` - the transition usage
Returns:
stream of effect actions
getTriggerActions
public static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[AcceptActionUsage](sysml/AcceptActionUsage.html)> getTriggerActions([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)
Returns all trigger actions of the transition usage.
Parameters:
`transitionUsage` - the transition usage
Returns:
stream of trigger actions
setSourceChain
public static boolean setSourceChain([TransitionUsage](sysml/TransitionUsage.html) transitionUsage,
 [Succession](../../kerml/model/kerml/Succession.html) succession,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](../../kerml/model/kerml/Feature.html)> chain)
Store passed chain in the [`TransitionUsage`](sysml/TransitionUsage.html).source [`Membership`](../../kerml/model/kerml/Membership.html).
 Create implied [`ReferenceSubsetting`](../../kerml/model/kerml/ReferenceSubsetting.html) from the source of [`Succession`](../../kerml/model/kerml/Succession.html) to that [`Membership`](../../kerml/model/kerml/Membership.html).memberElement.
Parameters:
`succession` - succession
`chain` - source chain
Returns:
true if a source was changed
getSourceMembership
@CheckForNullpublic static [Membership](../../kerml/model/kerml/Membership.html) getSourceMembership([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)
Returns the source membership of the transition usage. The source membership
 is a non-feature membership whose referent is an [`ActionUsage`](sysml/ActionUsage.html).
Parameters:
`transitionUsage` - the transition usage
Returns:
source membership, or null if none exists
getOrCreateSuccession
public static [Succession](../../kerml/model/kerml/Succession.html) getOrCreateSuccession([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)
Returns the succession of the transition usage, creating one if necessary.
Parameters:
`transitionUsage` - the transition usage
Returns:
existing or newly created succession
getTransitionUsageKind
@CheckForNullpublic static [Transitions.TransitionUsageKind](Transitions.TransitionUsageKind.html) getTransitionUsageKind([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)
Determines the kind of transition usage based on its owning type and source.
Parameters:
`transitionUsage` - the transition usage
Returns:
transition usage kind, or null if none applies
createTriggerAction
public static [AcceptActionUsage](sysml/AcceptActionUsage.html) createTriggerAction([TransitionUsage](sysml/TransitionUsage.html) transitionUsage,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Definition](sysml/Definition.html)> definitions)
Creates a trigger action for the transition usage with the given payload definitions.
Parameters:
`transitionUsage` - the transition usage
`definitions` - payload definitions
Returns:
created trigger action
getOrCreateSourceParameter
public static [Feature](../../kerml/model/kerml/Feature.html) getOrCreateSourceParameter([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)
Returns the source parameter of the transition usage, creating it if necessary.
Parameters:
`transitionUsage` - the transition usage
Returns:
existing or newly created source parameter
getOwnedSourceParameter
@CheckForNullpublic static [Feature](../../kerml/model/kerml/Feature.html) getOwnedSourceParameter([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)
Returns the owned source parameter of the transition usage.
Parameters:
`transitionUsage` - the transition usage
Returns:
source parameter, or null if none exists
getOrCreatePayloadParameter
public static [Feature](../../kerml/model/kerml/Feature.html) getOrCreatePayloadParameter([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)
Returns the payload parameter of the transition usage, creating it if necessary.
Parameters:
`transitionUsage` - the transition usage
Returns:
existing or newly created payload parameter
getOwnedPayloadParameter
@CheckForNullpublic static [Feature](../../kerml/model/kerml/Feature.html) getOwnedPayloadParameter([TransitionUsage](sysml/TransitionUsage.html) transitionUsage)
Returns the owned payload parameter of the transition usage.
Parameters:
`transitionUsage` - the transition usage
Returns:
payload parameter, or null if none exists

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Transitions">Class Transitions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Transitions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">Transitions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class providing helper methods for working with <a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>TransitionUsage</code></a></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Transitions.TransitionUsageKind.html" title="enum class in com.dassault_systemes.modeler.sysml.model">Transitions.TransitionUsageKind</a></code></div>
<div class="col-last even-row-color">
<div class="block">Enumeration of transition usage kinds.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Transitions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTriggerAction(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,java.util.List)">createTriggerAction</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a>&gt; definitions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a trigger action for the transition usage with the given payload definitions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEffectActions(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">getEffectActions</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all effect actions of the transition usage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreatePayloadParameter(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">getOrCreatePayloadParameter</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the payload parameter of the transition usage, creating it if necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateSourceParameter(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">getOrCreateSourceParameter</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the source parameter of the transition usage, creating it if necessary.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateSuccession(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">getOrCreateSuccession</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the succession of the transition usage, creating one if necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedGuardExpressions(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">getOwnedGuardExpressions</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all guard expressions owned by the transition usage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedPayloadParameter(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">getOwnedPayloadParameter</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned payload parameter of the transition usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedSourceParameter(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">getOwnedSourceParameter</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned source parameter of the transition usage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceMembership(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">getSourceMembership</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the source membership of the transition usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Transitions.TransitionUsageKind.html" title="enum class in com.dassault_systemes.modeler.sysml.model">Transitions.TransitionUsageKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransitionUsageKind(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">getTransitionUsageKind</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Determines the kind of transition usage based on its owning type and source.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTriggerActions(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">getTriggerActions</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all trigger actions of the transition usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setOwnedGuardExpression(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,com.dassault_systemes.modeler.kerml.model.kerml.Expression)">setOwnedGuardExpression</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage,
 <a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> guard)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the guard expression of the transition usage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSourceChain(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,com.dassault_systemes.modeler.kerml.model.kerml.Succession,java.util.List)">setSourceChain</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage,
 <a href="../../kerml/model/kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a> succession,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Store passed chain in the <a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>TransitionUsage</code></a>.source <a href="../../kerml/model/kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Membership</code></a>.</div>
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
<h3>Transitions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Transitions</span>()</div>
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
<section class="detail" id="getOwnedGuardExpressions(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">
<h3>getOwnedGuardExpressions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt;</span> <span class="element-name">getOwnedGuardExpressions</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</span></div>
<div class="block">Returns all guard expressions owned by the transition usage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transitionUsage</code> - the transition usage</dd>
<dt>Returns:</dt>
<dd>stream of guard expressions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwnedGuardExpression(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,com.dassault_systemes.modeler.kerml.model.kerml.Expression)">
<h3>setOwnedGuardExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setOwnedGuardExpression</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage,
 <a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> guard)</span></div>
<div class="block">Sets the guard expression of the transition usage. If a guard membership
 does not yet exist, one is created. If an existing guard is replaced,
 the old guard is disposed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transitionUsage</code> - the transition usage</dd>
<dd><code>guard</code> - the new guard expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEffectActions(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">
<h3>getEffectActions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt;</span> <span class="element-name">getEffectActions</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</span></div>
<div class="block">Returns all effect actions of the transition usage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transitionUsage</code> - the transition usage</dd>
<dt>Returns:</dt>
<dd>stream of effect actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTriggerActions(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">
<h3>getTriggerActions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a>&gt;</span> <span class="element-name">getTriggerActions</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</span></div>
<div class="block">Returns all trigger actions of the transition usage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transitionUsage</code> - the transition usage</dd>
<dt>Returns:</dt>
<dd>stream of trigger actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSourceChain(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,com.dassault_systemes.modeler.kerml.model.kerml.Succession,java.util.List)">
<h3>setSourceChain</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">setSourceChain</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage,
 <a href="../../kerml/model/kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a> succession,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain)</span></div>
<div class="block">Store passed chain in the <a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>TransitionUsage</code></a>.source <a href="../../kerml/model/kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Membership</code></a>.
 Create implied <a href="../../kerml/model/kerml/ReferenceSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ReferenceSubsetting</code></a> from the source of <a href="../../kerml/model/kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Succession</code></a> to that <a href="../../kerml/model/kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Membership</code></a>.memberElement.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>succession</code> - succession</dd>
<dd><code>chain</code> - source chain</dd>
<dt>Returns:</dt>
<dd>true if a source was changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceMembership(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">
<h3>getSourceMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></span> <span class="element-name">getSourceMembership</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</span></div>
<div class="block">Returns the source membership of the transition usage. The source membership
 is a non-feature membership whose referent is an <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActionUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transitionUsage</code> - the transition usage</dd>
<dt>Returns:</dt>
<dd>source membership, or null if none exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateSuccession(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">
<h3>getOrCreateSuccession</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a></span> <span class="element-name">getOrCreateSuccession</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</span></div>
<div class="block">Returns the succession of the transition usage, creating one if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transitionUsage</code> - the transition usage</dd>
<dt>Returns:</dt>
<dd>existing or newly created succession</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTransitionUsageKind(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">
<h3>getTransitionUsageKind</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="Transitions.TransitionUsageKind.html" title="enum class in com.dassault_systemes.modeler.sysml.model">Transitions.TransitionUsageKind</a></span> <span class="element-name">getTransitionUsageKind</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</span></div>
<div class="block">Determines the kind of transition usage based on its owning type and source.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transitionUsage</code> - the transition usage</dd>
<dt>Returns:</dt>
<dd>transition usage kind, or null if none applies</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTriggerAction(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,java.util.List)">
<h3>createTriggerAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a></span> <span class="element-name">createTriggerAction</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a>&gt; definitions)</span></div>
<div class="block">Creates a trigger action for the transition usage with the given payload definitions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transitionUsage</code> - the transition usage</dd>
<dd><code>definitions</code> - payload definitions</dd>
<dt>Returns:</dt>
<dd>created trigger action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateSourceParameter(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">
<h3>getOrCreateSourceParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreateSourceParameter</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</span></div>
<div class="block">Returns the source parameter of the transition usage, creating it if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transitionUsage</code> - the transition usage</dd>
<dt>Returns:</dt>
<dd>existing or newly created source parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedSourceParameter(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">
<h3>getOwnedSourceParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOwnedSourceParameter</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</span></div>
<div class="block">Returns the owned source parameter of the transition usage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transitionUsage</code> - the transition usage</dd>
<dt>Returns:</dt>
<dd>source parameter, or null if none exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreatePayloadParameter(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">
<h3>getOrCreatePayloadParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreatePayloadParameter</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</span></div>
<div class="block">Returns the payload parameter of the transition usage, creating it if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transitionUsage</code> - the transition usage</dd>
<dt>Returns:</dt>
<dd>existing or newly created payload parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedPayloadParameter(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage)">
<h3>getOwnedPayloadParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOwnedPayloadParameter</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> transitionUsage)</span></div>
<div class="block">Returns the owned payload parameter of the transition usage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transitionUsage</code> - the transition usage</dd>
<dt>Returns:</dt>
<dd>payload parameter, or null if none exists</dd>
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
