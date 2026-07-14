# JAVA OPENAPI: ValidationHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/validation/ValidationHelper.html
- source_path: `com/nomagic/magicdraw/validation/ValidationHelper.html`
- source_sha256: `7c5edabefba278c5802eb817fd6c57caae1267cc567ae01ce9515d01eeab2d49`
- captured_utc: `2026-07-14T16:56:08.308602+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.validation](package-summary.html)

## Class ValidationHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.validation.ValidationHelper

@OpenApiAllpublic classValidationHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Utility class for working with validation.
 It is able to invoke validation with given [`ValidationRunData`](ValidationRunData.html) or for specific [`Element`](../../uml2/ext/magicdraw/classes/mdkernel/Element.html).
 It is also able to open validation window and display validation results in it.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ValidationHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[openValidationWindow](#openValidationWindow(com.nomagic.magicdraw.validation.ValidationRunData,java.lang.String,java.util.Collection))([ValidationRunData](ValidationRunData.html) validationRunData,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) windowID,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[RuleViolationResult](RuleViolationResult.html)> results)`
Opens validation window and displays [`RuleViolationResult`](RuleViolationResult.html) in it.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[RuleViolationResult](RuleViolationResult.html)>`
`[validate](#validate(com.nomagic.magicdraw.validation.ValidationRunData,java.lang.String,com.nomagic.task.ProgressStatus))([ValidationRunData](ValidationRunData.html) validationRunData,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) validationTaskName,
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus)`
Runs validation for given [`ValidationRunData`](ValidationRunData.html)
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[RuleViolationResult](RuleViolationResult.html)>`
`[validateElement](#validateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) elementForValidation,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> rules,
 boolean excludeReadOnly)`
