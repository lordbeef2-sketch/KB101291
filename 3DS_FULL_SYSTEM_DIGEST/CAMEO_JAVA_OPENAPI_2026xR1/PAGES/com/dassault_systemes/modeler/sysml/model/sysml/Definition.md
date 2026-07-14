# JAVA OPENAPI: Definition (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/sysml/Definition.html
- source_path: `com/dassault_systemes/modeler/sysml/model/sysml/Definition.html`
- source_sha256: `6fe7559acbcc31e97c116ecd76076a3e05e2b377647dcf7360c692450b2f00b9`
- captured_utc: `2026-07-14T16:45:03.991056+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model.sysml](package-summary.html)

## Interface Definition

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Classifier](../../../kerml/model/kerml/Classifier.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../../kerml/model/kerml/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `[Namespace](../../../kerml/model/kerml/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[Type](../../../kerml/model/kerml/Type.html)`

All Known Subinterfaces:
`[ActionDefinition](ActionDefinition.html)`, `[AllocationDefinition](AllocationDefinition.html)`, `[AnalysisCaseDefinition](AnalysisCaseDefinition.html)`, `[AttributeDefinition](AttributeDefinition.html)`, `[CalculationDefinition](CalculationDefinition.html)`, `[CaseDefinition](CaseDefinition.html)`, `[ConcernDefinition](ConcernDefinition.html)`, `[ConjugatedPortDefinition](ConjugatedPortDefinition.html)`, `[ConnectionDefinition](ConnectionDefinition.html)`, `[ConstraintDefinition](ConstraintDefinition.html)`, `[EnumerationDefinition](EnumerationDefinition.html)`, `[FlowDefinition](FlowDefinition.html)`, `[InterfaceDefinition](InterfaceDefinition.html)`, `[ItemDefinition](ItemDefinition.html)`, `[MetadataDefinition](MetadataDefinition.html)`, `[OccurrenceDefinition](OccurrenceDefinition.html)`, `[PartDefinition](PartDefinition.html)`, `[PortDefinition](PortDefinition.html)`, `[RenderingDefinition](RenderingDefinition.html)`, `[RequirementDefinition](RequirementDefinition.html)`, `[StateDefinition](StateDefinition.html)`, `[UseCaseDefinition](UseCaseDefinition.html)`, `[VerificationCaseDefinition](VerificationCaseDefinition.html)`, `[ViewDefinition](ViewDefinition.html)`, `[ViewpointDefinition](ViewpointDefinition.html)`

@OpenApiAllpublic interfaceDefinitionextends [Classifier](../../../kerml/model/kerml/Classifier.html)

A `Definition` is a `Classifier` of `Usages`. The actual kinds of `Definition` that may appear in a model are given by the subclasses of `Definition` (possibly as extended with user-defined *`SemanticMetadata`*).
Normally, a `Definition` has owned Usages that model `features` of the thing being defined. A `Definition` may also have other `Definitions` nested in it, but this has no semantic significance, other than the nested scoping resulting from the `Definition` being considered as a `Namespace` for any nested `Definitions`.
However, if a `Definition` has `isVariation` = `true`, then it represents a *variation point* `Definition`. In this case, all of its `members` must be `variant` `Usages`, related to the `Definition` by `VariantMembership` `Relationships`. Rather than being `features` of the `Definition`, `variant` `Usages` model different concrete alternatives that can be chosen to fill in for an abstract `Usage` of the variation point `Definition`.
 
 isVariation implies ownedFeatureMembership->isEmpty()
 variant = variantMembership.ownedVariantUsage
 variantMembership = ownedMembership->selectByKind(VariantMembership)
 isVariation implies
 not ownedSpecialization.specific->exists(
 oclIsKindOf(Definition) and
 oclAsType(Definition).isVariation)
 usage = feature->selectByKind(Usage)
 directedUsage = directedFeature->selectByKind(Usage)
 ownedUsage = ownedFeature->selectByKind(Usage)
 ownedAttribute = ownedUsage->selectByKind(AttributeUsage)
 ownedReference = ownedUsage->selectByKind(ReferenceUsage)
 ownedEnumeration = ownedUsage->selectByKind(EnumerationUsage)
 ownedOccurrence = ownedUsage->selectByKind(OccurrenceUsage)
 ownedItem = ownedUsage->selectByKind(ItemUsage)
 ownedPart = ownedUsage->selectByKind(PartUsage)
 ownedPort = ownedUsage->selectByKind(PortUsage)
 ownedConnection = ownedUsage->selectByKind(ConnectorAsUsage)
 ownedFlow = ownedUsage->selectByKind(FlowConnectionUsage)
 ownedInterface = ownedUsage->selectByKind(ReferenceUsage)
 ownedAllocation = ownedUsage->selectByKind(AllocationUsage)
 ownedAction = ownedUsage->selectByKind(ActionUsage)
 ownedState = ownedUsage->selectByKind(StateUsage)
 ownedTransition = ownedUsage->selectByKind(TransitionUsage)
 ownedCalculation = ownedUsage->selectByKind(CalculationUsage)
 ownedConstraint = ownedUsage->selectByKind(ConstraintUsage)
 ownedRequirement = ownedUsage->selectByKind(RequirementUsage)
 ownedConcern = ownedUsage->selectByKind(ConcernUsage)
 ownedCase = ownedUsage->selectByKind(CaseUsage)
 ownedAnalysisCase = ownedUsage->selectByKind(AnalysisCaseUsage)
 ownedVerificationCase = ownedUsage->selectByKind(VerificationCaseUsage)
 ownedUseCase = ownedUsage->selectByKind(UseCaseUsage)
 ownedView = ownedUsage->selectByKind(ViewUsage)
 ownedViewpoint = ownedUsage->selectByKind(ViewpointUsage)
 ownedRendering = ownedUsage->selectByKind(RenderingUsage)
 ownedMetadata = ownedUsage->selectByKind(MetadataUsage)
 isVariation implies isAbstract

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)>`
`[getDirectedUsage](#getDirectedUsage())()`
The `usages` of this `Definition` that are `directedFeatures`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ActionUsage](ActionUsage.html)>`
`[getOwnedAction](#getOwnedAction())()`
The `ActionUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[AllocationUsage](AllocationUsage.html)>`
`[getOwnedAllocation](#getOwnedAllocation())()`
The `AllocationUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[AnalysisCaseUsage](AnalysisCaseUsage.html)>`
`[getOwnedAnalysisCase](#getOwnedAnalysisCase())()`
The `AnalysisCaseUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[AttributeUsage](AttributeUsage.html)>`
`[getOwnedAttribute](#getOwnedAttribute())()`
The `AttributeUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CalculationUsage](CalculationUsage.html)>`
`[getOwnedCalculation](#getOwnedCalculation())()`
The `CalculationUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CaseUsage](CaseUsage.html)>`
`[getOwnedCase](#getOwnedCase())()`
The code>CaseUsages that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConcernUsage](ConcernUsage.html)>`
`[getOwnedConcern](#getOwnedConcern())()`
The `ConcernUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConnectorAsUsage](ConnectorAsUsage.html)>`
`[getOwnedConnection](#getOwnedConnection())()`
The `ConnectorAsUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConstraintUsage](ConstraintUsage.html)>`
`[getOwnedConstraint](#getOwnedConstraint())()`
The `ConstraintUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[EnumerationUsage](EnumerationUsage.html)>`
`[getOwnedEnumeration](#getOwnedEnumeration())()`
The `EnumerationUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FlowUsage](FlowUsage.html)>`
`[getOwnedFlow](#getOwnedFlow())()`
The `FlowUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[InterfaceUsage](InterfaceUsage.html)>`
`[getOwnedInterface](#getOwnedInterface())()`
The `InterfaceUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ItemUsage](ItemUsage.html)>`
`[getOwnedItem](#getOwnedItem())()`
The `ItemUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataUsage](MetadataUsage.html)>`
`[getOwnedMetadata](#getOwnedMetadata())()`
The `MetadataUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[OccurrenceUsage](OccurrenceUsage.html)>`
`[getOwnedOccurrence](#getOwnedOccurrence())()`
The `OccurrenceUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](PartUsage.html)>`
`[getOwnedPart](#getOwnedPart())()`
The `PartUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PortUsage](PortUsage.html)>`
`[getOwnedPort](#getOwnedPort())()`
The `PortUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ReferenceUsage](ReferenceUsage.html)>`
`[getOwnedReference](#getOwnedReference())()`
The `ReferenceUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RenderingUsage](RenderingUsage.html)>`
`[getOwnedRendering](#getOwnedRendering())()`
The `RenderingUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RequirementUsage](RequirementUsage.html)>`
`[getOwnedRequirement](#getOwnedRequirement())()`
The `RequirementUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[StateUsage](StateUsage.html)>`
`[getOwnedState](#getOwnedState())()`
The `StateUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[TransitionUsage](TransitionUsage.html)>`
`[getOwnedTransition](#getOwnedTransition())()`
The `TransitionUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)>`
`[getOwnedUsage](#getOwnedUsage())()`
The `Usages` that are `ownedFeatures` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[UseCaseUsage](UseCaseUsage.html)>`
`[getOwnedUseCase](#getOwnedUseCase())()`
The `UseCaseUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[VerificationCaseUsage](VerificationCaseUsage.html)>`
`[getOwnedVerificationCase](#getOwnedVerificationCase())()`
The `VerificationCaseUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ViewUsage](ViewUsage.html)>`
`[getOwnedView](#getOwnedView())()`
The `ViewUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ViewpointUsage](ViewpointUsage.html)>`
`[getOwnedViewpoint](#getOwnedViewpoint())()`
The `ViewpointUsages` that are `ownedUsages` of this `Definition`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)>`
`[getUsage](#getUsage())()`
The `Usages` that are `features` of this `Definition` (not necessarily owned).
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)>`
`[getVariant](#getVariant())()`
The `Usages` which represent the variants of this `Definition` as a variation point `Definition`, if `isVariation` = true.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[VariantMembership](VariantMembership.html)>`
`[getVariantMembership](#getVariantMembership())()`
The `ownedMemberships` of this `Definition` that are `VariantMemberships`.
`boolean`
`[isVariation](#isVariation())()`
Whether this `Definition` is for a variation point or not.
`void`
`[setIsVariation](#setIsVariation(boolean))(boolean value)`
Whether this `Definition` is for a variation point or not.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Classifier](../../../kerml/model/kerml/Classifier.html)
`[getOwnedSubclassification](../../../kerml/model/kerml/Classifier.html#getOwnedSubclassification())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](../../../kerml/model/kerml/Element.html)
`[effectiveName](../../../kerml/model/kerml/Element.html#effectiveName()), [effectiveShortName](../../../kerml/model/kerml/Element.html#effectiveShortName()), [escapedName](../../../kerml/model/kerml/Element.html#escapedName()), [getAliasIds](../../../kerml/model/kerml/Element.html#getAliasIds()), [getDeclaredName](../../../kerml/model/kerml/Element.html#getDeclaredName()), [getDeclaredShortName](../../../kerml/model/kerml/Element.html#getDeclaredShortName()), [getDocumentation](../../../kerml/model/kerml/Element.html#getDocumentation()), [getElementId](../../../kerml/model/kerml/Element.html#getElementId()), [getName](../../../kerml/model/kerml/Element.html#getName()), [getOwnedAnnotation](../../../kerml/model/kerml/Element.html#getOwnedAnnotation()), [getOwnedElement](../../../kerml/model/kerml/Element.html#getOwnedElement()), [getOwnedRelationship](../../../kerml/model/kerml/Element.html#getOwnedRelationship()), [getOwner](../../../kerml/model/kerml/Element.html#getOwner()), [getOwningMembership](../../../kerml/model/kerml/Element.html#getOwningMembership()), [getOwningNamespace](../../../kerml/model/kerml/Element.html#getOwningNamespace()), [getOwningRelationship](../../../kerml/model/kerml/Element.html#getOwningRelationship()), [getQualifiedName](../../../kerml/model/kerml/Element.html#getQualifiedName()), [getShortName](../../../kerml/model/kerml/Element.html#getShortName()), [getTextualRepresentation](../../../kerml/model/kerml/Element.html#getTextualRepresentation()), [isImpliedIncluded](../../../kerml/model/kerml/Element.html#isImpliedIncluded()), [isLibraryElement](../../../kerml/model/kerml/Element.html#isLibraryElement()), [libraryNamespace](../../../kerml/model/kerml/Element.html#libraryNamespace()), [path](../../../kerml/model/kerml/Element.html#path()), [setDeclaredName](../../../kerml/model/kerml/Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](../../../kerml/model/kerml/Element.html#setDeclaredShortName(java.lang.String)), [setElementId](../../../kerml/model/kerml/Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](../../../kerml/model/kerml/Element.html#setIsImpliedIncluded(boolean)), [setOwner](../../../kerml/model/kerml/Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](../../../kerml/model/kerml/Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](../../../kerml/model/kerml/Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject
`getModelExtension, getModelExtension`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Namespace](../../../kerml/model/kerml/Namespace.html)
`[getImportedMembership](../../../kerml/model/kerml/Namespace.html#getImportedMembership()), [getMember](../../../kerml/model/kerml/Namespace.html#getMember()), [getMembership](../../../kerml/model/kerml/Namespace.html#getMembership()), [getOwnedImport](../../../kerml/model/kerml/Namespace.html#getOwnedImport()), [getOwnedMember](../../../kerml/model/kerml/Namespace.html#getOwnedMember()), [getOwnedMembership](../../../kerml/model/kerml/Namespace.html#getOwnedMembership()), [importedMemberships](../../../kerml/model/kerml/Namespace.html#importedMemberships(java.util.List)), [membershipsOfVisibility](../../../kerml/model/kerml/Namespace.html#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)), [namesOf](../../../kerml/model/kerml/Namespace.html#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [qualificationOf](../../../kerml/model/kerml/Namespace.html#qualificationOf(java.lang.String)), [resolve](../../../kerml/model/kerml/Namespace.html#resolve(java.lang.String)), [resolveGlobal](../../../kerml/model/kerml/Namespace.html#resolveGlobal(java.lang.String)), [resolveLocal](../../../kerml/model/kerml/Namespace.html#resolveLocal(java.lang.String)), [resolveVisible](../../../kerml/model/kerml/Namespace.html#resolveVisible(java.lang.String)), [unqualifiedNameOf](../../../kerml/model/kerml/Namespace.html#unqualifiedNameOf(java.lang.String)), [visibilityOf](../../../kerml/model/kerml/Namespace.html#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Type](../../../kerml/model/kerml/Type.html)
`[allRedefinedFeaturesOf](../../../kerml/model/kerml/Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)), [allSupertypes](../../../kerml/model/kerml/Type.html#allSupertypes()), [directionOf](../../../kerml/model/kerml/Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [directionOfExcluding](../../../kerml/model/kerml/Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)), [getDifferencingType](../../../kerml/model/kerml/Type.html#getDifferencingType()), [getDirectedFeature](../../../kerml/model/kerml/Type.html#getDirectedFeature()), [getEndFeature](../../../kerml/model/kerml/Type.html#getEndFeature()), [getFeature](../../../kerml/model/kerml/Type.html#getFeature()), [getFeatureMembership](../../../kerml/model/kerml/Type.html#getFeatureMembership()), [getInheritedFeature](../../../kerml/model/kerml/Type.html#getInheritedFeature()), [getInheritedMembership](../../../kerml/model/kerml/Type.html#getInheritedMembership()), [getInput](../../../kerml/model/kerml/Type.html#getInput()), [getIntersectingType](../../../kerml/model/kerml/Type.html#getIntersectingType()), [getMultiplicity](../../../kerml/model/kerml/Type.html#getMultiplicity()), [getOutput](../../../kerml/model/kerml/Type.html#getOutput()), [getOwnedConjugator](../../../kerml/model/kerml/Type.html#getOwnedConjugator()), [getOwnedDifferencing](../../../kerml/model/kerml/Type.html#getOwnedDifferencing()), [getOwnedDisjoining](../../../kerml/model/kerml/Type.html#getOwnedDisjoining()), [getOwnedEndFeature](../../../kerml/model/kerml/Type.html#getOwnedEndFeature()), [getOwnedFeature](../../../kerml/model/kerml/Type.html#getOwnedFeature()), [getOwnedFeatureMembership](../../../kerml/model/kerml/Type.html#getOwnedFeatureMembership()), [getOwnedIntersecting](../../../kerml/model/kerml/Type.html#getOwnedIntersecting()), [getOwnedSpecialization](../../../kerml/model/kerml/Type.html#getOwnedSpecialization()), [getOwnedUnioning](../../../kerml/model/kerml/Type.html#getOwnedUnioning()), [getUnioningType](../../../kerml/model/kerml/Type.html#getUnioningType()), [inheritableMemberships](../../../kerml/model/kerml/Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)), [inheritedMemberships](../../../kerml/model/kerml/Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)), [isAbstract](../../../kerml/model/kerml/Type.html#isAbstract()), [isCompatibleWith](../../../kerml/model/kerml/Type.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isConjugated](../../../kerml/model/kerml/Type.html#isConjugated()), [isSufficient](../../../kerml/model/kerml/Type.html#isSufficient()), [multiplicities](../../../kerml/model/kerml/Type.html#multiplicities()), [nonPrivateMemberships](../../../kerml/model/kerml/Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)), [removeRedefinedFeatures](../../../kerml/model/kerml/Type.html#removeRedefinedFeatures(java.util.List)), [setIsAbstract](../../../kerml/model/kerml/Type.html#setIsAbstract(boolean)), [setIsSufficient](../../../kerml/model/kerml/Type.html#setIsSufficient(boolean)), [specializes](../../../kerml/model/kerml/Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [specializesFromLibrary](../../../kerml/model/kerml/Type.html#specializesFromLibrary(java.lang.String)), [supertypes](../../../kerml/model/kerml/Type.html#supertypes(boolean)), [visibleMemberships](../../../kerml/model/kerml/Type.html#visibleMemberships(java.util.List,boolean,boolean))`

============ METHOD DETAIL ========== 
Method Details
isVariation
boolean isVariation()
Whether this `Definition` is for a variation point or not. If true, then all the `memberships` of the `Definition` must be `VariantMemberships`.
Returns:
the isVariation value
Model:
derived="false"
 transient="false"
setIsVariation
void setIsVariation(boolean value)
Whether this `Definition` is for a variation point or not. If true, then all the `memberships` of the `Definition` must be `VariantMemberships`.
Parameters:
`value` - the isVariation value
Model:
derived="false"
 transient="false"
getVariant
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)> getVariant()
The `Usages` which represent the variants of this `Definition` as a variation point `Definition`, if `isVariation` = true. If `isVariation = false`, the there must be no `variants`.
Returns:
the variant value
Model:
derived="true"
 transient="true"
 oppositeRoleName="owningVariationDefinition"
getVariantMembership
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[VariantMembership](VariantMembership.html)> getVariantMembership()
The `ownedMemberships` of this `Definition` that are `VariantMemberships`. If `isVariation` = true, then this must be all `ownedMemberships` of the `Definition`. If `isVariation` = false, then `variantMembership`must be empty.
Returns:
the variantMembership value
Model:
derived="true"
 transient="true"
 oppositeRoleName="owningVariationDefinition"
getUsage
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)> getUsage()
The `Usages` that are `features` of this `Definition` (not necessarily owned).
Returns:
the usage value
Model:
derived="true"
 transient="true"
 oppositeRoleName="featuringDefinition"
