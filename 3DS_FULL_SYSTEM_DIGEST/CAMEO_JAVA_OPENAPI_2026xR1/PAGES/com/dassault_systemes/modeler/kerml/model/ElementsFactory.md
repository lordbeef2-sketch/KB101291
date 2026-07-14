# JAVA OPENAPI: ElementsFactory (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/ElementsFactory.html
- source_path: `com/dassault_systemes/modeler/kerml/model/ElementsFactory.html`
- source_sha256: `088d5b16400e7c65299acd95e364bab5c700e57d9952e11f7165faac8870b174`
- captured_utc: `2026-07-14T16:44:47.364835+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Interface ElementsFactory

All Superinterfaces:
`com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory`, `[KerMLElementsFactory](KerMLElementsFactory.html)`

All Known Subinterfaces:
`[ElementsFactory](../../sysml/model/ElementsFactory.html)`

@OpenApiAllpublic interfaceElementsFactoryextends [KerMLElementsFactory](KerMLElementsFactory.html)

Entry point for creating KerML model elements.

Use this factory to instantiate base modeling elements in a specific project.
 It provides the core element creation API used by higher-level layers (e.g., SysML).

**Typical usage:**

````java
ElementsFactory factory = ElementsFactory.get(project);
 // factory.createXxx(...)
````

========== METHOD SUMMARY =========== 
Method Summary
Static Methods
Modifier and Type
Method
Description
`static [ElementsFactory](ElementsFactory.html)`
`[get](#get(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../foundation/project/ModelElementProject.html) project)`
Gets a factory for the given project.
`static [ElementsFactory](ElementsFactory.html)`
`[get](#get(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Gets a factory using the project of the given element.
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory
`create, initializeElement`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.[KerMLElementsFactory](KerMLElementsFactory.html)
`[create](KerMLElementsFactory.html#create(java.lang.Class)), [createAnnotatingElement](KerMLElementsFactory.html#createAnnotatingElement()), [createAnnotation](KerMLElementsFactory.html#createAnnotation()), [createAssociation](KerMLElementsFactory.html#createAssociation()), [createAssociationStructure](KerMLElementsFactory.html#createAssociationStructure()), [createBehavior](KerMLElementsFactory.html#createBehavior()), [createBindingConnector](KerMLElementsFactory.html#createBindingConnector()), [createBooleanExpression](KerMLElementsFactory.html#createBooleanExpression()), [createClass](KerMLElementsFactory.html#createClass()), [createClassifier](KerMLElementsFactory.html#createClassifier()), [createCollectExpression](KerMLElementsFactory.html#createCollectExpression()), [createComment](KerMLElementsFactory.html#createComment()), [createConjugation](KerMLElementsFactory.html#createConjugation()), [createConnector](KerMLElementsFactory.html#createConnector()), [createConstructorExpression](KerMLElementsFactory.html#createConstructorExpression()), [createCrossSubsetting](KerMLElementsFactory.html#createCrossSubsetting()), [createDataType](KerMLElementsFactory.html#createDataType()), [createDependency](KerMLElementsFactory.html#createDependency()), [createDifferencing](KerMLElementsFactory.html#createDifferencing()), [createDisjoining](KerMLElementsFactory.html#createDisjoining()), [createDocumentation](KerMLElementsFactory.html#createDocumentation()), [createElementFilterMembership](KerMLElementsFactory.html#createElementFilterMembership()), [createEndFeatureMembership](KerMLElementsFactory.html#createEndFeatureMembership()), [createExpression](KerMLElementsFactory.html#createExpression()), [createFeature](KerMLElementsFactory.html#createFeature()), [createFeatureChainExpression](KerMLElementsFactory.html#createFeatureChainExpression()), [createFeatureChaining](KerMLElementsFactory.html#createFeatureChaining()), [createFeatureInverting](KerMLElementsFactory.html#createFeatureInverting()), [createFeatureMembership](KerMLElementsFactory.html#createFeatureMembership()), [createFeatureReferenceExpression](KerMLElementsFactory.html#createFeatureReferenceExpression()), [createFeatureTyping](KerMLElementsFactory.html#createFeatureTyping()), [createFeatureValue](KerMLElementsFactory.html#createFeatureValue()), [createFlow](KerMLElementsFactory.html#createFlow()), [createFlowEnd](KerMLElementsFactory.html#createFlowEnd()), [createFunction](KerMLElementsFactory.html#createFunction()), [createIndexExpression](KerMLElementsFactory.html#createIndexExpression()), [createInteraction](KerMLElementsFactory.html#createInteraction()), [createIntersecting](KerMLElementsFactory.html#createIntersecting()), [createInvariant](KerMLElementsFactory.html#createInvariant()), [createInvocationExpression](KerMLElementsFactory.html#createInvocationExpression()), [createLibraryPackage](KerMLElementsFactory.html#createLibraryPackage()), [createLiteralBoolean](KerMLElementsFactory.html#createLiteralBoolean()), [createLiteralExpression](KerMLElementsFactory.html#createLiteralExpression()), [createLiteralInfinity](KerMLElementsFactory.html#createLiteralInfinity()), [createLiteralInteger](KerMLElementsFactory.html#createLiteralInteger()), [createLiteralRational](KerMLElementsFactory.html#createLiteralRational()), [createLiteralString](KerMLElementsFactory.html#createLiteralString()), [createMembership](KerMLElementsFactory.html#createMembership()), [createMembershipImport](KerMLElementsFactory.html#createMembershipImport()), [createMetaclass](KerMLElementsFactory.html#createMetaclass()), [createMetadataAccessExpression](KerMLElementsFactory.html#createMetadataAccessExpression()), [createMetadataFeature](KerMLElementsFactory.html#createMetadataFeature()), [createMultiplicity](KerMLElementsFactory.html#createMultiplicity()), [createMultiplicityRange](KerMLElementsFactory.html#createMultiplicityRange()), [createNamespace](KerMLElementsFactory.html#createNamespace()), [createNamespaceImport](KerMLElementsFactory.html#createNamespaceImport()), [createNullExpression](KerMLElementsFactory.html#createNullExpression()), [createOperatorExpression](KerMLElementsFactory.html#createOperatorExpression()), [createOwningMembership](KerMLElementsFactory.html#createOwningMembership()), [createPackage](KerMLElementsFactory.html#createPackage()), [createParameterMembership](KerMLElementsFactory.html#createParameterMembership()), [createPayloadFeature](KerMLElementsFactory.html#createPayloadFeature()), [createPredicate](KerMLElementsFactory.html#createPredicate()), [createRedefinition](KerMLElementsFactory.html#createRedefinition()), [createReferenceSubsetting](KerMLElementsFactory.html#createReferenceSubsetting()), [createResultExpressionMembership](KerMLElementsFactory.html#createResultExpressionMembership()), [createReturnParameterMembership](KerMLElementsFactory.html#createReturnParameterMembership()), [createSelectExpression](KerMLElementsFactory.html#createSelectExpression()), [createSpecialization](KerMLElementsFactory.html#createSpecialization()), [createStep](KerMLElementsFactory.html#createStep()), [createStructure](KerMLElementsFactory.html#createStructure()), [createSubclassification](KerMLElementsFactory.html#createSubclassification()), [createSubsetting](KerMLElementsFactory.html#createSubsetting()), [createSuccession](KerMLElementsFactory.html#createSuccession()), [createSuccessionFlow](KerMLElementsFactory.html#createSuccessionFlow()), [createTextualRepresentation](KerMLElementsFactory.html#createTextualRepresentation()), [createType](KerMLElementsFactory.html#createType()), [createTypeFeaturing](KerMLElementsFactory.html#createTypeFeaturing()), [createUnioning](KerMLElementsFactory.html#createUnioning())`

============ METHOD DETAIL ========== 
Method Details
get
static [ElementsFactory](ElementsFactory.html) get([ModelElementProject](../../foundation/project/ModelElementProject.html) project)
Gets a factory for the given project.
Parameters:
`project` - project context
Returns:
elements factory bound to the project
get
static [ElementsFactory](ElementsFactory.html) get([Element](kerml/Element.html) element)
Gets a factory using the project of the given element.
Parameters:
`element` - element to resolve project from
Returns:
elements factory bound to the element's project

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Interface ElementsFactory">Interface ElementsFactory</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory</code>, <code><a href="KerMLElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLElementsFactory</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../sysml/model/ElementsFactory.html" title="interface in com.dassault_systemes.modeler.sysml.model">ElementsFactory</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ElementsFactory</span><span class="extends-implements">
extends <a href="KerMLElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLElementsFactory</a></span></div>
<div class="block">Entry point for creating KerML model elements.

 <p>Use this factory to instantiate base modeling elements in a specific project.
 It provides the core element creation API used by higher-level layers (e.g., SysML).</p>
<p><b>Typical usage:</b></p>
<pre><code>
 ElementsFactory factory = ElementsFactory.get(project);
 // factory.createXxx(...)
 </code></pre></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div class="caption"><span>Static Methods</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">ElementsFactory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#get(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">get</a><wbr/>(<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Gets a factory for the given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">ElementsFactory</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#get(com.dassault_systemes.modeler.kerml.model.kerml.Element)">get</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Gets a factory using the project of the given element.</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory</h3>
<code>create, initializeElement</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.KerMLElementsFactory">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.<a href="KerMLElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLElementsFactory</a></h3>
<code><a href="KerMLElementsFactory.html#create(java.lang.Class)">create</a>, <a href="KerMLElementsFactory.html#createAnnotatingElement()">createAnnotatingElement</a>, <a href="KerMLElementsFactory.html#createAnnotation()">createAnnotation</a>, <a href="KerMLElementsFactory.html#createAssociation()">createAssociation</a>, <a href="KerMLElementsFactory.html#createAssociationStructure()">createAssociationStructure</a>, <a href="KerMLElementsFactory.html#createBehavior()">createBehavior</a>, <a href="KerMLElementsFactory.html#createBindingConnector()">createBindingConnector</a>, <a href="KerMLElementsFactory.html#createBooleanExpression()">createBooleanExpression</a>, <a href="KerMLElementsFactory.html#createClass()">createClass</a>, <a href="KerMLElementsFactory.html#createClassifier()">createClassifier</a>, <a href="KerMLElementsFactory.html#createCollectExpression()">createCollectExpression</a>, <a href="KerMLElementsFactory.html#createComment()">createComment</a>, <a href="KerMLElementsFactory.html#createConjugation()">createConjugation</a>, <a href="KerMLElementsFactory.html#createConnector()">createConnector</a>, <a href="KerMLElementsFactory.html#createConstructorExpression()">createConstructorExpression</a>, <a href="KerMLElementsFactory.html#createCrossSubsetting()">createCrossSubsetting</a>, <a href="KerMLElementsFactory.html#createDataType()">createDataType</a>, <a href="KerMLElementsFactory.html#createDependency()">createDependency</a>, <a href="KerMLElementsFactory.html#createDifferencing()">createDifferencing</a>, <a href="KerMLElementsFactory.html#createDisjoining()">createDisjoining</a>, <a href="KerMLElementsFactory.html#createDocumentation()">createDocumentation</a>, <a href="KerMLElementsFactory.html#createElementFilterMembership()">createElementFilterMembership</a>, <a href="KerMLElementsFactory.html#createEndFeatureMembership()">createEndFeatureMembership</a>, <a href="KerMLElementsFactory.html#createExpression()">createExpression</a>, <a href="KerMLElementsFactory.html#createFeature()">createFeature</a>, <a href="KerMLElementsFactory.html#createFeatureChainExpression()">createFeatureChainExpression</a>, <a href="KerMLElementsFactory.html#createFeatureChaining()">createFeatureChaining</a>, <a href="KerMLElementsFactory.html#createFeatureInverting()">createFeatureInverting</a>, <a href="KerMLElementsFactory.html#createFeatureMembership()">createFeatureMembership</a>, <a href="KerMLElementsFactory.html#createFeatureReferenceExpression()">createFeatureReferenceExpression</a>, <a href="KerMLElementsFactory.html#createFeatureTyping()">createFeatureTyping</a>, <a href="KerMLElementsFactory.html#createFeatureValue()">createFeatureValue</a>, <a href="KerMLElementsFactory.html#createFlow()">createFlow</a>, <a href="KerMLElementsFactory.html#createFlowEnd()">createFlowEnd</a>, <a href="KerMLElementsFactory.html#createFunction()">createFunction</a>, <a href="KerMLElementsFactory.html#createIndexExpression()">createIndexExpression</a>, <a href="KerMLElementsFactory.html#createInteraction()">createInteraction</a>, <a href="KerMLElementsFactory.html#createIntersecting()">createIntersecting</a>, <a href="KerMLElementsFactory.html#createInvariant()">createInvariant</a>, <a href="KerMLElementsFactory.html#createInvocationExpression()">createInvocationExpression</a>, <a href="KerMLElementsFactory.html#createLibraryPackage()">createLibraryPackage</a>, <a href="KerMLElementsFactory.html#createLiteralBoolean()">createLiteralBoolean</a>, <a href="KerMLElementsFactory.html#createLiteralExpression()">createLiteralExpression</a>, <a href="KerMLElementsFactory.html#createLiteralInfinity()">createLiteralInfinity</a>, <a href="KerMLElementsFactory.html#createLiteralInteger()">createLiteralInteger</a>, <a href="KerMLElementsFactory.html#createLiteralRational()">createLiteralRational</a>, <a href="KerMLElementsFactory.html#createLiteralString()">createLiteralString</a>, <a href="KerMLElementsFactory.html#createMembership()">createMembership</a>, <a href="KerMLElementsFactory.html#createMembershipImport()">createMembershipImport</a>, <a href="KerMLElementsFactory.html#createMetaclass()">createMetaclass</a>, <a href="KerMLElementsFactory.html#createMetadataAccessExpression()">createMetadataAccessExpression</a>, <a href="KerMLElementsFactory.html#createMetadataFeature()">createMetadataFeature</a>, <a href="KerMLElementsFactory.html#createMultiplicity()">createMultiplicity</a>, <a href="KerMLElementsFactory.html#createMultiplicityRange()">createMultiplicityRange</a>, <a href="KerMLElementsFactory.html#createNamespace()">createNamespace</a>, <a href="KerMLElementsFactory.html#createNamespaceImport()">createNamespaceImport</a>, <a href="KerMLElementsFactory.html#createNullExpression()">createNullExpression</a>, <a href="KerMLElementsFactory.html#createOperatorExpression()">createOperatorExpression</a>, <a href="KerMLElementsFactory.html#createOwningMembership()">createOwningMembership</a>, <a href="KerMLElementsFactory.html#createPackage()">createPackage</a>, <a href="KerMLElementsFactory.html#createParameterMembership()">createParameterMembership</a>, <a href="KerMLElementsFactory.html#createPayloadFeature()">createPayloadFeature</a>, <a href="KerMLElementsFactory.html#createPredicate()">createPredicate</a>, <a href="KerMLElementsFactory.html#createRedefinition()">createRedefinition</a>, <a href="KerMLElementsFactory.html#createReferenceSubsetting()">createReferenceSubsetting</a>, <a href="KerMLElementsFactory.html#createResultExpressionMembership()">createResultExpressionMembership</a>, <a href="KerMLElementsFactory.html#createReturnParameterMembership()">createReturnParameterMembership</a>, <a href="KerMLElementsFactory.html#createSelectExpression()">createSelectExpression</a>, <a href="KerMLElementsFactory.html#createSpecialization()">createSpecialization</a>, <a href="KerMLElementsFactory.html#createStep()">createStep</a>, <a href="KerMLElementsFactory.html#createStructure()">createStructure</a>, <a href="KerMLElementsFactory.html#createSubclassification()">createSubclassification</a>, <a href="KerMLElementsFactory.html#createSubsetting()">createSubsetting</a>, <a href="KerMLElementsFactory.html#createSuccession()">createSuccession</a>, <a href="KerMLElementsFactory.html#createSuccessionFlow()">createSuccessionFlow</a>, <a href="KerMLElementsFactory.html#createTextualRepresentation()">createTextualRepresentation</a>, <a href="KerMLElementsFactory.html#createType()">createType</a>, <a href="KerMLElementsFactory.html#createTypeFeaturing()">createTypeFeaturing</a>, <a href="KerMLElementsFactory.html#createUnioning()">createUnioning</a></code></div>
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
<section class="detail" id="get(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>get</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">ElementsFactory</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Gets a factory for the given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project context</dd>
<dt>Returns:</dt>
<dd>elements factory bound to the project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="get(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>get</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">ElementsFactory</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Gets a factory using the project of the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to resolve project from</dd>
<dt>Returns:</dt>
<dd>elements factory bound to the element's project</dd>
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
