# JAVA OPENAPI: ElementValidationRuleImpl (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/validation/ElementValidationRuleImpl.html
- source_path: `com/nomagic/magicdraw/validation/ElementValidationRuleImpl.html`
- source_sha256: `1bbb3415238fbd30f41865bcb3ed7f19ddf1b1221651c4e18864f8ae7790973a`
- captured_utc: `2026-07-14T16:52:26.772076+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.validation](package-summary.html)

## Interface ElementValidationRuleImpl

All Known Implementing Classes:
`[DefaultValidationRuleImpl](DefaultValidationRuleImpl.html)`

@OpenApiAllpublic interfaceElementValidationRuleImpl

Defines an interface for all validation rules which works with validation of model elements.
 
 
**NOTE: Implementations of this interface MUST have a default no-arg constructor.**

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault MethodsDeprecated Methods
Modifier and Type
Method
Description
`default void`
`[dispose](#dispose())()`
This method will be invoked when instance of the `ElementValidationRuleImpl` will become no longer needed.
`default void`
`[init](#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
This is the first method that is invoked on the implementation of
 the `ElementValidationRuleImpl` interface.
`default void`
`[postRun](#postRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
This method is invoked after run method
`default void`
`[preRun](#preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
Deprecated.
replaced by new method [`preRun(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint, java.util.Collection)`](#preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection))
`default void`
`[preRun](#preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection))([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> validatedElements)`
This method is invoked before run method
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Annotation](../annotation/Annotation.html)>`
`[run](#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection))([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)`
Implementation of the method should perform validating of the specified model elements using
 specified constraint.

============ METHOD DETAIL ========== 
Method Details
init
default void init([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
This is the first method that is invoked on the implementation of
 the `ElementValidationRuleImpl` interface. Implementation can initialize
 internal state if required.
Parameters:
`project` - a project of the constraint.
`constraint` - a constraint object.
preRun
default void preRun([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
Deprecated.
replaced by new method [`preRun(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint, java.util.Collection)`](#preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection))
This method is invoked before run method
Parameters:
`project` - a project of the constraint.
`constraint` - a constraint object.
preRun
default void preRun([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> validatedElements)
This method is invoked before run method
Parameters:
`project` - a project of the constraint.
`constraint` - a constraint object.
`validatedElements` - elements to be sent for run
postRun
default void postRun([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
This method is invoked after run method
Parameters:
`project` - a project of the constraint.
`constraint` - a constraint object.
run
[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Annotation](../annotation/Annotation.html)> run([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)
Implementation of the method should perform validating of the specified model elements using
 specified constraint. The method returns a set of [`Annotation`](../annotation/Annotation.html)
 objects that specifies information about invalid elements.
Parameters:
`project` - a project of the constraint.
`constraint` - constraint which defines validation rules.
`elements` - collection of elements that have to be validated.
Returns:
collection of `Annotation` objects that describes violations of the rule.
dispose
default void dispose()
This method will be invoked when instance of the `ElementValidationRuleImpl` will become no longer needed.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.validation</a></div>
<h1 class="title" title="Interface ElementValidationRuleImpl">Interface ElementValidationRuleImpl</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="DefaultValidationRuleImpl.html" title="class in com.nomagic.magicdraw.validation">DefaultValidationRuleImpl</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ElementValidationRuleImpl</span></div>
<div class="block">Defines an interface for all validation rules which works with validation of model elements.
 <br/><br/><b>NOTE: Implementations of this interface MUST have a default no-arg constructor.</b></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">This method will be invoked when instance of the <code>ElementValidationRuleImpl</code> will become no longer needed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">init</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">This is the first method that is invoked on the implementation of
 the <code>ElementValidationRuleImpl</code> interface.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#postRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">postRun</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">This method is invoked after run method</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code><a class="member-name-link" href="#preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">preRun</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">replaced by new method <a href="#preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection)"><code>preRun(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint, java.util.Collection)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection)">preRun</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; validatedElements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">This method is invoked before run method</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection)">run</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Implementation of the method should perform validating of the specified model elements using
 specified constraint.</div>
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
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="block">This is the first method that is invoked on the implementation of
 the <code>ElementValidationRuleImpl</code> interface. Implementation can initialize
 internal state if required.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project of the constraint.</dd>
<dd><code>constraint</code> - a constraint object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>preRun</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">preRun</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">replaced by new method <a href="#preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection)"><code>preRun(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint, java.util.Collection)</code></a></div>
</div>
<div class="block">This method is invoked before run method</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project of the constraint.</dd>
<dd><code>constraint</code> - a constraint object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection)">
<h3>preRun</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">preRun</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; validatedElements)</span></div>
<div class="block">This method is invoked before run method</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project of the constraint.</dd>
<dd><code>constraint</code> - a constraint object.</dd>
<dd><code>validatedElements</code> - elements to be sent for run</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="postRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>postRun</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">postRun</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="block">This method is invoked after run method</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project of the constraint.</dd>
<dd><code>constraint</code> - a constraint object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection)">
<h3>run</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">run</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block">Implementation of the method should perform validating of the specified model elements using
 specified constraint. The method returns a set of <a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation"><code>Annotation</code></a>
 objects that specifies information about invalid elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project of the constraint.</dd>
<dd><code>constraint</code> - constraint which defines validation rules.</dd>
<dd><code>elements</code> - collection of elements that have to be validated.</dd>
<dt>Returns:</dt>
<dd>collection of <code>Annotation</code> objects that describes violations of the rule.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">This method will be invoked when instance of the <code>ElementValidationRuleImpl</code> will become no longer needed.</div>
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
