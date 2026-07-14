# JAVA OPENAPI: Type (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Type.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Type.html`
- source_sha256: `73c28532bd3d1e8afdaa1c5c2f2311e7eb4404afbd1bb4162222ccdf5cc2f5d0`
- captured_utc: `2026-07-14T16:44:51.209890+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Type

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `[Namespace](Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`

All Known Subinterfaces:
`[AcceptActionUsage](../../../sysml/model/sysml/AcceptActionUsage.html)`, `[ActionDefinition](../../../sysml/model/sysml/ActionDefinition.html)`, `[ActionUsage](../../../sysml/model/sysml/ActionUsage.html)`, `[AllocationDefinition](../../../sysml/model/sysml/AllocationDefinition.html)`, `[AllocationUsage](../../../sysml/model/sysml/AllocationUsage.html)`, `[AnalysisCaseDefinition](../../../sysml/model/sysml/AnalysisCaseDefinition.html)`, `[AnalysisCaseUsage](../../../sysml/model/sysml/AnalysisCaseUsage.html)`, `[AssertConstraintUsage](../../../sysml/model/sysml/AssertConstraintUsage.html)`, `[AssignmentActionUsage](../../../sysml/model/sysml/AssignmentActionUsage.html)`, `[Association](Association.html)`, `[AssociationStructure](AssociationStructure.html)`, `[AttributeDefinition](../../../sysml/model/sysml/AttributeDefinition.html)`, `[AttributeUsage](../../../sysml/model/sysml/AttributeUsage.html)`, `[Behavior](Behavior.html)`, `[BindingConnector](BindingConnector.html)`, `[BindingConnectorAsUsage](../../../sysml/model/sysml/BindingConnectorAsUsage.html)`, `[BooleanExpression](BooleanExpression.html)`, `[CalculationDefinition](../../../sysml/model/sysml/CalculationDefinition.html)`, `[CalculationUsage](../../../sysml/model/sysml/CalculationUsage.html)`, `[CaseDefinition](../../../sysml/model/sysml/CaseDefinition.html)`, `[CaseUsage](../../../sysml/model/sysml/CaseUsage.html)`, `[Class](Class.html)`, `[Classifier](Classifier.html)`, `[CollectExpression](CollectExpression.html)`, `[ConcernDefinition](../../../sysml/model/sysml/ConcernDefinition.html)`, `[ConcernUsage](../../../sysml/model/sysml/ConcernUsage.html)`, `[ConjugatedPortDefinition](../../../sysml/model/sysml/ConjugatedPortDefinition.html)`, `[ConnectionDefinition](../../../sysml/model/sysml/ConnectionDefinition.html)`, `[ConnectionUsage](../../../sysml/model/sysml/ConnectionUsage.html)`, `[Connector](Connector.html)`, `[ConnectorAsUsage](../../../sysml/model/sysml/ConnectorAsUsage.html)`, `[ConstraintDefinition](../../../sysml/model/sysml/ConstraintDefinition.html)`, `[ConstraintUsage](../../../sysml/model/sysml/ConstraintUsage.html)`, `[ConstructorExpression](ConstructorExpression.html)`, `[ControlNode](../../../sysml/model/sysml/ControlNode.html)`, `[DataType](DataType.html)`, `[DecisionNode](../../../sysml/model/sysml/DecisionNode.html)`, `[Definition](../../../sysml/model/sysml/Definition.html)`, `[EnumerationDefinition](../../../sysml/model/sysml/EnumerationDefinition.html)`, `[EnumerationUsage](../../../sysml/model/sysml/EnumerationUsage.html)`, `[EventOccurrenceUsage](../../../sysml/model/sysml/EventOccurrenceUsage.html)`, `[ExhibitStateUsage](../../../sysml/model/sysml/ExhibitStateUsage.html)`, `[Expression](Expression.html)`, `[Feature](Feature.html)`, `[FeatureChainExpression](FeatureChainExpression.html)`, `[FeatureReferenceExpression](FeatureReferenceExpression.html)`, `[Flow](Flow.html)`, `[FlowDefinition](../../../sysml/model/sysml/FlowDefinition.html)`, `[FlowEnd](FlowEnd.html)`, `[FlowUsage](../../../sysml/model/sysml/FlowUsage.html)`, `[ForkNode](../../../sysml/model/sysml/ForkNode.html)`, `[ForLoopActionUsage](../../../sysml/model/sysml/ForLoopActionUsage.html)`, `[Function](Function.html)`, `[IfActionUsage](../../../sysml/model/sysml/IfActionUsage.html)`, `[IncludeUseCaseUsage](../../../sysml/model/sysml/IncludeUseCaseUsage.html)`, `[IndexExpression](IndexExpression.html)`, `[InstantiationExpression](InstantiationExpression.html)`, `[Interaction](Interaction.html)`, `[InterfaceDefinition](../../../sysml/model/sysml/InterfaceDefinition.html)`, `[InterfaceUsage](../../../sysml/model/sysml/InterfaceUsage.html)`, `[Invariant](Invariant.html)`, `[InvocationExpression](InvocationExpression.html)`, `[ItemDefinition](../../../sysml/model/sysml/ItemDefinition.html)`, `[ItemUsage](../../../sysml/model/sysml/ItemUsage.html)`, `[JoinNode](../../../sysml/model/sysml/JoinNode.html)`, `[LiteralBoolean](LiteralBoolean.html)`, `[LiteralExpression](LiteralExpression.html)`, `[LiteralInfinity](LiteralInfinity.html)`, `[LiteralInteger](LiteralInteger.html)`, `[LiteralRational](LiteralRational.html)`, `[LiteralString](LiteralString.html)`, `[LoopActionUsage](../../../sysml/model/sysml/LoopActionUsage.html)`, `[MergeNode](../../../sysml/model/sysml/MergeNode.html)`, `[Metaclass](Metaclass.html)`, `[MetadataAccessExpression](MetadataAccessExpression.html)`, `[MetadataDefinition](../../../sysml/model/sysml/MetadataDefinition.html)`, `[MetadataFeature](MetadataFeature.html)`, `[MetadataUsage](../../../sysml/model/sysml/MetadataUsage.html)`, `[Multiplicity](Multiplicity.html)`, `[MultiplicityRange](MultiplicityRange.html)`, `[NullExpression](NullExpression.html)`, `[OccurrenceDefinition](../../../sysml/model/sysml/OccurrenceDefinition.html)`, `[OccurrenceUsage](../../../sysml/model/sysml/OccurrenceUsage.html)`, `[OperatorExpression](OperatorExpression.html)`, `[PartDefinition](../../../sysml/model/sysml/PartDefinition.html)`, `[PartUsage](../../../sysml/model/sysml/PartUsage.html)`, `[PayloadFeature](PayloadFeature.html)`, `[PerformActionUsage](../../../sysml/model/sysml/PerformActionUsage.html)`, `[PortDefinition](../../../sysml/model/sysml/PortDefinition.html)`, `[PortUsage](../../../sysml/model/sysml/PortUsage.html)`, `[Predicate](Predicate.html)`, `[ReferenceUsage](../../../sysml/model/sysml/ReferenceUsage.html)`, `[RenderingDefinition](../../../sysml/model/sysml/RenderingDefinition.html)`, `[RenderingUsage](../../../sysml/model/sysml/RenderingUsage.html)`, `[RequirementDefinition](../../../sysml/model/sysml/RequirementDefinition.html)`, `[RequirementUsage](../../../sysml/model/sysml/RequirementUsage.html)`, `[SatisfyRequirementUsage](../../../sysml/model/sysml/SatisfyRequirementUsage.html)`, `[SelectExpression](SelectExpression.html)`, `[SendActionUsage](../../../sysml/model/sysml/SendActionUsage.html)`, `[StateDefinition](../../../sysml/model/sysml/StateDefinition.html)`, `[StateUsage](../../../sysml/model/sysml/StateUsage.html)`, `[Step](Step.html)`, `[Structure](Structure.html)`, `[Succession](Succession.html)`, `[SuccessionAsUsage](../../../sysml/model/sysml/SuccessionAsUsage.html)`, `[SuccessionFlow](SuccessionFlow.html)`, `[SuccessionFlowUsage](../../../sysml/model/sysml/SuccessionFlowUsage.html)`, `[TerminateActionUsage](../../../sysml/model/sysml/TerminateActionUsage.html)`, `[TransitionUsage](../../../sysml/model/sysml/TransitionUsage.html)`, `[TriggerInvocationExpression](../../../sysml/model/sysml/TriggerInvocationExpression.html)`, `[Usage](../../../sysml/model/sysml/Usage.html)`, `[UseCaseDefinition](../../../sysml/model/sysml/UseCaseDefinition.html)`, `[UseCaseUsage](../../../sysml/model/sysml/UseCaseUsage.html)`, `[VerificationCaseDefinition](../../../sysml/model/sysml/VerificationCaseDefinition.html)`, `[VerificationCaseUsage](../../../sysml/model/sysml/VerificationCaseUsage.html)`, `[ViewDefinition](../../../sysml/model/sysml/ViewDefinition.html)`, `[ViewpointDefinition](../../../sysml/model/sysml/ViewpointDefinition.html)`, `[ViewpointUsage](../../../sysml/model/sysml/ViewpointUsage.html)`, `[ViewUsage](../../../sysml/model/sysml/ViewUsage.html)`, `[WhileLoopActionUsage](../../../sysml/model/sysml/WhileLoopActionUsage.html)`

@OpenApiAllpublic interfaceTypeextends [Namespace](Namespace.html)

A `Type` is a `Namespace` that is the most general kind of `Element` supporting the semantics of classification. A `Type` may be a `Classifier` or a `Feature`, defining conditions on what is classified by the `Type` (see also the description of `isSufficient`).
 
 ownedSpecialization = ownedRelationship->selectByKind(Specialization)->
 select(s | s.special = self)
 
 multiplicity = 
 let ownedMultiplicities: Sequence(Multiplicity) =
 ownedMember->selectByKind(Multiplicity) in
 if ownedMultiplicities->isEmpty() then null
 else ownedMultiplicities->first()
 endif
 ownedFeatureMembership = ownedRelationship->selectByKind(FeatureMembership)
 ownedConjugator =
 let ownedConjugators: Sequence(Conjugator) = 
 ownedRelationship->selectByKind(Conjugation) in
 if ownedConjugators->isEmpty() then null 
 else ownedConjugators->at(1) endif
 output = feature->select(f | 
 let direction: FeatureDirectionKind = directionOf(f) in
 direction = FeatureDirectionKind::out or
 direction = FeatureDirectionKind::inout)
 input = feature->select(f | 
 let direction: FeatureDirectionKind = directionOf(f) in
 direction = FeatureDirectionKind::_'in' or
 direction = FeatureDirectionKind::inout)
 inheritedMembership = inheritedMemberships(Set{}, Set{}, false)
 specializesFromLibrary('Base::Anything')
 directedFeature = feature->select(f | directionOf(f) <> null)
 feature = featureMembership.ownedMemberFeature
 featureMembership = ownedFeatureMembership->union(
 inheritedMembership->selectByKind(FeatureMembership))
 ownedFeature = ownedFeatureMembership.ownedMemberFeature
 differencingType = ownedDifferencing.differencingType
 intersectingType->excludes(self)
 differencingType->excludes(self)
 unioningType = ownedUnioning.unioningType
 unioningType->excludes(self)
 intersectingType = ownedIntersecting.intersectingType
 ownedRelationship->selectByKind(Conjugation)->size() <= 1
 ownedMember->selectByKind(Multiplicity)->size() <= 1
 endFeature = feature->select(isEnd)
 ownedDisjoining =
 ownedRelationship->selectByKind(Disjoining)
 ownedUnioning =
 ownedRelationship->selectByKind(Unioning)
 ownedRelationship->selectByKind(Intersecting)
 ownedDifferencing =
 ownedRelationship->selectByKind(Differencing)
 ownedEndFeature = ownedFeature->select(isEnd)
 inheritedFeature = inheritedMemberships->
 selectByKind(FeatureMembership).memberFeature
 ownedUnioning->size() <> 1
 ownedIntersecting->size() <> 1
 ownedDifferencing->size() <> 1

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[allRedefinedFeaturesOf](#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership))([Membership](Membership.html) membership)`
If the `memberElement` of the given `membership` is a `Feature`, then return all `Features` directly or indirectly redefined by the `memberElement`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)>`
`[allSupertypes](#allSupertypes())()`
Return this `Type` and all `Types` that are directly or transitively supertypes of this `Type` (as determined by the `supertypes` operation with `excludeImplied = false`).
`[FeatureDirectionKind](FeatureDirectionKind.html)`
`[directionOf](#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](Feature.html) feature)`
If the given `feature` is a `feature` of this `Type`, then return its direction relative to this `Type`, taking conjugation into account.
`[FeatureDirectionKind](FeatureDirectionKind.html)`
`[directionOfExcluding](#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List))([Feature](Feature.html) feature,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> excluded)`
Return the direction of the given `feature` relative to this `Type`, excluding a given set of `Types` from the search of supertypes of this `Type`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)>`
`[getDifferencingType](#getDifferencingType())()`
The interpretations of a `Type` with `differencingTypes` are asserted to be those of the first of those `Types`, but not including those of the remaining `Types`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[getDirectedFeature](#getDirectedFeature())()`
The `features` of this `Type` that have a non-null `direction`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[getEndFeature](#getEndFeature())()`
All `features` of this `Type` with `isEnd = true`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[getFeature](#getFeature())()`
The `ownedMemberFeatures` of the `featureMemberships` of this `Type`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureMembership](FeatureMembership.html)>`
`[getFeatureMembership](#getFeatureMembership())()`
The `FeatureMemberships` for `features` of this `Type`, which include all `ownedFeatureMemberships` and those `inheritedMemberships` that are `FeatureMemberships` (but does *not* include any `importedMemberships`).
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[getInheritedFeature](#getInheritedFeature())()`
All the `memberFeatures` of the `inheritedMemberships` of this `Type` that are `FeatureMemberships`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)>`
`[getInheritedMembership](#getInheritedMembership())()`
All `Memberships` inherited by this `Type` via `Specialization` or `Conjugation`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[getInput](#getInput())()`
All `features` related to this `Type` by `FeatureMemberships` that have `direction` `in` or `inout`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)>`
`[getIntersectingType](#getIntersectingType())()`
The interpretations of a `Type` with `intersectingTypes` are asserted to be those in common among the `intersectingTypes`, which are the `Types` derived from the `intersectingType` of the `ownedIntersectings` of this `Type`.
`[Multiplicity](Multiplicity.html)`
`[getMultiplicity](#getMultiplicity())()`
An `ownedMember` of this `Type` that is a `Multiplicity`, which constraints the cardinality of the `Type`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[getOutput](#getOutput())()`
All `features` related to this `Type` by `FeatureMemberships` that have `direction` `out` or `inout`.
`[Conjugation](Conjugation.html)`
`[getOwnedConjugator](#getOwnedConjugator())()`
A `Conjugation` owned by this `Type` for which the `Type` is the `originalType`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Differencing](Differencing.html)>`
`[getOwnedDifferencing](#getOwnedDifferencing())()`
The `ownedRelationships` of this `Type` that are `Differencings`, having this `Type` as their `typeDifferenced`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Disjoining](Disjoining.html)>`
`[getOwnedDisjoining](#getOwnedDisjoining())()`
The `ownedRelationships` of this `Type` that are `Disjoinings`, for which the `Type` is the `typeDisjoined` `Type`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[getOwnedEndFeature](#getOwnedEndFeature())()`
All `endFeatures` of this `Type` that are `ownedFeatures`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[getOwnedFeature](#getOwnedFeature())()`
The `ownedMemberFeatures` of the `ownedFeatureMemberships` of this `Type`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureMembership](FeatureMembership.html)>`
`[getOwnedFeatureMembership](#getOwnedFeatureMembership())()`
The `ownedMemberships` of this `Type` that are `FeatureMemberships`, for which the `Type` is the `owningType`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Intersecting](Intersecting.html)>`
`[getOwnedIntersecting](#getOwnedIntersecting())()`
The `ownedRelationships` of this `Type` that are `Intersectings`, have the `Type` as their `typeIntersected`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Specialization](Specialization.html)>`
`[getOwnedSpecialization](#getOwnedSpecialization())()`
The `ownedRelationships` of this `Type` that are `Specializations`, for which the `Type` is the `specific` `Type`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Unioning](Unioning.html)>`
`[getOwnedUnioning](#getOwnedUnioning())()`
The `ownedRelationships` of this `Type` that are `Unionings`, having the `Type` as their `typeUnioned`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)>`
`[getUnioningType](#getUnioningType())()`
The interpretations of a `Type` with `unioningTypes` are asserted to be the same as those of all the `unioningTypes` together, which are the `Types` derived from the `unioningType` of the `ownedUnionings` of this `Type`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)>`
`[inheritableMemberships](#inheritableMemberships(java.util.List,java.util.List,boolean))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excludedNamespaces,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> excludedTypes,
 boolean excludeImplied)`
Return all the non-`private` `Memberships` of all the supertypes of this `Type`, excluding any supertypes that are this `Type` or are in the given set of `excludedTypes`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)>`
`[inheritedMemberships](#inheritedMemberships(java.util.List,java.util.List,boolean))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excludedNamespaces,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> excludedTypes,
 boolean excludeImplied)`
Return the `Memberships` inheritable from supertypes of this `Type` with redefined `Features` removed.
`boolean`
`[isAbstract](#isAbstract())()`
Indicates whether instances of this `Type` must also be instances of at least one of its specialized `Types`.
`boolean`
`[isCompatibleWith](#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](Type.html) otherType)`
By default, this `Type` is compatible with an `otherType` if it directly or indirectly specializes the `otherType`.
`boolean`
`[isConjugated](#isConjugated())()`
Indicates whether this `Type` has an `ownedConjugator`.
`boolean`
`[isSufficient](#isSufficient())()`
Whether all things that meet the classification conditions of this `Type` must be classified by the `Type`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Multiplicity](Multiplicity.html)>`
`[multiplicities](#multiplicities())()`
Return the owned or inherited `Multiplicities` for this `Typeinvalid input: '<'./code>.`
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)>`
`[nonPrivateMemberships](#nonPrivateMemberships(java.util.List,java.util.List,boolean))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excludedNamespaces,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> excludedTypes,
 boolean excludeImplied)`
Return the `public`, `protected` and inherited `Memberships` of this `Type`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)>`
`[removeRedefinedFeatures](#removeRedefinedFeatures(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> memberships)`
Return a subset of `memberships`, removing those `Memberships` whose `memberElements` are `Features` and for which either of the following two conditions holds:
`void`
`[setIsAbstract](#setIsAbstract(boolean))(boolean value)`
Indicates whether instances of this `Type` must also be instances of at least one of its specialized `Types`.
`void`
`[setIsSufficient](#setIsSufficient(boolean))(boolean value)`
Whether all things that meet the classification conditions of this `Type` must be classified by the `Type`.
`boolean`
`[specializes](#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](Type.html) supertype)`
Check whether this `Type` is a direct or indirect specialization of the given `supertype.`
`boolean`
`[specializesFromLibrary](#specializesFromLibrary(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) libraryTypeName)`
Check whether this `Type` is a direct or indirect specialization of the named library `Type`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)>`
`[supertypes](#supertypes(boolean))(boolean excludeImplied)`
If this `Type` is conjugated, then return just the `originalType` of the `Conjugation`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)>`
`[visibleMemberships](#visibleMemberships(java.util.List,boolean,boolean))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excluded,
 boolean isRecursive,
 boolean includeAll)`
The visible `Memberships` of a `Type` include `inheritedMemberships`.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
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

============ METHOD DETAIL ========== 
Method Details
getOwnedSpecialization
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Specialization](Specialization.html)> getOwnedSpecialization()
The `ownedRelationships` of this `Type` that are `Specializations`, for which the `Type` is the `specific` `Type`.
Returns:
the ownedSpecialization value
Model:
derived="true"
 transient="true"
 opposite=[`Specialization.getOwningType()`](Specialization.html#getOwningType())
 subsets=[`Element.getOwnedRelationship()`](Element.html#getOwnedRelationship())
getOwnedFeatureMembership
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureMembership](FeatureMembership.html)> getOwnedFeatureMembership()
The `ownedMemberships` of this `Type` that are `FeatureMemberships`, for which the `Type` is the `owningType`. Each such `FeatureMembership` identifies an `ownedFeature` of the `Type`.
Returns:
the ownedFeatureMembership value
Model:
derived="true"
 transient="true"
 opposite=[`FeatureMembership.getOwningType()`](FeatureMembership.html#getOwningType())
 subsets=[`Namespace.getOwnedMembership()`](Namespace.html#getOwnedMembership()), [`getFeatureMembership()`](#getFeatureMembership())
getFeature
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> getFeature()
The `ownedMemberFeatures` of the `featureMemberships` of this `Type`.
Returns:
the feature value
Model:
derived="true"
 transient="true"
 oppositeRoleName="typeWithFeature"
 subsets=[`Namespace.getMember()`](Namespace.html#getMember())
getOwnedFeature
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> getOwnedFeature()
The `ownedMemberFeatures` of the `ownedFeatureMemberships` of this `Type`.
Returns:
the ownedFeature value
Model:
derived="true"
 transient="true"
 opposite=[`Feature.getOwningType()`](Feature.html#getOwningType())
 subsets=[`Namespace.getOwnedMember()`](Namespace.html#getOwnedMember())
getInput
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> getInput()
All `features` related to this `Type` by `FeatureMemberships` that have `direction` `in` or `inout`.
Returns:
the input value
Model:
derived="true"
 transient="true"
 oppositeRoleName="typeWithInput"
 subsets=[`getDirectedFeature()`](#getDirectedFeature())
getOutput
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> getOutput()
All `features` related to this `Type` by `FeatureMemberships` that have `direction` `out` or `inout`.
Returns:
the output value
Model:
derived="true"
 transient="true"
 oppositeRoleName="typeWithOutput"
 subsets=[`getDirectedFeature()`](#getDirectedFeature())
isAbstract
boolean isAbstract()
Indicates whether instances of this `Type` must also be instances of at least one of its specialized `Types`.
Returns:
the isAbstract value
Model:
derived="false"
 transient="false"
setIsAbstract
void setIsAbstract(boolean value)
Indicates whether instances of this `Type` must also be instances of at least one of its specialized `Types`.
Parameters:
`value` - the isAbstract value
Model:
derived="false"
 transient="false"
getInheritedMembership
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> getInheritedMembership()
All `Memberships` inherited by this `Type` via `Specialization` or `Conjugation`. These are included in the derived union for the `memberships` of the `Type`.
Returns:
the inheritedMembership value
Model:
derived="true"
 transient="true"
 oppositeRoleName="inheritingType"
 subsets=[`Namespace.getMembership()`](Namespace.html#getMembership())
getEndFeature
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> getEndFeature()
All `features` of this `Type` with `isEnd = true`.
Returns:
the endFeature value
Model:
derived="true"
 transient="true"
 oppositeRoleName="typeWithEndFeature"
 subsets=[`getFeature()`](#getFeature())
getOwnedEndFeature
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> getOwnedEndFeature()
All `endFeatures` of this `Type` that are `ownedFeatures`.
Returns:
the ownedEndFeature value
Model:
derived="true"
 transient="true"
 opposite=[`Feature.getEndOwningType()`](Feature.html#getEndOwningType())
 subsets=[`getEndFeature()`](#getEndFeature()), [`getOwnedFeature()`](#getOwnedFeature())
isSufficient
boolean isSufficient()
Whether all things that meet the classification conditions of this `Type` must be classified by the `Type`.
(A `Type` gives conditions that must be met by whatever it classifies, but when `isSufficient` is false, things may meet those conditions but still not be classified by the `Type`. For example, a Type `*Car*` that is not sufficient could require everything it classifies to have four wheels, but not all four wheeled things would classify as cars. However, if the `Type` `*Car*` were sufficient, it would classify all four-wheeled things.)
Returns:
the isSufficient value
Model:
derived="false"
 transient="false"
setIsSufficient
void setIsSufficient(boolean value)
Whether all things that meet the classification conditions of this `Type` must be classified by the `Type`.
(A `Type` gives conditions that must be met by whatever it classifies, but when `isSufficient` is false, things may meet those conditions but still not be classified by the `Type`. For example, a Type `*Car*` that is not sufficient could require everything it classifies to have four wheels, but not all four wheeled things would classify as cars. However, if the `Type` `*Car*` were sufficient, it would classify all four-wheeled things.)
Parameters:
`value` - the isSufficient value
Model:
derived="false"
 transient="false"
getOwnedConjugator
@CheckForNull[Conjugation](Conjugation.html) getOwnedConjugator()
A `Conjugation` owned by this `Type` for which the `Type` is the `originalType`.
Returns:
the ownedConjugator value
Model:
derived="true"
 transient="true"
 opposite=[`Conjugation.getOwningType()`](Conjugation.html#getOwningType())
 subsets=[`Element.getOwnedRelationship()`](Element.html#getOwnedRelationship())
isConjugated
boolean isConjugated()
Indicates whether this `Type` has an `ownedConjugator`.
Returns:
the isConjugated value
Model:
derived="true"
 transient="true"
getInheritedFeature
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> getInheritedFeature()
All the `memberFeatures` of the `inheritedMemberships` of this `Type` that are `FeatureMemberships`.
Returns:
the inheritedFeature value
Model:
derived="true"
 transient="true"
 oppositeRoleName="inheritingType"
 subsets=[`getFeature()`](#getFeature())
getMultiplicity
@CheckForNull[Multiplicity](Multiplicity.html) getMultiplicity()
An `ownedMember` of this `Type` that is a `Multiplicity`, which constraints the cardinality of the `Type`. If there is no such `ownedMember`, then the cardinality of this `Type` is constrained by all the `Multiplicity` constraints applicable to any direct supertypes.
Returns:
the multiplicity value
Model:
derived="true"
 transient="true"
 oppositeRoleName="typeWithMultiplicity"
 subsets=[`Namespace.getOwnedMember()`](Namespace.html#getOwnedMember())
getUnioningType
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> getUnioningType()
The interpretations of a `Type` with `unioningTypes` are asserted to be the same as those of all the `unioningTypes` together, which are the `Types` derived from the `unioningType` of the `ownedUnionings` of this `Type`. For example, a `Classifier` for people might be the union of `Classifiers` for all the sexes. Similarly, a feature for people's children might be the union of features dividing them in the same ways as people in general.
Returns:
the unioningType value
Model:
derived="true"
 transient="true"
 oppositeRoleName="unionedType"
getOwnedIntersecting
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Intersecting](Intersecting.html)> getOwnedIntersecting()
The `ownedRelationships` of this `Type` that are `Intersectings`, have the `Type` as their `typeIntersected`.
Returns:
the ownedIntersecting value
Model:
derived="true"
 transient="true"
 opposite=[`Intersecting.getTypeIntersected()`](Intersecting.html#getTypeIntersected())
 subsets=[`Element.getOwnedRelationship()`](Element.html#getOwnedRelationship())
getIntersectingType
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> getIntersectingType()
The interpretations of a `Type` with `intersectingTypes` are asserted to be those in common among the `intersectingTypes`, which are the `Types` derived from the `intersectingType` of the `ownedIntersectings` of this `Type`. For example, a `Classifier` might be an intersection of `Classifiers` for people of a particular sex and of a particular nationality. Similarly, a feature for people's children of a particular sex might be the intersection of a `Feature` for their children and a `Classifier` for people of that sex (because the interpretations of the children `Feature` that identify those of that sex are also interpretations of the Classifier for that sex).
Returns:
the intersectingType value
Model:
derived="true"
 transient="true"
 oppositeRoleName="intersectedType"
getOwnedUnioning
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Unioning](Unioning.html)> getOwnedUnioning()
The `ownedRelationships` of this `Type` that are `Unionings`, having the `Type` as their `typeUnioned`.
Returns:
the ownedUnioning value
Model:
derived="true"
 transient="true"
 opposite=[`Unioning.getTypeUnioned()`](Unioning.html#getTypeUnioned())
 subsets=[`Element.getOwnedRelationship()`](Element.html#getOwnedRelationship())
getOwnedDisjoining
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Disjoining](Disjoining.html)> getOwnedDisjoining()
The `ownedRelationships` of this `Type` that are `Disjoinings`, for which the `Type` is the `typeDisjoined` `Type`.
Returns:
the ownedDisjoining value
Model:
derived="true"
 transient="true"
 opposite=[`Disjoining.getOwningType()`](Disjoining.html#getOwningType())
 subsets=[`Element.getOwnedRelationship()`](Element.html#getOwnedRelationship())
getFeatureMembership
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureMembership](FeatureMembership.html)> getFeatureMembership()
The `FeatureMemberships` for `features` of this `Type`, which include all `ownedFeatureMemberships` and those `inheritedMemberships` that are `FeatureMemberships` (but does *not* include any `importedMemberships`).
Returns:
the featureMembership value
Model:
derived="true"
 transient="true"
 oppositeRoleName="type"
getDifferencingType
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> getDifferencingType()
The interpretations of a `Type` with `differencingTypes` are asserted to be those of the first of those `Types`, but not including those of the remaining `Types`. For example, a `Classifier` might be the difference of a `Classifier` for people and another for people of a particular nationality, leaving people who are not of that nationality. Similarly, a feature of people might be the difference between a feature for their children and a `Classifier` for people of a particular sex, identifying their children not of that sex (because the interpretations of the children `Feature` that identify those of that sex are also interpretations of the `Classifier` for that sex).
Returns:
the differencingType value
Model:
derived="true"
 transient="true"
 oppositeRoleName="differencedType"
getOwnedDifferencing
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Differencing](Differencing.html)> getOwnedDifferencing()
The `ownedRelationships` of this `Type` that are `Differencings`, having this `Type` as their `typeDifferenced`.
Returns:
the ownedDifferencing value
Model:
derived="true"
 transient="true"
 opposite=[`Differencing.getTypeDifferenced()`](Differencing.html#getTypeDifferenced())
 subsets=[`Element.getOwnedRelationship()`](Element.html#getOwnedRelationship())
getDirectedFeature
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> getDirectedFeature()
The `features` of this `Type` that have a non-null `direction`.
Returns:
the directedFeature value
Model:
derived="true"
 transient="true"
 oppositeRoleName="typeWithDirectedFeature"
 subsets=[`getFeature()`](#getFeature())
visibleMemberships
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> visibleMemberships([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excluded,
 boolean isRecursive,
 boolean includeAll)
The visible `Memberships` of a `Type` include `inheritedMemberships`.
 
 let visibleMemberships : OrderedSet(Membership) =
 self.oclAsType(Namespace).
 visibleMemberships(excluded, isRecursive, includeAll) in
 let visibleInheritedMemberships : OrderedSet(Membership) = 
 inheritedMemberships(excluded->including(self), Set{}, isRecursive)->
 select(includeAll or visibility = VisibilityKind::public) in
 visibleMemberships->union(visibleInheritedMemberships)
Specified by:
`[visibleMemberships](Namespace.html#visibleMemberships(java.util.List,boolean,boolean))` in interface `[Namespace](Namespace.html)`
inheritedMemberships
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> inheritedMemberships([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excludedNamespaces,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> excludedTypes,
 boolean excludeImplied)
Return the `Memberships` inheritable from supertypes of this `Type` with redefined `Features` removed. When computing inheritable `Memberships`, exclude `Imports` of `excludedNamespaces`, `Specializations` of `excludedTypes`, and, if `excludeImplied = true`, all implied `Specializations`.
 
 removeRedefinedFeatures(
 inheritableMemberships(excludedNamespaces, excludedTypes, excludeImplied))
inheritableMemberships
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> inheritableMemberships([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excludedNamespaces,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> excludedTypes,
 boolean excludeImplied)
Return all the non-`private` `Memberships` of all the supertypes of this `Type`, excluding any supertypes that are this `Type` or are in the given set of `excludedTypes`. If `excludeImplied = true`, then also transitively exclude any supertypes from implied `Specializations`.
 let excludingSelf : Set(Type) = excludedType->including(self) in
 supertypes(excludeImplied)->reject(t | excludingSelf->includes(t)).
 nonPrivateMemberships(excludedNamespaces, excludingSelf, excludeImplied)
nonPrivateMemberships
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> nonPrivateMemberships([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excludedNamespaces,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> excludedTypes,
 boolean excludeImplied)
Return the `public`, `protected` and inherited `Memberships` of this `Type`. When computing imported `Memberships`, exclude the given set of `excludedNamespaces`. When computing inherited `Memberships`, exclude `Types` in the given set of `excludedTypes`. If `excludeImplied = true`, then also exclude any supertypes from implied `Specializations`.
 let publicMemberships : OrderedSet(Membership) = 
 membershipsOfVisibility(VisibilityKind::public, excludedNamespaces) in
 let protectedMemberships : OrderedSet(Membership) = 
 membershipsOfVisibility(VisibilityKind::protected, excludedNamespaces) in
 let inheritedMemberships : OrderedSet(Membership) =
 inheritedMemberships(excludedNamespaces, excludedTypes, excludeImplied) in
 publicMemberships->
 union(protectedMemberships)->
 union(inheritedMemberships)
removeRedefinedFeatures
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> removeRedefinedFeatures([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> memberships)
Return a subset of `memberships`, removing those `Memberships` whose `memberElements` are `Features` and for which either of the following two conditions holds:
The `memberElement` of the `Membership` is included in redefined `Features` of another `Membership` in `memberships`.
One of the redefined `Features` of the `Membership` is a directly `redefinedFeature` of an `ownedFeature` of this `Type`.
For this purpose, the redefined `Features` of a `Membership` whose `memberElement` is a `Feature` includes the `memberElement` and all `Features` directly or indirectly redefined by the `memberElement`.
 let reducedMemberships : Sequence(Membership) =
 memberships->reject(mem1 |
 memberships->excluding(mem1)->
 exists(mem2 | allRedefinedFeaturesOf(mem2)->
 includes(mem1.memberElement))) in
 let redefinedFeatures : Set(Feature) = 
 ownedFeature.redefinition.redefinedFeature->asSet() in
 reducedMemberships->reject(mem | allRedefinedFeaturesOf(mem)->
 exists(feature | redefinedFeatures->includes(feature)))
allRedefinedFeaturesOf
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> allRedefinedFeaturesOf([Membership](Membership.html) membership)
If the `memberElement` of the given `membership` is a `Feature`, then return all `Features` directly or indirectly redefined by the `memberElement`.
 if not membership.memberElement.oclIsType(Feature) then Set{} 
 else membership.memberElement.oclAsType(Feature).allRedefinedFeatures()
 endif
directionOf
[FeatureDirectionKind](FeatureDirectionKind.html) directionOf([Feature](Feature.html) feature)
If the given `feature` is a `feature` of this `Type`, then return its direction relative to this `Type`, taking conjugation into account.
 
 directionOfExcluding(f, Set{})
directionOfExcluding
[FeatureDirectionKind](FeatureDirectionKind.html) directionOfExcluding([Feature](Feature.html) feature,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> excluded)
Return the direction of the given `feature` relative to this `Type`, excluding a given set of `Types` from the search of supertypes of this `Type`.
 let excludedSelf : Set(Type) = excluded->including(self) in 
 if feature.owningType = self then feature.direction
 else
 let directions : Sequence(FeatureDirectionKind) =
 supertypes(false)->excluding(excludedSelf).
 directionOfExcluding(feature, excludedSelf)->
 select(d | d <> null) in
 if directions->isEmpty() then null
 else
 let direction : FeatureDirectionKind = directions->first() in
 if not isConjugated then direction
 else if direction = FeatureDirectionKind::_'in' then FeatureDirectionKind::out
 else if direction = FeatureDirectionKind::out then FeatureDirectionKind::_'in'
 else direction
 endif endif endif endif
 endif
supertypes
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> supertypes(boolean excludeImplied)
If this `Type` is conjugated, then return just the `originalType` of the `Conjugation`. Otherwise, return the `general` `Types` from all `ownedSpecializations` of this type, if `excludeImplied = false`, or all non-implied `ownedSpecializations`, if `excludeImplied = true`.
 if isConjugated then Sequence{conjugator.originalType}
 else if not excludeImplied then ownedSpecialization.general
 else ownedSpecialization->reject(isImplied).general
 endif
 endif
allSupertypes
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> allSupertypes()
Return this `Type` and all `Types` that are directly or transitively supertypes of this `Type` (as determined by the `supertypes` operation with `excludeImplied = false`).
 
 OrderedSet{self}->closure(supertypes(false))
specializes
boolean specializes([Type](Type.html) supertype)
Check whether this `Type` is a direct or indirect specialization of the given `supertype.`
 if isConjugated then 
 ownedConjugator.originalType.specializes(supertype)
 else
 allSupertypes()->includes(supertype)
 endif
specializesFromLibrary
boolean specializesFromLibrary([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) libraryTypeName)
Check whether this `Type` is a direct or indirect specialization of the named library `Type`. `libraryTypeName` must conform to the syntax of a KerML qualified name and must resolve to a `Type` in global scope.
 
 let mem : Membership = resolveGlobal(libraryTypeName) in
 mem <> null and mem.memberElement.oclIsKindOf(Type) and
 specializes(mem.memberElement.oclAsType(Type))
isCompatibleWith
boolean isCompatibleWith([Type](Type.html) otherType)
By default, this `Type` is compatible with an `otherType` if it directly or indirectly specializes the `otherType`.
 specializes(otherType)
multiplicities
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Multiplicity](Multiplicity.html)> multiplicities()
Return the owned or inherited `Multiplicities` for this `Typeinvalid input: '<'./code>.`
 if multiplicity <> null then OrderedSet{multiplicity}
 else 
 ownedSpecialization.general->closure(t |
 if t.multiplicity <> null then OrderedSet{}
 else ownedSpecialization.general
 )->select(multiplicity <> null).multiplicity->asOrderedSet()
 endif

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Type">Interface Type</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../sysml/model/sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationDefinition</a></code>, <code><a href="../../../sysml/model/sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a></code>, <code><a href="../../../sysml/model/sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssertConstraintUsage</a></code>, <code><a href="../../../sysml/model/sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a></code>, <code><a href="Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a></code>, <code><a href="AssociationStructure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AssociationStructure</a></code>, <code><a href="../../../sysml/model/sysml/AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeDefinition</a></code>, <code><a href="../../../sysml/model/sysml/AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a></code>, <code><a href="Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Behavior</a></code>, <code><a href="BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BindingConnector</a></code>, <code><a href="../../../sysml/model/sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">BindingConnectorAsUsage</a></code>, <code><a href="BooleanExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BooleanExpression</a></code>, <code><a href="../../../sysml/model/sysml/CalculationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationDefinition</a></code>, <code><a href="../../../sysml/model/sysml/CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a></code>, <code><a href="../../../sysml/model/sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a></code>, <code><a href="Class.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Class</a></code>, <code><a href="Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a></code>, <code><a href="CollectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CollectExpression</a></code>, <code><a href="../../../sysml/model/sysml/ConcernDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a></code>, <code><a href="../../../sysml/model/sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionUsage</a></code>, <code><a href="Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a></code>, <code><a href="../../../sysml/model/sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a></code>, <code><a href="../../../sysml/model/sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a></code>, <code><a href="ConstructorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ConstructorExpression</a></code>, <code><a href="../../../sysml/model/sysml/ControlNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ControlNode</a></code>, <code><a href="DataType.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">DataType</a></code>, <code><a href="../../../sysml/model/sysml/DecisionNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">DecisionNode</a></code>, <code><a href="../../../sysml/model/sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a></code>, <code><a href="../../../sysml/model/sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationDefinition</a></code>, <code><a href="../../../sysml/model/sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a></code>, <code><a href="../../../sysml/model/sysml/EventOccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EventOccurrenceUsage</a></code>, <code><a href="../../../sysml/model/sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ExhibitStateUsage</a></code>, <code><a href="Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code>, <code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code>, <code><a href="FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a></code>, <code><a href="FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a></code>, <code><a href="Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a></code>, <code><a href="../../../sysml/model/sysml/FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowDefinition</a></code>, <code><a href="FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FlowEnd</a></code>, <code><a href="../../../sysml/model/sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a></code>, <code><a href="../../../sysml/model/sysml/ForkNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForkNode</a></code>, <code><a href="../../../sysml/model/sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a></code>, <code><a href="Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a></code>, <code><a href="../../../sysml/model/sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IncludeUseCaseUsage</a></code>, <code><a href="IndexExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">IndexExpression</a></code>, <code><a href="InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InstantiationExpression</a></code>, <code><a href="Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Interaction</a></code>, <code><a href="../../../sysml/model/sysml/InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceDefinition</a></code>, <code><a href="../../../sysml/model/sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a></code>, <code><a href="Invariant.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Invariant</a></code>, <code><a href="InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></code>, <code><a href="../../../sysml/model/sysml/ItemDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a></code>, <code><a href="../../../sysml/model/sysml/JoinNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">JoinNode</a></code>, <code><a href="LiteralBoolean.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralBoolean</a></code>, <code><a href="LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralExpression</a></code>, <code><a href="LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInfinity</a></code>, <code><a href="LiteralInteger.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInteger</a></code>, <code><a href="LiteralRational.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralRational</a></code>, <code><a href="LiteralString.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralString</a></code>, <code><a href="../../../sysml/model/sysml/LoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">LoopActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/MergeNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MergeNode</a></code>, <code><a href="Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a></code>, <code><a href="MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a></code>, <code><a href="../../../sysml/model/sysml/MetadataDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataDefinition</a></code>, <code><a href="MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></code>, <code><a href="../../../sysml/model/sysml/MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a></code>, <code><a href="Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a></code>, <code><a href="MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a></code>, <code><a href="NullExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NullExpression</a></code>, <code><a href="../../../sysml/model/sysml/OccurrenceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceDefinition</a></code>, <code><a href="../../../sysml/model/sysml/OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a></code>, <code><a href="OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></code>, <code><a href="../../../sysml/model/sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartDefinition</a></code>, <code><a href="../../../sysml/model/sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a></code>, <code><a href="PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">PayloadFeature</a></code>, <code><a href="../../../sysml/model/sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></code>, <code><a href="../../../sysml/model/sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a></code>, <code><a href="Predicate.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Predicate</a></code>, <code><a href="../../../sysml/model/sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a></code>, <code><a href="../../../sysml/model/sysml/RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingDefinition</a></code>, <code><a href="../../../sysml/model/sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a></code>, <code><a href="../../../sysml/model/sysml/RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementDefinition</a></code>, <code><a href="../../../sysml/model/sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></code>, <code><a href="../../../sysml/model/sysml/SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SatisfyRequirementUsage</a></code>, <code><a href="SelectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SelectExpression</a></code>, <code><a href="../../../sysml/model/sysml/SendActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SendActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateDefinition</a></code>, <code><a href="../../../sysml/model/sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a></code>, <code><a href="Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></code>, <code><a href="Structure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Structure</a></code>, <code><a href="Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a></code>, <code><a href="../../../sysml/model/sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionAsUsage</a></code>, <code><a href="SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SuccessionFlow</a></code>, <code><a href="../../../sysml/model/sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a></code>, <code><a href="../../../sysml/model/sysml/TerminateActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TerminateActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a></code>, <code><a href="../../../sysml/model/sysml/TriggerInvocationExpression.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TriggerInvocationExpression</a></code>, <code><a href="../../../sysml/model/sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></code>, <code><a href="../../../sysml/model/sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a></code>, <code><a href="../../../sysml/model/sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a></code>, <code><a href="../../../sysml/model/sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Type</span><span class="extends-implements">
extends <a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></span></div>
<div class="block"><p>A <code>Type</code> is a <code>Namespace</code> that is the most general kind of <code>Element</code> supporting the semantics of classification. A <code>Type</code> may be a <code>Classifier</code> or a <code>Feature</code>, defining conditions on what is classified by the <code>Type</code> (see also the description of <code>isSufficient</code>).</p>
 
 ownedSpecialization = ownedRelationship-&gt;selectByKind(Specialization)-&gt;
     select(s | s.special = self)
     
 multiplicity = 
     let ownedMultiplicities: Sequence(Multiplicity) =
         ownedMember-&gt;selectByKind(Multiplicity) in
     if ownedMultiplicities-&gt;isEmpty() then null
     else ownedMultiplicities-&gt;first()
     endif
 ownedFeatureMembership = ownedRelationship-&gt;selectByKind(FeatureMembership)
 ownedConjugator =
     let ownedConjugators: Sequence(Conjugator) = 
         ownedRelationship-&gt;selectByKind(Conjugation) in
     if ownedConjugators-&gt;isEmpty() then null 
     else ownedConjugators-&gt;at(1) endif
 output = feature-&gt;select(f | 
     let direction: FeatureDirectionKind = directionOf(f) in
     direction = FeatureDirectionKind::out or
     direction = FeatureDirectionKind::inout)
 input = feature-&gt;select(f | 
     let direction: FeatureDirectionKind = directionOf(f) in
     direction = FeatureDirectionKind::_'in' or
     direction = FeatureDirectionKind::inout)
 inheritedMembership = inheritedMemberships(Set{}, Set{}, false)
 specializesFromLibrary('Base::Anything')
 directedFeature = feature-&gt;select(f | directionOf(f) &lt;&gt; null)
 feature = featureMembership.ownedMemberFeature
 featureMembership = ownedFeatureMembership-&gt;union(
     inheritedMembership-&gt;selectByKind(FeatureMembership))
 ownedFeature = ownedFeatureMembership.ownedMemberFeature
 differencingType = ownedDifferencing.differencingType
 intersectingType-&gt;excludes(self)
 differencingType-&gt;excludes(self)
 unioningType = ownedUnioning.unioningType
 unioningType-&gt;excludes(self)
 intersectingType = ownedIntersecting.intersectingType
 ownedRelationship-&gt;selectByKind(Conjugation)-&gt;size() &lt;= 1
 ownedMember-&gt;selectByKind(Multiplicity)-&gt;size() &lt;= 1
 endFeature = feature-&gt;select(isEnd)
 ownedDisjoining =
     ownedRelationship-&gt;selectByKind(Disjoining)
 ownedUnioning =
     ownedRelationship-&gt;selectByKind(Unioning)
 ownedRelationship-&gt;selectByKind(Intersecting)
 ownedDifferencing =
     ownedRelationship-&gt;selectByKind(Differencing)
 ownedEndFeature = ownedFeature-&gt;select(isEnd)
 inheritedFeature = inheritedMemberships-&gt;
     selectByKind(FeatureMembership).memberFeature
 ownedUnioning-&gt;size() &lt;&gt; 1
 ownedIntersecting-&gt;size() &lt;&gt; 1
 ownedDifferencing-&gt;size() &lt;&gt; 1</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">allRedefinedFeaturesOf</a><wbr/>(<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> membership)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If the <code>memberElement</code> of the given <code>membership</code> is a <code>Feature</code>, then return all <code>Features</code> directly or indirectly redefined by the <code>memberElement</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#allSupertypes()">allSupertypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return this <code>Type</code> and all <code>Types</code> that are directly or transitively supertypes of this <code>Type</code> (as determined by the <code>supertypes</code> operation with <code>excludeImplied = false</code>).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">directionOf</a><wbr/>(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If the given <code>feature</code> is a <code>feature</code> of this <code>Type</code>, then return its direction relative to this <code>Type</code>, taking conjugation into account.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">directionOfExcluding</a><wbr/>(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; excluded)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the direction of the given <code>feature</code> relative to this <code>Type</code>, excluding a given set of <code>Types</code> from the search of supertypes of this <code>Type</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDifferencingType()">getDifferencingType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The interpretations of a <code>Type</code> with <code>differencingTypes</code> are asserted to be those of the first of those <code>Types</code>, but not including those of the remaining <code>Types</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDirectedFeature()">getDirectedFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>features</code> of this <code>Type</code> that have a non-null <code>direction</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEndFeature()">getEndFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">All <code>features</code> of this <code>Type</code> with <code>isEnd = true</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFeature()">getFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedMemberFeatures</code> of the <code>featureMemberships</code> of this <code>Type</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFeatureMembership()">getFeatureMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>FeatureMemberships</code> for <code>features</code> of this <code>Type</code>, which include all <code>ownedFeatureMemberships</code> and those <code>inheritedMemberships</code> that are <code>FeatureMemberships</code> (but does <em>not</em> include any <code>importedMemberships</code>).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInheritedFeature()">getInheritedFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">All the <code>memberFeatures</code> of the <code>inheritedMemberships</code> of this <code>Type</code> that are <code>FeatureMemberships</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInheritedMembership()">getInheritedMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">All <code>Memberships</code> inherited by this <code>Type</code> via <code>Specialization</code> or <code>Conjugation</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInput()">getInput</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">All <code>features</code> related to this <code>Type</code> by <code>FeatureMemberships</code> that have <code>direction</code> <code>in</code> or <code>inout</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getIntersectingType()">getIntersectingType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The interpretations of a <code>Type</code> with <code>intersectingTypes</code> are asserted to be those in common among the <code>intersectingTypes</code>, which are the <code>Types</code> derived from the <code>intersectingType</code> of the <code>ownedIntersectings</code> of this <code>Type</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMultiplicity()">getMultiplicity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">An <code>ownedMember</code> of this <code>Type</code> that is a <code>Multiplicity</code>, which constraints the cardinality of the <code>Type</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOutput()">getOutput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">All <code>features</code> related to this <code>Type</code> by <code>FeatureMemberships</code> that have <code>direction</code> <code>out</code> or <code>inout</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Conjugation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Conjugation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedConjugator()">getOwnedConjugator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">A <code>Conjugation</code> owned by this <code>Type</code> for which the <code>Type</code> is the <code>originalType</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Differencing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Differencing</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedDifferencing()">getOwnedDifferencing</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedRelationships</code> of this <code>Type</code> that are <code>Differencings</code>, having this <code>Type</code> as their <code>typeDifferenced</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Disjoining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Disjoining</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedDisjoining()">getOwnedDisjoining</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedRelationships</code> of this <code>Type</code> that are <code>Disjoinings</code>, for which the <code>Type</code> is the <code>typeDisjoined</code> <code>Type</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedEndFeature()">getOwnedEndFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">All <code>endFeatures</code> of this <code>Type</code> that are <code>ownedFeatures</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedFeature()">getOwnedFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedMemberFeatures</code> of the <code>ownedFeatureMemberships</code> of this <code>Type</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedFeatureMembership()">getOwnedFeatureMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedMemberships</code> of this <code>Type</code> that are <code>FeatureMemberships</code>, for which the <code>Type</code> is the <code>owningType</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Intersecting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Intersecting</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedIntersecting()">getOwnedIntersecting</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedRelationships</code> of this <code>Type</code> that are <code>Intersectings</code>, have the <code>Type</code> as their <code>typeIntersected</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedSpecialization()">getOwnedSpecialization</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedRelationships</code> of this <code>Type</code> that are <code>Specializations</code>, for which the <code>Type</code> is the <code>specific</code> <code>Type</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Unioning.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Unioning</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedUnioning()">getOwnedUnioning</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedRelationships</code> of this <code>Type</code> that are <code>Unionings</code>, having the <code>Type</code> as their <code>typeUnioned</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUnioningType()">getUnioningType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The interpretations of a <code>Type</code> with <code>unioningTypes</code> are asserted to be the same as those of all the <code>unioningTypes</code> together, which are the <code>Types</code> derived from the <code>unioningType</code> of the <code>ownedUnionings</code> of this <code>Type</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#inheritableMemberships(java.util.List,java.util.List,boolean)">inheritableMemberships</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excludedNamespaces,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; excludedTypes,
 boolean excludeImplied)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return all the non-<code>private</code> <code>Memberships</code> of all the supertypes of this <code>Type</code>, excluding any supertypes that are this <code>Type</code> or are in the given set of <code>excludedTypes</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#inheritedMemberships(java.util.List,java.util.List,boolean)">inheritedMemberships</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excludedNamespaces,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; excludedTypes,
 boolean excludeImplied)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the <code>Memberships</code> inheritable from supertypes of this <code>Type</code> with redefined <code>Features</code> removed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isAbstract()">isAbstract</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates whether instances of this <code>Type</code> must also be instances of at least one of its specialized <code>Types</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isCompatibleWith</a><wbr/>(<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> otherType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">By default, this <code>Type</code> is compatible with an <code>otherType</code> if it directly or indirectly specializes the <code>otherType</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isConjugated()">isConjugated</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates whether this <code>Type</code> has an <code>ownedConjugator</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSufficient()">isSufficient</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether all things that meet the classification conditions of this <code>Type</code> must be classified by the <code>Type</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#multiplicities()">multiplicities</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the owned or inherited <code>Multiplicities</code> for this <code>Type<span class="invalid-tag">invalid input: '&lt;'</span>./code&gt;.</code></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#nonPrivateMemberships(java.util.List,java.util.List,boolean)">nonPrivateMemberships</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excludedNamespaces,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; excludedTypes,
 boolean excludeImplied)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the <code>public</code>, <code>protected</code> and inherited <code>Memberships</code> of this <code>Type</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeRedefinedFeatures(java.util.List)">removeRedefinedFeatures</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt; memberships)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return a subset of <code>memberships</code>, removing those <code>Memberships</code> whose <code>memberElements</code> are <code>Features</code> and for which either of the following two conditions holds:</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsAbstract(boolean)">setIsAbstract</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates whether instances of this <code>Type</code> must also be instances of at least one of its specialized <code>Types</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsSufficient(boolean)">setIsSufficient</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether all things that meet the classification conditions of this <code>Type</code> must be classified by the <code>Type</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">specializes</a><wbr/>(<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> supertype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check whether this <code>Type</code> is a direct or indirect specialization of the given <code>supertype<code>.</code></code></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#specializesFromLibrary(java.lang.String)">specializesFromLibrary</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> libraryTypeName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check whether this <code>Type</code> is a direct or indirect specialization of the named library <code>Type</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#supertypes(boolean)">supertypes</a><wbr/>(boolean excludeImplied)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If this <code>Type</code> is conjugated, then return just the <code>originalType</code> of the <code>Conjugation</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visibleMemberships(java.util.List,boolean,boolean)">visibleMemberships</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excluded,
 boolean isRecursive,
 boolean includeAll)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The visible <code>Memberships</code> of a <code>Type</code> include <code>inheritedMemberships</code>.</div>
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
<section class="detail" id="getOwnedSpecialization()">
<h3>getOwnedSpecialization</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a>&gt;</span> <span class="element-name">getOwnedSpecialization</span>()</div>
<div class="block"><p>The <code>ownedRelationships</code> of this <code>Type</code> that are <code>Specializations</code>, for which the <code>Type</code> is the <code>specific</code> <code>Type</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedSpecialization value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Specialization.html#getOwningType()"><code>Specialization.getOwningType()</code></a>
        subsets=<a href="Element.html#getOwnedRelationship()"><code>Element.getOwnedRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedFeatureMembership()">
<h3>getOwnedFeatureMembership</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a>&gt;</span> <span class="element-name">getOwnedFeatureMembership</span>()</div>
<div class="block"><p>The <code>ownedMemberships</code> of this <code>Type</code> that are <code>FeatureMemberships</code>, for which the <code>Type</code> is the <code>owningType</code>. Each such <code>FeatureMembership</code> identifies an <code>ownedFeature</code> of the <code>Type</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedFeatureMembership value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="FeatureMembership.html#getOwningType()"><code>FeatureMembership.getOwningType()</code></a>
        subsets=<a href="Namespace.html#getOwnedMembership()"><code>Namespace.getOwnedMembership()</code></a>, <a href="#getFeatureMembership()"><code>getFeatureMembership()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeature()">
<h3>getFeature</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getFeature</span>()</div>
<div class="block"><p>The <code>ownedMemberFeatures</code> of the <code>featureMemberships</code> of this <code>Type</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the feature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="typeWithFeature"
        subsets=<a href="Namespace.html#getMember()"><code>Namespace.getMember()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedFeature()">
<h3>getOwnedFeature</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getOwnedFeature</span>()</div>
<div class="block"><p>The <code>ownedMemberFeatures</code> of the <code>ownedFeatureMemberships</code> of this <code>Type</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Feature.html#getOwningType()"><code>Feature.getOwningType()</code></a>
        subsets=<a href="Namespace.html#getOwnedMember()"><code>Namespace.getOwnedMember()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInput()">
<h3>getInput</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getInput</span>()</div>
<div class="block"><p>All <code>features</code> related to this <code>Type</code> by <code>FeatureMemberships</code> that have <code>direction</code> <code>in</code> or <code>inout</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the input value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="typeWithInput"
        subsets=<a href="#getDirectedFeature()"><code>getDirectedFeature()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOutput()">
<h3>getOutput</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getOutput</span>()</div>
<div class="block"><p>All <code>features</code> related to this <code>Type</code> by <code>FeatureMemberships</code> that have <code>direction</code> <code>out</code> or <code>inout</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the output value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="typeWithOutput"
        subsets=<a href="#getDirectedFeature()"><code>getDirectedFeature()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAbstract()">
<h3>isAbstract</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isAbstract</span>()</div>
<div class="block"><p>Indicates whether instances of this <code>Type</code> must also be instances of at least one of its specialized <code>Types</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isAbstract value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsAbstract(boolean)">
<h3>setIsAbstract</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsAbstract</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Indicates whether instances of this <code>Type</code> must also be instances of at least one of its specialized <code>Types</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isAbstract value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInheritedMembership()">
<h3>getInheritedMembership</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</span> <span class="element-name">getInheritedMembership</span>()</div>
<div class="block"><p>All <code>Memberships</code> inherited by this <code>Type</code> via <code>Specialization</code> or <code>Conjugation</code>. These are included in the derived union for the <code>memberships</code> of the <code>Type</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the inheritedMembership value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="inheritingType"
        subsets=<a href="Namespace.html#getMembership()"><code>Namespace.getMembership()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEndFeature()">
<h3>getEndFeature</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getEndFeature</span>()</div>
<div class="block"><p>All <code>features</code> of this <code>Type</code> with <code>isEnd = true</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the endFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="typeWithEndFeature"
        subsets=<a href="#getFeature()"><code>getFeature()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedEndFeature()">
<h3>getOwnedEndFeature</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getOwnedEndFeature</span>()</div>
<div class="block"><p>All <code>endFeatures</code> of this <code>Type</code> that are <code>ownedFeatures</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedEndFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Feature.html#getEndOwningType()"><code>Feature.getEndOwningType()</code></a>
        subsets=<a href="#getEndFeature()"><code>getEndFeature()</code></a>, <a href="#getOwnedFeature()"><code>getOwnedFeature()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSufficient()">
<h3>isSufficient</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isSufficient</span>()</div>
<div class="block"><p>Whether all things that meet the classification conditions of this <code>Type</code> must be classified by the <code>Type</code>.</p>
<p>(A <code>Type</code> gives conditions that must be met by whatever it classifies, but when <code>isSufficient</code> is false, things may meet those conditions but still not be classified by the <code>Type</code>. For example, a Type <code><em>Car</em></code> that is not sufficient could require everything it classifies to have four wheels, but not all four wheeled things would classify as cars. However, if the <code>Type</code> <code><em>Car</em></code> were sufficient, it would classify all four-wheeled things.)</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isSufficient value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsSufficient(boolean)">
<h3>setIsSufficient</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsSufficient</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether all things that meet the classification conditions of this <code>Type</code> must be classified by the <code>Type</code>.</p>
<p>(A <code>Type</code> gives conditions that must be met by whatever it classifies, but when <code>isSufficient</code> is false, things may meet those conditions but still not be classified by the <code>Type</code>. For example, a Type <code><em>Car</em></code> that is not sufficient could require everything it classifies to have four wheels, but not all four wheeled things would classify as cars. However, if the <code>Type</code> <code><em>Car</em></code> were sufficient, it would classify all four-wheeled things.)</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isSufficient value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedConjugator()">
<h3>getOwnedConjugator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Conjugation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Conjugation</a></span> <span class="element-name">getOwnedConjugator</span>()</div>
<div class="block"><p>A <code>Conjugation</code> owned by this <code>Type</code> for which the <code>Type</code> is the <code>originalType</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedConjugator value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Conjugation.html#getOwningType()"><code>Conjugation.getOwningType()</code></a>
        subsets=<a href="Element.html#getOwnedRelationship()"><code>Element.getOwnedRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConjugated()">
<h3>isConjugated</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isConjugated</span>()</div>
<div class="block"><p>Indicates whether this <code>Type</code> has an <code>ownedConjugator</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isConjugated value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInheritedFeature()">
<h3>getInheritedFeature</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getInheritedFeature</span>()</div>
<div class="block"><p>All the <code>memberFeatures</code> of the <code>inheritedMemberships</code> of this <code>Type</code> that are <code>FeatureMemberships</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the inheritedFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="inheritingType"
        subsets=<a href="#getFeature()"><code>getFeature()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMultiplicity()">
<h3>getMultiplicity</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a></span> <span class="element-name">getMultiplicity</span>()</div>
<div class="block"><p>An <code>ownedMember</code> of this <code>Type</code> that is a <code>Multiplicity</code>, which constraints the cardinality of the <code>Type</code>. If there is no such <code>ownedMember</code>, then the cardinality of this <code>Type</code> is constrained by all the <code>Multiplicity</code> constraints applicable to any direct supertypes.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the multiplicity value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="typeWithMultiplicity"
        subsets=<a href="Namespace.html#getOwnedMember()"><code>Namespace.getOwnedMember()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUnioningType()">
<h3>getUnioningType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">getUnioningType</span>()</div>
<div class="block"><p>The interpretations of a <code>Type</code> with <code>unioningTypes</code> are asserted to be the same as those of all the <code>unioningTypes</code> together, which are the <code>Types</code> derived from the <code>unioningType</code> of the <code>ownedUnionings</code> of this <code>Type</code>. For example, a <code>Classifier</code> for people might be the union of <code>Classifiers</code> for all the sexes. Similarly, a feature for people's children might be the union of features dividing them in the same ways as people in general.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the unioningType value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="unionedType"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedIntersecting()">
<h3>getOwnedIntersecting</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Intersecting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Intersecting</a>&gt;</span> <span class="element-name">getOwnedIntersecting</span>()</div>
<div class="block"><p>The <code>ownedRelationships</code> of this <code>Type</code> that are <code>Intersectings</code>, have the <code>Type</code> as their <code>typeIntersected</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedIntersecting value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Intersecting.html#getTypeIntersected()"><code>Intersecting.getTypeIntersected()</code></a>
        subsets=<a href="Element.html#getOwnedRelationship()"><code>Element.getOwnedRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIntersectingType()">
<h3>getIntersectingType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">getIntersectingType</span>()</div>
<div class="block"><p>The interpretations of a <code>Type</code> with <code>intersectingTypes</code> are asserted to be those in common among the <code>intersectingTypes</code>, which are the <code>Types</code> derived from the <code>intersectingType</code> of the <code>ownedIntersectings</code> of this <code>Type</code>. For example, a <code>Classifier</code> might be an intersection of <code>Classifiers</code> for people of a particular sex and of a particular nationality. Similarly, a feature for people's children of a particular sex might be the intersection of a <code>Feature</code> for their children and a <code>Classifier</code> for people of that sex (because the interpretations of the children <code>Feature</code> that identify those of that sex are also interpretations of the Classifier for that sex).</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the intersectingType value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="intersectedType"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedUnioning()">
<h3>getOwnedUnioning</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Unioning.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Unioning</a>&gt;</span> <span class="element-name">getOwnedUnioning</span>()</div>
<div class="block"><p>The <code>ownedRelationships</code> of this <code>Type</code> that are <code>Unionings</code>, having the <code>Type</code> as their <code>typeUnioned</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedUnioning value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Unioning.html#getTypeUnioned()"><code>Unioning.getTypeUnioned()</code></a>
        subsets=<a href="Element.html#getOwnedRelationship()"><code>Element.getOwnedRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedDisjoining()">
<h3>getOwnedDisjoining</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Disjoining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Disjoining</a>&gt;</span> <span class="element-name">getOwnedDisjoining</span>()</div>
<div class="block"><p>The <code>ownedRelationships</code> of this <code>Type</code> that are <code>Disjoinings</code>, for which the <code>Type</code> is the <code>typeDisjoined</code> <code>Type</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedDisjoining value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Disjoining.html#getOwningType()"><code>Disjoining.getOwningType()</code></a>
        subsets=<a href="Element.html#getOwnedRelationship()"><code>Element.getOwnedRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeatureMembership()">
<h3>getFeatureMembership</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a>&gt;</span> <span class="element-name">getFeatureMembership</span>()</div>
<div class="block"><p>The <code>FeatureMemberships</code> for <code>features</code> of this <code>Type</code>, which include all <code>ownedFeatureMemberships</code> and those <code>inheritedMemberships</code> that are <code>FeatureMemberships</code> (but does <em>not</em> include any <code>importedMemberships</code>).</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the featureMembership value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="type"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDifferencingType()">
<h3>getDifferencingType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">getDifferencingType</span>()</div>
<div class="block"><p>The interpretations of a <code>Type</code> with <code>differencingTypes</code> are asserted to be those of the first of those <code>Types</code>, but not including those of the remaining <code>Types</code>. For example, a <code>Classifier</code> might be the difference of a <code>Classifier</code> for people and another for people of a particular nationality, leaving people who are not of that nationality. Similarly, a feature of people might be the difference between a feature for their children and a <code>Classifier</code> for people of a particular sex, identifying their children not of that sex (because the interpretations of the children <code>Feature</code> that identify those of that sex are also interpretations of the <code>Classifier</code> for that sex).</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the differencingType value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="differencedType"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedDifferencing()">
<h3>getOwnedDifferencing</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Differencing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Differencing</a>&gt;</span> <span class="element-name">getOwnedDifferencing</span>()</div>
<div class="block"><p>The <code>ownedRelationships</code> of this <code>Type</code> that are <code>Differencings</code>, having this <code>Type</code> as their <code>typeDifferenced</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedDifferencing value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Differencing.html#getTypeDifferenced()"><code>Differencing.getTypeDifferenced()</code></a>
        subsets=<a href="Element.html#getOwnedRelationship()"><code>Element.getOwnedRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirectedFeature()">
<h3>getDirectedFeature</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getDirectedFeature</span>()</div>
<div class="block"><p>The <code>features</code> of this <code>Type</code> that have a non-null <code>direction</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the directedFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="typeWithDirectedFeature"
        subsets=<a href="#getFeature()"><code>getFeature()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visibleMemberships(java.util.List,boolean,boolean)">
<h3>visibleMemberships</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</span> <span class="element-name">visibleMemberships</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excluded,
 boolean isRecursive,
 boolean includeAll)</span></div>
<div class="block"><p>The visible <code>Memberships</code> of a <code>Type</code> include <code>inheritedMemberships</code>.</p>
 
 let visibleMemberships : OrderedSet(Membership) =
     self.oclAsType(Namespace).
         visibleMemberships(excluded, isRecursive, includeAll) in
 let visibleInheritedMemberships : OrderedSet(Membership) = 
     inheritedMemberships(excluded-&gt;including(self), Set{}, isRecursive)-&gt;
         select(includeAll or visibility = VisibilityKind::public) in
 visibleMemberships-&gt;union(visibleInheritedMemberships)</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Namespace.html#visibleMemberships(java.util.List,boolean,boolean)">visibleMemberships</a></code> in interface <code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="inheritedMemberships(java.util.List,java.util.List,boolean)">
<h3>inheritedMemberships</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</span> <span class="element-name">inheritedMemberships</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excludedNamespaces,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; excludedTypes,
 boolean excludeImplied)</span></div>
<div class="block"><p>Return the <code>Memberships</code> inheritable from supertypes of this <code>Type</code> with redefined <code>Features</code> removed. When computing inheritable <code>Memberships</code>, exclude <code>Imports</code> of <code>excludedNamespaces</code>, <code>Specializations</code> of <code>excludedTypes</code>, and, if <code>excludeImplied = true</code>, all implied <code>Specializations</code>.</p>
 
 removeRedefinedFeatures(
     inheritableMemberships(excludedNamespaces, excludedTypes, excludeImplied))</div>
</section>
</li>
<li>
<section class="detail" id="inheritableMemberships(java.util.List,java.util.List,boolean)">
<h3>inheritableMemberships</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</span> <span class="element-name">inheritableMemberships</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excludedNamespaces,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; excludedTypes,
 boolean excludeImplied)</span></div>
<div class="block"><p>Return all the non-<code>private</code> <code>Memberships</code> of all the supertypes of this <code>Type</code>, excluding any supertypes that are this <code>Type</code> or are in the given set of <code>excludedTypes</code>. If <code>excludeImplied = true</code>, then also transitively exclude any supertypes from implied <code>Specializations</code>.</p>
 let excludingSelf : Set(Type) = excludedType-&gt;including(self) in
 supertypes(excludeImplied)-&gt;reject(t | excludingSelf-&gt;includes(t)).
     nonPrivateMemberships(excludedNamespaces, excludingSelf, excludeImplied)</div>
</section>
</li>
<li>
<section class="detail" id="nonPrivateMemberships(java.util.List,java.util.List,boolean)">
<h3>nonPrivateMemberships</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</span> <span class="element-name">nonPrivateMemberships</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excludedNamespaces,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; excludedTypes,
 boolean excludeImplied)</span></div>
<div class="block"><p>Return the <code>public</code>, <code>protected</code> and inherited <code>Memberships</code> of this <code>Type</code>. When computing imported <code>Memberships</code>, exclude the given set of <code>excludedNamespaces</code>. When computing inherited <code>Memberships</code>, exclude <code>Types</code> in the given set of <code>excludedTypes</code>. If <code>excludeImplied = true</code>, then also exclude any supertypes from implied <code>Specializations</code>.</p>
 let publicMemberships : OrderedSet(Membership) = 
     membershipsOfVisibility(VisibilityKind::public, excludedNamespaces) in
 let protectedMemberships : OrderedSet(Membership) = 
     membershipsOfVisibility(VisibilityKind::protected, excludedNamespaces) in
 let inheritedMemberships : OrderedSet(Membership) =
     inheritedMemberships(excludedNamespaces, excludedTypes, excludeImplied) in
 publicMemberships-&gt;
     union(protectedMemberships)-&gt;
     union(inheritedMemberships)</div>
</section>
</li>
<li>
<section class="detail" id="removeRedefinedFeatures(java.util.List)">
<h3>removeRedefinedFeatures</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</span> <span class="element-name">removeRedefinedFeatures</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt; memberships)</span></div>
<div class="block"><p>Return a subset of <code>memberships</code>, removing those <code>Memberships</code> whose <code>memberElements</code> are <code>Features</code> and for which either of the following two conditions holds:</p>
<ol>
<li>The <code>memberElement</code> of the <code>Membership</code> is included in redefined <code>Features</code> of another <code>Membership</code> in <code>memberships</code>.</li>
<li>One of the redefined <code>Features</code> of the <code>Membership</code> is a directly <code>redefinedFeature</code> of an <code>ownedFeature</code> of this <code>Type</code>.</li>
</ol>
<p>For this purpose, the redefined <code>Features</code> of a <code>Membership</code> whose <code>memberElement</code> is a <code>Feature</code> includes the <code>memberElement</code> and all <code>Features</code> directly or indirectly redefined by the <code>memberElement</code>.</p>
 let reducedMemberships : Sequence(Membership) =
     memberships-&gt;reject(mem1 |
         memberships-&gt;excluding(mem1)-&gt;
             exists(mem2 | allRedefinedFeaturesOf(mem2)-&gt;
                 includes(mem1.memberElement))) in
 let redefinedFeatures : Set(Feature) = 
     ownedFeature.redefinition.redefinedFeature-&gt;asSet() in
 reducedMemberships-&gt;reject(mem | allRedefinedFeaturesOf(mem)-&gt;
     exists(feature | redefinedFeatures-&gt;includes(feature)))</div>
</section>
</li>
<li>
<section class="detail" id="allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">
<h3>allRedefinedFeaturesOf</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">allRedefinedFeaturesOf</span><wbr/><span class="parameters">(<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> membership)</span></div>
<div class="block"><p>If the <code>memberElement</code> of the given <code>membership</code> is a <code>Feature</code>, then return all <code>Features</code> directly or indirectly redefined by the <code>memberElement</code>.</p>
 if not membership.memberElement.oclIsType(Feature) then Set{} 
 else membership.memberElement.oclAsType(Feature).allRedefinedFeatures()
 endif</div>
</section>
</li>
<li>
<section class="detail" id="directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>directionOf</h3>
<div class="member-signature"><span class="return-type"><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">directionOf</span><wbr/><span class="parameters">(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block"><p>If the given <code>feature</code> is a <code>feature</code> of this <code>Type</code>, then return its direction relative to this <code>Type</code>, taking conjugation into account.</p>
 
 directionOfExcluding(f, Set{})</div>
</section>
</li>
<li>
<section class="detail" id="directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">
<h3>directionOfExcluding</h3>
<div class="member-signature"><span class="return-type"><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">directionOfExcluding</span><wbr/><span class="parameters">(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; excluded)</span></div>
<div class="block"><p>Return the direction of the given <code>feature</code> relative to this <code>Type</code>, excluding a given set of <code>Types</code> from the search of supertypes of this <code>Type</code>.</p>
 let excludedSelf : Set(Type) = excluded-&gt;including(self) in 
 if feature.owningType = self then feature.direction
 else
     let directions : Sequence(FeatureDirectionKind) =
         supertypes(false)-&gt;excluding(excludedSelf).
         directionOfExcluding(feature, excludedSelf)-&gt;
         select(d | d &lt;&gt; null) in
     if directions-&gt;isEmpty() then null
  else
     let direction : FeatureDirectionKind = directions-&gt;first() in
     if not isConjugated then direction
     else if direction = FeatureDirectionKind::_'in' then FeatureDirectionKind::out
     else if direction = FeatureDirectionKind::out then FeatureDirectionKind::_'in'
     else direction
     endif endif endif   endif
 endif</div>
</section>
</li>
<li>
<section class="detail" id="supertypes(boolean)">
<h3>supertypes</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">supertypes</span><wbr/><span class="parameters">(boolean excludeImplied)</span></div>
<div class="block"><p>If this <code>Type</code> is conjugated, then return just the <code>originalType</code> of the <code>Conjugation</code>. Otherwise, return the <code>general</code> <code>Types</code> from all <code>ownedSpecializations</code> of this type, if <code>excludeImplied = false</code>, or all non-implied <code>ownedSpecializations</code>, if <code>excludeImplied = true</code>.</p>
 if isConjugated then Sequence{conjugator.originalType}
 else if not excludeImplied then ownedSpecialization.general
 else ownedSpecialization-&gt;reject(isImplied).general
 endif
 endif</div>
</section>
</li>
<li>
<section class="detail" id="allSupertypes()">
<h3>allSupertypes</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">allSupertypes</span>()</div>
<div class="block"><p>Return this <code>Type</code> and all <code>Types</code> that are directly or transitively supertypes of this <code>Type</code> (as determined by the <code>supertypes</code> operation with <code>excludeImplied = false</code>).</p>
 
 OrderedSet{self}-&gt;closure(supertypes(false))</div>
</section>
</li>
<li>
<section class="detail" id="specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>specializes</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">specializes</span><wbr/><span class="parameters">(<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> supertype)</span></div>
<div class="block"><p>Check whether this <code>Type</code> is a direct or indirect specialization of the given <code>supertype<code>.</code></code></p>
 if isConjugated then 
     ownedConjugator.originalType.specializes(supertype)
 else
     allSupertypes()-&gt;includes(supertype)
 endif</div>
</section>
</li>
<li>
<section class="detail" id="specializesFromLibrary(java.lang.String)">
<h3>specializesFromLibrary</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">specializesFromLibrary</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> libraryTypeName)</span></div>
<div class="block"><p>Check whether this <code>Type</code> is a direct or indirect specialization of the named library <code>Type</code>. <code>libraryTypeName</code> must conform to the syntax of a KerML qualified name and must resolve to a <code>Type</code> in global scope.</p>
 
 let mem : Membership = resolveGlobal(libraryTypeName) in
 mem &lt;&gt; null and mem.memberElement.oclIsKindOf(Type) and
 specializes(mem.memberElement.oclAsType(Type))</div>
</section>
</li>
<li>
<section class="detail" id="isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isCompatibleWith</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isCompatibleWith</span><wbr/><span class="parameters">(<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> otherType)</span></div>
<div class="block"><p>By default, this <code>Type</code> is compatible with an <code>otherType</code> if it directly or indirectly specializes the <code>otherType</code>.</p>
 specializes(otherType)</div>
</section>
</li>
<li>
<section class="detail" id="multiplicities()">
<h3>multiplicities</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a>&gt;</span> <span class="element-name">multiplicities</span>()</div>
<div class="block"><p>Return the owned or inherited <code>Multiplicities</code> for this <code>Type<span class="invalid-tag">invalid input: '&lt;'</span>./code&gt;.</code></p>
 if multiplicity &lt;&gt; null then OrderedSet{multiplicity}
 else 
     ownedSpecialization.general-&gt;closure(t |
         if t.multiplicity &lt;&gt; null then OrderedSet{}
         else ownedSpecialization.general
     )-&gt;select(multiplicity &lt;&gt; null).multiplicity-&gt;asOrderedSet()
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
