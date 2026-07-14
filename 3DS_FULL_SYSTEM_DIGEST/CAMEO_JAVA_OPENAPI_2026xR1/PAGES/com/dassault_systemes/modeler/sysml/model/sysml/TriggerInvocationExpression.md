# JAVA OPENAPI: TriggerInvocationExpression (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/sysml/TriggerInvocationExpression.html
- source_path: `com/dassault_systemes/modeler/sysml/model/sysml/TriggerInvocationExpression.html`
- source_sha256: `e7c5f7178b0deb0ae6eb5474846c8bc776d31e381b479bc3179811711123db6b`
- captured_utc: `2026-07-14T16:45:05.037068+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model.sysml](package-summary.html)

## Interface TriggerInvocationExpression

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../../kerml/model/kerml/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[Expression](../../../kerml/model/kerml/Expression.html)`, `[Feature](../../../kerml/model/kerml/Feature.html)`, `[InstantiationExpression](../../../kerml/model/kerml/InstantiationExpression.html)`, `[InvocationExpression](../../../kerml/model/kerml/InvocationExpression.html)`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `[Namespace](../../../kerml/model/kerml/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[Step](../../../kerml/model/kerml/Step.html)`, `[Type](../../../kerml/model/kerml/Type.html)`

@OpenApiAllpublic interfaceTriggerInvocationExpressionextends [InvocationExpression](../../../kerml/model/kerml/InvocationExpression.html)

