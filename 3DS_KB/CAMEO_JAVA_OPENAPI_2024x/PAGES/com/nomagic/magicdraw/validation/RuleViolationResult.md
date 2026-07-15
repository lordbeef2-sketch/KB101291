# JAVA OPENAPI: RuleViolationResult (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/validation/RuleViolationResult.html
- source_path: `com/nomagic/magicdraw/validation/RuleViolationResult.html`
- source_sha256: `6b2f3af60eaaa74cb6dd49fe6cca17dbf2365dc2b1badcc0559da454de7c1f24`
- captured_utc: `2026-07-14T16:52:26.809076+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.validation](package-summary.html)

## Class RuleViolationResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.validation.RuleViolationResult

@OpenApiAllpublic classRuleViolationResult
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Class for rule violation result storage.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[RuleViolationResult](#%3Cinit%3E(com.nomagic.magicdraw.annotation.Annotation,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Annotation](../annotation/Annotation.html) annotation,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) rule)`
Constructor.
`[RuleViolationResult](#%3Cinit%3E(com.nomagic.magicdraw.annotation.Annotation,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,boolean))([Annotation](../annotation/Annotation.html) annotation,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) rule,
 boolean systemRule)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`

`[Annotation](../annotation/Annotation.html)`
`[getAnnotation](#getAnnotation())()`
Returns [`Annotation`](../annotation/Annotation.html) of violation.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](../annotation/Annotation.html)>`
`[getAnnotations](#getAnnotations(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) results)`
Collects annotations from a list of RuleViolationResult list.
`[Project](../core/Project.html)`
`[getConstrainedProject](#getConstrainedProject())()`
Returns project of the violated constraint
`[BaseElement](../uml/BaseElement.html)`
`[getElement](#getElement())()`
Returns target [`Element`](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getErrorMessage](#getErrorMessage())()`
Violation message or empty String.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getParentObject](#getParentObject())()`
Returns parent object that should be used for grouping the results.
`[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)`
`[getParentRule](#getParentRule())()`
Returns parent rule if such is specified.
`[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)`
`[getRule](#getRule())()`
Returns violated rule.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getTargetObject](#getTargetObject())()`
Returns target object of the rule violation result.
`int`
`[hashCode](#hashCode())()`

`boolean`
`[isIgnored](#isIgnored())()`
Checks if this violation result is ignored by user.
`boolean`
`[isSystemValidationResult](#isSystemValidationResult())()`
If true validation result came from system rule, else false.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
RuleViolationResult
public RuleViolationResult([Annotation](../annotation/Annotation.html) annotation,
 @CheckForNull
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) rule)
Constructor.
Parameters:
`annotation` - of this violation
`rule` - violated constraint
RuleViolationResult
public RuleViolationResult([Annotation](../annotation/Annotation.html) annotation,
 @CheckForNull
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) rule,
 boolean systemRule)
Constructor.
Parameters:
`annotation` - of this violation
`rule` - violated constraint
`systemRule` - is system validation rule
 ============ METHOD DETAIL ========== 
