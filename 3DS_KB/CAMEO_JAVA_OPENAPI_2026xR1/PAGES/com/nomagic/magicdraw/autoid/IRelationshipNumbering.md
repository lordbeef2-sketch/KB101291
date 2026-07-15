# JAVA OPENAPI: IRelationshipNumbering (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/autoid/IRelationshipNumbering.html
- source_path: `com/nomagic/magicdraw/autoid/IRelationshipNumbering.html`
- source_sha256: `e3a519b6e18f24f9d226c32f3901b169deb28af90f24d2ba9dcc63aa8218f373`
- captured_utc: `2026-07-14T16:45:08.334115+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.autoid](package-summary.html)

## Interface IRelationshipNumbering

All Known Implementing Classes:
`[AbstractionNumbering](custom/AbstractionNumbering.html)`, `[ComponentRealizationNumbering](custom/ComponentRealizationNumbering.html)`, `[DependencyNumbering](custom/DependencyNumbering.html)`, `[DeploymentNumbering](custom/DeploymentNumbering.html)`, `[DirectedRelationshipNumbering](custom/DirectedRelationshipNumbering.html)`, `[ElementImportNumbering](custom/ElementImportNumbering.html)`, `[ExtendNumbering](custom/ExtendNumbering.html)`, `[GeneralizationNumbering](custom/GeneralizationNumbering.html)`, `[IncludeNumbering](custom/IncludeNumbering.html)`, `[InformationFlowNumbering](custom/InformationFlowNumbering.html)`, `[InterfaceRealizationNumbering](custom/InterfaceRealizationNumbering.html)`, `[ManifestationNumbering](custom/ManifestationNumbering.html)`, `[PackageImportNumbering](custom/PackageImportNumbering.html)`, `[PackageMergeNumbering](custom/PackageMergeNumbering.html)`, `[ProfileApplicationNumbering](custom/ProfileApplicationNumbering.html)`, `[ProtocolConformanceNumbering](custom/ProtocolConformanceNumbering.html)`, `[RealizationNumbering](custom/RealizationNumbering.html)`, `[SubstitutionNumbering](custom/SubstitutionNumbering.html)`, `[TemplateBindingNumbering](custom/TemplateBindingNumbering.html)`, `[UsageNumbering](custom/UsageNumbering.html)`

@OpenApiAllpublic interfaceIRelationshipNumbering

Interface for Numbering customizations to be applied to
 Elements that are connected by some types of directedRelationships

 Feb 20, 2012

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [DirectedRelationship](../../uml2/ext/magicdraw/classes/mdkernel/DirectedRelationship.html)>>`
`[getRelationTypes](#getRelationTypes())()`
Which types of directedRelationships should be taken into consideration
 for element sthat are eithe rsource or target of the given relation types.

============ METHOD DETAIL ========== 
Method Details
getRelationTypes
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [DirectedRelationship](../../uml2/ext/magicdraw/classes/mdkernel/DirectedRelationship.html)>> getRelationTypes()
Which types of directedRelationships should be taken into consideration
 for element sthat are eithe rsource or target of the given relation types.
Returns:
a collection of directed relationship types

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.autoid</a></div>
<h1 class="title" title="Interface IRelationshipNumbering">Interface IRelationshipNumbering</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="custom/AbstractionNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">AbstractionNumbering</a></code>, <code><a href="custom/ComponentRealizationNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">ComponentRealizationNumbering</a></code>, <code><a href="custom/DependencyNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">DependencyNumbering</a></code>, <code><a href="custom/DeploymentNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">DeploymentNumbering</a></code>, <code><a href="custom/DirectedRelationshipNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">DirectedRelationshipNumbering</a></code>, <code><a href="custom/ElementImportNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">ElementImportNumbering</a></code>, <code><a href="custom/ExtendNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">ExtendNumbering</a></code>, <code><a href="custom/GeneralizationNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">GeneralizationNumbering</a></code>, <code><a href="custom/IncludeNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">IncludeNumbering</a></code>, <code><a href="custom/InformationFlowNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">InformationFlowNumbering</a></code>, <code><a href="custom/InterfaceRealizationNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">InterfaceRealizationNumbering</a></code>, <code><a href="custom/ManifestationNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">ManifestationNumbering</a></code>, <code><a href="custom/PackageImportNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">PackageImportNumbering</a></code>, <code><a href="custom/PackageMergeNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">PackageMergeNumbering</a></code>, <code><a href="custom/ProfileApplicationNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">ProfileApplicationNumbering</a></code>, <code><a href="custom/ProtocolConformanceNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">ProtocolConformanceNumbering</a></code>, <code><a href="custom/RealizationNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">RealizationNumbering</a></code>, <code><a href="custom/SubstitutionNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">SubstitutionNumbering</a></code>, <code><a href="custom/TemplateBindingNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">TemplateBindingNumbering</a></code>, <code><a href="custom/UsageNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">UsageNumbering</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IRelationshipNumbering</span></div>
<div class="block">Interface for Numbering customizations to be applied to
 Elements that are connected by some types of directedRelationships

 Feb 20, 2012</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a>&gt;&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRelationTypes()">getRelationTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Which types of directedRelationships should be taken into consideration
 for element sthat are eithe rsource or target of the given relation types.</div>
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
<section class="detail" id="getRelationTypes()">
<h3>getRelationTypes</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a>&gt;&gt;</span> <span class="element-name">getRelationTypes</span>()</div>
<div class="block">Which types of directedRelationships should be taken into consideration
 for element sthat are eithe rsource or target of the given relation types.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a collection of directed relationship types</dd>
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