Validates given element with given list of validation rules.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[RuleViolationResult](RuleViolationResult.html)>`
`[validateElement](#validateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List,boolean,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) elementForValidation,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> rules,
 boolean excludeReadOnly,
 boolean recursive)`
Validates given element with given list of validation rules.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ValidationHelper
public ValidationHelper()
 ============ METHOD DETAIL ========== 
Method Details
validate
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[RuleViolationResult](RuleViolationResult.html)> validate([ValidationRunData](ValidationRunData.html) validationRunData,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) validationTaskName,
 @CheckForNull
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus)
Runs validation for given [`ValidationRunData`](ValidationRunData.html)
Parameters:
`validationRunData` - instance of [`ValidationRunData`](ValidationRunData.html)
`validationTaskName` - which is visible when running validation. If Passed null, it will show default value "Validating"
`progressStatus` - for validation, or null if to run validation with owe progress
Returns:
collection of validation results
validateElement
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[RuleViolationResult](RuleViolationResult.html)> validateElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) elementForValidation,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> rules,
 boolean excludeReadOnly)
Validates given element with given list of validation rules.
Parameters:
`elementForValidation` - element which should be validated
`rules` - list of validation rules
`excludeReadOnly` - exclude read only elements or not
Returns:
list of violation results
validateElement
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[RuleViolationResult](RuleViolationResult.html)> validateElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) elementForValidation,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> rules,
 boolean excludeReadOnly,
 boolean recursive)
Validates given element with given list of validation rules.
Parameters:
`elementForValidation` - element which should be validated.
`rules` - list of validation rules.
`excludeReadOnly` - exclude read only elements or not
`recursive` - validate owned elements of given element recursively
Returns:
list of violation results
openValidationWindow
public static void openValidationWindow([ValidationRunData](ValidationRunData.html) validationRunData,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) windowID,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[RuleViolationResult](RuleViolationResult.html)> results)
Opens validation window and displays [`RuleViolationResult`](RuleViolationResult.html) in it.
Parameters:
`validationRunData` - instance of [`ValidationRunData`](ValidationRunData.html)
`windowID` - id which will be set to validation window.
`results` - collection of [`RuleViolationResult`](RuleViolationResult.html)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.validation</a></div>
<h1 class="title" title="Class ValidationHelper">Class ValidationHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.validation.ValidationHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ValidationHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class for working with validation.
 It is able to invoke validation with given <a href="ValidationRunData.html" title="class in com.nomagic.magicdraw.validation"><code>ValidationRunData</code></a> or for specific <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a>.
 It is also able to open validation window and display validation results in it.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ValidationHelper</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#openValidationWindow(com.nomagic.magicdraw.validation.ValidationRunData,java.lang.String,java.util.Collection)">openValidationWindow</a><wbr/>(<a href="ValidationRunData.html" title="class in com.nomagic.magicdraw.validation">ValidationRunData</a> validationRunData,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> windowID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation">RuleViolationResult</a>&gt; results)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Opens validation window and displays <a href="RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation"><code>RuleViolationResult</code></a> in it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation">RuleViolationResult</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#validate(com.nomagic.magicdraw.validation.ValidationRunData,java.lang.String,com.nomagic.task.ProgressStatus)">validate</a><wbr/>(<a href="ValidationRunData.html" title="class in com.nomagic.magicdraw.validation">ValidationRunData</a> validationRunData,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> validationTaskName,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Runs validation for given <a href="ValidationRunData.html" title="class in com.nomagic.magicdraw.validation"><code>ValidationRunData</code></a></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation">RuleViolationResult</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#validateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List,boolean)">validateElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> elementForValidation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; rules,
 boolean excludeReadOnly)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Validates given element with given list of validation rules.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation">RuleViolationResult</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#validateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List,boolean,boolean)">validateElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> elementForValidation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; rules,
 boolean excludeReadOnly,
 boolean recursive)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Validates given element with given list of validation rules.</div>
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
<h3>ValidationHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationHelper</span>()</div>
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
<section class="detail" id="validate(com.nomagic.magicdraw.validation.ValidationRunData,java.lang.String,com.nomagic.task.ProgressStatus)">
<h3>validate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation">RuleViolationResult</a>&gt;</span> <span class="element-name">validate</span><wbr/><span class="parameters">(<a href="ValidationRunData.html" title="class in com.nomagic.magicdraw.validation">ValidationRunData</a> validationRunData,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> validationTaskName,
 @CheckForNull
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</span></div>
<div class="block">Runs validation for given <a href="ValidationRunData.html" title="class in com.nomagic.magicdraw.validation"><code>ValidationRunData</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>validationRunData</code> - instance of <a href="ValidationRunData.html" title="class in com.nomagic.magicdraw.validation"><code>ValidationRunData</code></a></dd>
<dd><code>validationTaskName</code> - which is visible when running validation. If Passed null, it will show default value "Validating"</dd>
<dd><code>progressStatus</code> - for validation, or null if to run validation with owe progress</dd>
<dt>Returns:</dt>
<dd>collection of validation results</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="validateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List,boolean)">
<h3>validateElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation">RuleViolationResult</a>&gt;</span> <span class="element-name">validateElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> elementForValidation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; rules,
 boolean excludeReadOnly)</span></div>
<div class="block">Validates given element with given list of validation rules.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementForValidation</code> - element which should be validated</dd>
<dd><code>rules</code> - list of validation rules</dd>
<dd><code>excludeReadOnly</code> - exclude read only elements or not</dd>
<dt>Returns:</dt>
<dd>list of violation results</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="validateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List,boolean,boolean)">
<h3>validateElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation">RuleViolationResult</a>&gt;</span> <span class="element-name">validateElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> elementForValidation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; rules,
 boolean excludeReadOnly,
 boolean recursive)</span></div>
<div class="block">Validates given element with given list of validation rules.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementForValidation</code> - element which should be validated.</dd>
<dd><code>rules</code> - list of validation rules.</dd>
<dd><code>excludeReadOnly</code> - exclude read only elements or not</dd>
<dd><code>recursive</code> - validate owned elements of given  element recursively</dd>
<dt>Returns:</dt>
<dd>list of violation results</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openValidationWindow(com.nomagic.magicdraw.validation.ValidationRunData,java.lang.String,java.util.Collection)">
<h3>openValidationWindow</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">openValidationWindow</span><wbr/><span class="parameters">(<a href="ValidationRunData.html" title="class in com.nomagic.magicdraw.validation">ValidationRunData</a> validationRunData,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> windowID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation">RuleViolationResult</a>&gt; results)</span></div>
<div class="block">Opens validation window and displays <a href="RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation"><code>RuleViolationResult</code></a> in it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>validationRunData</code> - instance of <a href="ValidationRunData.html" title="class in com.nomagic.magicdraw.validation"><code>ValidationRunData</code></a></dd>
<dd><code>windowID</code> - id which will be set to validation window.</dd>
<dd><code>results</code> - collection of <a href="RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation"><code>RuleViolationResult</code></a></dd>
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
