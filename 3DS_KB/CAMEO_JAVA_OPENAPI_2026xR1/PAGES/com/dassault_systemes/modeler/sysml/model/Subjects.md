# JAVA OPENAPI: Subjects (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Subjects.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Subjects.html`
- source_sha256: `39c309e5614f98cabb77628bdec40fac1d1089b5bdf892d2936301784587ab91`
- captured_utc: `2026-07-14T16:45:02.651036+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Subjects

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Subjects

@OpenApiAllpublic classSubjects
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class providing helper methods for working with Subjects

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Subjects](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Usage](sysml/Usage.html)`
`[createSubject](#createSubject(com.dassault_systemes.modeler.kerml.model.kerml.Type,int))([Type](../../kerml/model/kerml/Type.html) type,
 int relationshipPosition)`
Creates a new subject parameter on the given type at the specified
 relationship position.
`static [Usage](sysml/Usage.html)`
`[getOwnedSubjectParameter](#getOwnedSubjectParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the subject parameter owned by the given type, if any.
`static [Expression](../../kerml/model/kerml/Expression.html)`
`[getOwnedSubjectParameterOwnedValue](#getOwnedSubjectParameterOwnedValue(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the owned value expression of the subject parameter, if any.
`static [Expression](../../kerml/model/kerml/Expression.html)`
`[getOwnedSubjectParameterValue](#getOwnedSubjectParameterValue(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the value expression of the owned subject parameter, if any.
`static [Usage](sysml/Usage.html)`
`[getSubjectParameter](#getSubjectParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the subject parameter of the given type, if the type supports
 subject parameters (e.g., requirements and cases).
`static boolean`
`[isSubject](#isSubject(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Checks whether the given feature is a subject parameter.
`static boolean`
`[isSubject](#isSubject(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership))([FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)`
Checks whether the given membership represents a subject membership.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Subjects
public Subjects()
 ============ METHOD DETAIL ========== 
Method Details
createSubject
public static [Usage](sysml/Usage.html) createSubject([Type](../../kerml/model/kerml/Type.html) type,
 int relationshipPosition)
Creates a new subject parameter on the given type at the specified
 relationship position. The subject is represented as a [`ReferenceUsage`](sysml/ReferenceUsage.html)
 with [`FeatureDirectionKind.IN`](../../kerml/model/kerml/FeatureDirectionKind.html#IN) direction, owned through a
 [`SubjectMembership`](sysml/SubjectMembership.html).
Parameters:
`type` - the type on which the subject is created
`relationshipPosition` - index at which the membership is inserted,
 or a negative value to append
Returns:
the created subject parameter
getOwnedSubjectParameter
@CheckForNullpublic static [Usage](sysml/Usage.html) getOwnedSubjectParameter([Type](../../kerml/model/kerml/Type.html) type)
Returns the subject parameter owned by the given type, if any.
Parameters:
`type` - the type
Returns:
subject parameter, or null if none exists
getOwnedSubjectParameterValue
@CheckForNullpublic static [Expression](../../kerml/model/kerml/Expression.html) getOwnedSubjectParameterValue([Type](../../kerml/model/kerml/Type.html) type)
Returns the value expression of the owned subject parameter, if any.
Parameters:
`type` - the type
Returns:
value expression, or null if none exists
getOwnedSubjectParameterOwnedValue
@CheckForNullpublic static [Expression](../../kerml/model/kerml/Expression.html) getOwnedSubjectParameterOwnedValue([Type](../../kerml/model/kerml/Type.html) type)
Returns the owned value expression of the subject parameter, if any.
 This retrieves the expression directly owned by the feature value.
Parameters:
`type` - the type
Returns:
owned value expression, or null if none exists
isSubject
public static boolean isSubject([Feature](../../kerml/model/kerml/Feature.html) feature)
Checks whether the given feature is a subject parameter.
Parameters:
`feature` - the feature
Returns:
true if the feature is a subject parameter
isSubject
public static boolean isSubject(@CheckForNull
 [FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)
Checks whether the given membership represents a subject membership.
Parameters:
`membership` - the membership
Returns:
true if the membership is a [`SubjectMembership`](sysml/SubjectMembership.html)
getSubjectParameter
@CheckForNullpublic static [Usage](sysml/Usage.html) getSubjectParameter(@CheckForNull
 [Type](../../kerml/model/kerml/Type.html) type)
Returns the subject parameter of the given type, if the type supports
 subject parameters (e.g., requirements and cases).
Parameters:
`type` - the type
Returns:
subject parameter, or null if none exists

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Subjects">Class Subjects</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Subjects</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Subjects</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class providing helper methods for working with Subjects</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Subjects</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSubject(com.dassault_systemes.modeler.kerml.model.kerml.Type,int)">createSubject</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 int relationshipPosition)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a new subject parameter on the given type at the specified
 relationship position.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedSubjectParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedSubjectParameter</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the subject parameter owned by the given type, if any.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedSubjectParameterOwnedValue(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedSubjectParameterOwnedValue</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned value expression of the subject parameter, if any.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedSubjectParameterValue(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedSubjectParameterValue</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the value expression of the owned subject parameter, if any.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSubjectParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getSubjectParameter</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the subject parameter of the given type, if the type supports
 subject parameters (e.g., requirements and cases).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSubject(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isSubject</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given feature is a subject parameter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSubject(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">isSubject</a><wbr/>(<a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given membership represents a subject membership.</div>
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
<h3>Subjects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Subjects</span>()</div>
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
<section class="detail" id="createSubject(com.dassault_systemes.modeler.kerml.model.kerml.Type,int)">
<h3>createSubject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></span> <span class="element-name">createSubject</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 int relationshipPosition)</span></div>
<div class="block">Creates a new subject parameter on the given type at the specified
 relationship position. The subject is represented as a <a href="sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ReferenceUsage</code></a>
 with <a href="../../kerml/model/kerml/FeatureDirectionKind.html#IN"><code>FeatureDirectionKind.IN</code></a> direction, owned through a
 <a href="sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>SubjectMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type on which the subject is created</dd>
<dd><code>relationshipPosition</code> - index at which the membership is inserted,
                             or a negative value to append</dd>
<dt>Returns:</dt>
<dd>the created subject parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedSubjectParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedSubjectParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></span> <span class="element-name">getOwnedSubjectParameter</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the subject parameter owned by the given type, if any.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>subject parameter, or null if none exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedSubjectParameterValue(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedSubjectParameterValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">getOwnedSubjectParameterValue</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the value expression of the owned subject parameter, if any.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>value expression, or null if none exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedSubjectParameterOwnedValue(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedSubjectParameterOwnedValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">getOwnedSubjectParameterOwnedValue</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the owned value expression of the subject parameter, if any.
 This retrieves the expression directly owned by the feature value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>owned value expression, or null if none exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSubject(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isSubject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSubject</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the given feature is a subject parameter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if the feature is a subject parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSubject(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">
<h3>isSubject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSubject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</span></div>
<div class="block">Checks whether the given membership represents a subject membership.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the membership</dd>
<dt>Returns:</dt>
<dd>true if the membership is a <a href="sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>SubjectMembership</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSubjectParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getSubjectParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></span> <span class="element-name">getSubjectParameter</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the subject parameter of the given type, if the type supports
 subject parameters (e.g., requirements and cases).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>subject parameter, or null if none exists</dd>
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