Method Details
getAnnotation
public [Annotation](../annotation/Annotation.html) getAnnotation()
Returns [`Annotation`](../annotation/Annotation.html) of violation.
Returns:
annotation of violation.
getElement
@CheckForNullpublic [BaseElement](../uml/BaseElement.html) getElement()
Returns target [`Element`](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)
Returns:
target element.
getTargetObject
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getTargetObject()
Returns target object of the rule violation result.
Returns:
target object.
getErrorMessage
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getErrorMessage()
Violation message or empty String.
Returns:
violation message or empty String.
getRule
@CheckForNullpublic [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) getRule()
Returns violated rule.
Returns:
violated rule.
isIgnored
public boolean isIgnored()
Checks if this violation result is ignored by user. User can ignore pair of violation - target element & constraint.
Returns:
ignored flag.
getConstrainedProject
@CheckForNullpublic [Project](../core/Project.html) getConstrainedProject()
Returns project of the violated constraint
getParentRule
@CheckForNullpublic [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) getParentRule()
Returns parent rule if such is specified.
Returns:
parent rule or null.
getParentObject
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getParentObject()
Returns parent object that should be used for grouping the results.
Returns:
parent object.
getAnnotations
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](../annotation/Annotation.html)> getAnnotations([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) results)
Collects annotations from a list of RuleViolationResult list.
Parameters:
`results` - list of RuleViolationResult objects
Returns:
list of Annotation objects
isSystemValidationResult
public boolean isSystemValidationResult()
If true validation result came from system rule, else false.
Returns:
true if validation result came from system rule, else false.
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.validation</a></div>
<h1 class="title" title="Class RuleViolationResult">Class RuleViolationResult</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.validation.RuleViolationResult</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">RuleViolationResult</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Class for rule violation result storage.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.annotation.Annotation,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">RuleViolationResult</a><wbr/>(<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> rule)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.annotation.Annotation,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,boolean)">RuleViolationResult</a><wbr/>(<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> rule,
 boolean systemRule)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotation()">getAnnotation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns <a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation"><code>Annotation</code></a> of violation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotations(java.util.Collection)">getAnnotations</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> results)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects annotations from a list of RuleViolationResult list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConstrainedProject()">getConstrainedProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns project of the violated constraint</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns target <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getErrorMessage()">getErrorMessage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Violation message or empty String.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentObject()">getParentObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns parent object that should be used for grouping the results.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentRule()">getParentRule</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns parent rule if such is specified.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRule()">getRule</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns violated rule.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetObject()">getTargetObject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns target object of the rule violation result.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isIgnored()">isIgnored</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if this violation result is ignored by user.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSystemValidationResult()">isSystemValidationResult</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If true validation result came from system rule, else false.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.annotation.Annotation,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>RuleViolationResult</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RuleViolationResult</span><wbr/><span class="parameters">(<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> rule)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotation</code> - of this violation</dd>
<dd><code>rule</code> - violated constraint</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.annotation.Annotation,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,boolean)">
<h3>RuleViolationResult</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RuleViolationResult</span><wbr/><span class="parameters">(<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> rule,
 boolean systemRule)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotation</code> - of this violation</dd>
<dd><code>rule</code> - violated constraint</dd>
<dd><code>systemRule</code> - is system validation rule</dd>
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
<section class="detail" id="getAnnotation()">
<h3>getAnnotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a></span> <span class="element-name">getAnnotation</span>()</div>
<div class="block">Returns <a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation"><code>Annotation</code></a> of violation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>annotation of violation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getElement</span>()</div>
<div class="block">Returns target <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>target element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetObject()">
<h3>getTargetObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getTargetObject</span>()</div>
<div class="block">Returns target object of the rule violation result.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>target object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getErrorMessage()">
<h3>getErrorMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getErrorMessage</span>()</div>
<div class="block">Violation message or empty String.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>violation message or empty String.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRule()">
<h3>getRule</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">getRule</span>()</div>
<div class="block">Returns violated rule.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>violated rule.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isIgnored()">
<h3>isIgnored</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isIgnored</span>()</div>
<div class="block">Checks if this violation result is ignored by user. User can ignore pair of violation - target element &amp; constraint.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ignored flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConstrainedProject()">
<h3>getConstrainedProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getConstrainedProject</span>()</div>
<div class="block">Returns project of the violated constraint</div>
</section>
</li>
<li>
<section class="detail" id="getParentRule()">
<h3>getParentRule</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">getParentRule</span>()</div>
<div class="block">Returns parent rule if such is specified.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent rule or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentObject()">
<h3>getParentObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getParentObject</span>()</div>
<div class="block">Returns parent object that should be used for grouping the results.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotations(java.util.Collection)">
<h3>getAnnotations</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">getAnnotations</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> results)</span></div>
<div class="block">Collects annotations from a list of RuleViolationResult list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>results</code> - list of RuleViolationResult objects</dd>
<dt>Returns:</dt>
<dd>list of Annotation objects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSystemValidationResult()">
<h3>isSystemValidationResult</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSystemValidationResult</span>()</div>
<div class="block">If true validation result came from system rule, else false.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if validation result came from system rule, else false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
