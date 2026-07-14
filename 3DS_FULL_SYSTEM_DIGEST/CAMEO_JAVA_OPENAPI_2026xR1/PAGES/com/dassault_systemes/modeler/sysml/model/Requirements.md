# JAVA OPENAPI: Requirements (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Requirements.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Requirements.html`
- source_sha256: `af0b0a8aa202d5aac2235da92b9a005e6947314882d49a5daed575cbfab74159`
- captured_utc: `2026-07-14T16:45:02.945043+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Requirements

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Requirements

@OpenApiAllpublic classRequirements
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`RequirementUsage`](sysml/RequirementUsage.html) or [`RequirementDefinition`](sysml/RequirementDefinition.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Requirements](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [RequirementUsage](sysml/RequirementUsage.html)`
`[getActualRequirementUsage](#getActualRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage))([ConstraintUsage](sysml/ConstraintUsage.html) usage)`
Returns the actual requirement usage represented by the given constraint usage.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConstraintUsage](sysml/ConstraintUsage.html)>`
`[getAssumedConstraint](#getAssumedConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns all assumed constraints of the given type.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConcernUsage](sysml/ConcernUsage.html)>`
`[getFramedConcern](#getFramedConcern(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns all framed concerns of the given type.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConstraintUsage](sysml/ConstraintUsage.html)>`
`[getOwnedAssumedConstraint](#getOwnedAssumedConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the assumed constraints owned directly by the type.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConcernUsage](sysml/ConcernUsage.html)>`
`[getOwnedFramedConcern](#getOwnedFramedConcern(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the framed concerns owned directly by the type.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConstraintUsage](sysml/ConstraintUsage.html)>`
`[getOwnedRequiredConstraint](#getOwnedRequiredConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the required constraints owned directly by the type.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](sysml/PartUsage.html)>`
`[getOwnedStakeholderParameter](#getOwnedStakeholderParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the stakeholder parameters owned directly by the type.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getReqId](#getReqId(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the requirement ID of the given type, if any.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConstraintUsage](sysml/ConstraintUsage.html)>`
`[getRequiredConstraint](#getRequiredConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns all required constraints of the given type.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](sysml/PartUsage.html)>`
`[getStakeholderParameter](#getStakeholderParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the stakeholder parameters of the given type.
`static boolean`
`[isAssumedConstraint](#isAssumedConstraint(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership))([FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)`
Checks whether the membership represents an assumed requirement constraint.
`static boolean`
`[isFramedConcern](#isFramedConcern(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Checks whether the feature is a framed concern.
`static boolean`
`[isFramedConcern](#isFramedConcern(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership))([FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)`
Checks whether the membership represents a framed concern membership.
`static boolean`
`[isOwningTypeRequirementUsageOrDefinition](#isOwningTypeRequirementUsageOrDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage))([RequirementUsage](sysml/RequirementUsage.html) requirementUsage)`
Checks whether the owning type of the requirement usage is itself
 a requirement usage or definition.
`static boolean`
`[isRequiredConstraint](#isRequiredConstraint(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership))([FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)`
Checks whether the membership represents a required requirement constraint.
`static boolean`
`[isRequirementParameter](#isRequirementParameter(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Checks whether the feature is a requirement parameter.
`static boolean`
`[isRequirementUsageOrDefinition](#isRequirementUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Checks whether the element is a requirement usage or definition.
`static boolean`
`[isRequirementUsageOrDefinition](#isRequirementUsageOrDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the given EClass represents a requirement usage or definition.
`static boolean`
`[isStakeholder](#isStakeholder(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Checks whether the feature is a stakeholder parameter.
`static boolean`
`[isStakeholder](#isStakeholder(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership))([FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)`
Checks whether the membership represents a stakeholder membership.
`static boolean`
`[isVerify](#isVerify(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership))([FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)`
Checks whether the membership represents a requirement verification.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Requirements
public Requirements()
 ============ METHOD DETAIL ========== 
Method Details
isVerify
public static boolean isVerify(@CheckForNull
 [FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)
Checks whether the membership represents a requirement verification.
Parameters:
`membership` - the membership
Returns:
true if the membership is a [`RequirementVerificationMembership`](sysml/RequirementVerificationMembership.html)
isStakeholder
public static boolean isStakeholder([Feature](../../kerml/model/kerml/Feature.html) feature)
Checks whether the feature is a stakeholder parameter.
Parameters:
`feature` - the feature
Returns:
true if the feature is a stakeholder parameter
isStakeholder
public static boolean isStakeholder(@CheckForNull
 [FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)
Checks whether the membership represents a stakeholder membership.
Parameters:
`membership` - the membership
Returns:
true if stakeholder membership
isFramedConcern
public static boolean isFramedConcern([Feature](../../kerml/model/kerml/Feature.html) feature)
Checks whether the feature is a framed concern.
Parameters:
`feature` - the feature
Returns:
true if the feature is a framed concern
isFramedConcern
public static boolean isFramedConcern(@CheckForNull
 [FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)
Checks whether the membership represents a framed concern membership.
Parameters:
`membership` - the membership
Returns:
true if framed concern membership
isRequirementParameter
public static boolean isRequirementParameter([Feature](../../kerml/model/kerml/Feature.html) feature)
Checks whether the feature is a requirement parameter.
 Requirement parameters include:
 actors
stakeholders
subjects
Parameters:
`feature` - the feature
Returns:
true if requirement parameter
isAssumedConstraint
public static boolean isAssumedConstraint(@CheckForNull
 [FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)
Checks whether the membership represents an assumed requirement constraint.
Parameters:
`membership` - the membership
Returns:
true if assumed constraint
isRequiredConstraint
public static boolean isRequiredConstraint(@CheckForNull
 [FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)
Checks whether the membership represents a required requirement constraint.
Parameters:
`membership` - the membership
Returns:
true if required constraint
isRequirementUsageOrDefinition
public static boolean isRequirementUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Checks whether the element is a requirement usage or definition.
Parameters:
`element` - the element
Returns:
true if requirement usage or definition
isRequirementUsageOrDefinition
public static boolean isRequirementUsageOrDefinition(org.eclipse.emf.ecore.EClass eClass)
Checks whether the given EClass represents a requirement usage or definition.
Parameters:
`eClass` - the class
Returns:
true if requirement usage or definition
isOwningTypeRequirementUsageOrDefinition
public static boolean isOwningTypeRequirementUsageOrDefinition([RequirementUsage](sysml/RequirementUsage.html) requirementUsage)
Checks whether the owning type of the requirement usage is itself
 a requirement usage or definition.
Parameters:
`requirementUsage` - the requirement usage
Returns:
true if owning type is requirement usage or definition
getActualRequirementUsage
@CheckForNullpublic static [RequirementUsage](sysml/RequirementUsage.html) getActualRequirementUsage([ConstraintUsage](sysml/ConstraintUsage.html) usage)
Returns the actual requirement usage represented by the given constraint usage.
 For satisfy requirement usages, this returns the satisfied requirement.
Parameters:
`usage` - the constraint usage
Returns:
requirement usage, or null if none applies
getRequiredConstraint
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConstraintUsage](sysml/ConstraintUsage.html)> getRequiredConstraint([Type](../../kerml/model/kerml/Type.html) type)
Returns all required constraints of the given type.
Parameters:
`type` - the type
Returns:
list of required constraints
getOwnedRequiredConstraint
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConstraintUsage](sysml/ConstraintUsage.html)> getOwnedRequiredConstraint([Type](../../kerml/model/kerml/Type.html) type)
Returns the required constraints owned directly by the type.
Parameters:
`type` - the type
Returns:
list of owned required constraints
getAssumedConstraint
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConstraintUsage](sysml/ConstraintUsage.html)> getAssumedConstraint([Type](../../kerml/model/kerml/Type.html) type)
Returns all assumed constraints of the given type.
Parameters:
`type` - the type
Returns:
list of assumed constraints
getOwnedAssumedConstraint
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConstraintUsage](sysml/ConstraintUsage.html)> getOwnedAssumedConstraint([Type](../../kerml/model/kerml/Type.html) type)
Returns the assumed constraints owned directly by the type.
Parameters:
`type` - the type
Returns:
list of owned assumed constraints
getFramedConcern
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConcernUsage](sysml/ConcernUsage.html)> getFramedConcern([Type](../../kerml/model/kerml/Type.html) type)
Returns all framed concerns of the given type.
Parameters:
`type` - the type
Returns:
list of framed concerns
getOwnedFramedConcern
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConcernUsage](sysml/ConcernUsage.html)> getOwnedFramedConcern([Type](../../kerml/model/kerml/Type.html) type)
Returns the framed concerns owned directly by the type.
Parameters:
`type` - the type
Returns:
list of owned framed concerns
getReqId
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getReqId([Type](../../kerml/model/kerml/Type.html) type)
Returns the requirement ID of the given type, if any.
Parameters:
`type` - the type
Returns:
requirement ID, or null if none exists
getStakeholderParameter
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](sysml/PartUsage.html)> getStakeholderParameter([Type](../../kerml/model/kerml/Type.html) type)
Returns the stakeholder parameters of the given type.
Parameters:
`type` - the type
Returns:
list of stakeholder parameters
getOwnedStakeholderParameter
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](sysml/PartUsage.html)> getOwnedStakeholderParameter([Type](../../kerml/model/kerml/Type.html) type)
Returns the stakeholder parameters owned directly by the type.
Parameters:
`type` - the type
Returns:
list of owned stakeholder parameters

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Requirements">Class Requirements</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Requirements</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Requirements</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementUsage</code></a> or <a href="sysml/RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementDefinition</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Requirements</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getActualRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage)">getActualRequirementUsage</a><wbr/>(<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a> usage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the actual requirement usage represented by the given constraint usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssumedConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getAssumedConstraint</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all assumed constraints of the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFramedConcern(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getFramedConcern</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all framed concerns of the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedAssumedConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedAssumedConstraint</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the assumed constraints owned directly by the type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedFramedConcern(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedFramedConcern</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the framed concerns owned directly by the type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedRequiredConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedRequiredConstraint</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the required constraints owned directly by the type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedStakeholderParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedStakeholderParameter</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the stakeholder parameters owned directly by the type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReqId(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getReqId</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the requirement ID of the given type, if any.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiredConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getRequiredConstraint</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all required constraints of the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStakeholderParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getStakeholderParameter</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the stakeholder parameters of the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAssumedConstraint(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">isAssumedConstraint</a><wbr/>(<a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the membership represents an assumed requirement constraint.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFramedConcern(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isFramedConcern</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the feature is a framed concern.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFramedConcern(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">isFramedConcern</a><wbr/>(<a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the membership represents a framed concern membership.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOwningTypeRequirementUsageOrDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage)">isOwningTypeRequirementUsageOrDefinition</a><wbr/>(<a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a> requirementUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the owning type of the requirement usage is itself
 a requirement usage or definition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRequiredConstraint(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">isRequiredConstraint</a><wbr/>(<a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the membership represents a required requirement constraint.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRequirementParameter(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isRequirementParameter</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the feature is a requirement parameter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRequirementUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isRequirementUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is a requirement usage or definition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRequirementUsageOrDefinition(org.eclipse.emf.ecore.EClass)">isRequirementUsageOrDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given EClass represents a requirement usage or definition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStakeholder(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isStakeholder</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the feature is a stakeholder parameter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStakeholder(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">isStakeholder</a><wbr/>(<a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the membership represents a stakeholder membership.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isVerify(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">isVerify</a><wbr/>(<a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the membership represents a requirement verification.</div>
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
<h3>Requirements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Requirements</span>()</div>
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
<section class="detail" id="isVerify(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">
<h3>isVerify</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isVerify</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</span></div>
<div class="block">Checks whether the membership represents a requirement verification.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the membership</dd>
<dt>Returns:</dt>
<dd>true if the membership is a <a href="sysml/RequirementVerificationMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementVerificationMembership</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStakeholder(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isStakeholder</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStakeholder</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the feature is a stakeholder parameter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if the feature is a stakeholder parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStakeholder(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">
<h3>isStakeholder</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStakeholder</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</span></div>
<div class="block">Checks whether the membership represents a stakeholder membership.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the membership</dd>
<dt>Returns:</dt>
<dd>true if stakeholder membership</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFramedConcern(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isFramedConcern</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFramedConcern</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the feature is a framed concern.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if the feature is a framed concern</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFramedConcern(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">
<h3>isFramedConcern</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFramedConcern</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</span></div>
<div class="block">Checks whether the membership represents a framed concern membership.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the membership</dd>
<dt>Returns:</dt>
<dd>true if framed concern membership</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRequirementParameter(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isRequirementParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRequirementParameter</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the feature is a requirement parameter.
 Requirement parameters include:
 <ul>
<li>actors</li>
<li>stakeholders</li>
<li>subjects</li>
</ul></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if requirement parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAssumedConstraint(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">
<h3>isAssumedConstraint</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAssumedConstraint</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</span></div>
<div class="block">Checks whether the membership represents an assumed requirement constraint.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the membership</dd>
<dt>Returns:</dt>
<dd>true if assumed constraint</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRequiredConstraint(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">
<h3>isRequiredConstraint</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRequiredConstraint</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</span></div>
<div class="block">Checks whether the membership represents a required requirement constraint.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the membership</dd>
<dt>Returns:</dt>
<dd>true if required constraint</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRequirementUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isRequirementUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRequirementUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the element is a requirement usage or definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>true if requirement usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRequirementUsageOrDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isRequirementUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRequirementUsageOrDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the given EClass represents a requirement usage or definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class</dd>
<dt>Returns:</dt>
<dd>true if requirement usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOwningTypeRequirementUsageOrDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage)">
<h3>isOwningTypeRequirementUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOwningTypeRequirementUsageOrDefinition</span><wbr/><span class="parameters">(<a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a> requirementUsage)</span></div>
<div class="block">Checks whether the owning type of the requirement usage is itself
 a requirement usage or definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>requirementUsage</code> - the requirement usage</dd>
<dt>Returns:</dt>
<dd>true if owning type is requirement usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActualRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage)">
<h3>getActualRequirementUsage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></span> <span class="element-name">getActualRequirementUsage</span><wbr/><span class="parameters">(<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a> usage)</span></div>
<div class="block">Returns the actual requirement usage represented by the given constraint usage.
 For satisfy requirement usages, this returns the satisfied requirement.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usage</code> - the constraint usage</dd>
<dt>Returns:</dt>
<dd>requirement usage, or null if none applies</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiredConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getRequiredConstraint</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a>&gt;</span> <span class="element-name">getRequiredConstraint</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns all required constraints of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>list of required constraints</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedRequiredConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedRequiredConstraint</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a>&gt;</span> <span class="element-name">getOwnedRequiredConstraint</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the required constraints owned directly by the type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>list of owned required constraints</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssumedConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getAssumedConstraint</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a>&gt;</span> <span class="element-name">getAssumedConstraint</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns all assumed constraints of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>list of assumed constraints</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedAssumedConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedAssumedConstraint</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a>&gt;</span> <span class="element-name">getOwnedAssumedConstraint</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the assumed constraints owned directly by the type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>list of owned assumed constraints</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFramedConcern(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getFramedConcern</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a>&gt;</span> <span class="element-name">getFramedConcern</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns all framed concerns of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>list of framed concerns</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedFramedConcern(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedFramedConcern</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a>&gt;</span> <span class="element-name">getOwnedFramedConcern</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the framed concerns owned directly by the type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>list of owned framed concerns</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReqId(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getReqId</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getReqId</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the requirement ID of the given type, if any.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>requirement ID, or null if none exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStakeholderParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getStakeholderParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</span> <span class="element-name">getStakeholderParameter</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the stakeholder parameters of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>list of stakeholder parameters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedStakeholderParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedStakeholderParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</span> <span class="element-name">getOwnedStakeholderParameter</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the stakeholder parameters owned directly by the type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>list of owned stakeholder parameters</dd>
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
