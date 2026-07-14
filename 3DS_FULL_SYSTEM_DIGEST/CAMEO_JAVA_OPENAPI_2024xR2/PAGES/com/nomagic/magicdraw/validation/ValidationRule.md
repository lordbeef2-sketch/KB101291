# JAVA OPENAPI: ValidationRule (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/validation/ValidationRule.html
- source_path: `com/nomagic/magicdraw/validation/ValidationRule.html`
- source_sha256: `dfc36626ba7c03eaec4813e30454f84b462fdfc3166e7148b37a322161cb2f3e`
- captured_utc: `2026-07-14T16:56:01.451525+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.validation](package-summary.html)

## Interface ValidationRule

All Known Implementing Classes:
`[DiagramValidator](DiagramValidator.html)`, `[OpenedDiagramValidator](OpenedDiagramValidator.html)`

@OpenApiAllpublic interfaceValidationRule

Defines interface for all validation rules. This interface should be implemented by classes that: 

Want to control whether validation should occur.
Want to control what should be validated. 

 The implementing class must have a public no-arg constructor. If implementing class is designed for validating model
 elements then implementer of the class must honor project properties:
 Validation scope
Exclude elements from read-only modules
 In other words implementer of the class is responsible for correctly implement validating of elements from the
 specified validation scope and validating or not validating of elements from read-only modules. Also it
 is responsibility of implementer to detect changes of these properties and providing appropriate validation results.
 If you need to implement model element validation rule it is more convenient to do by implementing
 [`ElementValidationRuleImpl`](ElementValidationRuleImpl.html) interface.

See Also:
[`ElementValidationRuleImpl`](ElementValidationRuleImpl.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[dispose](#dispose())()`
This method will be invoked when instance of the `ValidationRule` will become no longer needed.
`void`
`[init](#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
This is the first method that is invoked on the implementation of the `ValidationRule` interface.
`boolean`
`[needsRun](#needsRun())()`
Returns whether the validation rule needs to run.
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Annotation](../annotation/Annotation.html)>`
`[run](#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
Run the validation.

============ METHOD DETAIL ========== 
Method Details
init
void init([Project](../core/Project.html) project,
 @CheckForNull
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
This is the first method that is invoked on the implementation of the `ValidationRule` interface.
 Implementation can initialize internal state if required.
Parameters:
`project` - a project of the constraint
`constraint` - a constraint object
needsRun
boolean needsRun()
Returns whether the validation rule needs to run.
Returns:
true if validation rule needs to run, otherwise false
run
[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Annotation](../annotation/Annotation.html)> run([Project](../core/Project.html) project,
 @CheckForNull
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
Run the validation.
Parameters:
`project` - a project of the constraint
`constraint` - a constraint object
Returns:
set of [`Annotation`](../annotation/Annotation.html) objects
dispose
void dispose()
This method will be invoked when instance of the `ValidationRule` will become no longer needed.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.validation</a></div>
<h1 class="title" title="Interface ValidationRule">Interface ValidationRule</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="DiagramValidator.html" title="class in com.nomagic.magicdraw.validation">DiagramValidator</a></code>, <code><a href="OpenedDiagramValidator.html" title="class in com.nomagic.magicdraw.validation">OpenedDiagramValidator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ValidationRule</span></div>
<div class="block">Defines interface for all validation rules. This interface should be implemented by classes that:<br/>
<ol>
<li>Want to control whether validation should occur.</li>
<li>Want to control what should be validated.</li>
</ol><br/>
 The implementing class must have a public no-arg constructor. If implementing class is designed for validating model
 elements then implementer of the class must honor project properties:
 <ol>
<li>Validation scope
<li>Exclude elements from read-only modules</li>
</li></ol>
 In other words implementer of the class is responsible for correctly implement validating of elements from the
 specified validation scope and validating or not validating of elements from read-only modules. Also it
 is responsibility of implementer to detect changes of these properties and providing appropriate validation results.
 If you need to implement model element validation rule it is more convenient to do by implementing
 <a href="ElementValidationRuleImpl.html" title="interface in com.nomagic.magicdraw.validation"><code>ElementValidationRuleImpl</code></a> interface.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="ElementValidationRuleImpl.html" title="interface in com.nomagic.magicdraw.validation"><code>ElementValidationRuleImpl</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method will be invoked when instance of the <code>ValidationRule</code> will become no longer needed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">init</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This is the first method that is invoked on the implementation of the <code>ValidationRule</code> interface.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#needsRun()">needsRun</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns whether the validation rule needs to run.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">run</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Run the validation.</div>
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
<section class="detail" id="init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>init</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="block">This is the first method that is invoked on the implementation of the <code>ValidationRule</code> interface.
 Implementation can initialize internal state if required.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project of the constraint</dd>
<dd><code>constraint</code> - a constraint object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="needsRun()">
<h3>needsRun</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">needsRun</span>()</div>
<div class="block">Returns whether the validation rule needs to run.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if validation rule needs to run, otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>run</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">run</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="block">Run the validation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project of the constraint</dd>
<dd><code>constraint</code> - a constraint object</dd>
<dt>Returns:</dt>
<dd>set of <a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation"><code>Annotation</code></a> objects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">This method will be invoked when instance of the <code>ValidationRule</code> will become no longer needed.</div>
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
