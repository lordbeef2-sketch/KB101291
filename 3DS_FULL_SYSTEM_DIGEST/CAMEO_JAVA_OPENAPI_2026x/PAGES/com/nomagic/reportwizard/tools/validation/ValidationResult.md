# JAVA OPENAPI: ValidationResult (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/reportwizard/tools/validation/ValidationResult.html
- source_path: `com/nomagic/reportwizard/tools/validation/ValidationResult.html`
- source_sha256: `db573c5c8caa780140761e036cff422734a4dd7e84d4761d857ae842d87b0453`
- captured_utc: `2026-07-14T16:58:40.781322+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.validation](package-summary.html)

## Class ValidationResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.reportwizard.tools.validation.ValidationResult

@OpenApiAllpublic classValidationResult
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Contains data for model validation result.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ValidationResult](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getAbbreviation](#getAbbreviation())()`
Gets abbreviation.
`[Annotation](../../../magicdraw/annotation/Annotation.html)`
`[getAnnotation](#getAnnotation())()`
Returns [`Annotation`](../../../magicdraw/annotation/Annotation.html) of violation.
`[Project](../../../magicdraw/core/Project.html)`
`[getConstrainedProject](#getConstrainedProject())()`
Returns project of the violated constraint
`[BaseElement](../../../magicdraw/uml/BaseElement.html)`
`[getElement](#getElement())()`
Gets element.
`boolean`
`[getIsIgnored](#getIsIgnored())()`
Checks if this violation result is ignored by user.
`boolean`
`[getIsSystemValidationResult](#getIsSystemValidationResult())()`
If true validation result came from system rule, else false.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getMessage](#getMessage())()`
Gets message.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getParentObject](#getParentObject())()`
Returns parent object that should be used for grouping the results.
`[Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)`
`[getParentRule](#getParentRule())()`
Returns parent rule if such is specified.
`[Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)`
`[getRule](#getRule())()`
Returns violated rule.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getSeverity](#getSeverity())()`
Gets severity.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getTargetObject](#getTargetObject())()`
Returns target object of the rule violation result.
`boolean`
`[isIgnored](#isIgnored())()`
Checks if this violation result is ignored by user.
`boolean`
`[isSystemValidationResult](#isSystemValidationResult())()`
If true validation result came from system rule, else false.
`void`
`[setAbbreviation](#setAbbreviation(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) abbreviation)`
Sets abbreviation.
`void`
`[setAnnotation](#setAnnotation(com.nomagic.magicdraw.annotation.Annotation))([Annotation](../../../magicdraw/annotation/Annotation.html) annotation)`
Set [`Annotation`](../../../magicdraw/annotation/Annotation.html) of violation.
`void`
`[setConstrainedProject](#setConstrainedProject(com.nomagic.magicdraw.core.Project))([Project](../../../magicdraw/core/Project.html) constrainedProject)`
Set project of the violated constraint
`void`
`[setElement](#setElement(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../magicdraw/uml/BaseElement.html) baseElement)`
Sets element.
`void`
`[setIgnored](#setIgnored(boolean))(boolean isIgnored)`
Set if this violation result is ignored by user.
`void`
`[setMessage](#setMessage(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)`
Sets message.
`void`
`[setParentObject](#setParentObject(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) parentObject)`
set parent object that should be used for grouping the results.
`void`
`[setParentRule](#setParentRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) parentRule)`
Set parent rule if such is specified.
`void`
`[setRule](#setRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) rule)`
Set violated rule.
`void`
`[setSeverity](#setSeverity(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) severity)`
Sets severity.
`void`
`[setSystemValidationResult](#setSystemValidationResult(boolean))(boolean isSystemValidationResult)`
Set If true validation result came from system rule.
`void`
`[setTargetObject](#setTargetObject(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) targetObject)`
Set target object of the rule violation result.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ValidationResult
public ValidationResult()
 ============ METHOD DETAIL ========== 
Method Details
getElement
public [BaseElement](../../../magicdraw/uml/BaseElement.html) getElement()
Gets element.
Returns:
the element
setElement
public void setElement([BaseElement](../../../magicdraw/uml/BaseElement.html) baseElement)
Sets element.
Parameters:
`baseElement` - the element to set
getSeverity
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getSeverity()
Gets severity.
Returns:
the severity
setSeverity
public void setSeverity([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) severity)
Sets severity.
Parameters:
`severity` - the severity to set
getAbbreviation
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getAbbreviation()
Gets abbreviation.
Returns:
the abbreviation
setAbbreviation
public void setAbbreviation([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) abbreviation)
Sets abbreviation.
Parameters:
`abbreviation` - the abbreviation to set
getMessage
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getMessage()
Gets message.
Returns:
the message
setMessage
public void setMessage([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)
Sets message.
Parameters:
`message` - the message to set
getAnnotation
public [Annotation](../../../magicdraw/annotation/Annotation.html) getAnnotation()
Returns [`Annotation`](../../../magicdraw/annotation/Annotation.html) of violation.
Returns:
annotation of violation.
setAnnotation
public void setAnnotation([Annotation](../../../magicdraw/annotation/Annotation.html) annotation)
Set [`Annotation`](../../../magicdraw/annotation/Annotation.html) of violation.
Parameters:
`an` - annotation of violation.
getConstrainedProject
public [Project](../../../magicdraw/core/Project.html) getConstrainedProject()
Returns project of the violated constraint
setConstrainedProject
public void setConstrainedProject([Project](../../../magicdraw/core/Project.html) constrainedProject)
Set project of the violated constraint
Parameters:
`constrainedProject` - project of the violated constraint
getParentObject
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getParentObject()
Returns parent object that should be used for grouping the results.
Returns:
parent object.
setParentObject
public void setParentObject([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) parentObject)
set parent object that should be used for grouping the results.
Parameters:
`parentObject` - parent object that should be used for grouping the results
getParentRule
public [Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) getParentRule()
Returns parent rule if such is specified.
Returns:
parent rule or null.
setParentRule
public void setParentRule([Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) parentRule)
Set parent rule if such is specified.
Parameters:
`parentRule` - parent rule if such is specified
getRule
public [Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) getRule()
Returns violated rule.
Returns:
violated rule.
setRule
public void setRule([Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) rule)
Set violated rule.
Parameters:
`rule` - violated rule
getTargetObject
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getTargetObject()
Returns target object of the rule violation result.
Returns:
target object.
setTargetObject
public void setTargetObject([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) targetObject)
Set target object of the rule violation result.
Parameters:
`targetObject` - target object of the rule violation result
isIgnored
public boolean isIgnored()
Checks if this violation result is ignored by user. User can ignore pair of violation - target element invalid input: '&' constraint.
Returns:
ignored flag.
getIsIgnored
public boolean getIsIgnored()
Checks if this violation result is ignored by user. User can ignore pair of violation - target element invalid input: '&' constraint.
Returns:
ignored flag.
setIgnored
public void setIgnored(boolean isIgnored)
Set if this violation result is ignored by user.
Parameters:
`isIgnored` - true if this violation result is ignored by user, else false
getIsSystemValidationResult
public boolean getIsSystemValidationResult()
If true validation result came from system rule, else false.
Returns:
true if validation result came from system rule, else false.
isSystemValidationResult
public boolean isSystemValidationResult()
If true validation result came from system rule, else false.
Returns:
true if validation result came from system rule, else false.
setSystemValidationResult
public void setSystemValidationResult(boolean isSystemValidationResult)
Set If true validation result came from system rule.
Parameters:
`isSystemValidationResult` - true if validation result came from system rule, else false.
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.validation</a></div>
<h1 class="title" title="Class ValidationResult">Class ValidationResult</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.reportwizard.tools.validation.ValidationResult</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ValidationResult</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Contains data for model validation result.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ValidationResult</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbbreviation()">getAbbreviation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets abbreviation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../magicdraw/annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotation()">getAnnotation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns <a href="../../../magicdraw/annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation"><code>Annotation</code></a> of violation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConstrainedProject()">getConstrainedProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns project of the violated constraint</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIsIgnored()">getIsIgnored</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if this violation result is ignored by user.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIsSystemValidationResult()">getIsSystemValidationResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If true validation result came from system rule, else false.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessage()">getMessage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentObject()">getParentObject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns parent object that should be used for grouping the results.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentRule()">getParentRule</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns parent rule if such is specified.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRule()">getRule</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns violated rule.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeverity()">getSeverity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets severity.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetObject()">getTargetObject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns target object of the rule violation result.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isIgnored()">isIgnored</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if this violation result is ignored by user.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSystemValidationResult()">isSystemValidationResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If true validation result came from system rule, else false.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAbbreviation(java.lang.String)">setAbbreviation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> abbreviation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets abbreviation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAnnotation(com.nomagic.magicdraw.annotation.Annotation)">setAnnotation</a><wbr/>(<a href="../../../magicdraw/annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set <a href="../../../magicdraw/annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation"><code>Annotation</code></a> of violation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setConstrainedProject(com.nomagic.magicdraw.core.Project)">setConstrainedProject</a><wbr/>(<a href="../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> constrainedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set project of the violated constraint</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setElement(com.nomagic.magicdraw.uml.BaseElement)">setElement</a><wbr/>(<a href="../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIgnored(boolean)">setIgnored</a><wbr/>(boolean isIgnored)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if this violation result is ignored by user.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMessage(java.lang.String)">setMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParentObject(java.lang.Object)">setParentObject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> parentObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">set parent object that should be used for grouping the results.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParentRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">setParentRule</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> parentRule)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set parent rule if such is specified.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">setRule</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> rule)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set violated rule.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSeverity(java.lang.String)">setSeverity</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> severity)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets severity.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSystemValidationResult(boolean)">setSystemValidationResult</a><wbr/>(boolean isSystemValidationResult)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set If true validation result came from system rule.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTargetObject(java.lang.Object)">setTargetObject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> targetObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set target object of the rule violation result.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>ValidationResult</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationResult</span>()</div>
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
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getElement</span>()</div>
<div class="block">Gets element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setElement(com.nomagic.magicdraw.uml.BaseElement)">
<h3>setElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setElement</span><wbr/><span class="parameters">(<a href="../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</span></div>
<div class="block">Sets element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>baseElement</code> - the element to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSeverity()">
<h3>getSeverity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSeverity</span>()</div>
<div class="block">Gets severity.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the severity</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSeverity(java.lang.String)">
<h3>setSeverity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSeverity</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> severity)</span></div>
<div class="block">Sets severity.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>severity</code> - the severity to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbbreviation()">
<h3>getAbbreviation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAbbreviation</span>()</div>
<div class="block">Gets abbreviation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the abbreviation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAbbreviation(java.lang.String)">
<h3>setAbbreviation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAbbreviation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> abbreviation)</span></div>
<div class="block">Sets abbreviation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>abbreviation</code> - the abbreviation to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMessage()">
<h3>getMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMessage</span>()</div>
<div class="block">Gets message.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMessage(java.lang.String)">
<h3>setMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Sets message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotation()">
<h3>getAnnotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../magicdraw/annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a></span> <span class="element-name">getAnnotation</span>()</div>
<div class="block">Returns <a href="../../../magicdraw/annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation"><code>Annotation</code></a> of violation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>annotation of violation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAnnotation(com.nomagic.magicdraw.annotation.Annotation)">
<h3>setAnnotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAnnotation</span><wbr/><span class="parameters">(<a href="../../../magicdraw/annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation)</span></div>
<div class="block">Set <a href="../../../magicdraw/annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation"><code>Annotation</code></a> of violation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>an</code> - annotation of violation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConstrainedProject()">
<h3>getConstrainedProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getConstrainedProject</span>()</div>
<div class="block">Returns project of the violated constraint</div>
</section>
</li>
<li>
<section class="detail" id="setConstrainedProject(com.nomagic.magicdraw.core.Project)">
<h3>setConstrainedProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setConstrainedProject</span><wbr/><span class="parameters">(<a href="../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> constrainedProject)</span></div>
<div class="block">Set project of the violated constraint</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constrainedProject</code> - project of the violated constraint</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentObject()">
<h3>getParentObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getParentObject</span>()</div>
<div class="block">Returns parent object that should be used for grouping the results.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParentObject(java.lang.Object)">
<h3>setParentObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParentObject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> parentObject)</span></div>
<div class="block">set parent object that should be used for grouping the results.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parentObject</code> - parent object that should be used for grouping the results</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentRule()">
<h3>getParentRule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">getParentRule</span>()</div>
<div class="block">Returns parent rule if such is specified.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent rule or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParentRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>setParentRule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParentRule</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> parentRule)</span></div>
<div class="block">Set parent rule if such is specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parentRule</code> - parent rule if such is specified</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRule()">
<h3>getRule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">getRule</span>()</div>
<div class="block">Returns violated rule.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>violated rule.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>setRule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRule</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> rule)</span></div>
<div class="block">Set violated rule.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rule</code> - violated rule</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetObject()">
<h3>getTargetObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getTargetObject</span>()</div>
<div class="block">Returns target object of the rule violation result.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>target object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTargetObject(java.lang.Object)">
<h3>setTargetObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTargetObject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> targetObject)</span></div>
<div class="block">Set target object of the rule violation result.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetObject</code> - target object of the rule violation result</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isIgnored()">
<h3>isIgnored</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isIgnored</span>()</div>
<div class="block">Checks if this violation result is ignored by user. User can ignore pair of violation - target element <span class="invalid-tag">invalid input: '&amp;'</span> constraint.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ignored flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIsIgnored()">
<h3>getIsIgnored</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getIsIgnored</span>()</div>
<div class="block">Checks if this violation result is ignored by user. User can ignore pair of violation - target element <span class="invalid-tag">invalid input: '&amp;'</span> constraint.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ignored flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIgnored(boolean)">
<h3>setIgnored</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIgnored</span><wbr/><span class="parameters">(boolean isIgnored)</span></div>
<div class="block">Set if this violation result is ignored by user.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>isIgnored</code> - true if this violation result is ignored by user, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIsSystemValidationResult()">
<h3>getIsSystemValidationResult</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getIsSystemValidationResult</span>()</div>
<div class="block">If true validation result came from system rule, else false.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if validation result came from system rule, else false.</dd>
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
<section class="detail" id="setSystemValidationResult(boolean)">
<h3>setSystemValidationResult</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSystemValidationResult</span><wbr/><span class="parameters">(boolean isSystemValidationResult)</span></div>
<div class="block">Set If true validation result came from system rule.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>isSystemValidationResult</code> - true if validation result came from system rule, else false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
