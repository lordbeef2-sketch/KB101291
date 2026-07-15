# JAVA OPENAPI: Usage (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/sysml/Usage.html
- source_path: `com/dassault_systemes/modeler/sysml/model/sysml/Usage.html`
- source_sha256: `bc626d0f1160c356d40c53fe3c9c8031aa07ceb63940dd9130ee278025851095`
- captured_utc: `2026-07-14T16:45:05.099070+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model.sysml](package-summary.html)

## Interface Usage

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../../kerml/model/kerml/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[Feature](../../../kerml/model/kerml/Feature.html)`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `[Namespace](../../../kerml/model/kerml/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[Type](../../../kerml/model/kerml/Type.html)`

All Known Subinterfaces:
`[AcceptActionUsage](AcceptActionUsage.html)`, `[ActionUsage](ActionUsage.html)`, `[AllocationUsage](AllocationUsage.html)`, `[AnalysisCaseUsage](AnalysisCaseUsage.html)`, `[AssertConstraintUsage](AssertConstraintUsage.html)`, `[AssignmentActionUsage](AssignmentActionUsage.html)`, `[AttributeUsage](AttributeUsage.html)`, `[BindingConnectorAsUsage](BindingConnectorAsUsage.html)`, `[CalculationUsage](CalculationUsage.html)`, `[CaseUsage](CaseUsage.html)`, `[ConcernUsage](ConcernUsage.html)`, `[ConnectionUsage](ConnectionUsage.html)`, `[ConnectorAsUsage](ConnectorAsUsage.html)`, `[ConstraintUsage](ConstraintUsage.html)`, `[ControlNode](ControlNode.html)`, `[DecisionNode](DecisionNode.html)`, `[EnumerationUsage](EnumerationUsage.html)`, `[EventOccurrenceUsage](EventOccurrenceUsage.html)`, `[ExhibitStateUsage](ExhibitStateUsage.html)`, `[FlowUsage](FlowUsage.html)`, `[ForkNode](ForkNode.html)`, `[ForLoopActionUsage](ForLoopActionUsage.html)`, `[IfActionUsage](IfActionUsage.html)`, `[IncludeUseCaseUsage](IncludeUseCaseUsage.html)`, `[InterfaceUsage](InterfaceUsage.html)`, `[ItemUsage](ItemUsage.html)`, `[JoinNode](JoinNode.html)`, `[LoopActionUsage](LoopActionUsage.html)`, `[MergeNode](MergeNode.html)`, `[MetadataUsage](MetadataUsage.html)`, `[OccurrenceUsage](OccurrenceUsage.html)`, `[PartUsage](PartUsage.html)`, `[PerformActionUsage](PerformActionUsage.html)`, `[PortUsage](PortUsage.html)`, `[ReferenceUsage](ReferenceUsage.html)`, `[RenderingUsage](RenderingUsage.html)`, `[RequirementUsage](RequirementUsage.html)`, `[SatisfyRequirementUsage](SatisfyRequirementUsage.html)`, `[SendActionUsage](SendActionUsage.html)`, `[StateUsage](StateUsage.html)`, `[SuccessionAsUsage](SuccessionAsUsage.html)`, `[SuccessionFlowUsage](SuccessionFlowUsage.html)`, `[TerminateActionUsage](TerminateActionUsage.html)`, `[TransitionUsage](TransitionUsage.html)`, `[UseCaseUsage](UseCaseUsage.html)`, `[VerificationCaseUsage](VerificationCaseUsage.html)`, `[ViewpointUsage](ViewpointUsage.html)`, `[ViewUsage](ViewUsage.html)`, `[WhileLoopActionUsage](WhileLoopActionUsage.html)`

@OpenApiAllpublic interfaceUsageextends [Feature](../../../kerml/model/kerml/Feature.html)

