# JAVA OPENAPI: ActionsLibrary (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/libraries/standard/ActionsLibrary.html
- source_path: `com/dassault_systemes/modeler/sysml/libraries/standard/ActionsLibrary.html`
- source_sha256: `98e9d3dde22b95c064733aef7fbd9ed8d7b730a50b03dea746c764e7ca44fba9`
- captured_utc: `2026-07-14T16:44:51.938896+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.libraries.standard](package-summary.html)

## Class ActionsLibrary

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[ModelElementProject](../../../foundation/project/ModelElementProject.html)>
[com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)
com.dassault_systemes.modeler.sysml.libraries.standard.ActionsLibrary

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`

@OpenApiAllpublic classActionsLibrary
extends [AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)

Access helper for the actions standard library.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[ActionsLibrary.AcceptActionsActionUsage](ActionsLibrary.AcceptActionsActionUsage.html)`
Wrapper for the accept actions action usage library element.
`static class`
`[ActionsLibrary.ActionActionDefinition](ActionsLibrary.ActionActionDefinition.html)`
Wrapper for the action action definition library element.
`static class`
`[ActionsLibrary.ActionsActionUsage](ActionsLibrary.ActionsActionUsage.html)`
Wrapper for the actions action usage library element.
`static class`
`[ActionsLibrary.AssignmentActionsActionUsage](ActionsLibrary.AssignmentActionsActionUsage.html)`
Wrapper for the assignment actions action usage library element.
`static class`
`[ActionsLibrary.ForLoopActionActionDefinition](ActionsLibrary.ForLoopActionActionDefinition.html)`
Wrapper for the for loop action action definition library element.
`static class`
`[ActionsLibrary.ForLoopActionsActionUsage](ActionsLibrary.ForLoopActionsActionUsage.html)`
Wrapper for the for loop actions action usage library element.
`static class`
`[ActionsLibrary.IfThenActionsActionUsage](ActionsLibrary.IfThenActionsActionUsage.html)`
Wrapper for the if then actions action usage library element.
`static class`
`[ActionsLibrary.IfThenElseActionActionDefinition](ActionsLibrary.IfThenElseActionActionDefinition.html)`
Wrapper for the if then else action action definition library element.
`static class`
`[ActionsLibrary.IfThenElseActionsActionUsage](ActionsLibrary.IfThenElseActionsActionUsage.html)`
Wrapper for the if then else actions action usage library element.
`static class`
`[ActionsLibrary.SendActionsActionUsage](ActionsLibrary.SendActionsActionUsage.html)`
Wrapper for the send actions action usage library element.
`static class`
`[ActionsLibrary.TerminateActionsActionUsage](ActionsLibrary.TerminateActionsActionUsage.html)`
Wrapper for the terminate actions action usage library element.
`static class`
`[ActionsLibrary.TransitionActionActionDefinition](ActionsLibrary.TransitionActionActionDefinition.html)`
Wrapper for the transition action action definition library element.
`static class`
`[ActionsLibrary.TransitionActionsActionUsage](ActionsLibrary.TransitionActionsActionUsage.html)`
Wrapper for the transition actions action usage library element.
`static class`
`[ActionsLibrary.WhileLoopActionsActionUsage](ActionsLibrary.WhileLoopActionsActionUsage.html)`
Wrapper for the while loop actions action usage library element.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ActionsLibrary](#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Creates a new actions library instance.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[ActionsLibrary.AcceptActionsActionUsage](ActionsLibrary.AcceptActionsActionUsage.html)`
`[acceptActions](#acceptActions())()`
Returns accept actions.
`[ActionsLibrary.ActionActionDefinition](ActionsLibrary.ActionActionDefinition.html)`
`[Action](#Action())()`
Returns action.
`[ActionsLibrary.ActionsActionUsage](ActionsLibrary.ActionsActionUsage.html)`
`[actions](#actions())()`
Returns actions.
`[ActionsLibrary.AssignmentActionsActionUsage](ActionsLibrary.AssignmentActionsActionUsage.html)`
`[assignmentActions](#assignmentActions())()`
Returns assignment actions.
`[ActionsLibrary.ForLoopActionActionDefinition](ActionsLibrary.ForLoopActionActionDefinition.html)`
`[ForLoopAction](#ForLoopAction())()`
Returns for loop action.
`[ActionsLibrary.ForLoopActionsActionUsage](ActionsLibrary.ForLoopActionsActionUsage.html)`
`[forLoopActions](#forLoopActions())()`
Returns for loop actions.
`static [ActionsLibrary](ActionsLibrary.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)`
Returns the library instance for the project that owns the given element.
`static [ActionsLibrary](ActionsLibrary.html)`
`[getInstanceByProject](#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Returns the library instance for the given project.
`protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper>`
`[getTypeWrappers](#getTypeWrappers())()`
Returns get type wrappers.
`[ActionsLibrary.IfThenActionsActionUsage](ActionsLibrary.IfThenActionsActionUsage.html)`
`[ifThenActions](#ifThenActions())()`
Returns if then actions.
`[ActionsLibrary.IfThenElseActionActionDefinition](ActionsLibrary.IfThenElseActionActionDefinition.html)`
`[IfThenElseAction](#IfThenElseAction())()`
Returns if then else action.
`[ActionsLibrary.IfThenElseActionsActionUsage](ActionsLibrary.IfThenElseActionsActionUsage.html)`
`[ifThenElseActions](#ifThenElseActions())()`
Returns if then else actions.
`boolean`
`[isSemantic](#isSemantic())()`
Returns whether this library is semantic.
`protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[packagesNames](#packagesNames())()`
Returns the names of the packages that belong to this library.
`[ActionsLibrary.SendActionsActionUsage](ActionsLibrary.SendActionsActionUsage.html)`
`[sendActions](#sendActions())()`
Returns send actions.
`[ActionsLibrary.TerminateActionsActionUsage](ActionsLibrary.TerminateActionsActionUsage.html)`
`[terminateActions](#terminateActions())()`
Returns terminate actions.
`[ActionsLibrary.TransitionActionActionDefinition](ActionsLibrary.TransitionActionActionDefinition.html)`
`[TransitionAction](#TransitionAction())()`
Returns transition action.
`[ActionsLibrary.TransitionActionsActionUsage](ActionsLibrary.TransitionActionsActionUsage.html)`
`[transitionActions](#transitionActions())()`
Returns transition actions.
`[ActionsLibrary.WhileLoopActionsActionUsage](ActionsLibrary.WhileLoopActionsActionUsage.html)`
`[whileLoopActions](#whileLoopActions())()`
Returns while loop actions.
Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)
`[findFunctionInLibrary](../../../kerml/libraries/AbstractLibrary.html#findFunctionInLibrary(java.lang.String)), [findLibraryPackage](../../../kerml/libraries/AbstractLibrary.html#findLibraryPackage(java.lang.String)), [findPackage](../../../kerml/libraries/AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)), [getLibraryPackages](../../../kerml/libraries/AbstractLibrary.html#getLibraryPackages()), [getNamespace](../../../kerml/libraries/AbstractLibrary.html#getNamespace()), [initialized](../../../kerml/libraries/AbstractLibrary.html#initialized())`
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ActionsLibrary
public ActionsLibrary([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Creates a new actions library instance.
Parameters:
`project` - the project
 ============ METHOD DETAIL ========== 
Method Details
getInstanceByProject
public static [ActionsLibrary](ActionsLibrary.html) getInstanceByProject([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Returns the library instance for the given project.
Parameters:
`project` - the project
Returns:
get instance by project
getInstance
public static [ActionsLibrary](ActionsLibrary.html) getInstance([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)
Returns the library instance for the project that owns the given element.
Parameters:
`element` - the element
Returns:
get instance
isSemantic
public boolean isSemantic()
Returns whether this library is semantic.
Specified by:
`[isSemantic](../../../kerml/libraries/AbstractLibrary.html#isSemantic())` in class `[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)`
Returns:
`true` if semantic; `false` otherwise
packagesNames
protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> packagesNames()
Returns the names of the packages that belong to this library.
Specified by:
`[packagesNames](../../../kerml/libraries/AbstractLibrary.html#packagesNames())` in class `[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)`
Returns:
packages names
Action
public [ActionsLibrary.ActionActionDefinition](ActionsLibrary.ActionActionDefinition.html) Action()
Returns action.
Returns:
action
actions
public [ActionsLibrary.ActionsActionUsage](ActionsLibrary.ActionsActionUsage.html) actions()
Returns actions.
Returns:
actions
sendActions
public [ActionsLibrary.SendActionsActionUsage](ActionsLibrary.SendActionsActionUsage.html) sendActions()
Returns send actions.
Returns:
send actions
acceptActions
public [ActionsLibrary.AcceptActionsActionUsage](ActionsLibrary.AcceptActionsActionUsage.html) acceptActions()
Returns accept actions.
Returns:
accept actions
terminateActions
public [ActionsLibrary.TerminateActionsActionUsage](ActionsLibrary.TerminateActionsActionUsage.html) terminateActions()
Returns terminate actions.
Returns:
terminate actions
TransitionAction
public [ActionsLibrary.TransitionActionActionDefinition](ActionsLibrary.TransitionActionActionDefinition.html) TransitionAction()
Returns transition action.
Returns:
transition action
transitionActions
public [ActionsLibrary.TransitionActionsActionUsage](ActionsLibrary.TransitionActionsActionUsage.html) transitionActions()
Returns transition actions.
Returns:
transition actions
assignmentActions
public [ActionsLibrary.AssignmentActionsActionUsage](ActionsLibrary.AssignmentActionsActionUsage.html) assignmentActions()
Returns assignment actions.
Returns:
assignment actions
IfThenElseAction
public [ActionsLibrary.IfThenElseActionActionDefinition](ActionsLibrary.IfThenElseActionActionDefinition.html) IfThenElseAction()
Returns if then else action.
Returns:
if then else action
ifThenActions
public [ActionsLibrary.IfThenActionsActionUsage](ActionsLibrary.IfThenActionsActionUsage.html) ifThenActions()
Returns if then actions.
Returns:
if then actions
ifThenElseActions
public [ActionsLibrary.IfThenElseActionsActionUsage](ActionsLibrary.IfThenElseActionsActionUsage.html) ifThenElseActions()
Returns if then else actions.
Returns:
if then else actions
ForLoopAction
public [ActionsLibrary.ForLoopActionActionDefinition](ActionsLibrary.ForLoopActionActionDefinition.html) ForLoopAction()
Returns for loop action.
Returns:
for loop action
whileLoopActions
public [ActionsLibrary.WhileLoopActionsActionUsage](ActionsLibrary.WhileLoopActionsActionUsage.html) whileLoopActions()
Returns while loop actions.
Returns:
while loop actions
forLoopActions
public [ActionsLibrary.ForLoopActionsActionUsage](ActionsLibrary.ForLoopActionsActionUsage.html) forLoopActions()
Returns for loop actions.
Returns:
for loop actions
getTypeWrappers
protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper> getTypeWrappers()
Returns get type wrappers.
Specified by:
`[getTypeWrappers](../../../kerml/libraries/AbstractLibrary.html#getTypeWrappers())` in class `[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)`
Returns:
get type wrappers

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.libraries.standard</a></div>
<h1 class="title" title="Class ActionsLibrary">Class ActionsLibrary</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a>&gt;
<div class="inheritance"><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.libraries.standard.ActionsLibrary</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.service.DisposableService</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ActionsLibrary</span>
<span class="extends-implements">extends <a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></span></div>
<div class="block">Access helper for the actions standard library.</div>
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
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ActionsLibrary.AcceptActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.AcceptActionsActionUsage</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the accept actions action usage library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ActionsLibrary.ActionActionDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.ActionActionDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the action action definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ActionsLibrary.ActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.ActionsActionUsage</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the actions action usage library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ActionsLibrary.AssignmentActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.AssignmentActionsActionUsage</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the assignment actions action usage library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ActionsLibrary.ForLoopActionActionDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.ForLoopActionActionDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the for loop action action definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ActionsLibrary.ForLoopActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.ForLoopActionsActionUsage</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the for loop actions action usage library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ActionsLibrary.IfThenActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.IfThenActionsActionUsage</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the if then actions action usage library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ActionsLibrary.IfThenElseActionActionDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.IfThenElseActionActionDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the if then else action action definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ActionsLibrary.IfThenElseActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.IfThenElseActionsActionUsage</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the if then else actions action usage library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ActionsLibrary.SendActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.SendActionsActionUsage</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the send actions action usage library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ActionsLibrary.TerminateActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.TerminateActionsActionUsage</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the terminate actions action usage library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ActionsLibrary.TransitionActionActionDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.TransitionActionActionDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the transition action action definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ActionsLibrary.TransitionActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.TransitionActionsActionUsage</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the transition actions action usage library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ActionsLibrary.WhileLoopActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.WhileLoopActionsActionUsage</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the while loop actions action usage library element.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">ActionsLibrary</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new actions library instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.AcceptActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.AcceptActionsActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#acceptActions()">acceptActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns accept actions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.ActionActionDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.ActionActionDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Action()">Action</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.ActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.ActionsActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#actions()">actions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns actions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.AssignmentActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.AssignmentActionsActionUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#assignmentActions()">assignmentActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns assignment actions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.ForLoopActionActionDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.ForLoopActionActionDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ForLoopAction()">ForLoopAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns for loop action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.ForLoopActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.ForLoopActionsActionUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#forLoopActions()">forLoopActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns for loop actions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ActionsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the library instance for the project that owns the given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ActionsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getInstanceByProject</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the library instance for the given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeWrappers()">getTypeWrappers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns get type wrappers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.IfThenActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.IfThenActionsActionUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ifThenActions()">ifThenActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns if then actions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.IfThenElseActionActionDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.IfThenElseActionActionDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#IfThenElseAction()">IfThenElseAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns if then else action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.IfThenElseActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.IfThenElseActionsActionUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ifThenElseActions()">ifThenElseActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns if then else actions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSemantic()">isSemantic</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether this library is semantic.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#packagesNames()">packagesNames</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the names of the packages that belong to this library.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.SendActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.SendActionsActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sendActions()">sendActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns send actions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.TerminateActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.TerminateActionsActionUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#terminateActions()">terminateActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns terminate actions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.TransitionActionActionDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.TransitionActionActionDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#TransitionAction()">TransitionAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns transition action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.TransitionActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.TransitionActionsActionUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#transitionActions()">transitionActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns transition actions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsLibrary.WhileLoopActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.WhileLoopActionsActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#whileLoopActions()">whileLoopActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns while loop actions.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary">Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.<a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></h3>
<code><a href="../../../kerml/libraries/AbstractLibrary.html#findFunctionInLibrary(java.lang.String)">findFunctionInLibrary</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#findLibraryPackage(java.lang.String)">findLibraryPackage</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)">findPackage</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#getLibraryPackages()">getLibraryPackages</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#getNamespace()">getNamespace</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#initialized()">initialized</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService">Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService</h3>
<code>disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject</code></div>
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
<section class="detail" id="&lt;init&gt;(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>ActionsLibrary</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ActionsLibrary</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Creates a new actions library instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project</dd>
</dl>
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
<section class="detail" id="getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>getInstanceByProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ActionsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Returns the library instance for the given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project</dd>
<dt>Returns:</dt>
<dd>get instance by project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ActionsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns the library instance for the project that owns the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>get instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSemantic()">
<h3>isSemantic</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSemantic</span>()</div>
<div class="block">Returns whether this library is semantic.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/libraries/AbstractLibrary.html#isSemantic()">isSemantic</a></code> in class <code><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd><code>true</code> if semantic; <code>false</code> otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="packagesNames()">
<h3>packagesNames</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">packagesNames</span>()</div>
<div class="block">Returns the names of the packages that belong to this library.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/libraries/AbstractLibrary.html#packagesNames()">packagesNames</a></code> in class <code><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd>packages names</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Action()">
<h3>Action</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.ActionActionDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.ActionActionDefinition</a></span> <span class="element-name">Action</span>()</div>
<div class="block">Returns action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="actions()">
<h3>actions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.ActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.ActionsActionUsage</a></span> <span class="element-name">actions</span>()</div>
<div class="block">Returns actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendActions()">
<h3>sendActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.SendActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.SendActionsActionUsage</a></span> <span class="element-name">sendActions</span>()</div>
<div class="block">Returns send actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>send actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="acceptActions()">
<h3>acceptActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.AcceptActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.AcceptActionsActionUsage</a></span> <span class="element-name">acceptActions</span>()</div>
<div class="block">Returns accept actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>accept actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="terminateActions()">
<h3>terminateActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.TerminateActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.TerminateActionsActionUsage</a></span> <span class="element-name">terminateActions</span>()</div>
<div class="block">Returns terminate actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>terminate actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TransitionAction()">
<h3>TransitionAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.TransitionActionActionDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.TransitionActionActionDefinition</a></span> <span class="element-name">TransitionAction</span>()</div>
<div class="block">Returns transition action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>transition action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="transitionActions()">
<h3>transitionActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.TransitionActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.TransitionActionsActionUsage</a></span> <span class="element-name">transitionActions</span>()</div>
<div class="block">Returns transition actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>transition actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="assignmentActions()">
<h3>assignmentActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.AssignmentActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.AssignmentActionsActionUsage</a></span> <span class="element-name">assignmentActions</span>()</div>
<div class="block">Returns assignment actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>assignment actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IfThenElseAction()">
<h3>IfThenElseAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.IfThenElseActionActionDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.IfThenElseActionActionDefinition</a></span> <span class="element-name">IfThenElseAction</span>()</div>
<div class="block">Returns if then else action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>if then else action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ifThenActions()">
<h3>ifThenActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.IfThenActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.IfThenActionsActionUsage</a></span> <span class="element-name">ifThenActions</span>()</div>
<div class="block">Returns if then actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>if then actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ifThenElseActions()">
<h3>ifThenElseActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.IfThenElseActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.IfThenElseActionsActionUsage</a></span> <span class="element-name">ifThenElseActions</span>()</div>
<div class="block">Returns if then else actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>if then else actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ForLoopAction()">
<h3>ForLoopAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.ForLoopActionActionDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.ForLoopActionActionDefinition</a></span> <span class="element-name">ForLoopAction</span>()</div>
<div class="block">Returns for loop action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>for loop action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="whileLoopActions()">
<h3>whileLoopActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.WhileLoopActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.WhileLoopActionsActionUsage</a></span> <span class="element-name">whileLoopActions</span>()</div>
<div class="block">Returns while loop actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>while loop actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="forLoopActions()">
<h3>forLoopActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsLibrary.ForLoopActionsActionUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary.ForLoopActionsActionUsage</a></span> <span class="element-name">forLoopActions</span>()</div>
<div class="block">Returns for loop actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>for loop actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypeWrappers()">
<h3>getTypeWrappers</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</span> <span class="element-name">getTypeWrappers</span>()</div>
<div class="block">Returns get type wrappers.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/libraries/AbstractLibrary.html#getTypeWrappers()">getTypeWrappers</a></code> in class <code><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd>get type wrappers</dd>
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
