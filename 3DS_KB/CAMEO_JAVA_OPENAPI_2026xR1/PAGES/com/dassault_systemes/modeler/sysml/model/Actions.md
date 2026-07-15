# JAVA OPENAPI: Actions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Actions.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Actions.html`
- source_sha256: `e77e6e19e7f979bae051ce1b7a56b16f8a6cb8fec170d741dcc2af75c28256d7`
- captured_utc: `2026-07-14T16:45:02.105029+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Actions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Actions

@OpenApiAllpublic classActions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility methods for identifying action usages and definitions, as well as
 common action subtypes such as if-actions, loop-actions, assignment actions,
 accept actions, send actions, and terminate actions.
 These helpers centralize common type checks and provide convenience access
 to owned and created input parameters of [`ActionUsage`](sysml/ActionUsage.html) elements.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Actions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ActionUsage](sysml/ActionUsage.html)>`
`[getActions](#getActions(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns all [`ActionUsage`](sysml/ActionUsage.html) elements referenced by the given type.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOrCreateInputParameter](#getOrCreateInputParameter(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,int))([ActionUsage](sysml/ActionUsage.html) actionUsage,
 int index)`
Returns the input parameter at the given index, creating it if necessary.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ActionUsage](sysml/ActionUsage.html)>`
`[getOwnedActions](#getOwnedActions(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the actions owned directly by the given type.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOwnedInputParameter](#getOwnedInputParameter(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,int))([ActionUsage](sysml/ActionUsage.html) actionUsage,
 int index)`
Returns the owned input parameter at the given index, or `null`
 if it does not exist.
`static boolean`
`[isActionUsageOrDefinition](#isActionUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Returns whether the given element is an [`ActionUsage`](sysml/ActionUsage.html) or
 [`ActionDefinition`](sysml/ActionDefinition.html).
`static boolean`
`[isActionUsageOrDefinition](#isActionUsageOrDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents an action usage or definition.
`static boolean`
`[isDoneActionUsage](#isDoneActionUsage(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Returns whether the given element represents a “done” action usage.
`static boolean`
`[isForLoopActionUsage](#isForLoopActionUsage(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents a for-loop action usage.
`static boolean`
`[isIfActionUsage](#isIfActionUsage(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents an if-action usage.
`static boolean`
`[isIfOrLoopActionUsage](#isIfOrLoopActionUsage(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents an if-action or a loop-action.
`static boolean`
`[isSpecialAction](#isSpecialAction(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents a “special” action.
`static boolean`
`[isStartActionUsage](#isStartActionUsage(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Returns whether the given element represents a “start” action usage.
`static boolean`
`[isWhileLoopActionUsage](#isWhileLoopActionUsage(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents a while-loop action usage.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Actions
public Actions()
 ============ METHOD DETAIL ========== 
Method Details
isSpecialAction
public static boolean isSpecialAction(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents a “special” action.
 Special actions include:
 control nodes,
if- and loop-action usages,
assignment actions,
accept actions,
send actions, and
terminate actions.
Parameters:
`eClass` - the class to test
Returns:
`true` if the class represents a special action
isIfOrLoopActionUsage
public static boolean isIfOrLoopActionUsage(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents an if-action or a loop-action.
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is an if-action or loop-action usage
isForLoopActionUsage
public static boolean isForLoopActionUsage(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents a for-loop action usage.
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is a for-loop action usage
isIfActionUsage
public static boolean isIfActionUsage(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents an if-action usage.
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is an if-action usage
isWhileLoopActionUsage
public static boolean isWhileLoopActionUsage(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents a while-loop action usage.
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is a while-loop action usage
isActionUsageOrDefinition
public static boolean isActionUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Returns whether the given element is an [`ActionUsage`](sysml/ActionUsage.html) or
 [`ActionDefinition`](sysml/ActionDefinition.html).
Parameters:
`element` - the element to test
Returns:
`true` if the element is an action usage or definition
isActionUsageOrDefinition
public static boolean isActionUsageOrDefinition(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents an action usage or definition.
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is an action usage or definition
getActions
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ActionUsage](sysml/ActionUsage.html)> getActions([Type](../../kerml/model/kerml/Type.html) type)
Returns all [`ActionUsage`](sysml/ActionUsage.html) elements referenced by the given type.
 This includes inherited and non-owned actions.
Parameters:
`type` - the type whose actions are requested
Returns:
a list of action usages
getOwnedActions
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ActionUsage](sysml/ActionUsage.html)> getOwnedActions([Type](../../kerml/model/kerml/Type.html) type)
Returns the actions owned directly by the given type.
 Definitions expose owned actions.
Usages expose nested actions.
Parameters:
`type` - the type whose owned actions are requested
Returns:
a list of owned action usages
isDoneActionUsage
public static boolean isDoneActionUsage([Element](../../kerml/model/kerml/Element.html) element)
Returns whether the given element represents a “done” action usage.
 This is determined via the [`ActionsLibrary`](../libraries/standard/ActionsLibrary.html) and redefinition semantics.
Parameters:
`element` - the element to test
Returns:
`true` if the element is a done action usage
isStartActionUsage
public static boolean isStartActionUsage([Element](../../kerml/model/kerml/Element.html) element)
Returns whether the given element represents a “start” action usage.
Parameters:
`element` - the element to test
Returns:
`true` if the element is a start action usage
getOrCreateInputParameter
public static [Feature](../../kerml/model/kerml/Feature.html) getOrCreateInputParameter([ActionUsage](sysml/ActionUsage.html) actionUsage,
 int index)
Returns the input parameter at the given index, creating it if necessary.
Parameters:
`actionUsage` - the action usage
`index` - the parameter index
Returns:
the existing or newly created input parameter
getOwnedInputParameter
@CheckForNullpublic static [Feature](../../kerml/model/kerml/Feature.html) getOwnedInputParameter([ActionUsage](sysml/ActionUsage.html) actionUsage,
 int index)
Returns the owned input parameter at the given index, or `null`
 if it does not exist.
Parameters:
`actionUsage` - the action usage
`index` - the parameter index
Returns:
the owned input parameter, or `null`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Actions">Class Actions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Actions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Actions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility methods for identifying action usages and definitions, as well as
 common action subtypes such as if-actions, loop-actions, assignment actions,
 accept actions, send actions, and terminate actions.
 <p>
 These helpers centralize common type checks and provide convenience access
 to owned and created input parameters of <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActionUsage</code></a> elements.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Actions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getActions(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getActions</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActionUsage</code></a> elements referenced by the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateInputParameter(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,int)">getOrCreateInputParameter</a><wbr/>(<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> actionUsage,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the input parameter at the given index, creating it if necessary.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedActions(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedActions</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the actions owned directly by the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedInputParameter(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,int)">getOwnedInputParameter</a><wbr/>(<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> actionUsage,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned input parameter at the given index, or <code>null</code>
 if it does not exist.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isActionUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isActionUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given element is an <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActionUsage</code></a> or
 <a href="sysml/ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActionDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isActionUsageOrDefinition(org.eclipse.emf.ecore.EClass)">isActionUsageOrDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents an action usage or definition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDoneActionUsage(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isDoneActionUsage</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given element represents a “done” action usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isForLoopActionUsage(org.eclipse.emf.ecore.EClass)">isForLoopActionUsage</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents a for-loop action usage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isIfActionUsage(org.eclipse.emf.ecore.EClass)">isIfActionUsage</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents an if-action usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isIfOrLoopActionUsage(org.eclipse.emf.ecore.EClass)">isIfOrLoopActionUsage</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents an if-action or a loop-action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSpecialAction(org.eclipse.emf.ecore.EClass)">isSpecialAction</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents a “special” action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStartActionUsage(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isStartActionUsage</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given element represents a “start” action usage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isWhileLoopActionUsage(org.eclipse.emf.ecore.EClass)">isWhileLoopActionUsage</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents a while-loop action usage.</div>
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
<h3>Actions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Actions</span>()</div>
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
<section class="detail" id="isSpecialAction(org.eclipse.emf.ecore.EClass)">
<h3>isSpecialAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSpecialAction</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents a “special” action.
 Special actions include:
 <ul>
<li>control nodes,</li>
<li>if- and loop-action usages,</li>
<li>assignment actions,</li>
<li>accept actions,</li>
<li>send actions, and</li>
<li>terminate actions.</li>
</ul></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class represents a special action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isIfOrLoopActionUsage(org.eclipse.emf.ecore.EClass)">
<h3>isIfOrLoopActionUsage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isIfOrLoopActionUsage</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents an if-action or a loop-action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is an if-action or loop-action usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isForLoopActionUsage(org.eclipse.emf.ecore.EClass)">
<h3>isForLoopActionUsage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isForLoopActionUsage</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents a for-loop action usage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is a for-loop action usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isIfActionUsage(org.eclipse.emf.ecore.EClass)">
<h3>isIfActionUsage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isIfActionUsage</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents an if-action usage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is an if-action usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isWhileLoopActionUsage(org.eclipse.emf.ecore.EClass)">
<h3>isWhileLoopActionUsage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isWhileLoopActionUsage</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents a while-loop action usage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is a while-loop action usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isActionUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isActionUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isActionUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns whether the given element is an <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActionUsage</code></a> or
 <a href="sysml/ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActionDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the element is an action usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isActionUsageOrDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isActionUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isActionUsageOrDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents an action usage or definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is an action usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActions(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getActions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt;</span> <span class="element-name">getActions</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns all <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActionUsage</code></a> elements referenced by the given type.
 This includes inherited and non-owned actions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose actions are requested</dd>
<dt>Returns:</dt>
<dd>a list of action usages</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedActions(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedActions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt;</span> <span class="element-name">getOwnedActions</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the actions owned directly by the given type.
 <ul>
<li>Definitions expose owned actions.</li>
<li>Usages expose nested actions.</li>
</ul></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose owned actions are requested</dd>
<dt>Returns:</dt>
<dd>a list of owned action usages</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDoneActionUsage(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isDoneActionUsage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDoneActionUsage</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns whether the given element represents a “done” action usage.
 This is determined via the <a href="../libraries/standard/ActionsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard"><code>ActionsLibrary</code></a> and redefinition semantics.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the element is a done action usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStartActionUsage(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isStartActionUsage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStartActionUsage</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns whether the given element represents a “start” action usage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the element is a start action usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateInputParameter(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,int)">
<h3>getOrCreateInputParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreateInputParameter</span><wbr/><span class="parameters">(<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> actionUsage,
 int index)</span></div>
<div class="block">Returns the input parameter at the given index, creating it if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the action usage</dd>
<dd><code>index</code> - the parameter index</dd>
<dt>Returns:</dt>
<dd>the existing or newly created input parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedInputParameter(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,int)">
<h3>getOwnedInputParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOwnedInputParameter</span><wbr/><span class="parameters">(<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> actionUsage,
 int index)</span></div>
<div class="block">Returns the owned input parameter at the given index, or <code>null</code>
 if it does not exist.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the action usage</dd>
<dd><code>index</code> - the parameter index</dd>
<dt>Returns:</dt>
<dd>the owned input parameter, or <code>null</code></dd>
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
