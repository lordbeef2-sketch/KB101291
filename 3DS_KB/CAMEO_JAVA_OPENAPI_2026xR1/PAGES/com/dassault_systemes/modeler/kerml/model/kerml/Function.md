# JAVA OPENAPI: Function (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Function.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Function.html`
- source_sha256: `b766c880f0084d5aa8775086f8d6a915daeb16ff7ee4a117fefbf99d3332d1f1`
- captured_utc: `2026-07-14T16:44:49.079857+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Function

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Behavior](Behavior.html)`, `[Class](Class.html)`, `[Classifier](Classifier.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `[Namespace](Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[Type](Type.html)`

All Known Subinterfaces:
`[AnalysisCaseDefinition](../../../sysml/model/sysml/AnalysisCaseDefinition.html)`, `[CalculationDefinition](../../../sysml/model/sysml/CalculationDefinition.html)`, `[CaseDefinition](../../../sysml/model/sysml/CaseDefinition.html)`, `[ConcernDefinition](../../../sysml/model/sysml/ConcernDefinition.html)`, `[ConstraintDefinition](../../../sysml/model/sysml/ConstraintDefinition.html)`, `[Predicate](Predicate.html)`, `[RequirementDefinition](../../../sysml/model/sysml/RequirementDefinition.html)`, `[UseCaseDefinition](../../../sysml/model/sysml/UseCaseDefinition.html)`, `[VerificationCaseDefinition](../../../sysml/model/sysml/VerificationCaseDefinition.html)`, `[ViewpointDefinition](../../../sysml/model/sysml/ViewpointDefinition.html)`

@OpenApiAllpublic interfaceFunctionextends [Behavior](Behavior.html)

A `Function` is a `Behavior` that has an `out` `parameter` that is identified as its `result`. A `Function` represents the performance of a calculation that produces the values of its `result` `parameter`. This calculation may be decomposed into `Expressions` that are `steps` of the `Function`.
 
 featureMembership->
 selectByKind(ReturnParameterMembership)->
 size() = 1
 specializesFromLibrary('Performances::Evaluation')
 ownedMembership.selectByKind(ResultExpressionMembership)->
 forAll(mem | ownedFeature.selectByKind(BindingConnector)->
 exists(binding |
 binding.relatedFeature->includes(result) and
 binding.relatedFeature->includes(mem.ownedResultExpression.result)))
 result =
 let resultParams : Sequence(Feature) =
 featureMemberships->
 selectByKind(ReturnParameterMembership).
 ownedMemberParameter in
 if resultParams->notEmpty() then resultParams->first()
 else null
 endif
 membership->selectByKind(ResultExpressionMembership)->size() <= 1

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Expression](Expression.html)>`
`[getExpression](#getExpression())()`
The `Expressions` that are `steps` in the calculation of the `result` of this `Function`.
`[Feature](Feature.html)`
`[getResult](#getResult())()`
The object or value that is the result of evaluating the Function.
`boolean`
`[isModelLevelEvaluable](#isModelLevelEvaluable())()`
Whether this `Function` can be used as the `function` of a model-level evaluable `InvocationExpression`.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Behavior](Behavior.html)
`[getParameter](Behavior.html#getParameter()), [getStep](Behavior.html#getStep())`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Classifier](Classifier.html)
`[getOwnedSubclassification](Classifier.html#getOwnedSubclassification())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](Element.html)
`[effectiveName](Element.html#effectiveName()), [effectiveShortName](Element.html#effectiveShortName()), [escapedName](Element.html#escapedName()), [getAliasIds](Element.html#getAliasIds()), [getDeclaredName](Element.html#getDeclaredName()), [getDeclaredShortName](Element.html#getDeclaredShortName()), [getDocumentation](Element.html#getDocumentation()), [getElementId](Element.html#getElementId()), [getName](Element.html#getName()), [getOwnedAnnotation](Element.html#getOwnedAnnotation()), [getOwnedElement](Element.html#getOwnedElement()), [getOwnedRelationship](Element.html#getOwnedRelationship()), [getOwner](Element.html#getOwner()), [getOwningMembership](Element.html#getOwningMembership()), [getOwningNamespace](Element.html#getOwningNamespace()), [getOwningRelationship](Element.html#getOwningRelationship()), [getQualifiedName](Element.html#getQualifiedName()), [getShortName](Element.html#getShortName()), [getTextualRepresentation](Element.html#getTextualRepresentation()), [isImpliedIncluded](Element.html#isImpliedIncluded()), [isLibraryElement](Element.html#isLibraryElement()), [libraryNamespace](Element.html#libraryNamespace()), [path](Element.html#path()), [setDeclaredName](Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](Element.html#setDeclaredShortName(java.lang.String)), [setElementId](Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](Element.html#setIsImpliedIncluded(boolean)), [setOwner](Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject
`getModelExtension, getModelExtension`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Namespace](Namespace.html)
`[getImportedMembership](Namespace.html#getImportedMembership()), [getMember](Namespace.html#getMember()), [getMembership](Namespace.html#getMembership()), [getOwnedImport](Namespace.html#getOwnedImport()), [getOwnedMember](Namespace.html#getOwnedMember()), [getOwnedMembership](Namespace.html#getOwnedMembership()), [importedMemberships](Namespace.html#importedMemberships(java.util.List)), [membershipsOfVisibility](Namespace.html#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)), [namesOf](Namespace.html#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [qualificationOf](Namespace.html#qualificationOf(java.lang.String)), [resolve](Namespace.html#resolve(java.lang.String)), [resolveGlobal](Namespace.html#resolveGlobal(java.lang.String)), [resolveLocal](Namespace.html#resolveLocal(java.lang.String)), [resolveVisible](Namespace.html#resolveVisible(java.lang.String)), [unqualifiedNameOf](Namespace.html#unqualifiedNameOf(java.lang.String)), [visibilityOf](Namespace.html#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Type](Type.html)
`[allRedefinedFeaturesOf](Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)), [allSupertypes](Type.html#allSupertypes()), [directionOf](Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [directionOfExcluding](Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)), [getDifferencingType](Type.html#getDifferencingType()), [getDirectedFeature](Type.html#getDirectedFeature()), [getEndFeature](Type.html#getEndFeature()), [getFeature](Type.html#getFeature()), [getFeatureMembership](Type.html#getFeatureMembership()), [getInheritedFeature](Type.html#getInheritedFeature()), [getInheritedMembership](Type.html#getInheritedMembership()), [getInput](Type.html#getInput()), [getIntersectingType](Type.html#getIntersectingType()), [getMultiplicity](Type.html#getMultiplicity()), [getOutput](Type.html#getOutput()), [getOwnedConjugator](Type.html#getOwnedConjugator()), [getOwnedDifferencing](Type.html#getOwnedDifferencing()), [getOwnedDisjoining](Type.html#getOwnedDisjoining()), [getOwnedEndFeature](Type.html#getOwnedEndFeature()), [getOwnedFeature](Type.html#getOwnedFeature()), [getOwnedFeatureMembership](Type.html#getOwnedFeatureMembership()), [getOwnedIntersecting](Type.html#getOwnedIntersecting()), [getOwnedSpecialization](Type.html#getOwnedSpecialization()), [getOwnedUnioning](Type.html#getOwnedUnioning()), [getUnioningType](Type.html#getUnioningType()), [inheritableMemberships](Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)), [inheritedMemberships](Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)), [isAbstract](Type.html#isAbstract()), [isCompatibleWith](Type.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isConjugated](Type.html#isConjugated()), [isSufficient](Type.html#isSufficient()), [multiplicities](Type.html#multiplicities()), [nonPrivateMemberships](Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)), [removeRedefinedFeatures](Type.html#removeRedefinedFeatures(java.util.List)), [setIsAbstract](Type.html#setIsAbstract(boolean)), [setIsSufficient](Type.html#setIsSufficient(boolean)), [specializes](Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [specializesFromLibrary](Type.html#specializesFromLibrary(java.lang.String)), [supertypes](Type.html#supertypes(boolean)), [visibleMemberships](Type.html#visibleMemberships(java.util.List,boolean,boolean))`

============ METHOD DETAIL ========== 
Method Details
getExpression
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Expression](Expression.html)> getExpression()
The `Expressions` that are `steps` in the calculation of the `result` of this `Function`.
The set of expressions that represent computational steps or parts of a system of equations within the Function.
Returns:
the expression value
Model:
derived="true"
 transient="true"
 oppositeRoleName="computedFunction"
 subsets=[`Behavior.getStep()`](Behavior.html#getStep())
getResult
@CheckForNull[Feature](Feature.html) getResult()
The object or value that is the result of evaluating the Function.
The `result` `parameter` of the `Function`, which is owned by the `Function` via a `ReturnParameterMembership`.
Returns:
the result value
Model:
derived="true"
 transient="true"
 oppositeRoleName="computingFunction"
 subsets=[`Type.getOutput()`](Type.html#getOutput()), [`Behavior.getParameter()`](Behavior.html#getParameter())
isModelLevelEvaluable
boolean isModelLevelEvaluable()
Whether this `Function` can be used as the `function` of a model-level evaluable `InvocationExpression`. Certain `Functions` from the Kernel Functions Library are considered to have `isModelLevelEvaluable = true`. For all other `Functions` it is `false`.
**Note:** See the specification of the KerML concrete syntax notation for `Expressions` for an identification of which library `Functions` are model-level evaluable.
Returns:
the isModelLevelEvaluable value
Model:
derived="true"
 transient="true"

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Function">Interface Function</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Behavior</a></code>, <code><a href="Class.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Class</a></code>, <code><a href="Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../sysml/model/sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/CalculationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationDefinition</a></code>, <code><a href="../../../sysml/model/sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConcernDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintDefinition</a></code>, <code><a href="Predicate.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Predicate</a></code>, <code><a href="../../../sysml/model/sysml/RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementDefinition</a></code>, <code><a href="../../../sysml/model/sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointDefinition</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Function</span><span class="extends-implements">
extends <a href="Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Behavior</a></span></div>
<div class="block"><p>A <code>Function</code> is a <code>Behavior</code> that has an <code>out</code> <code>parameter</code> that is identified as its <code>result</code>. A <code>Function</code> represents the performance of a calculation that produces the values of its <code>result</code> <code>parameter</code>. This calculation may be decomposed into <code>Expressions</code> that are <code>steps</code> of the <code>Function</code>.</p>
 
 featureMembership-&gt;
     selectByKind(ReturnParameterMembership)-&gt;
     size() = 1
 specializesFromLibrary('Performances::Evaluation')
 ownedMembership.selectByKind(ResultExpressionMembership)-&gt;
     forAll(mem | ownedFeature.selectByKind(BindingConnector)-&gt;
         exists(binding |
             binding.relatedFeature-&gt;includes(result) and
             binding.relatedFeature-&gt;includes(mem.ownedResultExpression.result)))
 result =
     let resultParams : Sequence(Feature) =
         featureMemberships-&gt;
             selectByKind(ReturnParameterMembership).
             ownedMemberParameter in
     if resultParams-&gt;notEmpty() then resultParams-&gt;first()
     else null
     endif
 membership-&gt;selectByKind(ResultExpressionMembership)-&gt;size() &lt;= 1</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExpression()">getExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Expressions</code> that are <code>steps</code> in the calculation of the <code>result</code> of this <code>Function</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getResult()">getResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The object or value that is the result of evaluating the Function.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isModelLevelEvaluable()">isModelLevelEvaluable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this <code>Function</code> can be used as the <code>function</code> of a model-level evaluable <code>InvocationExpression</code>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()">getID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)">setID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Behavior">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Behavior</a></h3>
<code><a href="Behavior.html#getParameter()">getParameter</a>, <a href="Behavior.html#getStep()">getStep</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Classifier">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a></h3>
<code><a href="Classifier.html#getOwnedSubclassification()">getOwnedSubclassification</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Element">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></h3>
<code><a href="Element.html#effectiveName()">effectiveName</a>, <a href="Element.html#effectiveShortName()">effectiveShortName</a>, <a href="Element.html#escapedName()">escapedName</a>, <a href="Element.html#getAliasIds()">getAliasIds</a>, <a href="Element.html#getDeclaredName()">getDeclaredName</a>, <a href="Element.html#getDeclaredShortName()">getDeclaredShortName</a>, <a href="Element.html#getDocumentation()">getDocumentation</a>, <a href="Element.html#getElementId()">getElementId</a>, <a href="Element.html#getName()">getName</a>, <a href="Element.html#getOwnedAnnotation()">getOwnedAnnotation</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwnedRelationship()">getOwnedRelationship</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getOwningMembership()">getOwningMembership</a>, <a href="Element.html#getOwningNamespace()">getOwningNamespace</a>, <a href="Element.html#getOwningRelationship()">getOwningRelationship</a>, <a href="Element.html#getQualifiedName()">getQualifiedName</a>, <a href="Element.html#getShortName()">getShortName</a>, <a href="Element.html#getTextualRepresentation()">getTextualRepresentation</a>, <a href="Element.html#isImpliedIncluded()">isImpliedIncluded</a>, <a href="Element.html#isLibraryElement()">isLibraryElement</a>, <a href="Element.html#libraryNamespace()">libraryNamespace</a>, <a href="Element.html#path()">path</a>, <a href="Element.html#setDeclaredName(java.lang.String)">setDeclaredName</a>, <a href="Element.html#setDeclaredShortName(java.lang.String)">setDeclaredShortName</a>, <a href="Element.html#setElementId(java.lang.String)">setElementId</a>, <a href="Element.html#setIsImpliedIncluded(boolean)">setIsImpliedIncluded</a>, <a href="Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwner</a>, <a href="Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">setOwningMembership</a>, <a href="Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">setOwningRelationship</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.<a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></h3>
<code><a href="../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">canChangeElementOwner</a>, <a href="../../../foundation/model/ModelElement.html#dispose()">dispose</a>, <a href="../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)">eDynamicGet</a>, <a href="../../../foundation/model/ModelElement.html#getElementOwner()">getElementOwner</a>, <a href="../../../foundation/model/ModelElement.html#getLocalID()">getLocalID</a>, <a href="../../../foundation/model/ModelElement.html#getObjectParent()">getObjectParent</a>, <a href="../../../foundation/model/ModelElement.html#selfDispose()">selfDispose</a>, <a href="../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)">setLocalID</a>, <a href="../../../foundation/model/ModelElement.html#sGetLocalID()">sGetLocalID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject">Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</h3>
<code>getModelExtension, getModelExtension</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Namespace">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></h3>
<code><a href="Namespace.html#getImportedMembership()">getImportedMembership</a>, <a href="Namespace.html#getMember()">getMember</a>, <a href="Namespace.html#getMembership()">getMembership</a>, <a href="Namespace.html#getOwnedImport()">getOwnedImport</a>, <a href="Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="Namespace.html#getOwnedMembership()">getOwnedMembership</a>, <a href="Namespace.html#importedMemberships(java.util.List)">importedMemberships</a>, <a href="Namespace.html#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)">membershipsOfVisibility</a>, <a href="Namespace.html#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)">namesOf</a>, <a href="Namespace.html#qualificationOf(java.lang.String)">qualificationOf</a>, <a href="Namespace.html#resolve(java.lang.String)">resolve</a>, <a href="Namespace.html#resolveGlobal(java.lang.String)">resolveGlobal</a>, <a href="Namespace.html#resolveLocal(java.lang.String)">resolveLocal</a>, <a href="Namespace.html#resolveVisible(java.lang.String)">resolveVisible</a>, <a href="Namespace.html#unqualifiedNameOf(java.lang.String)">unqualifiedNameOf</a>, <a href="Namespace.html#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">visibilityOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Type">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></h3>
<code><a href="Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">allRedefinedFeaturesOf</a>, <a href="Type.html#allSupertypes()">allSupertypes</a>, <a href="Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">directionOf</a>, <a href="Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">directionOfExcluding</a>, <a href="Type.html#getDifferencingType()">getDifferencingType</a>, <a href="Type.html#getDirectedFeature()">getDirectedFeature</a>, <a href="Type.html#getEndFeature()">getEndFeature</a>, <a href="Type.html#getFeature()">getFeature</a>, <a href="Type.html#getFeatureMembership()">getFeatureMembership</a>, <a href="Type.html#getInheritedFeature()">getInheritedFeature</a>, <a href="Type.html#getInheritedMembership()">getInheritedMembership</a>, <a href="Type.html#getInput()">getInput</a>, <a href="Type.html#getIntersectingType()">getIntersectingType</a>, <a href="Type.html#getMultiplicity()">getMultiplicity</a>, <a href="Type.html#getOutput()">getOutput</a>, <a href="Type.html#getOwnedConjugator()">getOwnedConjugator</a>, <a href="Type.html#getOwnedDifferencing()">getOwnedDifferencing</a>, <a href="Type.html#getOwnedDisjoining()">getOwnedDisjoining</a>, <a href="Type.html#getOwnedEndFeature()">getOwnedEndFeature</a>, <a href="Type.html#getOwnedFeature()">getOwnedFeature</a>, <a href="Type.html#getOwnedFeatureMembership()">getOwnedFeatureMembership</a>, <a href="Type.html#getOwnedIntersecting()">getOwnedIntersecting</a>, <a href="Type.html#getOwnedSpecialization()">getOwnedSpecialization</a>, <a href="Type.html#getOwnedUnioning()">getOwnedUnioning</a>, <a href="Type.html#getUnioningType()">getUnioningType</a>, <a href="Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)">inheritableMemberships</a>, <a href="Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)">inheritedMemberships</a>, <a href="Type.html#isAbstract()">isAbstract</a>, <a href="Type.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isCompatibleWith</a>, <a href="Type.html#isConjugated()">isConjugated</a>, <a href="Type.html#isSufficient()">isSufficient</a>, <a href="Type.html#multiplicities()">multiplicities</a>, <a href="Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)">nonPrivateMemberships</a>, <a href="Type.html#removeRedefinedFeatures(java.util.List)">removeRedefinedFeatures</a>, <a href="Type.html#setIsAbstract(boolean)">setIsAbstract</a>, <a href="Type.html#setIsSufficient(boolean)">setIsSufficient</a>, <a href="Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">specializes</a>, <a href="Type.html#specializesFromLibrary(java.lang.String)">specializesFromLibrary</a>, <a href="Type.html#supertypes(boolean)">supertypes</a>, <a href="Type.html#visibleMemberships(java.util.List,boolean,boolean)">visibleMemberships</a></code></div>
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
<section class="detail" id="getExpression()">
<h3>getExpression</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt;</span> <span class="element-name">getExpression</span>()</div>
<div class="block"><p>The <code>Expressions</code> that are <code>steps</code> in the calculation of the <code>result</code> of this <code>Function</code>.</p>
<p>The set of expressions that represent computational steps or parts of a system of equations within the Function.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the expression value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="computedFunction"
        subsets=<a href="Behavior.html#getStep()"><code>Behavior.getStep()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResult()">
<h3>getResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getResult</span>()</div>
<div class="block"><p>The object or value that is the result of evaluating the Function.</p>
<p>The <code>result</code> <code>parameter</code> of the <code>Function</code>, which is owned by the <code>Function</code> via a <code>ReturnParameterMembership</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the result value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="computingFunction"
        subsets=<a href="Type.html#getOutput()"><code>Type.getOutput()</code></a>, <a href="Behavior.html#getParameter()"><code>Behavior.getParameter()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isModelLevelEvaluable()">
<h3>isModelLevelEvaluable</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isModelLevelEvaluable</span>()</div>
<div class="block"><p>Whether this <code>Function</code> can be used as the <code>function</code> of a model-level evaluable <code>InvocationExpression</code>. Certain <code>Functions</code> from the Kernel Functions Library are considered to have <code>isModelLevelEvaluable = true</code>. For all other <code>Functions</code> it is <code>false</code>.</p>
<p><strong>Note:</strong> See the specification of the KerML concrete syntax notation for <code>Expressions</code> for an identification of which library <code>Functions</code> are model-level evaluable.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isModelLevelEvaluable value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"</dd>
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
