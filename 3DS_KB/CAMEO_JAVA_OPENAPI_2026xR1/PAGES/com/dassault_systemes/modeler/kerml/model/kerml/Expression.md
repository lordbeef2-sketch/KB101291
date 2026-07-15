# JAVA OPENAPI: Expression (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Expression.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Expression.html`
- source_sha256: `f9942ed1d76c113ec2e1d8579694a8a50995c275814e63c3ce791979aa2d5f74`
- captured_utc: `2026-07-14T16:44:48.862854+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Expression

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[Feature](Feature.html)`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `[Namespace](Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[Step](Step.html)`, `[Type](Type.html)`

All Known Subinterfaces:
`[AnalysisCaseUsage](../../../sysml/model/sysml/AnalysisCaseUsage.html)`, `[AssertConstraintUsage](../../../sysml/model/sysml/AssertConstraintUsage.html)`, `[BooleanExpression](BooleanExpression.html)`, `[CalculationUsage](../../../sysml/model/sysml/CalculationUsage.html)`, `[CaseUsage](../../../sysml/model/sysml/CaseUsage.html)`, `[CollectExpression](CollectExpression.html)`, `[ConcernUsage](../../../sysml/model/sysml/ConcernUsage.html)`, `[ConstraintUsage](../../../sysml/model/sysml/ConstraintUsage.html)`, `[ConstructorExpression](ConstructorExpression.html)`, `[FeatureChainExpression](FeatureChainExpression.html)`, `[FeatureReferenceExpression](FeatureReferenceExpression.html)`, `[IncludeUseCaseUsage](../../../sysml/model/sysml/IncludeUseCaseUsage.html)`, `[IndexExpression](IndexExpression.html)`, `[InstantiationExpression](InstantiationExpression.html)`, `[Invariant](Invariant.html)`, `[InvocationExpression](InvocationExpression.html)`, `[LiteralBoolean](LiteralBoolean.html)`, `[LiteralExpression](LiteralExpression.html)`, `[LiteralInfinity](LiteralInfinity.html)`, `[LiteralInteger](LiteralInteger.html)`, `[LiteralRational](LiteralRational.html)`, `[LiteralString](LiteralString.html)`, `[MetadataAccessExpression](MetadataAccessExpression.html)`, `[NullExpression](NullExpression.html)`, `[OperatorExpression](OperatorExpression.html)`, `[RequirementUsage](../../../sysml/model/sysml/RequirementUsage.html)`, `[SatisfyRequirementUsage](../../../sysml/model/sysml/SatisfyRequirementUsage.html)`, `[SelectExpression](SelectExpression.html)`, `[TriggerInvocationExpression](../../../sysml/model/sysml/TriggerInvocationExpression.html)`, `[UseCaseUsage](../../../sysml/model/sysml/UseCaseUsage.html)`, `[VerificationCaseUsage](../../../sysml/model/sysml/VerificationCaseUsage.html)`, `[ViewpointUsage](../../../sysml/model/sysml/ViewpointUsage.html)`

@OpenApiAllpublic interfaceExpressionextends [Step](Step.html)