A `Usage` is a usage of a `Definition`.
A `Usage` may have `nestedUsages` that model `features` that apply in the context of the `owningUsage`. A `Usage` may also have `Definitions` nested in it, but this has no semantic significance, other than the nested scoping resulting from the `Usage` being considered as a `Namespace` for any nested `Definitions`.
However, if a `Usage` has `isVariation = true`, then it represents a *variation point* `Usage`. In this case, all of its `members` must be `variant` `Usages`, related to the `Usage` by `VariantMembership` `Relationships`. Rather than being `features` of the `Usage`, `variant` `Usages` model different concrete alternatives that can be chosen to fill in for the variation point `Usage`.
 variant = variantMembership.ownedVariantUsage
 variantMembership = ownedMembership->selectByKind(VariantMembership)
 isVariation implies ownedFeatureMembership->isEmpty()
 isReference = not isComposite
 owningVariationUsage <> null implies
 specializes(owningVariationUsage)
 isVariation implies
 not ownedSpecialization.specific->exists(
 oclIsKindOf(Definition) and
 oclAsType(Definition).isVariation or
 oclIsKindOf(Usage) and
 oclAsType(Usage).isVariation)
 owningVariationDefinition <> null implies
 specializes(owningVariationDefinition)
 directedUsage = directedFeature->selectByKind(Usage)
 nestedAction = nestedUsage->selectByKind(ActionUsage)
 nestedAllocation = nestedUsage->selectByKind(AllocationUsage)
 nestedAnalysisCase = nestedUsage->selectByKind(AnalysisCaseUsage)
 nestedAttribute = nestedUsage->selectByKind(AttributeUsage)
 nestedCalculation = nestedUsage->selectByKind(CalculationUsage)
 nestedCase = nestedUsage->selectByKind(CaseUsage)
 nestedConcern = nestedUsage->selectByKind(ConcernUsage)
 nestedConnection = nestedUsage->selectByKind(ConnectorAsUsage)
 nestedConstraint = nestedUsage->selectByKind(ConstraintUsage)
 ownedNested = nestedUsage->selectByKind(EnumerationUsage)
 nestedFlow = nestedUsage->selectByKind(FlowConnectionUsage)
 nestedInterface = nestedUsage->selectByKind(ReferenceUsage)
 nestedItem = nestedUsage->selectByKind(ItemUsage)
 nestedMetadata = nestedUsage->selectByKind(MetadataUsage)
 nestedOccurrence = nestedUsage->selectByKind(OccurrenceUsage)
 nestedPart = nestedUsage->selectByKind(PartUsage)
 nestedPort = nestedUsage->selectByKind(PortUsage)
 nestedReference = nestedUsage->selectByKind(ReferenceUsage)
 nestedRendering = nestedUsage->selectByKind(RenderingUsage)
 nestedRequirement = nestedUsage->selectByKind(RequirementUsage)
 nestedState = nestedUsage->selectByKind(StateUsage)
 nestedTransition = nestedUsage->selectByKind(TransitionUsage)
 nestedUsage = ownedFeature->selectByKind(Usage)
 nestedUseCase = nestedUsage->selectByKind(UseCaseUsage)
 nestedVerificationCase = nestedUsage->selectByKind(VerificationCaseUsage)
 nestedView = nestedUsage->selectByKind(ViewUsage)
 nestedViewpoint = nestedUsage->selectByKind(ViewpointUsage)
 usage = feature->selectByKind(Usage)
 direction <> null or isEnd or featuringType->isEmpty() implies
 isReference
 isVariation implies isAbstract
 mayTimeVary =
 owningType <> null and
 owningType.specializesFromLibrary('Occurrences::Occurrence') and
 not (
 isPortion or
 specializesFromLibrary('Links::SelfLink') or
 specializesFromLibrary('Occurrences::HappensLink') or
 isComposite and specializesFromLibrary('Actions::Action')
 )
 owningVariationUsage <> null implies
 featuringType->asSet() = owningVariationUsage.featuringType->asSet()

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](../../../kerml/model/kerml/Classifier.html)>`
`[getDefinition](#getDefinition())()`
The `Classifiers` that are the types of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)>`
`[getDirectedUsage](#getDirectedUsage())()`
The `usages` of this `Usage` that are `directedFeatures`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ActionUsage](ActionUsage.html)>`
`[getNestedAction](#getNestedAction())()`
The `ActionUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[AllocationUsage](AllocationUsage.html)>`
`[getNestedAllocation](#getNestedAllocation())()`
The `AllocationUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[AnalysisCaseUsage](AnalysisCaseUsage.html)>`
`[getNestedAnalysisCase](#getNestedAnalysisCase())()`
The `AnalysisCaseUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[AttributeUsage](AttributeUsage.html)>`
`[getNestedAttribute](#getNestedAttribute())()`
The code>AttributeUsages that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CalculationUsage](CalculationUsage.html)>`
`[getNestedCalculation](#getNestedCalculation())()`
The `CalculationUsage` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CaseUsage](CaseUsage.html)>`
`[getNestedCase](#getNestedCase())()`
The `CaseUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConcernUsage](ConcernUsage.html)>`
`[getNestedConcern](#getNestedConcern())()`
The `ConcernUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConnectorAsUsage](ConnectorAsUsage.html)>`
`[getNestedConnection](#getNestedConnection())()`
The `ConnectorAsUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConstraintUsage](ConstraintUsage.html)>`
`[getNestedConstraint](#getNestedConstraint())()`
The `ConstraintUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[EnumerationUsage](EnumerationUsage.html)>`
`[getNestedEnumeration](#getNestedEnumeration())()`
The code>EnumerationUsages that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FlowUsage](FlowUsage.html)>`
`[getNestedFlow](#getNestedFlow())()`
The code>FlowUsages that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[InterfaceUsage](InterfaceUsage.html)>`
`[getNestedInterface](#getNestedInterface())()`
The `InterfaceUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ItemUsage](ItemUsage.html)>`
`[getNestedItem](#getNestedItem())()`
The `ItemUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataUsage](MetadataUsage.html)>`
`[getNestedMetadata](#getNestedMetadata())()`
The `MetadataUsages` that are `nestedUsages` of this of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[OccurrenceUsage](OccurrenceUsage.html)>`
`[getNestedOccurrence](#getNestedOccurrence())()`
The `OccurrenceUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](PartUsage.html)>`
`[getNestedPart](#getNestedPart())()`
The `PartUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PortUsage](PortUsage.html)>`
`[getNestedPort](#getNestedPort())()`
The `PortUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ReferenceUsage](ReferenceUsage.html)>`
`[getNestedReference](#getNestedReference())()`
The `ReferenceUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RenderingUsage](RenderingUsage.html)>`
`[getNestedRendering](#getNestedRendering())()`
The `RenderingUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RequirementUsage](RequirementUsage.html)>`
`[getNestedRequirement](#getNestedRequirement())()`
The `RequirementUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[StateUsage](StateUsage.html)>`
`[getNestedState](#getNestedState())()`
The `StateUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[TransitionUsage](TransitionUsage.html)>`
`[getNestedTransition](#getNestedTransition())()`
The `TransitionUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)>`
`[getNestedUsage](#getNestedUsage())()`
The `Usages` that are `ownedFeatures` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[UseCaseUsage](UseCaseUsage.html)>`
`[getNestedUseCase](#getNestedUseCase())()`
The `UseCaseUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[VerificationCaseUsage](VerificationCaseUsage.html)>`
`[getNestedVerificationCase](#getNestedVerificationCase())()`
The `VerificationCaseUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ViewUsage](ViewUsage.html)>`
`[getNestedView](#getNestedView())()`
The `ViewUsages` that are `nestedUsages` of this `Usage`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ViewpointUsage](ViewpointUsage.html)>`
`[getNestedViewpoint](#getNestedViewpoint())()`
The `ViewpointUsages` that are `nestedUsages` of this `Usage`.
`[Definition](Definition.html)`
`[getOwningDefinition](#getOwningDefinition())()`
The `Definition` that owns this `Usage` (if any).
`[Usage](Usage.html)`
`[getOwningUsage](#getOwningUsage())()`
The `Usage` in which this `Usage` is nested (if any).
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)>`
`[getUsage](#getUsage())()`
The `Usages` that are `features` of this `Usage` (not necessarily owned).
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)>`
`[getVariant](#getVariant())()`
The `Usages` which represent the variants of this `Usage` as a variation point `Usage`, if `isVariation = true`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[VariantMembership](VariantMembership.html)>`
`[getVariantMembership](#getVariantMembership())()`
The `ownedMemberships` of this `Usage` that are `VariantMemberships`.
`boolean`
`[isMayTimeVary](#isMayTimeVary())()`
Whether this `Usage` may be time varying (that is, whether it is featured by the snapshots of its `owningType`, rather than being featured by the `owningType` itself).
`boolean`
`[isReference](#isReference())()`
Whether this `Usage` is a referential `Usage`, that is, it has `isComposite = false`.
`boolean`
`[isVariation](#isVariation())()`
Whether this `Usage` is for a variation point or not.
`[Feature](../../../kerml/model/kerml/Feature.html)`
`[namingFeature](#namingFeature())()`
If this `Usage` is a variant, then its naming `Feature` is the `referencedFeature` of its `ownedReferenceSubsetting`.
`[Feature](../../../kerml/model/kerml/Feature.html)`
`[referencedFeatureTarget](#referencedFeatureTarget())()`
If `ownedReferenceSubsetting` is not null, return the `featureTarget` of the `referencedFeature` of the `ownedReferenceSubsetting`.
`void`
`[setIsReference](#setIsReference(boolean))(boolean value)`
Whether this `Usage` is a referential `Usage`, that is, it has `isComposite = false`.
`void`
`[setIsVariation](#setIsVariation(boolean))(boolean value)`
Whether this `Usage` is for a variation point or not.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](../../../kerml/model/kerml/Element.html)
`[escapedName](../../../kerml/model/kerml/Element.html#escapedName()), [getAliasIds](../../../kerml/model/kerml/Element.html#getAliasIds()), [getDeclaredName](../../../kerml/model/kerml/Element.html#getDeclaredName()), [getDeclaredShortName](../../../kerml/model/kerml/Element.html#getDeclaredShortName()), [getDocumentation](../../../kerml/model/kerml/Element.html#getDocumentation()), [getElementId](../../../kerml/model/kerml/Element.html#getElementId()), [getName](../../../kerml/model/kerml/Element.html#getName()), [getOwnedAnnotation](../../../kerml/model/kerml/Element.html#getOwnedAnnotation()), [getOwnedElement](../../../kerml/model/kerml/Element.html#getOwnedElement()), [getOwnedRelationship](../../../kerml/model/kerml/Element.html#getOwnedRelationship()), [getOwner](../../../kerml/model/kerml/Element.html#getOwner()), [getOwningMembership](../../../kerml/model/kerml/Element.html#getOwningMembership()), [getOwningNamespace](../../../kerml/model/kerml/Element.html#getOwningNamespace()), [getOwningRelationship](../../../kerml/model/kerml/Element.html#getOwningRelationship()), [getQualifiedName](../../../kerml/model/kerml/Element.html#getQualifiedName()), [getShortName](../../../kerml/model/kerml/Element.html#getShortName()), [getTextualRepresentation](../../../kerml/model/kerml/Element.html#getTextualRepresentation()), [isImpliedIncluded](../../../kerml/model/kerml/Element.html#isImpliedIncluded()), [isLibraryElement](../../../kerml/model/kerml/Element.html#isLibraryElement()), [libraryNamespace](../../../kerml/model/kerml/Element.html#libraryNamespace()), [path](../../../kerml/model/kerml/Element.html#path()), [setDeclaredName](../../../kerml/model/kerml/Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](../../../kerml/model/kerml/Element.html#setDeclaredShortName(java.lang.String)), [setElementId](../../../kerml/model/kerml/Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](../../../kerml/model/kerml/Element.html#setIsImpliedIncluded(boolean)), [setOwner](../../../kerml/model/kerml/Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](../../../kerml/model/kerml/Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](../../../kerml/model/kerml/Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Feature](../../../kerml/model/kerml/Feature.html)
`[allRedefinedFeatures](../../../kerml/model/kerml/Feature.html#allRedefinedFeatures()), [asCartesianProduct](../../../kerml/model/kerml/Feature.html#asCartesianProduct()), [canAccess](../../../kerml/model/kerml/Feature.html#canAccess(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [directionFor](../../../kerml/model/kerml/Feature.html#directionFor(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [effectiveName](../../../kerml/model/kerml/Feature.html#effectiveName()), [effectiveShortName](../../../kerml/model/kerml/Feature.html#effectiveShortName()), [getChainingFeature](../../../kerml/model/kerml/Feature.html#getChainingFeature()), [getCrossFeature](../../../kerml/model/kerml/Feature.html#getCrossFeature()), [getDirection](../../../kerml/model/kerml/Feature.html#getDirection()), [getEndOwningType](../../../kerml/model/kerml/Feature.html#getEndOwningType()), [getFeatureTarget](../../../kerml/model/kerml/Feature.html#getFeatureTarget()), [getFeaturingType](../../../kerml/model/kerml/Feature.html#getFeaturingType()), [getOwnedCrossSubsetting](../../../kerml/model/kerml/Feature.html#getOwnedCrossSubsetting()), [getOwnedFeatureChaining](../../../kerml/model/kerml/Feature.html#getOwnedFeatureChaining()), [getOwnedFeatureInverting](../../../kerml/model/kerml/Feature.html#getOwnedFeatureInverting()), [getOwnedRedefinition](../../../kerml/model/kerml/Feature.html#getOwnedRedefinition()), [getOwnedReferenceSubsetting](../../../kerml/model/kerml/Feature.html#getOwnedReferenceSubsetting()), [getOwnedSubsetting](../../../kerml/model/kerml/Feature.html#getOwnedSubsetting()), [getOwnedTypeFeaturing](../../../kerml/model/kerml/Feature.html#getOwnedTypeFeaturing()), [getOwnedTyping](../../../kerml/model/kerml/Feature.html#getOwnedTyping()), [getOwningFeatureMembership](../../../kerml/model/kerml/Feature.html#getOwningFeatureMembership()), [getOwningType](../../../kerml/model/kerml/Feature.html#getOwningType()), [getType](../../../kerml/model/kerml/Feature.html#getType()), [isCartesianProduct](../../../kerml/model/kerml/Feature.html#isCartesianProduct()), [isCompatibleWith](../../../kerml/model/kerml/Feature.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isComposite](../../../kerml/model/kerml/Feature.html#isComposite()), [isConstant](../../../kerml/model/kerml/Feature.html#isConstant()), [isDerived](../../../kerml/model/kerml/Feature.html#isDerived()), [isEnd](../../../kerml/model/kerml/Feature.html#isEnd()), [isFeaturedWithin](../../../kerml/model/kerml/Feature.html#isFeaturedWithin(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isFeaturingType](../../../kerml/model/kerml/Feature.html#isFeaturingType(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isOrdered](../../../kerml/model/kerml/Feature.html#isOrdered()), [isOwnedCrossFeature](../../../kerml/model/kerml/Feature.html#isOwnedCrossFeature()), [isPortion](../../../kerml/model/kerml/Feature.html#isPortion()), [isUnique](../../../kerml/model/kerml/Feature.html#isUnique()), [isVariable](../../../kerml/model/kerml/Feature.html#isVariable()), [ownedCrossFeature](../../../kerml/model/kerml/Feature.html#ownedCrossFeature()), [redefines](../../../kerml/model/kerml/Feature.html#redefines(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [redefinesFromLibrary](../../../kerml/model/kerml/Feature.html#redefinesFromLibrary(java.lang.String)), [setDirection](../../../kerml/model/kerml/Feature.html#setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)), [setIsComposite](../../../kerml/model/kerml/Feature.html#setIsComposite(boolean)), [setIsConstant](../../../kerml/model/kerml/Feature.html#setIsConstant(boolean)), [setIsDerived](../../../kerml/model/kerml/Feature.html#setIsDerived(boolean)), [setIsEnd](../../../kerml/model/kerml/Feature.html#setIsEnd(boolean)), [setIsOrdered](../../../kerml/model/kerml/Feature.html#setIsOrdered(boolean)), [setIsPortion](../../../kerml/model/kerml/Feature.html#setIsPortion(boolean)), [setIsUnique](../../../kerml/model/kerml/Feature.html#setIsUnique(boolean)), [setIsVariable](../../../kerml/model/kerml/Feature.html#setIsVariable(boolean)), [subsetsChain](../../../kerml/model/kerml/Feature.html#subsetsChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [supertypes](../../../kerml/model/kerml/Feature.html#supertypes(boolean)), [typingFeatures](../../../kerml/model/kerml/Feature.html#typingFeatures())`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject
`getModelExtension, getModelExtension`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Namespace](../../../kerml/model/kerml/Namespace.html)
`[getImportedMembership](../../../kerml/model/kerml/Namespace.html#getImportedMembership()), [getMember](../../../kerml/model/kerml/Namespace.html#getMember()), [getMembership](../../../kerml/model/kerml/Namespace.html#getMembership()), [getOwnedImport](../../../kerml/model/kerml/Namespace.html#getOwnedImport()), [getOwnedMember](../../../kerml/model/kerml/Namespace.html#getOwnedMember()), [getOwnedMembership](../../../kerml/model/kerml/Namespace.html#getOwnedMembership()), [importedMemberships](../../../kerml/model/kerml/Namespace.html#importedMemberships(java.util.List)), [membershipsOfVisibility](../../../kerml/model/kerml/Namespace.html#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)), [namesOf](../../../kerml/model/kerml/Namespace.html#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [qualificationOf](../../../kerml/model/kerml/Namespace.html#qualificationOf(java.lang.String)), [resolve](../../../kerml/model/kerml/Namespace.html#resolve(java.lang.String)), [resolveGlobal](../../../kerml/model/kerml/Namespace.html#resolveGlobal(java.lang.String)), [resolveLocal](../../../kerml/model/kerml/Namespace.html#resolveLocal(java.lang.String)), [resolveVisible](../../../kerml/model/kerml/Namespace.html#resolveVisible(java.lang.String)), [unqualifiedNameOf](../../../kerml/model/kerml/Namespace.html#unqualifiedNameOf(java.lang.String)), [visibilityOf](../../../kerml/model/kerml/Namespace.html#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Type](../../../kerml/model/kerml/Type.html)
`[allRedefinedFeaturesOf](../../../kerml/model/kerml/Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)), [allSupertypes](../../../kerml/model/kerml/Type.html#allSupertypes()), [directionOf](../../../kerml/model/kerml/Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [directionOfExcluding](../../../kerml/model/kerml/Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)), [getDifferencingType](../../../kerml/model/kerml/Type.html#getDifferencingType()), [getDirectedFeature](../../../kerml/model/kerml/Type.html#getDirectedFeature()), [getEndFeature](../../../kerml/model/kerml/Type.html#getEndFeature()), [getFeature](../../../kerml/model/kerml/Type.html#getFeature()), [getFeatureMembership](../../../kerml/model/kerml/Type.html#getFeatureMembership()), [getInheritedFeature](../../../kerml/model/kerml/Type.html#getInheritedFeature()), [getInheritedMembership](../../../kerml/model/kerml/Type.html#getInheritedMembership()), [getInput](../../../kerml/model/kerml/Type.html#getInput()), [getIntersectingType](../../../kerml/model/kerml/Type.html#getIntersectingType()), [getMultiplicity](../../../kerml/model/kerml/Type.html#getMultiplicity()), [getOutput](../../../kerml/model/kerml/Type.html#getOutput()), [getOwnedConjugator](../../../kerml/model/kerml/Type.html#getOwnedConjugator()), [getOwnedDifferencing](../../../kerml/model/kerml/Type.html#getOwnedDifferencing()), [getOwnedDisjoining](../../../kerml/model/kerml/Type.html#getOwnedDisjoining()), [getOwnedEndFeature](../../../kerml/model/kerml/Type.html#getOwnedEndFeature()), [getOwnedFeature](../../../kerml/model/kerml/Type.html#getOwnedFeature()), [getOwnedFeatureMembership](../../../kerml/model/kerml/Type.html#getOwnedFeatureMembership()), [getOwnedIntersecting](../../../kerml/model/kerml/Type.html#getOwnedIntersecting()), [getOwnedSpecialization](../../../kerml/model/kerml/Type.html#getOwnedSpecialization()), [getOwnedUnioning](../../../kerml/model/kerml/Type.html#getOwnedUnioning()), [getUnioningType](../../../kerml/model/kerml/Type.html#getUnioningType()), [inheritableMemberships](../../../kerml/model/kerml/Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)), [inheritedMemberships](../../../kerml/model/kerml/Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)), [isAbstract](../../../kerml/model/kerml/Type.html#isAbstract()), [isConjugated](../../../kerml/model/kerml/Type.html#isConjugated()), [isSufficient](../../../kerml/model/kerml/Type.html#isSufficient()), [multiplicities](../../../kerml/model/kerml/Type.html#multiplicities()), [nonPrivateMemberships](../../../kerml/model/kerml/Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)), [removeRedefinedFeatures](../../../kerml/model/kerml/Type.html#removeRedefinedFeatures(java.util.List)), [setIsAbstract](../../../kerml/model/kerml/Type.html#setIsAbstract(boolean)), [setIsSufficient](../../../kerml/model/kerml/Type.html#setIsSufficient(boolean)), [specializes](../../../kerml/model/kerml/Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [specializesFromLibrary](../../../kerml/model/kerml/Type.html#specializesFromLibrary(java.lang.String)), [visibleMemberships](../../../kerml/model/kerml/Type.html#visibleMemberships(java.util.List,boolean,boolean))`

============ METHOD DETAIL ========== 
Method Details
isMayTimeVary
boolean isMayTimeVary()
Whether this `Usage` may be time varying (that is, whether it is featured by the snapshots of its `owningType`, rather than being featured by the `owningType` itself). However, if `isConstant` is also true, then the value of the `Usage` is nevertheless constant over the entire duration of an instance of its `owningType` (that is, it has the same value on all snapshots).
The property `mayTimeVary` redefines the KerML property `Feature::isVariable`, making it derived. The property `isConstant` is inherited from `Feature`.
Returns:
the mayTimeVary value
Model:
derived="true"
 transient="true"
isReference
boolean isReference()
Whether this `Usage` is a referential `Usage`, that is, it has `isComposite = false`.
Returns:
the isReference value
Model:
derived="true"
 transient="true"
setIsReference
void setIsReference(boolean value)
Whether this `Usage` is a referential `Usage`, that is, it has `isComposite = false`.
Parameters:
`value` - the isReference value
Model:
derived="true"
 transient="true"
getVariant
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)> getVariant()
The `Usages` which represent the variants of this `Usage` as a variation point `Usage`, if `isVariation = true`. If `isVariation = false`, then there must be no `variants`.
Returns:
the variant value
Model:
derived="true"
 transient="true"
 oppositeRoleName="owningVariationUsage"
getVariantMembership
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[VariantMembership](VariantMembership.html)> getVariantMembership()
The `ownedMemberships` of this `Usage` that are `VariantMemberships`. If `isVariation = true`, then this must be all `memberships` of the `Usage`. If `isVariation = false`, then `variantMembership`must be empty.
Returns:
the variantMembership value
Model:
derived="true"
 transient="true"
 oppositeRoleName="owningVariationUsage"
getOwningDefinition
@CheckForNull[Definition](Definition.html) getOwningDefinition()
The `Definition` that owns this `Usage` (if any).
Returns:
the owningDefinition value
Model:
derived="true"
 transient="true"
 opposite=[`Definition.getOwnedUsage()`](Definition.html#getOwnedUsage())
getOwningUsage
@CheckForNull[Usage](Usage.html) getOwningUsage()
The `Usage` in which this `Usage` is nested (if any).
Returns:
the owningUsage value
Model:
derived="true"
 transient="true"
 opposite=[`getNestedUsage()`](#getNestedUsage())
getDefinition
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](../../../kerml/model/kerml/Classifier.html)> getDefinition()
The `Classifiers` that are the types of this `Usage`. Nominally, these are `Definitions`, but other kinds of Kernel `Classifiers` are also allowed, to permit use of `Classifiers` from the Kernel Model Libraries.
Returns:
the definition value
Model:
derived="true"
 transient="true"
 oppositeRoleName="definedUsage"
getUsage
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)> getUsage()
The `Usages` that are `features` of this `Usage` (not necessarily owned).
Returns:
the usage value
Model:
derived="true"
 transient="true"
 oppositeRoleName="featuringUsage"
getDirectedUsage
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)> getDirectedUsage()
The `usages` of this `Usage` that are `directedFeatures`.
Returns:
the directedUsage value
Model:
derived="true"
 transient="true"
 oppositeRoleName="usageWithDirectedUsage"
 subsets=[`getUsage()`](#getUsage())
getNestedUsage
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)> getNestedUsage()
The `Usages` that are `ownedFeatures` of this `Usage`.
Returns:
the nestedUsage value
Model:
derived="true"
 transient="true"
 opposite=[`getOwningUsage()`](#getOwningUsage())
 subsets=[`getUsage()`](#getUsage())
getNestedReference
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ReferenceUsage](ReferenceUsage.html)> getNestedReference()
The `ReferenceUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedReference value
Model:
derived="true"
 transient="true"
 oppositeRoleName="referenceOwningUsage"
 subsets=[`getNestedUsage()`](#getNestedUsage())
getNestedAttribute
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[AttributeUsage](AttributeUsage.html)> getNestedAttribute()
The code>AttributeUsages that are `nestedUsages` of this `Usage`.
Returns:
the nestedAttribute value
Model:
derived="true"
 transient="true"
 oppositeRoleName="attributeOwningUsage"
 subsets=[`getNestedUsage()`](#getNestedUsage())
getNestedEnumeration
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[EnumerationUsage](EnumerationUsage.html)> getNestedEnumeration()
The code>EnumerationUsages that are `nestedUsages` of this `Usage`.
Returns:
the nestedEnumeration value
Model:
derived="true"
 transient="true"
 oppositeRoleName="enumerationOwningUsage"
 subsets=[`getNestedAttribute()`](#getNestedAttribute())
getNestedOccurrence
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[OccurrenceUsage](OccurrenceUsage.html)> getNestedOccurrence()
The `OccurrenceUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedOccurrence value
Model:
derived="true"
 transient="true"
 oppositeRoleName="occurrenceOwningUsage"
 subsets=[`getNestedUsage()`](#getNestedUsage())
getNestedItem
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ItemUsage](ItemUsage.html)> getNestedItem()
The `ItemUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedItem value
Model:
derived="true"
 transient="true"
 oppositeRoleName="itemOwningUsage"
 subsets=[`getNestedOccurrence()`](#getNestedOccurrence())
getNestedPart
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](PartUsage.html)> getNestedPart()
The `PartUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedPart value
Model:
derived="true"
 transient="true"
 oppositeRoleName="partOwningUsage"
 subsets=[`getNestedItem()`](#getNestedItem())
getNestedPort
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PortUsage](PortUsage.html)> getNestedPort()
The `PortUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedPort value
Model:
derived="true"
 transient="true"
 oppositeRoleName="portOwningUsage"
 subsets=[`getNestedUsage()`](#getNestedUsage())
getNestedConnection
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConnectorAsUsage](ConnectorAsUsage.html)> getNestedConnection()
The `ConnectorAsUsages` that are `nestedUsages` of this `Usage`. Note that this list includes `BindingConnectorAsUsages`, `SuccessionAsUsages`, and `FlowConnectionUsages` because these are `ConnectorAsUsages` even though they are not `ConnectionUsages`.
Returns:
the nestedConnection value
Model:
derived="true"
 transient="true"
 oppositeRoleName="connectionOwningUsage"
 subsets=[`getNestedUsage()`](#getNestedUsage())
getNestedFlow
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FlowUsage](FlowUsage.html)> getNestedFlow()
The code>FlowUsages that are `nestedUsages` of this `Usage`.
Returns:
the nestedFlow value
Model:
derived="true"
 transient="true"
 oppositeRoleName="flowOwningUsage"
 subsets=[`getNestedConnection()`](#getNestedConnection())
getNestedInterface
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[InterfaceUsage](InterfaceUsage.html)> getNestedInterface()
The `InterfaceUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedInterface value
Model:
derived="true"
 transient="true"
 oppositeRoleName="interfaceOwningUsage"
 subsets=[`getNestedConnection()`](#getNestedConnection())
getNestedAllocation
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[AllocationUsage](AllocationUsage.html)> getNestedAllocation()
The `AllocationUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedAllocation value
Model:
derived="true"
 transient="true"
 oppositeRoleName="allocationOwningUsage"
 subsets=[`getNestedConnection()`](#getNestedConnection())
getNestedAction
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ActionUsage](ActionUsage.html)> getNestedAction()
The `ActionUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedAction value
Model:
derived="true"
 transient="true"
 oppositeRoleName="actionOwningUsage"
 subsets=[`getNestedOccurrence()`](#getNestedOccurrence())
getNestedState
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[StateUsage](StateUsage.html)> getNestedState()
The `StateUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedState value
Model:
derived="true"
 transient="true"
 oppositeRoleName="stateOwningUsage"
 subsets=[`getNestedAction()`](#getNestedAction())
getNestedTransition
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[TransitionUsage](TransitionUsage.html)> getNestedTransition()
The `TransitionUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedTransition value
Model:
derived="true"
 transient="true"
 oppositeRoleName="transitionOwningUsage"
 subsets=[`getNestedUsage()`](#getNestedUsage())
getNestedCalculation
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CalculationUsage](CalculationUsage.html)> getNestedCalculation()
The `CalculationUsage` that are `nestedUsages` of this `Usage`.
Returns:
the nestedCalculation value
Model:
derived="true"
 transient="true"
 oppositeRoleName="calculationOwningUsage"
 subsets=[`getNestedAction()`](#getNestedAction())
getNestedConstraint
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConstraintUsage](ConstraintUsage.html)> getNestedConstraint()
The `ConstraintUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedConstraint value
Model:
derived="true"
 transient="true"
 oppositeRoleName="constraintOwningUsage"
 subsets=[`getNestedOccurrence()`](#getNestedOccurrence())
getNestedRequirement
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RequirementUsage](RequirementUsage.html)> getNestedRequirement()
The `RequirementUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedRequirement value
Model:
derived="true"
 transient="true"
 oppositeRoleName="requirementOwningUsage"
 subsets=[`getNestedConstraint()`](#getNestedConstraint())
getNestedConcern
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConcernUsage](ConcernUsage.html)> getNestedConcern()
The `ConcernUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedConcern value
Model:
derived="true"
 transient="true"
 oppositeRoleName="concernOwningUsage"
 subsets=[`getNestedRequirement()`](#getNestedRequirement())
getNestedCase
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CaseUsage](CaseUsage.html)> getNestedCase()
The `CaseUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedCase value
Model:
derived="true"
 transient="true"
 oppositeRoleName="caseOwningUsage"
 subsets=[`getNestedCalculation()`](#getNestedCalculation())
getNestedAnalysisCase
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[AnalysisCaseUsage](AnalysisCaseUsage.html)> getNestedAnalysisCase()
The `AnalysisCaseUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedAnalysisCase value
Model:
derived="true"
 transient="true"
 oppositeRoleName="analysisCaseOwningUsage"
 subsets=[`getNestedCase()`](#getNestedCase())
getNestedVerificationCase
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[VerificationCaseUsage](VerificationCaseUsage.html)> getNestedVerificationCase()
The `VerificationCaseUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedVerificationCase value
Model:
derived="true"
 transient="true"
 oppositeRoleName="verificationCaseOwningUsage"
 subsets=[`getNestedCase()`](#getNestedCase())
getNestedUseCase
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[UseCaseUsage](UseCaseUsage.html)> getNestedUseCase()
The `UseCaseUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedUseCase value
Model:
derived="true"
 transient="true"
 oppositeRoleName="useCaseOwningUsage"
 subsets=[`getNestedCase()`](#getNestedCase())
getNestedView
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ViewUsage](ViewUsage.html)> getNestedView()
The `ViewUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedView value
Model:
derived="true"
 transient="true"
 oppositeRoleName="viewOwningUsage"
 subsets=[`getNestedPart()`](#getNestedPart())
getNestedViewpoint
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ViewpointUsage](ViewpointUsage.html)> getNestedViewpoint()
The `ViewpointUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedViewpoint value
Model:
derived="true"
 transient="true"
 oppositeRoleName="viewpointOwningUsage"
 subsets=[`getNestedRequirement()`](#getNestedRequirement())
getNestedRendering
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RenderingUsage](RenderingUsage.html)> getNestedRendering()
The `RenderingUsages` that are `nestedUsages` of this `Usage`.
Returns:
the nestedRendering value
Model:
derived="true"
 transient="true"
 oppositeRoleName="renderingOwningUsage"
 subsets=[`getNestedPart()`](#getNestedPart())
getNestedMetadata
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataUsage](MetadataUsage.html)> getNestedMetadata()
The `MetadataUsages` that are `nestedUsages` of this of this `Usage`.
Returns:
the nestedMetadata value
Model:
derived="true"
 transient="true"
 oppositeRoleName="metadataOwningUsage"
 subsets=[`getNestedItem()`](#getNestedItem())
isVariation
boolean isVariation()
Whether this `Usage` is for a variation point or not. If true, then all the `memberships` of the `Usage` must be `VariantMemberships`.
Returns:
the isVariation value
Model:
derived="false"
 transient="false"
setIsVariation
void setIsVariation(boolean value)
Whether this `Usage` is for a variation point or not. If true, then all the `memberships` of the `Usage` must be `VariantMemberships`.
Parameters:
`value` - the isVariation value
Model:
derived="false"
 transient="false"
namingFeature
[Feature](../../../kerml/model/kerml/Feature.html) namingFeature()
If this `Usage` is a variant, then its naming `Feature` is the `referencedFeature` of its `ownedReferenceSubsetting`.
 if not owningMembership.oclIsKindOf(VariantMembership) then
 self.oclAsType(Feature).namingFeature()
 else if ownedReferenceSubsetting = null then null
 else ownedReferenceSubsetting.referencedFeature
 endif endif
Specified by:
`[namingFeature](../../../kerml/model/kerml/Feature.html#namingFeature())` in interface `[Feature](../../../kerml/model/kerml/Feature.html)`
referencedFeatureTarget
[Feature](../../../kerml/model/kerml/Feature.html) referencedFeatureTarget()
If `ownedReferenceSubsetting` is not null, return the `featureTarget` of the `referencedFeature` of the `ownedReferenceSubsetting`.
 if ownedReferenceSubsetting = null then null
 else ownedReferenceSubsetting.referencedFeature.featureTarget
 endif

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model.sysml</a></div>
<h1 class="title" title="Interface Usage">Interface Usage</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code><a href="../../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a></code>, <code><a href="ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></code>, <code><a href="AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a></code>, <code><a href="AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a></code>, <code><a href="AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssertConstraintUsage</a></code>, <code><a href="AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a></code>, <code><a href="AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a></code>, <code><a href="BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">BindingConnectorAsUsage</a></code>, <code><a href="CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a></code>, <code><a href="CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a></code>, <code><a href="ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a></code>, <code><a href="ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionUsage</a></code>, <code><a href="ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a></code>, <code><a href="ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a></code>, <code><a href="ControlNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ControlNode</a></code>, <code><a href="DecisionNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">DecisionNode</a></code>, <code><a href="EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a></code>, <code><a href="EventOccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EventOccurrenceUsage</a></code>, <code><a href="ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ExhibitStateUsage</a></code>, <code><a href="FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a></code>, <code><a href="ForkNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForkNode</a></code>, <code><a href="ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a></code>, <code><a href="IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a></code>, <code><a href="IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IncludeUseCaseUsage</a></code>, <code><a href="InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a></code>, <code><a href="ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a></code>, <code><a href="JoinNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">JoinNode</a></code>, <code><a href="LoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">LoopActionUsage</a></code>, <code><a href="MergeNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MergeNode</a></code>, <code><a href="MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a></code>, <code><a href="OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a></code>, <code><a href="PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a></code>, <code><a href="PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a></code>, <code><a href="PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a></code>, <code><a href="ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a></code>, <code><a href="RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a></code>, <code><a href="RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></code>, <code><a href="SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SatisfyRequirementUsage</a></code>, <code><a href="SendActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SendActionUsage</a></code>, <code><a href="StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a></code>, <code><a href="SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionAsUsage</a></code>, <code><a href="SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a></code>, <code><a href="TerminateActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TerminateActionUsage</a></code>, <code><a href="TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a></code>, <code><a href="UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a></code>, <code><a href="VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a></code>, <code><a href="ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a></code>, <code><a href="ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a></code>, <code><a href="WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Usage</span><span class="extends-implements">
extends <a href="../../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span></div>
<div class="block"><p>A <code>Usage</code> is a usage of a <code>Definition</code>.</p>
<p>A <code>Usage</code> may have <code>nestedUsages</code> that model <code>features</code> that apply in the context of the <code>owningUsage</code>. A <code>Usage</code> may also have <code>Definitions</code> nested in it, but this has no semantic significance, other than the nested scoping resulting from the <code>Usage</code> being considered as a <code>Namespace</code> for any nested <code>Definitions</code>.</p>
<p>However, if a <code>Usage</code> has <code>isVariation = true</code>, then it represents a <em>variation point</em> <code>Usage</code>. In this case, all of its <code>members</code> must be <code>variant</code> <code>Usages</code>, related to the <code>Usage</code> by <code>VariantMembership</code> <code>Relationships</code>. Rather than being <code>features</code> of the <code>Usage</code>, <code>variant</code> <code>Usages</code> model different concrete alternatives that can be chosen to fill in for the variation point <code>Usage</code>.</p>
 variant = variantMembership.ownedVariantUsage
 variantMembership = ownedMembership-&gt;selectByKind(VariantMembership)
 isVariation implies ownedFeatureMembership-&gt;isEmpty()
 isReference = not isComposite
 owningVariationUsage &lt;&gt; null implies
     specializes(owningVariationUsage)
 isVariation implies
     not ownedSpecialization.specific-&gt;exists(
         oclIsKindOf(Definition) and
         oclAsType(Definition).isVariation or
         oclIsKindOf(Usage) and
         oclAsType(Usage).isVariation)
 owningVariationDefinition &lt;&gt; null implies
     specializes(owningVariationDefinition)
 directedUsage = directedFeature-&gt;selectByKind(Usage)
 nestedAction = nestedUsage-&gt;selectByKind(ActionUsage)
 nestedAllocation = nestedUsage-&gt;selectByKind(AllocationUsage)
 nestedAnalysisCase = nestedUsage-&gt;selectByKind(AnalysisCaseUsage)
 nestedAttribute = nestedUsage-&gt;selectByKind(AttributeUsage)
 nestedCalculation = nestedUsage-&gt;selectByKind(CalculationUsage)
 nestedCase = nestedUsage-&gt;selectByKind(CaseUsage)
 nestedConcern = nestedUsage-&gt;selectByKind(ConcernUsage)
 nestedConnection = nestedUsage-&gt;selectByKind(ConnectorAsUsage)
 nestedConstraint = nestedUsage-&gt;selectByKind(ConstraintUsage)
 ownedNested = nestedUsage-&gt;selectByKind(EnumerationUsage)
 nestedFlow = nestedUsage-&gt;selectByKind(FlowConnectionUsage)
 nestedInterface = nestedUsage-&gt;selectByKind(ReferenceUsage)
 nestedItem = nestedUsage-&gt;selectByKind(ItemUsage)
 nestedMetadata = nestedUsage-&gt;selectByKind(MetadataUsage)
 nestedOccurrence = nestedUsage-&gt;selectByKind(OccurrenceUsage)
 nestedPart = nestedUsage-&gt;selectByKind(PartUsage)
 nestedPort = nestedUsage-&gt;selectByKind(PortUsage)
 nestedReference = nestedUsage-&gt;selectByKind(ReferenceUsage)
 nestedRendering = nestedUsage-&gt;selectByKind(RenderingUsage)
 nestedRequirement = nestedUsage-&gt;selectByKind(RequirementUsage)
 nestedState = nestedUsage-&gt;selectByKind(StateUsage)
 nestedTransition = nestedUsage-&gt;selectByKind(TransitionUsage)
 nestedUsage = ownedFeature-&gt;selectByKind(Usage)
 nestedUseCase = nestedUsage-&gt;selectByKind(UseCaseUsage)
 nestedVerificationCase = nestedUsage-&gt;selectByKind(VerificationCaseUsage)
 nestedView = nestedUsage-&gt;selectByKind(ViewUsage)
 nestedViewpoint = nestedUsage-&gt;selectByKind(ViewpointUsage)
 usage = feature-&gt;selectByKind(Usage)
 direction &lt;&gt; null or isEnd or featuringType-&gt;isEmpty() implies
     isReference
 isVariation implies isAbstract
 mayTimeVary =
     owningType &lt;&gt; null and
     owningType.specializesFromLibrary('Occurrences::Occurrence') and
     not (
         isPortion or
         specializesFromLibrary('Links::SelfLink') or
         specializesFromLibrary('Occurrences::HappensLink') or
         isComposite and specializesFromLibrary('Actions::Action')
     )
 owningVariationUsage &lt;&gt; null implies
     featuringType-&gt;asSet() = owningVariationUsage.featuringType-&gt;asSet()</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../../kerml/model/kerml/Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDefinition()">getDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Classifiers</code> that are the types of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDirectedUsage()">getDirectedUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>usages</code> of this <code>Usage</code> that are <code>directedFeatures</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedAction()">getNestedAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ActionUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedAllocation()">getNestedAllocation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>AllocationUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedAnalysisCase()">getNestedAnalysisCase</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>AnalysisCaseUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedAttribute()">getNestedAttribute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The code&gt;AttributeUsages that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedCalculation()">getNestedCalculation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>CalculationUsage</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedCase()">getNestedCase</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>CaseUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedConcern()">getNestedConcern</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ConcernUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedConnection()">getNestedConnection</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ConnectorAsUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedConstraint()">getNestedConstraint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ConstraintUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedEnumeration()">getNestedEnumeration</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The code&gt;EnumerationUsages that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedFlow()">getNestedFlow</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The code&gt;FlowUsages that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedInterface()">getNestedInterface</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>InterfaceUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedItem()">getNestedItem</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ItemUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedMetadata()">getNestedMetadata</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>MetadataUsages</code> that are <code>nestedUsages</code> of this of this <code>Usage</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedOccurrence()">getNestedOccurrence</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>OccurrenceUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedPart()">getNestedPart</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>PartUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedPort()">getNestedPort</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>PortUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedReference()">getNestedReference</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ReferenceUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedRendering()">getNestedRendering</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>RenderingUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedRequirement()">getNestedRequirement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>RequirementUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedState()">getNestedState</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>StateUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedTransition()">getNestedTransition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>TransitionUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedUsage()">getNestedUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Usages</code> that are <code>ownedFeatures</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedUseCase()">getNestedUseCase</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>UseCaseUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedVerificationCase()">getNestedVerificationCase</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>VerificationCaseUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedView()">getNestedView</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ViewUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedViewpoint()">getNestedViewpoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ViewpointUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningDefinition()">getOwningDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Definition</code> that owns this <code>Usage</code> (if any).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningUsage()">getOwningUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Usage</code> in which this <code>Usage</code> is nested (if any).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUsage()">getUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Usages</code> that are <code>features</code> of this <code>Usage</code> (not necessarily owned).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVariant()">getVariant</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Usages</code> which represent the variants of this <code>Usage</code> as a variation point <code>Usage</code>, if <code>isVariation = true</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VariantMembership</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVariantMembership()">getVariantMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedMemberships</code> of this <code>Usage</code> that are <code>VariantMemberships</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isMayTimeVary()">isMayTimeVary</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this <code>Usage</code> may be time varying (that is, whether it is featured by the snapshots of its <code>owningType</code>, rather than being featured by the <code>owningType</code> itself).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isReference()">isReference</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this <code>Usage</code> is a referential <code>Usage</code>, that is, it has <code>isComposite = false</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isVariation()">isVariation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this <code>Usage</code> is for a variation point or not.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#namingFeature()">namingFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If this <code>Usage</code> is a variant, then its naming <code>Feature</code> is the <code>referencedFeature</code> of its <code>ownedReferenceSubsetting</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#referencedFeatureTarget()">referencedFeatureTarget</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If <code>ownedReferenceSubsetting</code> is not null, return the <code>featureTarget</code> of the <code>referencedFeature</code> of the <code>ownedReferenceSubsetting</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsReference(boolean)">setIsReference</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this <code>Usage</code> is a referential <code>Usage</code>, that is, it has <code>isComposite = false</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsVariation(boolean)">setIsVariation</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this <code>Usage</code> is for a variation point or not.</div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Feature">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></h3>
<code><a href="../../../kerml/model/kerml/Feature.html#allRedefinedFeatures()">allRedefinedFeatures</a>, <a href="../../../kerml/model/kerml/Feature.html#asCartesianProduct()">asCartesianProduct</a>, <a href="../../../kerml/model/kerml/Feature.html#canAccess(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">canAccess</a>, <a href="../../../kerml/model/kerml/Feature.html#directionFor(com.dassault_systemes.modeler.kerml.model.kerml.Type)">directionFor</a>, <a href="../../../kerml/model/kerml/Feature.html#effectiveName()">effectiveName</a>, <a href="../../../kerml/model/kerml/Feature.html#effectiveShortName()">effectiveShortName</a>, <a href="../../../kerml/model/kerml/Feature.html#getChainingFeature()">getChainingFeature</a>, <a href="../../../kerml/model/kerml/Feature.html#getCrossFeature()">getCrossFeature</a>, <a href="../../../kerml/model/kerml/Feature.html#getDirection()">getDirection</a>, <a href="../../../kerml/model/kerml/Feature.html#getEndOwningType()">getEndOwningType</a>, <a href="../../../kerml/model/kerml/Feature.html#getFeatureTarget()">getFeatureTarget</a>, <a href="../../../kerml/model/kerml/Feature.html#getFeaturingType()">getFeaturingType</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedCrossSubsetting()">getOwnedCrossSubsetting</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedFeatureChaining()">getOwnedFeatureChaining</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedFeatureInverting()">getOwnedFeatureInverting</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedRedefinition()">getOwnedRedefinition</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedReferenceSubsetting()">getOwnedReferenceSubsetting</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedSubsetting()">getOwnedSubsetting</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedTypeFeaturing()">getOwnedTypeFeaturing</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwnedTyping()">getOwnedTyping</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwningFeatureMembership()">getOwningFeatureMembership</a>, <a href="../../../kerml/model/kerml/Feature.html#getOwningType()">getOwningType</a>, <a href="../../../kerml/model/kerml/Feature.html#getType()">getType</a>, <a href="../../../kerml/model/kerml/Feature.html#isCartesianProduct()">isCartesianProduct</a>, <a href="../../../kerml/model/kerml/Feature.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isCompatibleWith</a>, <a href="../../../kerml/model/kerml/Feature.html#isComposite()">isComposite</a>, <a href="../../../kerml/model/kerml/Feature.html#isConstant()">isConstant</a>, <a href="../../../kerml/model/kerml/Feature.html#isDerived()">isDerived</a>, <a href="../../../kerml/model/kerml/Feature.html#isEnd()">isEnd</a>, <a href="../../../kerml/model/kerml/Feature.html#isFeaturedWithin(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isFeaturedWithin</a>, <a href="../../../kerml/model/kerml/Feature.html#isFeaturingType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isFeaturingType</a>, <a href="../../../kerml/model/kerml/Feature.html#isOrdered()">isOrdered</a>, <a href="../../../kerml/model/kerml/Feature.html#isOwnedCrossFeature()">isOwnedCrossFeature</a>, <a href="../../../kerml/model/kerml/Feature.html#isPortion()">isPortion</a>, <a href="../../../kerml/model/kerml/Feature.html#isUnique()">isUnique</a>, <a href="../../../kerml/model/kerml/Feature.html#isVariable()">isVariable</a>, <a href="../../../kerml/model/kerml/Feature.html#ownedCrossFeature()">ownedCrossFeature</a>, <a href="../../../kerml/model/kerml/Feature.html#redefines(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">redefines</a>, <a href="../../../kerml/model/kerml/Feature.html#redefinesFromLibrary(java.lang.String)">redefinesFromLibrary</a>, <a href="../../../kerml/model/kerml/Feature.html#setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)">setDirection</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsComposite(boolean)">setIsComposite</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsConstant(boolean)">setIsConstant</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsDerived(boolean)">setIsDerived</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsEnd(boolean)">setIsEnd</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsOrdered(boolean)">setIsOrdered</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsPortion(boolean)">setIsPortion</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsUnique(boolean)">setIsUnique</a>, <a href="../../../kerml/model/kerml/Feature.html#setIsVariable(boolean)">setIsVariable</a>, <a href="../../../kerml/model/kerml/Feature.html#subsetsChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">subsetsChain</a>, <a href="../../../kerml/model/kerml/Feature.html#supertypes(boolean)">supertypes</a>, <a href="../../../kerml/model/kerml/Feature.html#typingFeatures()">typingFeatures</a></code></div>
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
<section class="detail" id="isMayTimeVary()">
<h3>isMayTimeVary</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isMayTimeVary</span>()</div>
<div class="block"><p>Whether this <code>Usage</code> may be time varying (that is, whether it is featured by the snapshots of its <code>owningType</code>, rather than being featured by the <code>owningType</code> itself). However, if <code>isConstant</code> is also true, then the value of the <code>Usage</code> is nevertheless constant over the entire duration of an instance of its <code>owningType</code> (that is, it has the same value on all snapshots).</p>
<p>The property <code>mayTimeVary</code> redefines the KerML property <code>Feature::isVariable</code>, making it derived. The property <code>isConstant</code> is inherited from <code>Feature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the mayTimeVary value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReference()">
<h3>isReference</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isReference</span>()</div>
<div class="block"><p>Whether this <code>Usage</code> is a referential <code>Usage</code>, that is, it has <code>isComposite = false</code>.<p></p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isReference value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsReference(boolean)">
<h3>setIsReference</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsReference</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether this <code>Usage</code> is a referential <code>Usage</code>, that is, it has <code>isComposite = false</code>.<p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isReference value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVariant()">
<h3>getVariant</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</span> <span class="element-name">getVariant</span>()</div>
<div class="block"><p>The <code>Usages</code> which represent the variants of this <code>Usage</code> as a variation point <code>Usage</code>, if <code>isVariation = true</code>. If <code>isVariation = false</code>, then there must be no <code>variants</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the variant value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="owningVariationUsage"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVariantMembership()">
<h3>getVariantMembership</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VariantMembership</a>&gt;</span> <span class="element-name">getVariantMembership</span>()</div>
<div class="block"><p>The <code>ownedMemberships</code> of this <code>Usage</code> that are <code>VariantMemberships</code>. If <code>isVariation = true</code>, then this must be all <code>memberships</code> of the <code>Usage</code>. If <code>isVariation = false</code>, then <code>variantMembership</code>must be empty.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the variantMembership value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="owningVariationUsage"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningDefinition()">
<h3>getOwningDefinition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a></span> <span class="element-name">getOwningDefinition</span>()</div>
<div class="block"><p>The <code>Definition</code> that owns this <code>Usage</code> (if any).</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the owningDefinition value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Definition.html#getOwnedUsage()"><code>Definition.getOwnedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningUsage()">
<h3>getOwningUsage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></span> <span class="element-name">getOwningUsage</span>()</div>
<div class="block"><p>The <code>Usage</code> in which this <code>Usage</code> is nested (if any).</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the owningUsage value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="#getNestedUsage()"><code>getNestedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefinition()">
<h3>getDefinition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../kerml/model/kerml/Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a>&gt;</span> <span class="element-name">getDefinition</span>()</div>
<div class="block"><p>The <code>Classifiers</code> that are the types of this <code>Usage</code>. Nominally, these are <code>Definitions</code>, but other kinds of Kernel <code>Classifiers</code> are also allowed, to permit use of <code>Classifiers</code> from the Kernel Model Libraries.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the definition value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="definedUsage"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsage()">
<h3>getUsage</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</span> <span class="element-name">getUsage</span>()</div>
<div class="block"><p>The <code>Usages</code> that are <code>features</code> of this <code>Usage</code> (not necessarily owned).</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the usage value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="featuringUsage"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirectedUsage()">
<h3>getDirectedUsage</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</span> <span class="element-name">getDirectedUsage</span>()</div>
<div class="block"><p>The <code>usages</code> of this <code>Usage</code> that are <code>directedFeatures</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the directedUsage value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="usageWithDirectedUsage"
        subsets=<a href="#getUsage()"><code>getUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedUsage()">
<h3>getNestedUsage</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</span> <span class="element-name">getNestedUsage</span>()</div>
<div class="block"><p>The <code>Usages</code> that are <code>ownedFeatures</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedUsage value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="#getOwningUsage()"><code>getOwningUsage()</code></a>
        subsets=<a href="#getUsage()"><code>getUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedReference()">
<h3>getNestedReference</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a>&gt;</span> <span class="element-name">getNestedReference</span>()</div>
<div class="block"><p>The <code>ReferenceUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedReference value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="referenceOwningUsage"
        subsets=<a href="#getNestedUsage()"><code>getNestedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedAttribute()">
<h3>getNestedAttribute</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a>&gt;</span> <span class="element-name">getNestedAttribute</span>()</div>
<div class="block"><p>The code&gt;AttributeUsages that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedAttribute value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="attributeOwningUsage"
        subsets=<a href="#getNestedUsage()"><code>getNestedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedEnumeration()">
<h3>getNestedEnumeration</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a>&gt;</span> <span class="element-name">getNestedEnumeration</span>()</div>
<div class="block"><p>The code&gt;EnumerationUsages that are <code>nestedUsages</code> of this <code>Usage</code>.<p></p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedEnumeration value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="enumerationOwningUsage"
        subsets=<a href="#getNestedAttribute()"><code>getNestedAttribute()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedOccurrence()">
<h3>getNestedOccurrence</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a>&gt;</span> <span class="element-name">getNestedOccurrence</span>()</div>
<div class="block"><p>The <code>OccurrenceUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedOccurrence value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="occurrenceOwningUsage"
        subsets=<a href="#getNestedUsage()"><code>getNestedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedItem()">
<h3>getNestedItem</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a>&gt;</span> <span class="element-name">getNestedItem</span>()</div>
<div class="block"><p>The <code>ItemUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedItem value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="itemOwningUsage"
        subsets=<a href="#getNestedOccurrence()"><code>getNestedOccurrence()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedPart()">
<h3>getNestedPart</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</span> <span class="element-name">getNestedPart</span>()</div>
<div class="block"><p>The <code>PartUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedPart value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="partOwningUsage"
        subsets=<a href="#getNestedItem()"><code>getNestedItem()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedPort()">
<h3>getNestedPort</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a>&gt;</span> <span class="element-name">getNestedPort</span>()</div>
<div class="block"><p>The <code>PortUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedPort value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="portOwningUsage"
        subsets=<a href="#getNestedUsage()"><code>getNestedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedConnection()">
<h3>getNestedConnection</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a>&gt;</span> <span class="element-name">getNestedConnection</span>()</div>
<div class="block"><p>The <code>ConnectorAsUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>. Note that this list includes <code>BindingConnectorAsUsages</code>, <code>SuccessionAsUsages</code>, and <code>FlowConnectionUsages</code> because these are <code>ConnectorAsUsages</code> even though they are not <code>ConnectionUsages</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedConnection value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="connectionOwningUsage"
        subsets=<a href="#getNestedUsage()"><code>getNestedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedFlow()">
<h3>getNestedFlow</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a>&gt;</span> <span class="element-name">getNestedFlow</span>()</div>
<div class="block"><p>The code&gt;FlowUsages that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedFlow value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="flowOwningUsage"
        subsets=<a href="#getNestedConnection()"><code>getNestedConnection()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedInterface()">
<h3>getNestedInterface</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a>&gt;</span> <span class="element-name">getNestedInterface</span>()</div>
<div class="block"><p>The <code>InterfaceUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedInterface value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="interfaceOwningUsage"
        subsets=<a href="#getNestedConnection()"><code>getNestedConnection()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedAllocation()">
<h3>getNestedAllocation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a>&gt;</span> <span class="element-name">getNestedAllocation</span>()</div>
<div class="block"><p>The <code>AllocationUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedAllocation value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="allocationOwningUsage"
        subsets=<a href="#getNestedConnection()"><code>getNestedConnection()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedAction()">
<h3>getNestedAction</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt;</span> <span class="element-name">getNestedAction</span>()</div>
<div class="block"><p>The <code>ActionUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedAction value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="actionOwningUsage"
        subsets=<a href="#getNestedOccurrence()"><code>getNestedOccurrence()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedState()">
<h3>getNestedState</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a>&gt;</span> <span class="element-name">getNestedState</span>()</div>
<div class="block"><p>The <code>StateUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedState value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="stateOwningUsage"
        subsets=<a href="#getNestedAction()"><code>getNestedAction()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedTransition()">
<h3>getNestedTransition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a>&gt;</span> <span class="element-name">getNestedTransition</span>()</div>
<div class="block"><p>The <code>TransitionUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedTransition value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="transitionOwningUsage"
        subsets=<a href="#getNestedUsage()"><code>getNestedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedCalculation()">
<h3>getNestedCalculation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a>&gt;</span> <span class="element-name">getNestedCalculation</span>()</div>
<div class="block"><p>The <code>CalculationUsage</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedCalculation value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="calculationOwningUsage"
        subsets=<a href="#getNestedAction()"><code>getNestedAction()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedConstraint()">
<h3>getNestedConstraint</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a>&gt;</span> <span class="element-name">getNestedConstraint</span>()</div>
<div class="block"><p>The <code>ConstraintUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedConstraint value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="constraintOwningUsage"
        subsets=<a href="#getNestedOccurrence()"><code>getNestedOccurrence()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedRequirement()">
<h3>getNestedRequirement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a>&gt;</span> <span class="element-name">getNestedRequirement</span>()</div>
<div class="block"><p>The <code>RequirementUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedRequirement value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="requirementOwningUsage"
        subsets=<a href="#getNestedConstraint()"><code>getNestedConstraint()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedConcern()">
<h3>getNestedConcern</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a>&gt;</span> <span class="element-name">getNestedConcern</span>()</div>
<div class="block"><p>The <code>ConcernUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedConcern value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="concernOwningUsage"
        subsets=<a href="#getNestedRequirement()"><code>getNestedRequirement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedCase()">
<h3>getNestedCase</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a>&gt;</span> <span class="element-name">getNestedCase</span>()</div>
<div class="block"><p>The <code>CaseUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedCase value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="caseOwningUsage"
        subsets=<a href="#getNestedCalculation()"><code>getNestedCalculation()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedAnalysisCase()">
<h3>getNestedAnalysisCase</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a>&gt;</span> <span class="element-name">getNestedAnalysisCase</span>()</div>
<div class="block"><p>The <code>AnalysisCaseUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedAnalysisCase value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="analysisCaseOwningUsage"
        subsets=<a href="#getNestedCase()"><code>getNestedCase()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedVerificationCase()">
<h3>getNestedVerificationCase</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a>&gt;</span> <span class="element-name">getNestedVerificationCase</span>()</div>
<div class="block"><p>The <code>VerificationCaseUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedVerificationCase value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="verificationCaseOwningUsage"
        subsets=<a href="#getNestedCase()"><code>getNestedCase()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedUseCase()">
<h3>getNestedUseCase</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a>&gt;</span> <span class="element-name">getNestedUseCase</span>()</div>
<div class="block"><p>The <code>UseCaseUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedUseCase value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="useCaseOwningUsage"
        subsets=<a href="#getNestedCase()"><code>getNestedCase()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedView()">
<h3>getNestedView</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a>&gt;</span> <span class="element-name">getNestedView</span>()</div>
<div class="block"><p>The <code>ViewUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedView value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="viewOwningUsage"
        subsets=<a href="#getNestedPart()"><code>getNestedPart()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedViewpoint()">
<h3>getNestedViewpoint</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a>&gt;</span> <span class="element-name">getNestedViewpoint</span>()</div>
<div class="block"><p>The <code>ViewpointUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedViewpoint value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="viewpointOwningUsage"
        subsets=<a href="#getNestedRequirement()"><code>getNestedRequirement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedRendering()">
<h3>getNestedRendering</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a>&gt;</span> <span class="element-name">getNestedRendering</span>()</div>
<div class="block"><p>The <code>RenderingUsages</code> that are <code>nestedUsages</code> of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedRendering value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="renderingOwningUsage"
        subsets=<a href="#getNestedPart()"><code>getNestedPart()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedMetadata()">
<h3>getNestedMetadata</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a>&gt;</span> <span class="element-name">getNestedMetadata</span>()</div>
<div class="block"><p>The <code>MetadataUsages</code> that are <code>nestedUsages</code> of this of this <code>Usage</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the nestedMetadata value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="metadataOwningUsage"
        subsets=<a href="#getNestedItem()"><code>getNestedItem()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVariation()">
<h3>isVariation</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isVariation</span>()</div>
<div class="block"><p>Whether this <code>Usage</code> is for a variation point or not. If true, then all the <code>memberships</code> of the <code>Usage</code> must be <code>VariantMemberships</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isVariation value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsVariation(boolean)">
<h3>setIsVariation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsVariation</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether this <code>Usage</code> is for a variation point or not. If true, then all the <code>memberships</code> of the <code>Usage</code> must be <code>VariantMemberships</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isVariation value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="namingFeature()">
<h3>namingFeature</h3>
<div class="member-signature"><span class="return-type"><a href="../../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">namingFeature</span>()</div>
<div class="block"><p>If this <code>Usage</code> is a variant, then its naming <code>Feature</code> is the <code>referencedFeature</code> of its <code>ownedReferenceSubsetting</code>.</p>
 if not owningMembership.oclIsKindOf(VariantMembership) then
     self.oclAsType(Feature).namingFeature()
 else if ownedReferenceSubsetting = null then null
 else ownedReferenceSubsetting.referencedFeature
 endif endif</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/model/kerml/Feature.html#namingFeature()">namingFeature</a></code> in interface <code><a href="../../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="referencedFeatureTarget()">
<h3>referencedFeatureTarget</h3>
<div class="member-signature"><span class="return-type"><a href="../../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">referencedFeatureTarget</span>()</div>
<div class="block"><p>If <code>ownedReferenceSubsetting</code> is not null, return the <code>featureTarget</code> of the <code>referencedFeature</code> of the <code>ownedReferenceSubsetting</code>.</p>
 if ownedReferenceSubsetting = null then null
 else ownedReferenceSubsetting.referencedFeature.featureTarget
 endif</div>
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