A `TriggerInvocationExpression` is an `InvocationExpression` that invokes one of the trigger `Functions` from the Kernel Semantic Library `*Triggers***` package, as indicated by its `kind`.
 kind = TriggerKind::after implies
 argument->notEmpty() and
 argument->at(1).result.specializesFromLibrary('Quantities::ScalarQuantityValue') and
 let mRef : Element = 
 resolveGlobal('Quantities::TensorQuantityValue::mRef').ownedMemberElement in
 argument->at(1).result.feature->
 select(ownedRedefinition.redefinedFeature->
 closure(ownedRedefinition.redefinedFeature)->
 includes(mRef))->
 exists(specializesFromLibrary('ISQBase::DurationUnit'))
 kind = TriggerKind::at implies
 argument->notEmpty() and
 argument->at(1).result.specializesFromLibrary('Time::TimeInstantValue')
 kind = TriggerKind::when implies
 argument->notEmpty() and
 argument->at(1).oclIsKindOf(FeatureReferenceExpression) and
 let referent : Feature = 
 argument->at(1).oclAsType(FeatureReferenceExpression).referent in
 referent.oclIsKindOf(Expression) and
 referent.oclAsType(Expression).result.specializesFromLibrary('ScalarValues::Boolean')

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[TriggerKind](TriggerKind.html)`
`[getKind](#getKind())()`
Indicates which of the `Functions` from the `*Triggers*` model in the Kernel Semantic Library is to be invoked by this `TriggerInvocationExpression`.
`[Type](../../../kerml/model/kerml/Type.html)`
`[instantiatedType](#instantiatedType())()`
Return one of the `Functions` *`TriggerWhen`*, *`TriggerAt`* or *`TriggerAfter`*, from the Kernel Semantic Library *`Triggers`* package, depending on whether the `kind` of this `TriggerInvocationExpression` is `when`, `at` or `after`, respectively.
`void`
`[setKind](#setKind(com.dassault_systemes.modeler.sysml.model.sysml.TriggerKind))([TriggerKind](TriggerKind.html) value)`
Indicates which of the `Functions` from the `*Triggers*` model in the Kernel Semantic Library is to be invoked by this `TriggerInvocationExpression`.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](../../../kerml/model/kerml/Element.html)
`[escapedName](../../../kerml/model/kerml/Element.html#escapedName()), [getAliasIds](../../../kerml/model/kerml/Element.html#getAliasIds()), [getDeclaredName](../../../kerml/model/kerml/Element.html#getDeclaredName()), [getDeclaredShortName](../../../kerml/model/kerml/Element.html#getDeclaredShortName()), [getDocumentation](../../../kerml/model/kerml/Element.html#getDocumentation()), [getElementId](../../../kerml/model/kerml/Element.html#getElementId()), [getName](../../../kerml/model/kerml/Element.html#getName()), [getOwnedAnnotation](../../../kerml/model/kerml/Element.html#getOwnedAnnotation()), [getOwnedElement](../../../kerml/model/kerml/Element.html#getOwnedElement()), [getOwnedRelationship](../../../kerml/model/kerml/Element.html#getOwnedRelationship()), [getOwner](../../../kerml/model/kerml/Element.html#getOwner()), [getOwningMembership](../../../kerml/model/kerml/Element.html#getOwningMembership()), [getOwningNamespace](../../../kerml/model/kerml/Element.html#getOwningNamespace()), [getOwningRelationship](../../../kerml/model/kerml/Element.html#getOwningRelationship()), [getQualifiedName](../../../kerml/model/kerml/Element.html#getQualifiedName()), [getShortName](../../../kerml/model/kerml/Element.html#getShortName()), [getTextualRepresentation](../../../kerml/model/kerml/Element.html#getTextualRepresentation()), [isImpliedIncluded](../../../kerml/model/kerml/Element.html#isImpliedIncluded()), [isLibraryElement](../../../kerml/model/kerml/Element.html#isLibraryElement()), [libraryNamespace](../../../kerml/model/kerml/Element.html#libraryNamespace()), [path](../../../kerml/model/kerml/Element.html#path()), [setDeclaredName](../../../kerml/model/kerml/Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](../../../kerml/model/kerml/Element.html#setDeclaredShortName(java.lang.String)), [setElementId](../../../kerml/model/kerml/Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](../../../kerml/model/kerml/Element.html#setIsImpliedIncluded(boolean)), [setOwner](../../../kerml/model/kerml/Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](../../../kerml/model/kerml/Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](../../../kerml/model/kerml/Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Expression](../../../kerml/model/kerml/Expression.html)
`[checkCondition](../../../kerml/model/kerml/Expression.html#checkCondition(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [getFunction](../../../kerml/model/kerml/Expression.html#getFunction()), [getResult](../../../kerml/model/kerml/Expression.html#getResult()), [isModelLevelEvaluable](../../../kerml/model/kerml/Expression.html#isModelLevelEvaluable())`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Feature](../../../kerml/model/kerml/Feature.html)
`[allRedefinedFeatures](../../../kerml/model/kerml/Feature.html#allRedefinedFeatures()), [asCartesianProduct](../../../kerml/model/kerml/Feature.html#asCartesianProduct()), [canAccess](../../../kerml/model/kerml/Feature.html#canAccess(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [directionFor](../../../kerml/model/kerml/Feature.html#directionFor(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [effectiveName](../../../kerml/model/kerml/Feature.html#effectiveName()), [effectiveShortName](../../../kerml/model/kerml/Feature.html#effectiveShortName()), [getChainingFeature](../../../kerml/model/kerml/Feature.html#getChainingFeature()), [getCrossFeature](../../../kerml/model/kerml/Feature.html#getCrossFeature()), [getDirection](../../../kerml/model/kerml/Feature.html#getDirection()), [getEndOwningType](../../../kerml/model/kerml/Feature.html#getEndOwningType()), [getFeatureTarget](../../../kerml/model/kerml/Feature.html#getFeatureTarget()), [getFeaturingType](../../../kerml/model/kerml/Feature.html#getFeaturingType()), [getOwnedCrossSubsetting](../../../kerml/model/kerml/Feature.html#getOwnedCrossSubsetting()), [getOwnedFeatureChaining](../../../kerml/model/kerml/Feature.html#getOwnedFeatureChaining()), [getOwnedFeatureInverting](../../../kerml/model/kerml/Feature.html#getOwnedFeatureInverting()), [getOwnedRedefinition](../../../kerml/model/kerml/Feature.html#getOwnedRedefinition()), [getOwnedReferenceSubsetting](../../../kerml/model/kerml/Feature.html#getOwnedReferenceSubsetting()), [getOwnedSubsetting](../../../kerml/model/kerml/Feature.html#getOwnedSubsetting()), [getOwnedTypeFeaturing](../../../kerml/model/kerml/Feature.html#getOwnedTypeFeaturing()), [getOwnedTyping](../../../kerml/model/kerml/Feature.html#getOwnedTyping()), [getOwningFeatureMembership](../../../kerml/model/kerml/Feature.html#getOwningFeatureMembership()), [getOwningType](../../../kerml/model/kerml/Feature.html#getOwningType()), [getType](../../../kerml/model/kerml/Feature.html#getType()), [isCartesianProduct](../../../kerml/model/kerml/Feature.html#isCartesianProduct()), [isCompatibleWith](../../../kerml/model/kerml/Feature.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isComposite](../../../kerml/model/kerml/Feature.html#isComposite()), [isConstant](../../../kerml/model/kerml/Feature.html#isConstant()), [isDerived](../../../kerml/model/kerml/Feature.html#isDerived()), [isEnd](../../../kerml/model/kerml/Feature.html#isEnd()), [isFeaturedWithin](../../../kerml/model/kerml/Feature.html#isFeaturedWithin(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isFeaturingType](../../../kerml/model/kerml/Feature.html#isFeaturingType(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isOrdered](../../../kerml/model/kerml/Feature.html#isOrdered()), [isOwnedCrossFeature](../../../kerml/model/kerml/Feature.html#isOwnedCrossFeature()), [isPortion](../../../kerml/model/kerml/Feature.html#isPortion()), [isUnique](../../../kerml/model/kerml/Feature.html#isUnique()), [isVariable](../../../kerml/model/kerml/Feature.html#isVariable()), [namingFeature](../../../kerml/model/kerml/Feature.html#namingFeature()), [ownedCrossFeature](../../../kerml/model/kerml/Feature.html#ownedCrossFeature()), [redefines](../../../kerml/model/kerml/Feature.html#redefines(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [redefinesFromLibrary](../../../kerml/model/kerml/Feature.html#redefinesFromLibrary(java.lang.String)), [setDirection](../../../kerml/model/kerml/Feature.html#setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)), [setIsComposite](../../../kerml/model/kerml/Feature.html#setIsComposite(boolean)), [setIsConstant](../../../kerml/model/kerml/Feature.html#setIsConstant(boolean)), [setIsDerived](../../../kerml/model/kerml/Feature.html#setIsDerived(boolean)), [setIsEnd](../../../kerml/model/kerml/Feature.html#setIsEnd(boolean)), [setIsOrdered](../../../kerml/model/kerml/Feature.html#setIsOrdered(boolean)), [setIsPortion](../../../kerml/model/kerml/Feature.html#setIsPortion(boolean)), [setIsUnique](../../../kerml/model/kerml/Feature.html#setIsUnique(boolean)), [setIsVariable](../../../kerml/model/kerml/Feature.html#setIsVariable(boolean)), [subsetsChain](../../../kerml/model/kerml/Feature.html#subsetsChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [supertypes](../../../kerml/model/kerml/Feature.html#supertypes(boolean)), [typingFeatures](../../../kerml/model/kerml/Feature.html#typingFeatures())`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[InstantiationExpression](../../../kerml/model/kerml/InstantiationExpression.html)
`[getArgument](../../../kerml/model/kerml/InstantiationExpression.html#getArgument()), [getInstantiatedType](../../../kerml/model/kerml/InstantiationExpression.html#getInstantiatedType())`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[InvocationExpression](../../../kerml/model/kerml/InvocationExpression.html)
`[evaluate](../../../kerml/model/kerml/InvocationExpression.html#evaluate(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [modelLevelEvaluable](../../../kerml/model/kerml/InvocationExpression.html#modelLevelEvaluable(java.util.List))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject
`getModelExtension, getModelExtension`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Namespace](../../../kerml/model/kerml/Namespace.html)
`[getImportedMembership](../../../kerml/model/kerml/Namespace.html#getImportedMembership()), [getMember](../../../kerml/model/kerml/Namespace.html#getMember()), [getMembership](../../../kerml/model/kerml/Namespace.html#getMembership()), [getOwnedImport](../../../kerml/model/kerml/Namespace.html#getOwnedImport()), [getOwnedMember](../../../kerml/model/kerml/Namespace.html#getOwnedMember()), [getOwnedMembership](../../../kerml/model/kerml/Namespace.html#getOwnedMembership()), [importedMemberships](../../../kerml/model/kerml/Namespace.html#importedMemberships(java.util.List)), [membershipsOfVisibility](../../../kerml/model/kerml/Namespace.html#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)), [namesOf](../../../kerml/model/kerml/Namespace.html#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [qualificationOf](../../../kerml/model/kerml/Namespace.html#qualificationOf(java.lang.String)), [resolve](../../../kerml/model/kerml/Namespace.html#resolve(java.lang.String)), [resolveGlobal](../../../kerml/model/kerml/Namespace.html#resolveGlobal(java.lang.String)), [resolveLocal](../../../kerml/model/kerml/Namespace.html#resolveLocal(java.lang.String)), [resolveVisible](../../../kerml/model/kerml/Namespace.html#resolveVisible(java.lang.String)), [unqualifiedNameOf](../../../kerml/model/kerml/Namespace.html#unqualifiedNameOf(java.lang.String)), [visibilityOf](../../../kerml/model/kerml/Namespace.html#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Step](../../../kerml/model/kerml/Step.html)
`[getBehavior](../../../kerml/model/kerml/Step.html#getBehavior()), [getParameter](../../../kerml/model/kerml/Step.html#getParameter())`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Type](../../../kerml/model/kerml/Type.html)
`[allRedefinedFeaturesOf](../../../kerml/model/kerml/Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)), [allSupertypes](../../../kerml/model/kerml/Type.html#allSupertypes()), [directionOf](../../../kerml/model/kerml/Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [directionOfExcluding](../../../kerml/model/kerml/Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)), [getDifferencingType](../../../kerml/model/kerml/Type.html#getDifferencingType()), [getDirectedFeature](../../../kerml/model/kerml/Type.html#getDirectedFeature()), [getEndFeature](../../../kerml/model/kerml/Type.html#getEndFeature()), [getFeature](../../../kerml/model/kerml/Type.html#getFeature()), [getFeatureMembership](../../../kerml/model/kerml/Type.html#getFeatureMembership()), [getInheritedFeature](../../../kerml/model/kerml/Type.html#getInheritedFeature()), [getInheritedMembership](../../../kerml/model/kerml/Type.html#getInheritedMembership()), [getInput](../../../kerml/model/kerml/Type.html#getInput()), [getIntersectingType](../../../kerml/model/kerml/Type.html#getIntersectingType()), [getMultiplicity](../../../kerml/model/kerml/Type.html#getMultiplicity()), [getOutput](../../../kerml/model/kerml/Type.html#getOutput()), [getOwnedConjugator](../../../kerml/model/kerml/Type.html#getOwnedConjugator()), [getOwnedDifferencing](../../../kerml/model/kerml/Type.html#getOwnedDifferencing()), [getOwnedDisjoining](../../../kerml/model/kerml/Type.html#getOwnedDisjoining()), [getOwnedEndFeature](../../../kerml/model/kerml/Type.html#getOwnedEndFeature()), [getOwnedFeature](../../../kerml/model/kerml/Type.html#getOwnedFeature()), [getOwnedFeatureMembership](../../../kerml/model/kerml/Type.html#getOwnedFeatureMembership()), [getOwnedIntersecting](../../../kerml/model/kerml/Type.html#getOwnedIntersecting()), [getOwnedSpecialization](../../../kerml/model/kerml/Type.html#getOwnedSpecialization()), [getOwnedUnioning](../../../kerml/model/kerml/Type.html#getOwnedUnioning()), [getUnioningType](../../../kerml/model/kerml/Type.html#getUnioningType()), [inheritableMemberships](../../../kerml/model/kerml/Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)), [inheritedMemberships](../../../kerml/model/kerml/Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)), [isAbstract](../../../kerml/model/kerml/Type.html#isAbstract()), [isConjugated](../../../kerml/model/kerml/Type.html#isConjugated()), [isSufficient](../../../kerml/model/kerml/Type.html#isSufficient()), [multiplicities](../../../kerml/model/kerml/Type.html#multiplicities()), [nonPrivateMemberships](../../../kerml/model/kerml/Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)), [removeRedefinedFeatures](../../../kerml/model/kerml/Type.html#removeRedefinedFeatures(java.util.List)), [setIsAbstract](../../../kerml/model/kerml/Type.html#setIsAbstract(boolean)), [setIsSufficient](../../../kerml/model/kerml/Type.html#setIsSufficient(boolean)), [specializes](../../../kerml/model/kerml/Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [specializesFromLibrary](../../../kerml/model/kerml/Type.html#specializesFromLibrary(java.lang.String)), [visibleMemberships](../../../kerml/model/kerml/Type.html#visibleMemberships(java.util.List,boolean,boolean))`

============ METHOD DETAIL ========== 
Method Details
getKind
@CheckForNull[TriggerKind](TriggerKind.html) getKind()
Indicates which of the `Functions` from the `*Triggers*` model in the Kernel Semantic Library is to be invoked by this `TriggerInvocationExpression`.
Returns:
the kind value
Model:
derived="false"
 transient="false"
setKind
void setKind(@CheckForNull
 [TriggerKind](TriggerKind.html) value)
Indicates which of the `Functions` from the `*Triggers*` model in the Kernel Semantic Library is to be invoked by this `TriggerInvocationExpression`.
Parameters:
`value` - the kind value
Model:
derived="false"
 transient="false"
instantiatedType
[Type](../../../kerml/model/kerml/Type.html) instantiatedType()
Return one of the `Functions` *`TriggerWhen`*, *`TriggerAt`* or *`TriggerAfter`*, from the Kernel Semantic Library *`Triggers`* package, depending on whether the `kind` of this `TriggerInvocationExpression` is `when`, `at` or `after`, respectively.
 resolveGlobal(
 if kind = TriggerKind::when then
 'Triggers::TriggerWhen'
 else if kind = TriggerKind::at then
 'Triggers::TriggerAt'
 else
 'Triggers::TriggerAfter'
 endif endif
 ).memberElement.oclAsType(Type)
Specified by:
`[instantiatedType](../../../kerml/model/kerml/InstantiationExpression.html#instantiatedType())` in interface `[InstantiationExpression](../../../kerml/model/kerml/InstantiationExpression.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model.sysml</a></div>
<h1 class="title" title="Interface TriggerInvocationExpression">Interface TriggerInvocationExpression</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code>, <code><a href="../../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code>, <code><a href="../../../kerml/model/kerml/InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InstantiationExpression</a></code>, <code><a href="../../../kerml/model/kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code><a href="../../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../../kerml/model/kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></code>, <code><a href="../../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">TriggerInvocationExpression</span><span class="extends-implements">
extends <a href="../../../kerml/model/kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></span></div>
<div class="block"><p>A <code>TriggerInvocationExpression</code> is an <code>InvocationExpression</code> that invokes one of the trigger <code>Functions</code> from the Kernel Semantic Library <code><em>Triggers<em></em></em></code> package, as indicated by its <code>kind</code>.</p>
 kind = TriggerKind::after implies
     argument-&gt;notEmpty() and
     argument-&gt;at(1).result.specializesFromLibrary('Quantities::ScalarQuantityValue') and
     let mRef : Element = 
         resolveGlobal('Quantities::TensorQuantityValue::mRef').ownedMemberElement in
     argument-&gt;at(1).result.feature-&gt;
         select(ownedRedefinition.redefinedFeature-&gt;
            closure(ownedRedefinition.redefinedFeature)-&gt;
            includes(mRef))-&gt;
         exists(specializesFromLibrary('ISQBase::DurationUnit'))
 kind = TriggerKind::at implies
     argument-&gt;notEmpty() and
     argument-&gt;at(1).result.specializesFromLibrary('Time::TimeInstantValue')
 kind = TriggerKind::when implies
     argument-&gt;notEmpty() and
     argument-&gt;at(1).oclIsKindOf(FeatureReferenceExpression) and
     let referent : Feature = 
         argument-&gt;at(1).oclAsType(FeatureReferenceExpression).referent in
     referent.oclIsKindOf(Expression) and
     referent.oclAsType(Expression).result.specializesFromLibrary('ScalarValues::Boolean')</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getKind()">getKind</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates which of the <code>Functions</code> from the <code><em>Triggers</em></code> model in the Kernel Semantic Library is to be invoked by this <code>TriggerInvocationExpression</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#instantiatedType()">instantiatedType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return one of the <code>Functions</code> <em><code>TriggerWhen</code></em>, <em><code>TriggerAt</code></em> or <em><code>TriggerAfter</code></em>, from the Kernel Semantic Library <em><code>Triggers</code></em> package, depending on whether the <code>kind</code> of this <code>TriggerInvocationExpression</code> is <code>when</code>, <code>at</code> or <code>after</code>, respectively.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setKind(com.dassault_systemes.modeler.sysml.model.sysml.TriggerKind)">setKind</a><wbr/>(<a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates which of the <code>Functions</code> from the <code><em>Triggers</em></code> model in the Kernel Semantic Library is to be invoked by this <code>TriggerInvocationExpression</code>.</div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Element">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></h3>
<code><a href="../../../kerml/model/kerml/Element.html#escapedName()">escapedName</a>, <a href="../../../kerml/model/kerml/Element.html#getAliasIds()">getAliasIds</a>, <a href="../../../kerml/model/kerml/Element.html#getDeclaredName()">getDeclaredName</a>, <a href="../../../kerml/model/kerml/Element.html#getDeclaredShortName()">getDeclaredShortName</a>, <a href="../../../kerml/model/kerml/Element.html#getDocumentation()">getDocumentation</a>, <a href="../../../kerml/model/kerml/Element.html#getElementId()">getElementId</a>, <a href="../../../kerml/model/kerml/Element.html#getName()">getName</a>, <a href="../../../kerml/model/kerml/Element.html#getOwnedAnnotation()">getOwnedAnnotation</a>, <a href="../../../kerml/model/kerml/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../../../kerml/model/kerml/Element.html#getOwnedRelationship()">getOwnedRelationship</a>, <a href="../../../kerml/model/kerml/Element.html#getOwner()">getOwner</a>, <a href="../../../kerml/model/kerml/Element.html#getOwningMembership()">getOwningMembership</a>, <a href="../../../kerml/model/kerml/Element.html#getOwningNamespace()">getOwningNamespace</a>, <a href="../../../kerml/model/kerml/Element.html#getOwningRelationship()">getOwningRelationship</a>, <a href="../../../kerml/model/kerml/Element.html#getQualifiedName()">getQualifiedName</a>, <a href="../../../kerml/model/kerml/Element.html#getShortName()">getShortName</a>, <a href="../../../kerml/model/kerml/Element.html#getTextualRepresentation()">getTextualRepresentation</a>, <a href="../../../kerml/model/kerml/Element.html#isImpliedIncluded()">isImpliedIncluded</a>, <a href="../../../kerml/model/kerml/Element.html#isLibraryElement()">isLibraryElement</a>, <a href="../../../kerml/model/kerml/Element.html#libraryNamespace()">libraryNamespace</a>, <a href="../../../kerml/model/kerml/Element.html#path()">path</a>, <a href="../../../kerml/model/kerml/Element.html#setDeclaredName(java.lang.String)">setDeclaredName</a>, <a href="../../../kerml/model/kerml/Element.html#setDeclaredShortName(java.lang.String)">setDeclaredShortName</a>, <a href="../../../kerml/model/kerml/Element.html#setElementId(java.lang.String)">setElementId</a>, <a href="../../../kerml/model/kerml/Element.html#setIsImpliedIncluded(boolean)">setIsImpliedIncluded</a>, <a href="../../../kerml/model/kerml/Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwner</a>, <a href="../../../kerml/model/kerml/Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">setOwningMembership</a>, <a href="../../../kerml/model/kerml/Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">setOwningRelationship</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Expression">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></h3>
<code><a href="../../../kerml/model/kerml/Expression.html#checkCondition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">checkCondition</a>, <a href="../../../kerml/model/kerml/Expression.html#getFunction()">getFunction</a>, <a href="../../../kerml/model/kerml/Expression.html#getResult()">getResult</a>, <a href="../../../kerml/model/kerml/Expression.html#isModelLevelEvaluable()">isModelLevelEvaluable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Feature">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></h3>
<code><a href="../../../kerml/model/kerml/Feature.html#allRedefinedFeatures()">allRedefinedFeatures</a>, <a href="../../../kerml/model/kerml/Feature.html#asCartesianProduct()">asCartesianProduct</a>, <a href="../../../kerml/model/kerml/Feature.html#canAccess(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">canAccess</a>, <a href="../../../kerml/model/kerml/Feature.html#directionFor(com.dassault_systemes.modeler.kerml.model.kerml.Type)">directionFor</a>, <a href="../../../kerml/model/kerml/Feature.html#effectiveName()">effectiveName</a>, <a href="../../../kerml/model/kerml/Feature.html#effectiveShortName()">effectiveShortName</a>, <a href="../../../kerml/model/kerml/Feature.html#getChainingFeature()">getChainingFeature</a>, <a href="../../../kerml/model/kerml/Feature.html#getCrossFeature()">getCrossFeature</a>, <a href="../../../kerml/model/kerml/Feature.html#getDirection()">getDirection</a>, <a href="../../../kerml/model/kerml/Feature.html#getEndOwningType()">getEndOwningType</a>, <a href="../../../kerml/model/kerml/Feature.html#getFeatureTarget()">getFeatureTarget</a>, <a href="../../../kerml/model/kerml/Feature.html#getFeaturingType()">getFeaturingType</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedCrossSubsetting()">getOwnedCrossSubsetting</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedFeatureChaining()">getOwnedFeatureChaining</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedFeatureInverting()">getOwnedFeatureInverting</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedRedefinition()">getOwnedRedefinition</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedReferenceSubsetting()">getOwnedReferenceSubsetting</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedSubsetting()">getOwnedSubsetting</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedTypeFeaturing()">getOwnedTypeFeaturing</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedTyping()">getOwnedTyping</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwningFeatureMembership()">getOwningFeatureMembership</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwningType()">getOwningType</a>, <a href="../../../kerml/model/kerml/Feature.html#getType()">getType</a>, <a href="../../../kerml/model/kerml/Feature.html#isCartesianProduct()">isCartesianProduct</a>, <a href="../../../kerml/model/kerml/Feature.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isCompatibleWith</a>, <a href="../../../kerml/model/kerml/Feature.html#isComposite()">isComposite</a>, <a href="../../../kerml/model/kerml/Feature.html#isConstant()">isConstant</a>, <a href="../../../kerml/model/kerml/Feature.html#isDerived()">isDerived</a>, <a href="../../../kerml/model/kerml/Feature.html#isEnd()">isEnd</a>, <a href="../../../kerml/model/kerml/Feature.html#isFeaturedWithin(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isFeaturedWithin</a>, <a href="../../../kerml/model/kerml/Feature.html#isFeaturingType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isFeaturingType</a>, <a href="../../../kerml/model/kerml/Feature.html#isOrdered()">isOrdered</a>, <a href="../../../kerml/model/kerml/Feature.html#isOwnedCrossFeature()">isOwnedCrossFeature</a>, <a href="../../../kerml/model/kerml/Feature.html#isPortion()">isPortion</a>, <a href="../../../kerml/model/kerml/Feature.html#isUnique()">isUnique</a>, <a href="../../../kerml/model/kerml/Feature.html#isVariable()">isVariable</a>, <a href="../../../kerml/model/kerml/Feature.html#namingFeature()">namingFeature</a>, <a href="../../../kerml/model/kerml/Feature.html#ownedCrossFeature()">ownedCrossFeature</a>, <a href="../../../kerml/model/kerml/Feature.html#redefines(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">redefines</a>, <a href="../../../kerml/model/kerml/Feature.html#redefinesFromLibrary(java.lang.String)">redefinesFromLibrary</a>, <a href="../../../kerml/model/kerml/Feature.html#setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)">setDirection</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsComposite(boolean)">setIsComposite</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsConstant(boolean)">setIsConstant</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsDerived(boolean)">setIsDerived</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsEnd(boolean)">setIsEnd</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsOrdered(boolean)">setIsOrdered</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsPortion(boolean)">setIsPortion</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsUnique(boolean)">setIsUnique</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsVariable(boolean)">setIsVariable</a>, <a href="../../../kerml/model/kerml/Feature.html#subsetsChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">subsetsChain</a>, <a href="../../../kerml/model/kerml/Feature.html#supertypes(boolean)">supertypes</a>, <a href="../../../kerml/model/kerml/Feature.html#typingFeatures()">typingFeatures</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InstantiationExpression</a></h3>
<code><a href="../../../kerml/model/kerml/InstantiationExpression.html#getArgument()">getArgument</a>, <a href="../../../kerml/model/kerml/InstantiationExpression.html#getInstantiatedType()">getInstantiatedType</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></h3>
<code><a href="../../../kerml/model/kerml/InvocationExpression.html#evaluate(com.dassault_systemes.modeler.kerml.model.kerml.Element)">evaluate</a>, <a href="../../../kerml/model/kerml/InvocationExpression.html#modelLevelEvaluable(java.util.List)">modelLevelEvaluable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.<a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></h3>
<code><a href="../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">canChangeElementOwner</a>, <a href="../../../foundation/model/ModelElement.html#dispose()">dispose</a>, <a href="../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)">eDynamicGet</a>, <a href="../../../foundation/model/ModelElement.html#getElementOwner()">getElementOwner</a>, <a href="../../../foundation/model/ModelElement.html#getLocalID()">getLocalID</a>, <a href="../../../foundation/model/ModelElement.html#getObjectParent()">getObjectParent</a>, <a href="../../../foundation/model/ModelElement.html#selfDispose()">selfDispose</a>, <a href="../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)">setLocalID</a>, <a href="../../../foundation/model/ModelElement.html#sGetLocalID()">sGetLocalID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject">Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</h3>
<code>getModelExtension, getModelExtension</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Namespace">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></h3>
<code><a href="../../../kerml/model/kerml/Namespace.html#getImportedMembership()">getImportedMembership</a>, <a href="../../../kerml/model/kerml/Namespace.html#getMember()">getMember</a>, <a href="../../../kerml/model/kerml/Namespace.html#getMembership()">getMembership</a>, <a href="../../../kerml/model/kerml/Namespace.html#getOwnedImport()">getOwnedImport</a>, <a href="../../../kerml/model/kerml/Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="../../../kerml/model/kerml/Namespace.html#getOwnedMembership()">getOwnedMembership</a>, <a href="../../../kerml/model/kerml/Namespace.html#importedMemberships(java.util.List)">importedMemberships</a>, <a href="../../../kerml/model/kerml/Namespace.html#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)">membershipsOfVisibility</a>, <a href="../../../kerml/model/kerml/Namespace.html#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)">namesOf</a>, <a href="../../../kerml/model/kerml/Namespace.html#qualificationOf(java.lang.String)">qualificationOf</a>, <a href="../../../kerml/model/kerml/Namespace.html#resolve(java.lang.String)">resolve</a>, <a href="../../../kerml/model/kerml/Namespace.html#resolveGlobal(java.lang.String)">resolveGlobal</a>, <a href="../../../kerml/model/kerml/Namespace.html#resolveLocal(java.lang.String)">resolveLocal</a>, <a href="../../../kerml/model/kerml/Namespace.html#resolveVisible(java.lang.String)">resolveVisible</a>, <a href="../../../kerml/model/kerml/Namespace.html#unqualifiedNameOf(java.lang.String)">unqualifiedNameOf</a>, <a href="../../../kerml/model/kerml/Namespace.html#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">visibilityOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Step">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></h3>
<code><a href="../../../kerml/model/kerml/Step.html#getBehavior()">getBehavior</a>, <a href="../../../kerml/model/kerml/Step.html#getParameter()">getParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Type">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></h3>
<code><a href="../../../kerml/model/kerml/Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">allRedefinedFeaturesOf</a>, <a href="../../../kerml/model/kerml/Type.html#allSupertypes()">allSupertypes</a>, <a href="../../../kerml/model/kerml/Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">directionOf</a>, <a href="../../../kerml/model/kerml/Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">directionOfExcluding</a>, <a href="../../../kerml/model/kerml/Type.html#getDifferencingType()">getDifferencingType</a>, <a href="../../../kerml/model/kerml/Type.html#getDirectedFeature()">getDirectedFeature</a>, <a href="../../../kerml/model/kerml/Type.html#getEndFeature()">getEndFeature</a>, <a href="../../../kerml/model/kerml/Type.html#getFeature()">getFeature</a>, <a href="../../../kerml/model/kerml/Type.html#getFeatureMembership()">getFeatureMembership</a>, <a href="../../../kerml/model/kerml/Type.html#getInheritedFeature()">getInheritedFeature</a>, <a href="../../../kerml/model/kerml/Type.html#getInheritedMembership()">getInheritedMembership</a>, <a href="../../../kerml/model/kerml/Type.html#getInput()">getInput</a>, <a href="../../../kerml/model/kerml/Type.html#getIntersectingType()">getIntersectingType</a>, <a href="../../../kerml/model/kerml/Type.html#getMultiplicity()">getMultiplicity</a>, <a href="../../../kerml/model/kerml/Type.html#getOutput()">getOutput</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedConjugator()">getOwnedConjugator</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedDifferencing()">getOwnedDifferencing</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedDisjoining()">getOwnedDisjoining</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedEndFeature()">getOwnedEndFeature</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedFeature()">getOwnedFeature</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedFeatureMembership()">getOwnedFeatureMembership</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedIntersecting()">getOwnedIntersecting</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedSpecialization()">getOwnedSpecialization</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedUnioning()">getOwnedUnioning</a>, <a href="../../../kerml/model/kerml/Type.html#getUnioningType()">getUnioningType</a>, <a href="../../../kerml/model/kerml/Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)">inheritableMemberships</a>, <a href="../../../kerml/model/kerml/Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)">inheritedMemberships</a>, <a href="../../../kerml/model/kerml/Type.html#isAbstract()">isAbstract</a>, <a href="../../../kerml/model/kerml/Type.html#isConjugated()">isConjugated</a>, <a href="../../../kerml/model/kerml/Type.html#isSufficient()">isSufficient</a>, <a href="../../../kerml/model/kerml/Type.html#multiplicities()">multiplicities</a>, <a href="../../../kerml/model/kerml/Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)">nonPrivateMemberships</a>, <a href="../../../kerml/model/kerml/Type.html#removeRedefinedFeatures(java.util.List)">removeRedefinedFeatures</a>, <a href="../../../kerml/model/kerml/Type.html#setIsAbstract(boolean)">setIsAbstract</a>, <a href="../../../kerml/model/kerml/Type.html#setIsSufficient(boolean)">setIsSufficient</a>, <a href="../../../kerml/model/kerml/Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">specializes</a>, <a href="../../../kerml/model/kerml/Type.html#specializesFromLibrary(java.lang.String)">specializesFromLibrary</a>, <a href="../../../kerml/model/kerml/Type.html#visibleMemberships(java.util.List,boolean,boolean)">visibleMemberships</a></code></div>
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
<section class="detail" id="getKind()">
<h3>getKind</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a></span> <span class="element-name">getKind</span>()</div>
<div class="block"><p>Indicates which of the <code>Functions</code> from the <code><em>Triggers</em></code> model in the Kernel Semantic Library is to be invoked by this <code>TriggerInvocationExpression</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the kind value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setKind(com.dassault_systemes.modeler.sysml.model.sysml.TriggerKind)">
<h3>setKind</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setKind</span><wbr/><span class="parameters">(@CheckForNull
 <a href="TriggerKind.html" title="class in com.dassault_systemes.modeler.sysml.model.sysml">TriggerKind</a> value)</span></div>
<div class="block"><p>Indicates which of the <code>Functions</code> from the <code><em>Triggers</em></code> model in the Kernel Semantic Library is to be invoked by this <code>TriggerInvocationExpression</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the kind value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="instantiatedType()">
<h3>instantiatedType</h3>
<div class="member-signature"><span class="return-type"><a href="../../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">instantiatedType</span>()</div>
<div class="block"><p>Return one of the <code>Functions</code> <em><code>TriggerWhen</code></em>, <em><code>TriggerAt</code></em> or <em><code>TriggerAfter</code></em>, from the Kernel Semantic Library <em><code>Triggers</code></em> package, depending on whether the <code>kind</code> of this <code>TriggerInvocationExpression</code> is <code>when</code>, <code>at</code> or <code>after</code>, respectively.</p>
 resolveGlobal(
     if kind = TriggerKind::when then
         'Triggers::TriggerWhen'
     else if kind = TriggerKind::at then
         'Triggers::TriggerAt'
     else
         'Triggers::TriggerAfter'
     endif endif
 ).memberElement.oclAsType(Type)</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/model/kerml/InstantiationExpression.html#instantiatedType()">instantiatedType</a></code> in interface <code><a href="../../../kerml/model/kerml/InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InstantiationExpression</a></code></dd>
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
