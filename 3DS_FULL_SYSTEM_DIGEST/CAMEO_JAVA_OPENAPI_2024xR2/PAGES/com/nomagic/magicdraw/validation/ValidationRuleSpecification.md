# JAVA OPENAPI: ValidationRuleSpecification (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/validation/ValidationRuleSpecification.html
- source_path: `com/nomagic/magicdraw/validation/ValidationRuleSpecification.html`
- source_sha256: `be533b11835ec9e65137c004057aa53e7f8f13cbd858baa716d8e33333579f97`
- captured_utc: `2026-07-14T16:56:01.443525+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.validation](package-summary.html)

## Interface ValidationRuleSpecification

@OpenApiAllpublic interfaceValidationRuleSpecification

`ValidationRuleSpecification` is a wrapper for a constraint with applied validationRule stereotype.
 It provides convenience methods to access tag values.

Version:
1.0

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[ElementExpression](../expressions/ElementExpression.html)`
`[getParentObjectExpression](#getParentObjectExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](../../uml2/ext/magicdraw/classes/mdkernel/Class.html) context)`
Returns parent object expression.
`[ValidationRuleSpecification](ValidationRuleSpecification.html)`
`[getParentRule](#getParentRule())()`
Returns parent rule.
`[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)`
`[getParentValidationRuleConstraint](#getParentValidationRuleConstraint())()`
Returns parent validation rule constraint.
`[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)`
`[getStereotypedConstraint](#getStereotypedConstraint())()`
Returns stereotyped constraint.

============ METHOD DETAIL ========== 
Method Details
getParentRule
@CheckForNull[ValidationRuleSpecification](ValidationRuleSpecification.html) getParentRule()
Returns parent rule.
Returns:
parent rule.
getParentValidationRuleConstraint
@CheckForNull[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) getParentValidationRuleConstraint()
Returns parent validation rule constraint.
Returns:
parent validation rule.
getParentObjectExpression
@CheckForNull[ElementExpression](../expressions/ElementExpression.html) getParentObjectExpression([Class](../../uml2/ext/magicdraw/classes/mdkernel/Class.html) context)
Returns parent object expression.
Parameters:
`context` - context of the expression.
Returns:
parent object expression.
getStereotypedConstraint
[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) getStereotypedConstraint()
Returns stereotyped constraint.
Returns:
stereotyped constraint.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.validation</a></div>
<h1 class="title" title="Interface ValidationRuleSpecification">Interface ValidationRuleSpecification</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ValidationRuleSpecification</span></div>
<div class="block"><code>ValidationRuleSpecification</code> is a wrapper for a constraint with applied validationRule stereotype.
 It provides convenience methods to access tag values.</div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../expressions/ElementExpression.html" title="interface in com.nomagic.magicdraw.expressions">ElementExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParentObjectExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">getParentObjectExpression</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns parent object expression.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ValidationRuleSpecification.html" title="interface in com.nomagic.magicdraw.validation">ValidationRuleSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParentRule()">getParentRule</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns parent rule.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParentValidationRuleConstraint()">getParentValidationRuleConstraint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns parent validation rule constraint.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStereotypedConstraint()">getStereotypedConstraint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns stereotyped constraint.</div>
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
<section class="detail" id="getParentRule()">
<h3>getParentRule</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ValidationRuleSpecification.html" title="interface in com.nomagic.magicdraw.validation">ValidationRuleSpecification</a></span> <span class="element-name">getParentRule</span>()</div>
<div class="block">Returns parent rule.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent rule.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentValidationRuleConstraint()">
<h3>getParentValidationRuleConstraint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">getParentValidationRuleConstraint</span>()</div>
<div class="block">Returns parent validation rule constraint.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent validation rule.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentObjectExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>getParentObjectExpression</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../expressions/ElementExpression.html" title="interface in com.nomagic.magicdraw.expressions">ElementExpression</a></span> <span class="element-name">getParentObjectExpression</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> context)</span></div>
<div class="block">Returns parent object expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - context of the expression.</dd>
<dt>Returns:</dt>
<dd>parent object expression.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypedConstraint()">
<h3>getStereotypedConstraint</h3>
<div class="member-signature"><span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">getStereotypedConstraint</span>()</div>
<div class="block">Returns stereotyped constraint.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotyped constraint.</dd>
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