getDirectedUsage
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)> getDirectedUsage()
The `usages` of this `Definition` that are `directedFeatures`.
Returns:
the directedUsage value
Model:
derived="true"
 transient="true"
 oppositeRoleName="definitionWithDirectedUsage"
 subsets=[`getUsage()`](#getUsage())
getOwnedUsage
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Usage](Usage.html)> getOwnedUsage()
The `Usages` that are `ownedFeatures` of this `Definition`.
Returns:
the ownedUsage value
Model:
derived="true"
 transient="true"
 opposite=[`Usage.getOwningDefinition()`](Usage.html#getOwningDefinition())
 subsets=[`getUsage()`](#getUsage())
getOwnedReference
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ReferenceUsage](ReferenceUsage.html)> getOwnedReference()
The `ReferenceUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedReference value
Model:
derived="true"
 transient="true"
 oppositeRoleName="referenceOwningDefinition"
 subsets=[`getOwnedUsage()`](#getOwnedUsage())
getOwnedAttribute
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[AttributeUsage](AttributeUsage.html)> getOwnedAttribute()
The `AttributeUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedAttribute value
Model:
derived="true"
 transient="true"
 oppositeRoleName="attributeOwningDefinition"
 subsets=[`getOwnedUsage()`](#getOwnedUsage())
getOwnedEnumeration
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[EnumerationUsage](EnumerationUsage.html)> getOwnedEnumeration()
The `EnumerationUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedEnumeration value
Model:
derived="true"
 transient="true"
 oppositeRoleName="enumerationOwningDefinition"
 subsets=[`getOwnedAttribute()`](#getOwnedAttribute())
getOwnedOccurrence
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[OccurrenceUsage](OccurrenceUsage.html)> getOwnedOccurrence()
The `OccurrenceUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedOccurrence value
Model:
derived="true"
 transient="true"
 oppositeRoleName="occurrenceOwningDefinition"
 subsets=[`getOwnedUsage()`](#getOwnedUsage())
getOwnedItem
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ItemUsage](ItemUsage.html)> getOwnedItem()
The `ItemUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedItem value
Model:
derived="true"
 transient="true"
 oppositeRoleName="itemOwningDefinition"
 subsets=[`getOwnedOccurrence()`](#getOwnedOccurrence())
getOwnedPart
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](PartUsage.html)> getOwnedPart()
The `PartUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedPart value
Model:
derived="true"
 transient="true"
 oppositeRoleName="partOwningDefinition"
 subsets=[`getOwnedItem()`](#getOwnedItem())
getOwnedPort
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PortUsage](PortUsage.html)> getOwnedPort()
The `PortUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedPort value
Model:
derived="true"
 transient="true"
 oppositeRoleName="portOwningDefinition"
 subsets=[`getOwnedUsage()`](#getOwnedUsage())
getOwnedConnection
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConnectorAsUsage](ConnectorAsUsage.html)> getOwnedConnection()
The `ConnectorAsUsages` that are `ownedUsages` of this `Definition`. Note that this list includes `BindingConnectorAsUsages`, `SuccessionAsUsages`, and `FlowUsages` because these are `ConnectorAsUsages` even though they are not `ConnectionUsages`.
Returns:
the ownedConnection value
Model:
derived="true"
 transient="true"
 oppositeRoleName="connectionOwningDefinition"
 subsets=[`getOwnedUsage()`](#getOwnedUsage())
getOwnedFlow
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FlowUsage](FlowUsage.html)> getOwnedFlow()
The `FlowUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedFlow value
Model:
derived="true"
 transient="true"
 oppositeRoleName="flowOwningDefinition"
 subsets=[`getOwnedConnection()`](#getOwnedConnection())
getOwnedInterface
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[InterfaceUsage](InterfaceUsage.html)> getOwnedInterface()
The `InterfaceUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedInterface value
Model:
derived="true"
 transient="true"
 oppositeRoleName="interfaceOwningDefinition"
 subsets=[`getOwnedConnection()`](#getOwnedConnection())
getOwnedAllocation
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[AllocationUsage](AllocationUsage.html)> getOwnedAllocation()
The `AllocationUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedAllocation value
Model:
derived="true"
 transient="true"
 oppositeRoleName="allocationOwningDefinition"
 subsets=[`getOwnedConnection()`](#getOwnedConnection())
getOwnedAction
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ActionUsage](ActionUsage.html)> getOwnedAction()
The `ActionUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedAction value
Model:
derived="true"
 transient="true"
 oppositeRoleName="actionOwningDefinition"
 subsets=[`getOwnedOccurrence()`](#getOwnedOccurrence())
getOwnedState
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[StateUsage](StateUsage.html)> getOwnedState()
The `StateUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedState value
Model:
derived="true"
 transient="true"
 oppositeRoleName="stateOwningDefinition"
 subsets=[`getOwnedAction()`](#getOwnedAction())
getOwnedTransition
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[TransitionUsage](TransitionUsage.html)> getOwnedTransition()
The `TransitionUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedTransition value
Model:
derived="true"
 transient="true"
 oppositeRoleName="transitionOwningDefinition"
 subsets=[`getOwnedUsage()`](#getOwnedUsage())
getOwnedCalculation
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CalculationUsage](CalculationUsage.html)> getOwnedCalculation()
The `CalculationUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedCalculation value
Model:
derived="true"
 transient="true"
 oppositeRoleName="calculationOwningDefinition"
 subsets=[`getOwnedAction()`](#getOwnedAction())
getOwnedConstraint
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConstraintUsage](ConstraintUsage.html)> getOwnedConstraint()
The `ConstraintUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedConstraint value
Model:
derived="true"
 transient="true"
 oppositeRoleName="constraintOwningDefinition"
 subsets=[`getOwnedOccurrence()`](#getOwnedOccurrence())
getOwnedRequirement
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RequirementUsage](RequirementUsage.html)> getOwnedRequirement()
The `RequirementUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedRequirement value
Model:
derived="true"
 transient="true"
 oppositeRoleName="requirementOwningDefinition"
 subsets=[`getOwnedConstraint()`](#getOwnedConstraint())
getOwnedConcern
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConcernUsage](ConcernUsage.html)> getOwnedConcern()
The `ConcernUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedConcern value
Model:
derived="true"
 transient="true"
 oppositeRoleName="concernOwningDefinition"
 subsets=[`getOwnedRequirement()`](#getOwnedRequirement())
getOwnedCase
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CaseUsage](CaseUsage.html)> getOwnedCase()
The code>CaseUsages that are `ownedUsages` of this `Definition`.
Returns:
the ownedCase value
Model:
derived="true"
 transient="true"
 oppositeRoleName="caseOwningDefinition"
 subsets=[`getOwnedCalculation()`](#getOwnedCalculation())
getOwnedAnalysisCase
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[AnalysisCaseUsage](AnalysisCaseUsage.html)> getOwnedAnalysisCase()
The `AnalysisCaseUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedAnalysisCase value
Model:
derived="true"
 transient="true"
 oppositeRoleName="analysisCaseOwningDefinition"
 subsets=[`getOwnedCase()`](#getOwnedCase())
getOwnedVerificationCase
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[VerificationCaseUsage](VerificationCaseUsage.html)> getOwnedVerificationCase()
The `VerificationCaseUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedVerificationCase value
Model:
derived="true"
 transient="true"
 oppositeRoleName="verificationCaseOwningDefinition"
 subsets=[`getOwnedCase()`](#getOwnedCase())
getOwnedUseCase
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[UseCaseUsage](UseCaseUsage.html)> getOwnedUseCase()
The `UseCaseUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedUseCase value
Model:
derived="true"
 transient="true"
 oppositeRoleName="useCaseOwningDefinition"
 subsets=[`getOwnedCase()`](#getOwnedCase())
getOwnedView
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ViewUsage](ViewUsage.html)> getOwnedView()
The `ViewUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedView value
Model:
derived="true"
 transient="true"
 oppositeRoleName="viewOwningDefinition"
 subsets=[`getOwnedPart()`](#getOwnedPart())
getOwnedViewpoint
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ViewpointUsage](ViewpointUsage.html)> getOwnedViewpoint()
The `ViewpointUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedViewpoint value
Model:
derived="true"
 transient="true"
 oppositeRoleName="viewpointOwningDefinition"
 subsets=[`getOwnedRequirement()`](#getOwnedRequirement())
getOwnedRendering
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[RenderingUsage](RenderingUsage.html)> getOwnedRendering()
The `RenderingUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedRendering value
Model:
derived="true"
 transient="true"
 oppositeRoleName="redenderingOwningDefinition"
 subsets=[`getOwnedPart()`](#getOwnedPart())
getOwnedMetadata
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataUsage](MetadataUsage.html)> getOwnedMetadata()
The `MetadataUsages` that are `ownedUsages` of this `Definition`.
Returns:
the ownedMetadata value
Model:
derived="true"
 transient="true"
 oppositeRoleName="metadataOwningDefinition"
 subsets=[`getOwnedItem()`](#getOwnedItem())

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model.sysml</a></div>
<h1 class="title" title="Interface Definition">Interface Definition</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../../kerml/model/kerml/Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code><a href="../../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionDefinition</a></code>, <code><a href="AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationDefinition</a></code>, <code><a href="AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseDefinition</a></code>, <code><a href="AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeDefinition</a></code>, <code><a href="CalculationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationDefinition</a></code>, <code><a href="CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseDefinition</a></code>, <code><a href="ConcernDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernDefinition</a></code>, <code><a href="ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a></code>, <code><a href="ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionDefinition</a></code>, <code><a href="ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintDefinition</a></code>, <code><a href="EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationDefinition</a></code>, <code><a href="FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowDefinition</a></code>, <code><a href="InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceDefinition</a></code>, <code><a href="ItemDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemDefinition</a></code>, <code><a href="MetadataDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataDefinition</a></code>, <code><a href="OccurrenceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceDefinition</a></code>, <code><a href="PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartDefinition</a></code>, <code><a href="PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></code>, <code><a href="RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingDefinition</a></code>, <code><a href="RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementDefinition</a></code>, <code><a href="StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateDefinition</a></code>, <code><a href="UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseDefinition</a></code>, <code><a href="VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseDefinition</a></code>, <code><a href="ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewDefinition</a></code>, <code><a href="ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointDefinition</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Definition</span><span class="extends-implements">
extends <a href="../../../kerml/model/kerml/Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a></span></div>
<div class="block"><p>A <code>Definition</code> is a <code>Classifier</code> of <code>Usages</code>. The actual kinds of <code>Definition</code> that may appear in a model are given by the subclasses of <code>Definition</code> (possibly as extended with user-defined <em><code>SemanticMetadata</code></em>).</p>
<p>Normally, a <code>Definition</code> has owned Usages that model <code>features</code> of the thing being defined. A <code>Definition</code> may also have other <code>Definitions</code> nested in it, but this has no semantic significance, other than the nested scoping resulting from the <code>Definition</code> being considered as a <code>Namespace</code> for any nested <code>Definitions</code>.</p>
<p>However, if a <code>Definition</code> has <code>isVariation</code> = <code>true</code>, then it represents a <em>variation point</em> <code>Definition</code>. In this case, all of its <code>members</code> must be <code>variant</code> <code>Usages</code>, related to the <code>Definition</code> by <code>VariantMembership</code> <code>Relationships</code>. Rather than being <code>features</code> of the <code>Definition</code>, <code>variant</code> <code>Usages</code> model different concrete alternatives that can be chosen to fill in for an abstract <code>Usage</code> of the variation point <code>Definition</code>.</p>
 
 isVariation implies ownedFeatureMembership-&gt;isEmpty()
 variant = variantMembership.ownedVariantUsage
 variantMembership = ownedMembership-&gt;selectByKind(VariantMembership)
 isVariation implies
     not ownedSpecialization.specific-&gt;exists(
         oclIsKindOf(Definition) and
         oclAsType(Definition).isVariation)
 usage = feature-&gt;selectByKind(Usage)
 directedUsage = directedFeature-&gt;selectByKind(Usage)
 ownedUsage = ownedFeature-&gt;selectByKind(Usage)
 ownedAttribute = ownedUsage-&gt;selectByKind(AttributeUsage)
 ownedReference = ownedUsage-&gt;selectByKind(ReferenceUsage)
 ownedEnumeration = ownedUsage-&gt;selectByKind(EnumerationUsage)
 ownedOccurrence = ownedUsage-&gt;selectByKind(OccurrenceUsage)
 ownedItem = ownedUsage-&gt;selectByKind(ItemUsage)
 ownedPart = ownedUsage-&gt;selectByKind(PartUsage)
 ownedPort = ownedUsage-&gt;selectByKind(PortUsage)
 ownedConnection = ownedUsage-&gt;selectByKind(ConnectorAsUsage)
 ownedFlow = ownedUsage-&gt;selectByKind(FlowConnectionUsage)
 ownedInterface = ownedUsage-&gt;selectByKind(ReferenceUsage)
 ownedAllocation = ownedUsage-&gt;selectByKind(AllocationUsage)
 ownedAction = ownedUsage-&gt;selectByKind(ActionUsage)
 ownedState = ownedUsage-&gt;selectByKind(StateUsage)
 ownedTransition = ownedUsage-&gt;selectByKind(TransitionUsage)
 ownedCalculation = ownedUsage-&gt;selectByKind(CalculationUsage)
 ownedConstraint = ownedUsage-&gt;selectByKind(ConstraintUsage)
 ownedRequirement = ownedUsage-&gt;selectByKind(RequirementUsage)
 ownedConcern = ownedUsage-&gt;selectByKind(ConcernUsage)
 ownedCase = ownedUsage-&gt;selectByKind(CaseUsage)
 ownedAnalysisCase = ownedUsage-&gt;selectByKind(AnalysisCaseUsage)
 ownedVerificationCase = ownedUsage-&gt;selectByKind(VerificationCaseUsage)
 ownedUseCase = ownedUsage-&gt;selectByKind(UseCaseUsage)
 ownedView = ownedUsage-&gt;selectByKind(ViewUsage)
 ownedViewpoint = ownedUsage-&gt;selectByKind(ViewpointUsage)
 ownedRendering = ownedUsage-&gt;selectByKind(RenderingUsage)
 ownedMetadata = ownedUsage-&gt;selectByKind(MetadataUsage)
 isVariation implies isAbstract</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDirectedUsage()">getDirectedUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>usages</code> of this <code>Definition</code> that are <code>directedFeatures</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedAction()">getOwnedAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ActionUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedAllocation()">getOwnedAllocation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>AllocationUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedAnalysisCase()">getOwnedAnalysisCase</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>AnalysisCaseUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedAttribute()">getOwnedAttribute</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>AttributeUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedCalculation()">getOwnedCalculation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>CalculationUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedCase()">getOwnedCase</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The code&gt;CaseUsages that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedConcern()">getOwnedConcern</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ConcernUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedConnection()">getOwnedConnection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ConnectorAsUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedConstraint()">getOwnedConstraint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ConstraintUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedEnumeration()">getOwnedEnumeration</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>EnumerationUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedFlow()">getOwnedFlow</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>FlowUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedInterface()">getOwnedInterface</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>InterfaceUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedItem()">getOwnedItem</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ItemUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedMetadata()">getOwnedMetadata</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>MetadataUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedOccurrence()">getOwnedOccurrence</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>OccurrenceUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedPart()">getOwnedPart</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>PartUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedPort()">getOwnedPort</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>PortUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedReference()">getOwnedReference</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ReferenceUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedRendering()">getOwnedRendering</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>RenderingUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedRequirement()">getOwnedRequirement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>RequirementUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedState()">getOwnedState</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>StateUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedTransition()">getOwnedTransition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>TransitionUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedUsage()">getOwnedUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Usages</code> that are <code>ownedFeatures</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedUseCase()">getOwnedUseCase</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>UseCaseUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedVerificationCase()">getOwnedVerificationCase</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>VerificationCaseUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedView()">getOwnedView</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ViewUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedViewpoint()">getOwnedViewpoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ViewpointUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUsage()">getUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Usages</code> that are <code>features</code> of this <code>Definition</code> (not necessarily owned).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVariant()">getVariant</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Usages</code> which represent the variants of this <code>Definition</code> as a variation point <code>Definition</code>, if <code>isVariation</code> = true.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VariantMembership</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVariantMembership()">getVariantMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedMemberships</code> of this <code>Definition</code> that are <code>VariantMemberships</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isVariation()">isVariation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this <code>Definition</code> is for a variation point or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsVariation(boolean)">setIsVariation</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this <code>Definition</code> is for a variation point or not.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()">getID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)">setID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Classifier">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a></h3>
<code><a href="../../../kerml/model/kerml/Classifier.html#getOwnedSubclassification()">getOwnedSubclassification</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Element">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></h3>
<code><a href="../../../kerml/model/kerml/Element.html#effectiveName()">effectiveName</a>, <a href="../../../kerml/model/kerml/Element.html#effectiveShortName()">effectiveShortName</a>, <a href="../../../kerml/model/kerml/Element.html#escapedName()">escapedName</a>, <a href="../../../kerml/model/kerml/Element.html#getAliasIds()">getAliasIds</a>, <a href="../../../kerml/model/kerml/Element.html#getDeclaredName()">getDeclaredName</a>, <a href="../../../kerml/model/kerml/Element.html#getDeclaredShortName()">getDeclaredShortName</a>, <a href="../../../kerml/model/kerml/Element.html#getDocumentation()">getDocumentation</a>, <a href="../../../kerml/model/kerml/Element.html#getElementId()">getElementId</a>, <a href="../../../kerml/model/kerml/Element.html#getName()">getName</a>, <a href="../../../kerml/model/kerml/Element.html#getOwnedAnnotation()">getOwnedAnnotation</a>, <a href="../../../kerml/model/kerml/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../../../kerml/model/kerml/Element.html#getOwnedRelationship()">getOwnedRelationship</a>, <a href="../../../kerml/model/kerml/Element.html#getOwner()">getOwner</a>, <a href="../../../kerml/model/kerml/Element.html#getOwningMembership()">getOwningMembership</a>, <a href="../../../kerml/model/kerml/Element.html#getOwningNamespace()">getOwningNamespace</a>, <a href="../../../kerml/model/kerml/Element.html#getOwningRelationship()">getOwningRelationship</a>, <a href="../../../kerml/model/kerml/Element.html#getQualifiedName()">getQualifiedName</a>, <a href="../../../kerml/model/kerml/Element.html#getShortName()">getShortName</a>, <a href="../../../kerml/model/kerml/Element.html#getTextualRepresentation()">getTextualRepresentation</a>, <a href="../../../kerml/model/kerml/Element.html#isImpliedIncluded()">isImpliedIncluded</a>, <a href="../../../kerml/model/kerml/Element.html#isLibraryElement()">isLibraryElement</a>, <a href="../../../kerml/model/kerml/Element.html#libraryNamespace()">libraryNamespace</a>, <a href="../../../kerml/model/kerml/Element.html#path()">path</a>, <a href="../../../kerml/model/kerml/Element.html#setDeclaredName(java.lang.String)">setDeclaredName</a>, <a href="../../../kerml/model/kerml/Element.html#setDeclaredShortName(java.lang.String)">setDeclaredShortName</a>, <a href="../../../kerml/model/kerml/Element.html#setElementId(java.lang.String)">setElementId</a>, <a href="../../../kerml/model/kerml/Element.html#setIsImpliedIncluded(boolean)">setIsImpliedIncluded</a>, <a href="../../../kerml/model/kerml/Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwner</a>, <a href="../../../kerml/model/kerml/Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">setOwningMembership</a>, <a href="../../../kerml/model/kerml/Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">setOwningRelationship</a></code></div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Namespace">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></h3>
<code><a href="../../../kerml/model/kerml/Namespace.html#getImportedMembership()">getImportedMembership</a>, <a href="../../../kerml/model/kerml/Namespace.html#getMember()">getMember</a>, <a href="../../../kerml/model/kerml/Namespace.html#getMembership()">getMembership</a>, <a href="../../../kerml/model/kerml/Namespace.html#getOwnedImport()">getOwnedImport</a>, <a href="../../../kerml/model/kerml/Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="../../../kerml/model/kerml/Namespace.html#getOwnedMembership()">getOwnedMembership</a>, <a href="../../../kerml/model/kerml/Namespace.html#importedMemberships(java.util.List)">importedMemberships</a>, <a href="../../../kerml/model/kerml/Namespace.html#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)">membershipsOfVisibility</a>, <a href="../../../kerml/model/kerml/Namespace.html#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)">namesOf</a>, <a href="../../../kerml/model/kerml/Namespace.html#qualificationOf(java.lang.String)">qualificationOf</a>, <a href="../../../kerml/model/kerml/Namespace.html#resolve(java.lang.String)">resolve</a>, <a href="../../../kerml/model/kerml/Namespace.html#resolveGlobal(java.lang.String)">resolveGlobal</a>, <a href="../../../kerml/model/kerml/Namespace.html#resolveLocal(java.lang.String)">resolveLocal</a>, <a href="../../../kerml/model/kerml/Namespace.html#resolveVisible(java.lang.String)">resolveVisible</a>, <a href="../../../kerml/model/kerml/Namespace.html#unqualifiedNameOf(java.lang.String)">unqualifiedNameOf</a>, <a href="../../../kerml/model/kerml/Namespace.html#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">visibilityOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Type">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></h3>
<code><a href="../../../kerml/model/kerml/Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">allRedefinedFeaturesOf</a>, <a href="../../../kerml/model/kerml/Type.html#allSupertypes()">allSupertypes</a>, <a href="../../../kerml/model/kerml/Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">directionOf</a>, <a href="../../../kerml/model/kerml/Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">directionOfExcluding</a>, <a href="../../../kerml/model/kerml/Type.html#getDifferencingType()">getDifferencingType</a>, <a href="../../../kerml/model/kerml/Type.html#getDirectedFeature()">getDirectedFeature</a>, <a href="../../../kerml/model/kerml/Type.html#getEndFeature()">getEndFeature</a>, <a href="../../../kerml/model/kerml/Type.html#getFeature()">getFeature</a>, <a href="../../../kerml/model/kerml/Type.html#getFeatureMembership()">getFeatureMembership</a>, <a href="../../../kerml/model/kerml/Type.html#getInheritedFeature()">getInheritedFeature</a>, <a href="../../../kerml/model/kerml/Type.html#getInheritedMembership()">getInheritedMembership</a>, <a href="../../../kerml/model/kerml/Type.html#getInput()">getInput</a>, <a href="../../../kerml/model/kerml/Type.html#getIntersectingType()">getIntersectingType</a>, <a href="../../../kerml/model/kerml/Type.html#getMultiplicity()">getMultiplicity</a>, <a href="../../../kerml/model/kerml/Type.html#getOutput()">getOutput</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedConjugator()">getOwnedConjugator</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedDifferencing()">getOwnedDifferencing</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedDisjoining()">getOwnedDisjoining</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedEndFeature()">getOwnedEndFeature</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedFeature()">getOwnedFeature</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedFeatureMembership()">getOwnedFeatureMembership</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedIntersecting()">getOwnedIntersecting</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedSpecialization()">getOwnedSpecialization</a>, <a href="../../../kerml/model/kerml/Type.html#getOwnedUnioning()">getOwnedUnioning</a>, <a href="../../../kerml/model/kerml/Type.html#getUnioningType()">getUnioningType</a>, <a href="../../../kerml/model/kerml/Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)">inheritableMemberships</a>, <a href="../../../kerml/model/kerml/Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)">inheritedMemberships</a>, <a href="../../../kerml/model/kerml/Type.html#isAbstract()">isAbstract</a>, <a href="../../../kerml/model/kerml/Type.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isCompatibleWith</a>, <a href="../../../kerml/model/kerml/Type.html#isConjugated()">isConjugated</a>, <a href="../../../kerml/model/kerml/Type.html#isSufficient()">isSufficient</a>, <a href="../../../kerml/model/kerml/Type.html#multiplicities()">multiplicities</a>, <a href="../../../kerml/model/kerml/Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)">nonPrivateMemberships</a>, <a href="../../../kerml/model/kerml/Type.html#removeRedefinedFeatures(java.util.List)">removeRedefinedFeatures</a>, <a href="../../../kerml/model/kerml/Type.html#setIsAbstract(boolean)">setIsAbstract</a>, <a href="../../../kerml/model/kerml/Type.html#setIsSufficient(boolean)">setIsSufficient</a>, <a href="../../../kerml/model/kerml/Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">specializes</a>, <a href="../../../kerml/model/kerml/Type.html#specializesFromLibrary(java.lang.String)">specializesFromLibrary</a>, <a href="../../../kerml/model/kerml/Type.html#supertypes(boolean)">supertypes</a>, <a href="../../../kerml/model/kerml/Type.html#visibleMemberships(java.util.List,boolean,boolean)">visibleMemberships</a></code></div>
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
<section class="detail" id="isVariation()">
<h3>isVariation</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isVariation</span>()</div>
<div class="block"><p>Whether this <code>Definition</code> is for a variation point or not. If true, then all the <code>memberships</code> of the <code>Definition</code> must be <code>VariantMemberships</code>.</p></div>
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
<div class="block"><p>Whether this <code>Definition</code> is for a variation point or not. If true, then all the <code>memberships</code> of the <code>Definition</code> must be <code>VariantMemberships</code>.</p></div>
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
<section class="detail" id="getVariant()">
<h3>getVariant</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</span> <span class="element-name">getVariant</span>()</div>
<div class="block"><p>The <code>Usages</code> which represent the variants of this <code>Definition</code> as a variation point <code>Definition</code>, if <code>isVariation</code> = true. If <code>isVariation = false</code>, the there must be no <code>variants</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the variant value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="owningVariationDefinition"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVariantMembership()">
<h3>getVariantMembership</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VariantMembership</a>&gt;</span> <span class="element-name">getVariantMembership</span>()</div>
<div class="block"><p>The <code>ownedMemberships</code> of this <code>Definition</code> that are <code>VariantMemberships</code>. If <code>isVariation</code> = true, then this must be all <code>ownedMemberships</code> of the <code>Definition</code>. If <code>isVariation</code> = false, then <code>variantMembership</code>must be empty.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the variantMembership value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="owningVariationDefinition"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsage()">
<h3>getUsage</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</span> <span class="element-name">getUsage</span>()</div>
<div class="block"><p>The <code>Usages</code> that are <code>features</code> of this <code>Definition</code> (not necessarily owned).</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the usage value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="featuringDefinition"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirectedUsage()">
<h3>getDirectedUsage</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</span> <span class="element-name">getDirectedUsage</span>()</div>
<div class="block"><p>The <code>usages</code> of this <code>Definition</code> that are <code>directedFeatures</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the directedUsage value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="definitionWithDirectedUsage"
        subsets=<a href="#getUsage()"><code>getUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedUsage()">
<h3>getOwnedUsage</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a>&gt;</span> <span class="element-name">getOwnedUsage</span>()</div>
<div class="block"><p>The <code>Usages</code> that are <code>ownedFeatures</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedUsage value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Usage.html#getOwningDefinition()"><code>Usage.getOwningDefinition()</code></a>
        subsets=<a href="#getUsage()"><code>getUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedReference()">
<h3>getOwnedReference</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a>&gt;</span> <span class="element-name">getOwnedReference</span>()</div>
<div class="block"><p>The <code>ReferenceUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedReference value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="referenceOwningDefinition"
        subsets=<a href="#getOwnedUsage()"><code>getOwnedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedAttribute()">
<h3>getOwnedAttribute</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a>&gt;</span> <span class="element-name">getOwnedAttribute</span>()</div>
<div class="block"><p>The <code>AttributeUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.<p></p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedAttribute value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="attributeOwningDefinition"
        subsets=<a href="#getOwnedUsage()"><code>getOwnedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedEnumeration()">
<h3>getOwnedEnumeration</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a>&gt;</span> <span class="element-name">getOwnedEnumeration</span>()</div>
<div class="block"><p>The <code>EnumerationUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.<p></p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedEnumeration value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="enumerationOwningDefinition"
        subsets=<a href="#getOwnedAttribute()"><code>getOwnedAttribute()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedOccurrence()">
<h3>getOwnedOccurrence</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a>&gt;</span> <span class="element-name">getOwnedOccurrence</span>()</div>
<div class="block"><p>The <code>OccurrenceUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedOccurrence value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="occurrenceOwningDefinition"
        subsets=<a href="#getOwnedUsage()"><code>getOwnedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedItem()">
<h3>getOwnedItem</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a>&gt;</span> <span class="element-name">getOwnedItem</span>()</div>
<div class="block"><p>The <code>ItemUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedItem value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="itemOwningDefinition"
        subsets=<a href="#getOwnedOccurrence()"><code>getOwnedOccurrence()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedPart()">
<h3>getOwnedPart</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</span> <span class="element-name">getOwnedPart</span>()</div>
<div class="block"><p>The <code>PartUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedPart value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="partOwningDefinition"
        subsets=<a href="#getOwnedItem()"><code>getOwnedItem()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedPort()">
<h3>getOwnedPort</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a>&gt;</span> <span class="element-name">getOwnedPort</span>()</div>
<div class="block"><p>The <code>PortUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedPort value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="portOwningDefinition"
        subsets=<a href="#getOwnedUsage()"><code>getOwnedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedConnection()">
<h3>getOwnedConnection</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a>&gt;</span> <span class="element-name">getOwnedConnection</span>()</div>
<div class="block"><p>The <code>ConnectorAsUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>. Note that this list includes <code>BindingConnectorAsUsages</code>, <code>SuccessionAsUsages</code>, and <code>FlowUsages</code> because these are <code>ConnectorAsUsages</code> even though they are not <code>ConnectionUsages</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedConnection value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="connectionOwningDefinition"
        subsets=<a href="#getOwnedUsage()"><code>getOwnedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedFlow()">
<h3>getOwnedFlow</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a>&gt;</span> <span class="element-name">getOwnedFlow</span>()</div>
<div class="block"><p>The <code>FlowUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedFlow value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="flowOwningDefinition"
        subsets=<a href="#getOwnedConnection()"><code>getOwnedConnection()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedInterface()">
<h3>getOwnedInterface</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a>&gt;</span> <span class="element-name">getOwnedInterface</span>()</div>
<div class="block"><p>The <code>InterfaceUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedInterface value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="interfaceOwningDefinition"
        subsets=<a href="#getOwnedConnection()"><code>getOwnedConnection()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedAllocation()">
<h3>getOwnedAllocation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a>&gt;</span> <span class="element-name">getOwnedAllocation</span>()</div>
<div class="block"><p>The <code>AllocationUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedAllocation value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="allocationOwningDefinition"
        subsets=<a href="#getOwnedConnection()"><code>getOwnedConnection()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedAction()">
<h3>getOwnedAction</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt;</span> <span class="element-name">getOwnedAction</span>()</div>
<div class="block"><p>The <code>ActionUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedAction value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="actionOwningDefinition"
        subsets=<a href="#getOwnedOccurrence()"><code>getOwnedOccurrence()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedState()">
<h3>getOwnedState</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a>&gt;</span> <span class="element-name">getOwnedState</span>()</div>
<div class="block"><p>The <code>StateUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedState value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="stateOwningDefinition"
        subsets=<a href="#getOwnedAction()"><code>getOwnedAction()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedTransition()">
<h3>getOwnedTransition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a>&gt;</span> <span class="element-name">getOwnedTransition</span>()</div>
<div class="block"><p>The <code>TransitionUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedTransition value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="transitionOwningDefinition"
        subsets=<a href="#getOwnedUsage()"><code>getOwnedUsage()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedCalculation()">
<h3>getOwnedCalculation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a>&gt;</span> <span class="element-name">getOwnedCalculation</span>()</div>
<div class="block"><p>The <code>CalculationUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedCalculation value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="calculationOwningDefinition"
        subsets=<a href="#getOwnedAction()"><code>getOwnedAction()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedConstraint()">
<h3>getOwnedConstraint</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a>&gt;</span> <span class="element-name">getOwnedConstraint</span>()</div>
<div class="block"><p>The <code>ConstraintUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedConstraint value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="constraintOwningDefinition"
        subsets=<a href="#getOwnedOccurrence()"><code>getOwnedOccurrence()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedRequirement()">
<h3>getOwnedRequirement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a>&gt;</span> <span class="element-name">getOwnedRequirement</span>()</div>
<div class="block"><p>The <code>RequirementUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedRequirement value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="requirementOwningDefinition"
        subsets=<a href="#getOwnedConstraint()"><code>getOwnedConstraint()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedConcern()">
<h3>getOwnedConcern</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a>&gt;</span> <span class="element-name">getOwnedConcern</span>()</div>
<div class="block"><p>The <code>ConcernUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedConcern value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="concernOwningDefinition"
        subsets=<a href="#getOwnedRequirement()"><code>getOwnedRequirement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedCase()">
<h3>getOwnedCase</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a>&gt;</span> <span class="element-name">getOwnedCase</span>()</div>
<div class="block"><p>The code&gt;CaseUsages that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedCase value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="caseOwningDefinition"
        subsets=<a href="#getOwnedCalculation()"><code>getOwnedCalculation()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedAnalysisCase()">
<h3>getOwnedAnalysisCase</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a>&gt;</span> <span class="element-name">getOwnedAnalysisCase</span>()</div>
<div class="block"><p>The <code>AnalysisCaseUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedAnalysisCase value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="analysisCaseOwningDefinition"
        subsets=<a href="#getOwnedCase()"><code>getOwnedCase()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedVerificationCase()">
<h3>getOwnedVerificationCase</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a>&gt;</span> <span class="element-name">getOwnedVerificationCase</span>()</div>
<div class="block"><p>The <code>VerificationCaseUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedVerificationCase value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="verificationCaseOwningDefinition"
        subsets=<a href="#getOwnedCase()"><code>getOwnedCase()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedUseCase()">
<h3>getOwnedUseCase</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a>&gt;</span> <span class="element-name">getOwnedUseCase</span>()</div>
<div class="block"><p>The <code>UseCaseUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedUseCase value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="useCaseOwningDefinition"
        subsets=<a href="#getOwnedCase()"><code>getOwnedCase()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedView()">
<h3>getOwnedView</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a>&gt;</span> <span class="element-name">getOwnedView</span>()</div>
<div class="block"><p>The <code>ViewUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedView value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="viewOwningDefinition"
        subsets=<a href="#getOwnedPart()"><code>getOwnedPart()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedViewpoint()">
<h3>getOwnedViewpoint</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a>&gt;</span> <span class="element-name">getOwnedViewpoint</span>()</div>
<div class="block"><p>The <code>ViewpointUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedViewpoint value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="viewpointOwningDefinition"
        subsets=<a href="#getOwnedRequirement()"><code>getOwnedRequirement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedRendering()">
<h3>getOwnedRendering</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a>&gt;</span> <span class="element-name">getOwnedRendering</span>()</div>
<div class="block"><p>The <code>RenderingUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedRendering value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="redenderingOwningDefinition"
        subsets=<a href="#getOwnedPart()"><code>getOwnedPart()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedMetadata()">
<h3>getOwnedMetadata</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a>&gt;</span> <span class="element-name">getOwnedMetadata</span>()</div>
<div class="block"><p>The <code>MetadataUsages</code> that are <code>ownedUsages</code> of this <code>Definition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedMetadata value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="metadataOwningDefinition"
        subsets=<a href="#getOwnedItem()"><code>getOwnedItem()</code></a></dd>
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
