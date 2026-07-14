# JAVA OPENAPI: SysMLElementsFactory (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/SysMLElementsFactory.html
- source_path: `com/dassault_systemes/modeler/sysml/model/SysMLElementsFactory.html`
- source_sha256: `e3ef4113c733054b3d681398b7e370e1ef13c7eb63979882c164d9caee516683`
- captured_utc: `2026-07-14T16:45:03.075042+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Interface SysMLElementsFactory

All Superinterfaces:
`com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory`, `[KerMLElementsFactory](../../kerml/model/KerMLElementsFactory.html)`

All Known Subinterfaces:
`[ElementsFactory](ElementsFactory.html)`

@OpenApiAllpublic interfaceSysMLElementsFactoryextends [KerMLElementsFactory](../../kerml/model/KerMLElementsFactory.html)

Factory for creating SysML model elements.

Extends the KerML factory with SysML-specific elements such as definitions,
 usages, actions, requirements, ports, and more.

Use **Definition** elements (e.g., `PartDefinition`) to describe types,
 and **Usage** elements (e.g., `PartUsage`) to represent instances or
 occurrences of those types in a model.

All created elements are automatically initialized and ready to be owned
 (e.g., added to a namespace or connected via memberships).

In most cases, obtain the factory via `ElementsFactory.get(project)`.

**Typical usage:**

````java
ElementsFactory factory = ElementsFactory.get(project);

 PartDefinition partDef = factory.createPartDefinition();
 PartUsage part = factory.createPartUsage();
````

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsDefault Methods
Modifier and Type
Method
Description
`default <T extends [Element](../../kerml/model/kerml/Element.html)> 
T`
`[create](#create(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> aClass)`

`default [AcceptActionUsage](sysml/AcceptActionUsage.html)`
`[createAcceptActionUsage](#createAcceptActionUsage())()`
Returns a new object of class '*Accept Action Usage*'.
`default [ActionDefinition](sysml/ActionDefinition.html)`
`[createActionDefinition](#createActionDefinition())()`
Returns a new object of class '*Action Definition*'.
`default [ActionUsage](sysml/ActionUsage.html)`
`[createActionUsage](#createActionUsage())()`
Returns a new object of class '*Action Usage*'.
`default [ActorMembership](sysml/ActorMembership.html)`
`[createActorMembership](#createActorMembership())()`
Returns a new object of class '*Actor Membership*'.
`default [AllocationDefinition](sysml/AllocationDefinition.html)`
`[createAllocationDefinition](#createAllocationDefinition())()`
Returns a new object of class '*Allocation Definition*'.
`default [AllocationUsage](sysml/AllocationUsage.html)`
`[createAllocationUsage](#createAllocationUsage())()`
Returns a new object of class '*Allocation Usage*'.
`default [AnalysisCaseDefinition](sysml/AnalysisCaseDefinition.html)`
`[createAnalysisCaseDefinition](#createAnalysisCaseDefinition())()`
Returns a new object of class '*Analysis Case Definition*'.
`default [AnalysisCaseUsage](sysml/AnalysisCaseUsage.html)`
`[createAnalysisCaseUsage](#createAnalysisCaseUsage())()`
Returns a new object of class '*Analysis Case Usage*'.
`default [AssertConstraintUsage](sysml/AssertConstraintUsage.html)`
`[createAssertConstraintUsage](#createAssertConstraintUsage())()`
Returns a new object of class '*Assert Constraint Usage*'.
`default [AssignmentActionUsage](sysml/AssignmentActionUsage.html)`
`[createAssignmentActionUsage](#createAssignmentActionUsage())()`
Returns a new object of class '*Assignment Action Usage*'.
`default [AttributeDefinition](sysml/AttributeDefinition.html)`
`[createAttributeDefinition](#createAttributeDefinition())()`
Returns a new object of class '*Attribute Definition*'.
`default [AttributeUsage](sysml/AttributeUsage.html)`
`[createAttributeUsage](#createAttributeUsage())()`
Returns a new object of class '*Attribute Usage*'.
`default [BindingConnectorAsUsage](sysml/BindingConnectorAsUsage.html)`
`[createBindingConnectorAsUsage](#createBindingConnectorAsUsage())()`
Returns a new object of class '*Binding Connector As Usage*'.
`default [CalculationDefinition](sysml/CalculationDefinition.html)`
`[createCalculationDefinition](#createCalculationDefinition())()`
Returns a new object of class '*Calculation Definition*'.
`default [CalculationUsage](sysml/CalculationUsage.html)`
`[createCalculationUsage](#createCalculationUsage())()`
Returns a new object of class '*Calculation Usage*'.
`default [CaseDefinition](sysml/CaseDefinition.html)`
`[createCaseDefinition](#createCaseDefinition())()`
Returns a new object of class '*Case Definition*'.
`default [CaseUsage](sysml/CaseUsage.html)`
`[createCaseUsage](#createCaseUsage())()`
Returns a new object of class '*Case Usage*'.
`default [ConcernDefinition](sysml/ConcernDefinition.html)`
`[createConcernDefinition](#createConcernDefinition())()`
Returns a new object of class '*Concern Definition*'.
`default [ConcernUsage](sysml/ConcernUsage.html)`
`[createConcernUsage](#createConcernUsage())()`
Returns a new object of class '*Concern Usage*'.
`default [ConjugatedPortDefinition](sysml/ConjugatedPortDefinition.html)`
`[createConjugatedPortDefinition](#createConjugatedPortDefinition())()`
Returns a new object of class '*Conjugated Port Definition*'.
`default [ConjugatedPortTyping](sysml/ConjugatedPortTyping.html)`
`[createConjugatedPortTyping](#createConjugatedPortTyping())()`
Returns a new object of class '*Conjugated Port Typing*'.
`default [ConnectionDefinition](sysml/ConnectionDefinition.html)`
`[createConnectionDefinition](#createConnectionDefinition())()`
Returns a new object of class '*Connection Definition*'.
`default [ConnectionUsage](sysml/ConnectionUsage.html)`
`[createConnectionUsage](#createConnectionUsage())()`
Returns a new object of class '*Connection Usage*'.
`default [ConstraintDefinition](sysml/ConstraintDefinition.html)`
`[createConstraintDefinition](#createConstraintDefinition())()`
Returns a new object of class '*Constraint Definition*'.
`default [ConstraintUsage](sysml/ConstraintUsage.html)`
`[createConstraintUsage](#createConstraintUsage())()`
Returns a new object of class '*Constraint Usage*'.
`default [DecisionNode](sysml/DecisionNode.html)`
`[createDecisionNode](#createDecisionNode())()`
Returns a new object of class '*Decision Node*'.
`default [Definition](sysml/Definition.html)`
`[createDefinition](#createDefinition())()`
Returns a new object of class '*Definition*'.
`default [EnumerationDefinition](sysml/EnumerationDefinition.html)`
`[createEnumerationDefinition](#createEnumerationDefinition())()`
Returns a new object of class '*Enumeration Definition*'.
`default [EnumerationUsage](sysml/EnumerationUsage.html)`
`[createEnumerationUsage](#createEnumerationUsage())()`
Returns a new object of class '*Enumeration Usage*'.
`default [EventOccurrenceUsage](sysml/EventOccurrenceUsage.html)`
`[createEventOccurrenceUsage](#createEventOccurrenceUsage())()`
Returns a new object of class '*Event Occurrence Usage*'.
`default [ExhibitStateUsage](sysml/ExhibitStateUsage.html)`
`[createExhibitStateUsage](#createExhibitStateUsage())()`
Returns a new object of class '*Exhibit State Usage*'.
`default [FlowDefinition](sysml/FlowDefinition.html)`
`[createFlowDefinition](#createFlowDefinition())()`
Returns a new object of class '*Flow Definition*'.
`default [FlowUsage](sysml/FlowUsage.html)`
`[createFlowUsage](#createFlowUsage())()`
Returns a new object of class '*Flow Usage*'.
`default [ForkNode](sysml/ForkNode.html)`
`[createForkNode](#createForkNode())()`
Returns a new object of class '*Fork Node*'.
`default [ForLoopActionUsage](sysml/ForLoopActionUsage.html)`
`[createForLoopActionUsage](#createForLoopActionUsage())()`
Returns a new object of class '*For Loop Action Usage*'.
`default [FramedConcernMembership](sysml/FramedConcernMembership.html)`
`[createFramedConcernMembership](#createFramedConcernMembership())()`
Returns a new object of class '*Framed Concern Membership*'.
`default [IfActionUsage](sysml/IfActionUsage.html)`
`[createIfActionUsage](#createIfActionUsage())()`
Returns a new object of class '*If Action Usage*'.
`default [IncludeUseCaseUsage](sysml/IncludeUseCaseUsage.html)`
`[createIncludeUseCaseUsage](#createIncludeUseCaseUsage())()`
Returns a new object of class '*Include Use Case Usage*'.
`default [InterfaceDefinition](sysml/InterfaceDefinition.html)`
`[createInterfaceDefinition](#createInterfaceDefinition())()`
Returns a new object of class '*Interface Definition*'.
`default [InterfaceUsage](sysml/InterfaceUsage.html)`
`[createInterfaceUsage](#createInterfaceUsage())()`
Returns a new object of class '*Interface Usage*'.
`default [ItemDefinition](sysml/ItemDefinition.html)`
`[createItemDefinition](#createItemDefinition())()`
Returns a new object of class '*Item Definition*'.
`default [ItemUsage](sysml/ItemUsage.html)`
`[createItemUsage](#createItemUsage())()`
Returns a new object of class '*Item Usage*'.
`default [JoinNode](sysml/JoinNode.html)`
`[createJoinNode](#createJoinNode())()`
Returns a new object of class '*Join Node*'.
`default [MembershipExpose](sysml/MembershipExpose.html)`
`[createMembershipExpose](#createMembershipExpose())()`
Returns a new object of class '*Membership Expose*'.
`default [MergeNode](sysml/MergeNode.html)`
`[createMergeNode](#createMergeNode())()`
Returns a new object of class '*Merge Node*'.
`default [MetadataDefinition](sysml/MetadataDefinition.html)`
`[createMetadataDefinition](#createMetadataDefinition())()`
Returns a new object of class '*Metadata Definition*'.
`default [MetadataUsage](sysml/MetadataUsage.html)`
`[createMetadataUsage](#createMetadataUsage())()`
Returns a new object of class '*Metadata Usage*'.
`default [NamespaceExpose](sysml/NamespaceExpose.html)`
`[createNamespaceExpose](#createNamespaceExpose())()`
Returns a new object of class '*Namespace Expose*'.
`default [ObjectiveMembership](sysml/ObjectiveMembership.html)`
`[createObjectiveMembership](#createObjectiveMembership())()`
Returns a new object of class '*Objective Membership*'.
`default [OccurrenceDefinition](sysml/OccurrenceDefinition.html)`
`[createOccurrenceDefinition](#createOccurrenceDefinition())()`
Returns a new object of class '*Occurrence Definition*'.
`default [OccurrenceUsage](sysml/OccurrenceUsage.html)`
`[createOccurrenceUsage](#createOccurrenceUsage())()`
Returns a new object of class '*Occurrence Usage*'.
`default [PartDefinition](sysml/PartDefinition.html)`
`[createPartDefinition](#createPartDefinition())()`
Returns a new object of class '*Part Definition*'.
`default [PartUsage](sysml/PartUsage.html)`
`[createPartUsage](#createPartUsage())()`
Returns a new object of class '*Part Usage*'.
`default [PerformActionUsage](sysml/PerformActionUsage.html)`
`[createPerformActionUsage](#createPerformActionUsage())()`
Returns a new object of class '*Perform Action Usage*'.
`default [PortConjugation](sysml/PortConjugation.html)`
`[createPortConjugation](#createPortConjugation())()`
Returns a new object of class '*Port Conjugation*'.
`default [PortDefinition](sysml/PortDefinition.html)`
`[createPortDefinition](#createPortDefinition())()`
Returns a new object of class '*Port Definition*'.
`default [PortUsage](sysml/PortUsage.html)`
`[createPortUsage](#createPortUsage())()`
Returns a new object of class '*Port Usage*'.
`default [ReferenceUsage](sysml/ReferenceUsage.html)`
`[createReferenceUsage](#createReferenceUsage())()`
Returns a new object of class '*Reference Usage*'.
`default [RenderingDefinition](sysml/RenderingDefinition.html)`
`[createRenderingDefinition](#createRenderingDefinition())()`
Returns a new object of class '*Rendering Definition*'.
`default [RenderingUsage](sysml/RenderingUsage.html)`
`[createRenderingUsage](#createRenderingUsage())()`
Returns a new object of class '*Rendering Usage*'.
`default [RequirementConstraintMembership](sysml/RequirementConstraintMembership.html)`
`[createRequirementConstraintMembership](#createRequirementConstraintMembership())()`
Returns a new object of class '*Requirement Constraint Membership*'.
`default [RequirementDefinition](sysml/RequirementDefinition.html)`
`[createRequirementDefinition](#createRequirementDefinition())()`
Returns a new object of class '*Requirement Definition*'.
`default [RequirementUsage](sysml/RequirementUsage.html)`
`[createRequirementUsage](#createRequirementUsage())()`
Returns a new object of class '*Requirement Usage*'.
`default [RequirementVerificationMembership](sysml/RequirementVerificationMembership.html)`
`[createRequirementVerificationMembership](#createRequirementVerificationMembership())()`
Returns a new object of class '*Requirement Verification Membership*'.
`default [SatisfyRequirementUsage](sysml/SatisfyRequirementUsage.html)`
`[createSatisfyRequirementUsage](#createSatisfyRequirementUsage())()`
Returns a new object of class '*Satisfy Requirement Usage*'.
`default [SendActionUsage](sysml/SendActionUsage.html)`
`[createSendActionUsage](#createSendActionUsage())()`
Returns a new object of class '*Send Action Usage*'.
`default [StakeholderMembership](sysml/StakeholderMembership.html)`
`[createStakeholderMembership](#createStakeholderMembership())()`
Returns a new object of class '*Stakeholder Membership*'.
`default [StateDefinition](sysml/StateDefinition.html)`
`[createStateDefinition](#createStateDefinition())()`
Returns a new object of class '*State Definition*'.
`default [StateSubactionMembership](sysml/StateSubactionMembership.html)`
`[createStateSubactionMembership](#createStateSubactionMembership())()`
Returns a new object of class '*State Subaction Membership*'.
`default [StateUsage](sysml/StateUsage.html)`
`[createStateUsage](#createStateUsage())()`
Returns a new object of class '*State Usage*'.
`default [SubjectMembership](sysml/SubjectMembership.html)`
`[createSubjectMembership](#createSubjectMembership())()`
Returns a new object of class '*Subject Membership*'.
`default [SuccessionAsUsage](sysml/SuccessionAsUsage.html)`
`[createSuccessionAsUsage](#createSuccessionAsUsage())()`
Returns a new object of class '*Succession As Usage*'.
`default [SuccessionFlowUsage](sysml/SuccessionFlowUsage.html)`
`[createSuccessionFlowUsage](#createSuccessionFlowUsage())()`
Returns a new object of class '*Succession Flow Usage*'.
`default [TerminateActionUsage](sysml/TerminateActionUsage.html)`
`[createTerminateActionUsage](#createTerminateActionUsage())()`
Returns a new object of class '*Terminate Action Usage*'.
`default [TransitionFeatureMembership](sysml/TransitionFeatureMembership.html)`
`[createTransitionFeatureMembership](#createTransitionFeatureMembership())()`
Returns a new object of class '*Transition Feature Membership*'.
`default [TransitionUsage](sysml/TransitionUsage.html)`
`[createTransitionUsage](#createTransitionUsage())()`
Returns a new object of class '*Transition Usage*'.
`default [TriggerInvocationExpression](sysml/TriggerInvocationExpression.html)`
`[createTriggerInvocationExpression](#createTriggerInvocationExpression())()`
Returns a new object of class '*Trigger Invocation Expression*'.
`default [Usage](sysml/Usage.html)`
`[createUsage](#createUsage())()`
Returns a new object of class '*Usage*'.
`default [UseCaseDefinition](sysml/UseCaseDefinition.html)`
`[createUseCaseDefinition](#createUseCaseDefinition())()`
Returns a new object of class '*Use Case Definition*'.
`default [UseCaseUsage](sysml/UseCaseUsage.html)`
`[createUseCaseUsage](#createUseCaseUsage())()`
Returns a new object of class '*Use Case Usage*'.
`default [VariantMembership](sysml/VariantMembership.html)`
`[createVariantMembership](#createVariantMembership())()`
Returns a new object of class '*Variant Membership*'.
`default [VerificationCaseDefinition](sysml/VerificationCaseDefinition.html)`
`[createVerificationCaseDefinition](#createVerificationCaseDefinition())()`
Returns a new object of class '*Verification Case Definition*'.
`default [VerificationCaseUsage](sysml/VerificationCaseUsage.html)`
`[createVerificationCaseUsage](#createVerificationCaseUsage())()`
Returns a new object of class '*Verification Case Usage*'.
`default [ViewDefinition](sysml/ViewDefinition.html)`
`[createViewDefinition](#createViewDefinition())()`
Returns a new object of class '*View Definition*'.
`default [ViewpointDefinition](sysml/ViewpointDefinition.html)`
`[createViewpointDefinition](#createViewpointDefinition())()`
Returns a new object of class '*Viewpoint Definition*'.
`default [ViewpointUsage](sysml/ViewpointUsage.html)`
`[createViewpointUsage](#createViewpointUsage())()`
Returns a new object of class '*Viewpoint Usage*'.
`default [ViewRenderingMembership](sysml/ViewRenderingMembership.html)`
`[createViewRenderingMembership](#createViewRenderingMembership())()`
Returns a new object of class '*View Rendering Membership*'.
`default [ViewUsage](sysml/ViewUsage.html)`
`[createViewUsage](#createViewUsage())()`
Returns a new object of class '*View Usage*'.
`default [WhileLoopActionUsage](sysml/WhileLoopActionUsage.html)`
`[createWhileLoopActionUsage](#createWhileLoopActionUsage())()`
Returns a new object of class '*While Loop Action Usage*'.
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory
`create, initializeElement`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.[KerMLElementsFactory](../../kerml/model/KerMLElementsFactory.html)
`[createAnnotatingElement](../../kerml/model/KerMLElementsFactory.html#createAnnotatingElement()), [createAnnotation](../../kerml/model/KerMLElementsFactory.html#createAnnotation()), [createAssociation](../../kerml/model/KerMLElementsFactory.html#createAssociation()), [createAssociationStructure](../../kerml/model/KerMLElementsFactory.html#createAssociationStructure()), [createBehavior](../../kerml/model/KerMLElementsFactory.html#createBehavior()), [createBindingConnector](../../kerml/model/KerMLElementsFactory.html#createBindingConnector()), [createBooleanExpression](../../kerml/model/KerMLElementsFactory.html#createBooleanExpression()), [createClass](../../kerml/model/KerMLElementsFactory.html#createClass()), [createClassifier](../../kerml/model/KerMLElementsFactory.html#createClassifier()), [createCollectExpression](../../kerml/model/KerMLElementsFactory.html#createCollectExpression()), [createComment](../../kerml/model/KerMLElementsFactory.html#createComment()), [createConjugation](../../kerml/model/KerMLElementsFactory.html#createConjugation()), [createConnector](../../kerml/model/KerMLElementsFactory.html#createConnector()), [createConstructorExpression](../../kerml/model/KerMLElementsFactory.html#createConstructorExpression()), [createCrossSubsetting](../../kerml/model/KerMLElementsFactory.html#createCrossSubsetting()), [createDataType](../../kerml/model/KerMLElementsFactory.html#createDataType()), [createDependency](../../kerml/model/KerMLElementsFactory.html#createDependency()), [createDifferencing](../../kerml/model/KerMLElementsFactory.html#createDifferencing()), [createDisjoining](../../kerml/model/KerMLElementsFactory.html#createDisjoining()), [createDocumentation](../../kerml/model/KerMLElementsFactory.html#createDocumentation()), [createElementFilterMembership](../../kerml/model/KerMLElementsFactory.html#createElementFilterMembership()), [createEndFeatureMembership](../../kerml/model/KerMLElementsFactory.html#createEndFeatureMembership()), [createExpression](../../kerml/model/KerMLElementsFactory.html#createExpression()), [createFeature](../../kerml/model/KerMLElementsFactory.html#createFeature()), [createFeatureChainExpression](../../kerml/model/KerMLElementsFactory.html#createFeatureChainExpression()), [createFeatureChaining](../../kerml/model/KerMLElementsFactory.html#createFeatureChaining()), [createFeatureInverting](../../kerml/model/KerMLElementsFactory.html#createFeatureInverting()), [createFeatureMembership](../../kerml/model/KerMLElementsFactory.html#createFeatureMembership()), [createFeatureReferenceExpression](../../kerml/model/KerMLElementsFactory.html#createFeatureReferenceExpression()), [createFeatureTyping](../../kerml/model/KerMLElementsFactory.html#createFeatureTyping()), [createFeatureValue](../../kerml/model/KerMLElementsFactory.html#createFeatureValue()), [createFlow](../../kerml/model/KerMLElementsFactory.html#createFlow()), [createFlowEnd](../../kerml/model/KerMLElementsFactory.html#createFlowEnd()), [createFunction](../../kerml/model/KerMLElementsFactory.html#createFunction()), [createIndexExpression](../../kerml/model/KerMLElementsFactory.html#createIndexExpression()), [createInteraction](../../kerml/model/KerMLElementsFactory.html#createInteraction()), [createIntersecting](../../kerml/model/KerMLElementsFactory.html#createIntersecting()), [createInvariant](../../kerml/model/KerMLElementsFactory.html#createInvariant()), [createInvocationExpression](../../kerml/model/KerMLElementsFactory.html#createInvocationExpression()), [createLibraryPackage](../../kerml/model/KerMLElementsFactory.html#createLibraryPackage()), [createLiteralBoolean](../../kerml/model/KerMLElementsFactory.html#createLiteralBoolean()), [createLiteralExpression](../../kerml/model/KerMLElementsFactory.html#createLiteralExpression()), [createLiteralInfinity](../../kerml/model/KerMLElementsFactory.html#createLiteralInfinity()), [createLiteralInteger](../../kerml/model/KerMLElementsFactory.html#createLiteralInteger()), [createLiteralRational](../../kerml/model/KerMLElementsFactory.html#createLiteralRational()), [createLiteralString](../../kerml/model/KerMLElementsFactory.html#createLiteralString()), [createMembership](../../kerml/model/KerMLElementsFactory.html#createMembership()), [createMembershipImport](../../kerml/model/KerMLElementsFactory.html#createMembershipImport()), [createMetaclass](../../kerml/model/KerMLElementsFactory.html#createMetaclass()), [createMetadataAccessExpression](../../kerml/model/KerMLElementsFactory.html#createMetadataAccessExpression()), [createMetadataFeature](../../kerml/model/KerMLElementsFactory.html#createMetadataFeature()), [createMultiplicity](../../kerml/model/KerMLElementsFactory.html#createMultiplicity()), [createMultiplicityRange](../../kerml/model/KerMLElementsFactory.html#createMultiplicityRange()), [createNamespace](../../kerml/model/KerMLElementsFactory.html#createNamespace()), [createNamespaceImport](../../kerml/model/KerMLElementsFactory.html#createNamespaceImport()), [createNullExpression](../../kerml/model/KerMLElementsFactory.html#createNullExpression()), [createOperatorExpression](../../kerml/model/KerMLElementsFactory.html#createOperatorExpression()), [createOwningMembership](../../kerml/model/KerMLElementsFactory.html#createOwningMembership()), [createPackage](../../kerml/model/KerMLElementsFactory.html#createPackage()), [createParameterMembership](../../kerml/model/KerMLElementsFactory.html#createParameterMembership()), [createPayloadFeature](../../kerml/model/KerMLElementsFactory.html#createPayloadFeature()), [createPredicate](../../kerml/model/KerMLElementsFactory.html#createPredicate()), [createRedefinition](../../kerml/model/KerMLElementsFactory.html#createRedefinition()), [createReferenceSubsetting](../../kerml/model/KerMLElementsFactory.html#createReferenceSubsetting()), [createResultExpressionMembership](../../kerml/model/KerMLElementsFactory.html#createResultExpressionMembership()), [createReturnParameterMembership](../../kerml/model/KerMLElementsFactory.html#createReturnParameterMembership()), [createSelectExpression](../../kerml/model/KerMLElementsFactory.html#createSelectExpression()), [createSpecialization](../../kerml/model/KerMLElementsFactory.html#createSpecialization()), [createStep](../../kerml/model/KerMLElementsFactory.html#createStep()), [createStructure](../../kerml/model/KerMLElementsFactory.html#createStructure()), [createSubclassification](../../kerml/model/KerMLElementsFactory.html#createSubclassification()), [createSubsetting](../../kerml/model/KerMLElementsFactory.html#createSubsetting()), [createSuccession](../../kerml/model/KerMLElementsFactory.html#createSuccession()), [createSuccessionFlow](../../kerml/model/KerMLElementsFactory.html#createSuccessionFlow()), [createTextualRepresentation](../../kerml/model/KerMLElementsFactory.html#createTextualRepresentation()), [createType](../../kerml/model/KerMLElementsFactory.html#createType()), [createTypeFeaturing](../../kerml/model/KerMLElementsFactory.html#createTypeFeaturing()), [createUnioning](../../kerml/model/KerMLElementsFactory.html#createUnioning())`

============ METHOD DETAIL ========== 
Method Details
createAcceptActionUsage
default [AcceptActionUsage](sysml/AcceptActionUsage.html) createAcceptActionUsage()
Returns a new object of class '*Accept Action Usage*'.
Returns:
a new object of class '*Accept Action Usage*'.
createActionDefinition
default [ActionDefinition](sysml/ActionDefinition.html) createActionDefinition()
Returns a new object of class '*Action Definition*'.
Returns:
a new object of class '*Action Definition*'.
createActionUsage
default [ActionUsage](sysml/ActionUsage.html) createActionUsage()
Returns a new object of class '*Action Usage*'.
Returns:
a new object of class '*Action Usage*'.
createActorMembership
default [ActorMembership](sysml/ActorMembership.html) createActorMembership()
Returns a new object of class '*Actor Membership*'.
Returns:
a new object of class '*Actor Membership*'.
createAllocationDefinition
default [AllocationDefinition](sysml/AllocationDefinition.html) createAllocationDefinition()
Returns a new object of class '*Allocation Definition*'.
Returns:
a new object of class '*Allocation Definition*'.
createAllocationUsage
default [AllocationUsage](sysml/AllocationUsage.html) createAllocationUsage()
Returns a new object of class '*Allocation Usage*'.
Returns:
a new object of class '*Allocation Usage*'.
createAnalysisCaseDefinition
default [AnalysisCaseDefinition](sysml/AnalysisCaseDefinition.html) createAnalysisCaseDefinition()
Returns a new object of class '*Analysis Case Definition*'.
Returns:
a new object of class '*Analysis Case Definition*'.
createAnalysisCaseUsage
default [AnalysisCaseUsage](sysml/AnalysisCaseUsage.html) createAnalysisCaseUsage()
Returns a new object of class '*Analysis Case Usage*'.
Returns:
a new object of class '*Analysis Case Usage*'.
createAssertConstraintUsage
default [AssertConstraintUsage](sysml/AssertConstraintUsage.html) createAssertConstraintUsage()
Returns a new object of class '*Assert Constraint Usage*'.
Returns:
a new object of class '*Assert Constraint Usage*'.
createAssignmentActionUsage
default [AssignmentActionUsage](sysml/AssignmentActionUsage.html) createAssignmentActionUsage()
Returns a new object of class '*Assignment Action Usage*'.
Returns:
a new object of class '*Assignment Action Usage*'.
createAttributeDefinition
default [AttributeDefinition](sysml/AttributeDefinition.html) createAttributeDefinition()
Returns a new object of class '*Attribute Definition*'.
Returns:
a new object of class '*Attribute Definition*'.
createAttributeUsage
default [AttributeUsage](sysml/AttributeUsage.html) createAttributeUsage()
Returns a new object of class '*Attribute Usage*'.
Returns:
a new object of class '*Attribute Usage*'.
createBindingConnectorAsUsage
default [BindingConnectorAsUsage](sysml/BindingConnectorAsUsage.html) createBindingConnectorAsUsage()
Returns a new object of class '*Binding Connector As Usage*'.
Returns:
a new object of class '*Binding Connector As Usage*'.
createCalculationDefinition
default [CalculationDefinition](sysml/CalculationDefinition.html) createCalculationDefinition()
Returns a new object of class '*Calculation Definition*'.
Returns:
a new object of class '*Calculation Definition*'.
createCalculationUsage
default [CalculationUsage](sysml/CalculationUsage.html) createCalculationUsage()
Returns a new object of class '*Calculation Usage*'.
Returns:
a new object of class '*Calculation Usage*'.
createCaseDefinition
default [CaseDefinition](sysml/CaseDefinition.html) createCaseDefinition()
Returns a new object of class '*Case Definition*'.
Returns:
a new object of class '*Case Definition*'.
createCaseUsage
default [CaseUsage](sysml/CaseUsage.html) createCaseUsage()
Returns a new object of class '*Case Usage*'.
Returns:
a new object of class '*Case Usage*'.
createConcernDefinition
default [ConcernDefinition](sysml/ConcernDefinition.html) createConcernDefinition()
Returns a new object of class '*Concern Definition*'.
Returns:
a new object of class '*Concern Definition*'.
createConcernUsage
default [ConcernUsage](sysml/ConcernUsage.html) createConcernUsage()
Returns a new object of class '*Concern Usage*'.
Returns:
a new object of class '*Concern Usage*'.
createConjugatedPortDefinition
default [ConjugatedPortDefinition](sysml/ConjugatedPortDefinition.html) createConjugatedPortDefinition()
Returns a new object of class '*Conjugated Port Definition*'.
Returns:
a new object of class '*Conjugated Port Definition*'.
createConjugatedPortTyping
default [ConjugatedPortTyping](sysml/ConjugatedPortTyping.html) createConjugatedPortTyping()
Returns a new object of class '*Conjugated Port Typing*'.
Returns:
a new object of class '*Conjugated Port Typing*'.
createConnectionDefinition
default [ConnectionDefinition](sysml/ConnectionDefinition.html) createConnectionDefinition()
Returns a new object of class '*Connection Definition*'.
Returns:
a new object of class '*Connection Definition*'.
createConnectionUsage
default [ConnectionUsage](sysml/ConnectionUsage.html) createConnectionUsage()
Returns a new object of class '*Connection Usage*'.
Returns:
a new object of class '*Connection Usage*'.
createConstraintDefinition
default [ConstraintDefinition](sysml/ConstraintDefinition.html) createConstraintDefinition()
Returns a new object of class '*Constraint Definition*'.
Returns:
a new object of class '*Constraint Definition*'.
createConstraintUsage
default [ConstraintUsage](sysml/ConstraintUsage.html) createConstraintUsage()
Returns a new object of class '*Constraint Usage*'.
Returns:
a new object of class '*Constraint Usage*'.
createDecisionNode
default [DecisionNode](sysml/DecisionNode.html) createDecisionNode()
Returns a new object of class '*Decision Node*'.
Returns:
a new object of class '*Decision Node*'.
createDefinition
default [Definition](sysml/Definition.html) createDefinition()
Returns a new object of class '*Definition*'.
Returns:
a new object of class '*Definition*'.
createEnumerationDefinition
default [EnumerationDefinition](sysml/EnumerationDefinition.html) createEnumerationDefinition()
Returns a new object of class '*Enumeration Definition*'.
Returns:
a new object of class '*Enumeration Definition*'.
createEnumerationUsage
default [EnumerationUsage](sysml/EnumerationUsage.html) createEnumerationUsage()
Returns a new object of class '*Enumeration Usage*'.
Returns:
a new object of class '*Enumeration Usage*'.
createEventOccurrenceUsage
default [EventOccurrenceUsage](sysml/EventOccurrenceUsage.html) createEventOccurrenceUsage()
Returns a new object of class '*Event Occurrence Usage*'.
Returns:
a new object of class '*Event Occurrence Usage*'.
createExhibitStateUsage
default [ExhibitStateUsage](sysml/ExhibitStateUsage.html) createExhibitStateUsage()
Returns a new object of class '*Exhibit State Usage*'.
Returns:
a new object of class '*Exhibit State Usage*'.
createFlowDefinition
default [FlowDefinition](sysml/FlowDefinition.html) createFlowDefinition()
Returns a new object of class '*Flow Definition*'.
Returns:
a new object of class '*Flow Definition*'.
createFlowUsage
default [FlowUsage](sysml/FlowUsage.html) createFlowUsage()
Returns a new object of class '*Flow Usage*'.
Returns:
a new object of class '*Flow Usage*'.
createForLoopActionUsage
default [ForLoopActionUsage](sysml/ForLoopActionUsage.html) createForLoopActionUsage()
Returns a new object of class '*For Loop Action Usage*'.
Returns:
a new object of class '*For Loop Action Usage*'.
createForkNode
default [ForkNode](sysml/ForkNode.html) createForkNode()
Returns a new object of class '*Fork Node*'.
Returns:
a new object of class '*Fork Node*'.
createFramedConcernMembership
default [FramedConcernMembership](sysml/FramedConcernMembership.html) createFramedConcernMembership()
Returns a new object of class '*Framed Concern Membership*'.
Returns:
a new object of class '*Framed Concern Membership*'.
createIfActionUsage
default [IfActionUsage](sysml/IfActionUsage.html) createIfActionUsage()
Returns a new object of class '*If Action Usage*'.
Returns:
a new object of class '*If Action Usage*'.
createIncludeUseCaseUsage
default [IncludeUseCaseUsage](sysml/IncludeUseCaseUsage.html) createIncludeUseCaseUsage()
Returns a new object of class '*Include Use Case Usage*'.
Returns:
a new object of class '*Include Use Case Usage*'.
createInterfaceDefinition
default [InterfaceDefinition](sysml/InterfaceDefinition.html) createInterfaceDefinition()
Returns a new object of class '*Interface Definition*'.
Returns:
a new object of class '*Interface Definition*'.
createInterfaceUsage
default [InterfaceUsage](sysml/InterfaceUsage.html) createInterfaceUsage()
Returns a new object of class '*Interface Usage*'.
Returns:
a new object of class '*Interface Usage*'.
createItemDefinition
default [ItemDefinition](sysml/ItemDefinition.html) createItemDefinition()
Returns a new object of class '*Item Definition*'.
Returns:
a new object of class '*Item Definition*'.
createItemUsage
default [ItemUsage](sysml/ItemUsage.html) createItemUsage()
Returns a new object of class '*Item Usage*'.
Returns:
a new object of class '*Item Usage*'.
createJoinNode
default [JoinNode](sysml/JoinNode.html) createJoinNode()
Returns a new object of class '*Join Node*'.
Returns:
a new object of class '*Join Node*'.
createMembershipExpose
default [MembershipExpose](sysml/MembershipExpose.html) createMembershipExpose()
Returns a new object of class '*Membership Expose*'.
Returns:
a new object of class '*Membership Expose*'.
createMergeNode
default [MergeNode](sysml/MergeNode.html) createMergeNode()
Returns a new object of class '*Merge Node*'.
Returns:
a new object of class '*Merge Node*'.
createMetadataDefinition
default [MetadataDefinition](sysml/MetadataDefinition.html) createMetadataDefinition()
Returns a new object of class '*Metadata Definition*'.
Returns:
a new object of class '*Metadata Definition*'.
createMetadataUsage
default [MetadataUsage](sysml/MetadataUsage.html) createMetadataUsage()
Returns a new object of class '*Metadata Usage*'.
Returns:
a new object of class '*Metadata Usage*'.
createNamespaceExpose
default [NamespaceExpose](sysml/NamespaceExpose.html) createNamespaceExpose()
Returns a new object of class '*Namespace Expose*'.
Returns:
a new object of class '*Namespace Expose*'.
createObjectiveMembership
default [ObjectiveMembership](sysml/ObjectiveMembership.html) createObjectiveMembership()
Returns a new object of class '*Objective Membership*'.
Returns:
a new object of class '*Objective Membership*'.
createOccurrenceDefinition
default [OccurrenceDefinition](sysml/OccurrenceDefinition.html) createOccurrenceDefinition()
Returns a new object of class '*Occurrence Definition*'.
Returns:
a new object of class '*Occurrence Definition*'.
createOccurrenceUsage
default [OccurrenceUsage](sysml/OccurrenceUsage.html) createOccurrenceUsage()
Returns a new object of class '*Occurrence Usage*'.
Returns:
a new object of class '*Occurrence Usage*'.
createPartDefinition
default [PartDefinition](sysml/PartDefinition.html) createPartDefinition()
Returns a new object of class '*Part Definition*'.
Returns:
a new object of class '*Part Definition*'.
createPartUsage
default [PartUsage](sysml/PartUsage.html) createPartUsage()
Returns a new object of class '*Part Usage*'.
Returns:
a new object of class '*Part Usage*'.
createPerformActionUsage
default [PerformActionUsage](sysml/PerformActionUsage.html) createPerformActionUsage()
Returns a new object of class '*Perform Action Usage*'.
Returns:
a new object of class '*Perform Action Usage*'.
createPortConjugation
default [PortConjugation](sysml/PortConjugation.html) createPortConjugation()
Returns a new object of class '*Port Conjugation*'.
Returns:
a new object of class '*Port Conjugation*'.
createPortDefinition
default [PortDefinition](sysml/PortDefinition.html) createPortDefinition()
Returns a new object of class '*Port Definition*'.
Returns:
a new object of class '*Port Definition*'.
createPortUsage
default [PortUsage](sysml/PortUsage.html) createPortUsage()
Returns a new object of class '*Port Usage*'.
Returns:
a new object of class '*Port Usage*'.
createReferenceUsage
default [ReferenceUsage](sysml/ReferenceUsage.html) createReferenceUsage()
Returns a new object of class '*Reference Usage*'.
Returns:
a new object of class '*Reference Usage*'.
createRenderingDefinition
default [RenderingDefinition](sysml/RenderingDefinition.html) createRenderingDefinition()
Returns a new object of class '*Rendering Definition*'.
Returns:
a new object of class '*Rendering Definition*'.
createRenderingUsage
default [RenderingUsage](sysml/RenderingUsage.html) createRenderingUsage()
Returns a new object of class '*Rendering Usage*'.
Returns:
a new object of class '*Rendering Usage*'.
createRequirementConstraintMembership
default [RequirementConstraintMembership](sysml/RequirementConstraintMembership.html) createRequirementConstraintMembership()
Returns a new object of class '*Requirement Constraint Membership*'.
Returns:
a new object of class '*Requirement Constraint Membership*'.
createRequirementDefinition
default [RequirementDefinition](sysml/RequirementDefinition.html) createRequirementDefinition()
Returns a new object of class '*Requirement Definition*'.
Returns:
a new object of class '*Requirement Definition*'.
createRequirementUsage
default [RequirementUsage](sysml/RequirementUsage.html) createRequirementUsage()
Returns a new object of class '*Requirement Usage*'.
Returns:
a new object of class '*Requirement Usage*'.
createRequirementVerificationMembership
default [RequirementVerificationMembership](sysml/RequirementVerificationMembership.html) createRequirementVerificationMembership()
Returns a new object of class '*Requirement Verification Membership*'.
Returns:
a new object of class '*Requirement Verification Membership*'.
createSatisfyRequirementUsage
default [SatisfyRequirementUsage](sysml/SatisfyRequirementUsage.html) createSatisfyRequirementUsage()
Returns a new object of class '*Satisfy Requirement Usage*'.
Returns:
a new object of class '*Satisfy Requirement Usage*'.
createSendActionUsage
default [SendActionUsage](sysml/SendActionUsage.html) createSendActionUsage()
Returns a new object of class '*Send Action Usage*'.
Returns:
a new object of class '*Send Action Usage*'.
createStakeholderMembership
default [StakeholderMembership](sysml/StakeholderMembership.html) createStakeholderMembership()
Returns a new object of class '*Stakeholder Membership*'.
Returns:
a new object of class '*Stakeholder Membership*'.
createStateDefinition
default [StateDefinition](sysml/StateDefinition.html) createStateDefinition()
Returns a new object of class '*State Definition*'.
Returns:
a new object of class '*State Definition*'.
createStateSubactionMembership
default [StateSubactionMembership](sysml/StateSubactionMembership.html) createStateSubactionMembership()
Returns a new object of class '*State Subaction Membership*'.
Returns:
a new object of class '*State Subaction Membership*'.
createStateUsage
default [StateUsage](sysml/StateUsage.html) createStateUsage()
Returns a new object of class '*State Usage*'.
Returns:
a new object of class '*State Usage*'.
createSubjectMembership
default [SubjectMembership](sysml/SubjectMembership.html) createSubjectMembership()
Returns a new object of class '*Subject Membership*'.
Returns:
a new object of class '*Subject Membership*'.
createSuccessionAsUsage
default [SuccessionAsUsage](sysml/SuccessionAsUsage.html) createSuccessionAsUsage()
Returns a new object of class '*Succession As Usage*'.
Returns:
a new object of class '*Succession As Usage*'.
createSuccessionFlowUsage
default [SuccessionFlowUsage](sysml/SuccessionFlowUsage.html) createSuccessionFlowUsage()
Returns a new object of class '*Succession Flow Usage*'.
Returns:
a new object of class '*Succession Flow Usage*'.
createTerminateActionUsage
default [TerminateActionUsage](sysml/TerminateActionUsage.html) createTerminateActionUsage()
Returns a new object of class '*Terminate Action Usage*'.
Returns:
a new object of class '*Terminate Action Usage*'.
createTransitionFeatureMembership
default [TransitionFeatureMembership](sysml/TransitionFeatureMembership.html) createTransitionFeatureMembership()
Returns a new object of class '*Transition Feature Membership*'.
Returns:
a new object of class '*Transition Feature Membership*'.
createTransitionUsage
default [TransitionUsage](sysml/TransitionUsage.html) createTransitionUsage()
Returns a new object of class '*Transition Usage*'.
Returns:
a new object of class '*Transition Usage*'.
createTriggerInvocationExpression
default [TriggerInvocationExpression](sysml/TriggerInvocationExpression.html) createTriggerInvocationExpression()
Returns a new object of class '*Trigger Invocation Expression*'.
Returns:
a new object of class '*Trigger Invocation Expression*'.
createUsage
default [Usage](sysml/Usage.html) createUsage()
Returns a new object of class '*Usage*'.
Returns:
a new object of class '*Usage*'.
createUseCaseDefinition
default [UseCaseDefinition](sysml/UseCaseDefinition.html) createUseCaseDefinition()
Returns a new object of class '*Use Case Definition*'.
Returns:
a new object of class '*Use Case Definition*'.
createUseCaseUsage
default [UseCaseUsage](sysml/UseCaseUsage.html) createUseCaseUsage()
Returns a new object of class '*Use Case Usage*'.
Returns:
a new object of class '*Use Case Usage*'.
createVariantMembership
default [VariantMembership](sysml/VariantMembership.html) createVariantMembership()
Returns a new object of class '*Variant Membership*'.
Returns:
a new object of class '*Variant Membership*'.
createVerificationCaseDefinition
default [VerificationCaseDefinition](sysml/VerificationCaseDefinition.html) createVerificationCaseDefinition()
Returns a new object of class '*Verification Case Definition*'.
Returns:
a new object of class '*Verification Case Definition*'.
createVerificationCaseUsage
default [VerificationCaseUsage](sysml/VerificationCaseUsage.html) createVerificationCaseUsage()
Returns a new object of class '*Verification Case Usage*'.
Returns:
a new object of class '*Verification Case Usage*'.
createViewDefinition
default [ViewDefinition](sysml/ViewDefinition.html) createViewDefinition()
Returns a new object of class '*View Definition*'.
Returns:
a new object of class '*View Definition*'.
createViewRenderingMembership
default [ViewRenderingMembership](sysml/ViewRenderingMembership.html) createViewRenderingMembership()
Returns a new object of class '*View Rendering Membership*'.
Returns:
a new object of class '*View Rendering Membership*'.
createViewUsage
default [ViewUsage](sysml/ViewUsage.html) createViewUsage()
Returns a new object of class '*View Usage*'.
Returns:
a new object of class '*View Usage*'.
createViewpointDefinition
default [ViewpointDefinition](sysml/ViewpointDefinition.html) createViewpointDefinition()
Returns a new object of class '*Viewpoint Definition*'.
Returns:
a new object of class '*Viewpoint Definition*'.
createViewpointUsage
default [ViewpointUsage](sysml/ViewpointUsage.html) createViewpointUsage()
Returns a new object of class '*Viewpoint Usage*'.
Returns:
a new object of class '*Viewpoint Usage*'.
createWhileLoopActionUsage
default [WhileLoopActionUsage](sysml/WhileLoopActionUsage.html) createWhileLoopActionUsage()
Returns a new object of class '*While Loop Action Usage*'.
Returns:
a new object of class '*While Loop Action Usage*'.
create
default <T extends [Element](../../kerml/model/kerml/Element.html)> T create([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> aClass)
Specified by:
`[create](../../kerml/model/KerMLElementsFactory.html#create(java.lang.Class))` in interface `[KerMLElementsFactory](../../kerml/model/KerMLElementsFactory.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Interface SysMLElementsFactory">Interface SysMLElementsFactory</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory</code>, <code><a href="../../kerml/model/KerMLElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLElementsFactory</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.sysml.model">ElementsFactory</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">SysMLElementsFactory</span><span class="extends-implements">
extends <a href="../../kerml/model/KerMLElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLElementsFactory</a></span></div>
<div class="block">Factory for creating SysML model elements.

 <p>Extends the KerML factory with SysML-specific elements such as definitions,
 usages, actions, requirements, ports, and more.</p>
<p>Use <b>Definition</b> elements (e.g., <code>PartDefinition</code>) to describe types,
 and <b>Usage</b> elements (e.g., <code>PartUsage</code>) to represent instances or
 occurrences of those types in a model.</p>
<p>All created elements are automatically initialized and ready to be owned
 (e.g., added to a namespace or connected via memberships).</p>
<p>In most cases, obtain the factory via <code>ElementsFactory.get(project)</code>.</p>
<p><b>Typical usage:</b></p>
<pre><code>
 ElementsFactory factory = ElementsFactory.get(project);

 PartDefinition partDef = factory.createPartDefinition();
 PartUsage part = factory.createPartUsage();
 </code></pre></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default &lt;T extends <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#create(java.lang.Class)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; aClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAcceptActionUsage()">createAcceptActionUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Accept Action Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createActionDefinition()">createActionDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Action Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createActionUsage()">createActionUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Action Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActorMembership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createActorMembership()">createActorMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Actor Membership</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAllocationDefinition()">createAllocationDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Allocation Definition</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAllocationUsage()">createAllocationUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Allocation Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAnalysisCaseDefinition()">createAnalysisCaseDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Analysis Case Definition</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAnalysisCaseUsage()">createAnalysisCaseUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Analysis Case Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssertConstraintUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAssertConstraintUsage()">createAssertConstraintUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Assert Constraint Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAssignmentActionUsage()">createAssignmentActionUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Assignment Action Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAttributeDefinition()">createAttributeDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Attribute Definition</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAttributeUsage()">createAttributeUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Attribute Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">BindingConnectorAsUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createBindingConnectorAsUsage()">createBindingConnectorAsUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Binding Connector As Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/CalculationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createCalculationDefinition()">createCalculationDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Calculation Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createCalculationUsage()">createCalculationUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Calculation Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createCaseDefinition()">createCaseDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Case Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createCaseUsage()">createCaseUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Case Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ConcernDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createConcernDefinition()">createConcernDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Concern Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createConcernUsage()">createConcernUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Concern Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createConjugatedPortDefinition()">createConjugatedPortDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Conjugated Port Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ConjugatedPortTyping.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortTyping</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createConjugatedPortTyping()">createConjugatedPortTyping</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Conjugated Port Typing</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createConnectionDefinition()">createConnectionDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Connection Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createConnectionUsage()">createConnectionUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Connection Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createConstraintDefinition()">createConstraintDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Constraint Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createConstraintUsage()">createConstraintUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Constraint Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/DecisionNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">DecisionNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createDecisionNode()">createDecisionNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Decision Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createDefinition()">createDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Definition</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createEnumerationDefinition()">createEnumerationDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Enumeration Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createEnumerationUsage()">createEnumerationUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Enumeration Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/EventOccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EventOccurrenceUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createEventOccurrenceUsage()">createEventOccurrenceUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Event Occurrence Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ExhibitStateUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createExhibitStateUsage()">createExhibitStateUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Exhibit State Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFlowDefinition()">createFlowDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Flow Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFlowUsage()">createFlowUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Flow Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ForkNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForkNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createForkNode()">createForkNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Fork Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createForLoopActionUsage()">createForLoopActionUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>For Loop Action Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/FramedConcernMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FramedConcernMembership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFramedConcernMembership()">createFramedConcernMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Framed Concern Membership</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createIfActionUsage()">createIfActionUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>If Action Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IncludeUseCaseUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createIncludeUseCaseUsage()">createIncludeUseCaseUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Include Use Case Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createInterfaceDefinition()">createInterfaceDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Interface Definition</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createInterfaceUsage()">createInterfaceUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Interface Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ItemDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createItemDefinition()">createItemDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Item Definition</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createItemUsage()">createItemUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Item Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/JoinNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">JoinNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createJoinNode()">createJoinNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Join Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/MembershipExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MembershipExpose</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createMembershipExpose()">createMembershipExpose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Membership Expose</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/MergeNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MergeNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createMergeNode()">createMergeNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Merge Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/MetadataDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createMetadataDefinition()">createMetadataDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Metadata Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createMetadataUsage()">createMetadataUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Metadata Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/NamespaceExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">NamespaceExpose</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createNamespaceExpose()">createNamespaceExpose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Namespace Expose</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ObjectiveMembership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createObjectiveMembership()">createObjectiveMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Objective Membership</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/OccurrenceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createOccurrenceDefinition()">createOccurrenceDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Occurrence Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createOccurrenceUsage()">createOccurrenceUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Occurrence Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createPartDefinition()">createPartDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Part Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createPartUsage()">createPartUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Part Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createPerformActionUsage()">createPerformActionUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Perform Action Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/PortConjugation.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortConjugation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createPortConjugation()">createPortConjugation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Port Conjugation</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createPortDefinition()">createPortDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Port Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createPortUsage()">createPortUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Port Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createReferenceUsage()">createReferenceUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Reference Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createRenderingDefinition()">createRenderingDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Rendering Definition</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createRenderingUsage()">createRenderingUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Rendering Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintMembership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createRequirementConstraintMembership()">createRequirementConstraintMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Requirement Constraint Membership</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createRequirementDefinition()">createRequirementDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Requirement Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createRequirementUsage()">createRequirementUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Requirement Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/RequirementVerificationMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementVerificationMembership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createRequirementVerificationMembership()">createRequirementVerificationMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Requirement Verification Membership</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SatisfyRequirementUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createSatisfyRequirementUsage()">createSatisfyRequirementUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Satisfy Requirement Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/SendActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SendActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createSendActionUsage()">createSendActionUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Send Action Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/StakeholderMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StakeholderMembership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createStakeholderMembership()">createStakeholderMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Stakeholder Membership</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createStateDefinition()">createStateDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>State Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/StateSubactionMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionMembership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createStateSubactionMembership()">createStateSubactionMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>State Subaction Membership</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createStateUsage()">createStateUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>State Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SubjectMembership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createSubjectMembership()">createSubjectMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Subject Membership</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionAsUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createSuccessionAsUsage()">createSuccessionAsUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Succession As Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createSuccessionFlowUsage()">createSuccessionFlowUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Succession Flow Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/TerminateActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TerminateActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createTerminateActionUsage()">createTerminateActionUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Terminate Action Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/TransitionFeatureMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionFeatureMembership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createTransitionFeatureMembership()">createTransitionFeatureMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Transition Feature Membership</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createTransitionUsage()">createTransitionUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Transition Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/TriggerInvocationExpression.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TriggerInvocationExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createTriggerInvocationExpression()">createTriggerInvocationExpression</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Trigger Invocation Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createUsage()">createUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createUseCaseDefinition()">createUseCaseDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Use Case Definition</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createUseCaseUsage()">createUseCaseUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Use Case Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VariantMembership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createVariantMembership()">createVariantMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Variant Membership</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createVerificationCaseDefinition()">createVerificationCaseDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Verification Case Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createVerificationCaseUsage()">createVerificationCaseUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Verification Case Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createViewDefinition()">createViewDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>View Definition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createViewpointDefinition()">createViewpointDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Viewpoint Definition</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createViewpointUsage()">createViewpointUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Viewpoint Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ViewRenderingMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewRenderingMembership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createViewRenderingMembership()">createViewRenderingMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>View Rendering Membership</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createViewUsage()">createViewUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>View Usage</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createWhileLoopActionUsage()">createWhileLoopActionUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>While Loop Action Usage</em>'.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory</h3>
<code>create, initializeElement</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.KerMLElementsFactory">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.<a href="../../kerml/model/KerMLElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLElementsFactory</a></h3>
<code><a href="../../kerml/model/KerMLElementsFactory.html#createAnnotatingElement()">createAnnotatingElement</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createAnnotation()">createAnnotation</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createAssociation()">createAssociation</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createAssociationStructure()">createAssociationStructure</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createBehavior()">createBehavior</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createBindingConnector()">createBindingConnector</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createBooleanExpression()">createBooleanExpression</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createClass()">createClass</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createClassifier()">createClassifier</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createCollectExpression()">createCollectExpression</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createComment()">createComment</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createConjugation()">createConjugation</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createConnector()">createConnector</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createConstructorExpression()">createConstructorExpression</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createCrossSubsetting()">createCrossSubsetting</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createDataType()">createDataType</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createDependency()">createDependency</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createDifferencing()">createDifferencing</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createDisjoining()">createDisjoining</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createDocumentation()">createDocumentation</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createElementFilterMembership()">createElementFilterMembership</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createEndFeatureMembership()">createEndFeatureMembership</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createExpression()">createExpression</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createFeature()">createFeature</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createFeatureChainExpression()">createFeatureChainExpression</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createFeatureChaining()">createFeatureChaining</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createFeatureInverting()">createFeatureInverting</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createFeatureMembership()">createFeatureMembership</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createFeatureReferenceExpression()">createFeatureReferenceExpression</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createFeatureTyping()">createFeatureTyping</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createFeatureValue()">createFeatureValue</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createFlow()">createFlow</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createFlowEnd()">createFlowEnd</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createFunction()">createFunction</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createIndexExpression()">createIndexExpression</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createInteraction()">createInteraction</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createIntersecting()">createIntersecting</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createInvariant()">createInvariant</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createInvocationExpression()">createInvocationExpression</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createLibraryPackage()">createLibraryPackage</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createLiteralBoolean()">createLiteralBoolean</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createLiteralExpression()">createLiteralExpression</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createLiteralInfinity()">createLiteralInfinity</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createLiteralInteger()">createLiteralInteger</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createLiteralRational()">createLiteralRational</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createLiteralString()">createLiteralString</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createMembership()">createMembership</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createMembershipImport()">createMembershipImport</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createMetaclass()">createMetaclass</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createMetadataAccessExpression()">createMetadataAccessExpression</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createMetadataFeature()">createMetadataFeature</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createMultiplicity()">createMultiplicity</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createMultiplicityRange()">createMultiplicityRange</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createNamespace()">createNamespace</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createNamespaceImport()">createNamespaceImport</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createNullExpression()">createNullExpression</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createOperatorExpression()">createOperatorExpression</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createOwningMembership()">createOwningMembership</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createPackage()">createPackage</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createParameterMembership()">createParameterMembership</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createPayloadFeature()">createPayloadFeature</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createPredicate()">createPredicate</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createRedefinition()">createRedefinition</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createReferenceSubsetting()">createReferenceSubsetting</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createResultExpressionMembership()">createResultExpressionMembership</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createReturnParameterMembership()">createReturnParameterMembership</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createSelectExpression()">createSelectExpression</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createSpecialization()">createSpecialization</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createStep()">createStep</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createStructure()">createStructure</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createSubclassification()">createSubclassification</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createSubsetting()">createSubsetting</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createSuccession()">createSuccession</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createSuccessionFlow()">createSuccessionFlow</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createTextualRepresentation()">createTextualRepresentation</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createType()">createType</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createTypeFeaturing()">createTypeFeaturing</a>, <a href="../../kerml/model/KerMLElementsFactory.html#createUnioning()">createUnioning</a></code></div>
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
<section class="detail" id="createAcceptActionUsage()">
<h3>createAcceptActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a></span> <span class="element-name">createAcceptActionUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Accept Action Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Accept Action Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActionDefinition()">
<h3>createActionDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionDefinition</a></span> <span class="element-name">createActionDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Action Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Action Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActionUsage()">
<h3>createActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></span> <span class="element-name">createActionUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Action Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Action Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActorMembership()">
<h3>createActorMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActorMembership</a></span> <span class="element-name">createActorMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Actor Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Actor Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAllocationDefinition()">
<h3>createAllocationDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationDefinition</a></span> <span class="element-name">createAllocationDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Allocation Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Allocation Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAllocationUsage()">
<h3>createAllocationUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a></span> <span class="element-name">createAllocationUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Allocation Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Allocation Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAnalysisCaseDefinition()">
<h3>createAnalysisCaseDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseDefinition</a></span> <span class="element-name">createAnalysisCaseDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Analysis Case Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Analysis Case Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAnalysisCaseUsage()">
<h3>createAnalysisCaseUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a></span> <span class="element-name">createAnalysisCaseUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Analysis Case Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Analysis Case Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAssertConstraintUsage()">
<h3>createAssertConstraintUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssertConstraintUsage</a></span> <span class="element-name">createAssertConstraintUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Assert Constraint Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Assert Constraint Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAssignmentActionUsage()">
<h3>createAssignmentActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a></span> <span class="element-name">createAssignmentActionUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Assignment Action Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Assignment Action Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAttributeDefinition()">
<h3>createAttributeDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeDefinition</a></span> <span class="element-name">createAttributeDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Attribute Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Attribute Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAttributeUsage()">
<h3>createAttributeUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a></span> <span class="element-name">createAttributeUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Attribute Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Attribute Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBindingConnectorAsUsage()">
<h3>createBindingConnectorAsUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">BindingConnectorAsUsage</a></span> <span class="element-name">createBindingConnectorAsUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Binding Connector As Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Binding Connector As Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCalculationDefinition()">
<h3>createCalculationDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/CalculationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationDefinition</a></span> <span class="element-name">createCalculationDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Calculation Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Calculation Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCalculationUsage()">
<h3>createCalculationUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a></span> <span class="element-name">createCalculationUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Calculation Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Calculation Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCaseDefinition()">
<h3>createCaseDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseDefinition</a></span> <span class="element-name">createCaseDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Case Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Case Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCaseUsage()">
<h3>createCaseUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a></span> <span class="element-name">createCaseUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Case Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Case Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConcernDefinition()">
<h3>createConcernDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ConcernDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernDefinition</a></span> <span class="element-name">createConcernDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Concern Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Concern Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConcernUsage()">
<h3>createConcernUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a></span> <span class="element-name">createConcernUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Concern Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Concern Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConjugatedPortDefinition()">
<h3>createConjugatedPortDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a></span> <span class="element-name">createConjugatedPortDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Conjugated Port Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Conjugated Port Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConjugatedPortTyping()">
<h3>createConjugatedPortTyping</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ConjugatedPortTyping.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortTyping</a></span> <span class="element-name">createConjugatedPortTyping</span>()</div>
<div class="block">Returns a new object of class '<em>Conjugated Port Typing</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Conjugated Port Typing</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectionDefinition()">
<h3>createConnectionDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionDefinition</a></span> <span class="element-name">createConnectionDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Connection Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Connection Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectionUsage()">
<h3>createConnectionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionUsage</a></span> <span class="element-name">createConnectionUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Connection Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Connection Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConstraintDefinition()">
<h3>createConstraintDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintDefinition</a></span> <span class="element-name">createConstraintDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Constraint Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Constraint Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConstraintUsage()">
<h3>createConstraintUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a></span> <span class="element-name">createConstraintUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Constraint Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Constraint Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDecisionNode()">
<h3>createDecisionNode</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/DecisionNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">DecisionNode</a></span> <span class="element-name">createDecisionNode</span>()</div>
<div class="block">Returns a new object of class '<em>Decision Node</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Decision Node</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDefinition()">
<h3>createDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a></span> <span class="element-name">createDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEnumerationDefinition()">
<h3>createEnumerationDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationDefinition</a></span> <span class="element-name">createEnumerationDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Enumeration Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Enumeration Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEnumerationUsage()">
<h3>createEnumerationUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a></span> <span class="element-name">createEnumerationUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Enumeration Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Enumeration Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEventOccurrenceUsage()">
<h3>createEventOccurrenceUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/EventOccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EventOccurrenceUsage</a></span> <span class="element-name">createEventOccurrenceUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Event Occurrence Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Event Occurrence Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExhibitStateUsage()">
<h3>createExhibitStateUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ExhibitStateUsage</a></span> <span class="element-name">createExhibitStateUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Exhibit State Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Exhibit State Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFlowDefinition()">
<h3>createFlowDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowDefinition</a></span> <span class="element-name">createFlowDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Flow Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Flow Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFlowUsage()">
<h3>createFlowUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a></span> <span class="element-name">createFlowUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Flow Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Flow Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createForLoopActionUsage()">
<h3>createForLoopActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a></span> <span class="element-name">createForLoopActionUsage</span>()</div>
<div class="block">Returns a new object of class '<em>For Loop Action Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>For Loop Action Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createForkNode()">
<h3>createForkNode</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ForkNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForkNode</a></span> <span class="element-name">createForkNode</span>()</div>
<div class="block">Returns a new object of class '<em>Fork Node</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Fork Node</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFramedConcernMembership()">
<h3>createFramedConcernMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/FramedConcernMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FramedConcernMembership</a></span> <span class="element-name">createFramedConcernMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Framed Concern Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Framed Concern Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIfActionUsage()">
<h3>createIfActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a></span> <span class="element-name">createIfActionUsage</span>()</div>
<div class="block">Returns a new object of class '<em>If Action Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>If Action Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIncludeUseCaseUsage()">
<h3>createIncludeUseCaseUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IncludeUseCaseUsage</a></span> <span class="element-name">createIncludeUseCaseUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Include Use Case Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Include Use Case Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInterfaceDefinition()">
<h3>createInterfaceDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceDefinition</a></span> <span class="element-name">createInterfaceDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Interface Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Interface Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInterfaceUsage()">
<h3>createInterfaceUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a></span> <span class="element-name">createInterfaceUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Interface Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Interface Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createItemDefinition()">
<h3>createItemDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ItemDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemDefinition</a></span> <span class="element-name">createItemDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Item Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Item Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createItemUsage()">
<h3>createItemUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a></span> <span class="element-name">createItemUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Item Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Item Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createJoinNode()">
<h3>createJoinNode</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/JoinNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">JoinNode</a></span> <span class="element-name">createJoinNode</span>()</div>
<div class="block">Returns a new object of class '<em>Join Node</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Join Node</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMembershipExpose()">
<h3>createMembershipExpose</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/MembershipExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MembershipExpose</a></span> <span class="element-name">createMembershipExpose</span>()</div>
<div class="block">Returns a new object of class '<em>Membership Expose</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Membership Expose</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMergeNode()">
<h3>createMergeNode</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/MergeNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MergeNode</a></span> <span class="element-name">createMergeNode</span>()</div>
<div class="block">Returns a new object of class '<em>Merge Node</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Merge Node</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMetadataDefinition()">
<h3>createMetadataDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/MetadataDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataDefinition</a></span> <span class="element-name">createMetadataDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Metadata Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Metadata Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMetadataUsage()">
<h3>createMetadataUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a></span> <span class="element-name">createMetadataUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Metadata Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Metadata Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNamespaceExpose()">
<h3>createNamespaceExpose</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/NamespaceExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">NamespaceExpose</a></span> <span class="element-name">createNamespaceExpose</span>()</div>
<div class="block">Returns a new object of class '<em>Namespace Expose</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Namespace Expose</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createObjectiveMembership()">
<h3>createObjectiveMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ObjectiveMembership</a></span> <span class="element-name">createObjectiveMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Objective Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Objective Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOccurrenceDefinition()">
<h3>createOccurrenceDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/OccurrenceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceDefinition</a></span> <span class="element-name">createOccurrenceDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Occurrence Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Occurrence Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOccurrenceUsage()">
<h3>createOccurrenceUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a></span> <span class="element-name">createOccurrenceUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Occurrence Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Occurrence Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPartDefinition()">
<h3>createPartDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartDefinition</a></span> <span class="element-name">createPartDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Part Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Part Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPartUsage()">
<h3>createPartUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a></span> <span class="element-name">createPartUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Part Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Part Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPerformActionUsage()">
<h3>createPerformActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a></span> <span class="element-name">createPerformActionUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Perform Action Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Perform Action Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPortConjugation()">
<h3>createPortConjugation</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/PortConjugation.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortConjugation</a></span> <span class="element-name">createPortConjugation</span>()</div>
<div class="block">Returns a new object of class '<em>Port Conjugation</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Port Conjugation</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPortDefinition()">
<h3>createPortDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></span> <span class="element-name">createPortDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Port Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Port Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPortUsage()">
<h3>createPortUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a></span> <span class="element-name">createPortUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Port Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Port Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReferenceUsage()">
<h3>createReferenceUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a></span> <span class="element-name">createReferenceUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Reference Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Reference Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRenderingDefinition()">
<h3>createRenderingDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingDefinition</a></span> <span class="element-name">createRenderingDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Rendering Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Rendering Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRenderingUsage()">
<h3>createRenderingUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a></span> <span class="element-name">createRenderingUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Rendering Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Rendering Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRequirementConstraintMembership()">
<h3>createRequirementConstraintMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintMembership</a></span> <span class="element-name">createRequirementConstraintMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Requirement Constraint Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Requirement Constraint Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRequirementDefinition()">
<h3>createRequirementDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementDefinition</a></span> <span class="element-name">createRequirementDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Requirement Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Requirement Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRequirementUsage()">
<h3>createRequirementUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></span> <span class="element-name">createRequirementUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Requirement Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Requirement Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRequirementVerificationMembership()">
<h3>createRequirementVerificationMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/RequirementVerificationMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementVerificationMembership</a></span> <span class="element-name">createRequirementVerificationMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Requirement Verification Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Requirement Verification Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSatisfyRequirementUsage()">
<h3>createSatisfyRequirementUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SatisfyRequirementUsage</a></span> <span class="element-name">createSatisfyRequirementUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Satisfy Requirement Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Satisfy Requirement Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSendActionUsage()">
<h3>createSendActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/SendActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SendActionUsage</a></span> <span class="element-name">createSendActionUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Send Action Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Send Action Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStakeholderMembership()">
<h3>createStakeholderMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/StakeholderMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StakeholderMembership</a></span> <span class="element-name">createStakeholderMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Stakeholder Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Stakeholder Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateDefinition()">
<h3>createStateDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateDefinition</a></span> <span class="element-name">createStateDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>State Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>State Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateSubactionMembership()">
<h3>createStateSubactionMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/StateSubactionMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionMembership</a></span> <span class="element-name">createStateSubactionMembership</span>()</div>
<div class="block">Returns a new object of class '<em>State Subaction Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>State Subaction Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateUsage()">
<h3>createStateUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a></span> <span class="element-name">createStateUsage</span>()</div>
<div class="block">Returns a new object of class '<em>State Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>State Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSubjectMembership()">
<h3>createSubjectMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SubjectMembership</a></span> <span class="element-name">createSubjectMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Subject Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Subject Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSuccessionAsUsage()">
<h3>createSuccessionAsUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionAsUsage</a></span> <span class="element-name">createSuccessionAsUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Succession As Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Succession As Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSuccessionFlowUsage()">
<h3>createSuccessionFlowUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a></span> <span class="element-name">createSuccessionFlowUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Succession Flow Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Succession Flow Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTerminateActionUsage()">
<h3>createTerminateActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/TerminateActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TerminateActionUsage</a></span> <span class="element-name">createTerminateActionUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Terminate Action Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Terminate Action Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTransitionFeatureMembership()">
<h3>createTransitionFeatureMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/TransitionFeatureMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionFeatureMembership</a></span> <span class="element-name">createTransitionFeatureMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Transition Feature Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Transition Feature Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTransitionUsage()">
<h3>createTransitionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a></span> <span class="element-name">createTransitionUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Transition Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Transition Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTriggerInvocationExpression()">
<h3>createTriggerInvocationExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/TriggerInvocationExpression.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TriggerInvocationExpression</a></span> <span class="element-name">createTriggerInvocationExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Trigger Invocation Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Trigger Invocation Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUsage()">
<h3>createUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></span> <span class="element-name">createUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUseCaseDefinition()">
<h3>createUseCaseDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseDefinition</a></span> <span class="element-name">createUseCaseDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Use Case Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Use Case Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUseCaseUsage()">
<h3>createUseCaseUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a></span> <span class="element-name">createUseCaseUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Use Case Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Use Case Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createVariantMembership()">
<h3>createVariantMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VariantMembership</a></span> <span class="element-name">createVariantMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Variant Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Variant Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createVerificationCaseDefinition()">
<h3>createVerificationCaseDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseDefinition</a></span> <span class="element-name">createVerificationCaseDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Verification Case Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Verification Case Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createVerificationCaseUsage()">
<h3>createVerificationCaseUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a></span> <span class="element-name">createVerificationCaseUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Verification Case Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Verification Case Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createViewDefinition()">
<h3>createViewDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewDefinition</a></span> <span class="element-name">createViewDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>View Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>View Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createViewRenderingMembership()">
<h3>createViewRenderingMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ViewRenderingMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewRenderingMembership</a></span> <span class="element-name">createViewRenderingMembership</span>()</div>
<div class="block">Returns a new object of class '<em>View Rendering Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>View Rendering Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createViewUsage()">
<h3>createViewUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a></span> <span class="element-name">createViewUsage</span>()</div>
<div class="block">Returns a new object of class '<em>View Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>View Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createViewpointDefinition()">
<h3>createViewpointDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointDefinition</a></span> <span class="element-name">createViewpointDefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Viewpoint Definition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Viewpoint Definition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createViewpointUsage()">
<h3>createViewpointUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a></span> <span class="element-name">createViewpointUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Viewpoint Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Viewpoint Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createWhileLoopActionUsage()">
<h3>createWhileLoopActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a></span> <span class="element-name">createWhileLoopActionUsage</span>()</div>
<div class="block">Returns a new object of class '<em>While Loop Action Usage</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>While Loop Action Usage</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.lang.Class)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="type-parameters">&lt;T extends <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; aClass)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../kerml/model/KerMLElementsFactory.html#create(java.lang.Class)">create</a></code> in interface <code><a href="../../kerml/model/KerMLElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLElementsFactory</a></code></dd>
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