An `Expression` is a `Step` that is typed by a `Function`. An `Expression` that also has a `Function` as its `featuringType` is a computational step within that `Function`. An `Expression` always has a single `result` parameter, which redefines the `result` parameter of its defining `function`. This allows `Expressions` to be interconnected in tree structures, in which inputs to each `Expression` in the tree are determined as the results of other `Expression` in the tree.
 
 isModelLevelEvaluable = modelLevelEvaluable(Set(Element){})
 specializesFromLibrary('Performances::evaluations')
 owningMembership <> null and 
 owningMembership.oclIsKindOf(FeatureValue) implies
 let featureWithValue : Feature = 
 owningMembership.oclAsType(FeatureValue).featureWithValue in
 featuringType = featureWithValue.featuringType
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
 
 featureMembership->
 selectByKind(ReturnParameterMembership)->
 size() = 1
 membership->selectByKind(ResultExpressionMembership)->size() <= 1

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[checkCondition](#checkCondition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](Element.html) target)`
Model-level evaluate this `Expression` with the given `target`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)>`
`[evaluate](#evaluate(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](Element.html) target)`
If this `Expression` `isModelLevelEvaluable`, then evaluate it using the `target` as the context `Element` for resolving `Feature` names and testing classification.
`[Function](Function.html)`
`[getFunction](#getFunction())()`
The `Function` that types this `Expression`.
`[Feature](Feature.html)`
`[getResult](#getResult())()`

`boolean`
`[isModelLevelEvaluable](#isModelLevelEvaluable())()`
Whether this `Expression` meets the constraints necessary to be evaluated at *model level*, that is, using metadata within the model.
`boolean`
`[modelLevelEvaluable](#modelLevelEvaluable(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> visited)`
Return whether this `Expression` is model-level evaluable.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](Element.html)
`[escapedName](Element.html#escapedName()), [getAliasIds](Element.html#getAliasIds()), [getDeclaredName](Element.html#getDeclaredName()), [getDeclaredShortName](Element.html#getDeclaredShortName()), [getDocumentation](Element.html#getDocumentation()), [getElementId](Element.html#getElementId()), [getName](Element.html#getName()), [getOwnedAnnotation](Element.html#getOwnedAnnotation()), [getOwnedElement](Element.html#getOwnedElement()), [getOwnedRelationship](Element.html#getOwnedRelationship()), [getOwner](Element.html#getOwner()), [getOwningMembership](Element.html#getOwningMembership()), [getOwningNamespace](Element.html#getOwningNamespace()), [getOwningRelationship](Element.html#getOwningRelationship()), [getQualifiedName](Element.html#getQualifiedName()), [getShortName](Element.html#getShortName()), [getTextualRepresentation](Element.html#getTextualRepresentation()), [isImpliedIncluded](Element.html#isImpliedIncluded()), [isLibraryElement](Element.html#isLibraryElement()), [libraryNamespace](Element.html#libraryNamespace()), [path](Element.html#path()), [setDeclaredName](Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](Element.html#setDeclaredShortName(java.lang.String)), [setElementId](Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](Element.html#setIsImpliedIncluded(boolean)), [setOwner](Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Feature](Feature.html)
`[allRedefinedFeatures](Feature.html#allRedefinedFeatures()), [asCartesianProduct](Feature.html#asCartesianProduct()), [canAccess](Feature.html#canAccess(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [directionFor](Feature.html#directionFor(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [effectiveName](Feature.html#effectiveName()), [effectiveShortName](Feature.html#effectiveShortName()), [getChainingFeature](Feature.html#getChainingFeature()), [getCrossFeature](Feature.html#getCrossFeature()), [getDirection](Feature.html#getDirection()), [getEndOwningType](Feature.html#getEndOwningType()), [getFeatureTarget](Feature.html#getFeatureTarget()), [getFeaturingType](Feature.html#getFeaturingType()), [getOwnedCrossSubsetting](Feature.html#getOwnedCrossSubsetting()), [getOwnedFeatureChaining](Feature.html#getOwnedFeatureChaining()), [getOwnedFeatureInverting](Feature.html#getOwnedFeatureInverting()), [getOwnedRedefinition](Feature.html#getOwnedRedefinition()), [getOwnedReferenceSubsetting](Feature.html#getOwnedReferenceSubsetting()), [getOwnedSubsetting](Feature.html#getOwnedSubsetting()), [getOwnedTypeFeaturing](Feature.html#getOwnedTypeFeaturing()), [getOwnedTyping](Feature.html#getOwnedTyping()), [getOwningFeatureMembership](Feature.html#getOwningFeatureMembership()), [getOwningType](Feature.html#getOwningType()), [getType](Feature.html#getType()), [isCartesianProduct](Feature.html#isCartesianProduct()), [isCompatibleWith](Feature.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isComposite](Feature.html#isComposite()), [isConstant](Feature.html#isConstant()), [isDerived](Feature.html#isDerived()), [isEnd](Feature.html#isEnd()), [isFeaturedWithin](Feature.html#isFeaturedWithin(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isFeaturingType](Feature.html#isFeaturingType(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isOrdered](Feature.html#isOrdered()), [isOwnedCrossFeature](Feature.html#isOwnedCrossFeature()), [isPortion](Feature.html#isPortion()), [isUnique](Feature.html#isUnique()), [isVariable](Feature.html#isVariable()), [namingFeature](Feature.html#namingFeature()), [ownedCrossFeature](Feature.html#ownedCrossFeature()), [redefines](Feature.html#redefines(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [redefinesFromLibrary](Feature.html#redefinesFromLibrary(java.lang.String)), [setDirection](Feature.html#setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)), [setIsComposite](Feature.html#setIsComposite(boolean)), [setIsConstant](Feature.html#setIsConstant(boolean)), [setIsDerived](Feature.html#setIsDerived(boolean)), [setIsEnd](Feature.html#setIsEnd(boolean)), [setIsOrdered](Feature.html#setIsOrdered(boolean)), [setIsPortion](Feature.html#setIsPortion(boolean)), [setIsUnique](Feature.html#setIsUnique(boolean)), [setIsVariable](Feature.html#setIsVariable(boolean)), [subsetsChain](Feature.html#subsetsChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [supertypes](Feature.html#supertypes(boolean)), [typingFeatures](Feature.html#typingFeatures())`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject
`getModelExtension, getModelExtension`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Namespace](Namespace.html)
`[getImportedMembership](Namespace.html#getImportedMembership()), [getMember](Namespace.html#getMember()), [getMembership](Namespace.html#getMembership()), [getOwnedImport](Namespace.html#getOwnedImport()), [getOwnedMember](Namespace.html#getOwnedMember()), [getOwnedMembership](Namespace.html#getOwnedMembership()), [importedMemberships](Namespace.html#importedMemberships(java.util.List)), [membershipsOfVisibility](Namespace.html#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)), [namesOf](Namespace.html#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [qualificationOf](Namespace.html#qualificationOf(java.lang.String)), [resolve](Namespace.html#resolve(java.lang.String)), [resolveGlobal](Namespace.html#resolveGlobal(java.lang.String)), [resolveLocal](Namespace.html#resolveLocal(java.lang.String)), [resolveVisible](Namespace.html#resolveVisible(java.lang.String)), [unqualifiedNameOf](Namespace.html#unqualifiedNameOf(java.lang.String)), [visibilityOf](Namespace.html#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Step](Step.html)
`[getBehavior](Step.html#getBehavior()), [getParameter](Step.html#getParameter())`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Type](Type.html)
`[allRedefinedFeaturesOf](Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)), [allSupertypes](Type.html#allSupertypes()), [directionOf](Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [directionOfExcluding](Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)), [getDifferencingType](Type.html#getDifferencingType()), [getDirectedFeature](Type.html#getDirectedFeature()), [getEndFeature](Type.html#getEndFeature()), [getFeature](Type.html#getFeature()), [getFeatureMembership](Type.html#getFeatureMembership()), [getInheritedFeature](Type.html#getInheritedFeature()), [getInheritedMembership](Type.html#getInheritedMembership()), [getInput](Type.html#getInput()), [getIntersectingType](Type.html#getIntersectingType()), [getMultiplicity](Type.html#getMultiplicity()), [getOutput](Type.html#getOutput()), [getOwnedConjugator](Type.html#getOwnedConjugator()), [getOwnedDifferencing](Type.html#getOwnedDifferencing()), [getOwnedDisjoining](Type.html#getOwnedDisjoining()), [getOwnedEndFeature](Type.html#getOwnedEndFeature()), [getOwnedFeature](Type.html#getOwnedFeature()), [getOwnedFeatureMembership](Type.html#getOwnedFeatureMembership()), [getOwnedIntersecting](Type.html#getOwnedIntersecting()), [getOwnedSpecialization](Type.html#getOwnedSpecialization()), [getOwnedUnioning](Type.html#getOwnedUnioning()), [getUnioningType](Type.html#getUnioningType()), [inheritableMemberships](Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)), [inheritedMemberships](Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)), [isAbstract](Type.html#isAbstract()), [isConjugated](Type.html#isConjugated()), [isSufficient](Type.html#isSufficient()), [multiplicities](Type.html#multiplicities()), [nonPrivateMemberships](Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)), [removeRedefinedFeatures](Type.html#removeRedefinedFeatures(java.util.List)), [setIsAbstract](Type.html#setIsAbstract(boolean)), [setIsSufficient](Type.html#setIsSufficient(boolean)), [specializes](Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [specializesFromLibrary](Type.html#specializesFromLibrary(java.lang.String)), [visibleMemberships](Type.html#visibleMemberships(java.util.List,boolean,boolean))`

============ METHOD DETAIL ========== 
Method Details
getFunction
@CheckForNull[Function](Function.html) getFunction()
The `Function` that types this `Expression`.
This is the Function that types the Expression.
Returns:
the function value
Model:
derived="true"
 transient="true"
 oppositeRoleName="typedExpression"
 redefines=[`Step.getBehavior()`](Step.html#getBehavior())
getResult
@CheckForNull[Feature](Feature.html) getResult()
An `output` `parameter` of the `Expression` whose value is the result of the `Expression`. The result of an `Expression` is either inherited from its `function` or it is related to the `Expression` via a `ReturnParameterMembership`, in which case it redefines the `result` `parameter` of its `function`.
Returns:
the result value
Model:
derived="true"
 transient="true"
 oppositeRoleName="computingExpression"
 subsets=[`Type.getOutput()`](Type.html#getOutput()), [`Step.getParameter()`](Step.html#getParameter())
isModelLevelEvaluable
boolean isModelLevelEvaluable()
Whether this `Expression` meets the constraints necessary to be evaluated at *model level*, that is, using metadata within the model.
Returns:
the isModelLevelEvaluable value
Model:
derived="true"
 transient="true"
modelLevelEvaluable
boolean modelLevelEvaluable([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> visited)
Return whether this `Expression` is model-level evaluable. The `visited` parameter is used to track possible circular `Feature` references made from `FeatureReferenceExpressions` (see the redefinition of this operation for `FeatureReferenceExpression`). Such circular references are not allowed in model-level evaluable expressions.
An `Expression` that is not otherwise specialized is model-level evaluable if it has no (non-implied) `ownedSpecializations` and all its `ownedFeatures` are either `in` parameters, the `result` `parameter` or a result `Expression` owned via a `ResultExpressionMembership`. The `parameters` must not have any `ownedFeatures` or a `FeatureValue`, and the result `Expression` must be model-level evaluable.
 ownedSpecialization->forAll(isImplied) and 
 ownedFeature->forAll(f |
 (directionOf(f) = FeatureDirectionKind::_'in' or f = result) and
 f.ownedFeature->isEmpty() and f.valuation = null or
 f.owningFeatureMembership.oclIsKindOf(ResultExpressionMembership) and
 f.oclAsType(Expression).modelLevelEvaluable(visited)
evaluate
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)> evaluate([Element](Element.html) target)
If this `Expression` `isModelLevelEvaluable`, then evaluate it using the `target` as the context `Element` for resolving `Feature` names and testing classification. The result is a collection of `Elements`, which, for a fully evaluable `Expression`, will be a `LiteralExpression` or a `Feature` that is not an `Expression`.
 isModelLevelEvaluable
 let resultExprs : Sequence(Expression) =
 ownedFeatureMembership->
 selectByKind(ResultExpressionMembership).
 ownedResultExpression in
 if resultExpr->isEmpty() then Sequence{}
 else resultExprs->first().evaluate(target)
 endif
checkCondition
boolean checkCondition([Element](Element.html) target)
Model-level evaluate this `Expression` with the given `target`. If the result is a `LiteralBoolean`, return its `value`. Otherwise return `false`.
 
 let results: Sequence(Element) = evaluate(target) in
 result->size() = 1 and
 results->first().oclIsKindOf(LiteralBoolean) and 
 results->first().oclAsType(LiteralBoolean).value

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Expression">Interface Expression</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></code>, <code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../sysml/model/sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssertConstraintUsage</a></code>, <code><a href="BooleanExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BooleanExpression</a></code>, <code><a href="../../../sysml/model/sysml/CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a></code>, <code><a href="../../../sysml/model/sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a></code>, <code><a href="CollectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CollectExpression</a></code>, <code><a href="../../../sysml/model/sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a></code>, <code><a href="../../../sysml/model/sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a></code>, <code><a href="ConstructorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ConstructorExpression</a></code>, <code><a href="FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a></code>, <code><a href="FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a></code>, <code><a href="../../../sysml/model/sysml/IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IncludeUseCaseUsage</a></code>, <code><a href="IndexExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">IndexExpression</a></code>, <code><a href="InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InstantiationExpression</a></code>, <code><a href="Invariant.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Invariant</a></code>, <code><a href="InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></code>, <code><a href="LiteralBoolean.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralBoolean</a></code>, <code><a href="LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralExpression</a></code>, <code><a href="LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInfinity</a></code>, <code><a href="LiteralInteger.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInteger</a></code>, <code><a href="LiteralRational.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralRational</a></code>, <code><a href="LiteralString.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralString</a></code>, <code><a href="MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a></code>, <code><a href="NullExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NullExpression</a></code>, <code><a href="OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></code>, <code><a href="../../../sysml/model/sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></code>, <code><a href="../../../sysml/model/sysml/SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SatisfyRequirementUsage</a></code>, <code><a href="SelectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SelectExpression</a></code>, <code><a href="../../../sysml/model/sysml/TriggerInvocationExpression.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TriggerInvocationExpression</a></code>, <code><a href="../../../sysml/model/sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Expression</span><span class="extends-implements">
extends <a href="Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></span></div>
<div class="block"><p>An <code>Expression</code> is a <code>Step</code> that is typed by a <code>Function</code>. An <code>Expression</code> that also has a <code>Function</code> as its <code>featuringType</code> is a computational step within that <code>Function</code>. An <code>Expression</code> always has a single <code>result</code> parameter, which redefines the <code>result</code> parameter of its defining <code>function</code>. This allows <code>Expressions</code> to be interconnected in tree structures, in which inputs to each <code>Expression</code> in the tree are determined as the results of other <code>Expression</code> in the tree.</p>
 
 isModelLevelEvaluable = modelLevelEvaluable(Set(Element){})
 specializesFromLibrary('Performances::evaluations')
 owningMembership &lt;&gt; null and 
 owningMembership.oclIsKindOf(FeatureValue) implies
     let featureWithValue : Feature = 
         owningMembership.oclAsType(FeatureValue).featureWithValue in
     featuringType = featureWithValue.featuringType
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
 
 featureMembership-&gt;
     selectByKind(ReturnParameterMembership)-&gt;
     size() = 1
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#checkCondition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">checkCondition</a><wbr/>(<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Model-level evaluate this <code>Expression</code> with the given <code>target</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#evaluate(com.dassault_systemes.modeler.kerml.model.kerml.Element)">evaluate</a><wbr/>(<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If this <code>Expression</code> <code>isModelLevelEvaluable</code>, then evaluate it using the <code>target</code> as the context <code>Element</code> for resolving <code>Feature</code> names and testing classification.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFunction()">getFunction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Function</code> that types this <code>Expression</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getResult()">getResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"></div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isModelLevelEvaluable()">isModelLevelEvaluable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this <code>Expression</code> meets the constraints necessary to be evaluated at <em>model level</em>, that is, using metadata within the model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#modelLevelEvaluable(java.util.List)">modelLevelEvaluable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; visited)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return whether this <code>Expression</code> is model-level evaluable.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()">getID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)">setID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Element">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></h3>
<code><a href="Element.html#escapedName()">escapedName</a>, <a href="Element.html#getAliasIds()">getAliasIds</a>, <a href="Element.html#getDeclaredName()">getDeclaredName</a>, <a href="Element.html#getDeclaredShortName()">getDeclaredShortName</a>, <a href="Element.html#getDocumentation()">getDocumentation</a>, <a href="Element.html#getElementId()">getElementId</a>, <a href="Element.html#getName()">getName</a>, <a href="Element.html#getOwnedAnnotation()">getOwnedAnnotation</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwnedRelationship()">getOwnedRelationship</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getOwningMembership()">getOwningMembership</a>, <a href="Element.html#getOwningNamespace()">getOwningNamespace</a>, <a href="Element.html#getOwningRelationship()">getOwningRelationship</a>, <a href="Element.html#getQualifiedName()">getQualifiedName</a>, <a href="Element.html#getShortName()">getShortName</a>, <a href="Element.html#getTextualRepresentation()">getTextualRepresentation</a>, <a href="Element.html#isImpliedIncluded()">isImpliedIncluded</a>, <a href="Element.html#isLibraryElement()">isLibraryElement</a>, <a href="Element.html#libraryNamespace()">libraryNamespace</a>, <a href="Element.html#path()">path</a>, <a href="Element.html#setDeclaredName(java.lang.String)">setDeclaredName</a>, <a href="Element.html#setDeclaredShortName(java.lang.String)">setDeclaredShortName</a>, <a href="Element.html#setElementId(java.lang.String)">setElementId</a>, <a href="Element.html#setIsImpliedIncluded(boolean)">setIsImpliedIncluded</a>, <a href="Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwner</a>, <a href="Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">setOwningMembership</a>, <a href="Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">setOwningRelationship</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Feature">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></h3>
<code><a href="Feature.html#allRedefinedFeatures()">allRedefinedFeatures</a>, <a href="Feature.html#asCartesianProduct()">asCartesianProduct</a>, <a href="Feature.html#canAccess(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">canAccess</a>, <a href="Feature.html#directionFor(com.dassault_systemes.modeler.kerml.model.kerml.Type)">directionFor</a>, <a href="Feature.html#effectiveName()">effectiveName</a>, <a href="Feature.html#effectiveShortName()">effectiveShortName</a>, <a href="Feature.html#getChainingFeature()">getChainingFeature</a>, <a href="Feature.html#getCrossFeature()">getCrossFeature</a>, <a href="Feature.html#getDirection()">getDirection</a>, <a href="Feature.html#getEndOwningType()">getEndOwningType</a>, <a href="Feature.html#getFeatureTarget()">getFeatureTarget</a>, <a href="Feature.html#getFeaturingType()">getFeaturingType</a>, <a href="Feature.html#getOwnedCrossSubsetting()">getOwnedCrossSubsetting</a>, <a href="Feature.html#getOwnedFeatureChaining()">getOwnedFeatureChaining</a>, <a href="Feature.html#getOwnedFeatureInverting()">getOwnedFeatureInverting</a>, <a href="Feature.html#getOwnedRedefinition()">getOwnedRedefinition</a>, <a href="Feature.html#getOwnedReferenceSubsetting()">getOwnedReferenceSubsetting</a>, <a href="Feature.html#getOwnedSubsetting()">getOwnedSubsetting</a>, <a href="Feature.html#getOwnedTypeFeaturing()">getOwnedTypeFeaturing</a>, <a href="Feature.html#getOwnedTyping()">getOwnedTyping</a>, <a href="Feature.html#getOwningFeatureMembership()">getOwningFeatureMembership</a>, <a href="Feature.html#getOwningType()">getOwningType</a>, <a href="Feature.html#getType()">getType</a>, <a href="Feature.html#isCartesianProduct()">isCartesianProduct</a>, <a href="Feature.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isCompatibleWith</a>, <a href="Feature.html#isComposite()">isComposite</a>, <a href="Feature.html#isConstant()">isConstant</a>, <a href="Feature.html#isDerived()">isDerived</a>, <a href="Feature.html#isEnd()">isEnd</a>, <a href="Feature.html#isFeaturedWithin(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isFeaturedWithin</a>, <a href="Feature.html#isFeaturingType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isFeaturingType</a>, <a href="Feature.html#isOrdered()">isOrdered</a>, <a href="Feature.html#isOwnedCrossFeature()">isOwnedCrossFeature</a>, <a href="Feature.html#isPortion()">isPortion</a>, <a href="Feature.html#isUnique()">isUnique</a>, <a href="Feature.html#isVariable()">isVariable</a>, <a href="Feature.html#namingFeature()">namingFeature</a>, <a href="Feature.html#ownedCrossFeature()">ownedCrossFeature</a>, <a href="Feature.html#redefines(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">redefines</a>, <a href="Feature.html#redefinesFromLibrary(java.lang.String)">redefinesFromLibrary</a>, <a href="Feature.html#setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)">setDirection</a>, <a href="Feature.html#setIsComposite(boolean)">setIsComposite</a>, <a href="Feature.html#setIsConstant(boolean)">setIsConstant</a>, <a href="Feature.html#setIsDerived(boolean)">setIsDerived</a>, <a href="Feature.html#setIsEnd(boolean)">setIsEnd</a>, <a href="Feature.html#setIsOrdered(boolean)">setIsOrdered</a>, <a href="Feature.html#setIsPortion(boolean)">setIsPortion</a>, <a href="Feature.html#setIsUnique(boolean)">setIsUnique</a>, <a href="Feature.html#setIsVariable(boolean)">setIsVariable</a>, <a href="Feature.html#subsetsChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">subsetsChain</a>, <a href="Feature.html#supertypes(boolean)">supertypes</a>, <a href="Feature.html#typingFeatures()">typingFeatures</a></code></div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Step">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></h3>
<code><a href="Step.html#getBehavior()">getBehavior</a>, <a href="Step.html#getParameter()">getParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Type">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></h3>
<code><a href="Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">allRedefinedFeaturesOf</a>, <a href="Type.html#allSupertypes()">allSupertypes</a>, <a href="Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">directionOf</a>, <a href="Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">directionOfExcluding</a>, <a href="Type.html#getDifferencingType()">getDifferencingType</a>, <a href="Type.html#getDirectedFeature()">getDirectedFeature</a>, <a href="Type.html#getEndFeature()">getEndFeature</a>, <a href="Type.html#getFeature()">getFeature</a>, <a href="Type.html#getFeatureMembership()">getFeatureMembership</a>, <a href="Type.html#getInheritedFeature()">getInheritedFeature</a>, <a href="Type.html#getInheritedMembership()">getInheritedMembership</a>, <a href="Type.html#getInput()">getInput</a>, <a href="Type.html#getIntersectingType()">getIntersectingType</a>, <a href="Type.html#getMultiplicity()">getMultiplicity</a>, <a href="Type.html#getOutput()">getOutput</a>, <a href="Type.html#getOwnedConjugator()">getOwnedConjugator</a>, <a href="Type.html#getOwnedDifferencing()">getOwnedDifferencing</a>, <a href="Type.html#getOwnedDisjoining()">getOwnedDisjoining</a>, <a href="Type.html#getOwnedEndFeature()">getOwnedEndFeature</a>, <a href="Type.html#getOwnedFeature()">getOwnedFeature</a>, <a href="Type.html#getOwnedFeatureMembership()">getOwnedFeatureMembership</a>, <a href="Type.html#getOwnedIntersecting()">getOwnedIntersecting</a>, <a href="Type.html#getOwnedSpecialization()">getOwnedSpecialization</a>, <a href="Type.html#getOwnedUnioning()">getOwnedUnioning</a>, <a href="Type.html#getUnioningType()">getUnioningType</a>, <a href="Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)">inheritableMemberships</a>, <a href="Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)">inheritedMemberships</a>, <a href="Type.html#isAbstract()">isAbstract</a>, <a href="Type.html#isConjugated()">isConjugated</a>, <a href="Type.html#isSufficient()">isSufficient</a>, <a href="Type.html#multiplicities()">multiplicities</a>, <a href="Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)">nonPrivateMemberships</a>, <a href="Type.html#removeRedefinedFeatures(java.util.List)">removeRedefinedFeatures</a>, <a href="Type.html#setIsAbstract(boolean)">setIsAbstract</a>, <a href="Type.html#setIsSufficient(boolean)">setIsSufficient</a>, <a href="Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">specializes</a>, <a href="Type.html#specializesFromLibrary(java.lang.String)">specializesFromLibrary</a>, <a href="Type.html#visibleMemberships(java.util.List,boolean,boolean)">visibleMemberships</a></code></div>
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
<section class="detail" id="getFunction()">
<h3>getFunction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a></span> <span class="element-name">getFunction</span>()</div>
<div class="block"><p>The <code>Function</code> that types this <code>Expression</code>.</p>
<p>This is the Function that types the Expression.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the function value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="typedExpression"
        redefines=<a href="Step.html#getBehavior()"><code>Step.getBehavior()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResult()">
<h3>getResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getResult</span>()</div>
<div class="block"><p><p>An <code>output</code> <code>parameter</code> of the <code>Expression</code> whose value is the result of the <code>Expression</code>. The result of an <code>Expression</code> is either inherited from its <code>function</code> or it is related to the <code>Expression</code> via a <code>ReturnParameterMembership</code>, in which case it redefines the <code>result</code> <code>parameter</code> of its <code>function</code>.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the result value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="computingExpression"
        subsets=<a href="Type.html#getOutput()"><code>Type.getOutput()</code></a>, <a href="Step.html#getParameter()"><code>Step.getParameter()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isModelLevelEvaluable()">
<h3>isModelLevelEvaluable</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isModelLevelEvaluable</span>()</div>
<div class="block"><p>Whether this <code>Expression</code> meets the constraints necessary to be evaluated at <em>model level</em>, that is, using metadata within the model.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isModelLevelEvaluable value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="modelLevelEvaluable(java.util.List)">
<h3>modelLevelEvaluable</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">modelLevelEvaluable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; visited)</span></div>
<div class="block"><p>Return whether this <code>Expression</code> is model-level evaluable. The <code>visited</code> parameter is used to track possible circular <code>Feature</code> references made from <code>FeatureReferenceExpressions</code> (see the redefinition of this operation for <code>FeatureReferenceExpression</code>). Such circular references are not allowed in model-level evaluable expressions.</p>
<p>An <code>Expression</code> that is not otherwise specialized is model-level evaluable if it has no (non-implied) <code>ownedSpecializations</code> and all its <code>ownedFeatures</code> are either <code>in</code> parameters, the <code>result</code> <code>parameter</code> or a result <code>Expression</code> owned via a <code>ResultExpressionMembership</code>. The <code>parameters</code>  must not have any <code>ownedFeatures</code> or a <code>FeatureValue</code>, and the result <code>Expression</code> must be model-level evaluable.</p>
 ownedSpecialization-&gt;forAll(isImplied) and 
 ownedFeature-&gt;forAll(f |
     (directionOf(f) = FeatureDirectionKind::_'in' or f = result) and
         f.ownedFeature-&gt;isEmpty() and f.valuation = null or
     f.owningFeatureMembership.oclIsKindOf(ResultExpressionMembership) and
         f.oclAsType(Expression).modelLevelEvaluable(visited)</div>
</section>
</li>
<li>
<section class="detail" id="evaluate(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>evaluate</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="element-name">evaluate</span><wbr/><span class="parameters">(<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> target)</span></div>
<div class="block"><p>If this <code>Expression</code> <code>isModelLevelEvaluable</code>, then evaluate it using the <code>target</code> as the context <code>Element</code> for resolving <code>Feature</code> names and testing classification. The result is a collection of <code>Elements</code>, which, for a fully evaluable <code>Expression</code>, will be a <code>LiteralExpression</code> or a <code>Feature</code> that is not an <code>Expression</code>.</p>
 isModelLevelEvaluable
 let resultExprs : Sequence(Expression) =
     ownedFeatureMembership-&gt;
         selectByKind(ResultExpressionMembership).
         ownedResultExpression in
 if resultExpr-&gt;isEmpty() then Sequence{}
 else resultExprs-&gt;first().evaluate(target)
 endif</div>
</section>
</li>
<li>
<section class="detail" id="checkCondition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>checkCondition</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">checkCondition</span><wbr/><span class="parameters">(<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> target)</span></div>
<div class="block"><p>Model-level evaluate this <code>Expression</code> with the given <code>target</code>. If the result is a <code>LiteralBoolean</code>, return its <code>value</code>. Otherwise return <code>false</code>.</p>
 
 let results: Sequence(Element) = evaluate(target) in
     result-&gt;size() = 1 and
     results-&gt;first().oclIsKindOf(LiteralBoolean) and 
     results-&gt;first().oclAsType(LiteralBoolean).value</div>
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
