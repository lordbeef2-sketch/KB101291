# JAVA OPENAPI: DiagramValidator (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/validation/DiagramValidator.html
- source_path: `com/nomagic/magicdraw/validation/DiagramValidator.html`
- source_sha256: `76b2e339f4c8f95b8b984c159450c36ad68e52250a6b2f7fa32d7543fff0f5f8`
- captured_utc: `2026-07-14T16:52:20.146988+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.validation](package-summary.html)

## Class DiagramValidator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.validation.DiagramValidator

All Implemented Interfaces:
`[ValidationRule](ValidationRule.html)`

Direct Known Subclasses:
`[OpenedDiagramValidator](OpenedDiagramValidator.html)`

@OpenApiAllpublic abstract classDiagramValidator
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [ValidationRule](ValidationRule.html)

Rule to validate elements of diagrams by a given scope (all diagrams in project, only active diagrams or diagrams from a specific scope).
 Rule is triggered after various diagram related events like changes in the owned symbols, switching the active diagram.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramValidator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`protected boolean`
`[acceptDiagram](#acceptDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) diagram)`

`void`
`[dispose](#dispose())()`
Unregisters all listeners that were registered and releases other resources.
`abstract [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Annotation](../annotation/Annotation.html)>`
`[getAnnotations](#getAnnotations(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
Return [`Annotation`](../annotation/Annotation.html) object for each [`Element`](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) or [`PresentationElement`](../uml/symbols/PresentationElement.html) which should be annotated.
`protected final [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)>`
`[getDiagrams](#getDiagrams())()`

`protected final [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)>`
`[getDiagramsStream](#getDiagramsStream())()`

`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../uml/symbols/PresentationElement.html)>`
`[getPresentationElements](#getPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../uml/symbols/PresentationElement.html)>`
`[getPresentationElements](#getPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)> diagrams)`

`protected [Project](../core/Project.html)`
`[getProject](#getProject())()`
Get the project.
`void`
`[init](#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
This is the first method that is invoked on the implementation of the `ValidationRule` interface.
`boolean`
`[isElementInScope](#isElementInScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
If DiagramValidator is to be used in passive validation, then model part to validate can be selected.
`boolean`
`[needsRun](#needsRun())()`
Returns whether the validation rule needs to run.
`protected boolean`
`[needsRun](#needsRun(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) event)`
Check if validator needs to re-run after given change event occurred.
`final [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Annotation](../annotation/Annotation.html)>`
`[run](#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
Run the validation.
`protected void`
`[setNeedsRun](#setNeedsRun(boolean))(boolean run)`
Sets flag if this validator has to be re-run, meaning if [`getAnnotations(Project, Constraint)`](#getAnnotations(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)) method should be called again.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramValidator
public DiagramValidator()
 ============ METHOD DETAIL ========== 
Method Details
init
public void init([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
Description copied from interface: `[ValidationRule](ValidationRule.html#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))`
This is the first method that is invoked on the implementation of the `ValidationRule` interface.
 Implementation can initialize internal state if required.
Specified by:
`[init](ValidationRule.html#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))` in interface `[ValidationRule](ValidationRule.html)`
Parameters:
`project` - a project of the constraint
`constraint` - a constraint object
needsRun
protected boolean needsRun([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) event)
Check if validator needs to re-run after given change event occurred.
Parameters:
`event` - event occurred.
Returns:
true need to validate.
run
public final [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Annotation](../annotation/Annotation.html)> run([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
Description copied from interface: `[ValidationRule](ValidationRule.html#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))`
Run the validation.
Specified by:
`[run](ValidationRule.html#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))` in interface `[ValidationRule](ValidationRule.html)`
Parameters:
`project` - a project of the constraint
`constraint` - a constraint object
Returns:
set of [`Annotation`](../annotation/Annotation.html) objects
getAnnotations
public abstract [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Annotation](../annotation/Annotation.html)> getAnnotations([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
Return [`Annotation`](../annotation/Annotation.html) object for each [`Element`](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) or [`PresentationElement`](../uml/symbols/PresentationElement.html) which should be annotated.
 Only the elements represented in diagrams returned by [`getDiagrams()`](#getDiagrams()) method should be analyzed.
Parameters:
`project` - currently active project
`constraint` - a validation rule or a legend item. Use this element to construct [`Annotation`](../annotation/Annotation.html) objects.
Returns:
annotations targeting elements from the diagrams in scope
needsRun
public boolean needsRun()
Description copied from interface: `[ValidationRule](ValidationRule.html#needsRun())`
Returns whether the validation rule needs to run.
Specified by:
`[needsRun](ValidationRule.html#needsRun())` in interface `[ValidationRule](ValidationRule.html)`
Returns:
true if validation rule needs to run, otherwise false
setNeedsRun
protected void setNeedsRun(boolean run)
Sets flag if this validator has to be re-run, meaning if [`getAnnotations(Project, Constraint)`](#getAnnotations(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)) method should be called again.
 Actual re-run is done by the validation engine.
Parameters:
`run` - true to mark validator for rerun
dispose
public void dispose()
Unregisters all listeners that were registered and releases other resources.
Specified by:
`[dispose](ValidationRule.html#dispose())` in interface `[ValidationRule](ValidationRule.html)`
getProject
protected [Project](../core/Project.html) getProject()
Get the project.
Returns:
project
getDiagramsStream
protected final [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)> getDiagramsStream()
Returns:
Stream of the same diagrams as returned by [`getDiagrams()`](#getDiagrams()) method. Convenience method.
getDiagrams
protected final [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)> getDiagrams()
Returns:
collection of diagrams for which used elements annotations should be calculated in [`getAnnotations(Project, Constraint)`](#getAnnotations(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)) method.
acceptDiagram
protected boolean acceptDiagram([DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) diagram)
Returns:
true if the diagram in scope should be returned by [`getDiagrams()`](#getDiagrams()) method
getPresentationElements
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../uml/symbols/PresentationElement.html)> getPresentationElements([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Parameters:
`element` - element to get presentation elements for
Returns:
presentation elements of the given element from all diagrams that are currently in scope
getPresentationElements
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../uml/symbols/PresentationElement.html)> getPresentationElements([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)> diagrams)
Parameters:
`element` - element to get presentation elements for
`diagrams` - diagrams of interest
Returns:
presentation elements of the given element from given diagrams
isElementInScope
public boolean isElementInScope([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
If DiagramValidator is to be used in passive validation, then model part to validate can be selected.
 So certain elements used in the diagram should be validated (they are in selected model scope) and certain should be ignored.
 Only annotate the element, or it's symbol if the element is in scope.
 Recommendation is to call this method for failing elements only as the last check, since many calls to this method might affect performance in certain scenarios
Parameters:
`element` - element which is used in any of the diagrams in scope
Returns:
true if the element is in the model scope for the current validation

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.validation</a></div>
<h1 class="title" title="Class DiagramValidator">Class DiagramValidator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.validation.DiagramValidator</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ValidationRule.html" title="interface in com.nomagic.magicdraw.validation">ValidationRule</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="OpenedDiagramValidator.html" title="class in com.nomagic.magicdraw.validation">OpenedDiagramValidator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">DiagramValidator</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="ValidationRule.html" title="interface in com.nomagic.magicdraw.validation">ValidationRule</a></span></div>
<div class="block">Rule to validate elements of diagrams by a given scope (all diagrams in project, only active diagrams or diagrams from a specific scope).
 Rule is triggered after various diagram related events like changes in the owned symbols, switching the active diagram.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DiagramValidator</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#acceptDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">acceptDiagram</a><wbr/>(<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregisters all listeners that were registered and releases other resources.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAnnotations(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">getAnnotations</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return <a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation"><code>Annotation</code></a> object for each <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a> or <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>PresentationElement</code></a> which should be annotated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagrams()">getDiagrams</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramsStream()">getDiagramsStream</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getPresentationElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">getPresentationElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt; diagrams)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">init</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This is the first method that is invoked on the implementation of the <code>ValidationRule</code> interface.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementInScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isElementInScope</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If DiagramValidator is to be used in passive validation, then model part to validate can be selected.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#needsRun()">needsRun</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether the validation rule needs to run.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#needsRun(java.beans.PropertyChangeEvent)">needsRun</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> event)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if validator needs to re-run after given change event occurred.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">run</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Run the validation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNeedsRun(boolean)">setNeedsRun</a><wbr/>(boolean run)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets flag if this validator has to be re-run, meaning if <a href="#getAnnotations(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)"><code>getAnnotations(Project, Constraint)</code></a> method should be called again.</div>
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
<h3>DiagramValidator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramValidator</span>()</div>
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
<section class="detail" id="init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>init</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ValidationRule.html#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">ValidationRule</a></code></span></div>
<div class="block">This is the first method that is invoked on the implementation of the <code>ValidationRule</code> interface.
 Implementation can initialize internal state if required.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ValidationRule.html#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">init</a></code> in interface <code><a href="ValidationRule.html" title="interface in com.nomagic.magicdraw.validation">ValidationRule</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - a project of the constraint</dd>
<dd><code>constraint</code> - a constraint object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="needsRun(java.beans.PropertyChangeEvent)">
<h3>needsRun</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">needsRun</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> event)</span></div>
<div class="block">Check if validator needs to re-run after given change event occurred.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>event</code> - event occurred.</dd>
<dt>Returns:</dt>
<dd>true need to validate.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>run</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">run</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ValidationRule.html#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">ValidationRule</a></code></span></div>
<div class="block">Run the validation.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ValidationRule.html#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">run</a></code> in interface <code><a href="ValidationRule.html" title="interface in com.nomagic.magicdraw.validation">ValidationRule</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - a project of the constraint</dd>
<dd><code>constraint</code> - a constraint object</dd>
<dt>Returns:</dt>
<dd>set of <a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation"><code>Annotation</code></a> objects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotations(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>getAnnotations</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">getAnnotations</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="block">Return <a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation"><code>Annotation</code></a> object for each <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a> or <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>PresentationElement</code></a> which should be annotated.
 Only the elements represented in diagrams returned by <a href="#getDiagrams()"><code>getDiagrams()</code></a> method should be analyzed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - currently active project</dd>
<dd><code>constraint</code> - a validation rule or a legend item. Use this element to construct <a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation"><code>Annotation</code></a> objects.</dd>
<dt>Returns:</dt>
<dd>annotations targeting elements from the diagrams in scope</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="needsRun()">
<h3>needsRun</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">needsRun</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ValidationRule.html#needsRun()">ValidationRule</a></code></span></div>
<div class="block">Returns whether the validation rule needs to run.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ValidationRule.html#needsRun()">needsRun</a></code> in interface <code><a href="ValidationRule.html" title="interface in com.nomagic.magicdraw.validation">ValidationRule</a></code></dd>
<dt>Returns:</dt>
<dd>true if validation rule needs to run, otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNeedsRun(boolean)">
<h3>setNeedsRun</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setNeedsRun</span><wbr/><span class="parameters">(boolean run)</span></div>
<div class="block">Sets flag if this validator has to be re-run, meaning if <a href="#getAnnotations(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)"><code>getAnnotations(Project, Constraint)</code></a> method should be called again.
 Actual re-run is done by the validation engine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>run</code> - true to mark validator for rerun</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">Unregisters all listeners that were registered and releases other resources.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ValidationRule.html#dispose()">dispose</a></code> in interface <code><a href="ValidationRule.html" title="interface in com.nomagic.magicdraw.validation">ValidationRule</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<div class="block">Get the project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramsStream()">
<h3>getDiagramsStream</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt;</span> <span class="element-name">getDiagramsStream</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Stream of the same diagrams as returned by <a href="#getDiagrams()"><code>getDiagrams()</code></a> method. Convenience method.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagrams()">
<h3>getDiagrams</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt;</span> <span class="element-name">getDiagrams</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of diagrams for which used elements annotations should be calculated in <a href="#getAnnotations(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)"><code>getAnnotations(Project, Constraint)</code></a> method.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="acceptDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">
<h3>acceptDiagram</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">acceptDiagram</span><wbr/><span class="parameters">(<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if the diagram in scope should be returned by <a href="#getDiagrams()"><code>getDiagrams()</code></a> method</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getPresentationElements</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationElements</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to get presentation elements for</dd>
<dt>Returns:</dt>
<dd>presentation elements of the given element from all diagrams that are currently in scope</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>getPresentationElements</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationElements</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt; diagrams)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to get presentation elements for</dd>
<dd><code>diagrams</code> - diagrams of interest</dd>
<dt>Returns:</dt>
<dd>presentation elements of the given element from given diagrams</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isElementInScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isElementInScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isElementInScope</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">If DiagramValidator is to be used in passive validation, then model part to validate can be selected.
 So certain elements used in the diagram should be validated (they are in selected model scope) and certain should be ignored.
 <p>
 Only annotate the element, or it's symbol if the element is in scope.
 Recommendation is to call this method for failing elements only as the last check, since many calls to this method might affect performance in certain scenarios</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element which is used in any of the diagrams in scope</dd>
<dt>Returns:</dt>
<dd>true if the element is in the model scope for the current validation</dd>
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
