# JAVA OPENAPI: ReferentMemberships (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/ReferentMemberships.html
- source_path: `com/dassault_systemes/modeler/kerml/model/ReferentMemberships.html`
- source_sha256: `9c4d186453e6beadebd9f28439604da284ea20a60f484efd6d2fa488486a0722`
- captured_utc: `2026-07-14T16:44:48.148845+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class ReferentMemberships

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.ReferentMemberships

@OpenApiAllpublic classReferentMemberships
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Membership`](kerml/Membership.html) which represent some referent [`Element`](kerml/Element.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ReferentMemberships](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Membership](kerml/Membership.html)`
`[getNotFeatureMembership](#getNotFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate))([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Element](kerml/Element.html)> memberElementPredicate)`
Returns the first owned membership of the type that is not a FeatureMembership
 and whose member element matches the given predicate.
`static [Membership](kerml/Membership.html)`
`[getNotParameterMembership](#getNotParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate))([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Element](kerml/Element.html)> memberElementPredicate)`
Returns the first owned membership of the type that is not a ParameterMembership
 and whose member element matches the given predicate.
`static void`
`[setReferent](#setReferent(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Element,int,com.dassault_systemes.modeler.kerml.model.kerml.Membership))([Type](kerml/Type.html) type,
 [Element](kerml/Element.html) referent,
 int addAtIndex,
 [Membership](kerml/Membership.html) currentMembership)`
Sets or removes the referent element for the given type.
`static [Feature](kerml/Feature.html)`
`[setReferentFeature](#setReferentFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.List,int,com.dassault_systemes.modeler.kerml.model.kerml.Membership))([Type](kerml/Type.html) type,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> chain,
 int addAtIndex,
 [Membership](kerml/Membership.html) currentMembership)`
Sets the referent feature chain for the given type.
`static [Feature](kerml/Feature.html)`
`[setReferentFeature](#setReferentFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.List,int,org.eclipse.emf.ecore.EClass,com.dassault_systemes.modeler.kerml.model.kerml.Membership))([Type](kerml/Type.html) type,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> chain,
 int addAtIndex,
 org.eclipse.emf.ecore.EClass membershipEClass,
 [Membership](kerml/Membership.html) currentMembership)`
Sets the referent feature chain for the given type using the specified membership EClass.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ReferentMemberships
public ReferentMemberships()
 ============ METHOD DETAIL ========== 
Method Details
getNotFeatureMembership
@CheckForNullpublic static [Membership](kerml/Membership.html) getNotFeatureMembership([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Element](kerml/Element.html)> memberElementPredicate)
Returns the first owned membership of the type that is not a FeatureMembership
 and whose member element matches the given predicate.
Parameters:
`type` - the type whose memberships are inspected
`memberElementPredicate` - predicate applied to the member element
Returns:
matching membership, or null if none found
getNotParameterMembership
@CheckForNullpublic static [Membership](kerml/Membership.html) getNotParameterMembership([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Element](kerml/Element.html)> memberElementPredicate)
Returns the first owned membership of the type that is not a ParameterMembership
 and whose member element matches the given predicate.
Parameters:
`type` - the type whose memberships are inspected
`memberElementPredicate` - predicate applied to the member element
Returns:
matching membership, or null if none found
setReferent
public static void setReferent([Type](kerml/Type.html) type,
 @CheckForNull
 [Element](kerml/Element.html) referent,
 int addAtIndex,
 @CheckForNull
 [Membership](kerml/Membership.html) currentMembership)
Sets or removes the referent element for the given type.
 If referent is null, the existing membership is disposed.
 Otherwise, a membership is created or reused and updated.
Parameters:
`type` - the type whose referent is modified
`referent` - the new referent element, or null to remove
`addAtIndex` - index at which to insert a new membership
`currentMembership` - existing membership, or null
setReferentFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) setReferentFeature([Type](kerml/Type.html) type,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> chain,
 int addAtIndex,
 @CheckForNull
 [Membership](kerml/Membership.html) currentMembership)
Sets the referent feature chain for the given type.
 Chooses the appropriate membership EClass based on chain length.
Parameters:
`type` - the type whose referent is modified
`chain` - feature chain to set
`addAtIndex` - index at which to insert a new membership
`currentMembership` - existing membership, or null
Returns:
the final feature in the chain, or null if none
setReferentFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) setReferentFeature([Type](kerml/Type.html) type,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> chain,
 int addAtIndex,
 org.eclipse.emf.ecore.EClass membershipEClass,
 @CheckForNull
 [Membership](kerml/Membership.html) currentMembership)
