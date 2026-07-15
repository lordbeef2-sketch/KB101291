# JAVA OPENAPI: Feature (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Feature.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Feature.html`
- source_sha256: `d8c8ee57168aaf40a995ee39054667373c8dd522a84f4d244ebc507d505feafe`
- captured_utc: `2026-07-14T16:44:49.461862+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Feature

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `[Namespace](Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[Type](Type.html)`

All Known Subinterfaces:
`[AcceptActionUsage](../../../sysml/model/sysml/AcceptActionUsage.html)`, `[ActionUsage](../../../sysml/model/sysml/ActionUsage.html)`, `[AllocationUsage](../../../sysml/model/sysml/AllocationUsage.html)`, `[AnalysisCaseUsage](../../../sysml/model/sysml/AnalysisCaseUsage.html)`, `[AssertConstraintUsage](../../../sysml/model/sysml/AssertConstraintUsage.html)`, `[AssignmentActionUsage](../../../sysml/model/sysml/AssignmentActionUsage.html)`, `[AttributeUsage](../../../sysml/model/sysml/AttributeUsage.html)`, `[BindingConnector](BindingConnector.html)`, `[BindingConnectorAsUsage](../../../sysml/model/sysml/BindingConnectorAsUsage.html)`, `[BooleanExpression](BooleanExpression.html)`, `[CalculationUsage](../../../sysml/model/sysml/CalculationUsage.html)`, `[CaseUsage](../../../sysml/model/sysml/CaseUsage.html)`, `[CollectExpression](CollectExpression.html)`, `[ConcernUsage](../../../sysml/model/sysml/ConcernUsage.html)`, `[ConnectionUsage](../../../sysml/model/sysml/ConnectionUsage.html)`, `[Connector](Connector.html)`, `[ConnectorAsUsage](../../../sysml/model/sysml/ConnectorAsUsage.html)`, `[ConstraintUsage](../../../sysml/model/sysml/ConstraintUsage.html)`, `[ConstructorExpression](ConstructorExpression.html)`, `[ControlNode](../../../sysml/model/sysml/ControlNode.html)`, `[DecisionNode](../../../sysml/model/sysml/DecisionNode.html)`, `[EnumerationUsage](../../../sysml/model/sysml/EnumerationUsage.html)`, `[EventOccurrenceUsage](../../../sysml/model/sysml/EventOccurrenceUsage.html)`, `[ExhibitStateUsage](../../../sysml/model/sysml/ExhibitStateUsage.html)`, `[Expression](Expression.html)`, `[FeatureChainExpression](FeatureChainExpression.html)`, `[FeatureReferenceExpression](FeatureReferenceExpression.html)`, `[Flow](Flow.html)`, `[FlowEnd](FlowEnd.html)`, `[FlowUsage](../../../sysml/model/sysml/FlowUsage.html)`, `[ForkNode](../../../sysml/model/sysml/ForkNode.html)`, `[ForLoopActionUsage](../../../sysml/model/sysml/ForLoopActionUsage.html)`, `[IfActionUsage](../../../sysml/model/sysml/IfActionUsage.html)`, `[IncludeUseCaseUsage](../../../sysml/model/sysml/IncludeUseCaseUsage.html)`, `[IndexExpression](IndexExpression.html)`, `[InstantiationExpression](InstantiationExpression.html)`, `[InterfaceUsage](../../../sysml/model/sysml/InterfaceUsage.html)`, `[Invariant](Invariant.html)`, `[InvocationExpression](InvocationExpression.html)`, `[ItemUsage](../../../sysml/model/sysml/ItemUsage.html)`, `[JoinNode](../../../sysml/model/sysml/JoinNode.html)`, `[LiteralBoolean](LiteralBoolean.html)`, `[LiteralExpression](LiteralExpression.html)`, `[LiteralInfinity](LiteralInfinity.html)`, `[LiteralInteger](LiteralInteger.html)`, `[LiteralRational](LiteralRational.html)`, `[LiteralString](LiteralString.html)`, `[LoopActionUsage](../../../sysml/model/sysml/LoopActionUsage.html)`, `[MergeNode](../../../sysml/model/sysml/MergeNode.html)`, `[MetadataAccessExpression](MetadataAccessExpression.html)`, `[MetadataFeature](MetadataFeature.html)`, `[MetadataUsage](../../../sysml/model/sysml/MetadataUsage.html)`, `[Multiplicity](Multiplicity.html)`, `[MultiplicityRange](MultiplicityRange.html)`, `[NullExpression](NullExpression.html)`, `[OccurrenceUsage](../../../sysml/model/sysml/OccurrenceUsage.html)`, `[OperatorExpression](OperatorExpression.html)`, `[PartUsage](../../../sysml/model/sysml/PartUsage.html)`, `[PayloadFeature](PayloadFeature.html)`, `[PerformActionUsage](../../../sysml/model/sysml/PerformActionUsage.html)`, `[PortUsage](../../../sysml/model/sysml/PortUsage.html)`, `[ReferenceUsage](../../../sysml/model/sysml/ReferenceUsage.html)`, `[RenderingUsage](../../../sysml/model/sysml/RenderingUsage.html)`, `[RequirementUsage](../../../sysml/model/sysml/RequirementUsage.html)`, `[SatisfyRequirementUsage](../../../sysml/model/sysml/SatisfyRequirementUsage.html)`, `[SelectExpression](SelectExpression.html)`, `[SendActionUsage](../../../sysml/model/sysml/SendActionUsage.html)`, `[StateUsage](../../../sysml/model/sysml/StateUsage.html)`, `[Step](Step.html)`, `[Succession](Succession.html)`, `[SuccessionAsUsage](../../../sysml/model/sysml/SuccessionAsUsage.html)`, `[SuccessionFlow](SuccessionFlow.html)`, `[SuccessionFlowUsage](../../../sysml/model/sysml/SuccessionFlowUsage.html)`, `[TerminateActionUsage](../../../sysml/model/sysml/TerminateActionUsage.html)`, `[TransitionUsage](../../../sysml/model/sysml/TransitionUsage.html)`, `[TriggerInvocationExpression](../../../sysml/model/sysml/TriggerInvocationExpression.html)`, `[Usage](../../../sysml/model/sysml/Usage.html)`, `[UseCaseUsage](../../../sysml/model/sysml/UseCaseUsage.html)`, `[VerificationCaseUsage](../../../sysml/model/sysml/VerificationCaseUsage.html)`, `[ViewpointUsage](../../../sysml/model/sysml/ViewpointUsage.html)`, `[ViewUsage](../../../sysml/model/sysml/ViewUsage.html)`, `[WhileLoopActionUsage](../../../sysml/model/sysml/WhileLoopActionUsage.html)`

@OpenApiAllpublic interfaceFeatureextends [Type](Type.html)

A `Feature` is a `Type` that classifies relations between multiple things (in the universe). The domain of the relation is the intersection of the `featuringTypes` of the `Feature`. (The domain of a `Feature` with no `featuringTyps` is implicitly the most general `Type` *`Base::Anything`* from the Kernel Semantic Library.) The co-domain of the relation is the intersection of the `types` of the `Feature`.
 
 In the simplest cases, the `featuringTypes` and `types` are `Classifiers` and the `Feature` relates two things, one from the domain and one from the range. Examples include cars paired with wheels, people paired with other people, and cars paired with numbers representing the car length.
Since `Features` are `Types`, their `featuringTypes` and `types` can be `Features`. In this case, the `Feature` effectively classifies relations between relations, which can be interpreted as the sequence of things related by the domain `Feature` concatenated with the sequence of things related by the co-domain `Feature`.
The *values* of a `Feature` for a given instance of its domain are all the instances of its co-domain that are related to that domain instance by the `Feature`. The values of a `Feature` with `chainingFeatures` are the same as values of the last `Feature` in the chain, which can be found by starting with values of the first `Feature`, then using those values as domain instances to obtain valus of the second `Feature`, and so on, to values of the last `Feature`.
 
 ownedRedefinition = ownedSubsetting->selectByKind(Redefinition)
 ownedTypeFeaturing = ownedRelationship->selectByKind(TypeFeaturing)->
 select(tf | tf.featureOfType = self)
 ownedSubsetting = ownedSpecialization->selectByKind(Subsetting)
 ownedTyping = ownedGeneralization->selectByKind(FeatureTyping)
 type = 
 let types : OrderedSet(Types) = OrderedSet{self}->
 -- Note: The closure operation automatically handles circular relationships.
 closure(typingFeatures()).typing.type->asOrderedSet() in
 types->reject(t1 | types->exist(t2 | t2 <> t1 and t2.specializes(t1)))
 multiplicity <> null implies multiplicity.featuringType = featuringType 
 specializesFromLibrary('Base::things')
 chainingFeature->excludes(self)
 ownedFeatureChaining = ownedRelationship->selectByKind(FeatureChaining)
 chainingFeature = ownedFeatureChaining.chainingFeature
 chainingFeature->size() <> 1
 isEnd and owningType <> null implies
 let i : Integer = 
 owningType.ownedEndFeature->indexOf(self) in
 owningType.ownedSpecialization.general->
 forAll(supertype |
 supertype.endFeature->size() >= i implies
 redefines(supertype.endFeature->at(i))
 direction = null and
 ownedSpecializations->forAll(isImplied) implies
 ownedMembership->
 selectByKind(FeatureValue)->
 forAll(fv | specializes(fv.value.result))
 isEnd and owningType <> null and
 (owningType.oclIsKindOf(Association) or
 owningType.oclIsKindOf(Connector)) implies
 specializesFromLibrary('Links::Link::participant')
 isComposite and
 ownedTyping.type->includes(oclIsKindOf(Structure)) and
 owningType <> null and
 (owningType.oclIsKindOf(Structure) or
 owningType.type->includes(oclIsKindOf(Structure))) implies
 specializesFromLibrary('Occurrence::Occurrence::suboccurrences')
 ownedTyping.type->exists(selectByKind(Class)) implies
 specializesFromLibrary('Occurrences::occurrences')
 isComposite and
 ownedTyping.type->includes(oclIsKindOf(Class)) and
 owningType <> null and
 (owningType.oclIsKindOf(Class) or
 owningType.oclIsKindOf(Feature) and
 owningType.oclAsType(Feature).type->
 exists(oclIsKindOf(Class))) implies
 specializesFromLibrary('Occurrence::Occurrence::suboccurrences')
 ownedTyping.type->exists(selectByKind(DataType)) implies
 specializesFromLibrary('Base::dataValues')
 owningType <> null and
 owningType.oclIsKindOf(FlowEnd) and
 owningType.ownedFeature->at(1) = self implies
 let flowType : Type = owningType.owningType in
 flowType <> null implies
 let i : Integer = 
 flowType.ownedFeature.indexOf(owningType) in
 (i = 1 implies 
 redefinesFromLibrary('Transfers::Transfer::source::sourceOutput')) and
 (i = 2 implies
 redefinesFromLibrary('Transfers::Transfer::source::targetInput'))
 
 owningType <> null and
 not owningFeatureMembership.
 oclIsKindOf(ReturnParameterMembership) and
 (owningType.oclIsKindOf(Behavior) or
 owningType.oclIsKindOf(Step) and
 (owningType.oclIsKindOf(InvocationExpression) implies
 not ownedRedefinition->exists(not isImplied)) 
 implies
 let i : Integer =
 owningType.ownedFeature->select(direction <> null)->
 reject(owningFeatureMembership.
 oclIsKindOf(ReturnParameterMembership))->
 indexOf(self) in
 owningType.ownedSpecialization.general->
 forAll(supertype |
 let ownedParameters : Sequence(Feature) =
 supertype.ownedFeature->select(direction <> null)->
 reject(owningFeatureMembership.
 oclIsKindOf(ReturnParameterMembership)) in
 ownedParameters->size() >= i implies
 redefines(ownedParameters->at(i))
 ownedTyping.type->exists(selectByKind(Structure)) implies
 specializesFromLibary('Objects::objects')
 owningType <> null and
 (owningType.oclIsKindOf(Function) and
 self = owningType.oclAsType(Function).result or
 owningType.oclIsKindOf(Expression) and
 self = owningType.oclAsType(Expression).result) implies
 owningType.ownedSpecialization.general->
 select(oclIsKindOf(Function) or oclIsKindOf(Expression))->
 forAll(supertype |
 redefines(
 if superType.oclIsKindOf(Function) then
 superType.oclAsType(Function).result
 else
 superType.oclAsType(Expression).result
 endif)
 ownedFeatureInverting = ownedRelationship->selectByKind(FeatureInverting)->
 select(fi | fi.featureInverted = self)
 featuringType =
 let featuringTypes : OrderedSet(Type) = 
 featuring.type->asOrderedSet() in
 if chainingFeature->isEmpty() then featuringTypes
 else
 featuringTypes->
 union(chainingFeature->first().featuringType)->
 asOrderedSet()
 endif
 ownedReferenceSubsetting =
 let referenceSubsettings : OrderedSet(ReferenceSubsetting) =
 ownedSubsetting->selectByKind(ReferenceSubsetting) in
 if referenceSubsettings->isEmpty() then null
 else referenceSubsettings->first() endif
 ownedSubsetting->selectByKind(ReferenceSubsetting)->size() <= 1
 Sequence{2..chainingFeature->size()}->forAll(i |
 chainingFeature->at(i).isFeaturedWithin(chainingFeature->at(i-1)))
 
 isPortion and
 ownedTyping.type->includes(oclIsKindOf(Class)) and
 owningType <> null and
 (owningType.oclIsKindOf(Class) or
 owningType.oclIsKindOf(Feature) and
 owningType.oclAsType(Feature).type->
 exists(oclIsKindOf(Class))) implies
 specializesFromLibrary('Occurrence::Occurrence::portions')
 featureTarget = if chainingFeature->isEmpty() then self else chainingFeature->last() endif
 ownedCrossSubsetting =
 let crossSubsettings: Sequence(CrossSubsetting) = 
 ownedSubsetting->selectByKind(CrossSubsetting) in
 if crossSubsettings->isEmpty() then null
 else crossSubsettings->first()
 endif
 isEnd implies 
 multiplicities().allSuperTypes()->flatten()->
 selectByKind(MultiplicityRange)->exists(hasBounds(1,1))
 crossFeature <> null implies
 crossFeature.type->asSet() = type->asSet()
 ownedSubsetting->selectByKind(CrossSubsetting)->size() <= 1
 crossFeature =
 if ownedCrossSubsetting = null then null
 else 
 let chainingFeatures: Sequence(Feature) = 
 ownedCrossSubsetting.crossedFeature.chainingFeature in
 if chainingFeatures->size() < 2 then null
 else chainingFeatures->at(2)
 endif
 isOwnedCrossFeature() implies
 owner.oclAsType(Feature).type->forAll(t | self.specializes(t))
 isOwnedCrossFeature() implies
 ownedSubsetting.subsettedFeature->includesAll(
 owner.oclAsType(Feature).ownedRedefinition.redefinedFeature->
 select(crossFeature <> null).crossFeature)
 crossFeature <> null implies
 ownedRedefinition.redefinedFeature.crossFeature->
 forAll(f | f <> null implies crossFeature.specializes(f))
 ownedCrossFeature() <> null implies
 crossFeature = ownedCrossFeature()
 isOwnedCrossFeature() implies
 let otherEnds : OrderedSet(Feature) = 
 owner.oclAsType(Feature).owningType.endFeature->excluding(self) in
 if (otherEnds->size() = 1) then
 featuringType = otherEnds->first().type
 else
 featuringType->size() = 1 and
 featuringType->first().isCartesianProduct() and
 featuringType->first().asCartesianProduct() = otherEnds.type and
 featuringType->first().allSupertypes()->includesAll(
 owner.oclAsType(Feature).ownedRedefinition.redefinedFeature->
 select(crossFeature() <> null).crossFeature().featuringType) 
 endif
 isPortion implies not isVariable
 isEnd implied direction = null
 owningFeatureMembership <> null implies
 featuringTypes->exists(t | isFeaturingType(t))
 isConstant implies isVariable
 isVariable implies
 owningType <> null and 
 owningType.specializes('Occurrences::Occurrence')
 isEnd implies not (isDerived or isAbstract or isComposite or isPortion)
 isEnd and isVariable implies isConstant

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[allRedefinedFeatures](#allRedefinedFeatures())()`
Return this `Feature` and all the `Features` that are directly or indirectly `Redefined` by this `Feature`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)>`
`[asCartesianProduct](#asCartesianProduct())()`
If `isCartesianProduct` is true, then return the list of `Types` whose Cartesian product can be represented by this `Feature`.
`boolean`
`[canAccess](#canAccess(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](Feature.html) feature)`
A `Feature` can access another `feature` if the other `feature` is featured within one of the direct or indirect `featuringTypes` of this `Feature`.
`[FeatureDirectionKind](FeatureDirectionKind.html)`
`[directionFor](#directionFor(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](Type.html) type)`
Return the `directionOf` this `Feature` relative to the given `type`.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[effectiveName](#effectiveName())()`
If a `Feature` has no `declaredName` or `declaredShortName`
 , then its effective `name` is given by the effective `name` of the `Feature` returned by the `namingFeature()` operation, if any.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[effectiveShortName](#effectiveShortName())()`
If a `Feature` has no `declaredShortName` or `declaredName`, then its effective `shortName` is given by the effective `shortName` of the `Feature` returned by the `namingFeature()` operation, if any.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[getChainingFeature](#getChainingFeature())()`
The `Feature` that are chained together to determine the values of this `Feature`, derived from the `chainingFeatures` of the `ownedFeatureChainings` of this `Feature`, in the same order.
`[Feature](Feature.html)`
`[getCrossFeature](#getCrossFeature())()`
The second `chainingFeature` of the `crossedFeature` of the `ownedCrossSubsetting` of this `Feature`, if it has one.
`[FeatureDirectionKind](FeatureDirectionKind.html)`
`[getDirection](#getDirection())()`
Indicates how values of this `Feature` are determined or used (as specified for the `FeatureDirectionKind`).
`[Type](Type.html)`
`[getEndOwningType](#getEndOwningType())()`
The `Type` that is related to this `Feature` by an `EndFeatureMembership` in which the `Feature` is an `ownedMemberFeature`.
`[Feature](Feature.html)`
`[getFeatureTarget](#getFeatureTarget())()`
The last of the `chainingFeatures` of this `Feature`, if it has any.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)>`
`[getFeaturingType](#getFeaturingType())()`
`Types` that feature this `Feature`, such that any instance in the domain of the `Feature` must be classified by all of these `Types`, including at least all the `featuringTypes` of its `typeFeaturings`.
`[CrossSubsetting](CrossSubsetting.html)`
`[getOwnedCrossSubsetting](#getOwnedCrossSubsetting())()`
The one `ownedSubsetting` of this `Feature`, if any, that is a `CrossSubsetting}, for which the Feature is the crossingFeature.`
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureChaining](FeatureChaining.html)>`
`[getOwnedFeatureChaining](#getOwnedFeatureChaining())()`
The `ownedRelationships` of this `Feature` that are `FeatureChainings`, for which the `Feature` will be the `featureChained`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureInverting](FeatureInverting.html)>`
`[getOwnedFeatureInverting](#getOwnedFeatureInverting())()`
The `ownedRelationships` of this `Feature` that are `FeatureInvertings` and for which the `Feature` is the `featureInverted`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Redefinition](Redefinition.html)>`
`[getOwnedRedefinition](#getOwnedRedefinition())()`
The `ownedSubsettings` of this `Feature` that are `Redefinitions`, for which the `Feature` is the `redefiningFeature`.
`[ReferenceSubsetting](ReferenceSubsetting.html)`
`[getOwnedReferenceSubsetting](#getOwnedReferenceSubsetting())()`
The one `ownedSubsetting` of this `Feature`, if any, that is a `ReferenceSubsetting`, for which the `Feature` is the `referencingFeature`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Subsetting](Subsetting.html)>`
`[getOwnedSubsetting](#getOwnedSubsetting())()`
The `ownedSpecializations` of this `Feature` that are `Subsettings`, for which the `Feature` is the `subsettingFeature`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[TypeFeaturing](TypeFeaturing.html)>`
`[getOwnedTypeFeaturing](#getOwnedTypeFeaturing())()`
The `ownedRelationships` of this `Feature` that are `TypeFeaturings` and for which the `Feature` is the `featureOfType`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureTyping](FeatureTyping.html)>`
`[getOwnedTyping](#getOwnedTyping())()`
The `ownedSpecializations` of this `Feature` that are `FeatureTypings`, for which the `Feature` is the `typedFeature`.
`[FeatureMembership](FeatureMembership.html)`
`[getOwningFeatureMembership](#getOwningFeatureMembership())()`
The `FeatureMembership` that owns this `Feature` as an `ownedMemberFeature`, determining its `owningType`.
`[Type](Type.html)`
`[getOwningType](#getOwningType())()`
The `Type` that is the `owningType` of the `owningFeatureMembership` of this `Feature`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)>`
`[getType](#getType())()`
`Types` that restrict the values of this `Feature`, such that the values must be instances of all the `types`.
`boolean`
`[isCartesianProduct](#isCartesianProduct())()`
Check whether this `Feature` can be used to represent a Cartesian product of `Types`.
`boolean`
`[isCompatibleWith](#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](Type.html) otherType)`
A `Feature` is compatible with an `otherType` if it either directly or indirectly specializes the `otherType` or if the `otherType` is also a `Feature` and all of the following are true.
`boolean`
`[isComposite](#isComposite())()`
Whether the `Feature` is a composite `feature` of its `featuringType`.
`boolean`
`[isConstant](#isConstant())()`
If `isVariable` is true, then whether the value of this `Feature` nevertheless does not change over all `*snapshots*` of its `owningType`.
`boolean`
`[isDerived](#isDerived())()`
Whether the values of this `Feature` can always be computed from the values of other `Features`.
`boolean`
`[isEnd](#isEnd())()`
Whether or not this `Feature` is an end `Feature`.
`boolean`
`[isFeaturedWithin](#isFeaturedWithin(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](Type.html) type)`
Return if the `featuringTypes` of this `Feature` are compatible with the given `type`.
`boolean`
`[isFeaturingType](#isFeaturingType(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](Type.html) type)`
Return whether the given `type` must be a `featuringType` of this `Feature`.
`boolean`
`[isOrdered](#isOrdered())()`
Whether an order exists for the values of this `Feature` or not.
`boolean`
`[isOwnedCrossFeature](#isOwnedCrossFeature())()`
Return whether this `Feature` is an owned cross `Feature` of an end `Feature`.
`boolean`
`[isPortion](#isPortion())()`
Whether the values of this `Feature` are contained in the space and time of instances of the domain of the `Feature` and represent the same thing as those instances.
`boolean`
`[isUnique](#isUnique())()`
Whether or not values for this `Feature` must have no duplicates or not.
`boolean`
`[isVariable](#isVariable())()`
Whether the value of this `Feature` might vary over time.
`[Feature](Feature.html)`
`[namingFeature](#namingFeature())()`
By default, the naming `Feature` of a `Feature` is given by its first `redefinedFeature` of its first `ownedRedefinition`, if any.
`[Feature](Feature.html)`
`[ownedCrossFeature](#ownedCrossFeature())()`
If this `Feature` is an end `Feature` of its `owningType`, then return the first `ownedMember` of the `Feature` that is a `Feature`, but not a `Multiplicity` or a `MetadataFeature`, and whose `owningMembership` is *not* a `FeatureMembership`.
`boolean`
`[redefines](#redefines(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](Feature.html) redefinedFeature)`
Check whether this `Feature` *directly* redefines the given `redefinedFeature`.
`boolean`
`[redefinesFromLibrary](#redefinesFromLibrary(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) libraryFeatureName)`
Check whether this `Feature` *directly* redefines the named library `Feature`.
`void`
`[setDirection](#setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind))([FeatureDirectionKind](FeatureDirectionKind.html) value)`
Indicates how values of this `Feature` are determined or used (as specified for the `FeatureDirectionKind`).
`void`
`[setIsComposite](#setIsComposite(boolean))(boolean value)`
Whether the `Feature` is a composite `feature` of its `featuringType`.
`void`
`[setIsConstant](#setIsConstant(boolean))(boolean value)`
If `isVariable` is true, then whether the value of this `Feature` nevertheless does not change over all `*snapshots*` of its `owningType`.
`void`
`[setIsDerived](#setIsDerived(boolean))(boolean value)`
Whether the values of this `Feature` can always be computed from the values of other `Features`.
`void`
`[setIsEnd](#setIsEnd(boolean))(boolean value)`
Whether or not this `Feature` is an end `Feature`.
`void`
`[setIsOrdered](#setIsOrdered(boolean))(boolean value)`
Whether an order exists for the values of this `Feature` or not.
`void`
`[setIsPortion](#setIsPortion(boolean))(boolean value)`
Whether the values of this `Feature` are contained in the space and time of instances of the domain of the `Feature` and represent the same thing as those instances.
`void`
`[setIsUnique](#setIsUnique(boolean))(boolean value)`
Whether or not values for this `Feature` must have no duplicates or not.
`void`
`[setIsVariable](#setIsVariable(boolean))(boolean value)`
Whether the value of this `Feature` might vary over time.
`boolean`
`[subsetsChain](#subsetsChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](Feature.html) first,
 [Feature](Feature.html) second)`
Check whether this `Feature` directly or indirectly specializes a `Feature` whose last two `chainingFeatures` are the given `Features` `first` and `second`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)>`
`[supertypes](#supertypes(boolean))(boolean excludeImplied)`
let supertypes : OrderedSet(Type) = 
 self.oclAsType(Type).supertypes(excludeImplied) in
 if featureTarget = self then supertypes
 else supertypes->append(featureTarget)
 endif
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[typingFeatures](#typingFeatures())()`
Return the `Features` used to determine the `types` of this `Feature` (other than this `Feature` itself).
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](Element.html)
`[escapedName](Element.html#escapedName()), [getAliasIds](Element.html#getAliasIds()), [getDeclaredName](Element.html#getDeclaredName()), [getDeclaredShortName](Element.html#getDeclaredShortName()), [getDocumentation](Element.html#getDocumentation()), [getElementId](Element.html#getElementId()), [getName](Element.html#getName()), [getOwnedAnnotation](Element.html#getOwnedAnnotation()), [getOwnedElement](Element.html#getOwnedElement()), [getOwnedRelationship](Element.html#getOwnedRelationship()), [getOwner](Element.html#getOwner()), [getOwningMembership](Element.html#getOwningMembership()), [getOwningNamespace](Element.html#getOwningNamespace()), [getOwningRelationship](Element.html#getOwningRelationship()), [getQualifiedName](Element.html#getQualifiedName()), [getShortName](Element.html#getShortName()), [getTextualRepresentation](Element.html#getTextualRepresentation()), [isImpliedIncluded](Element.html#isImpliedIncluded()), [isLibraryElement](Element.html#isLibraryElement()), [libraryNamespace](Element.html#libraryNamespace()), [path](Element.html#path()), [setDeclaredName](Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](Element.html#setDeclaredShortName(java.lang.String)), [setElementId](Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](Element.html#setIsImpliedIncluded(boolean)), [setOwner](Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
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
`[allRedefinedFeaturesOf](Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)), [allSupertypes](Type.html#allSupertypes()), [directionOf](Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [directionOfExcluding](Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)), [getDifferencingType](Type.html#getDifferencingType()), [getDirectedFeature](Type.html#getDirectedFeature()), [getEndFeature](Type.html#getEndFeature()), [getFeature](Type.html#getFeature()), [getFeatureMembership](Type.html#getFeatureMembership()), [getInheritedFeature](Type.html#getInheritedFeature()), [getInheritedMembership](Type.html#getInheritedMembership()), [getInput](Type.html#getInput()), [getIntersectingType](Type.html#getIntersectingType()), [getMultiplicity](Type.html#getMultiplicity()), [getOutput](Type.html#getOutput()), [getOwnedConjugator](Type.html#getOwnedConjugator()), [getOwnedDifferencing](Type.html#getOwnedDifferencing()), [getOwnedDisjoining](Type.html#getOwnedDisjoining()), [getOwnedEndFeature](Type.html#getOwnedEndFeature()), [getOwnedFeature](Type.html#getOwnedFeature()), [getOwnedFeatureMembership](Type.html#getOwnedFeatureMembership()), [getOwnedIntersecting](Type.html#getOwnedIntersecting()), [getOwnedSpecialization](Type.html#getOwnedSpecialization()), [getOwnedUnioning](Type.html#getOwnedUnioning()), [getUnioningType](Type.html#getUnioningType()), [inheritableMemberships](Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)), [inheritedMemberships](Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)), [isAbstract](Type.html#isAbstract()), [isConjugated](Type.html#isConjugated()), [isSufficient](Type.html#isSufficient()), [multiplicities](Type.html#multiplicities()), [nonPrivateMemberships](Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)), [removeRedefinedFeatures](Type.html#removeRedefinedFeatures(java.util.List)), [setIsAbstract](Type.html#setIsAbstract(boolean)), [setIsSufficient](Type.html#setIsSufficient(boolean)), [specializes](Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [specializesFromLibrary](Type.html#specializesFromLibrary(java.lang.String)), [visibleMemberships](Type.html#visibleMemberships(java.util.List,boolean,boolean))`

============ METHOD DETAIL ========== 
Method Details
getOwningType
@CheckForNull[Type](Type.html) getOwningType()
The `Type` that is the `owningType` of the `owningFeatureMembership` of this `Feature`.
Returns:
the owningType value
Model:
derived="true"
 transient="true"
 opposite=[`Type.getOwnedFeature()`](Type.html#getOwnedFeature())
 subsets=[`Element.getOwningNamespace()`](Element.html#getOwningNamespace()), [`getFeaturingType()`](#getFeaturingType())
isUnique
boolean isUnique()
Whether or not values for this `Feature` must have no duplicates or not.
Returns:
the isUnique value
Model:
derived="false"
 transient="false"
setIsUnique
void setIsUnique(boolean value)
Whether or not values for this `Feature` must have no duplicates or not.
Parameters:
`value` - the isUnique value
Model:
derived="false"
 transient="false"
isOrdered
boolean isOrdered()
Whether an order exists for the values of this `Feature` or not.
Returns:
the isOrdered value
Model:
derived="false"
 transient="false"
setIsOrdered
void setIsOrdered(boolean value)
Whether an order exists for the values of this `Feature` or not.
Parameters:
`value` - the isOrdered value
Model:
derived="false"
 transient="false"
getType
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> getType()
`Types` that restrict the values of this `Feature`, such that the values must be instances of all the `types`. The types of a `Feature` are derived from its `typings` and the `types` of its `subsettings`. If the `Feature` is chained, then the `types` of the last `Feature` in the chain are also `types` of the chained `Feature`.
Returns:
the type value
Model:
derived="true"
 transient="true"
 oppositeRoleName="typedFeature"
getOwnedRedefinition
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Redefinition](Redefinition.html)> getOwnedRedefinition()
The `ownedSubsettings` of this `Feature` that are `Redefinitions`, for which the `Feature` is the `redefiningFeature`.
Returns:
the ownedRedefinition value
Model:
derived="true"
 transient="true"
 oppositeRoleName="owningFeature"
 subsets=[`getOwnedSubsetting()`](#getOwnedSubsetting())
getOwnedSubsetting
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Subsetting](Subsetting.html)> getOwnedSubsetting()
The `ownedSpecializations` of this `Feature` that are `Subsettings`, for which the `Feature` is the `subsettingFeature`.
Returns:
the ownedSubsetting value
Model:
derived="true"
 transient="true"
 opposite=[`Subsetting.getOwningFeature()`](Subsetting.html#getOwningFeature())
 subsets=[`Type.getOwnedSpecialization()`](Type.html#getOwnedSpecialization())
getOwningFeatureMembership
@CheckForNull[FeatureMembership](FeatureMembership.html) getOwningFeatureMembership()
The `FeatureMembership` that owns this `Feature` as an `ownedMemberFeature`, determining its `owningType`.
Returns:
the owningFeatureMembership value
Model:
derived="true"
 transient="true"
 opposite=[`FeatureMembership.getOwnedMemberFeature()`](FeatureMembership.html#getOwnedMemberFeature())
 subsets=[`Element.getOwningMembership()`](Element.html#getOwningMembership())
isComposite
boolean isComposite()
Whether the `Feature` is a composite `feature` of its `featuringType`. If so, the values of the `Feature` cannot exist after its featuring instance no longer does and cannot be values of another composite feature that is not on the same featuring instance.
Returns:
the isComposite value
Model:
derived="false"
 transient="false"
setIsComposite
void setIsComposite(boolean value)
Whether the `Feature` is a composite `feature` of its `featuringType`. If so, the values of the `Feature` cannot exist after its featuring instance no longer does and cannot be values of another composite feature that is not on the same featuring instance.
Parameters:
`value` - the isComposite value
Model:
derived="false"
 transient="false"
isEnd
boolean isEnd()
Whether or not this `Feature` is an end `Feature`. An end `Feature` always has multiplicity 1, mapping each of its domain instances to a single co-domain instance. However, it may have a `crossFeature`, in which case values of the `crossFeature` must be the same as those found by navigation across instances of the `owningType` from values of other end `Features` to values of this Feature. If the `owningType` has *n* end `Features`, then the multiplicity, ordering, and uniqueness declared for the `crossFeature` of any one of these end `Features` constrains the cardinality, ordering, and uniqueness of the collection of values of that `Feature` reached by navigation when the values of the other *n-1* end `Features` are held fixed.
Returns:
the isEnd value
Model:
derived="false"
 transient="false"
setIsEnd
void setIsEnd(boolean value)
Whether or not this `Feature` is an end `Feature`. An end `Feature` always has multiplicity 1, mapping each of its domain instances to a single co-domain instance. However, it may have a `crossFeature`, in which case values of the `crossFeature` must be the same as those found by navigation across instances of the `owningType` from values of other end `Features` to values of this Feature. If the `owningType` has *n* end `Features`, then the multiplicity, ordering, and uniqueness declared for the `crossFeature` of any one of these end `Features` constrains the cardinality, ordering, and uniqueness of the collection of values of that `Feature` reached by navigation when the values of the other *n-1* end `Features` are held fixed.
Parameters:
`value` - the isEnd value
Model:
derived="false"
 transient="false"
getEndOwningType
@CheckForNull[Type](Type.html) getEndOwningType()
The `Type` that is related to this `Feature` by an `EndFeatureMembership` in which the `Feature` is an `ownedMemberFeature`.
Returns:
the endOwningType value
Model:
derived="true"
 transient="true"
 opposite=[`Type.getOwnedEndFeature()`](Type.html#getOwnedEndFeature())
 subsets=[`getOwningType()`](#getOwningType())
getOwnedTyping
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureTyping](FeatureTyping.html)> getOwnedTyping()
The `ownedSpecializations` of this `Feature` that are `FeatureTypings`, for which the `Feature` is the `typedFeature`.
Returns:
the ownedTyping value
Model:
derived="true"
 transient="true"
 opposite=[`FeatureTyping.getOwningFeature()`](FeatureTyping.html#getOwningFeature())
 subsets=[`Type.getOwnedSpecialization()`](Type.html#getOwnedSpecialization())
getFeaturingType
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> getFeaturingType()
`Types` that feature this `Feature`, such that any instance in the domain of the `Feature` must be classified by all of these `Types`, including at least all the `featuringTypes` of its `typeFeaturings`. If the `Feature` is chained, then the `featuringTypes` of the first `Feature` in the chain are also `featuringTypes` of the chained `Feature`.
Returns:
the featuringType value
Model:
derived="true"
 transient="true"
 oppositeRoleName="featureOfType"
getOwnedTypeFeaturing
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[TypeFeaturing](TypeFeaturing.html)> getOwnedTypeFeaturing()
The `ownedRelationships` of this `Feature` that are `TypeFeaturings` and for which the `Feature` is the `featureOfType`.
Returns:
the ownedTypeFeaturing value
Model:
derived="true"
 transient="true"
 opposite=[`TypeFeaturing.getOwningFeatureOfType()`](TypeFeaturing.html#getOwningFeatureOfType())
 subsets=[`Element.getOwnedRelationship()`](Element.html#getOwnedRelationship())
isDerived
boolean isDerived()
Whether the values of this `Feature` can always be computed from the values of other `Features`.
Returns:
the isDerived value
Model:
derived="false"
 transient="false"
setIsDerived
void setIsDerived(boolean value)
Whether the values of this `Feature` can always be computed from the values of other `Features`.
Parameters:
`value` - the isDerived value
Model:
derived="false"
 transient="false"
getChainingFeature
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> getChainingFeature()
The `Feature` that are chained together to determine the values of this `Feature`, derived from the `chainingFeatures` of the `ownedFeatureChainings` of this `Feature`, in the same order. The values of a `Feature` with `chainingFeatures` are the same as values of the last `Feature` in the chain, which can be found by starting with the values of the first `Feature` (for each instance of the domain of the original `Feature`), then using each of those as domain instances to find the values of the second `Feature` in chainingFeatures, and so on, to values of the last `Feature`.
Returns:
the chainingFeature value
Model:
derived="true"
 transient="true"
 oppositeRoleName="chainedFeature"
getOwnedFeatureInverting
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureInverting](FeatureInverting.html)> getOwnedFeatureInverting()
The `ownedRelationships` of this `Feature` that are `FeatureInvertings` and for which the `Feature` is the `featureInverted`.
Returns:
the ownedFeatureInverting value
Model:
derived="true"
 transient="true"
 opposite=[`FeatureInverting.getOwningFeature()`](FeatureInverting.html#getOwningFeature())
 subsets=[`Element.getOwnedRelationship()`](Element.html#getOwnedRelationship())
getOwnedFeatureChaining
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureChaining](FeatureChaining.html)> getOwnedFeatureChaining()
The `ownedRelationships` of this `Feature` that are `FeatureChainings`, for which the `Feature` will be the `featureChained`.
Returns:
the ownedFeatureChaining value
Model:
derived="true"
 transient="true"
 opposite=[`FeatureChaining.getFeatureChained()`](FeatureChaining.html#getFeatureChained())
 subsets=[`Element.getOwnedRelationship()`](Element.html#getOwnedRelationship())
isPortion
boolean isPortion()
Whether the values of this `Feature` are contained in the space and time of instances of the domain of the `Feature` and represent the same thing as those instances.
Returns:
the isPortion value
Model:
derived="false"
 transient="false"
setIsPortion
void setIsPortion(boolean value)
Whether the values of this `Feature` are contained in the space and time of instances of the domain of the `Feature` and represent the same thing as those instances.
Parameters:
`value` - the isPortion value
Model:
derived="false"
 transient="false"
isVariable
boolean isVariable()
Whether the value of this `Feature` might vary over time. That is, whether the `Feature` may have a different value for each *`snapshot`* of an `owningType` that is an *`Occurrence`*.
Returns:
the isVariable value
Model:
derived="false"
 transient="false"
setIsVariable
void setIsVariable(boolean value)
Whether the value of this `Feature` might vary over time. That is, whether the `Feature` may have a different value for each *`snapshot`* of an `owningType` that is an *`Occurrence`*.
Parameters:
`value` - the isVariable value
Model:
derived="false"
 transient="false"
isConstant
boolean isConstant()
If `isVariable` is true, then whether the value of this `Feature` nevertheless does not change over all `*snapshots*` of its `owningType`.
Returns:
the isConstant value
Model:
derived="false"
 transient="false"
setIsConstant
void setIsConstant(boolean value)
If `isVariable` is true, then whether the value of this `Feature` nevertheless does not change over all `*snapshots*` of its `owningType`.
Parameters:
`value` - the isConstant value
Model:
derived="false"
 transient="false"
getOwnedReferenceSubsetting
@CheckForNull[ReferenceSubsetting](ReferenceSubsetting.html) getOwnedReferenceSubsetting()
The one `ownedSubsetting` of this `Feature`, if any, that is a `ReferenceSubsetting`, for which the `Feature` is the `referencingFeature`.
Returns:
the ownedReferenceSubsetting value
Model:
derived="true"
 transient="true"
 opposite=[`ReferenceSubsetting.getReferencingFeature()`](ReferenceSubsetting.html#getReferencingFeature())
 subsets=[`getOwnedSubsetting()`](#getOwnedSubsetting())
getFeatureTarget
[Feature](Feature.html) getFeatureTarget()
The last of the `chainingFeatures` of this `Feature`, if it has any. Otherwise, this `Feature` itself.
Returns:
the featureTarget value
Model:
derived="true"
 transient="true"
 oppositeRoleName="baseFeature"
getCrossFeature
@CheckForNull[Feature](Feature.html) getCrossFeature()
The second `chainingFeature` of the `crossedFeature` of the `ownedCrossSubsetting` of this `Feature`, if it has one. Semantically, the values of the `crossFeature` of an end `Feature` must include all values of the end `Feature` obtained when navigating from values of the other end `Features` of the same `owningType`.
Returns:
the crossFeature value
Model:
derived="true"
 transient="true"
 oppositeRoleName="featureCrossing"
getDirection
@CheckForNull[FeatureDirectionKind](FeatureDirectionKind.html) getDirection()
Indicates how values of this `Feature` are determined or used (as specified for the `FeatureDirectionKind`).
Returns:
the direction value
Model:
derived="false"
 transient="false"
setDirection
void setDirection(@CheckForNull
 [FeatureDirectionKind](FeatureDirectionKind.html) value)
Indicates how values of this `Feature` are determined or used (as specified for the `FeatureDirectionKind`).
Parameters:
`value` - the direction value
Model:
derived="false"
 transient="false"
getOwnedCrossSubsetting
@CheckForNull[CrossSubsetting](CrossSubsetting.html) getOwnedCrossSubsetting()
The one `ownedSubsetting` of this `Feature`, if any, that is a `CrossSubsetting}, for which the Feature is the crossingFeature.`
Returns:
the ownedCrossSubsetting value
Model:
derived="true"
 transient="true"
 opposite=[`CrossSubsetting.getCrossingFeature()`](CrossSubsetting.html#getCrossingFeature())
 subsets=[`getOwnedSubsetting()`](#getOwnedSubsetting())
directionFor
[FeatureDirectionKind](FeatureDirectionKind.html) directionFor([Type](Type.html) type)
Return the `directionOf` this `Feature` relative to the given `type`.
 type.directionOf(self)
effectiveShortName
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) effectiveShortName()
If a `Feature` has no `declaredShortName` or `declaredName`, then its effective `shortName` is given by the effective `shortName` of the `Feature` returned by the `namingFeature()` operation, if any.
 if declaredShortName <> null or declaredName <> null then
 declaredShortName
 else
 let namingFeature : Feature = namingFeature() in
 if namingFeature = null then
 null
 else
 namingFeature.effectiveShortName()
 endif
 endif
Specified by:
`[effectiveShortName](Element.html#effectiveShortName())` in interface `[Element](Element.html)`
effectiveName
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) effectiveName()
If a `Feature` has no `declaredName` or `declaredShortName`
 , then its effective `name` is given by the effective `name` of the `Feature` returned by the `namingFeature()` operation, if any.
 if declaredShortName <> null or declaredName <> null then
 declaredName
 else
 let namingFeature : Feature = namingFeature() in
 if namingFeature = null then
 null
 else
 namingFeature.effectiveName()
 endif
 endif
Specified by:
`[effectiveName](Element.html#effectiveName())` in interface `[Element](Element.html)`
namingFeature
[Feature](Feature.html) namingFeature()
By default, the naming `Feature` of a `Feature` is given by its first `redefinedFeature` of its first `ownedRedefinition`, if any.
 if ownedRedefinition->isEmpty() then
 null
 else
 ownedRedefinition->at(1).redefinedFeature
 endif
supertypes
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> supertypes(boolean excludeImplied)
let supertypes : OrderedSet(Type) = 
 self.oclAsType(Type).supertypes(excludeImplied) in
 if featureTarget = self then supertypes
 else supertypes->append(featureTarget)
 endif
Specified by:
`[supertypes](Type.html#supertypes(boolean))` in interface `[Type](Type.html)`
redefines
boolean redefines([Feature](Feature.html) redefinedFeature)
Check whether this `Feature` *directly* redefines the given `redefinedFeature`.
 ownedRedefinition.redefinedFeature->includes(redefinedFeature)
redefinesFromLibrary
boolean redefinesFromLibrary([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) libraryFeatureName)
Check whether this `Feature` *directly* redefines the named library `Feature`. `libraryFeatureName` must conform to the syntax of a KerML qualified name and must resolve to a `Feature` in global scope.
 let mem: Membership = resolveGlobal(libraryFeatureName) in
 mem <> null and mem.memberElement.oclIsKindOf(Feature) and
 redefines(mem.memberElement.oclAsType(Feature))
subsetsChain
boolean subsetsChain([Feature](Feature.html) first,
 [Feature](Feature.html) second)
Check whether this `Feature` directly or indirectly specializes a `Feature` whose last two `chainingFeatures` are the given `Features` `first` and `second`.
 allSuperTypes()->selectAsKind(Feature)->
 exists(f | let n: Integer = f.chainingFeature->size() in
 n >= 2 and
 f.chainingFeature->at(n-1) = first and
 f.chainingFeature->at(n) = second)
isCompatibleWith
boolean isCompatibleWith([Type](Type.html) otherType)
A `Feature` is compatible with an `otherType` if it either directly or indirectly specializes the `otherType` or if the `otherType` is also a `Feature` and all of the following are true.
Neither this `Feature` or the `otherType` have any `ownedFeatures`.
This `Feature` directly or indirectly redefines a `Feature` that is also directly or indirectly redefined by the `otherType`.
This `Feature` can access the `otherType`.
 specializes(otherType) or
 supertype.oclIsKindOf(Feature) and
 ownedFeature->isEmpty() and
 otherType.ownedFeature->isEmpty() and
 ownedRedefinitions.allRedefinedFeatures()->exists(f | 
 otherType.oclAsType(Feature).allRedefinedFeatures()->includes(f)) and
 canAccess(otherType.oclAsType(Feature))
Specified by:
`[isCompatibleWith](Type.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type))` in interface `[Type](Type.html)`
typingFeatures
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> typingFeatures()
Return the `Features` used to determine the `types` of this `Feature` (other than this `Feature` itself). If this `Feature` is *not* conjugated, then the `typingFeatures` consist of all subsetted `Features`, *except* from `CrossSubsetting`, and the last `chainingFeature` (if any). If this `Feature` *is* conjugated, then the `typingFeatures` are only its `originalType` (if the `originalType` is a `Feature`).
**Note.** `CrossSubsetting` is excluded from the determination of the `type` of a `Feature` in order to avoid circularity in the construction of implied `CrossSubsetting` relationships. The `validateFeatureCrossFeatureType` requires that the `crossFeature` of a `Feature` have the same `type` as the `Feature`.
 
 if not isConjugated then
 let subsettedFeatures : OrderedSet(Feature) = 
 subsetting->reject(s | s.oclIsKindOf(CrossSubsetting)).subsettedFeatures in 
 if chainingFeature->isEmpty() or
 subsettedFeature->includes(chainingFeature->last())
 then subsettedFeatures
 else subsettedFeatures->append(chainingFeature->last())
 endif
 else if conjugator.originalType.oclIsKindOf(Feature) then
 OrderedSet{conjugator.originalType.oclAsType(Feature)}
 else OrderedSet{}
 endif endif
asCartesianProduct
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> asCartesianProduct()
If `isCartesianProduct` is true, then return the list of `Types` whose Cartesian product can be represented by this `Feature`. (If `isCartesianProduct` is not true, the operation will still return a valid value, it will just not represent anything useful.)
 featuringType->select(t | t.owner <> self)->
 union(featuringType->select(t | t.owner = self)->
 selectByKind(Feature).asCartesianProduct())->
 union(type)
isCartesianProduct
boolean isCartesianProduct()
Check whether this `Feature` can be used to represent a Cartesian product of `Types`.
 type->size() = 1 and
 featuringType.size() = 1 and
 (featuringType.first().owner = self implies
 featuringType.first().oclIsKindOf(Feature) and
 featuringType.first().oclAsType(Feature).isCartesianProduct())
isOwnedCrossFeature
boolean isOwnedCrossFeature()
Return whether this `Feature` is an owned cross `Feature` of an end `Feature`.
 owningNamespace <> null and 
 owningNamespace.oclIsKindOf(Feature) and 
 owningNamespace.oclAsType(Feature).ownedCrossFeature() = self
ownedCrossFeature
[Feature](Feature.html) ownedCrossFeature()
If this `Feature` is an end `Feature` of its `owningType`, then return the first `ownedMember` of the `Feature` that is a `Feature`, but not a `Multiplicity` or a `MetadataFeature`, and whose `owningMembership` is *not* a `FeatureMembership`. If this exists, it is the `crossFeature` of the end `Feature`.
 if not isEnd or owningType = null then null
 else
 let ownedMemberFeatures: Sequence(Feature) =
 ownedMember->selectByKind(Feature)->
 reject(oclIsKindOf(Multiplicity) or 
 oclIsKindOf(MetadataFeature) or
 oclIsKindOf(FeatureValue))->
 reject(owningMembership.oclIsKindOf(FeatureMembership)) in
 if ownedMemberFeatures.isEmpty() then null
 else ownedMemberFeatures->first()
 endif
allRedefinedFeatures
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> allRedefinedFeatures()
Return this `Feature` and all the `Features` that are directly or indirectly `Redefined` by this `Feature`.
 ownedRedefinition.redefinedFeature->
 closure(ownedRedefinition.redefinedFeature)->
 asOrderedSet()->prepend(self)
isFeaturedWithin
boolean isFeaturedWithin([Type](Type.html) type)
Return if the `featuringTypes` of this `Feature` are compatible with the given `type`. If `type` is null, then check if this `Feature` is explicitly or implicitly featured by *`Base::Anything`*. If this `Feature` has `isVariable = true`, then also consider it to be featured within its `owningType`. If this `Feature` is a feature chain whose first `chainingFeature` has `isVariable = true`, then also consider it to be featured within the `owningType` of its first `chainingFeature`.
 if type = null then
 featuringType->forAll(f | f = resolveGlobal('Base::Anything').memberElement)
 else
 featuringType->forAll(f | type.isCompatibleWith(f)) or
 isVariable and type.specializes(owningType) or
 chainingFeature->notEmpty() and chainingFeature->first().isVariable and
 type.specializes(chainingFeature->first().owningType)
 endif
canAccess
boolean canAccess([Feature](Feature.html) feature)
A `Feature` can access another `feature` if the other `feature` is featured within one of the direct or indirect `featuringTypes` of this `Feature`.
 let anythingType: Element =
 subsettingFeature.resolveGlobal('Base::Anything').memberElement in
 let allFeaturingTypes : Sequence(Type) =
 featuringTypes->closure(t |
 if not t.oclIsKindOf(Feature) then Sequence{}
 else
 let featuringTypes : OrderedSet(Type) = t.oclAsType(Feature).featuringType in
 if featuringTypes->isEmpty() then Sequence{anythingType}
 else featuringTypes
 endif 
 endif) in
 allFeaturingTypes->exists(t | feature.isFeaturedWithin(t))
isFeaturingType
boolean isFeaturingType([Type](Type.html) type)
Return whether the given `type` must be a `featuringType` of this `Feature`. If this `Feature` has `isVariable = false`, then return true if the `type` is the `owningType` of the `Feature`. If `isVariable = true`, then return true if the `type` is a `Feature` representing the *`snapshots`* of the `owningType` of this `Feature`.
 owningType <> null and
 if not isVariable then type = owningType
 else if owningType = resolveGlobal('Occurrences::Occurrence').memberElement then
 type = resolveGlobal('Occurrences::Occurrence::snapshots').memberElement 
 else 
 type.oclIsKindOf(Feature) and
 let feature : Feature = type.oclAsType(Feature) in
 feature.featuringType->includes(owningType) and
 feature.redefinesFromLibrary('Occurrences::Occurrence::snapshots')
 endif

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Feature">Interface Feature</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../sysml/model/sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a></code>, <code><a href="../../../sysml/model/sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssertConstraintUsage</a></code>, <code><a href="../../../sysml/model/sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a></code>, <code><a href="BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BindingConnector</a></code>, <code><a href="../../../sysml/model/sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">BindingConnectorAsUsage</a></code>, <code><a href="BooleanExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BooleanExpression</a></code>, <code><a href="../../../sysml/model/sysml/CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a></code>, <code><a href="../../../sysml/model/sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a></code>, <code><a href="CollectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CollectExpression</a></code>, <code><a href="../../../sysml/model/sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a></code>, <code><a href="../../../sysml/model/sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionUsage</a></code>, <code><a href="Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a></code>, <code><a href="../../../sysml/model/sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a></code>, <code><a href="../../../sysml/model/sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a></code>, <code><a href="ConstructorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ConstructorExpression</a></code>, <code><a href="../../../sysml/model/sysml/ControlNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ControlNode</a></code>, <code><a href="../../../sysml/model/sysml/DecisionNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">DecisionNode</a></code>, <code><a href="../../../sysml/model/sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a></code>, <code><a href="../../../sysml/model/sysml/EventOccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EventOccurrenceUsage</a></code>, <code><a href="../../../sysml/model/sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ExhibitStateUsage</a></code>, <code><a href="Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code>, <code><a href="FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a></code>, <code><a href="FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a></code>, <code><a href="Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a></code>, <code><a href="FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FlowEnd</a></code>, <code><a href="../../../sysml/model/sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a></code>, <code><a href="../../../sysml/model/sysml/ForkNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForkNode</a></code>, <code><a href="../../../sysml/model/sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IncludeUseCaseUsage</a></code>, <code><a href="IndexExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">IndexExpression</a></code>, <code><a href="InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InstantiationExpression</a></code>, <code><a href="../../../sysml/model/sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a></code>, <code><a href="Invariant.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Invariant</a></code>, <code><a href="InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></code>, <code><a href="../../../sysml/model/sysml/ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a></code>, <code><a href="../../../sysml/model/sysml/JoinNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">JoinNode</a></code>, <code><a href="LiteralBoolean.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralBoolean</a></code>, <code><a href="LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralExpression</a></code>, <code><a href="LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInfinity</a></code>, <code><a href="LiteralInteger.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInteger</a></code>, <code><a href="LiteralRational.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralRational</a></code>, <code><a href="LiteralString.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralString</a></code>, <code><a href="../../../sysml/model/sysml/LoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">LoopActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/MergeNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MergeNode</a></code>, <code><a href="MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a></code>, <code><a href="MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></code>, <code><a href="../../../sysml/model/sysml/MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a></code>, <code><a href="Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a></code>, <code><a href="MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a></code>, <code><a href="NullExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NullExpression</a></code>, <code><a href="../../../sysml/model/sysml/OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a></code>, <code><a href="OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></code>, <code><a href="../../../sysml/model/sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a></code>, <code><a href="PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">PayloadFeature</a></code>, <code><a href="../../../sysml/model/sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a></code>, <code><a href="../../../sysml/model/sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a></code>, <code><a href="../../../sysml/model/sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a></code>, <code><a href="../../../sysml/model/sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></code>, <code><a href="../../../sysml/model/sysml/SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SatisfyRequirementUsage</a></code>, <code><a href="SelectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SelectExpression</a></code>, <code><a href="../../../sysml/model/sysml/SendActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SendActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a></code>, <code><a href="Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></code>, <code><a href="Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a></code>, <code><a href="../../../sysml/model/sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionAsUsage</a></code>, <code><a href="SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SuccessionFlow</a></code>, <code><a href="../../../sysml/model/sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a></code>, <code><a href="../../../sysml/model/sysml/TerminateActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TerminateActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a></code>, <code><a href="../../../sysml/model/sysml/TriggerInvocationExpression.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TriggerInvocationExpression</a></code>, <code><a href="../../../sysml/model/sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></code>, <code><a href="../../../sysml/model/sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a></code>, <code><a href="../../../sysml/model/sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a></code>, <code><a href="../../../sysml/model/sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Feature</span><span class="extends-implements">
extends <a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span></div>
<div class="block"><p>A <code>Feature</code> is a <code>Type</code> that classifies relations between multiple things (in the universe). The domain of the relation is the intersection of the <code>featuringTypes</code> of the <code>Feature</code>. (The domain of a <code>Feature</code> with no <code>featuringTyps</code> is implicitly the most general <code>Type</code> <em><code>Base::Anything</code></em> from the Kernel Semantic Library.) The co-domain of the relation is the intersection of the <code>types</code> of the <code>Feature</code>.
 
 <p>In the simplest cases, the <code>featuringTypes</code> and <code>types</code> are <code>Classifiers</code> and the <code>Feature</code> relates two things, one from the domain and one from the range. Examples include cars paired with wheels, people paired with other people, and cars paired with numbers representing the car length.</p>
<p>Since <code>Features</code> are <code>Types</code>, their <code>featuringTypes</code> and <code>types</code> can be <code>Features</code>. In this case, the <code>Feature</code> effectively classifies relations between relations, which can be interpreted as the sequence of things related by the domain <code>Feature</code> concatenated with the sequence of things related by the co-domain <code>Feature</code>.</p>
<p>The <em>values</em> of a <code>Feature</code> for a given instance of its domain are all the instances of its co-domain that are related to that domain instance by the <code>Feature</code>. The values of a <code>Feature</code> with <code>chainingFeatures</code> are the same as values of the last <code>Feature</code> in the chain, which can be found by starting with values of the first <code>Feature</code>, then using those values as domain instances to obtain valus of the second <code>Feature</code>, and so on, to values of the last <code>Feature</code>.</p>
 
 ownedRedefinition = ownedSubsetting-&gt;selectByKind(Redefinition)
 ownedTypeFeaturing = ownedRelationship-&gt;selectByKind(TypeFeaturing)-&gt;
     select(tf | tf.featureOfType = self)
 ownedSubsetting = ownedSpecialization-&gt;selectByKind(Subsetting)
 ownedTyping = ownedGeneralization-&gt;selectByKind(FeatureTyping)
 type = 
     let types : OrderedSet(Types) = OrderedSet{self}-&gt;
         -- Note: The closure operation automatically handles circular relationships.
         closure(typingFeatures()).typing.type-&gt;asOrderedSet() in
     types-&gt;reject(t1 | types-&gt;exist(t2 | t2 &lt;&gt; t1 and t2.specializes(t1)))
 multiplicity &lt;&gt; null implies multiplicity.featuringType = featuringType 
 specializesFromLibrary('Base::things')
 chainingFeature-&gt;excludes(self)
 ownedFeatureChaining = ownedRelationship-&gt;selectByKind(FeatureChaining)
 chainingFeature = ownedFeatureChaining.chainingFeature
 chainingFeature-&gt;size() &lt;&gt; 1
 isEnd and owningType &lt;&gt; null implies
     let i : Integer = 
         owningType.ownedEndFeature-&gt;indexOf(self) in
     owningType.ownedSpecialization.general-&gt;
         forAll(supertype |
              supertype.endFeature-&gt;size() &gt;= i implies
                 redefines(supertype.endFeature-&gt;at(i))
 direction = null and
 ownedSpecializations-&gt;forAll(isImplied) implies
     ownedMembership-&gt;
         selectByKind(FeatureValue)-&gt;
         forAll(fv | specializes(fv.value.result))
 isEnd and owningType &lt;&gt; null and
 (owningType.oclIsKindOf(Association) or
  owningType.oclIsKindOf(Connector)) implies
     specializesFromLibrary('Links::Link::participant')
 isComposite and
 ownedTyping.type-&gt;includes(oclIsKindOf(Structure)) and
 owningType &lt;&gt; null and
 (owningType.oclIsKindOf(Structure) or
  owningType.type-&gt;includes(oclIsKindOf(Structure))) implies
     specializesFromLibrary('Occurrence::Occurrence::suboccurrences')
 ownedTyping.type-&gt;exists(selectByKind(Class)) implies
     specializesFromLibrary('Occurrences::occurrences')
 isComposite and
 ownedTyping.type-&gt;includes(oclIsKindOf(Class)) and
 owningType &lt;&gt; null and
 (owningType.oclIsKindOf(Class) or
  owningType.oclIsKindOf(Feature) and
     owningType.oclAsType(Feature).type-&gt;
         exists(oclIsKindOf(Class))) implies
     specializesFromLibrary('Occurrence::Occurrence::suboccurrences')
 ownedTyping.type-&gt;exists(selectByKind(DataType)) implies
     specializesFromLibrary('Base::dataValues')
 owningType &lt;&gt; null and
 owningType.oclIsKindOf(FlowEnd) and
 owningType.ownedFeature-&gt;at(1) = self implies
     let flowType : Type = owningType.owningType in
     flowType &lt;&gt; null implies
         let i : Integer = 
             flowType.ownedFeature.indexOf(owningType) in
         (i = 1 implies 
             redefinesFromLibrary('Transfers::Transfer::source::sourceOutput')) and
         (i = 2 implies
             redefinesFromLibrary('Transfers::Transfer::source::targetInput'))
                  
 owningType &lt;&gt; null and
 not owningFeatureMembership.
     oclIsKindOf(ReturnParameterMembership) and
 (owningType.oclIsKindOf(Behavior) or
  owningType.oclIsKindOf(Step) and
     (owningType.oclIsKindOf(InvocationExpression) implies
       not ownedRedefinition-&gt;exists(not isImplied)) 
 implies
     let i : Integer =
         owningType.ownedFeature-&gt;select(direction &lt;&gt; null)-&gt;
             reject(owningFeatureMembership.
                 oclIsKindOf(ReturnParameterMembership))-&gt;
             indexOf(self) in
     owningType.ownedSpecialization.general-&gt;
         forAll(supertype |
             let ownedParameters : Sequence(Feature) =
                 supertype.ownedFeature-&gt;select(direction &lt;&gt; null)-&gt;
                      reject(owningFeatureMembership.
                          oclIsKindOf(ReturnParameterMembership)) in
             ownedParameters-&gt;size() &gt;= i implies
                 redefines(ownedParameters-&gt;at(i))
 ownedTyping.type-&gt;exists(selectByKind(Structure)) implies
     specializesFromLibary('Objects::objects')
 owningType &lt;&gt; null and
 (owningType.oclIsKindOf(Function) and
     self = owningType.oclAsType(Function).result or
  owningType.oclIsKindOf(Expression) and
     self = owningType.oclAsType(Expression).result) implies
     owningType.ownedSpecialization.general-&gt;
         select(oclIsKindOf(Function) or oclIsKindOf(Expression))-&gt;
         forAll(supertype |
             redefines(
                 if superType.oclIsKindOf(Function) then
                     superType.oclAsType(Function).result
                 else
                     superType.oclAsType(Expression).result
                 endif)
 ownedFeatureInverting = ownedRelationship-&gt;selectByKind(FeatureInverting)-&gt;
     select(fi | fi.featureInverted = self)
 featuringType =
     let featuringTypes : OrderedSet(Type) = 
         featuring.type-&gt;asOrderedSet() in
     if chainingFeature-&gt;isEmpty() then featuringTypes
     else
         featuringTypes-&gt;
             union(chainingFeature-&gt;first().featuringType)-&gt;
             asOrderedSet()
     endif
 ownedReferenceSubsetting =
     let referenceSubsettings : OrderedSet(ReferenceSubsetting) =
         ownedSubsetting-&gt;selectByKind(ReferenceSubsetting) in
     if referenceSubsettings-&gt;isEmpty() then null
     else referenceSubsettings-&gt;first() endif
 ownedSubsetting-&gt;selectByKind(ReferenceSubsetting)-&gt;size() &lt;= 1
 Sequence{2..chainingFeature-&gt;size()}-&gt;forAll(i |
     chainingFeature-&gt;at(i).isFeaturedWithin(chainingFeature-&gt;at(i-1)))
 
 isPortion and
 ownedTyping.type-&gt;includes(oclIsKindOf(Class)) and
 owningType &lt;&gt; null and
 (owningType.oclIsKindOf(Class) or
  owningType.oclIsKindOf(Feature) and
     owningType.oclAsType(Feature).type-&gt;
         exists(oclIsKindOf(Class))) implies
     specializesFromLibrary('Occurrence::Occurrence::portions')
 featureTarget = if chainingFeature-&gt;isEmpty() then self else chainingFeature-&gt;last() endif
 ownedCrossSubsetting =
     let crossSubsettings: Sequence(CrossSubsetting) = 
         ownedSubsetting-&gt;selectByKind(CrossSubsetting) in
     if crossSubsettings-&gt;isEmpty() then null
     else crossSubsettings-&gt;first()
     endif
 isEnd implies 
     multiplicities().allSuperTypes()-&gt;flatten()-&gt;
     selectByKind(MultiplicityRange)-&gt;exists(hasBounds(1,1))
 crossFeature &lt;&gt; null implies
     crossFeature.type-&gt;asSet() = type-&gt;asSet()
 ownedSubsetting-&gt;selectByKind(CrossSubsetting)-&gt;size() &lt;= 1
 crossFeature =
     if ownedCrossSubsetting = null then null
     else 
         let chainingFeatures: Sequence(Feature) = 
             ownedCrossSubsetting.crossedFeature.chainingFeature in
         if chainingFeatures-&gt;size() &lt; 2 then null
         else chainingFeatures-&gt;at(2)
     endif
 isOwnedCrossFeature() implies
     owner.oclAsType(Feature).type-&gt;forAll(t | self.specializes(t))
 isOwnedCrossFeature() implies
     ownedSubsetting.subsettedFeature-&gt;includesAll(
         owner.oclAsType(Feature).ownedRedefinition.redefinedFeature-&gt;
             select(crossFeature &lt;&gt; null).crossFeature)
 crossFeature &lt;&gt; null implies
     ownedRedefinition.redefinedFeature.crossFeature-&gt;
             forAll(f | f &lt;&gt; null implies crossFeature.specializes(f))
 ownedCrossFeature() &lt;&gt; null implies
     crossFeature = ownedCrossFeature()
 isOwnedCrossFeature() implies
     let otherEnds : OrderedSet(Feature) = 
         owner.oclAsType(Feature).owningType.endFeature-&gt;excluding(self) in
     if (otherEnds-&gt;size() = 1) then
         featuringType = otherEnds-&gt;first().type
     else
         featuringType-&gt;size() = 1 and
         featuringType-&gt;first().isCartesianProduct() and
         featuringType-&gt;first().asCartesianProduct() = otherEnds.type and
         featuringType-&gt;first().allSupertypes()-&gt;includesAll(
             owner.oclAsType(Feature).ownedRedefinition.redefinedFeature-&gt;
                select(crossFeature() &lt;&gt; null).crossFeature().featuringType)      
     endif
 isPortion implies not isVariable
 isEnd implied direction = null
 owningFeatureMembership &lt;&gt; null implies
     featuringTypes-&gt;exists(t | isFeaturingType(t))
 isConstant implies isVariable
 isVariable implies
     owningType &lt;&gt; null and 
     owningType.specializes('Occurrences::Occurrence')
 isEnd implies not (isDerived or isAbstract or isComposite or isPortion)
 isEnd and isVariable implies isConstant</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#allRedefinedFeatures()">allRedefinedFeatures</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return this <code>Feature</code> and all the <code>Features</code> that are directly or indirectly <code>Redefined</code> by this <code>Feature</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#asCartesianProduct()">asCartesianProduct</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If <code>isCartesianProduct</code> is true, then return the list of <code>Types</code> whose Cartesian product can be represented by this <code>Feature</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canAccess(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">canAccess</a><wbr/>(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">A <code>Feature</code> can access another <code>feature</code> if the other <code>feature</code> is featured within one of the direct or indirect <code>featuringTypes</code> of this <code>Feature</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#directionFor(com.dassault_systemes.modeler.kerml.model.kerml.Type)">directionFor</a><wbr/>(<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the <code>directionOf</code> this <code>Feature</code> relative to the given <code>type</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#effectiveName()">effectiveName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If a <code>Feature</code> has no <code>declaredName</code> or <code>declaredShortName</code>
 , then its effective <code>name</code> is given by the effective <code>name</code> of the <code>Feature</code> returned by the <code>namingFeature()</code> operation, if any.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#effectiveShortName()">effectiveShortName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If a <code>Feature</code> has no <code>declaredShortName</code> or <code>declaredName</code>, then its effective <code>shortName</code> is given by the effective <code>shortName</code> of the <code>Feature</code> returned by the <code>namingFeature()</code> operation, if any.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getChainingFeature()">getChainingFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Feature</code> that are chained together to determine the values of this <code>Feature</code>, derived from the <code>chainingFeatures</code> of the <code>ownedFeatureChainings</code> of this <code>Feature</code>, in the same order.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCrossFeature()">getCrossFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The second <code>chainingFeature</code> of the <code>crossedFeature</code> of the <code>ownedCrossSubsetting</code> of this <code>Feature</code>, if it has one.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDirection()">getDirection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates how values of this <code>Feature</code> are determined or used (as specified for the <code>FeatureDirectionKind</code>).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEndOwningType()">getEndOwningType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Type</code> that is related to this <code>Feature</code> by an <code>EndFeatureMembership</code> in which the <code>Feature</code> is an <code>ownedMemberFeature</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFeatureTarget()">getFeatureTarget</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The last of the <code>chainingFeatures</code> of this <code>Feature</code>, if it has any.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFeaturingType()">getFeaturingType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block"><code>Types</code> that feature this <code>Feature</code>, such that any instance in the domain of the <code>Feature</code> must be classified by all of these <code>Types</code>, including at least all the <code>featuringTypes</code> of its <code>typeFeaturings</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="CrossSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CrossSubsetting</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedCrossSubsetting()">getOwnedCrossSubsetting</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The one <code>ownedSubsetting</code> of this <code>Feature</code>, if any, that is a <code>CrossSubsetting}, for which the <code>Feature</code> is the <code>crossingFeature</code>.</code></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChaining</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedFeatureChaining()">getOwnedFeatureChaining</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedRelationships</code> of this <code>Feature</code> that are <code>FeatureChainings</code>, for which the <code>Feature</code> will be the <code>featureChained</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="FeatureInverting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureInverting</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedFeatureInverting()">getOwnedFeatureInverting</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedRelationships</code> of this <code>Feature</code> that are <code>FeatureInvertings</code> and for which the <code>Feature</code> is the <code>featureInverted</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Redefinition</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedRedefinition()">getOwnedRedefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedSubsettings</code> of this <code>Feature</code> that are <code>Redefinitions</code>, for which the <code>Feature</code> is the <code>redefiningFeature</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ReferenceSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReferenceSubsetting</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedReferenceSubsetting()">getOwnedReferenceSubsetting</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The one <code>ownedSubsetting</code> of this <code>Feature</code>, if any, that is a <code>ReferenceSubsetting</code>, for which the <code>Feature</code> is the <code>referencingFeature</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedSubsetting()">getOwnedSubsetting</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedSpecializations</code> of this <code>Feature</code> that are <code>Subsettings</code>, for which the <code>Feature</code> is the <code>subsettingFeature</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="TypeFeaturing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TypeFeaturing</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedTypeFeaturing()">getOwnedTypeFeaturing</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedRelationships</code> of this <code>Feature</code> that are <code>TypeFeaturings</code> and for which the <code>Feature</code> is the <code>featureOfType</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureTyping</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedTyping()">getOwnedTyping</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedSpecializations</code> of this <code>Feature</code> that are <code>FeatureTypings</code>, for which the <code>Feature</code> is the <code>typedFeature</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningFeatureMembership()">getOwningFeatureMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>FeatureMembership</code> that owns this <code>Feature</code> as an <code>ownedMemberFeature</code>, determining its <code>owningType</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningType()">getOwningType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Type</code> that is the <code>owningType</code> of the <code>owningFeatureMembership</code> of this <code>Feature</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block"><code>Types</code> that restrict the values of this <code>Feature</code>, such that the values must be instances of all the <code>types</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isCartesianProduct()">isCartesianProduct</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check whether this <code>Feature</code> can be used to represent a Cartesian product of <code>Types</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isCompatibleWith</a><wbr/>(<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> otherType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">A <code>Feature</code> is compatible with an <code>otherType</code> if it either directly or indirectly specializes the <code>otherType</code> or if the <code>otherType</code> is also a <code>Feature</code> and all of the following are true.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isComposite()">isComposite</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether the <code>Feature</code> is a composite <code>feature</code> of its <code>featuringType</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isConstant()">isConstant</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If <code>isVariable</code> is true, then whether the value of this <code>Feature</code> nevertheless does not change over all <code><em>snapshots</em></code> of its <code>owningType</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isDerived()">isDerived</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether the values of this <code>Feature</code> can always be computed from the values of other <code>Features</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isEnd()">isEnd</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether or not this <code>Feature</code> is an end <code>Feature</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isFeaturedWithin(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isFeaturedWithin</a><wbr/>(<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return if the <code>featuringTypes</code> of this <code>Feature</code> are compatible with the given <code>type</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isFeaturingType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isFeaturingType</a><wbr/>(<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return whether the given <code>type</code> must be a <code>featuringType</code> of this <code>Feature</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isOrdered()">isOrdered</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether an order exists for the values of this <code>Feature</code> or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isOwnedCrossFeature()">isOwnedCrossFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return whether this <code>Feature</code> is an owned cross <code>Feature</code> of an end <code>Feature</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isPortion()">isPortion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether the values of this <code>Feature</code> are contained in the space and time of instances of the domain of the <code>Feature</code> and represent the same thing as those instances.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isUnique()">isUnique</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether or not values for this <code>Feature</code> must have no duplicates or not.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isVariable()">isVariable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether the value of this <code>Feature</code> might vary over time.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#namingFeature()">namingFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">By default, the naming <code>Feature</code> of a <code>Feature</code> is given by its first <code>redefinedFeature</code> of its first <code>ownedRedefinition</code>, if any.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#ownedCrossFeature()">ownedCrossFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If this <code>Feature</code> is an end <code>Feature</code> of its <code>owningType</code>, then return the first <code>ownedMember</code> of the <code>Feature</code> that is a <code>Feature</code>, but not a <code>Multiplicity</code> or a <code>MetadataFeature</code>, and whose <code>owningMembership</code> is <em>not</em> a <code>FeatureMembership</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#redefines(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">redefines</a><wbr/>(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefinedFeature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check whether this <code>Feature</code> <em>directly</em> redefines the given <code>redefinedFeature</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#redefinesFromLibrary(java.lang.String)">redefinesFromLibrary</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> libraryFeatureName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check whether this <code>Feature</code> <em>directly</em> redefines the named library <code>Feature</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)">setDirection</a><wbr/>(<a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates how values of this <code>Feature</code> are determined or used (as specified for the <code>FeatureDirectionKind</code>).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsComposite(boolean)">setIsComposite</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether the <code>Feature</code> is a composite <code>feature</code> of its <code>featuringType</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsConstant(boolean)">setIsConstant</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If <code>isVariable</code> is true, then whether the value of this <code>Feature</code> nevertheless does not change over all <code><em>snapshots</em></code> of its <code>owningType</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsDerived(boolean)">setIsDerived</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether the values of this <code>Feature</code> can always be computed from the values of other <code>Features</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsEnd(boolean)">setIsEnd</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether or not this <code>Feature</code> is an end <code>Feature</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsOrdered(boolean)">setIsOrdered</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether an order exists for the values of this <code>Feature</code> or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsPortion(boolean)">setIsPortion</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether the values of this <code>Feature</code> are contained in the space and time of instances of the domain of the <code>Feature</code> and represent the same thing as those instances.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsUnique(boolean)">setIsUnique</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether or not values for this <code>Feature</code> must have no duplicates or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsVariable(boolean)">setIsVariable</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether the value of this <code>Feature</code> might vary over time.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#subsetsChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">subsetsChain</a><wbr/>(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> first,
 <a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> second)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check whether this <code>Feature</code> directly or indirectly specializes a <code>Feature</code> whose last two <code>chainingFeatures</code> are the given <code>Features</code> <code>first</code> and <code>second</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#supertypes(boolean)">supertypes</a><wbr/>(boolean excludeImplied)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">let supertypes : OrderedSet(Type) = 
     self.oclAsType(Type).supertypes(excludeImplied) in
 if featureTarget = self then supertypes
 else supertypes-&gt;append(featureTarget)
 endif</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#typingFeatures()">typingFeatures</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the <code>Features</code> used to determine the <code>types</code> of this <code>Feature</code> (other than this <code>Feature</code> itself).</div>
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
<section class="detail" id="getOwningType()">
<h3>getOwningType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">getOwningType</span>()</div>
<div class="block"><p>The <code>Type</code> that is the <code>owningType</code> of the <code>owningFeatureMembership</code> of this <code>Feature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the owningType value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Type.html#getOwnedFeature()"><code>Type.getOwnedFeature()</code></a>
        subsets=<a href="Element.html#getOwningNamespace()"><code>Element.getOwningNamespace()</code></a>, <a href="#getFeaturingType()"><code>getFeaturingType()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUnique()">
<h3>isUnique</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isUnique</span>()</div>
<div class="block"><p>Whether or not values for this <code>Feature</code> must have no duplicates or not.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isUnique value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsUnique(boolean)">
<h3>setIsUnique</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsUnique</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether or not values for this <code>Feature</code> must have no duplicates or not.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isUnique value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOrdered()">
<h3>isOrdered</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isOrdered</span>()</div>
<div class="block"><p>Whether an order exists for the values of this <code>Feature</code> or not.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isOrdered value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsOrdered(boolean)">
<h3>setIsOrdered</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsOrdered</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether an order exists for the values of this <code>Feature</code> or not.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isOrdered value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">getType</span>()</div>
<div class="block"><p><code>Types</code> that restrict the values of this <code>Feature</code>, such that the values must be instances of all the <code>types</code>. The types of a <code>Feature</code> are derived from its <code>typings</code> and the <code>types</code> of its <code>subsettings</code>. If the <code>Feature</code> is chained, then the <code>types</code> of the last <code>Feature</code> in the chain are also <code>types</code> of the chained <code>Feature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the type value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="typedFeature"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedRedefinition()">
<h3>getOwnedRedefinition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Redefinition</a>&gt;</span> <span class="element-name">getOwnedRedefinition</span>()</div>
<div class="block"><p>The <code>ownedSubsettings</code> of this <code>Feature</code> that are <code>Redefinitions</code>, for which the <code>Feature</code> is the <code>redefiningFeature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedRedefinition value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="owningFeature"
        subsets=<a href="#getOwnedSubsetting()"><code>getOwnedSubsetting()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedSubsetting()">
<h3>getOwnedSubsetting</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a>&gt;</span> <span class="element-name">getOwnedSubsetting</span>()</div>
<div class="block"><p>The <code>ownedSpecializations</code> of this <code>Feature</code> that are <code>Subsettings</code>, for which the <code>Feature</code> is the <code>subsettingFeature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedSubsetting value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Subsetting.html#getOwningFeature()"><code>Subsetting.getOwningFeature()</code></a>
        subsets=<a href="Type.html#getOwnedSpecialization()"><code>Type.getOwnedSpecialization()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningFeatureMembership()">
<h3>getOwningFeatureMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a></span> <span class="element-name">getOwningFeatureMembership</span>()</div>
<div class="block"><p>The <code>FeatureMembership</code> that owns this <code>Feature</code> as an <code>ownedMemberFeature</code>, determining its <code>owningType</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the owningFeatureMembership value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="FeatureMembership.html#getOwnedMemberFeature()"><code>FeatureMembership.getOwnedMemberFeature()</code></a>
        subsets=<a href="Element.html#getOwningMembership()"><code>Element.getOwningMembership()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isComposite()">
<h3>isComposite</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isComposite</span>()</div>
<div class="block"><p>Whether the <code>Feature</code> is a composite <code>feature</code> of its <code>featuringType</code>. If so, the values of the <code>Feature</code> cannot exist after its featuring instance no longer does and cannot be values of another composite feature that is not on the same featuring instance.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isComposite value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsComposite(boolean)">
<h3>setIsComposite</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsComposite</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether the <code>Feature</code> is a composite <code>feature</code> of its <code>featuringType</code>. If so, the values of the <code>Feature</code> cannot exist after its featuring instance no longer does and cannot be values of another composite feature that is not on the same featuring instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isComposite value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEnd()">
<h3>isEnd</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isEnd</span>()</div>
<div class="block"><p>Whether or not this <code>Feature</code> is an end <code>Feature</code>. An end <code>Feature</code> always has multiplicity 1, mapping each of its domain instances to a single co-domain instance. However, it may have a <code>crossFeature</code>, in which case values of the <code>crossFeature</code> must be the same as those found by navigation across instances of the <code>owningType</code> from values of other end <code>Features</code> to values of this Feature. If the <code>owningType</code> has <em>n</em> end <code>Features</code>, then the multiplicity, ordering, and uniqueness declared for the <code>crossFeature</code> of any one of these end <code>Features</code> constrains the cardinality, ordering, and uniqueness of the collection of values of that <code>Feature</code> reached by navigation when the values of the other <em>n-1</em> end <code>Features</code> are held fixed.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isEnd value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsEnd(boolean)">
<h3>setIsEnd</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsEnd</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether or not this <code>Feature</code> is an end <code>Feature</code>. An end <code>Feature</code> always has multiplicity 1, mapping each of its domain instances to a single co-domain instance. However, it may have a <code>crossFeature</code>, in which case values of the <code>crossFeature</code> must be the same as those found by navigation across instances of the <code>owningType</code> from values of other end <code>Features</code> to values of this Feature. If the <code>owningType</code> has <em>n</em> end <code>Features</code>, then the multiplicity, ordering, and uniqueness declared for the <code>crossFeature</code> of any one of these end <code>Features</code> constrains the cardinality, ordering, and uniqueness of the collection of values of that <code>Feature</code> reached by navigation when the values of the other <em>n-1</em> end <code>Features</code> are held fixed.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isEnd value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEndOwningType()">
<h3>getEndOwningType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">getEndOwningType</span>()</div>
<div class="block"><p>The <code>Type</code> that is related to this <code>Feature</code> by an <code>EndFeatureMembership</code> in which the <code>Feature</code> is an <code>ownedMemberFeature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the endOwningType value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Type.html#getOwnedEndFeature()"><code>Type.getOwnedEndFeature()</code></a>
        subsets=<a href="#getOwningType()"><code>getOwningType()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedTyping()">
<h3>getOwnedTyping</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureTyping</a>&gt;</span> <span class="element-name">getOwnedTyping</span>()</div>
<div class="block"><p>The <code>ownedSpecializations</code> of this <code>Feature</code> that are <code>FeatureTypings</code>, for which the <code>Feature</code> is the <code>typedFeature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedTyping value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="FeatureTyping.html#getOwningFeature()"><code>FeatureTyping.getOwningFeature()</code></a>
        subsets=<a href="Type.html#getOwnedSpecialization()"><code>Type.getOwnedSpecialization()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeaturingType()">
<h3>getFeaturingType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">getFeaturingType</span>()</div>
<div class="block"><p><code>Types</code> that feature this <code>Feature</code>, such that any instance in the domain of the <code>Feature</code> must be classified by all of these <code>Types</code>, including at least all the <code>featuringTypes</code> of its <code>typeFeaturings</code>.  If the <code>Feature</code> is chained, then the <code>featuringTypes</code> of the first <code>Feature</code> in the chain are also <code>featuringTypes</code> of the chained <code>Feature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the featuringType value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="featureOfType"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedTypeFeaturing()">
<h3>getOwnedTypeFeaturing</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="TypeFeaturing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TypeFeaturing</a>&gt;</span> <span class="element-name">getOwnedTypeFeaturing</span>()</div>
<div class="block"><p>The <code>ownedRelationships</code> of this <code>Feature</code> that are <code>TypeFeaturings</code> and for which the <code>Feature</code> is the <code>featureOfType</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedTypeFeaturing value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="TypeFeaturing.html#getOwningFeatureOfType()"><code>TypeFeaturing.getOwningFeatureOfType()</code></a>
        subsets=<a href="Element.html#getOwnedRelationship()"><code>Element.getOwnedRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDerived()">
<h3>isDerived</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isDerived</span>()</div>
<div class="block"><p>Whether the values of this <code>Feature</code> can always be computed from the values of other <code>Features</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isDerived value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsDerived(boolean)">
<h3>setIsDerived</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsDerived</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether the values of this <code>Feature</code> can always be computed from the values of other <code>Features</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isDerived value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChainingFeature()">
<h3>getChainingFeature</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getChainingFeature</span>()</div>
<div class="block"><p>The <code>Feature</code> that are chained together to determine the values of this <code>Feature</code>, derived from the <code>chainingFeatures</code> of the <code>ownedFeatureChainings</code> of this <code>Feature</code>, in the same order. The values of a <code>Feature</code> with <code>chainingFeatures</code> are the same as values of the last <code>Feature</code> in the chain, which can be found by starting with the values of the first <code>Feature</code> (for each instance of the domain of the original <code>Feature</code>), then using each of those as domain instances to find the values of the second <code>Feature</code> in chainingFeatures, and so on, to values of the last <code>Feature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the chainingFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="chainedFeature"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedFeatureInverting()">
<h3>getOwnedFeatureInverting</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FeatureInverting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureInverting</a>&gt;</span> <span class="element-name">getOwnedFeatureInverting</span>()</div>
<div class="block"><p>The <code>ownedRelationships</code> of this <code>Feature</code> that are <code>FeatureInvertings</code> and for which the <code>Feature</code> is the <code>featureInverted</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedFeatureInverting value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="FeatureInverting.html#getOwningFeature()"><code>FeatureInverting.getOwningFeature()</code></a>
        subsets=<a href="Element.html#getOwnedRelationship()"><code>Element.getOwnedRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedFeatureChaining()">
<h3>getOwnedFeatureChaining</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChaining</a>&gt;</span> <span class="element-name">getOwnedFeatureChaining</span>()</div>
<div class="block"><p>The <code>ownedRelationships</code> of this <code>Feature</code> that are <code>FeatureChainings</code>, for which the <code>Feature</code> will be the <code>featureChained</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedFeatureChaining value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="FeatureChaining.html#getFeatureChained()"><code>FeatureChaining.getFeatureChained()</code></a>
        subsets=<a href="Element.html#getOwnedRelationship()"><code>Element.getOwnedRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPortion()">
<h3>isPortion</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isPortion</span>()</div>
<div class="block"><p>Whether the values of this <code>Feature</code> are contained in the space and time of instances of the domain of the <code>Feature</code> and represent the same thing as those instances.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isPortion value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsPortion(boolean)">
<h3>setIsPortion</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsPortion</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether the values of this <code>Feature</code> are contained in the space and time of instances of the domain of the <code>Feature</code> and represent the same thing as those instances.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isPortion value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVariable()">
<h3>isVariable</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isVariable</span>()</div>
<div class="block"><p>Whether the value of this <code>Feature</code> might vary over time. That is, whether the <code>Feature</code> may have a different value for each <em><code>snapshot</code></em> of an <code>owningType</code> that is an <em><code>Occurrence</code></em>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isVariable value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsVariable(boolean)">
<h3>setIsVariable</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsVariable</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether the value of this <code>Feature</code> might vary over time. That is, whether the <code>Feature</code> may have a different value for each <em><code>snapshot</code></em> of an <code>owningType</code> that is an <em><code>Occurrence</code></em>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isVariable value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConstant()">
<h3>isConstant</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isConstant</span>()</div>
<div class="block"><p>If <code>isVariable</code> is true, then whether the value of this <code>Feature</code> nevertheless does not change over all <code><em>snapshots</em></code> of its <code>owningType</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isConstant value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsConstant(boolean)">
<h3>setIsConstant</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsConstant</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>If <code>isVariable</code> is true, then whether the value of this <code>Feature</code> nevertheless does not change over all <code><em>snapshots</em></code> of its <code>owningType</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isConstant value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedReferenceSubsetting()">
<h3>getOwnedReferenceSubsetting</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ReferenceSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReferenceSubsetting</a></span> <span class="element-name">getOwnedReferenceSubsetting</span>()</div>
<div class="block"><p>The one <code>ownedSubsetting</code> of this <code>Feature</code>, if any, that is a <code>ReferenceSubsetting</code>, for which the <code>Feature</code> is the <code>referencingFeature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedReferenceSubsetting value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="ReferenceSubsetting.html#getReferencingFeature()"><code>ReferenceSubsetting.getReferencingFeature()</code></a>
        subsets=<a href="#getOwnedSubsetting()"><code>getOwnedSubsetting()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeatureTarget()">
<h3>getFeatureTarget</h3>
<div class="member-signature"><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getFeatureTarget</span>()</div>
<div class="block"><p>The last of the <code>chainingFeatures</code> of this <code>Feature</code>, if it has any. Otherwise, this <code>Feature</code> itself.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the featureTarget value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="baseFeature"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCrossFeature()">
<h3>getCrossFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getCrossFeature</span>()</div>
<div class="block"><p>The second <code>chainingFeature</code> of the <code>crossedFeature</code> of the <code>ownedCrossSubsetting</code> of this <code>Feature</code>, if it has one. Semantically, the values of the <code>crossFeature</code> of an end <code>Feature</code> must include all values of the end <code>Feature</code> obtained when navigating from values of the other end <code>Features</code> of the same <code>owningType</code>.
 </p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the crossFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="featureCrossing"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirection()">
<h3>getDirection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">getDirection</span>()</div>
<div class="block"><p>Indicates how values of this <code>Feature</code> are determined or used (as specified for the <code>FeatureDirectionKind</code>).</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the direction value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)">
<h3>setDirection</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDirection</span><wbr/><span class="parameters">(@CheckForNull
 <a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a> value)</span></div>
<div class="block"><p>Indicates how values of this <code>Feature</code> are determined or used (as specified for the <code>FeatureDirectionKind</code>).</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the direction value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedCrossSubsetting()">
<h3>getOwnedCrossSubsetting</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="CrossSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CrossSubsetting</a></span> <span class="element-name">getOwnedCrossSubsetting</span>()</div>
<div class="block"><p>The one <code>ownedSubsetting</code> of this <code>Feature</code>, if any, that is a <code>CrossSubsetting}, for which the <code>Feature</code> is the <code>crossingFeature</code>.</code></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedCrossSubsetting value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="CrossSubsetting.html#getCrossingFeature()"><code>CrossSubsetting.getCrossingFeature()</code></a>
        subsets=<a href="#getOwnedSubsetting()"><code>getOwnedSubsetting()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="directionFor(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>directionFor</h3>
<div class="member-signature"><span class="return-type"><a href="FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">directionFor</span><wbr/><span class="parameters">(<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block"><p>Return the <code>directionOf</code> this <code>Feature</code> relative to the given <code>type</code>.</p>
 type.directionOf(self)</div>
</section>
</li>
<li>
<section class="detail" id="effectiveShortName()">
<h3>effectiveShortName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">effectiveShortName</span>()</div>
<div class="block"><p>If a <code>Feature</code> has no <code>declaredShortName</code> or <code>declaredName</code>, then its effective <code>shortName</code> is given by the effective <code>shortName</code> of the <code>Feature</code> returned by the <code>namingFeature()</code> operation, if any.</p>
 if declaredShortName &lt;&gt; null or declaredName &lt;&gt; null then
     declaredShortName
 else
     let namingFeature : Feature = namingFeature() in
     if namingFeature = null then
         null
     else
         namingFeature.effectiveShortName()
     endif
 endif</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Element.html#effectiveShortName()">effectiveShortName</a></code> in interface <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="effectiveName()">
<h3>effectiveName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">effectiveName</span>()</div>
<div class="block"><p>If a <code>Feature</code> has no <code>declaredName</code> or <code>declaredShortName</code>
 , then its effective <code>name</code> is given by the effective <code>name</code> of the <code>Feature</code> returned by the <code>namingFeature()</code> operation, if any.</p>
 if declaredShortName &lt;&gt; null or declaredName &lt;&gt; null then
     declaredName
 else
     let namingFeature : Feature = namingFeature() in
     if namingFeature = null then
         null
     else
         namingFeature.effectiveName()
     endif
 endif</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Element.html#effectiveName()">effectiveName</a></code> in interface <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="namingFeature()">
<h3>namingFeature</h3>
<div class="member-signature"><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">namingFeature</span>()</div>
<div class="block"><p>By default, the naming <code>Feature</code> of a <code>Feature</code> is given by its first <code>redefinedFeature</code> of its first <code>ownedRedefinition</code>, if any.</p>
 if ownedRedefinition-&gt;isEmpty() then
     null
 else
     ownedRedefinition-&gt;at(1).redefinedFeature
 endif</div>
</section>
</li>
<li>
<section class="detail" id="supertypes(boolean)">
<h3>supertypes</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">supertypes</span><wbr/><span class="parameters">(boolean excludeImplied)</span></div>
<div class="block">let supertypes : OrderedSet(Type) = 
     self.oclAsType(Type).supertypes(excludeImplied) in
 if featureTarget = self then supertypes
 else supertypes-&gt;append(featureTarget)
 endif</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Type.html#supertypes(boolean)">supertypes</a></code> in interface <code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="redefines(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>redefines</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">redefines</span><wbr/><span class="parameters">(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefinedFeature)</span></div>
<div class="block"><p>Check whether this <code>Feature</code> <em>directly</em> redefines the given <code>redefinedFeature</code>.</p>
 ownedRedefinition.redefinedFeature-&gt;includes(redefinedFeature)</div>
</section>
</li>
<li>
<section class="detail" id="redefinesFromLibrary(java.lang.String)">
<h3>redefinesFromLibrary</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">redefinesFromLibrary</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> libraryFeatureName)</span></div>
<div class="block"><p>Check whether this <code>Feature</code> <em>directly</em> redefines the named library <code>Feature</code>. <code>libraryFeatureName</code> must conform to the syntax of a KerML qualified name and must resolve to a <code>Feature</code> in global scope.</p>
 let mem: Membership = resolveGlobal(libraryFeatureName) in
 mem &lt;&gt; null and mem.memberElement.oclIsKindOf(Feature) and
 redefines(mem.memberElement.oclAsType(Feature))</div>
</section>
</li>
<li>
<section class="detail" id="subsetsChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>subsetsChain</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">subsetsChain</span><wbr/><span class="parameters">(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> first,
 <a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> second)</span></div>
<div class="block"><p>Check whether this <code>Feature</code> directly or indirectly specializes a <code>Feature</code> whose last two <code>chainingFeatures</code> are the given <code>Features</code> <code>first</code> and <code>second</code>.</p>
 allSuperTypes()-&gt;selectAsKind(Feature)-&gt;
     exists(f | let n: Integer = f.chainingFeature-&gt;size() in
         n &gt;= 2 and
         f.chainingFeature-&gt;at(n-1) = first and
         f.chainingFeature-&gt;at(n) = second)</div>
</section>
</li>
<li>
<section class="detail" id="isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isCompatibleWith</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isCompatibleWith</span><wbr/><span class="parameters">(<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> otherType)</span></div>
<div class="block"><p>A <code>Feature</code> is compatible with an <code>otherType</code> if it either directly or indirectly specializes the <code>otherType</code> or if the <code>otherType</code> is also a <code>Feature</code> and all of the following are true.</p>
<ol>
<li>Neither this <code>Feature</code> or the <code>otherType</code> have any <code>ownedFeatures</code>.</li>
<li>This <code>Feature</code> directly or indirectly redefines a <code>Feature</code> that is also directly or indirectly redefined by the <code>otherType</code>.</li>
<li>This <code>Feature</code> can access the <code>otherType</code>.
 </li></ol>
 specializes(otherType) or
     supertype.oclIsKindOf(Feature) and
     ownedFeature-&gt;isEmpty() and
     otherType.ownedFeature-&gt;isEmpty() and
     ownedRedefinitions.allRedefinedFeatures()-&gt;exists(f |  
         otherType.oclAsType(Feature).allRedefinedFeatures()-&gt;includes(f)) and
     canAccess(otherType.oclAsType(Feature))</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Type.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isCompatibleWith</a></code> in interface <code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="typingFeatures()">
<h3>typingFeatures</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">typingFeatures</span>()</div>
<div class="block"><p>Return the <code>Features</code> used to determine the <code>types</code> of this <code>Feature</code> (other than this <code>Feature</code> itself). If this <code>Feature</code> is <em>not</em> conjugated, then the <code>typingFeatures</code> consist of all subsetted <code>Features</code>, <em>except</em> from <code>CrossSubsetting</code>, and the last <code>chainingFeature</code> (if any). If this <code>Feature</code> <em>is</em> conjugated, then the <code>typingFeatures</code> are only its <code>originalType</code> (if the <code>originalType</code> is a <code>Feature</code>).</p>
<p><strong>Note.</strong> <code>CrossSubsetting</code> is excluded from the determination of the <code>type</code> of a <code>Feature</code> in order to avoid circularity in the construction of implied <code>CrossSubsetting</code> relationships. The <code>validateFeatureCrossFeatureType</code> requires that the <code>crossFeature</code> of a <code>Feature</code> have the same <code>type</code> as the <code>Feature</code>.</p>
 
 if not isConjugated then
     let subsettedFeatures : OrderedSet(Feature) = 
         subsetting-&gt;reject(s | s.oclIsKindOf(CrossSubsetting)).subsettedFeatures in 
     if chainingFeature-&gt;isEmpty() or
        subsettedFeature-&gt;includes(chainingFeature-&gt;last())
     then subsettedFeatures
     else subsettedFeatures-&gt;append(chainingFeature-&gt;last())
     endif
 else if conjugator.originalType.oclIsKindOf(Feature) then
     OrderedSet{conjugator.originalType.oclAsType(Feature)}
 else OrderedSet{}
 endif endif</div>
</section>
</li>
<li>
<section class="detail" id="asCartesianProduct()">
<h3>asCartesianProduct</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">asCartesianProduct</span>()</div>
<div class="block"><p>If <code>isCartesianProduct</code> is true, then return the list of <code>Types</code> whose Cartesian product can be represented by this <code>Feature</code>. (If <code>isCartesianProduct</code> is not true, the operation will still return a valid value, it will just not represent anything useful.)</p>
 featuringType-&gt;select(t | t.owner &lt;&gt; self)-&gt;
     union(featuringType-&gt;select(t | t.owner = self)-&gt;
         selectByKind(Feature).asCartesianProduct())-&gt;
     union(type)</div>
</section>
</li>
<li>
<section class="detail" id="isCartesianProduct()">
<h3>isCartesianProduct</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isCartesianProduct</span>()</div>
<div class="block"><p>Check whether this <code>Feature</code> can be used to represent a Cartesian product of <code>Types</code>.</p>
 type-&gt;size() = 1 and
 featuringType.size() = 1 and
 (featuringType.first().owner = self implies
     featuringType.first().oclIsKindOf(Feature) and
     featuringType.first().oclAsType(Feature).isCartesianProduct())</div>
</section>
</li>
<li>
<section class="detail" id="isOwnedCrossFeature()">
<h3>isOwnedCrossFeature</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isOwnedCrossFeature</span>()</div>
<div class="block"><p>Return whether this <code>Feature</code> is an owned cross <code>Feature</code> of an end <code>Feature</code>.</p>
 owningNamespace &lt;&gt; null and 
 owningNamespace.oclIsKindOf(Feature) and 
 owningNamespace.oclAsType(Feature).ownedCrossFeature() = self</div>
</section>
</li>
<li>
<section class="detail" id="ownedCrossFeature()">
<h3>ownedCrossFeature</h3>
<div class="member-signature"><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">ownedCrossFeature</span>()</div>
<div class="block"><p>If this <code>Feature</code> is an end <code>Feature</code> of its <code>owningType</code>, then return the first <code>ownedMember</code> of the <code>Feature</code> that is a <code>Feature</code>, but not a <code>Multiplicity</code> or a <code>MetadataFeature</code>, and whose <code>owningMembership</code> is <em>not</em> a <code>FeatureMembership</code>. If this exists, it is the <code>crossFeature</code> of the end <code>Feature</code>.</p>
 if not isEnd or owningType = null then null
 else
     let ownedMemberFeatures: Sequence(Feature) =
         ownedMember-&gt;selectByKind(Feature)-&gt;
             reject(oclIsKindOf(Multiplicity) or 
                    oclIsKindOf(MetadataFeature) or
                    oclIsKindOf(FeatureValue))-&gt;
             reject(owningMembership.oclIsKindOf(FeatureMembership)) in
     if ownedMemberFeatures.isEmpty() then null
     else ownedMemberFeatures-&gt;first()
     endif</div>
</section>
</li>
<li>
<section class="detail" id="allRedefinedFeatures()">
<h3>allRedefinedFeatures</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">allRedefinedFeatures</span>()</div>
<div class="block"><p>Return this <code>Feature</code> and all the <code>Features</code> that are directly or indirectly <code>Redefined</code> by this <code>Feature</code>.</p>
 ownedRedefinition.redefinedFeature-&gt;
     closure(ownedRedefinition.redefinedFeature)-&gt;
     asOrderedSet()-&gt;prepend(self)</div>
</section>
</li>
<li>
<section class="detail" id="isFeaturedWithin(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isFeaturedWithin</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isFeaturedWithin</span><wbr/><span class="parameters">(<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block"><p>Return if the <code>featuringTypes</code> of this <code>Feature</code> are compatible with the given <code>type</code>. If <code>type</code> is null, then check if this <code>Feature</code> is explicitly or implicitly featured by <em><code>Base::Anything</code></em>. If this <code>Feature</code> has <code>isVariable = true</code>, then also consider it to be featured within its <code>owningType</code>. If this <code>Feature</code> is a feature chain whose first <code>chainingFeature</code> has <code>isVariable = true</code>, then also consider it to be featured within the <code>owningType</code> of its first <code>chainingFeature</code>.</p>
 if type = null then
     featuringType-&gt;forAll(f | f = resolveGlobal('Base::Anything').memberElement)
 else
     featuringType-&gt;forAll(f | type.isCompatibleWith(f)) or
     isVariable and type.specializes(owningType) or
     chainingFeature-&gt;notEmpty() and chainingFeature-&gt;first().isVariable and
         type.specializes(chainingFeature-&gt;first().owningType)
 endif</div>
</section>
</li>
<li>
<section class="detail" id="canAccess(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>canAccess</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canAccess</span><wbr/><span class="parameters">(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block"><p>A <code>Feature</code> can access another <code>feature</code> if the other <code>feature</code> is featured within one of the direct or indirect <code>featuringTypes</code> of this <code>Feature</code>.</p>
 let anythingType: Element =
     subsettingFeature.resolveGlobal('Base::Anything').memberElement in
 let allFeaturingTypes : Sequence(Type) =
     featuringTypes-&gt;closure(t |
         if not t.oclIsKindOf(Feature) then Sequence{}
         else
             let featuringTypes : OrderedSet(Type) = t.oclAsType(Feature).featuringType in
             if featuringTypes-&gt;isEmpty() then Sequence{anythingType}
             else featuringTypes
             endif 
         endif) in
 allFeaturingTypes-&gt;exists(t | feature.isFeaturedWithin(t))</div>
</section>
</li>
<li>
<section class="detail" id="isFeaturingType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isFeaturingType</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isFeaturingType</span><wbr/><span class="parameters">(<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block"><p>Return whether the given <code>type</code> must be a <code>featuringType</code> of this <code>Feature</code>. If this <code>Feature</code> has <code>isVariable = false</code>, then return true if the <code>type</code> is the <code>owningType</code> of the <code>Feature</code>. If <code>isVariable = true</code>, then return true if the <code>type</code> is a <code>Feature</code> representing the <em><code>snapshots</code></em> of the <code>owningType</code> of this <code>Feature</code>.</p>
 owningType &lt;&gt; null and
 if not isVariable then type = owningType
 else if owningType = resolveGlobal('Occurrences::Occurrence').memberElement then
     type = resolveGlobal('Occurrences::Occurrence::snapshots').memberElement 
 else 
     type.oclIsKindOf(Feature) and
     let feature : Feature = type.oclAsType(Feature) in
     feature.featuringType-&gt;includes(owningType) and
     feature.redefinesFromLibrary('Occurrences::Occurrence::snapshots')
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