Sets the referent feature chain for the given type using the specified membership EClass.
Parameters:
`type` - the type whose referent is modified
`chain` - feature chain to set
`addAtIndex` - index at which to insert a new membership
`membershipEClass` - membership class to use
`currentMembership` - existing membership, or null
Returns:
the final feature in the chain, or null if none

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class ReferentMemberships">Class ReferentMemberships</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.ReferentMemberships</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ReferentMemberships</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Membership</code></a> which represent some referent <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ReferentMemberships</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate)">getNotFeatureMembership</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; memberElementPredicate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first owned membership of the type that is not a FeatureMembership
 and whose member element matches the given predicate.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate)">getNotParameterMembership</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; memberElementPredicate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first owned membership of the type that is not a ParameterMembership
 and whose member element matches the given predicate.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReferent(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Element,int,com.dassault_systemes.modeler.kerml.model.kerml.Membership)">setReferent</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> referent,
 int addAtIndex,
 <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> currentMembership)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets or removes the referent element for the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReferentFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.List,int,com.dassault_systemes.modeler.kerml.model.kerml.Membership)">setReferentFeature</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain,
 int addAtIndex,
 <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> currentMembership)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the referent feature chain for the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReferentFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.List,int,org.eclipse.emf.ecore.EClass,com.dassault_systemes.modeler.kerml.model.kerml.Membership)">setReferentFeature</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain,
 int addAtIndex,
 org.eclipse.emf.ecore.EClass membershipEClass,
 <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> currentMembership)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the referent feature chain for the given type using the specified membership EClass.</div>
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
<h3>ReferentMemberships</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ReferentMemberships</span>()</div>
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
<section class="detail" id="getNotFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate)">
<h3>getNotFeatureMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></span> <span class="element-name">getNotFeatureMembership</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; memberElementPredicate)</span></div>
<div class="block">Returns the first owned membership of the type that is not a FeatureMembership
 and whose member element matches the given predicate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose memberships are inspected</dd>
<dd><code>memberElementPredicate</code> - predicate applied to the member element</dd>
<dt>Returns:</dt>
<dd>matching membership, or null if none found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNotParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate)">
<h3>getNotParameterMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></span> <span class="element-name">getNotParameterMembership</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; memberElementPredicate)</span></div>
<div class="block">Returns the first owned membership of the type that is not a ParameterMembership
 and whose member element matches the given predicate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose memberships are inspected</dd>
<dd><code>memberElementPredicate</code> - predicate applied to the member element</dd>
<dt>Returns:</dt>
<dd>matching membership, or null if none found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReferent(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Element,int,com.dassault_systemes.modeler.kerml.model.kerml.Membership)">
<h3>setReferent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setReferent</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 @CheckForNull
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> referent,
 int addAtIndex,
 @CheckForNull
 <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> currentMembership)</span></div>
<div class="block">Sets or removes the referent element for the given type.
 If referent is null, the existing membership is disposed.
 Otherwise, a membership is created or reused and updated.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose referent is modified</dd>
<dd><code>referent</code> - the new referent element, or null to remove</dd>
<dd><code>addAtIndex</code> - index at which to insert a new membership</dd>
<dd><code>currentMembership</code> - existing membership, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReferentFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.List,int,com.dassault_systemes.modeler.kerml.model.kerml.Membership)">
<h3>setReferentFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">setReferentFeature</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain,
 int addAtIndex,
 @CheckForNull
 <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> currentMembership)</span></div>
<div class="block">Sets the referent feature chain for the given type.
 Chooses the appropriate membership EClass based on chain length.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose referent is modified</dd>
<dd><code>chain</code> - feature chain to set</dd>
<dd><code>addAtIndex</code> - index at which to insert a new membership</dd>
<dd><code>currentMembership</code> - existing membership, or null</dd>
<dt>Returns:</dt>
<dd>the final feature in the chain, or null if none</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReferentFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.List,int,org.eclipse.emf.ecore.EClass,com.dassault_systemes.modeler.kerml.model.kerml.Membership)">
<h3>setReferentFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">setReferentFeature</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain,
 int addAtIndex,
 org.eclipse.emf.ecore.EClass membershipEClass,
 @CheckForNull
 <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> currentMembership)</span></div>
<div class="block">Sets the referent feature chain for the given type using the specified membership EClass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose referent is modified</dd>
<dd><code>chain</code> - feature chain to set</dd>
<dd><code>addAtIndex</code> - index at which to insert a new membership</dd>
<dd><code>membershipEClass</code> - membership class to use</dd>
<dd><code>currentMembership</code> - existing membership, or null</dd>
<dt>Returns:</dt>
<dd>the final feature in the chain, or null if none</dd>
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
