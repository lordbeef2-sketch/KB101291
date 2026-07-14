# JAVA OPENAPI: ElementsFactory (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/impl/ElementsFactory.html
- source_path: `com/nomagic/uml2/impl/ElementsFactory.html`
- source_sha256: `c6fb4d7b88330c8118a80b64e335e5dba80da032fae4d9305dc7b93d61039873`
- captured_utc: `2026-07-14T16:59:01.974561+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.impl](package-summary.html)

## Class ElementsFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.impl.ElementsFactory

public classElementsFactory
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ElementsFactory](#%3Cinit%3E(com.nomagic.uml2.ext.TASRepository))([TASRepository](../ext/TASRepository.html) repository)`

`[ElementsFactory](#%3Cinit%3E(com.nomagic.uml2.ext.TASRepository,com.nomagic.uml2.impl.ModelVisitor))([TASRepository](../ext/TASRepository.html) repository,
 [ModelVisitor](ModelVisitor.html) configurator)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Abstraction](../ext/magicdraw/classes/mddependencies/Abstraction.html)`
`[createAbstractionInstance](#createAbstractionInstance())()`

`[AcceptCallAction](../ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html)`
`[createAcceptCallActionInstance](#createAcceptCallActionInstance())()`

`[AcceptEventAction](../ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html)`
`[createAcceptEventActionInstance](#createAcceptEventActionInstance())()`

`[ActionExecutionSpecification](../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html)`
`[createActionExecutionSpecificationInstance](#createActionExecutionSpecificationInstance())()`

`[ActionInputPin](../ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html)`
`[createActionInputPinInstance](#createActionInputPinInstance())()`

`[ActivityFinalNode](../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html)`
`[createActivityFinalNodeInstance](#createActivityFinalNodeInstance())()`

`[Activity](../ext/magicdraw/activities/mdfundamentalactivities/Activity.html)`
`[createActivityInstance](#createActivityInstance())()`

`[ActivityParameterNode](../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html)`
`[createActivityParameterNodeInstance](#createActivityParameterNodeInstance())()`

`[ActivityPartition](../ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html)`
`[createActivityPartitionInstance](#createActivityPartitionInstance())()`

`[Actor](../ext/magicdraw/mdusecases/Actor.html)`
`[createActorInstance](#createActorInstance())()`

`[AddStructuralFeatureValueAction](../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html)`
`[createAddStructuralFeatureValueActionInstance](#createAddStructuralFeatureValueActionInstance())()`

`[AddVariableValueAction](../ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html)`
`[createAddVariableValueActionInstance](#createAddVariableValueActionInstance())()`

`[AnyReceiveEvent](../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html)`
`[createAnyReceiveEventInstance](#createAnyReceiveEventInstance())()`

`[Artifact](../ext/magicdraw/deployments/mdartifacts/Artifact.html)`
`[createArtifactInstance](#createArtifactInstance())()`

`[AssociationClass](../ext/magicdraw/classes/mdassociationclasses/AssociationClass.html)`
`[createAssociationClassInstance](#createAssociationClassInstance())()`

`[Association](../ext/magicdraw/classes/mdkernel/Association.html)`
`[createAssociationInstance](#createAssociationInstance())()`

`[BehaviorExecutionSpecification](../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html)`
`[createBehaviorExecutionSpecificationInstance](#createBehaviorExecutionSpecificationInstance())()`

`[BooleanTaggedValue](../ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html)`
`[createBooleanTaggedValueInstance](#createBooleanTaggedValueInstance())()`

`[BroadcastSignalAction](../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html)`
`[createBroadcastSignalActionInstance](#createBroadcastSignalActionInstance())()`

`[CallBehaviorAction](../ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html)`
`[createCallBehaviorActionInstance](#createCallBehaviorActionInstance())()`

`[CallEvent](../ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html)`
`[createCallEventInstance](#createCallEventInstance())()`

`[CallOperationAction](../ext/magicdraw/actions/mdbasicactions/CallOperationAction.html)`
`[createCallOperationActionInstance](#createCallOperationActionInstance())()`

`[CentralBufferNode](../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html)`
`[createCentralBufferNodeInstance](#createCentralBufferNodeInstance())()`

`[ChangeEvent](../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html)`
`[createChangeEventInstance](#createChangeEventInstance())()`

`[ClassifierTemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html)`
`[createClassifierTemplateParameterInstance](#createClassifierTemplateParameterInstance())()`

`[Class](../ext/magicdraw/classes/mdkernel/Class.html)`
`[createClassInstance](#createClassInstance())()`

`[Clause](../ext/magicdraw/activities/mdstructuredactivities/Clause.html)`
`[createClauseInstance](#createClauseInstance())()`

`[ClearAssociationAction](../ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html)`
`[createClearAssociationActionInstance](#createClearAssociationActionInstance())()`

`[ClearStructuralFeatureAction](../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html)`
`[createClearStructuralFeatureActionInstance](#createClearStructuralFeatureActionInstance())()`

`[ClearVariableAction](../ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html)`
`[createClearVariableActionInstance](#createClearVariableActionInstance())()`

`[Collaboration](../ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html)`
`[createCollaborationInstance](#createCollaborationInstance())()`

`[CollaborationUse](../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html)`
`[createCollaborationUseInstance](#createCollaborationUseInstance())()`

`[CombinedFragment](../ext/magicdraw/interactions/mdfragments/CombinedFragment.html)`
`[createCombinedFragmentInstance](#createCombinedFragmentInstance())()`

`[Comment](../ext/magicdraw/classes/mdkernel/Comment.html)`
`[createCommentInstance](#createCommentInstance())()`

`[CommunicationPath](../ext/magicdraw/deployments/mdnodes/CommunicationPath.html)`
`[createCommunicationPathInstance](#createCommunicationPathInstance())()`

`[Component](../ext/magicdraw/components/mdbasiccomponents/Component.html)`
`[createComponentInstance](#createComponentInstance())()`

`[ComponentRealization](../ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html)`
`[createComponentRealizationInstance](#createComponentRealizationInstance())()`

`[ConditionalNode](../ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html)`
`[createConditionalNodeInstance](#createConditionalNodeInstance())()`

`[ConnectableElementTemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html)`
`[createConnectableElementTemplateParameterInstance](#createConnectableElementTemplateParameterInstance())()`

`[ConnectionPointReference](../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html)`
`[createConnectionPointReferenceInstance](#createConnectionPointReferenceInstance())()`

`[ConnectorEnd](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html)`
`[createConnectorEndInstance](#createConnectorEndInstance())()`

`[Connector](../ext/magicdraw/compositestructures/mdinternalstructures/Connector.html)`
`[createConnectorInstance](#createConnectorInstance())()`

`[ConsiderIgnoreFragment](../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html)`
`[createConsiderIgnoreFragmentInstance](#createConsiderIgnoreFragmentInstance())()`

`[Constraint](../ext/magicdraw/classes/mdkernel/Constraint.html)`
`[createConstraintInstance](#createConstraintInstance())()`

`[Continuation](../ext/magicdraw/interactions/mdfragments/Continuation.html)`
`[createContinuationInstance](#createContinuationInstance())()`

`[ControlFlow](../ext/magicdraw/activities/mdbasicactivities/ControlFlow.html)`
`[createControlFlowInstance](#createControlFlowInstance())()`

`[CreateLinkAction](../ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html)`
`[createCreateLinkActionInstance](#createCreateLinkActionInstance())()`

`[CreateLinkObjectAction](../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html)`
`[createCreateLinkObjectActionInstance](#createCreateLinkObjectActionInstance())()`

`[CreateObjectAction](../ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html)`
`[createCreateObjectActionInstance](#createCreateObjectActionInstance())()`

`[DataStoreNode](../ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html)`
`[createDataStoreNodeInstance](#createDataStoreNodeInstance())()`

`[DataType](../ext/magicdraw/classes/mdkernel/DataType.html)`
`[createDataTypeInstance](#createDataTypeInstance())()`

`[DecisionNode](../ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html)`
`[createDecisionNodeInstance](#createDecisionNodeInstance())()`

`[Dependency](../ext/magicdraw/classes/mddependencies/Dependency.html)`
`[createDependencyInstance](#createDependencyInstance())()`

`[Deployment](../ext/magicdraw/deployments/mdnodes/Deployment.html)`
`[createDeploymentInstance](#createDeploymentInstance())()`

`[DeploymentSpecification](../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html)`
`[createDeploymentSpecificationInstance](#createDeploymentSpecificationInstance())()`

`[DestroyLinkAction](../ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html)`
`[createDestroyLinkActionInstance](#createDestroyLinkActionInstance())()`

`[DestroyObjectAction](../ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html)`
`[createDestroyObjectActionInstance](#createDestroyObjectActionInstance())()`

`[DestructionOccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html)`
`[createDestructionOccurrenceSpecificationInstance](#createDestructionOccurrenceSpecificationInstance())()`

`[Device](../ext/magicdraw/deployments/mdnodes/Device.html)`
`[createDeviceInstance](#createDeviceInstance())()`

`[Diagram](../ext/magicdraw/classes/mdkernel/Diagram.html)`
`[createDiagramInstance](#createDiagramInstance())()`

`[DurationConstraint](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html)`
`[createDurationConstraintInstance](#createDurationConstraintInstance())()`

`[Duration](../ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html)`
`[createDurationInstance](#createDurationInstance())()`

`[DurationInterval](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html)`
`[createDurationIntervalInstance](#createDurationIntervalInstance())()`

`[DurationObservation](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html)`
`[createDurationObservationInstance](#createDurationObservationInstance())()`

`[ElementImport](../ext/magicdraw/classes/mdkernel/ElementImport.html)`
`[createElementImportInstance](#createElementImportInstance())()`

`[ElementTaggedValue](../ext/magicdraw/classes/mdkernel/ElementTaggedValue.html)`
`[createElementTaggedValueInstance](#createElementTaggedValueInstance())()`

`[ElementValue](../ext/magicdraw/classes/mdkernel/ElementValue.html)`
`[createElementValueInstance](#createElementValueInstance())()`

`[Enumeration](../ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[createEnumerationInstance](#createEnumerationInstance())()`

`[EnumerationLiteral](../ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[createEnumerationLiteralInstance](#createEnumerationLiteralInstance())()`

`[ExceptionHandler](../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html)`
`[createExceptionHandlerInstance](#createExceptionHandlerInstance())()`

`[ExecutionEnvironment](../ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html)`
`[createExecutionEnvironmentInstance](#createExecutionEnvironmentInstance())()`

`[ExecutionOccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html)`
`[createExecutionOccurrenceSpecificationInstance](#createExecutionOccurrenceSpecificationInstance())()`

`[ExpansionNode](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html)`
`[createExpansionNodeInstance](#createExpansionNodeInstance())()`

`[ExpansionRegion](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html)`
`[createExpansionRegionInstance](#createExpansionRegionInstance())()`

`[Expression](../ext/magicdraw/classes/mdkernel/Expression.html)`
`[createExpressionInstance](#createExpressionInstance())()`

`[Extend](../ext/magicdraw/mdusecases/Extend.html)`
`[createExtendInstance](#createExtendInstance())()`

`[ExtensionEnd](../ext/magicdraw/mdprofiles/ExtensionEnd.html)`
`[createExtensionEndInstance](#createExtensionEndInstance())()`

`[Extension](../ext/magicdraw/mdprofiles/Extension.html)`
`[createExtensionInstance](#createExtensionInstance())()`

`[ExtensionPoint](../ext/magicdraw/mdusecases/ExtensionPoint.html)`
`[createExtensionPointInstance](#createExtensionPointInstance())()`

`[FinalState](../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html)`
`[createFinalStateInstance](#createFinalStateInstance())()`

`[FlowFinalNode](../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html)`
`[createFlowFinalNodeInstance](#createFlowFinalNodeInstance())()`

`[ForkNode](../ext/magicdraw/activities/mdintermediateactivities/ForkNode.html)`
`[createForkNodeInstance](#createForkNodeInstance())()`

`[FunctionBehavior](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html)`
`[createFunctionBehaviorInstance](#createFunctionBehaviorInstance())()`

`[Gate](../ext/magicdraw/interactions/mdfragments/Gate.html)`
`[createGateInstance](#createGateInstance())()`

`[Generalization](../ext/magicdraw/classes/mdkernel/Generalization.html)`
`[createGeneralizationInstance](#createGeneralizationInstance())()`

`[GeneralizationSet](../ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html)`
`[createGeneralizationSetInstance](#createGeneralizationSetInstance())()`

`[GeneralOrdering](../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html)`
`[createGeneralOrderingInstance](#createGeneralOrderingInstance())()`

`[Image](../ext/magicdraw/mdprofiles/Image.html)`
`[createImageInstance](#createImageInstance())()`

`[Include](../ext/magicdraw/mdusecases/Include.html)`
`[createIncludeInstance](#createIncludeInstance())()`

`[InformationFlow](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html)`
`[createInformationFlowInstance](#createInformationFlowInstance())()`

`[InformationItem](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html)`
`[createInformationItemInstance](#createInformationItemInstance())()`

`[InitialNode](../ext/magicdraw/activities/mdbasicactivities/InitialNode.html)`
`[createInitialNodeInstance](#createInitialNodeInstance())()`

`[InputPin](../ext/magicdraw/actions/mdbasicactions/InputPin.html)`
`[createInputPinInstance](#createInputPinInstance())()`

`[InstanceSpecification](../ext/magicdraw/classes/mdkernel/InstanceSpecification.html)`
`[createInstanceSpecificationInstance](#createInstanceSpecificationInstance())()`

`[InstanceValue](../ext/magicdraw/classes/mdkernel/InstanceValue.html)`
`[createInstanceValueInstance](#createInstanceValueInstance())()`

`[IntegerTaggedValue](../ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html)`
`[createIntegerTaggedValueInstance](#createIntegerTaggedValueInstance())()`

`[InteractionConstraint](../ext/magicdraw/interactions/mdfragments/InteractionConstraint.html)`
`[createInteractionConstraintInstance](#createInteractionConstraintInstance())()`

`[Interaction](../ext/magicdraw/interactions/mdbasicinteractions/Interaction.html)`
`[createInteractionInstance](#createInteractionInstance())()`

`[InteractionOperand](../ext/magicdraw/interactions/mdfragments/InteractionOperand.html)`
`[createInteractionOperandInstance](#createInteractionOperandInstance())()`

`[InteractionUse](../ext/magicdraw/interactions/mdfragments/InteractionUse.html)`
`[createInteractionUseInstance](#createInteractionUseInstance())()`

`[Interface](../ext/magicdraw/classes/mdinterfaces/Interface.html)`
`[createInterfaceInstance](#createInterfaceInstance())()`

`[InterfaceRealization](../ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html)`
`[createInterfaceRealizationInstance](#createInterfaceRealizationInstance())()`

`[InterruptibleActivityRegion](../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html)`
`[createInterruptibleActivityRegionInstance](#createInterruptibleActivityRegionInstance())()`

`[IntervalConstraint](../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html)`
`[createIntervalConstraintInstance](#createIntervalConstraintInstance())()`

`[Interval](../ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html)`
`[createIntervalInstance](#createIntervalInstance())()`

`[JoinNode](../ext/magicdraw/activities/mdintermediateactivities/JoinNode.html)`
`[createJoinNodeInstance](#createJoinNodeInstance())()`

`[Lifeline](../ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html)`
`[createLifelineInstance](#createLifelineInstance())()`

`[LinkEndCreationData](../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html)`
`[createLinkEndCreationDataInstance](#createLinkEndCreationDataInstance())()`

`[LinkEndData](../ext/magicdraw/actions/mdintermediateactions/LinkEndData.html)`
`[createLinkEndDataInstance](#createLinkEndDataInstance())()`

`[LinkEndDestructionData](../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html)`
`[createLinkEndDestructionDataInstance](#createLinkEndDestructionDataInstance())()`

`[LiteralBoolean](../ext/magicdraw/classes/mdkernel/LiteralBoolean.html)`
`[createLiteralBooleanInstance](#createLiteralBooleanInstance())()`

`[LiteralInteger](../ext/magicdraw/classes/mdkernel/LiteralInteger.html)`
`[createLiteralIntegerInstance](#createLiteralIntegerInstance())()`

`[LiteralNull](../ext/magicdraw/classes/mdkernel/LiteralNull.html)`
`[createLiteralNullInstance](#createLiteralNullInstance())()`

`[LiteralReal](../ext/magicdraw/classes/mdkernel/LiteralReal.html)`
`[createLiteralRealInstance](#createLiteralRealInstance())()`

`[LiteralString](../ext/magicdraw/classes/mdkernel/LiteralString.html)`
`[createLiteralStringInstance](#createLiteralStringInstance())()`

`[LiteralUnlimitedNatural](../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html)`
`[createLiteralUnlimitedNaturalInstance](#createLiteralUnlimitedNaturalInstance())()`

`[LoopNode](../ext/magicdraw/activities/mdstructuredactivities/LoopNode.html)`
`[createLoopNodeInstance](#createLoopNodeInstance())()`

`[Manifestation](../ext/magicdraw/deployments/mdartifacts/Manifestation.html)`
`[createManifestationInstance](#createManifestationInstance())()`

`[MergeNode](../ext/magicdraw/activities/mdintermediateactivities/MergeNode.html)`
`[createMergeNodeInstance](#createMergeNodeInstance())()`

`[Message](../ext/magicdraw/interactions/mdbasicinteractions/Message.html)`
`[createMessageInstance](#createMessageInstance())()`

`[MessageOccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html)`
`[createMessageOccurrenceSpecificationInstance](#createMessageOccurrenceSpecificationInstance())()`

`[Model](../ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html)`
`[createModelInstance](#createModelInstance())()`

`[Node](../ext/magicdraw/deployments/mdnodes/Node.html)`
`[createNodeInstance](#createNodeInstance())()`

`[Element](../ext/magicdraw/classes/mdkernel/Element.html)`
`[createNotConfigure](#createNotConfigure(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Create object by EClass, created object is not configured by configurator
`[ObjectFlow](../ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html)`
`[createObjectFlowInstance](#createObjectFlowInstance())()`

`[OccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html)`
`[createOccurrenceSpecificationInstance](#createOccurrenceSpecificationInstance())()`

`[OpaqueAction](../ext/magicdraw/actions/mdbasicactions/OpaqueAction.html)`
`[createOpaqueActionInstance](#createOpaqueActionInstance())()`

`[OpaqueBehavior](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html)`
`[createOpaqueBehaviorInstance](#createOpaqueBehaviorInstance())()`

`[OpaqueExpression](../ext/magicdraw/classes/mdkernel/OpaqueExpression.html)`
`[createOpaqueExpressionInstance](#createOpaqueExpressionInstance())()`

`[Operation](../ext/magicdraw/classes/mdkernel/Operation.html)`
`[createOperationInstance](#createOperationInstance())()`

`[OperationTemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html)`
`[createOperationTemplateParameterInstance](#createOperationTemplateParameterInstance())()`

`[OutputPin](../ext/magicdraw/actions/mdbasicactions/OutputPin.html)`
`[createOutputPinInstance](#createOutputPinInstance())()`

`[PackageImport](../ext/magicdraw/classes/mdkernel/PackageImport.html)`
`[createPackageImportInstance](#createPackageImportInstance())()`

`[Package](../ext/magicdraw/classes/mdkernel/Package.html)`
`[createPackageInstance](#createPackageInstance())()`

`[PackageMerge](../ext/magicdraw/classes/mdkernel/PackageMerge.html)`
`[createPackageMergeInstance](#createPackageMergeInstance())()`

`[Parameter](../ext/magicdraw/classes/mdkernel/Parameter.html)`
`[createParameterInstance](#createParameterInstance())()`

`[ParameterSet](../ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html)`
`[createParameterSetInstance](#createParameterSetInstance())()`

`[PartDecomposition](../ext/magicdraw/interactions/mdfragments/PartDecomposition.html)`
`[createPartDecompositionInstance](#createPartDecompositionInstance())()`

`[Port](../ext/magicdraw/compositestructures/mdports/Port.html)`
`[createPortInstance](#createPortInstance())()`

`[PrimitiveType](../ext/magicdraw/classes/mdkernel/PrimitiveType.html)`
`[createPrimitiveTypeInstance](#createPrimitiveTypeInstance())()`

`[ProfileApplication](../ext/magicdraw/mdprofiles/ProfileApplication.html)`
`[createProfileApplicationInstance](#createProfileApplicationInstance())()`

`[Profile](../ext/magicdraw/mdprofiles/Profile.html)`
`[createProfileInstance](#createProfileInstance())()`

`[Property](../ext/magicdraw/classes/mdkernel/Property.html)`
`[createPropertyInstance](#createPropertyInstance())()`

`[ProtocolConformance](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html)`
`[createProtocolConformanceInstance](#createProtocolConformanceInstance())()`

`[ProtocolStateMachine](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)`
`[createProtocolStateMachineInstance](#createProtocolStateMachineInstance())()`

`[ProtocolTransition](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html)`
`[createProtocolTransitionInstance](#createProtocolTransitionInstance())()`

`[Pseudostate](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html)`
`[createPseudostateInstance](#createPseudostateInstance())()`

`[QualifierValue](../ext/magicdraw/actions/mdcompleteactions/QualifierValue.html)`
`[createQualifierValueInstance](#createQualifierValueInstance())()`

`[RaiseExceptionAction](../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html)`
`[createRaiseExceptionActionInstance](#createRaiseExceptionActionInstance())()`

`[ReadExtentAction](../ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html)`
`[createReadExtentActionInstance](#createReadExtentActionInstance())()`

`[ReadIsClassifiedObjectAction](../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html)`
`[createReadIsClassifiedObjectActionInstance](#createReadIsClassifiedObjectActionInstance())()`

`[ReadLinkAction](../ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html)`
`[createReadLinkActionInstance](#createReadLinkActionInstance())()`

`[ReadLinkObjectEndAction](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html)`
`[createReadLinkObjectEndActionInstance](#createReadLinkObjectEndActionInstance())()`

`[ReadLinkObjectEndQualifierAction](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html)`
`[createReadLinkObjectEndQualifierActionInstance](#createReadLinkObjectEndQualifierActionInstance())()`

`[ReadSelfAction](../ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html)`
`[createReadSelfActionInstance](#createReadSelfActionInstance())()`

`[ReadStructuralFeatureAction](../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html)`
`[createReadStructuralFeatureActionInstance](#createReadStructuralFeatureActionInstance())()`

`[ReadVariableAction](../ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html)`
`[createReadVariableActionInstance](#createReadVariableActionInstance())()`

`[Realization](../ext/magicdraw/classes/mddependencies/Realization.html)`
`[createRealizationInstance](#createRealizationInstance())()`

`[RealTaggedValue](../ext/magicdraw/classes/mdkernel/RealTaggedValue.html)`
`[createRealTaggedValueInstance](#createRealTaggedValueInstance())()`

`[Reception](../ext/magicdraw/commonbehaviors/mdcommunications/Reception.html)`
`[createReceptionInstance](#createReceptionInstance())()`

`[ReclassifyObjectAction](../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html)`
`[createReclassifyObjectActionInstance](#createReclassifyObjectActionInstance())()`

`[RedefinableTemplateSignature](../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html)`
`[createRedefinableTemplateSignatureInstance](#createRedefinableTemplateSignatureInstance())()`

`[ReduceAction](../ext/magicdraw/actions/mdcompleteactions/ReduceAction.html)`
`[createReduceActionInstance](#createReduceActionInstance())()`

`[Region](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html)`
`[createRegionInstance](#createRegionInstance())()`

`[RemoveStructuralFeatureValueAction](../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html)`
`[createRemoveStructuralFeatureValueActionInstance](#createRemoveStructuralFeatureValueActionInstance())()`

`[RemoveVariableValueAction](../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html)`
`[createRemoveVariableValueActionInstance](#createRemoveVariableValueActionInstance())()`

`[ReplyAction](../ext/magicdraw/actions/mdcompleteactions/ReplyAction.html)`
`[createReplyActionInstance](#createReplyActionInstance())()`

`[SendObjectAction](../ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html)`
`[createSendObjectActionInstance](#createSendObjectActionInstance())()`

`[SendSignalAction](../ext/magicdraw/actions/mdbasicactions/SendSignalAction.html)`
`[createSendSignalActionInstance](#createSendSignalActionInstance())()`

`[SequenceNode](../ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html)`
`[createSequenceNodeInstance](#createSequenceNodeInstance())()`

`[SignalEvent](../ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html)`
`[createSignalEventInstance](#createSignalEventInstance())()`

`[Signal](../ext/magicdraw/commonbehaviors/mdcommunications/Signal.html)`
`[createSignalInstance](#createSignalInstance())()`

`[Slot](../ext/magicdraw/classes/mdkernel/Slot.html)`
`[createSlotInstance](#createSlotInstance())()`

`[StartClassifierBehaviorAction](../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html)`
`[createStartClassifierBehaviorActionInstance](#createStartClassifierBehaviorActionInstance())()`

`[StartObjectBehaviorAction](../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html)`
`[createStartObjectBehaviorActionInstance](#createStartObjectBehaviorActionInstance())()`

`[State](../ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html)`
`[createStateInstance](#createStateInstance())()`

`[StateInvariant](../ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html)`
`[createStateInvariantInstance](#createStateInvariantInstance())()`

`[StateMachine](../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html)`
`[createStateMachineInstance](#createStateMachineInstance())()`

`[Stereotype](../ext/magicdraw/mdprofiles/Stereotype.html)`
`[createStereotypeInstance](#createStereotypeInstance())()`

`[StringExpression](../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html)`
`[createStringExpressionInstance](#createStringExpressionInstance())()`

`[StringTaggedValue](../ext/magicdraw/classes/mdkernel/StringTaggedValue.html)`
`[createStringTaggedValueInstance](#createStringTaggedValueInstance())()`

`[StructuredActivityNode](../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html)`
`[createStructuredActivityNodeInstance](#createStructuredActivityNodeInstance())()`

`[Substitution](../ext/magicdraw/classes/mddependencies/Substitution.html)`
`[createSubstitutionInstance](#createSubstitutionInstance())()`

`[TemplateBinding](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html)`
`[createTemplateBindingInstance](#createTemplateBindingInstance())()`

`[TemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html)`
`[createTemplateParameterInstance](#createTemplateParameterInstance())()`

`[TemplateParameterSubstitution](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html)`
`[createTemplateParameterSubstitutionInstance](#createTemplateParameterSubstitutionInstance())()`

`[TemplateSignature](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html)`
`[createTemplateSignatureInstance](#createTemplateSignatureInstance())()`

`[TestIdentityAction](../ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html)`
`[createTestIdentityActionInstance](#createTestIdentityActionInstance())()`

`[TimeConstraint](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html)`
`[createTimeConstraintInstance](#createTimeConstraintInstance())()`

`[TimeEvent](../ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html)`
`[createTimeEventInstance](#createTimeEventInstance())()`

`[TimeExpression](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html)`
`[createTimeExpressionInstance](#createTimeExpressionInstance())()`

`[TimeInterval](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html)`
`[createTimeIntervalInstance](#createTimeIntervalInstance())()`

`[TimeObservation](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html)`
`[createTimeObservationInstance](#createTimeObservationInstance())()`

`[Transition](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html)`
`[createTransitionInstance](#createTransitionInstance())()`

`[Trigger](../ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html)`
`[createTriggerInstance](#createTriggerInstance())()`

`[UnmarshallAction](../ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html)`
`[createUnmarshallActionInstance](#createUnmarshallActionInstance())()`

`[Usage](../ext/magicdraw/classes/mddependencies/Usage.html)`
`[createUsageInstance](#createUsageInstance())()`

`[UseCase](../ext/magicdraw/mdusecases/UseCase.html)`
`[createUseCaseInstance](#createUseCaseInstance())()`

`[ValuePin](../ext/magicdraw/actions/mdbasicactions/ValuePin.html)`
`[createValuePinInstance](#createValuePinInstance())()`

`[ValueSpecificationAction](../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html)`
`[createValueSpecificationActionInstance](#createValueSpecificationActionInstance())()`

`[Variable](../ext/magicdraw/activities/mdstructuredactivities/Variable.html)`
`[createVariableInstance](#createVariableInstance())()`

`[AbstractionClass](../ext/magicdraw/classes/mddependencies/AbstractionClass.html)`
`[getAbstractionClass](#getAbstractionClass())()`

`[AcceptCallActionClass](../ext/magicdraw/actions/mdcompleteactions/AcceptCallActionClass.html)`
`[getAcceptCallActionClass](#getAcceptCallActionClass())()`

`[AcceptEventActionClass](../ext/magicdraw/actions/mdcompleteactions/AcceptEventActionClass.html)`
`[getAcceptEventActionClass](#getAcceptEventActionClass())()`

`[ActionClass](../ext/magicdraw/actions/mdbasicactions/ActionClass.html)`
`[getActionClass](#getActionClass())()`

`[ActionExecutionSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecificationClass.html)`
`[getActionExecutionSpecificationClass](#getActionExecutionSpecificationClass())()`

`[ActionInputPinClass](../ext/magicdraw/actions/mdstructuredactions/ActionInputPinClass.html)`
`[getActionInputPinClass](#getActionInputPinClass())()`

`[ActivityClass](../ext/magicdraw/activities/mdfundamentalactivities/ActivityClass.html)`
`[getActivityClass](#getActivityClass())()`

`[ActivityEdgeClass](../ext/magicdraw/activities/mdbasicactivities/ActivityEdgeClass.html)`
`[getActivityEdgeClass](#getActivityEdgeClass())()`

`[ActivityFinalNodeClass](../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNodeClass.html)`
`[getActivityFinalNodeClass](#getActivityFinalNodeClass())()`

`[ActivityGroupClass](../ext/magicdraw/activities/mdfundamentalactivities/ActivityGroupClass.html)`
`[getActivityGroupClass](#getActivityGroupClass())()`

`[ActivityNodeClass](../ext/magicdraw/activities/mdfundamentalactivities/ActivityNodeClass.html)`
`[getActivityNodeClass](#getActivityNodeClass())()`

`[ActivityParameterNodeClass](../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNodeClass.html)`
`[getActivityParameterNodeClass](#getActivityParameterNodeClass())()`

`[ActivityPartitionClass](../ext/magicdraw/activities/mdintermediateactivities/ActivityPartitionClass.html)`
`[getActivityPartitionClass](#getActivityPartitionClass())()`

`[ActorClass](../ext/magicdraw/mdusecases/ActorClass.html)`
`[getActorClass](#getActorClass())()`

`[AddStructuralFeatureValueActionClass](../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueActionClass.html)`
`[getAddStructuralFeatureValueActionClass](#getAddStructuralFeatureValueActionClass())()`

`[AddVariableValueActionClass](../ext/magicdraw/actions/mdstructuredactions/AddVariableValueActionClass.html)`
`[getAddVariableValueActionClass](#getAddVariableValueActionClass())()`

`[AnyReceiveEventClass](../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEventClass.html)`
`[getAnyReceiveEventClass](#getAnyReceiveEventClass())()`

`[ArtifactClass](../ext/magicdraw/deployments/mdartifacts/ArtifactClass.html)`
`[getArtifactClass](#getArtifactClass())()`

`[AssociationClass](../ext/magicdraw/classes/mdkernel/AssociationClass.html)`
`[getAssociationClass](#getAssociationClass())()`

`[AssociationClassClass](../ext/magicdraw/classes/mdassociationclasses/AssociationClassClass.html)`
`[getAssociationClassClass](#getAssociationClassClass())()`

`[BehavioralFeatureClass](../ext/magicdraw/classes/mdkernel/BehavioralFeatureClass.html)`
`[getBehavioralFeatureClass](#getBehavioralFeatureClass())()`

`[BehaviorClass](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehaviorClass.html)`
`[getBehaviorClass](#getBehaviorClass())()`

`[BehavioredClassifierClass](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifierClass.html)`
`[getBehavioredClassifierClass](#getBehavioredClassifierClass())()`

`[BehaviorExecutionSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecificationClass.html)`
`[getBehaviorExecutionSpecificationClass](#getBehaviorExecutionSpecificationClass())()`

`[BooleanTaggedValueClass](../ext/magicdraw/classes/mdkernel/BooleanTaggedValueClass.html)`
`[getBooleanTaggedValueClass](#getBooleanTaggedValueClass())()`

`[BroadcastSignalActionClass](../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalActionClass.html)`
`[getBroadcastSignalActionClass](#getBroadcastSignalActionClass())()`

`[CallActionClass](../ext/magicdraw/actions/mdbasicactions/CallActionClass.html)`
`[getCallActionClass](#getCallActionClass())()`

`[CallBehaviorActionClass](../ext/magicdraw/actions/mdbasicactions/CallBehaviorActionClass.html)`
`[getCallBehaviorActionClass](#getCallBehaviorActionClass())()`

`[CallEventClass](../ext/magicdraw/commonbehaviors/mdcommunications/CallEventClass.html)`
`[getCallEventClass](#getCallEventClass())()`

`[CallOperationActionClass](../ext/magicdraw/actions/mdbasicactions/CallOperationActionClass.html)`
`[getCallOperationActionClass](#getCallOperationActionClass())()`

`[CentralBufferNodeClass](../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNodeClass.html)`
`[getCentralBufferNodeClass](#getCentralBufferNodeClass())()`

`[ChangeEventClass](../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEventClass.html)`
`[getChangeEventClass](#getChangeEventClass())()`

`[ClassClass](../ext/magicdraw/classes/mdkernel/ClassClass.html)`
`[getClassClass](#getClassClass())()`

`[ClassifierClass](../ext/magicdraw/classes/mdkernel/ClassifierClass.html)`
`[getClassifierClass](#getClassifierClass())()`

`[ClassifierTemplateParameterClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameterClass.html)`
`[getClassifierTemplateParameterClass](#getClassifierTemplateParameterClass())()`

`[ClauseClass](../ext/magicdraw/activities/mdstructuredactivities/ClauseClass.html)`
`[getClauseClass](#getClauseClass())()`

`[ClearAssociationActionClass](../ext/magicdraw/actions/mdintermediateactions/ClearAssociationActionClass.html)`
`[getClearAssociationActionClass](#getClearAssociationActionClass())()`

`[ClearStructuralFeatureActionClass](../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureActionClass.html)`
`[getClearStructuralFeatureActionClass](#getClearStructuralFeatureActionClass())()`

`[ClearVariableActionClass](../ext/magicdraw/actions/mdstructuredactions/ClearVariableActionClass.html)`
`[getClearVariableActionClass](#getClearVariableActionClass())()`

`[CollaborationClass](../ext/magicdraw/compositestructures/mdcollaborations/CollaborationClass.html)`
`[getCollaborationClass](#getCollaborationClass())()`

`[CollaborationUseClass](../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUseClass.html)`
`[getCollaborationUseClass](#getCollaborationUseClass())()`

`[CombinedFragmentClass](../ext/magicdraw/interactions/mdfragments/CombinedFragmentClass.html)`
`[getCombinedFragmentClass](#getCombinedFragmentClass())()`

`[CommentClass](../ext/magicdraw/classes/mdkernel/CommentClass.html)`
`[getCommentClass](#getCommentClass())()`

`[CommunicationPathClass](../ext/magicdraw/deployments/mdnodes/CommunicationPathClass.html)`
`[getCommunicationPathClass](#getCommunicationPathClass())()`

`[ComponentClass](../ext/magicdraw/components/mdbasiccomponents/ComponentClass.html)`
`[getComponentClass](#getComponentClass())()`

`[ComponentRealizationClass](../ext/magicdraw/components/mdbasiccomponents/ComponentRealizationClass.html)`
`[getComponentRealizationClass](#getComponentRealizationClass())()`

`[ConditionalNodeClass](../ext/magicdraw/activities/mdstructuredactivities/ConditionalNodeClass.html)`
`[getConditionalNodeClass](#getConditionalNodeClass())()`

`[ConnectableElementClass](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElementClass.html)`
`[getConnectableElementClass](#getConnectableElementClass())()`

`[ConnectableElementTemplateParameterClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameterClass.html)`
`[getConnectableElementTemplateParameterClass](#getConnectableElementTemplateParameterClass())()`

`[ConnectionPointReferenceClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReferenceClass.html)`
`[getConnectionPointReferenceClass](#getConnectionPointReferenceClass())()`

`[ConnectorClass](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorClass.html)`
`[getConnectorClass](#getConnectorClass())()`

`[ConnectorEndClass](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEndClass.html)`
`[getConnectorEndClass](#getConnectorEndClass())()`

`[ConsiderIgnoreFragmentClass](../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragmentClass.html)`
`[getConsiderIgnoreFragmentClass](#getConsiderIgnoreFragmentClass())()`

`[ConstraintClass](../ext/magicdraw/classes/mdkernel/ConstraintClass.html)`
`[getConstraintClass](#getConstraintClass())()`

`[ContinuationClass](../ext/magicdraw/interactions/mdfragments/ContinuationClass.html)`
`[getContinuationClass](#getContinuationClass())()`

`[ControlFlowClass](../ext/magicdraw/activities/mdbasicactivities/ControlFlowClass.html)`
`[getControlFlowClass](#getControlFlowClass())()`

`[ControlNodeClass](../ext/magicdraw/activities/mdbasicactivities/ControlNodeClass.html)`
`[getControlNodeClass](#getControlNodeClass())()`

`[CreateLinkActionClass](../ext/magicdraw/actions/mdintermediateactions/CreateLinkActionClass.html)`
`[getCreateLinkActionClass](#getCreateLinkActionClass())()`

`[CreateLinkObjectActionClass](../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectActionClass.html)`
`[getCreateLinkObjectActionClass](#getCreateLinkObjectActionClass())()`

`[CreateObjectActionClass](../ext/magicdraw/actions/mdintermediateactions/CreateObjectActionClass.html)`
`[getCreateObjectActionClass](#getCreateObjectActionClass())()`

`[DataStoreNodeClass](../ext/magicdraw/activities/mdcompleteactivities/DataStoreNodeClass.html)`
`[getDataStoreNodeClass](#getDataStoreNodeClass())()`

`[DataTypeClass](../ext/magicdraw/classes/mdkernel/DataTypeClass.html)`
`[getDataTypeClass](#getDataTypeClass())()`

`[DecisionNodeClass](../ext/magicdraw/activities/mdintermediateactivities/DecisionNodeClass.html)`
`[getDecisionNodeClass](#getDecisionNodeClass())()`

`[DependencyClass](../ext/magicdraw/classes/mddependencies/DependencyClass.html)`
`[getDependencyClass](#getDependencyClass())()`

`[DeployedArtifactClass](../ext/magicdraw/deployments/mdnodes/DeployedArtifactClass.html)`
`[getDeployedArtifactClass](#getDeployedArtifactClass())()`

`[DeploymentClass](../ext/magicdraw/deployments/mdnodes/DeploymentClass.html)`
`[getDeploymentClass](#getDeploymentClass())()`

`[DeploymentSpecificationClass](../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecificationClass.html)`
`[getDeploymentSpecificationClass](#getDeploymentSpecificationClass())()`

`[DeploymentTargetClass](../ext/magicdraw/deployments/mdnodes/DeploymentTargetClass.html)`
`[getDeploymentTargetClass](#getDeploymentTargetClass())()`

`[DestroyLinkActionClass](../ext/magicdraw/actions/mdintermediateactions/DestroyLinkActionClass.html)`
`[getDestroyLinkActionClass](#getDestroyLinkActionClass())()`

`[DestroyObjectActionClass](../ext/magicdraw/actions/mdintermediateactions/DestroyObjectActionClass.html)`
`[getDestroyObjectActionClass](#getDestroyObjectActionClass())()`

`[DestructionOccurrenceSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecificationClass.html)`
`[getDestructionOccurrenceSpecificationClass](#getDestructionOccurrenceSpecificationClass())()`

`[DeviceClass](../ext/magicdraw/deployments/mdnodes/DeviceClass.html)`
`[getDeviceClass](#getDeviceClass())()`

`[DiagramClass](../ext/magicdraw/classes/mdkernel/DiagramClass.html)`
`[getDiagramClass](#getDiagramClass())()`

`[DirectedRelationshipClass](../ext/magicdraw/classes/mdkernel/DirectedRelationshipClass.html)`
`[getDirectedRelationshipClass](#getDirectedRelationshipClass())()`

`[DurationClass](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationClass.html)`
`[getDurationClass](#getDurationClass())()`

`[DurationConstraintClass](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraintClass.html)`
`[getDurationConstraintClass](#getDurationConstraintClass())()`

`[DurationIntervalClass](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationIntervalClass.html)`
`[getDurationIntervalClass](#getDurationIntervalClass())()`

`[DurationObservationClass](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservationClass.html)`
`[getDurationObservationClass](#getDurationObservationClass())()`

`[ElementClass](../ext/magicdraw/classes/mdkernel/ElementClass.html)`
`[getElementClass](#getElementClass())()`

`[ElementImportClass](../ext/magicdraw/classes/mdkernel/ElementImportClass.html)`
`[getElementImportClass](#getElementImportClass())()`

`[ElementTaggedValueClass](../ext/magicdraw/classes/mdkernel/ElementTaggedValueClass.html)`
`[getElementTaggedValueClass](#getElementTaggedValueClass())()`

`[ElementValueClass](../ext/magicdraw/classes/mdkernel/ElementValueClass.html)`
`[getElementValueClass](#getElementValueClass())()`

`[EncapsulatedClassifierClass](../ext/magicdraw/compositestructures/mdports/EncapsulatedClassifierClass.html)`
`[getEncapsulatedClassifierClass](#getEncapsulatedClassifierClass())()`

`[EnumerationClass](../ext/magicdraw/classes/mdkernel/EnumerationClass.html)`
`[getEnumerationClass](#getEnumerationClass())()`

`[EnumerationLiteralClass](../ext/magicdraw/classes/mdkernel/EnumerationLiteralClass.html)`
`[getEnumerationLiteralClass](#getEnumerationLiteralClass())()`

`[EventClass](../ext/magicdraw/commonbehaviors/mdcommunications/EventClass.html)`
`[getEventClass](#getEventClass())()`

`[ExceptionHandlerClass](../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandlerClass.html)`
`[getExceptionHandlerClass](#getExceptionHandlerClass())()`

`[ExecutableNodeClass](../ext/magicdraw/activities/mdstructuredactivities/ExecutableNodeClass.html)`
`[getExecutableNodeClass](#getExecutableNodeClass())()`

`[ExecutionEnvironmentClass](../ext/magicdraw/deployments/mdnodes/ExecutionEnvironmentClass.html)`
`[getExecutionEnvironmentClass](#getExecutionEnvironmentClass())()`

`[ExecutionOccurrenceSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecificationClass.html)`
`[getExecutionOccurrenceSpecificationClass](#getExecutionOccurrenceSpecificationClass())()`

`[ExecutionSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecificationClass.html)`
`[getExecutionSpecificationClass](#getExecutionSpecificationClass())()`

`[ExpansionNodeClass](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNodeClass.html)`
`[getExpansionNodeClass](#getExpansionNodeClass())()`

`[ExpansionRegionClass](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegionClass.html)`
`[getExpansionRegionClass](#getExpansionRegionClass())()`

`[ExpressionClass](../ext/magicdraw/classes/mdkernel/ExpressionClass.html)`
`[getExpressionClass](#getExpressionClass())()`

`[ExtendClass](../ext/magicdraw/mdusecases/ExtendClass.html)`
`[getExtendClass](#getExtendClass())()`

`[ExtensionClass](../ext/magicdraw/mdprofiles/ExtensionClass.html)`
`[getExtensionClass](#getExtensionClass())()`

`[ExtensionEndClass](../ext/magicdraw/mdprofiles/ExtensionEndClass.html)`
`[getExtensionEndClass](#getExtensionEndClass())()`

`[ExtensionPointClass](../ext/magicdraw/mdusecases/ExtensionPointClass.html)`
`[getExtensionPointClass](#getExtensionPointClass())()`

`[FeatureClass](../ext/magicdraw/classes/mdkernel/FeatureClass.html)`
`[getFeatureClass](#getFeatureClass())()`

`[FinalNodeClass](../ext/magicdraw/activities/mdintermediateactivities/FinalNodeClass.html)`
`[getFinalNodeClass](#getFinalNodeClass())()`

`[FinalStateClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalStateClass.html)`
`[getFinalStateClass](#getFinalStateClass())()`

`[FlowFinalNodeClass](../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNodeClass.html)`
`[getFlowFinalNodeClass](#getFlowFinalNodeClass())()`

`[ForkNodeClass](../ext/magicdraw/activities/mdintermediateactivities/ForkNodeClass.html)`
`[getForkNodeClass](#getForkNodeClass())()`

`[FunctionBehaviorClass](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehaviorClass.html)`
`[getFunctionBehaviorClass](#getFunctionBehaviorClass())()`

`[GateClass](../ext/magicdraw/interactions/mdfragments/GateClass.html)`
`[getGateClass](#getGateClass())()`

`[GeneralizationClass](../ext/magicdraw/classes/mdkernel/GeneralizationClass.html)`
`[getGeneralizationClass](#getGeneralizationClass())()`

`[GeneralizationSetClass](../ext/magicdraw/classes/mdpowertypes/GeneralizationSetClass.html)`
`[getGeneralizationSetClass](#getGeneralizationSetClass())()`

`[GeneralOrderingClass](../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrderingClass.html)`
`[getGeneralOrderingClass](#getGeneralOrderingClass())()`

`[ImageClass](../ext/magicdraw/mdprofiles/ImageClass.html)`
`[getImageClass](#getImageClass())()`

`[IncludeClass](../ext/magicdraw/mdusecases/IncludeClass.html)`
`[getIncludeClass](#getIncludeClass())()`

`[InformationFlowClass](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlowClass.html)`
`[getInformationFlowClass](#getInformationFlowClass())()`

`[InformationItemClass](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItemClass.html)`
`[getInformationItemClass](#getInformationItemClass())()`

`[InitialNodeClass](../ext/magicdraw/activities/mdbasicactivities/InitialNodeClass.html)`
`[getInitialNodeClass](#getInitialNodeClass())()`

`[InputPinClass](../ext/magicdraw/actions/mdbasicactions/InputPinClass.html)`
`[getInputPinClass](#getInputPinClass())()`

`[InstanceSpecificationClass](../ext/magicdraw/classes/mdkernel/InstanceSpecificationClass.html)`
`[getInstanceSpecificationClass](#getInstanceSpecificationClass())()`

`[InstanceValueClass](../ext/magicdraw/classes/mdkernel/InstanceValueClass.html)`
`[getInstanceValueClass](#getInstanceValueClass())()`

`[IntegerTaggedValueClass](../ext/magicdraw/classes/mdkernel/IntegerTaggedValueClass.html)`
`[getIntegerTaggedValueClass](#getIntegerTaggedValueClass())()`

`[InteractionClass](../ext/magicdraw/interactions/mdbasicinteractions/InteractionClass.html)`
`[getInteractionClass](#getInteractionClass())()`

`[InteractionConstraintClass](../ext/magicdraw/interactions/mdfragments/InteractionConstraintClass.html)`
`[getInteractionConstraintClass](#getInteractionConstraintClass())()`

`[InteractionFragmentClass](../ext/magicdraw/interactions/mdbasicinteractions/InteractionFragmentClass.html)`
`[getInteractionFragmentClass](#getInteractionFragmentClass())()`

`[InteractionOperandClass](../ext/magicdraw/interactions/mdfragments/InteractionOperandClass.html)`
`[getInteractionOperandClass](#getInteractionOperandClass())()`

`[InteractionUseClass](../ext/magicdraw/interactions/mdfragments/InteractionUseClass.html)`
`[getInteractionUseClass](#getInteractionUseClass())()`

`[InterfaceClass](../ext/magicdraw/classes/mdinterfaces/InterfaceClass.html)`
`[getInterfaceClass](#getInterfaceClass())()`

`[InterfaceRealizationClass](../ext/magicdraw/classes/mdinterfaces/InterfaceRealizationClass.html)`
`[getInterfaceRealizationClass](#getInterfaceRealizationClass())()`

`[InterruptibleActivityRegionClass](../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegionClass.html)`
`[getInterruptibleActivityRegionClass](#getInterruptibleActivityRegionClass())()`

`[IntervalClass](../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalClass.html)`
`[getIntervalClass](#getIntervalClass())()`

`[IntervalConstraintClass](../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraintClass.html)`
`[getIntervalConstraintClass](#getIntervalConstraintClass())()`

`[InvocationActionClass](../ext/magicdraw/actions/mdbasicactions/InvocationActionClass.html)`
`[getInvocationActionClass](#getInvocationActionClass())()`

`[JoinNodeClass](../ext/magicdraw/activities/mdintermediateactivities/JoinNodeClass.html)`
`[getJoinNodeClass](#getJoinNodeClass())()`

`[LifelineClass](../ext/magicdraw/interactions/mdbasicinteractions/LifelineClass.html)`
`[getLifelineClass](#getLifelineClass())()`

`[LinkActionClass](../ext/magicdraw/actions/mdintermediateactions/LinkActionClass.html)`
`[getLinkActionClass](#getLinkActionClass())()`

`[LinkEndCreationDataClass](../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationDataClass.html)`
`[getLinkEndCreationDataClass](#getLinkEndCreationDataClass())()`

`[LinkEndDataClass](../ext/magicdraw/actions/mdintermediateactions/LinkEndDataClass.html)`
`[getLinkEndDataClass](#getLinkEndDataClass())()`

`[LinkEndDestructionDataClass](../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionDataClass.html)`
`[getLinkEndDestructionDataClass](#getLinkEndDestructionDataClass())()`

`[LiteralBooleanClass](../ext/magicdraw/classes/mdkernel/LiteralBooleanClass.html)`
`[getLiteralBooleanClass](#getLiteralBooleanClass())()`

`[LiteralIntegerClass](../ext/magicdraw/classes/mdkernel/LiteralIntegerClass.html)`
`[getLiteralIntegerClass](#getLiteralIntegerClass())()`

`[LiteralNullClass](../ext/magicdraw/classes/mdkernel/LiteralNullClass.html)`
`[getLiteralNullClass](#getLiteralNullClass())()`

`[LiteralRealClass](../ext/magicdraw/classes/mdkernel/LiteralRealClass.html)`
`[getLiteralRealClass](#getLiteralRealClass())()`

`[LiteralSpecificationClass](../ext/magicdraw/classes/mdkernel/LiteralSpecificationClass.html)`
`[getLiteralSpecificationClass](#getLiteralSpecificationClass())()`

`[LiteralStringClass](../ext/magicdraw/classes/mdkernel/LiteralStringClass.html)`
`[getLiteralStringClass](#getLiteralStringClass())()`

`[LiteralUnlimitedNaturalClass](../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNaturalClass.html)`
`[getLiteralUnlimitedNaturalClass](#getLiteralUnlimitedNaturalClass())()`

`[LoopNodeClass](../ext/magicdraw/activities/mdstructuredactivities/LoopNodeClass.html)`
`[getLoopNodeClass](#getLoopNodeClass())()`

`[ManifestationClass](../ext/magicdraw/deployments/mdartifacts/ManifestationClass.html)`
`[getManifestationClass](#getManifestationClass())()`

`[MergeNodeClass](../ext/magicdraw/activities/mdintermediateactivities/MergeNodeClass.html)`
`[getMergeNodeClass](#getMergeNodeClass())()`

`[MessageClass](../ext/magicdraw/interactions/mdbasicinteractions/MessageClass.html)`
`[getMessageClass](#getMessageClass())()`

`[MessageEndClass](../ext/magicdraw/interactions/mdbasicinteractions/MessageEndClass.html)`
`[getMessageEndClass](#getMessageEndClass())()`

`[MessageEventClass](../ext/magicdraw/commonbehaviors/mdcommunications/MessageEventClass.html)`
`[getMessageEventClass](#getMessageEventClass())()`

`[MessageOccurrenceSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecificationClass.html)`
`[getMessageOccurrenceSpecificationClass](#getMessageOccurrenceSpecificationClass())()`

`[ModelClass](../ext/magicdraw/auxiliaryconstructs/mdmodels/ModelClass.html)`
`[getModelClass](#getModelClass())()`

`[MultiplicityElementClass](../ext/magicdraw/classes/mdkernel/MultiplicityElementClass.html)`
`[getMultiplicityElementClass](#getMultiplicityElementClass())()`

`[NamedElementClass](../ext/magicdraw/classes/mdkernel/NamedElementClass.html)`
`[getNamedElementClass](#getNamedElementClass())()`

`[NamespaceClass](../ext/magicdraw/classes/mdkernel/NamespaceClass.html)`
`[getNamespaceClass](#getNamespaceClass())()`

`[NodeClass](../ext/magicdraw/deployments/mdnodes/NodeClass.html)`
`[getNodeClass](#getNodeClass())()`

`[ObjectFlowClass](../ext/magicdraw/activities/mdbasicactivities/ObjectFlowClass.html)`
`[getObjectFlowClass](#getObjectFlowClass())()`

`[ObjectNodeClass](../ext/magicdraw/activities/mdbasicactivities/ObjectNodeClass.html)`
`[getObjectNodeClass](#getObjectNodeClass())()`

`[ObservationClass](../ext/magicdraw/commonbehaviors/mdsimpletime/ObservationClass.html)`
`[getObservationClass](#getObservationClass())()`

`[OccurrenceSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecificationClass.html)`
`[getOccurrenceSpecificationClass](#getOccurrenceSpecificationClass())()`

`[OpaqueActionClass](../ext/magicdraw/actions/mdbasicactions/OpaqueActionClass.html)`
`[getOpaqueActionClass](#getOpaqueActionClass())()`

`[OpaqueBehaviorClass](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehaviorClass.html)`
`[getOpaqueBehaviorClass](#getOpaqueBehaviorClass())()`

`[OpaqueExpressionClass](../ext/magicdraw/classes/mdkernel/OpaqueExpressionClass.html)`
`[getOpaqueExpressionClass](#getOpaqueExpressionClass())()`

`[OperationClass](../ext/magicdraw/classes/mdkernel/OperationClass.html)`
`[getOperationClass](#getOperationClass())()`

`[OperationTemplateParameterClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameterClass.html)`
`[getOperationTemplateParameterClass](#getOperationTemplateParameterClass())()`

`[OutputPinClass](../ext/magicdraw/actions/mdbasicactions/OutputPinClass.html)`
`[getOutputPinClass](#getOutputPinClass())()`

`[PackageableElementClass](../ext/magicdraw/classes/mdkernel/PackageableElementClass.html)`
`[getPackageableElementClass](#getPackageableElementClass())()`

`[PackageClass](../ext/magicdraw/classes/mdkernel/PackageClass.html)`
`[getPackageClass](#getPackageClass())()`

`[PackageImportClass](../ext/magicdraw/classes/mdkernel/PackageImportClass.html)`
`[getPackageImportClass](#getPackageImportClass())()`

`[PackageMergeClass](../ext/magicdraw/classes/mdkernel/PackageMergeClass.html)`
`[getPackageMergeClass](#getPackageMergeClass())()`

`[ParameterableElementClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElementClass.html)`
`[getParameterableElementClass](#getParameterableElementClass())()`

`[ParameterClass](../ext/magicdraw/classes/mdkernel/ParameterClass.html)`
`[getParameterClass](#getParameterClass())()`

`[ParameterSetClass](../ext/magicdraw/activities/mdcompleteactivities/ParameterSetClass.html)`
`[getParameterSetClass](#getParameterSetClass())()`

`[PartDecompositionClass](../ext/magicdraw/interactions/mdfragments/PartDecompositionClass.html)`
`[getPartDecompositionClass](#getPartDecompositionClass())()`

`[PinClass](../ext/magicdraw/actions/mdbasicactions/PinClass.html)`
`[getPinClass](#getPinClass())()`

`[PortClass](../ext/magicdraw/compositestructures/mdports/PortClass.html)`
`[getPortClass](#getPortClass())()`

`[PrimitiveTypeClass](../ext/magicdraw/classes/mdkernel/PrimitiveTypeClass.html)`
`[getPrimitiveTypeClass](#getPrimitiveTypeClass())()`

`[ProfileApplicationClass](../ext/magicdraw/mdprofiles/ProfileApplicationClass.html)`
`[getProfileApplicationClass](#getProfileApplicationClass())()`

`[ProfileClass](../ext/magicdraw/mdprofiles/ProfileClass.html)`
`[getProfileClass](#getProfileClass())()`

`[PropertyClass](../ext/magicdraw/classes/mdkernel/PropertyClass.html)`
`[getPropertyClass](#getPropertyClass())()`

`[ProtocolConformanceClass](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformanceClass.html)`
`[getProtocolConformanceClass](#getProtocolConformanceClass())()`

`[ProtocolStateMachineClass](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachineClass.html)`
`[getProtocolStateMachineClass](#getProtocolStateMachineClass())()`

`[ProtocolTransitionClass](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransitionClass.html)`
`[getProtocolTransitionClass](#getProtocolTransitionClass())()`

`[PseudostateClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/PseudostateClass.html)`
`[getPseudostateClass](#getPseudostateClass())()`

`[QualifierValueClass](../ext/magicdraw/actions/mdcompleteactions/QualifierValueClass.html)`
`[getQualifierValueClass](#getQualifierValueClass())()`

`[RaiseExceptionActionClass](../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionActionClass.html)`
`[getRaiseExceptionActionClass](#getRaiseExceptionActionClass())()`

`[ReadExtentActionClass](../ext/magicdraw/actions/mdcompleteactions/ReadExtentActionClass.html)`
`[getReadExtentActionClass](#getReadExtentActionClass())()`

`[ReadIsClassifiedObjectActionClass](../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectActionClass.html)`
`[getReadIsClassifiedObjectActionClass](#getReadIsClassifiedObjectActionClass())()`

`[ReadLinkActionClass](../ext/magicdraw/actions/mdintermediateactions/ReadLinkActionClass.html)`
`[getReadLinkActionClass](#getReadLinkActionClass())()`

`[ReadLinkObjectEndActionClass](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndActionClass.html)`
`[getReadLinkObjectEndActionClass](#getReadLinkObjectEndActionClass())()`

`[ReadLinkObjectEndQualifierActionClass](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierActionClass.html)`
`[getReadLinkObjectEndQualifierActionClass](#getReadLinkObjectEndQualifierActionClass())()`

`[ReadSelfActionClass](../ext/magicdraw/actions/mdintermediateactions/ReadSelfActionClass.html)`
`[getReadSelfActionClass](#getReadSelfActionClass())()`

`[ReadStructuralFeatureActionClass](../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureActionClass.html)`
`[getReadStructuralFeatureActionClass](#getReadStructuralFeatureActionClass())()`

`[ReadVariableActionClass](../ext/magicdraw/actions/mdstructuredactions/ReadVariableActionClass.html)`
`[getReadVariableActionClass](#getReadVariableActionClass())()`

`[RealizationClass](../ext/magicdraw/classes/mddependencies/RealizationClass.html)`
`[getRealizationClass](#getRealizationClass())()`

`[RealTaggedValueClass](../ext/magicdraw/classes/mdkernel/RealTaggedValueClass.html)`
`[getRealTaggedValueClass](#getRealTaggedValueClass())()`

`[ReceptionClass](../ext/magicdraw/commonbehaviors/mdcommunications/ReceptionClass.html)`
`[getReceptionClass](#getReceptionClass())()`

`[ReclassifyObjectActionClass](../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectActionClass.html)`
`[getReclassifyObjectActionClass](#getReclassifyObjectActionClass())()`

`[RedefinableElementClass](../ext/magicdraw/classes/mdkernel/RedefinableElementClass.html)`
`[getRedefinableElementClass](#getRedefinableElementClass())()`

`[RedefinableTemplateSignatureClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignatureClass.html)`
`[getRedefinableTemplateSignatureClass](#getRedefinableTemplateSignatureClass())()`

`[ReduceActionClass](../ext/magicdraw/actions/mdcompleteactions/ReduceActionClass.html)`
`[getReduceActionClass](#getReduceActionClass())()`

`[RegionClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/RegionClass.html)`
`[getRegionClass](#getRegionClass())()`

`[RelationshipClass](../ext/magicdraw/classes/mdkernel/RelationshipClass.html)`
`[getRelationshipClass](#getRelationshipClass())()`

`[RemoveStructuralFeatureValueActionClass](../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueActionClass.html)`
`[getRemoveStructuralFeatureValueActionClass](#getRemoveStructuralFeatureValueActionClass())()`

`[RemoveVariableValueActionClass](../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueActionClass.html)`
`[getRemoveVariableValueActionClass](#getRemoveVariableValueActionClass())()`

`[ReplyActionClass](../ext/magicdraw/actions/mdcompleteactions/ReplyActionClass.html)`
`[getReplyActionClass](#getReplyActionClass())()`

`[SendObjectActionClass](../ext/magicdraw/actions/mdintermediateactions/SendObjectActionClass.html)`
`[getSendObjectActionClass](#getSendObjectActionClass())()`

`[SendSignalActionClass](../ext/magicdraw/actions/mdbasicactions/SendSignalActionClass.html)`
`[getSendSignalActionClass](#getSendSignalActionClass())()`

`[SequenceNodeClass](../ext/magicdraw/activities/mdstructuredactivities/SequenceNodeClass.html)`
`[getSequenceNodeClass](#getSequenceNodeClass())()`

`[SignalClass](../ext/magicdraw/commonbehaviors/mdcommunications/SignalClass.html)`
`[getSignalClass](#getSignalClass())()`

`[SignalEventClass](../ext/magicdraw/commonbehaviors/mdcommunications/SignalEventClass.html)`
`[getSignalEventClass](#getSignalEventClass())()`

`[SlotClass](../ext/magicdraw/classes/mdkernel/SlotClass.html)`
`[getSlotClass](#getSlotClass())()`

`[StartClassifierBehaviorActionClass](../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorActionClass.html)`
`[getStartClassifierBehaviorActionClass](#getStartClassifierBehaviorActionClass())()`

`[StartObjectBehaviorActionClass](../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorActionClass.html)`
`[getStartObjectBehaviorActionClass](#getStartObjectBehaviorActionClass())()`

`[StateClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateClass.html)`
`[getStateClass](#getStateClass())()`

`[StateInvariantClass](../ext/magicdraw/interactions/mdbasicinteractions/StateInvariantClass.html)`
`[getStateInvariantClass](#getStateInvariantClass())()`

`[StateMachineClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachineClass.html)`
`[getStateMachineClass](#getStateMachineClass())()`

`[StereotypeClass](../ext/magicdraw/mdprofiles/StereotypeClass.html)`
`[getStereotypeClass](#getStereotypeClass())()`

`[StringExpressionClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpressionClass.html)`
`[getStringExpressionClass](#getStringExpressionClass())()`

`[StringTaggedValueClass](../ext/magicdraw/classes/mdkernel/StringTaggedValueClass.html)`
`[getStringTaggedValueClass](#getStringTaggedValueClass())()`

`[StructuralFeatureActionClass](../ext/magicdraw/actions/mdintermediateactions/StructuralFeatureActionClass.html)`
`[getStructuralFeatureActionClass](#getStructuralFeatureActionClass())()`

`[StructuralFeatureClass](../ext/magicdraw/classes/mdkernel/StructuralFeatureClass.html)`
`[getStructuralFeatureClass](#getStructuralFeatureClass())()`

`[StructuredActivityNodeClass](../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNodeClass.html)`
`[getStructuredActivityNodeClass](#getStructuredActivityNodeClass())()`

`[StructuredClassifierClass](../ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifierClass.html)`
`[getStructuredClassifierClass](#getStructuredClassifierClass())()`

`[SubstitutionClass](../ext/magicdraw/classes/mddependencies/SubstitutionClass.html)`
`[getSubstitutionClass](#getSubstitutionClass())()`

`[TaggedValueClass](../ext/magicdraw/classes/mdkernel/TaggedValueClass.html)`
`[getTaggedValueClass](#getTaggedValueClass())()`

`[TemplateableElementClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElementClass.html)`
`[getTemplateableElementClass](#getTemplateableElementClass())()`

`[TemplateBindingClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBindingClass.html)`
`[getTemplateBindingClass](#getTemplateBindingClass())()`

`[TemplateParameterClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterClass.html)`
`[getTemplateParameterClass](#getTemplateParameterClass())()`

`[TemplateParameterSubstitutionClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitutionClass.html)`
`[getTemplateParameterSubstitutionClass](#getTemplateParameterSubstitutionClass())()`

`[TemplateSignatureClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignatureClass.html)`
`[getTemplateSignatureClass](#getTemplateSignatureClass())()`

`[TestIdentityActionClass](../ext/magicdraw/actions/mdintermediateactions/TestIdentityActionClass.html)`
`[getTestIdentityActionClass](#getTestIdentityActionClass())()`

`[TimeConstraintClass](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraintClass.html)`
`[getTimeConstraintClass](#getTimeConstraintClass())()`

`[TimeEventClass](../ext/magicdraw/commonbehaviors/mdcommunications/TimeEventClass.html)`
`[getTimeEventClass](#getTimeEventClass())()`

`[TimeExpressionClass](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpressionClass.html)`
`[getTimeExpressionClass](#getTimeExpressionClass())()`

`[TimeIntervalClass](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeIntervalClass.html)`
`[getTimeIntervalClass](#getTimeIntervalClass())()`

`[TimeObservationClass](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservationClass.html)`
`[getTimeObservationClass](#getTimeObservationClass())()`

`[TransitionClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/TransitionClass.html)`
`[getTransitionClass](#getTransitionClass())()`

`[TriggerClass](../ext/magicdraw/commonbehaviors/mdcommunications/TriggerClass.html)`
`[getTriggerClass](#getTriggerClass())()`

`[TypeClass](../ext/magicdraw/classes/mdkernel/TypeClass.html)`
`[getTypeClass](#getTypeClass())()`

`[TypedElementClass](../ext/magicdraw/classes/mdkernel/TypedElementClass.html)`
`[getTypedElementClass](#getTypedElementClass())()`

`[UnmarshallActionClass](../ext/magicdraw/actions/mdcompleteactions/UnmarshallActionClass.html)`
`[getUnmarshallActionClass](#getUnmarshallActionClass())()`

`[UsageClass](../ext/magicdraw/classes/mddependencies/UsageClass.html)`
`[getUsageClass](#getUsageClass())()`

`[UseCaseClass](../ext/magicdraw/mdusecases/UseCaseClass.html)`
`[getUseCaseClass](#getUseCaseClass())()`

`[ValuePinClass](../ext/magicdraw/actions/mdbasicactions/ValuePinClass.html)`
`[getValuePinClass](#getValuePinClass())()`

`[ValueSpecificationActionClass](../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationActionClass.html)`
`[getValueSpecificationActionClass](#getValueSpecificationActionClass())()`

`[ValueSpecificationClass](../ext/magicdraw/classes/mdkernel/ValueSpecificationClass.html)`
`[getValueSpecificationClass](#getValueSpecificationClass())()`

`[VariableActionClass](../ext/magicdraw/actions/mdstructuredactions/VariableActionClass.html)`
`[getVariableActionClass](#getVariableActionClass())()`

`[VariableClass](../ext/magicdraw/activities/mdstructuredactivities/VariableClass.html)`
`[getVariableClass](#getVariableClass())()`

`[VertexClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/VertexClass.html)`
`[getVertexClass](#getVertexClass())()`

`[WriteLinkActionClass](../ext/magicdraw/actions/mdintermediateactions/WriteLinkActionClass.html)`
`[getWriteLinkActionClass](#getWriteLinkActionClass())()`

`[WriteStructuralFeatureActionClass](../ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureActionClass.html)`
`[getWriteStructuralFeatureActionClass](#getWriteStructuralFeatureActionClass())()`

`[WriteVariableActionClass](../ext/magicdraw/actions/mdstructuredactions/WriteVariableActionClass.html)`
`[getWriteVariableActionClass](#getWriteVariableActionClass())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ElementsFactory
public ElementsFactory([TASRepository](../ext/TASRepository.html) repository)
ElementsFactory
public ElementsFactory([TASRepository](../ext/TASRepository.html) repository,
 @CheckForNull
 [ModelVisitor](ModelVisitor.html) configurator)
 ============ METHOD DETAIL ========== 
Method Details
createNotConfigure
@CheckForNullpublic [Element](../ext/magicdraw/classes/mdkernel/Element.html) createNotConfigure(org.eclipse.emf.ecore.EClass eClass)
Create object by EClass, created object is not configured by configurator
Parameters:
`eClass` - type for object to create
Returns:
created object, or null if given EClass is not in repository
getAbstractionClass
public [AbstractionClass](../ext/magicdraw/classes/mddependencies/AbstractionClass.html) getAbstractionClass()
Returns:
class of type AbstractionClass
getAcceptCallActionClass
public [AcceptCallActionClass](../ext/magicdraw/actions/mdcompleteactions/AcceptCallActionClass.html) getAcceptCallActionClass()
Returns:
class of type AcceptCallActionClass
getAcceptEventActionClass
public [AcceptEventActionClass](../ext/magicdraw/actions/mdcompleteactions/AcceptEventActionClass.html) getAcceptEventActionClass()
Returns:
class of type AcceptEventActionClass
getActionClass
public [ActionClass](../ext/magicdraw/actions/mdbasicactions/ActionClass.html) getActionClass()
Returns:
class of type ActionClass
getActionExecutionSpecificationClass
public [ActionExecutionSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecificationClass.html) getActionExecutionSpecificationClass()
Returns:
class of type ActionExecutionSpecificationClass
getActionInputPinClass
public [ActionInputPinClass](../ext/magicdraw/actions/mdstructuredactions/ActionInputPinClass.html) getActionInputPinClass()
Returns:
class of type ActionInputPinClass
getActivityClass
public [ActivityClass](../ext/magicdraw/activities/mdfundamentalactivities/ActivityClass.html) getActivityClass()
Returns:
class of type ActivityClass
getActivityEdgeClass
public [ActivityEdgeClass](../ext/magicdraw/activities/mdbasicactivities/ActivityEdgeClass.html) getActivityEdgeClass()
Returns:
class of type ActivityEdgeClass
getActivityFinalNodeClass
public [ActivityFinalNodeClass](../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNodeClass.html) getActivityFinalNodeClass()
Returns:
class of type ActivityFinalNodeClass
getActivityGroupClass
public [ActivityGroupClass](../ext/magicdraw/activities/mdfundamentalactivities/ActivityGroupClass.html) getActivityGroupClass()
Returns:
class of type ActivityGroupClass
getActivityNodeClass
public [ActivityNodeClass](../ext/magicdraw/activities/mdfundamentalactivities/ActivityNodeClass.html) getActivityNodeClass()
Returns:
class of type ActivityNodeClass
getActivityParameterNodeClass
public [ActivityParameterNodeClass](../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNodeClass.html) getActivityParameterNodeClass()
Returns:
class of type ActivityParameterNodeClass
getActivityPartitionClass
public [ActivityPartitionClass](../ext/magicdraw/activities/mdintermediateactivities/ActivityPartitionClass.html) getActivityPartitionClass()
Returns:
class of type ActivityPartitionClass
getActorClass
public [ActorClass](../ext/magicdraw/mdusecases/ActorClass.html) getActorClass()
Returns:
class of type ActorClass
getAddStructuralFeatureValueActionClass
public [AddStructuralFeatureValueActionClass](../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueActionClass.html) getAddStructuralFeatureValueActionClass()
Returns:
class of type AddStructuralFeatureValueActionClass
getAddVariableValueActionClass
public [AddVariableValueActionClass](../ext/magicdraw/actions/mdstructuredactions/AddVariableValueActionClass.html) getAddVariableValueActionClass()
Returns:
class of type AddVariableValueActionClass
getAnyReceiveEventClass
public [AnyReceiveEventClass](../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEventClass.html) getAnyReceiveEventClass()
Returns:
class of type AnyReceiveEventClass
getArtifactClass
public [ArtifactClass](../ext/magicdraw/deployments/mdartifacts/ArtifactClass.html) getArtifactClass()
Returns:
class of type ArtifactClass
getAssociationClass
public [AssociationClass](../ext/magicdraw/classes/mdkernel/AssociationClass.html) getAssociationClass()
Returns:
class of type AssociationClass
getAssociationClassClass
public [AssociationClassClass](../ext/magicdraw/classes/mdassociationclasses/AssociationClassClass.html) getAssociationClassClass()
Returns:
class of type AssociationClassClass
getBehaviorClass
public [BehaviorClass](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehaviorClass.html) getBehaviorClass()
Returns:
class of type BehaviorClass
getBehaviorExecutionSpecificationClass
public [BehaviorExecutionSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecificationClass.html) getBehaviorExecutionSpecificationClass()
Returns:
class of type BehaviorExecutionSpecificationClass
getBehavioralFeatureClass
public [BehavioralFeatureClass](../ext/magicdraw/classes/mdkernel/BehavioralFeatureClass.html) getBehavioralFeatureClass()
Returns:
class of type BehavioralFeatureClass
getBehavioredClassifierClass
public [BehavioredClassifierClass](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifierClass.html) getBehavioredClassifierClass()
Returns:
class of type BehavioredClassifierClass
getBroadcastSignalActionClass
public [BroadcastSignalActionClass](../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalActionClass.html) getBroadcastSignalActionClass()
Returns:
class of type BroadcastSignalActionClass
getCallActionClass
public [CallActionClass](../ext/magicdraw/actions/mdbasicactions/CallActionClass.html) getCallActionClass()
Returns:
class of type CallActionClass
getCallBehaviorActionClass
public [CallBehaviorActionClass](../ext/magicdraw/actions/mdbasicactions/CallBehaviorActionClass.html) getCallBehaviorActionClass()
Returns:
class of type CallBehaviorActionClass
getCallEventClass
public [CallEventClass](../ext/magicdraw/commonbehaviors/mdcommunications/CallEventClass.html) getCallEventClass()
Returns:
class of type CallEventClass
getCallOperationActionClass
public [CallOperationActionClass](../ext/magicdraw/actions/mdbasicactions/CallOperationActionClass.html) getCallOperationActionClass()
Returns:
class of type CallOperationActionClass
getCentralBufferNodeClass
public [CentralBufferNodeClass](../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNodeClass.html) getCentralBufferNodeClass()
Returns:
class of type CentralBufferNodeClass
getChangeEventClass
public [ChangeEventClass](../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEventClass.html) getChangeEventClass()
Returns:
class of type ChangeEventClass
getClassClass
public [ClassClass](../ext/magicdraw/classes/mdkernel/ClassClass.html) getClassClass()
Returns:
class of type ClassClass
getClassifierClass
public [ClassifierClass](../ext/magicdraw/classes/mdkernel/ClassifierClass.html) getClassifierClass()
Returns:
class of type ClassifierClass
getClassifierTemplateParameterClass
public [ClassifierTemplateParameterClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameterClass.html) getClassifierTemplateParameterClass()
Returns:
class of type ClassifierTemplateParameterClass
getClauseClass
public [ClauseClass](../ext/magicdraw/activities/mdstructuredactivities/ClauseClass.html) getClauseClass()
Returns:
class of type ClauseClass
getClearAssociationActionClass
public [ClearAssociationActionClass](../ext/magicdraw/actions/mdintermediateactions/ClearAssociationActionClass.html) getClearAssociationActionClass()
Returns:
class of type ClearAssociationActionClass
getClearStructuralFeatureActionClass
public [ClearStructuralFeatureActionClass](../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureActionClass.html) getClearStructuralFeatureActionClass()
Returns:
class of type ClearStructuralFeatureActionClass
getClearVariableActionClass
public [ClearVariableActionClass](../ext/magicdraw/actions/mdstructuredactions/ClearVariableActionClass.html) getClearVariableActionClass()
Returns:
class of type ClearVariableActionClass
getCollaborationClass
public [CollaborationClass](../ext/magicdraw/compositestructures/mdcollaborations/CollaborationClass.html) getCollaborationClass()
Returns:
class of type CollaborationClass
getCollaborationUseClass
public [CollaborationUseClass](../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUseClass.html) getCollaborationUseClass()
Returns:
class of type CollaborationUseClass
getCombinedFragmentClass
public [CombinedFragmentClass](../ext/magicdraw/interactions/mdfragments/CombinedFragmentClass.html) getCombinedFragmentClass()
Returns:
class of type CombinedFragmentClass
getCommentClass
public [CommentClass](../ext/magicdraw/classes/mdkernel/CommentClass.html) getCommentClass()
Returns:
class of type CommentClass
getCommunicationPathClass
public [CommunicationPathClass](../ext/magicdraw/deployments/mdnodes/CommunicationPathClass.html) getCommunicationPathClass()
Returns:
class of type CommunicationPathClass
getComponentClass
public [ComponentClass](../ext/magicdraw/components/mdbasiccomponents/ComponentClass.html) getComponentClass()
Returns:
class of type ComponentClass
getComponentRealizationClass
public [ComponentRealizationClass](../ext/magicdraw/components/mdbasiccomponents/ComponentRealizationClass.html) getComponentRealizationClass()
Returns:
class of type ComponentRealizationClass
getConditionalNodeClass
public [ConditionalNodeClass](../ext/magicdraw/activities/mdstructuredactivities/ConditionalNodeClass.html) getConditionalNodeClass()
Returns:
class of type ConditionalNodeClass
getConnectableElementClass
public [ConnectableElementClass](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElementClass.html) getConnectableElementClass()
Returns:
class of type ConnectableElementClass
getConnectableElementTemplateParameterClass
public [ConnectableElementTemplateParameterClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameterClass.html) getConnectableElementTemplateParameterClass()
Returns:
class of type ConnectableElementTemplateParameterClass
getConnectionPointReferenceClass
public [ConnectionPointReferenceClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReferenceClass.html) getConnectionPointReferenceClass()
Returns:
class of type ConnectionPointReferenceClass
getConnectorClass
public [ConnectorClass](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorClass.html) getConnectorClass()
Returns:
class of type ConnectorClass
getConnectorEndClass
public [ConnectorEndClass](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEndClass.html) getConnectorEndClass()
Returns:
class of type ConnectorEndClass
getConsiderIgnoreFragmentClass
public [ConsiderIgnoreFragmentClass](../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragmentClass.html) getConsiderIgnoreFragmentClass()
Returns:
class of type ConsiderIgnoreFragmentClass
getConstraintClass
public [ConstraintClass](../ext/magicdraw/classes/mdkernel/ConstraintClass.html) getConstraintClass()
Returns:
class of type ConstraintClass
getContinuationClass
public [ContinuationClass](../ext/magicdraw/interactions/mdfragments/ContinuationClass.html) getContinuationClass()
Returns:
class of type ContinuationClass
getControlFlowClass
public [ControlFlowClass](../ext/magicdraw/activities/mdbasicactivities/ControlFlowClass.html) getControlFlowClass()
Returns:
class of type ControlFlowClass
getControlNodeClass
public [ControlNodeClass](../ext/magicdraw/activities/mdbasicactivities/ControlNodeClass.html) getControlNodeClass()
Returns:
class of type ControlNodeClass
getCreateLinkActionClass
public [CreateLinkActionClass](../ext/magicdraw/actions/mdintermediateactions/CreateLinkActionClass.html) getCreateLinkActionClass()
Returns:
class of type CreateLinkActionClass
getCreateLinkObjectActionClass
public [CreateLinkObjectActionClass](../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectActionClass.html) getCreateLinkObjectActionClass()
Returns:
class of type CreateLinkObjectActionClass
getCreateObjectActionClass
public [CreateObjectActionClass](../ext/magicdraw/actions/mdintermediateactions/CreateObjectActionClass.html) getCreateObjectActionClass()
Returns:
class of type CreateObjectActionClass
getDataStoreNodeClass
public [DataStoreNodeClass](../ext/magicdraw/activities/mdcompleteactivities/DataStoreNodeClass.html) getDataStoreNodeClass()
Returns:
class of type DataStoreNodeClass
getDataTypeClass
public [DataTypeClass](../ext/magicdraw/classes/mdkernel/DataTypeClass.html) getDataTypeClass()
Returns:
class of type DataTypeClass
getDecisionNodeClass
public [DecisionNodeClass](../ext/magicdraw/activities/mdintermediateactivities/DecisionNodeClass.html) getDecisionNodeClass()
Returns:
class of type DecisionNodeClass
getDependencyClass
public [DependencyClass](../ext/magicdraw/classes/mddependencies/DependencyClass.html) getDependencyClass()
Returns:
class of type DependencyClass
getDeployedArtifactClass
public [DeployedArtifactClass](../ext/magicdraw/deployments/mdnodes/DeployedArtifactClass.html) getDeployedArtifactClass()
Returns:
class of type DeployedArtifactClass
getDeploymentClass
public [DeploymentClass](../ext/magicdraw/deployments/mdnodes/DeploymentClass.html) getDeploymentClass()
Returns:
class of type DeploymentClass
getDeploymentSpecificationClass
public [DeploymentSpecificationClass](../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecificationClass.html) getDeploymentSpecificationClass()
Returns:
class of type DeploymentSpecificationClass
getDeploymentTargetClass
public [DeploymentTargetClass](../ext/magicdraw/deployments/mdnodes/DeploymentTargetClass.html) getDeploymentTargetClass()
Returns:
class of type DeploymentTargetClass
getDestroyLinkActionClass
public [DestroyLinkActionClass](../ext/magicdraw/actions/mdintermediateactions/DestroyLinkActionClass.html) getDestroyLinkActionClass()
Returns:
class of type DestroyLinkActionClass
getDestroyObjectActionClass
public [DestroyObjectActionClass](../ext/magicdraw/actions/mdintermediateactions/DestroyObjectActionClass.html) getDestroyObjectActionClass()
Returns:
class of type DestroyObjectActionClass
getDestructionOccurrenceSpecificationClass
public [DestructionOccurrenceSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecificationClass.html) getDestructionOccurrenceSpecificationClass()
Returns:
class of type DestructionOccurrenceSpecificationClass
getDeviceClass
public [DeviceClass](../ext/magicdraw/deployments/mdnodes/DeviceClass.html) getDeviceClass()
Returns:
class of type DeviceClass
getDiagramClass
public [DiagramClass](../ext/magicdraw/classes/mdkernel/DiagramClass.html) getDiagramClass()
Returns:
class of type DiagramClass
getDirectedRelationshipClass
public [DirectedRelationshipClass](../ext/magicdraw/classes/mdkernel/DirectedRelationshipClass.html) getDirectedRelationshipClass()
Returns:
class of type DirectedRelationshipClass
getDurationClass
public [DurationClass](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationClass.html) getDurationClass()
Returns:
class of type DurationClass
getDurationConstraintClass
public [DurationConstraintClass](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraintClass.html) getDurationConstraintClass()
Returns:
class of type DurationConstraintClass
getDurationIntervalClass
public [DurationIntervalClass](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationIntervalClass.html) getDurationIntervalClass()
Returns:
class of type DurationIntervalClass
getDurationObservationClass
public [DurationObservationClass](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservationClass.html) getDurationObservationClass()
Returns:
class of type DurationObservationClass
getElementClass
public [ElementClass](../ext/magicdraw/classes/mdkernel/ElementClass.html) getElementClass()
Returns:
class of type ElementClass
getElementImportClass
public [ElementImportClass](../ext/magicdraw/classes/mdkernel/ElementImportClass.html) getElementImportClass()
Returns:
class of type ElementImportClass
getElementValueClass
public [ElementValueClass](../ext/magicdraw/classes/mdkernel/ElementValueClass.html) getElementValueClass()
Returns:
class of type ElementValueClass
getEncapsulatedClassifierClass
public [EncapsulatedClassifierClass](../ext/magicdraw/compositestructures/mdports/EncapsulatedClassifierClass.html) getEncapsulatedClassifierClass()
Returns:
class of type EncapsulatedClassifierClass
getEnumerationClass
public [EnumerationClass](../ext/magicdraw/classes/mdkernel/EnumerationClass.html) getEnumerationClass()
Returns:
class of type EnumerationClass
getEnumerationLiteralClass
public [EnumerationLiteralClass](../ext/magicdraw/classes/mdkernel/EnumerationLiteralClass.html) getEnumerationLiteralClass()
Returns:
class of type EnumerationLiteralClass
getEventClass
public [EventClass](../ext/magicdraw/commonbehaviors/mdcommunications/EventClass.html) getEventClass()
Returns:
class of type EventClass
getExceptionHandlerClass
public [ExceptionHandlerClass](../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandlerClass.html) getExceptionHandlerClass()
Returns:
class of type ExceptionHandlerClass
getExecutableNodeClass
public [ExecutableNodeClass](../ext/magicdraw/activities/mdstructuredactivities/ExecutableNodeClass.html) getExecutableNodeClass()
Returns:
class of type ExecutableNodeClass
getExecutionEnvironmentClass
public [ExecutionEnvironmentClass](../ext/magicdraw/deployments/mdnodes/ExecutionEnvironmentClass.html) getExecutionEnvironmentClass()
Returns:
class of type ExecutionEnvironmentClass
getExecutionOccurrenceSpecificationClass
public [ExecutionOccurrenceSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecificationClass.html) getExecutionOccurrenceSpecificationClass()
Returns:
class of type ExecutionOccurrenceSpecificationClass
getExecutionSpecificationClass
public [ExecutionSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecificationClass.html) getExecutionSpecificationClass()
Returns:
class of type ExecutionSpecificationClass
getExpansionNodeClass
public [ExpansionNodeClass](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNodeClass.html) getExpansionNodeClass()
Returns:
class of type ExpansionNodeClass
getExpansionRegionClass
public [ExpansionRegionClass](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegionClass.html) getExpansionRegionClass()
Returns:
class of type ExpansionRegionClass
getExpressionClass
public [ExpressionClass](../ext/magicdraw/classes/mdkernel/ExpressionClass.html) getExpressionClass()
Returns:
class of type ExpressionClass
getExtendClass
public [ExtendClass](../ext/magicdraw/mdusecases/ExtendClass.html) getExtendClass()
Returns:
class of type ExtendClass
getExtensionClass
public [ExtensionClass](../ext/magicdraw/mdprofiles/ExtensionClass.html) getExtensionClass()
Returns:
class of type ExtensionClass
getExtensionEndClass
public [ExtensionEndClass](../ext/magicdraw/mdprofiles/ExtensionEndClass.html) getExtensionEndClass()
Returns:
class of type ExtensionEndClass
getExtensionPointClass
public [ExtensionPointClass](../ext/magicdraw/mdusecases/ExtensionPointClass.html) getExtensionPointClass()
Returns:
class of type ExtensionPointClass
getFeatureClass
public [FeatureClass](../ext/magicdraw/classes/mdkernel/FeatureClass.html) getFeatureClass()
Returns:
class of type FeatureClass
getFinalNodeClass
public [FinalNodeClass](../ext/magicdraw/activities/mdintermediateactivities/FinalNodeClass.html) getFinalNodeClass()
Returns:
class of type FinalNodeClass
getFinalStateClass
public [FinalStateClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalStateClass.html) getFinalStateClass()
Returns:
class of type FinalStateClass
getFlowFinalNodeClass
public [FlowFinalNodeClass](../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNodeClass.html) getFlowFinalNodeClass()
Returns:
class of type FlowFinalNodeClass
getForkNodeClass
public [ForkNodeClass](../ext/magicdraw/activities/mdintermediateactivities/ForkNodeClass.html) getForkNodeClass()
Returns:
class of type ForkNodeClass
getFunctionBehaviorClass
public [FunctionBehaviorClass](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehaviorClass.html) getFunctionBehaviorClass()
Returns:
class of type FunctionBehaviorClass
getGateClass
public [GateClass](../ext/magicdraw/interactions/mdfragments/GateClass.html) getGateClass()
Returns:
class of type GateClass
getGeneralOrderingClass
public [GeneralOrderingClass](../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrderingClass.html) getGeneralOrderingClass()
Returns:
class of type GeneralOrderingClass
getGeneralizationClass
public [GeneralizationClass](../ext/magicdraw/classes/mdkernel/GeneralizationClass.html) getGeneralizationClass()
Returns:
class of type GeneralizationClass
getGeneralizationSetClass
public [GeneralizationSetClass](../ext/magicdraw/classes/mdpowertypes/GeneralizationSetClass.html) getGeneralizationSetClass()
Returns:
class of type GeneralizationSetClass
getImageClass
public [ImageClass](../ext/magicdraw/mdprofiles/ImageClass.html) getImageClass()
Returns:
class of type ImageClass
getIncludeClass
public [IncludeClass](../ext/magicdraw/mdusecases/IncludeClass.html) getIncludeClass()
Returns:
class of type IncludeClass
getInformationFlowClass
public [InformationFlowClass](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlowClass.html) getInformationFlowClass()
Returns:
class of type InformationFlowClass
getInformationItemClass
public [InformationItemClass](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItemClass.html) getInformationItemClass()
Returns:
class of type InformationItemClass
getInitialNodeClass
public [InitialNodeClass](../ext/magicdraw/activities/mdbasicactivities/InitialNodeClass.html) getInitialNodeClass()
Returns:
class of type InitialNodeClass
getInputPinClass
public [InputPinClass](../ext/magicdraw/actions/mdbasicactions/InputPinClass.html) getInputPinClass()
Returns:
class of type InputPinClass
getInstanceSpecificationClass
public [InstanceSpecificationClass](../ext/magicdraw/classes/mdkernel/InstanceSpecificationClass.html) getInstanceSpecificationClass()
Returns:
class of type InstanceSpecificationClass
getInstanceValueClass
public [InstanceValueClass](../ext/magicdraw/classes/mdkernel/InstanceValueClass.html) getInstanceValueClass()
Returns:
class of type InstanceValueClass
getInteractionClass
public [InteractionClass](../ext/magicdraw/interactions/mdbasicinteractions/InteractionClass.html) getInteractionClass()
Returns:
class of type InteractionClass
getInteractionConstraintClass
public [InteractionConstraintClass](../ext/magicdraw/interactions/mdfragments/InteractionConstraintClass.html) getInteractionConstraintClass()
Returns:
class of type InteractionConstraintClass
getInteractionFragmentClass
public [InteractionFragmentClass](../ext/magicdraw/interactions/mdbasicinteractions/InteractionFragmentClass.html) getInteractionFragmentClass()
Returns:
class of type InteractionFragmentClass
getInteractionOperandClass
public [InteractionOperandClass](../ext/magicdraw/interactions/mdfragments/InteractionOperandClass.html) getInteractionOperandClass()
Returns:
class of type InteractionOperandClass
getInteractionUseClass
public [InteractionUseClass](../ext/magicdraw/interactions/mdfragments/InteractionUseClass.html) getInteractionUseClass()
Returns:
class of type InteractionUseClass
getInterfaceClass
public [InterfaceClass](../ext/magicdraw/classes/mdinterfaces/InterfaceClass.html) getInterfaceClass()
Returns:
class of type InterfaceClass
getInterfaceRealizationClass
public [InterfaceRealizationClass](../ext/magicdraw/classes/mdinterfaces/InterfaceRealizationClass.html) getInterfaceRealizationClass()
Returns:
class of type InterfaceRealizationClass
getInterruptibleActivityRegionClass
public [InterruptibleActivityRegionClass](../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegionClass.html) getInterruptibleActivityRegionClass()
Returns:
class of type InterruptibleActivityRegionClass
getIntervalClass
public [IntervalClass](../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalClass.html) getIntervalClass()
Returns:
class of type IntervalClass
getIntervalConstraintClass
public [IntervalConstraintClass](../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraintClass.html) getIntervalConstraintClass()
Returns:
class of type IntervalConstraintClass
getInvocationActionClass
public [InvocationActionClass](../ext/magicdraw/actions/mdbasicactions/InvocationActionClass.html) getInvocationActionClass()
Returns:
class of type InvocationActionClass
getJoinNodeClass
public [JoinNodeClass](../ext/magicdraw/activities/mdintermediateactivities/JoinNodeClass.html) getJoinNodeClass()
Returns:
class of type JoinNodeClass
getLifelineClass
public [LifelineClass](../ext/magicdraw/interactions/mdbasicinteractions/LifelineClass.html) getLifelineClass()
Returns:
class of type LifelineClass
getLinkActionClass
public [LinkActionClass](../ext/magicdraw/actions/mdintermediateactions/LinkActionClass.html) getLinkActionClass()
Returns:
class of type LinkActionClass
getLinkEndCreationDataClass
public [LinkEndCreationDataClass](../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationDataClass.html) getLinkEndCreationDataClass()
Returns:
class of type LinkEndCreationDataClass
getLinkEndDataClass
public [LinkEndDataClass](../ext/magicdraw/actions/mdintermediateactions/LinkEndDataClass.html) getLinkEndDataClass()
Returns:
class of type LinkEndDataClass
getLinkEndDestructionDataClass
public [LinkEndDestructionDataClass](../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionDataClass.html) getLinkEndDestructionDataClass()
Returns:
class of type LinkEndDestructionDataClass
getLiteralBooleanClass
public [LiteralBooleanClass](../ext/magicdraw/classes/mdkernel/LiteralBooleanClass.html) getLiteralBooleanClass()
Returns:
class of type LiteralBooleanClass
getLiteralIntegerClass
public [LiteralIntegerClass](../ext/magicdraw/classes/mdkernel/LiteralIntegerClass.html) getLiteralIntegerClass()
Returns:
class of type LiteralIntegerClass
getLiteralNullClass
public [LiteralNullClass](../ext/magicdraw/classes/mdkernel/LiteralNullClass.html) getLiteralNullClass()
Returns:
class of type LiteralNullClass
getLiteralRealClass
public [LiteralRealClass](../ext/magicdraw/classes/mdkernel/LiteralRealClass.html) getLiteralRealClass()
Returns:
class of type LiteralRealClass
getLiteralSpecificationClass
public [LiteralSpecificationClass](../ext/magicdraw/classes/mdkernel/LiteralSpecificationClass.html) getLiteralSpecificationClass()
Returns:
class of type LiteralSpecificationClass
getLiteralStringClass
public [LiteralStringClass](../ext/magicdraw/classes/mdkernel/LiteralStringClass.html) getLiteralStringClass()
Returns:
class of type LiteralStringClass
getLiteralUnlimitedNaturalClass
public [LiteralUnlimitedNaturalClass](../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNaturalClass.html) getLiteralUnlimitedNaturalClass()
Returns:
class of type LiteralUnlimitedNaturalClass
getLoopNodeClass
public [LoopNodeClass](../ext/magicdraw/activities/mdstructuredactivities/LoopNodeClass.html) getLoopNodeClass()
Returns:
class of type LoopNodeClass
getManifestationClass
public [ManifestationClass](../ext/magicdraw/deployments/mdartifacts/ManifestationClass.html) getManifestationClass()
Returns:
class of type ManifestationClass
getMergeNodeClass
public [MergeNodeClass](../ext/magicdraw/activities/mdintermediateactivities/MergeNodeClass.html) getMergeNodeClass()
Returns:
class of type MergeNodeClass
getMessageClass
public [MessageClass](../ext/magicdraw/interactions/mdbasicinteractions/MessageClass.html) getMessageClass()
Returns:
class of type MessageClass
getMessageEndClass
public [MessageEndClass](../ext/magicdraw/interactions/mdbasicinteractions/MessageEndClass.html) getMessageEndClass()
Returns:
class of type MessageEndClass
getMessageEventClass
public [MessageEventClass](../ext/magicdraw/commonbehaviors/mdcommunications/MessageEventClass.html) getMessageEventClass()
Returns:
class of type MessageEventClass
getMessageOccurrenceSpecificationClass
public [MessageOccurrenceSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecificationClass.html) getMessageOccurrenceSpecificationClass()
Returns:
class of type MessageOccurrenceSpecificationClass
getModelClass
public [ModelClass](../ext/magicdraw/auxiliaryconstructs/mdmodels/ModelClass.html) getModelClass()
Returns:
class of type ModelClass
getMultiplicityElementClass
public [MultiplicityElementClass](../ext/magicdraw/classes/mdkernel/MultiplicityElementClass.html) getMultiplicityElementClass()
Returns:
class of type MultiplicityElementClass
getNamedElementClass
public [NamedElementClass](../ext/magicdraw/classes/mdkernel/NamedElementClass.html) getNamedElementClass()
Returns:
class of type NamedElementClass
getNamespaceClass
public [NamespaceClass](../ext/magicdraw/classes/mdkernel/NamespaceClass.html) getNamespaceClass()
Returns:
class of type NamespaceClass
getNodeClass
public [NodeClass](../ext/magicdraw/deployments/mdnodes/NodeClass.html) getNodeClass()
Returns:
class of type NodeClass
getObjectFlowClass
public [ObjectFlowClass](../ext/magicdraw/activities/mdbasicactivities/ObjectFlowClass.html) getObjectFlowClass()
Returns:
class of type ObjectFlowClass
getObjectNodeClass
public [ObjectNodeClass](../ext/magicdraw/activities/mdbasicactivities/ObjectNodeClass.html) getObjectNodeClass()
Returns:
class of type ObjectNodeClass
getObservationClass
public [ObservationClass](../ext/magicdraw/commonbehaviors/mdsimpletime/ObservationClass.html) getObservationClass()
Returns:
class of type ObservationClass
getOccurrenceSpecificationClass
public [OccurrenceSpecificationClass](../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecificationClass.html) getOccurrenceSpecificationClass()
Returns:
class of type OccurrenceSpecificationClass
getOpaqueActionClass
public [OpaqueActionClass](../ext/magicdraw/actions/mdbasicactions/OpaqueActionClass.html) getOpaqueActionClass()
Returns:
class of type OpaqueActionClass
getOpaqueBehaviorClass
public [OpaqueBehaviorClass](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehaviorClass.html) getOpaqueBehaviorClass()
Returns:
class of type OpaqueBehaviorClass
getOpaqueExpressionClass
public [OpaqueExpressionClass](../ext/magicdraw/classes/mdkernel/OpaqueExpressionClass.html) getOpaqueExpressionClass()
Returns:
class of type OpaqueExpressionClass
getOperationClass
public [OperationClass](../ext/magicdraw/classes/mdkernel/OperationClass.html) getOperationClass()
Returns:
class of type OperationClass
getOperationTemplateParameterClass
public [OperationTemplateParameterClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameterClass.html) getOperationTemplateParameterClass()
Returns:
class of type OperationTemplateParameterClass
getOutputPinClass
public [OutputPinClass](../ext/magicdraw/actions/mdbasicactions/OutputPinClass.html) getOutputPinClass()
Returns:
class of type OutputPinClass
getPackageClass
public [PackageClass](../ext/magicdraw/classes/mdkernel/PackageClass.html) getPackageClass()
Returns:
class of type PackageClass
getPackageImportClass
public [PackageImportClass](../ext/magicdraw/classes/mdkernel/PackageImportClass.html) getPackageImportClass()
Returns:
class of type PackageImportClass
getPackageMergeClass
public [PackageMergeClass](../ext/magicdraw/classes/mdkernel/PackageMergeClass.html) getPackageMergeClass()
Returns:
class of type PackageMergeClass
getPackageableElementClass
public [PackageableElementClass](../ext/magicdraw/classes/mdkernel/PackageableElementClass.html) getPackageableElementClass()
Returns:
class of type PackageableElementClass
getParameterClass
public [ParameterClass](../ext/magicdraw/classes/mdkernel/ParameterClass.html) getParameterClass()
Returns:
class of type ParameterClass
getParameterSetClass
public [ParameterSetClass](../ext/magicdraw/activities/mdcompleteactivities/ParameterSetClass.html) getParameterSetClass()
Returns:
class of type ParameterSetClass
getParameterableElementClass
public [ParameterableElementClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElementClass.html) getParameterableElementClass()
Returns:
class of type ParameterableElementClass
getPartDecompositionClass
public [PartDecompositionClass](../ext/magicdraw/interactions/mdfragments/PartDecompositionClass.html) getPartDecompositionClass()
Returns:
class of type PartDecompositionClass
getPinClass
public [PinClass](../ext/magicdraw/actions/mdbasicactions/PinClass.html) getPinClass()
Returns:
class of type PinClass
getPortClass
public [PortClass](../ext/magicdraw/compositestructures/mdports/PortClass.html) getPortClass()
Returns:
class of type PortClass
getPrimitiveTypeClass
public [PrimitiveTypeClass](../ext/magicdraw/classes/mdkernel/PrimitiveTypeClass.html) getPrimitiveTypeClass()
Returns:
class of type PrimitiveTypeClass
getProfileClass
public [ProfileClass](../ext/magicdraw/mdprofiles/ProfileClass.html) getProfileClass()
Returns:
class of type ProfileClass
getProfileApplicationClass
public [ProfileApplicationClass](../ext/magicdraw/mdprofiles/ProfileApplicationClass.html) getProfileApplicationClass()
Returns:
class of type ProfileApplicationClass
getPropertyClass
public [PropertyClass](../ext/magicdraw/classes/mdkernel/PropertyClass.html) getPropertyClass()
Returns:
class of type PropertyClass
getProtocolConformanceClass
public [ProtocolConformanceClass](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformanceClass.html) getProtocolConformanceClass()
Returns:
class of type ProtocolConformanceClass
getProtocolStateMachineClass
public [ProtocolStateMachineClass](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachineClass.html) getProtocolStateMachineClass()
Returns:
class of type ProtocolStateMachineClass
getProtocolTransitionClass
public [ProtocolTransitionClass](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransitionClass.html) getProtocolTransitionClass()
Returns:
class of type ProtocolTransitionClass
getPseudostateClass
public [PseudostateClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/PseudostateClass.html) getPseudostateClass()
Returns:
class of type PseudostateClass
getQualifierValueClass
public [QualifierValueClass](../ext/magicdraw/actions/mdcompleteactions/QualifierValueClass.html) getQualifierValueClass()
Returns:
class of type QualifierValueClass
getRaiseExceptionActionClass
public [RaiseExceptionActionClass](../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionActionClass.html) getRaiseExceptionActionClass()
Returns:
class of type RaiseExceptionActionClass
getReadExtentActionClass
public [ReadExtentActionClass](../ext/magicdraw/actions/mdcompleteactions/ReadExtentActionClass.html) getReadExtentActionClass()
Returns:
class of type ReadExtentActionClass
getReadIsClassifiedObjectActionClass
public [ReadIsClassifiedObjectActionClass](../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectActionClass.html) getReadIsClassifiedObjectActionClass()
Returns:
class of type ReadIsClassifiedObjectActionClass
getReadLinkActionClass
public [ReadLinkActionClass](../ext/magicdraw/actions/mdintermediateactions/ReadLinkActionClass.html) getReadLinkActionClass()
Returns:
class of type ReadLinkActionClass
getReadLinkObjectEndActionClass
public [ReadLinkObjectEndActionClass](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndActionClass.html) getReadLinkObjectEndActionClass()
Returns:
class of type ReadLinkObjectEndActionClass
getReadLinkObjectEndQualifierActionClass
public [ReadLinkObjectEndQualifierActionClass](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierActionClass.html) getReadLinkObjectEndQualifierActionClass()
Returns:
class of type ReadLinkObjectEndQualifierActionClass
getReadSelfActionClass
public [ReadSelfActionClass](../ext/magicdraw/actions/mdintermediateactions/ReadSelfActionClass.html) getReadSelfActionClass()
Returns:
class of type ReadSelfActionClass
getReadStructuralFeatureActionClass
public [ReadStructuralFeatureActionClass](../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureActionClass.html) getReadStructuralFeatureActionClass()
Returns:
class of type ReadStructuralFeatureActionClass
getReadVariableActionClass
public [ReadVariableActionClass](../ext/magicdraw/actions/mdstructuredactions/ReadVariableActionClass.html) getReadVariableActionClass()
Returns:
class of type ReadVariableActionClass
getRealizationClass
public [RealizationClass](../ext/magicdraw/classes/mddependencies/RealizationClass.html) getRealizationClass()
Returns:
class of type RealizationClass
getReceptionClass
public [ReceptionClass](../ext/magicdraw/commonbehaviors/mdcommunications/ReceptionClass.html) getReceptionClass()
Returns:
class of type ReceptionClass
getReclassifyObjectActionClass
public [ReclassifyObjectActionClass](../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectActionClass.html) getReclassifyObjectActionClass()
Returns:
class of type ReclassifyObjectActionClass
getRedefinableElementClass
public [RedefinableElementClass](../ext/magicdraw/classes/mdkernel/RedefinableElementClass.html) getRedefinableElementClass()
Returns:
class of type RedefinableElementClass
getRedefinableTemplateSignatureClass
public [RedefinableTemplateSignatureClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignatureClass.html) getRedefinableTemplateSignatureClass()
Returns:
class of type RedefinableTemplateSignatureClass
getReduceActionClass
public [ReduceActionClass](../ext/magicdraw/actions/mdcompleteactions/ReduceActionClass.html) getReduceActionClass()
Returns:
class of type ReduceActionClass
getRegionClass
public [RegionClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/RegionClass.html) getRegionClass()
Returns:
class of type RegionClass
getRelationshipClass
public [RelationshipClass](../ext/magicdraw/classes/mdkernel/RelationshipClass.html) getRelationshipClass()
Returns:
class of type RelationshipClass
getRemoveStructuralFeatureValueActionClass
public [RemoveStructuralFeatureValueActionClass](../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueActionClass.html) getRemoveStructuralFeatureValueActionClass()
Returns:
class of type RemoveStructuralFeatureValueActionClass
getRemoveVariableValueActionClass
public [RemoveVariableValueActionClass](../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueActionClass.html) getRemoveVariableValueActionClass()
Returns:
class of type RemoveVariableValueActionClass
getReplyActionClass
public [ReplyActionClass](../ext/magicdraw/actions/mdcompleteactions/ReplyActionClass.html) getReplyActionClass()
Returns:
class of type ReplyActionClass
getSendObjectActionClass
public [SendObjectActionClass](../ext/magicdraw/actions/mdintermediateactions/SendObjectActionClass.html) getSendObjectActionClass()
Returns:
class of type SendObjectActionClass
getSendSignalActionClass
public [SendSignalActionClass](../ext/magicdraw/actions/mdbasicactions/SendSignalActionClass.html) getSendSignalActionClass()
Returns:
class of type SendSignalActionClass
getSequenceNodeClass
public [SequenceNodeClass](../ext/magicdraw/activities/mdstructuredactivities/SequenceNodeClass.html) getSequenceNodeClass()
Returns:
class of type SequenceNodeClass
getSignalClass
public [SignalClass](../ext/magicdraw/commonbehaviors/mdcommunications/SignalClass.html) getSignalClass()
Returns:
class of type SignalClass
getSignalEventClass
public [SignalEventClass](../ext/magicdraw/commonbehaviors/mdcommunications/SignalEventClass.html) getSignalEventClass()
Returns:
class of type SignalEventClass
getSlotClass
public [SlotClass](../ext/magicdraw/classes/mdkernel/SlotClass.html) getSlotClass()
Returns:
class of type SlotClass
getStartClassifierBehaviorActionClass
public [StartClassifierBehaviorActionClass](../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorActionClass.html) getStartClassifierBehaviorActionClass()
Returns:
class of type StartClassifierBehaviorActionClass
getStartObjectBehaviorActionClass
public [StartObjectBehaviorActionClass](../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorActionClass.html) getStartObjectBehaviorActionClass()
Returns:
class of type StartObjectBehaviorActionClass
getStateClass
public [StateClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateClass.html) getStateClass()
Returns:
class of type StateClass
getStateInvariantClass
public [StateInvariantClass](../ext/magicdraw/interactions/mdbasicinteractions/StateInvariantClass.html) getStateInvariantClass()
Returns:
class of type StateInvariantClass
getStateMachineClass
public [StateMachineClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachineClass.html) getStateMachineClass()
Returns:
class of type StateMachineClass
getStereotypeClass
public [StereotypeClass](../ext/magicdraw/mdprofiles/StereotypeClass.html) getStereotypeClass()
Returns:
class of type StereotypeClass
getStringExpressionClass
public [StringExpressionClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpressionClass.html) getStringExpressionClass()
Returns:
class of type StringExpressionClass
getStructuralFeatureClass
public [StructuralFeatureClass](../ext/magicdraw/classes/mdkernel/StructuralFeatureClass.html) getStructuralFeatureClass()
Returns:
class of type StructuralFeatureClass
getStructuralFeatureActionClass
public [StructuralFeatureActionClass](../ext/magicdraw/actions/mdintermediateactions/StructuralFeatureActionClass.html) getStructuralFeatureActionClass()
Returns:
class of type StructuralFeatureActionClass
getStructuredActivityNodeClass
public [StructuredActivityNodeClass](../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNodeClass.html) getStructuredActivityNodeClass()
Returns:
class of type StructuredActivityNodeClass
getStructuredClassifierClass
public [StructuredClassifierClass](../ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifierClass.html) getStructuredClassifierClass()
Returns:
class of type StructuredClassifierClass
getSubstitutionClass
public [SubstitutionClass](../ext/magicdraw/classes/mddependencies/SubstitutionClass.html) getSubstitutionClass()
Returns:
class of type SubstitutionClass
getTemplateBindingClass
public [TemplateBindingClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBindingClass.html) getTemplateBindingClass()
Returns:
class of type TemplateBindingClass
getTemplateParameterClass
public [TemplateParameterClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterClass.html) getTemplateParameterClass()
Returns:
class of type TemplateParameterClass
getTemplateParameterSubstitutionClass
public [TemplateParameterSubstitutionClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitutionClass.html) getTemplateParameterSubstitutionClass()
Returns:
class of type TemplateParameterSubstitutionClass
getTemplateSignatureClass
public [TemplateSignatureClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignatureClass.html) getTemplateSignatureClass()
Returns:
class of type TemplateSignatureClass
getTemplateableElementClass
public [TemplateableElementClass](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElementClass.html) getTemplateableElementClass()
Returns:
class of type TemplateableElementClass
getTestIdentityActionClass
public [TestIdentityActionClass](../ext/magicdraw/actions/mdintermediateactions/TestIdentityActionClass.html) getTestIdentityActionClass()
Returns:
class of type TestIdentityActionClass
getTimeConstraintClass
public [TimeConstraintClass](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraintClass.html) getTimeConstraintClass()
Returns:
class of type TimeConstraintClass
getTimeEventClass
public [TimeEventClass](../ext/magicdraw/commonbehaviors/mdcommunications/TimeEventClass.html) getTimeEventClass()
Returns:
class of type TimeEventClass
getTimeExpressionClass
public [TimeExpressionClass](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpressionClass.html) getTimeExpressionClass()
Returns:
class of type TimeExpressionClass
getTimeIntervalClass
public [TimeIntervalClass](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeIntervalClass.html) getTimeIntervalClass()
Returns:
class of type TimeIntervalClass
getTimeObservationClass
public [TimeObservationClass](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservationClass.html) getTimeObservationClass()
Returns:
class of type TimeObservationClass
getTransitionClass
public [TransitionClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/TransitionClass.html) getTransitionClass()
Returns:
class of type TransitionClass
getTriggerClass
public [TriggerClass](../ext/magicdraw/commonbehaviors/mdcommunications/TriggerClass.html) getTriggerClass()
Returns:
class of type TriggerClass
getTypeClass
public [TypeClass](../ext/magicdraw/classes/mdkernel/TypeClass.html) getTypeClass()
Returns:
class of type TypeClass
getTypedElementClass
public [TypedElementClass](../ext/magicdraw/classes/mdkernel/TypedElementClass.html) getTypedElementClass()
Returns:
class of type TypedElementClass
getUnmarshallActionClass
public [UnmarshallActionClass](../ext/magicdraw/actions/mdcompleteactions/UnmarshallActionClass.html) getUnmarshallActionClass()
Returns:
class of type UnmarshallActionClass
getUsageClass
public [UsageClass](../ext/magicdraw/classes/mddependencies/UsageClass.html) getUsageClass()
Returns:
class of type UsageClass
getUseCaseClass
public [UseCaseClass](../ext/magicdraw/mdusecases/UseCaseClass.html) getUseCaseClass()
Returns:
class of type UseCaseClass
getValuePinClass
public [ValuePinClass](../ext/magicdraw/actions/mdbasicactions/ValuePinClass.html) getValuePinClass()
Returns:
class of type ValuePinClass
getValueSpecificationClass
public [ValueSpecificationClass](../ext/magicdraw/classes/mdkernel/ValueSpecificationClass.html) getValueSpecificationClass()
Returns:
class of type ValueSpecificationClass
getValueSpecificationActionClass
public [ValueSpecificationActionClass](../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationActionClass.html) getValueSpecificationActionClass()
Returns:
class of type ValueSpecificationActionClass
getVariableClass
public [VariableClass](../ext/magicdraw/activities/mdstructuredactivities/VariableClass.html) getVariableClass()
Returns:
class of type VariableClass
getVariableActionClass
public [VariableActionClass](../ext/magicdraw/actions/mdstructuredactions/VariableActionClass.html) getVariableActionClass()
Returns:
class of type VariableActionClass
getVertexClass
public [VertexClass](../ext/magicdraw/statemachines/mdbehaviorstatemachines/VertexClass.html) getVertexClass()
Returns:
class of type VertexClass
getWriteLinkActionClass
public [WriteLinkActionClass](../ext/magicdraw/actions/mdintermediateactions/WriteLinkActionClass.html) getWriteLinkActionClass()
Returns:
class of type WriteLinkActionClass
getWriteStructuralFeatureActionClass
public [WriteStructuralFeatureActionClass](../ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureActionClass.html) getWriteStructuralFeatureActionClass()
Returns:
class of type WriteStructuralFeatureActionClass
getWriteVariableActionClass
public [WriteVariableActionClass](../ext/magicdraw/actions/mdstructuredactions/WriteVariableActionClass.html) getWriteVariableActionClass()
Returns:
class of type WriteVariableActionClass
getTaggedValueClass
public [TaggedValueClass](../ext/magicdraw/classes/mdkernel/TaggedValueClass.html) getTaggedValueClass()
Returns:
class of type TaggedValueClass
getBooleanTaggedValueClass
public [BooleanTaggedValueClass](../ext/magicdraw/classes/mdkernel/BooleanTaggedValueClass.html) getBooleanTaggedValueClass()
Returns:
class of type BooleanTaggedValueClass
getIntegerTaggedValueClass
public [IntegerTaggedValueClass](../ext/magicdraw/classes/mdkernel/IntegerTaggedValueClass.html) getIntegerTaggedValueClass()
Returns:
class of type IntegerTaggedValueClass
getRealTaggedValueClass
public [RealTaggedValueClass](../ext/magicdraw/classes/mdkernel/RealTaggedValueClass.html) getRealTaggedValueClass()
Returns:
class of type RealTaggedValueClass
getStringTaggedValueClass
public [StringTaggedValueClass](../ext/magicdraw/classes/mdkernel/StringTaggedValueClass.html) getStringTaggedValueClass()
Returns:
class of type StringTaggedValueClass
getElementTaggedValueClass
public [ElementTaggedValueClass](../ext/magicdraw/classes/mdkernel/ElementTaggedValueClass.html) getElementTaggedValueClass()
Returns:
class of type ElementTaggedValueClass
createAbstractionInstance
public [Abstraction](../ext/magicdraw/classes/mddependencies/Abstraction.html) createAbstractionInstance()
Returns:
created instance of type Abstraction
createAcceptCallActionInstance
public [AcceptCallAction](../ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html) createAcceptCallActionInstance()
Returns:
created instance of type AcceptCallAction
createAcceptEventActionInstance
public [AcceptEventAction](../ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html) createAcceptEventActionInstance()
Returns:
created instance of type AcceptEventAction
createActionExecutionSpecificationInstance
public [ActionExecutionSpecification](../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html) createActionExecutionSpecificationInstance()
Returns:
created instance of type ActionExecutionSpecification
createActionInputPinInstance
public [ActionInputPin](../ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html) createActionInputPinInstance()
Returns:
created instance of type ActionInputPin
createActivityInstance
public [Activity](../ext/magicdraw/activities/mdfundamentalactivities/Activity.html) createActivityInstance()
Returns:
created instance of type Activity
createActivityFinalNodeInstance
public [ActivityFinalNode](../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html) createActivityFinalNodeInstance()
Returns:
created instance of type ActivityFinalNode
createActivityParameterNodeInstance
public [ActivityParameterNode](../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html) createActivityParameterNodeInstance()
Returns:
created instance of type ActivityParameterNode
createActivityPartitionInstance
public [ActivityPartition](../ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html) createActivityPartitionInstance()
Returns:
created instance of type ActivityPartition
createActorInstance
public [Actor](../ext/magicdraw/mdusecases/Actor.html) createActorInstance()
Returns:
created instance of type Actor
createAddStructuralFeatureValueActionInstance
public [AddStructuralFeatureValueAction](../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html) createAddStructuralFeatureValueActionInstance()
Returns:
created instance of type AddStructuralFeatureValueAction
createAddVariableValueActionInstance
public [AddVariableValueAction](../ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html) createAddVariableValueActionInstance()
Returns:
created instance of type AddVariableValueAction
createAnyReceiveEventInstance
public [AnyReceiveEvent](../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html) createAnyReceiveEventInstance()
Returns:
created instance of type AnyReceiveEvent
createArtifactInstance
public [Artifact](../ext/magicdraw/deployments/mdartifacts/Artifact.html) createArtifactInstance()
Returns:
created instance of type Artifact
createAssociationInstance
public [Association](../ext/magicdraw/classes/mdkernel/Association.html) createAssociationInstance()
Returns:
created instance of type Association
createAssociationClassInstance
public [AssociationClass](../ext/magicdraw/classes/mdassociationclasses/AssociationClass.html) createAssociationClassInstance()
Returns:
created instance of type AssociationClass
createBehaviorExecutionSpecificationInstance
public [BehaviorExecutionSpecification](../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html) createBehaviorExecutionSpecificationInstance()
Returns:
created instance of type BehaviorExecutionSpecification
createBroadcastSignalActionInstance
public [BroadcastSignalAction](../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html) createBroadcastSignalActionInstance()
Returns:
created instance of type BroadcastSignalAction
createCallBehaviorActionInstance
public [CallBehaviorAction](../ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html) createCallBehaviorActionInstance()
Returns:
created instance of type CallBehaviorAction
createCallEventInstance
public [CallEvent](../ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html) createCallEventInstance()
Returns:
created instance of type CallEvent
createCallOperationActionInstance
public [CallOperationAction](../ext/magicdraw/actions/mdbasicactions/CallOperationAction.html) createCallOperationActionInstance()
Returns:
created instance of type CallOperationAction
createCentralBufferNodeInstance
public [CentralBufferNode](../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html) createCentralBufferNodeInstance()
Returns:
created instance of type CentralBufferNode
createChangeEventInstance
public [ChangeEvent](../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html) createChangeEventInstance()
Returns:
created instance of type ChangeEvent
createClassInstance
public [Class](../ext/magicdraw/classes/mdkernel/Class.html) createClassInstance()
Returns:
created instance of type Class
createClassifierTemplateParameterInstance
public [ClassifierTemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html) createClassifierTemplateParameterInstance()
Returns:
created instance of type ClassifierTemplateParameter
createClauseInstance
public [Clause](../ext/magicdraw/activities/mdstructuredactivities/Clause.html) createClauseInstance()
Returns:
created instance of type Clause
createClearAssociationActionInstance
public [ClearAssociationAction](../ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html) createClearAssociationActionInstance()
Returns:
created instance of type ClearAssociationAction
createClearStructuralFeatureActionInstance
public [ClearStructuralFeatureAction](../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html) createClearStructuralFeatureActionInstance()
Returns:
created instance of type ClearStructuralFeatureAction
createClearVariableActionInstance
public [ClearVariableAction](../ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html) createClearVariableActionInstance()
Returns:
created instance of type ClearVariableAction
createCollaborationInstance
public [Collaboration](../ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html) createCollaborationInstance()
Returns:
created instance of type Collaboration
createCollaborationUseInstance
public [CollaborationUse](../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html) createCollaborationUseInstance()
Returns:
created instance of type CollaborationUse
createCombinedFragmentInstance
public [CombinedFragment](../ext/magicdraw/interactions/mdfragments/CombinedFragment.html) createCombinedFragmentInstance()
Returns:
created instance of type CombinedFragment
createCommentInstance
public [Comment](../ext/magicdraw/classes/mdkernel/Comment.html) createCommentInstance()
Returns:
created instance of type Comment
createCommunicationPathInstance
public [CommunicationPath](../ext/magicdraw/deployments/mdnodes/CommunicationPath.html) createCommunicationPathInstance()
Returns:
created instance of type CommunicationPath
createComponentInstance
public [Component](../ext/magicdraw/components/mdbasiccomponents/Component.html) createComponentInstance()
Returns:
created instance of type Component
createComponentRealizationInstance
public [ComponentRealization](../ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html) createComponentRealizationInstance()
Returns:
created instance of type ComponentRealization
createConditionalNodeInstance
public [ConditionalNode](../ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html) createConditionalNodeInstance()
Returns:
created instance of type ConditionalNode
createConnectableElementTemplateParameterInstance
public [ConnectableElementTemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html) createConnectableElementTemplateParameterInstance()
Returns:
created instance of type ConnectableElementTemplateParameter
createConnectionPointReferenceInstance
public [ConnectionPointReference](../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html) createConnectionPointReferenceInstance()
Returns:
created instance of type ConnectionPointReference
createConnectorInstance
public [Connector](../ext/magicdraw/compositestructures/mdinternalstructures/Connector.html) createConnectorInstance()
Returns:
created instance of type Connector
createConnectorEndInstance
public [ConnectorEnd](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html) createConnectorEndInstance()
Returns:
created instance of type ConnectorEnd
createConsiderIgnoreFragmentInstance
public [ConsiderIgnoreFragment](../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html) createConsiderIgnoreFragmentInstance()
Returns:
created instance of type ConsiderIgnoreFragment
createConstraintInstance
public [Constraint](../ext/magicdraw/classes/mdkernel/Constraint.html) createConstraintInstance()
Returns:
created instance of type Constraint
createContinuationInstance
public [Continuation](../ext/magicdraw/interactions/mdfragments/Continuation.html) createContinuationInstance()
Returns:
created instance of type Continuation
createControlFlowInstance
public [ControlFlow](../ext/magicdraw/activities/mdbasicactivities/ControlFlow.html) createControlFlowInstance()
Returns:
created instance of type ControlFlow
createCreateLinkActionInstance
public [CreateLinkAction](../ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html) createCreateLinkActionInstance()
Returns:
created instance of type CreateLinkAction
createCreateLinkObjectActionInstance
public [CreateLinkObjectAction](../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html) createCreateLinkObjectActionInstance()
Returns:
created instance of type CreateLinkObjectAction
createCreateObjectActionInstance
public [CreateObjectAction](../ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html) createCreateObjectActionInstance()
Returns:
created instance of type CreateObjectAction
createDataStoreNodeInstance
public [DataStoreNode](../ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html) createDataStoreNodeInstance()
Returns:
created instance of type DataStoreNode
createDataTypeInstance
public [DataType](../ext/magicdraw/classes/mdkernel/DataType.html) createDataTypeInstance()
Returns:
created instance of type DataType
createDecisionNodeInstance
public [DecisionNode](../ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html) createDecisionNodeInstance()
Returns:
created instance of type DecisionNode
createDependencyInstance
public [Dependency](../ext/magicdraw/classes/mddependencies/Dependency.html) createDependencyInstance()
Returns:
created instance of type Dependency
createDeploymentInstance
public [Deployment](../ext/magicdraw/deployments/mdnodes/Deployment.html) createDeploymentInstance()
Returns:
created instance of type Deployment
createDeploymentSpecificationInstance
public [DeploymentSpecification](../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html) createDeploymentSpecificationInstance()
Returns:
created instance of type DeploymentSpecification
createDestroyLinkActionInstance
public [DestroyLinkAction](../ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html) createDestroyLinkActionInstance()
Returns:
created instance of type DestroyLinkAction
createDestroyObjectActionInstance
public [DestroyObjectAction](../ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html) createDestroyObjectActionInstance()
Returns:
created instance of type DestroyObjectAction
createDestructionOccurrenceSpecificationInstance
public [DestructionOccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html) createDestructionOccurrenceSpecificationInstance()
Returns:
created instance of type DestructionOccurrenceSpecification
createDeviceInstance
public [Device](../ext/magicdraw/deployments/mdnodes/Device.html) createDeviceInstance()
Returns:
created instance of type Device
createDiagramInstance
public [Diagram](../ext/magicdraw/classes/mdkernel/Diagram.html) createDiagramInstance()
Returns:
created instance of type Diagram
createDurationInstance
public [Duration](../ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html) createDurationInstance()
Returns:
created instance of type Duration
createDurationConstraintInstance
public [DurationConstraint](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) createDurationConstraintInstance()
Returns:
created instance of type DurationConstraint
createDurationIntervalInstance
public [DurationInterval](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html) createDurationIntervalInstance()
Returns:
created instance of type DurationInterval
createDurationObservationInstance
public [DurationObservation](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html) createDurationObservationInstance()
Returns:
created instance of type DurationObservation
createElementImportInstance
public [ElementImport](../ext/magicdraw/classes/mdkernel/ElementImport.html) createElementImportInstance()
Returns:
created instance of type ElementImport
createElementValueInstance
public [ElementValue](../ext/magicdraw/classes/mdkernel/ElementValue.html) createElementValueInstance()
Returns:
created instance of type ElementValue
createEnumerationInstance
public [Enumeration](../ext/magicdraw/classes/mdkernel/Enumeration.html) createEnumerationInstance()
Returns:
created instance of type Enumeration
createEnumerationLiteralInstance
public [EnumerationLiteral](../ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) createEnumerationLiteralInstance()
Returns:
created instance of type EnumerationLiteral
createExceptionHandlerInstance
public [ExceptionHandler](../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html) createExceptionHandlerInstance()
Returns:
created instance of type ExceptionHandler
createExecutionEnvironmentInstance
public [ExecutionEnvironment](../ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html) createExecutionEnvironmentInstance()
Returns:
created instance of type ExecutionEnvironment
createExecutionOccurrenceSpecificationInstance
public [ExecutionOccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html) createExecutionOccurrenceSpecificationInstance()
Returns:
created instance of type ExecutionOccurrenceSpecification
createExpansionNodeInstance
public [ExpansionNode](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html) createExpansionNodeInstance()
Returns:
created instance of type ExpansionNode
createExpansionRegionInstance
public [ExpansionRegion](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html) createExpansionRegionInstance()
Returns:
created instance of type ExpansionRegion
createExpressionInstance
public [Expression](../ext/magicdraw/classes/mdkernel/Expression.html) createExpressionInstance()
Returns:
created instance of type Expression
createExtendInstance
public [Extend](../ext/magicdraw/mdusecases/Extend.html) createExtendInstance()
Returns:
created instance of type Extend
createExtensionInstance
public [Extension](../ext/magicdraw/mdprofiles/Extension.html) createExtensionInstance()
Returns:
created instance of type Extension
createExtensionEndInstance
public [ExtensionEnd](../ext/magicdraw/mdprofiles/ExtensionEnd.html) createExtensionEndInstance()
Returns:
created instance of type ExtensionEnd
createExtensionPointInstance
public [ExtensionPoint](../ext/magicdraw/mdusecases/ExtensionPoint.html) createExtensionPointInstance()
Returns:
created instance of type ExtensionPoint
createFinalStateInstance
public [FinalState](../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html) createFinalStateInstance()
Returns:
created instance of type FinalState
createFlowFinalNodeInstance
public [FlowFinalNode](../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html) createFlowFinalNodeInstance()
Returns:
created instance of type FlowFinalNode
createForkNodeInstance
public [ForkNode](../ext/magicdraw/activities/mdintermediateactivities/ForkNode.html) createForkNodeInstance()
Returns:
created instance of type ForkNode
createFunctionBehaviorInstance
public [FunctionBehavior](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html) createFunctionBehaviorInstance()
Returns:
created instance of type FunctionBehavior
createGateInstance
public [Gate](../ext/magicdraw/interactions/mdfragments/Gate.html) createGateInstance()
Returns:
created instance of type Gate
createGeneralOrderingInstance
public [GeneralOrdering](../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html) createGeneralOrderingInstance()
Returns:
created instance of type GeneralOrdering
createGeneralizationInstance
public [Generalization](../ext/magicdraw/classes/mdkernel/Generalization.html) createGeneralizationInstance()
Returns:
created instance of type Generalization
createGeneralizationSetInstance
public [GeneralizationSet](../ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html) createGeneralizationSetInstance()
Returns:
created instance of type GeneralizationSet
createImageInstance
public [Image](../ext/magicdraw/mdprofiles/Image.html) createImageInstance()
Returns:
created instance of type Image
createIncludeInstance
public [Include](../ext/magicdraw/mdusecases/Include.html) createIncludeInstance()
Returns:
created instance of type Include
createInformationFlowInstance
public [InformationFlow](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html) createInformationFlowInstance()
Returns:
created instance of type InformationFlow
createInformationItemInstance
public [InformationItem](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html) createInformationItemInstance()
Returns:
created instance of type InformationItem
createInitialNodeInstance
public [InitialNode](../ext/magicdraw/activities/mdbasicactivities/InitialNode.html) createInitialNodeInstance()
Returns:
created instance of type InitialNode
createInputPinInstance
public [InputPin](../ext/magicdraw/actions/mdbasicactions/InputPin.html) createInputPinInstance()
Returns:
created instance of type InputPin
createInstanceSpecificationInstance
public [InstanceSpecification](../ext/magicdraw/classes/mdkernel/InstanceSpecification.html) createInstanceSpecificationInstance()
Returns:
created instance of type InstanceSpecification
createInstanceValueInstance
public [InstanceValue](../ext/magicdraw/classes/mdkernel/InstanceValue.html) createInstanceValueInstance()
Returns:
created instance of type InstanceValue
createInteractionInstance
public [Interaction](../ext/magicdraw/interactions/mdbasicinteractions/Interaction.html) createInteractionInstance()
Returns:
created instance of type Interaction
createInteractionConstraintInstance
public [InteractionConstraint](../ext/magicdraw/interactions/mdfragments/InteractionConstraint.html) createInteractionConstraintInstance()
Returns:
created instance of type InteractionConstraint
createInteractionOperandInstance
public [InteractionOperand](../ext/magicdraw/interactions/mdfragments/InteractionOperand.html) createInteractionOperandInstance()
Returns:
created instance of type InteractionOperand
createInteractionUseInstance
public [InteractionUse](../ext/magicdraw/interactions/mdfragments/InteractionUse.html) createInteractionUseInstance()
Returns:
created instance of type InteractionUse
createInterfaceInstance
public [Interface](../ext/magicdraw/classes/mdinterfaces/Interface.html) createInterfaceInstance()
Returns:
created instance of type Interface
createInterfaceRealizationInstance
public [InterfaceRealization](../ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html) createInterfaceRealizationInstance()
Returns:
created instance of type InterfaceRealization
createInterruptibleActivityRegionInstance
public [InterruptibleActivityRegion](../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html) createInterruptibleActivityRegionInstance()
Returns:
created instance of type InterruptibleActivityRegion
createIntervalInstance
public [Interval](../ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html) createIntervalInstance()
Returns:
created instance of type Interval
createIntervalConstraintInstance
public [IntervalConstraint](../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html) createIntervalConstraintInstance()
Returns:
created instance of type IntervalConstraint
createJoinNodeInstance
public [JoinNode](../ext/magicdraw/activities/mdintermediateactivities/JoinNode.html) createJoinNodeInstance()
Returns:
created instance of type JoinNode
createLifelineInstance
public [Lifeline](../ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html) createLifelineInstance()
Returns:
created instance of type Lifeline
createLinkEndCreationDataInstance
public [LinkEndCreationData](../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html) createLinkEndCreationDataInstance()
Returns:
created instance of type LinkEndCreationData
createLinkEndDataInstance
public [LinkEndData](../ext/magicdraw/actions/mdintermediateactions/LinkEndData.html) createLinkEndDataInstance()
Returns:
created instance of type LinkEndData
createLinkEndDestructionDataInstance
public [LinkEndDestructionData](../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html) createLinkEndDestructionDataInstance()
Returns:
created instance of type LinkEndDestructionData
createLiteralBooleanInstance
public [LiteralBoolean](../ext/magicdraw/classes/mdkernel/LiteralBoolean.html) createLiteralBooleanInstance()
Returns:
created instance of type LiteralBoolean
createLiteralIntegerInstance
public [LiteralInteger](../ext/magicdraw/classes/mdkernel/LiteralInteger.html) createLiteralIntegerInstance()
Returns:
created instance of type LiteralInteger
createLiteralNullInstance
public [LiteralNull](../ext/magicdraw/classes/mdkernel/LiteralNull.html) createLiteralNullInstance()
Returns:
created instance of type LiteralNull
createLiteralRealInstance
public [LiteralReal](../ext/magicdraw/classes/mdkernel/LiteralReal.html) createLiteralRealInstance()
Returns:
created instance of type LiteralReal
createLiteralStringInstance
public [LiteralString](../ext/magicdraw/classes/mdkernel/LiteralString.html) createLiteralStringInstance()
Returns:
created instance of type LiteralString
createLiteralUnlimitedNaturalInstance
public [LiteralUnlimitedNatural](../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html) createLiteralUnlimitedNaturalInstance()
Returns:
created instance of type LiteralUnlimitedNatural
createLoopNodeInstance
public [LoopNode](../ext/magicdraw/activities/mdstructuredactivities/LoopNode.html) createLoopNodeInstance()
Returns:
created instance of type LoopNode
createManifestationInstance
public [Manifestation](../ext/magicdraw/deployments/mdartifacts/Manifestation.html) createManifestationInstance()
Returns:
created instance of type Manifestation
createMergeNodeInstance
public [MergeNode](../ext/magicdraw/activities/mdintermediateactivities/MergeNode.html) createMergeNodeInstance()
Returns:
created instance of type MergeNode
createMessageInstance
public [Message](../ext/magicdraw/interactions/mdbasicinteractions/Message.html) createMessageInstance()
Returns:
created instance of type Message
createMessageOccurrenceSpecificationInstance
public [MessageOccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html) createMessageOccurrenceSpecificationInstance()
Returns:
created instance of type MessageOccurrenceSpecification
createModelInstance
public [Model](../ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html) createModelInstance()
Returns:
created instance of type Model
createNodeInstance
public [Node](../ext/magicdraw/deployments/mdnodes/Node.html) createNodeInstance()
Returns:
created instance of type Node
createObjectFlowInstance
public [ObjectFlow](../ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html) createObjectFlowInstance()
Returns:
created instance of type ObjectFlow
createOccurrenceSpecificationInstance
public [OccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html) createOccurrenceSpecificationInstance()
Returns:
created instance of type OccurrenceSpecification
createOpaqueActionInstance
public [OpaqueAction](../ext/magicdraw/actions/mdbasicactions/OpaqueAction.html) createOpaqueActionInstance()
Returns:
created instance of type OpaqueAction
createOpaqueBehaviorInstance
public [OpaqueBehavior](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html) createOpaqueBehaviorInstance()
Returns:
created instance of type OpaqueBehavior
createOpaqueExpressionInstance
public [OpaqueExpression](../ext/magicdraw/classes/mdkernel/OpaqueExpression.html) createOpaqueExpressionInstance()
Returns:
created instance of type OpaqueExpression
createOperationInstance
public [Operation](../ext/magicdraw/classes/mdkernel/Operation.html) createOperationInstance()
Returns:
created instance of type Operation
createOperationTemplateParameterInstance
public [OperationTemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html) createOperationTemplateParameterInstance()
Returns:
created instance of type OperationTemplateParameter
createOutputPinInstance
public [OutputPin](../ext/magicdraw/actions/mdbasicactions/OutputPin.html) createOutputPinInstance()
Returns:
created instance of type OutputPin
createPackageInstance
public [Package](../ext/magicdraw/classes/mdkernel/Package.html) createPackageInstance()
Returns:
created instance of type Package
createPackageImportInstance
public [PackageImport](../ext/magicdraw/classes/mdkernel/PackageImport.html) createPackageImportInstance()
Returns:
created instance of type PackageImport
createPackageMergeInstance
public [PackageMerge](../ext/magicdraw/classes/mdkernel/PackageMerge.html) createPackageMergeInstance()
Returns:
created instance of type PackageMerge
createParameterInstance
public [Parameter](../ext/magicdraw/classes/mdkernel/Parameter.html) createParameterInstance()
Returns:
created instance of type Parameter
createParameterSetInstance
public [ParameterSet](../ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html) createParameterSetInstance()
Returns:
created instance of type ParameterSet
createPartDecompositionInstance
public [PartDecomposition](../ext/magicdraw/interactions/mdfragments/PartDecomposition.html) createPartDecompositionInstance()
Returns:
created instance of type PartDecomposition
createPortInstance
public [Port](../ext/magicdraw/compositestructures/mdports/Port.html) createPortInstance()
Returns:
created instance of type Port
createPrimitiveTypeInstance
public [PrimitiveType](../ext/magicdraw/classes/mdkernel/PrimitiveType.html) createPrimitiveTypeInstance()
Returns:
created instance of type PrimitiveType
createProfileInstance
public [Profile](../ext/magicdraw/mdprofiles/Profile.html) createProfileInstance()
Returns:
created instance of type Profile
createProfileApplicationInstance
public [ProfileApplication](../ext/magicdraw/mdprofiles/ProfileApplication.html) createProfileApplicationInstance()
Returns:
created instance of type ProfileApplication
createPropertyInstance
public [Property](../ext/magicdraw/classes/mdkernel/Property.html) createPropertyInstance()
Returns:
created instance of type Property
createProtocolConformanceInstance
public [ProtocolConformance](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html) createProtocolConformanceInstance()
Returns:
created instance of type ProtocolConformance
createProtocolStateMachineInstance
public [ProtocolStateMachine](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html) createProtocolStateMachineInstance()
Returns:
created instance of type ProtocolStateMachine
createProtocolTransitionInstance
public [ProtocolTransition](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html) createProtocolTransitionInstance()
Returns:
created instance of type ProtocolTransition
createPseudostateInstance
public [Pseudostate](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html) createPseudostateInstance()
Returns:
created instance of type Pseudostate
createQualifierValueInstance
public [QualifierValue](../ext/magicdraw/actions/mdcompleteactions/QualifierValue.html) createQualifierValueInstance()
Returns:
created instance of type QualifierValue
createRaiseExceptionActionInstance
public [RaiseExceptionAction](../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html) createRaiseExceptionActionInstance()
Returns:
created instance of type RaiseExceptionAction
createReadExtentActionInstance
public [ReadExtentAction](../ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html) createReadExtentActionInstance()
Returns:
created instance of type ReadExtentAction
createReadIsClassifiedObjectActionInstance
public [ReadIsClassifiedObjectAction](../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html) createReadIsClassifiedObjectActionInstance()
Returns:
created instance of type ReadIsClassifiedObjectAction
createReadLinkActionInstance
public [ReadLinkAction](../ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html) createReadLinkActionInstance()
Returns:
created instance of type ReadLinkAction
createReadLinkObjectEndActionInstance
public [ReadLinkObjectEndAction](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html) createReadLinkObjectEndActionInstance()
Returns:
created instance of type ReadLinkObjectEndAction
createReadLinkObjectEndQualifierActionInstance
public [ReadLinkObjectEndQualifierAction](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html) createReadLinkObjectEndQualifierActionInstance()
Returns:
created instance of type ReadLinkObjectEndQualifierAction
createReadSelfActionInstance
public [ReadSelfAction](../ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html) createReadSelfActionInstance()
Returns:
created instance of type ReadSelfAction
createReadStructuralFeatureActionInstance
public [ReadStructuralFeatureAction](../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html) createReadStructuralFeatureActionInstance()
Returns:
created instance of type ReadStructuralFeatureAction
createReadVariableActionInstance
public [ReadVariableAction](../ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html) createReadVariableActionInstance()
Returns:
created instance of type ReadVariableAction
createRealizationInstance
public [Realization](../ext/magicdraw/classes/mddependencies/Realization.html) createRealizationInstance()
Returns:
created instance of type Realization
createReceptionInstance
public [Reception](../ext/magicdraw/commonbehaviors/mdcommunications/Reception.html) createReceptionInstance()
Returns:
created instance of type Reception
createReclassifyObjectActionInstance
public [ReclassifyObjectAction](../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html) createReclassifyObjectActionInstance()
Returns:
created instance of type ReclassifyObjectAction
createRedefinableTemplateSignatureInstance
public [RedefinableTemplateSignature](../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html) createRedefinableTemplateSignatureInstance()
Returns:
created instance of type RedefinableTemplateSignature
createReduceActionInstance
public [ReduceAction](../ext/magicdraw/actions/mdcompleteactions/ReduceAction.html) createReduceActionInstance()
Returns:
created instance of type ReduceAction
createRegionInstance
public [Region](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html) createRegionInstance()
Returns:
created instance of type Region
createRemoveStructuralFeatureValueActionInstance
public [RemoveStructuralFeatureValueAction](../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html) createRemoveStructuralFeatureValueActionInstance()
Returns:
created instance of type RemoveStructuralFeatureValueAction
createRemoveVariableValueActionInstance
public [RemoveVariableValueAction](../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html) createRemoveVariableValueActionInstance()
Returns:
created instance of type RemoveVariableValueAction
createReplyActionInstance
public [ReplyAction](../ext/magicdraw/actions/mdcompleteactions/ReplyAction.html) createReplyActionInstance()
Returns:
created instance of type ReplyAction
createSendObjectActionInstance
public [SendObjectAction](../ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html) createSendObjectActionInstance()
Returns:
created instance of type SendObjectAction
createSendSignalActionInstance
public [SendSignalAction](../ext/magicdraw/actions/mdbasicactions/SendSignalAction.html) createSendSignalActionInstance()
Returns:
created instance of type SendSignalAction
createSequenceNodeInstance
public [SequenceNode](../ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html) createSequenceNodeInstance()
Returns:
created instance of type SequenceNode
createSignalInstance
public [Signal](../ext/magicdraw/commonbehaviors/mdcommunications/Signal.html) createSignalInstance()
Returns:
created instance of type Signal
createSignalEventInstance
public [SignalEvent](../ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html) createSignalEventInstance()
Returns:
created instance of type SignalEvent
createSlotInstance
public [Slot](../ext/magicdraw/classes/mdkernel/Slot.html) createSlotInstance()
Returns:
created instance of type Slot
createStartClassifierBehaviorActionInstance
public [StartClassifierBehaviorAction](../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html) createStartClassifierBehaviorActionInstance()
Returns:
created instance of type StartClassifierBehaviorAction
createStartObjectBehaviorActionInstance
public [StartObjectBehaviorAction](../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html) createStartObjectBehaviorActionInstance()
Returns:
created instance of type StartObjectBehaviorAction
createStateInstance
public [State](../ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html) createStateInstance()
Returns:
created instance of type State
createStateInvariantInstance
public [StateInvariant](../ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html) createStateInvariantInstance()
Returns:
created instance of type StateInvariant
createStateMachineInstance
public [StateMachine](../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html) createStateMachineInstance()
Returns:
created instance of type StateMachine
createStereotypeInstance
public [Stereotype](../ext/magicdraw/mdprofiles/Stereotype.html) createStereotypeInstance()
Returns:
created instance of type Stereotype
createStringExpressionInstance
public [StringExpression](../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html) createStringExpressionInstance()
Returns:
created instance of type StringExpression
createStructuredActivityNodeInstance
public [StructuredActivityNode](../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html) createStructuredActivityNodeInstance()
Returns:
created instance of type StructuredActivityNode
createSubstitutionInstance
public [Substitution](../ext/magicdraw/classes/mddependencies/Substitution.html) createSubstitutionInstance()
Returns:
created instance of type Substitution
createTemplateBindingInstance
public [TemplateBinding](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html) createTemplateBindingInstance()
Returns:
created instance of type TemplateBinding
createTemplateParameterInstance
public [TemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html) createTemplateParameterInstance()
Returns:
created instance of type TemplateParameter
createTemplateParameterSubstitutionInstance
public [TemplateParameterSubstitution](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html) createTemplateParameterSubstitutionInstance()
Returns:
created instance of type TemplateParameterSubstitution
createTemplateSignatureInstance
public [TemplateSignature](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html) createTemplateSignatureInstance()
Returns:
created instance of type TemplateSignature
createTestIdentityActionInstance
public [TestIdentityAction](../ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html) createTestIdentityActionInstance()
Returns:
created instance of type TestIdentityAction
createTimeConstraintInstance
public [TimeConstraint](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html) createTimeConstraintInstance()
Returns:
created instance of type TimeConstraint
createTimeEventInstance
public [TimeEvent](../ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html) createTimeEventInstance()
Returns:
created instance of type TimeEvent
createTimeExpressionInstance
public [TimeExpression](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html) createTimeExpressionInstance()
Returns:
created instance of type TimeExpression
createTimeIntervalInstance
public [TimeInterval](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html) createTimeIntervalInstance()
Returns:
created instance of type TimeInterval
createTimeObservationInstance
public [TimeObservation](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html) createTimeObservationInstance()
Returns:
created instance of type TimeObservation
createTransitionInstance
public [Transition](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) createTransitionInstance()
Returns:
created instance of type Transition
createTriggerInstance
public [Trigger](../ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html) createTriggerInstance()
Returns:
created instance of type Trigger
createUnmarshallActionInstance
public [UnmarshallAction](../ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html) createUnmarshallActionInstance()
Returns:
created instance of type UnmarshallAction
createUsageInstance
public [Usage](../ext/magicdraw/classes/mddependencies/Usage.html) createUsageInstance()
Returns:
created instance of type Usage
createUseCaseInstance
public [UseCase](../ext/magicdraw/mdusecases/UseCase.html) createUseCaseInstance()
Returns:
created instance of type UseCase
createValuePinInstance
public [ValuePin](../ext/magicdraw/actions/mdbasicactions/ValuePin.html) createValuePinInstance()
Returns:
created instance of type ValuePin
createValueSpecificationActionInstance
public [ValueSpecificationAction](../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html) createValueSpecificationActionInstance()
Returns:
created instance of type ValueSpecificationAction
createVariableInstance
public [Variable](../ext/magicdraw/activities/mdstructuredactivities/Variable.html) createVariableInstance()
Returns:
created instance of type Variable
createBooleanTaggedValueInstance
public [BooleanTaggedValue](../ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html) createBooleanTaggedValueInstance()
Returns:
created instance of type BooleanTaggedValue
createIntegerTaggedValueInstance
public [IntegerTaggedValue](../ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html) createIntegerTaggedValueInstance()
Returns:
created instance of type IntegerTaggedValue
createRealTaggedValueInstance
public [RealTaggedValue](../ext/magicdraw/classes/mdkernel/RealTaggedValue.html) createRealTaggedValueInstance()
Returns:
created instance of type RealTaggedValue
createStringTaggedValueInstance
public [StringTaggedValue](../ext/magicdraw/classes/mdkernel/StringTaggedValue.html) createStringTaggedValueInstance()
Returns:
created instance of type StringTaggedValue
createElementTaggedValueInstance
public [ElementTaggedValue](../ext/magicdraw/classes/mdkernel/ElementTaggedValue.html) createElementTaggedValueInstance()
Returns:
created instance of type ElementTaggedValue

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.impl</a></div>
<h1 class="title" title="Class ElementsFactory">Class ElementsFactory</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.impl.ElementsFactory</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">ElementsFactory</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.TASRepository)">ElementsFactory</a><wbr/>(<a href="../ext/TASRepository.html" title="interface in com.nomagic.uml2.ext">TASRepository</a> repository)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.TASRepository,com.nomagic.uml2.impl.ModelVisitor)">ElementsFactory</a><wbr/>(<a href="../ext/TASRepository.html" title="interface in com.nomagic.uml2.ext">TASRepository</a> repository,
 <a href="ModelVisitor.html" title="interface in com.nomagic.uml2.impl">ModelVisitor</a> configurator)</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAbstractionInstance()">createAbstractionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAcceptCallActionInstance()">createAcceptCallActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAcceptEventActionInstance()">createAcceptEventActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActionExecutionSpecificationInstance()">createActionExecutionSpecificationInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActionInputPinInstance()">createActionInputPinInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityFinalNodeInstance()">createActivityFinalNodeInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityInstance()">createActivityInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityParameterNodeInstance()">createActivityParameterNodeInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityPartitionInstance()">createActivityPartitionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActorInstance()">createActorInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAddStructuralFeatureValueActionInstance()">createAddStructuralFeatureValueActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAddVariableValueActionInstance()">createAddVariableValueActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEvent</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAnyReceiveEventInstance()">createAnyReceiveEventInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createArtifactInstance()">createArtifactInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAssociationClassInstance()">createAssociationClassInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAssociationInstance()">createAssociationInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createBehaviorExecutionSpecificationInstance()">createBehaviorExecutionSpecificationInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BooleanTaggedValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createBooleanTaggedValueInstance()">createBooleanTaggedValueInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createBroadcastSignalActionInstance()">createBroadcastSignalActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCallBehaviorActionInstance()">createCallBehaviorActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCallEventInstance()">createCallEventInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCallOperationActionInstance()">createCallOperationActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCentralBufferNodeInstance()">createCentralBufferNodeInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createChangeEventInstance()">createChangeEventInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClassifierTemplateParameterInstance()">createClassifierTemplateParameterInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClassInstance()">createClassInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClauseInstance()">createClauseInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClearAssociationActionInstance()">createClearAssociationActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClearStructuralFeatureActionInstance()">createClearStructuralFeatureActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClearVariableActionInstance()">createClearVariableActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCollaborationInstance()">createCollaborationInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCollaborationUseInstance()">createCollaborationUseInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCombinedFragmentInstance()">createCombinedFragmentInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCommentInstance()">createCommentInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCommunicationPathInstance()">createCommunicationPathInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createComponentInstance()">createComponentInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createComponentRealizationInstance()">createComponentRealizationInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConditionalNodeInstance()">createConditionalNodeInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConnectableElementTemplateParameterInstance()">createConnectableElementTemplateParameterInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConnectionPointReferenceInstance()">createConnectionPointReferenceInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConnectorEndInstance()">createConnectorEndInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConnectorInstance()">createConnectorInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragment</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConsiderIgnoreFragmentInstance()">createConsiderIgnoreFragmentInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConstraintInstance()">createConstraintInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Continuation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createContinuationInstance()">createContinuationInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createControlFlowInstance()">createControlFlowInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCreateLinkActionInstance()">createCreateLinkActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCreateLinkObjectActionInstance()">createCreateLinkObjectActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCreateObjectActionInstance()">createCreateObjectActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDataStoreNodeInstance()">createDataStoreNodeInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDataTypeInstance()">createDataTypeInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDecisionNodeInstance()">createDecisionNodeInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDependencyInstance()">createDependencyInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDeploymentInstance()">createDeploymentInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDeploymentSpecificationInstance()">createDeploymentSpecificationInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDestroyLinkActionInstance()">createDestroyLinkActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDestroyObjectActionInstance()">createDestroyObjectActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDestructionOccurrenceSpecificationInstance()">createDestructionOccurrenceSpecificationInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDeviceInstance()">createDeviceInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDiagramInstance()">createDiagramInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDurationConstraintInstance()">createDurationConstraintInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDurationInstance()">createDurationInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDurationIntervalInstance()">createDurationIntervalInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDurationObservationInstance()">createDurationObservationInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createElementImportInstance()">createElementImportInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/ElementTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementTaggedValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createElementTaggedValueInstance()">createElementTaggedValueInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createElementValueInstance()">createElementValueInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createEnumerationInstance()">createEnumerationInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createEnumerationLiteralInstance()">createEnumerationLiteralInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExceptionHandlerInstance()">createExceptionHandlerInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExecutionEnvironmentInstance()">createExecutionEnvironmentInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionOccurrenceSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExecutionOccurrenceSpecificationInstance()">createExecutionOccurrenceSpecificationInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExpansionNodeInstance()">createExpansionNodeInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExpansionRegionInstance()">createExpansionRegionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExpressionInstance()">createExpressionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExtendInstance()">createExtendInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExtensionEndInstance()">createExtensionEndInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExtensionInstance()">createExtensionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPoint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExtensionPointInstance()">createExtensionPointInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createFinalStateInstance()">createFinalStateInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createFlowFinalNodeInstance()">createFlowFinalNodeInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createForkNodeInstance()">createForkNodeInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createFunctionBehaviorInstance()">createFunctionBehaviorInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createGateInstance()">createGateInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createGeneralizationInstance()">createGeneralizationInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createGeneralizationSetInstance()">createGeneralizationSetInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">GeneralOrdering</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createGeneralOrderingInstance()">createGeneralOrderingInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createImageInstance()">createImageInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Include</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createIncludeInstance()">createIncludeInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInformationFlowInstance()">createInformationFlowInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInformationItemInstance()">createInformationItemInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInitialNodeInstance()">createInitialNodeInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInputPinInstance()">createInputPinInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInstanceSpecificationInstance()">createInstanceSpecificationInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInstanceValueInstance()">createInstanceValueInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">IntegerTaggedValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createIntegerTaggedValueInstance()">createIntegerTaggedValueInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInteractionConstraintInstance()">createInteractionConstraintInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInteractionInstance()">createInteractionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInteractionOperandInstance()">createInteractionOperandInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInteractionUseInstance()">createInteractionUseInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInterfaceInstance()">createInterfaceInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInterfaceRealizationInstance()">createInterfaceRealizationInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInterruptibleActivityRegionInstance()">createInterruptibleActivityRegionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createIntervalConstraintInstance()">createIntervalConstraintInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createIntervalInstance()">createIntervalInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createJoinNodeInstance()">createJoinNodeInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLifelineInstance()">createLifelineInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLinkEndCreationDataInstance()">createLinkEndCreationDataInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLinkEndDataInstance()">createLinkEndDataInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLinkEndDestructionDataInstance()">createLinkEndDestructionDataInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBoolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLiteralBooleanInstance()">createLiteralBooleanInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralInteger</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLiteralIntegerInstance()">createLiteralIntegerInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNull</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLiteralNullInstance()">createLiteralNullInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralReal</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLiteralRealInstance()">createLiteralRealInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralString</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLiteralStringInstance()">createLiteralStringInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNatural</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLiteralUnlimitedNaturalInstance()">createLiteralUnlimitedNaturalInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLoopNodeInstance()">createLoopNodeInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Manifestation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createManifestationInstance()">createManifestationInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMergeNodeInstance()">createMergeNodeInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMessageInstance()">createMessageInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMessageOccurrenceSpecificationInstance()">createMessageOccurrenceSpecificationInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createModelInstance()">createModelInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createNodeInstance()">createNodeInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createNotConfigure(org.eclipse.emf.ecore.EClass)">createNotConfigure</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create object by EClass, created object is not configured by configurator</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createObjectFlowInstance()">createObjectFlowInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOccurrenceSpecificationInstance()">createOccurrenceSpecificationInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOpaqueActionInstance()">createOpaqueActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOpaqueBehaviorInstance()">createOpaqueBehaviorInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOpaqueExpressionInstance()">createOpaqueExpressionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOperationInstance()">createOperationInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOperationTemplateParameterInstance()">createOperationTemplateParameterInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOutputPinInstance()">createOutputPinInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPackageImportInstance()">createPackageImportInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPackageInstance()">createPackageInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageMerge</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPackageMergeInstance()">createPackageMergeInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createParameterInstance()">createParameterInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createParameterSetInstance()">createParameterSetInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPartDecompositionInstance()">createPartDecompositionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPortInstance()">createPortInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPrimitiveTypeInstance()">createPrimitiveTypeInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplication</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProfileApplicationInstance()">createProfileApplicationInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProfileInstance()">createProfileInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPropertyInstance()">createPropertyInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolConformance</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProtocolConformanceInstance()">createProtocolConformanceInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProtocolStateMachineInstance()">createProtocolStateMachineInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProtocolTransitionInstance()">createProtocolTransitionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPseudostateInstance()">createPseudostateInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createQualifierValueInstance()">createQualifierValueInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRaiseExceptionActionInstance()">createRaiseExceptionActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadExtentActionInstance()">createReadExtentActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadIsClassifiedObjectActionInstance()">createReadIsClassifiedObjectActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadLinkActionInstance()">createReadLinkActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadLinkObjectEndActionInstance()">createReadLinkObjectEndActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadLinkObjectEndQualifierActionInstance()">createReadLinkObjectEndQualifierActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadSelfActionInstance()">createReadSelfActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadStructuralFeatureActionInstance()">createReadStructuralFeatureActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadVariableActionInstance()">createReadVariableActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRealizationInstance()">createRealizationInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/RealTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RealTaggedValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRealTaggedValueInstance()">createRealTaggedValueInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReceptionInstance()">createReceptionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReclassifyObjectActionInstance()">createReclassifyObjectActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRedefinableTemplateSignatureInstance()">createRedefinableTemplateSignatureInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReduceActionInstance()">createReduceActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRegionInstance()">createRegionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRemoveStructuralFeatureValueActionInstance()">createRemoveStructuralFeatureValueActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRemoveVariableValueActionInstance()">createRemoveVariableValueActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReplyActionInstance()">createReplyActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSendObjectActionInstance()">createSendObjectActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSendSignalActionInstance()">createSendSignalActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSequenceNodeInstance()">createSequenceNodeInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSignalEventInstance()">createSignalEventInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSignalInstance()">createSignalInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSlotInstance()">createSlotInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStartClassifierBehaviorActionInstance()">createStartClassifierBehaviorActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStartObjectBehaviorActionInstance()">createStartObjectBehaviorActionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStateInstance()">createStateInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStateInvariantInstance()">createStateInvariantInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStateMachineInstance()">createStateMachineInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStereotypeInstance()">createStereotypeInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStringExpressionInstance()">createStringExpressionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/StringTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StringTaggedValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStringTaggedValueInstance()">createStringTaggedValueInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStructuredActivityNodeInstance()">createStructuredActivityNodeInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSubstitutionInstance()">createSubstitutionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateBindingInstance()">createTemplateBindingInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateParameterInstance()">createTemplateParameterInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateParameterSubstitutionInstance()">createTemplateParameterSubstitutionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateSignatureInstance()">createTemplateSignatureInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTestIdentityActionInstance()">createTestIdentityActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTimeConstraintInstance()">createTimeConstraintInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEvent</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTimeEventInstance()">createTimeEventInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTimeExpressionInstance()">createTimeExpressionInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTimeIntervalInstance()">createTimeIntervalInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTimeObservationInstance()">createTimeObservationInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTransitionInstance()">createTransitionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTriggerInstance()">createTriggerInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createUnmarshallActionInstance()">createUnmarshallActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Usage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createUsageInstance()">createUsageInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createUseCaseInstance()">createUseCaseInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createValuePinInstance()">createValuePinInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueSpecificationActionInstance()">createValueSpecificationActionInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createVariableInstance()">createVariableInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mddependencies/AbstractionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">AbstractionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbstractionClass()">getAbstractionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/AcceptCallActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAcceptCallActionClass()">getAcceptCallActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/AcceptEventActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAcceptEventActionClass()">getAcceptEventActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/ActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActionClass()">getActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecificationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActionExecutionSpecificationClass()">getActionExecutionSpecificationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/ActionInputPinClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPinClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActionInputPinClass()">getActionInputPinClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActivityClass()">getActivityClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdbasicactivities/ActivityEdgeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdgeClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActivityEdgeClass()">getActivityEdgeClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNodeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActivityFinalNodeClass()">getActivityFinalNodeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityGroupClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroupClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActivityGroupClass()">getActivityGroupClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNodeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActivityNodeClass()">getActivityNodeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNodeClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActivityParameterNodeClass()">getActivityParameterNodeClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/ActivityPartitionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartitionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActivityPartitionClass()">getActivityPartitionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdusecases/ActorClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ActorClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActorClass()">getActorClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAddStructuralFeatureValueActionClass()">getAddStructuralFeatureValueActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/AddVariableValueActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAddVariableValueActionClass()">getAddVariableValueActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEventClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnyReceiveEventClass()">getAnyReceiveEventClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdartifacts/ArtifactClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">ArtifactClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getArtifactClass()">getArtifactClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AssociationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssociationClass()">getAssociationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdassociationclasses/AssociationClassClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClassClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssociationClassClass()">getAssociationClassClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/BehavioralFeatureClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeatureClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBehavioralFeatureClass()">getBehavioralFeatureClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehaviorClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehaviorClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBehaviorClass()">getBehaviorClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifierClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifierClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBehavioredClassifierClass()">getBehavioredClassifierClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecificationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBehaviorExecutionSpecificationClass()">getBehaviorExecutionSpecificationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/BooleanTaggedValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BooleanTaggedValueClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBooleanTaggedValueClass()">getBooleanTaggedValueClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBroadcastSignalActionClass()">getBroadcastSignalActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/CallActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCallActionClass()">getCallActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/CallBehaviorActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCallBehaviorActionClass()">getCallBehaviorActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/CallEventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEventClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCallEventClass()">getCallEventClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/CallOperationActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCallOperationActionClass()">getCallOperationActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNodeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCentralBufferNodeClass()">getCentralBufferNodeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEventClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChangeEventClass()">getChangeEventClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/ClassClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ClassClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassClass()">getClassClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/ClassifierClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ClassifierClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassifierClass()">getClassifierClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameterClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameterClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassifierTemplateParameterClass()">getClassifierTemplateParameterClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdstructuredactivities/ClauseClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ClauseClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClauseClass()">getClauseClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/ClearAssociationActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClearAssociationActionClass()">getClearAssociationActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClearStructuralFeatureActionClass()">getClearStructuralFeatureActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/ClearVariableActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClearVariableActionClass()">getClearVariableActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/compositestructures/mdcollaborations/CollaborationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCollaborationClass()">getCollaborationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUseClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUseClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCollaborationUseClass()">getCollaborationUseClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/CombinedFragmentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragmentClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCombinedFragmentClass()">getCombinedFragmentClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/CommentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">CommentClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCommentClass()">getCommentClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdnodes/CommunicationPathClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPathClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCommunicationPathClass()">getCommunicationPathClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/components/mdbasiccomponents/ComponentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getComponentClass()">getComponentClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/components/mdbasiccomponents/ComponentRealizationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealizationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getComponentRealizationClass()">getComponentRealizationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdstructuredactivities/ConditionalNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNodeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConditionalNodeClass()">getConditionalNodeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElementClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectableElementClass()">getConnectableElementClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameterClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameterClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectableElementTemplateParameterClass()">getConnectableElementTemplateParameterClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReferenceClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReferenceClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectionPointReferenceClass()">getConnectionPointReferenceClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectorClass()">getConnectorClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEndClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEndClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectorEndClass()">getConnectorEndClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragmentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragmentClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConsiderIgnoreFragmentClass()">getConsiderIgnoreFragmentClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/ConstraintClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ConstraintClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConstraintClass()">getConstraintClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/ContinuationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ContinuationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContinuationClass()">getContinuationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdbasicactivities/ControlFlowClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlowClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getControlFlowClass()">getControlFlowClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdbasicactivities/ControlNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlNodeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getControlNodeClass()">getControlNodeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/CreateLinkActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreateLinkActionClass()">getCreateLinkActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreateLinkObjectActionClass()">getCreateLinkObjectActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/CreateObjectActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreateObjectActionClass()">getCreateObjectActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdcompleteactivities/DataStoreNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNodeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDataStoreNodeClass()">getDataStoreNodeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/DataTypeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataTypeClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDataTypeClass()">getDataTypeClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/DecisionNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNodeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDecisionNodeClass()">getDecisionNodeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mddependencies/DependencyClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">DependencyClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDependencyClass()">getDependencyClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdnodes/DeployedArtifactClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeployedArtifactClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDeployedArtifactClass()">getDeployedArtifactClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdnodes/DeploymentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDeploymentClass()">getDeploymentClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecificationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDeploymentSpecificationClass()">getDeploymentSpecificationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdnodes/DeploymentTargetClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTargetClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDeploymentTargetClass()">getDeploymentTargetClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/DestroyLinkActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDestroyLinkActionClass()">getDestroyLinkActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/DestroyObjectActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDestroyObjectActionClass()">getDestroyObjectActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecificationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDestructionOccurrenceSpecificationClass()">getDestructionOccurrenceSpecificationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdnodes/DeviceClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeviceClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDeviceClass()">getDeviceClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/DiagramClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DiagramClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramClass()">getDiagramClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/DirectedRelationshipClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationshipClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirectedRelationshipClass()">getDirectedRelationshipClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDurationClass()">getDurationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraintClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraintClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDurationConstraintClass()">getDurationConstraintClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationIntervalClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationIntervalClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDurationIntervalClass()">getDurationIntervalClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDurationObservationClass()">getDurationObservationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/ElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementClass()">getElementClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/ElementImportClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImportClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementImportClass()">getElementImportClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/ElementTaggedValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementTaggedValueClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementTaggedValueClass()">getElementTaggedValueClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/ElementValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValueClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementValueClass()">getElementValueClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/compositestructures/mdports/EncapsulatedClassifierClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifierClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEncapsulatedClassifierClass()">getEncapsulatedClassifierClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/EnumerationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEnumerationClass()">getEnumerationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/EnumerationLiteralClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteralClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEnumerationLiteralClass()">getEnumerationLiteralClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/EventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">EventClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEventClass()">getEventClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandlerClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandlerClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExceptionHandlerClass()">getExceptionHandlerClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdstructuredactivities/ExecutableNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNodeClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExecutableNodeClass()">getExecutableNodeClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdnodes/ExecutionEnvironmentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironmentClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExecutionEnvironmentClass()">getExecutionEnvironmentClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionOccurrenceSpecificationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExecutionOccurrenceSpecificationClass()">getExecutionOccurrenceSpecificationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionSpecificationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExecutionSpecificationClass()">getExecutionSpecificationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNodeClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExpansionNodeClass()">getExpansionNodeClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExpansionRegionClass()">getExpansionRegionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/ExpressionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ExpressionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExpressionClass()">getExpressionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdusecases/ExtendClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtendClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtendClass()">getExtendClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdprofiles/ExtensionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensionClass()">getExtensionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdprofiles/ExtensionEndClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEndClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensionEndClass()">getExtensionEndClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdusecases/ExtensionPointClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPointClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensionPointClass()">getExtensionPointClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/FeatureClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">FeatureClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeatureClass()">getFeatureClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/FinalNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FinalNodeClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFinalNodeClass()">getFinalNodeClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalStateClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalStateClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFinalStateClass()">getFinalStateClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNodeClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFlowFinalNodeClass()">getFlowFinalNodeClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/ForkNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNodeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getForkNodeClass()">getForkNodeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehaviorClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehaviorClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFunctionBehaviorClass()">getFunctionBehaviorClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/GateClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">GateClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGateClass()">getGateClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/GeneralizationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">GeneralizationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeneralizationClass()">getGeneralizationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdpowertypes/GeneralizationSetClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSetClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeneralizationSetClass()">getGeneralizationSetClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrderingClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">GeneralOrderingClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeneralOrderingClass()">getGeneralOrderingClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdprofiles/ImageClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ImageClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageClass()">getImageClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdusecases/IncludeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">IncludeClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIncludeClass()">getIncludeClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlowClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlowClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInformationFlowClass()">getInformationFlowClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItemClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItemClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInformationItemClass()">getInformationItemClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdbasicactivities/InitialNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNodeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInitialNodeClass()">getInitialNodeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/InputPinClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPinClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInputPinClass()">getInputPinClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/InstanceSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecificationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceSpecificationClass()">getInstanceSpecificationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/InstanceValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValueClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceValueClass()">getInstanceValueClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/IntegerTaggedValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">IntegerTaggedValueClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIntegerTaggedValueClass()">getIntegerTaggedValueClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/InteractionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInteractionClass()">getInteractionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/InteractionConstraintClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraintClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInteractionConstraintClass()">getInteractionConstraintClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/InteractionFragmentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragmentClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInteractionFragmentClass()">getInteractionFragmentClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/InteractionOperandClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperandClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInteractionOperandClass()">getInteractionOperandClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/InteractionUseClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUseClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInteractionUseClass()">getInteractionUseClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdinterfaces/InterfaceClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInterfaceClass()">getInterfaceClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdinterfaces/InterfaceRealizationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealizationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInterfaceRealizationClass()">getInterfaceRealizationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInterruptibleActivityRegionClass()">getInterruptibleActivityRegionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIntervalClass()">getIntervalClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraintClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraintClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIntervalConstraintClass()">getIntervalConstraintClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/InvocationActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInvocationActionClass()">getInvocationActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/JoinNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNodeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getJoinNodeClass()">getJoinNodeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/LifelineClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">LifelineClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLifelineClass()">getLifelineClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/LinkActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLinkActionClass()">getLinkActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationDataClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationDataClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLinkEndCreationDataClass()">getLinkEndCreationDataClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndDataClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDataClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLinkEndDataClass()">getLinkEndDataClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionDataClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionDataClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLinkEndDestructionDataClass()">getLinkEndDestructionDataClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/LiteralBooleanClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBooleanClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLiteralBooleanClass()">getLiteralBooleanClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/LiteralIntegerClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralIntegerClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLiteralIntegerClass()">getLiteralIntegerClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/LiteralNullClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNullClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLiteralNullClass()">getLiteralNullClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/LiteralRealClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralRealClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLiteralRealClass()">getLiteralRealClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/LiteralSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralSpecificationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLiteralSpecificationClass()">getLiteralSpecificationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/LiteralStringClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralStringClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLiteralStringClass()">getLiteralStringClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNaturalClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNaturalClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLiteralUnlimitedNaturalClass()">getLiteralUnlimitedNaturalClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdstructuredactivities/LoopNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNodeClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoopNodeClass()">getLoopNodeClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdartifacts/ManifestationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">ManifestationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManifestationClass()">getManifestationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdintermediateactivities/MergeNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNodeClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMergeNodeClass()">getMergeNodeClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessageClass()">getMessageClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageEndClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEndClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessageEndClass()">getMessageEndClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/MessageEventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">MessageEventClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessageEventClass()">getMessageEventClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecificationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessageOccurrenceSpecificationClass()">getMessageOccurrenceSpecificationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdmodels/ModelClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">ModelClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelClass()">getModelClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/MultiplicityElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElementClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMultiplicityElementClass()">getMultiplicityElementClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/NamedElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElementClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNamedElementClass()">getNamedElementClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/NamespaceClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamespaceClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNamespaceClass()">getNamespaceClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/deployments/mdnodes/NodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">NodeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNodeClass()">getNodeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdbasicactivities/ObjectFlowClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlowClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectFlowClass()">getObjectFlowClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdbasicactivities/ObjectNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNodeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectNodeClass()">getObjectNodeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/ObservationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">ObservationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getObservationClass()">getObservationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecificationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOccurrenceSpecificationClass()">getOccurrenceSpecificationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/OpaqueActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOpaqueActionClass()">getOpaqueActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehaviorClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehaviorClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOpaqueBehaviorClass()">getOpaqueBehaviorClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/OpaqueExpressionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpressionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOpaqueExpressionClass()">getOpaqueExpressionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/OperationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OperationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOperationClass()">getOperationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameterClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameterClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOperationTemplateParameterClass()">getOperationTemplateParameterClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/OutputPinClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPinClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOutputPinClass()">getOutputPinClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/PackageableElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElementClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPackageableElementClass()">getPackageableElementClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/PackageClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPackageClass()">getPackageClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/PackageImportClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImportClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPackageImportClass()">getPackageImportClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/PackageMergeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageMergeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPackageMergeClass()">getPackageMergeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElementClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParameterableElementClass()">getParameterableElementClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/ParameterClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParameterClass()">getParameterClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdcompleteactivities/ParameterSetClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSetClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParameterSetClass()">getParameterSetClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdfragments/PartDecompositionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecompositionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPartDecompositionClass()">getPartDecompositionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/PinClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">PinClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPinClass()">getPinClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/compositestructures/mdports/PortClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">PortClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPortClass()">getPortClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/PrimitiveTypeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveTypeClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPrimitiveTypeClass()">getPrimitiveTypeClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdprofiles/ProfileApplicationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplicationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProfileApplicationClass()">getProfileApplicationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdprofiles/ProfileClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProfileClass()">getProfileClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/PropertyClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PropertyClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyClass()">getPropertyClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformanceClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolConformanceClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProtocolConformanceClass()">getProtocolConformanceClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachineClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachineClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProtocolStateMachineClass()">getProtocolStateMachineClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransitionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransitionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProtocolTransitionClass()">getProtocolTransitionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/PseudostateClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">PseudostateClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPseudostateClass()">getPseudostateClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/QualifierValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValueClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getQualifierValueClass()">getQualifierValueClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRaiseExceptionActionClass()">getRaiseExceptionActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReadExtentActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReadExtentActionClass()">getReadExtentActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReadIsClassifiedObjectActionClass()">getReadIsClassifiedObjectActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/ReadLinkActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReadLinkActionClass()">getReadLinkActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReadLinkObjectEndActionClass()">getReadLinkObjectEndActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReadLinkObjectEndQualifierActionClass()">getReadLinkObjectEndQualifierActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/ReadSelfActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReadSelfActionClass()">getReadSelfActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReadStructuralFeatureActionClass()">getReadStructuralFeatureActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/ReadVariableActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReadVariableActionClass()">getReadVariableActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mddependencies/RealizationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">RealizationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRealizationClass()">getRealizationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/RealTaggedValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RealTaggedValueClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRealTaggedValueClass()">getRealTaggedValueClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/ReceptionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ReceptionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReceptionClass()">getReceptionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReclassifyObjectActionClass()">getReclassifyObjectActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/RedefinableElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElementClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRedefinableElementClass()">getRedefinableElementClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignatureClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignatureClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRedefinableTemplateSignatureClass()">getRedefinableTemplateSignatureClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReduceActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReduceActionClass()">getReduceActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/RegionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">RegionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRegionClass()">getRegionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/RelationshipClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RelationshipClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationshipClass()">getRelationshipClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemoveStructuralFeatureValueActionClass()">getRemoveStructuralFeatureValueActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemoveVariableValueActionClass()">getRemoveVariableValueActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/ReplyActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReplyActionClass()">getReplyActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/SendObjectActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSendObjectActionClass()">getSendObjectActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/SendSignalActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSendSignalActionClass()">getSendSignalActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdstructuredactivities/SequenceNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNodeClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSequenceNodeClass()">getSequenceNodeClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/SignalClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSignalClass()">getSignalClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/SignalEventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEventClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSignalEventClass()">getSignalEventClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/SlotClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">SlotClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSlotClass()">getSlotClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStartClassifierBehaviorActionClass()">getStartClassifierBehaviorActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStartObjectBehaviorActionClass()">getStartObjectBehaviorActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStateClass()">getStateClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/interactions/mdbasicinteractions/StateInvariantClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariantClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStateInvariantClass()">getStateInvariantClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachineClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachineClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStateMachineClass()">getStateMachineClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdprofiles/StereotypeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">StereotypeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypeClass()">getStereotypeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpressionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpressionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStringExpressionClass()">getStringExpressionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/StringTaggedValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StringTaggedValueClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStringTaggedValueClass()">getStringTaggedValueClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/StructuralFeatureActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStructuralFeatureActionClass()">getStructuralFeatureActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/StructuralFeatureClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeatureClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStructuralFeatureClass()">getStructuralFeatureClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNodeClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStructuredActivityNodeClass()">getStructuredActivityNodeClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifierClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifierClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStructuredClassifierClass()">getStructuredClassifierClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mddependencies/SubstitutionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">SubstitutionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSubstitutionClass()">getSubstitutionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/TaggedValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValueClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTaggedValueClass()">getTaggedValueClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElementClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateableElementClass()">getTemplateableElementClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBindingClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBindingClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateBindingClass()">getTemplateBindingClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateParameterClass()">getTemplateParameterClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitutionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitutionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateParameterSubstitutionClass()">getTemplateParameterSubstitutionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignatureClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignatureClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateSignatureClass()">getTemplateSignatureClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/TestIdentityActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTestIdentityActionClass()">getTestIdentityActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraintClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraintClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeConstraintClass()">getTimeConstraintClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/TimeEventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEventClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeEventClass()">getTimeEventClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpressionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpressionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeExpressionClass()">getTimeExpressionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeIntervalClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeIntervalClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeIntervalClass()">getTimeIntervalClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeObservationClass()">getTimeObservationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/TransitionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransitionClass()">getTransitionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/commonbehaviors/mdcommunications/TriggerClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TriggerClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTriggerClass()">getTriggerClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/TypeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypeClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeClass()">getTypeClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/TypedElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElementClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypedElementClass()">getTypedElementClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdcompleteactions/UnmarshallActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUnmarshallActionClass()">getUnmarshallActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mddependencies/UsageClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">UsageClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUsageClass()">getUsageClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/mdusecases/UseCaseClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCaseClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUseCaseClass()">getUseCaseClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdbasicactions/ValuePinClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePinClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValuePinClass()">getValuePinClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueSpecificationActionClass()">getValueSpecificationActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/classes/mdkernel/ValueSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecificationClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueSpecificationClass()">getValueSpecificationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/VariableActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">VariableActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVariableActionClass()">getVariableActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/activities/mdstructuredactivities/VariableClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">VariableClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVariableClass()">getVariableClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/VertexClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">VertexClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVertexClass()">getVertexClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/WriteLinkActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteLinkActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWriteLinkActionClass()">getWriteLinkActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureActionClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWriteStructuralFeatureActionClass()">getWriteStructuralFeatureActionClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ext/magicdraw/actions/mdstructuredactions/WriteVariableActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableActionClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWriteVariableActionClass()">getWriteVariableActionClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.TASRepository)">
<h3>ElementsFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementsFactory</span><wbr/><span class="parameters">(<a href="../ext/TASRepository.html" title="interface in com.nomagic.uml2.ext">TASRepository</a> repository)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.TASRepository,com.nomagic.uml2.impl.ModelVisitor)">
<h3>ElementsFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementsFactory</span><wbr/><span class="parameters">(<a href="../ext/TASRepository.html" title="interface in com.nomagic.uml2.ext">TASRepository</a> repository,
 @CheckForNull
 <a href="ModelVisitor.html" title="interface in com.nomagic.uml2.impl">ModelVisitor</a> configurator)</span></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="createNotConfigure(org.eclipse.emf.ecore.EClass)">
<h3>createNotConfigure</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">createNotConfigure</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Create object by EClass, created object is not configured by configurator</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - type for object to create</dd>
<dt>Returns:</dt>
<dd>created object, or null if given EClass is not in repository</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractionClass()">
<h3>getAbstractionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mddependencies/AbstractionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">AbstractionClass</a></span> <span class="element-name">getAbstractionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type AbstractionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAcceptCallActionClass()">
<h3>getAcceptCallActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/AcceptCallActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallActionClass</a></span> <span class="element-name">getAcceptCallActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type AcceptCallActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAcceptEventActionClass()">
<h3>getAcceptEventActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/AcceptEventActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventActionClass</a></span> <span class="element-name">getAcceptEventActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type AcceptEventActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActionClass()">
<h3>getActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/ActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ActionClass</a></span> <span class="element-name">getActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActionExecutionSpecificationClass()">
<h3>getActionExecutionSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecificationClass</a></span> <span class="element-name">getActionExecutionSpecificationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ActionExecutionSpecificationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActionInputPinClass()">
<h3>getActionInputPinClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/ActionInputPinClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPinClass</a></span> <span class="element-name">getActionInputPinClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ActionInputPinClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActivityClass()">
<h3>getActivityClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityClass</a></span> <span class="element-name">getActivityClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ActivityClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActivityEdgeClass()">
<h3>getActivityEdgeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdbasicactivities/ActivityEdgeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdgeClass</a></span> <span class="element-name">getActivityEdgeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ActivityEdgeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActivityFinalNodeClass()">
<h3>getActivityFinalNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNodeClass</a></span> <span class="element-name">getActivityFinalNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ActivityFinalNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActivityGroupClass()">
<h3>getActivityGroupClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityGroupClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroupClass</a></span> <span class="element-name">getActivityGroupClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ActivityGroupClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActivityNodeClass()">
<h3>getActivityNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNodeClass</a></span> <span class="element-name">getActivityNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ActivityNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActivityParameterNodeClass()">
<h3>getActivityParameterNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNodeClass</a></span> <span class="element-name">getActivityParameterNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ActivityParameterNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActivityPartitionClass()">
<h3>getActivityPartitionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/ActivityPartitionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartitionClass</a></span> <span class="element-name">getActivityPartitionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ActivityPartitionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActorClass()">
<h3>getActorClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdusecases/ActorClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ActorClass</a></span> <span class="element-name">getActorClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ActorClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAddStructuralFeatureValueActionClass()">
<h3>getAddStructuralFeatureValueActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueActionClass</a></span> <span class="element-name">getAddStructuralFeatureValueActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type AddStructuralFeatureValueActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAddVariableValueActionClass()">
<h3>getAddVariableValueActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/AddVariableValueActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueActionClass</a></span> <span class="element-name">getAddVariableValueActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type AddVariableValueActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnyReceiveEventClass()">
<h3>getAnyReceiveEventClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEventClass</a></span> <span class="element-name">getAnyReceiveEventClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type AnyReceiveEventClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getArtifactClass()">
<h3>getArtifactClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdartifacts/ArtifactClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">ArtifactClass</a></span> <span class="element-name">getArtifactClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ArtifactClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssociationClass()">
<h3>getAssociationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AssociationClass</a></span> <span class="element-name">getAssociationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type AssociationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssociationClassClass()">
<h3>getAssociationClassClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdassociationclasses/AssociationClassClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClassClass</a></span> <span class="element-name">getAssociationClassClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type AssociationClassClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBehaviorClass()">
<h3>getBehaviorClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehaviorClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehaviorClass</a></span> <span class="element-name">getBehaviorClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type BehaviorClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBehaviorExecutionSpecificationClass()">
<h3>getBehaviorExecutionSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecificationClass</a></span> <span class="element-name">getBehaviorExecutionSpecificationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type BehaviorExecutionSpecificationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBehavioralFeatureClass()">
<h3>getBehavioralFeatureClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/BehavioralFeatureClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeatureClass</a></span> <span class="element-name">getBehavioralFeatureClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type BehavioralFeatureClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBehavioredClassifierClass()">
<h3>getBehavioredClassifierClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifierClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifierClass</a></span> <span class="element-name">getBehavioredClassifierClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type BehavioredClassifierClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBroadcastSignalActionClass()">
<h3>getBroadcastSignalActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalActionClass</a></span> <span class="element-name">getBroadcastSignalActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type BroadcastSignalActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCallActionClass()">
<h3>getCallActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/CallActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallActionClass</a></span> <span class="element-name">getCallActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type CallActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCallBehaviorActionClass()">
<h3>getCallBehaviorActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/CallBehaviorActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorActionClass</a></span> <span class="element-name">getCallBehaviorActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type CallBehaviorActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCallEventClass()">
<h3>getCallEventClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/CallEventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEventClass</a></span> <span class="element-name">getCallEventClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type CallEventClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCallOperationActionClass()">
<h3>getCallOperationActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/CallOperationActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationActionClass</a></span> <span class="element-name">getCallOperationActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type CallOperationActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCentralBufferNodeClass()">
<h3>getCentralBufferNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNodeClass</a></span> <span class="element-name">getCentralBufferNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type CentralBufferNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChangeEventClass()">
<h3>getChangeEventClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEventClass</a></span> <span class="element-name">getChangeEventClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ChangeEventClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassClass()">
<h3>getClassClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/ClassClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ClassClass</a></span> <span class="element-name">getClassClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ClassClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassifierClass()">
<h3>getClassifierClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/ClassifierClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ClassifierClass</a></span> <span class="element-name">getClassifierClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ClassifierClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassifierTemplateParameterClass()">
<h3>getClassifierTemplateParameterClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameterClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameterClass</a></span> <span class="element-name">getClassifierTemplateParameterClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ClassifierTemplateParameterClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClauseClass()">
<h3>getClauseClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdstructuredactivities/ClauseClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ClauseClass</a></span> <span class="element-name">getClauseClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ClauseClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClearAssociationActionClass()">
<h3>getClearAssociationActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/ClearAssociationActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationActionClass</a></span> <span class="element-name">getClearAssociationActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ClearAssociationActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClearStructuralFeatureActionClass()">
<h3>getClearStructuralFeatureActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureActionClass</a></span> <span class="element-name">getClearStructuralFeatureActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ClearStructuralFeatureActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClearVariableActionClass()">
<h3>getClearVariableActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/ClearVariableActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableActionClass</a></span> <span class="element-name">getClearVariableActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ClearVariableActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCollaborationClass()">
<h3>getCollaborationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/compositestructures/mdcollaborations/CollaborationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationClass</a></span> <span class="element-name">getCollaborationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type CollaborationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCollaborationUseClass()">
<h3>getCollaborationUseClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUseClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUseClass</a></span> <span class="element-name">getCollaborationUseClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type CollaborationUseClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCombinedFragmentClass()">
<h3>getCombinedFragmentClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/CombinedFragmentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragmentClass</a></span> <span class="element-name">getCombinedFragmentClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type CombinedFragmentClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCommentClass()">
<h3>getCommentClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/CommentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">CommentClass</a></span> <span class="element-name">getCommentClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type CommentClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCommunicationPathClass()">
<h3>getCommunicationPathClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdnodes/CommunicationPathClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPathClass</a></span> <span class="element-name">getCommunicationPathClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type CommunicationPathClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getComponentClass()">
<h3>getComponentClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/components/mdbasiccomponents/ComponentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentClass</a></span> <span class="element-name">getComponentClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ComponentClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getComponentRealizationClass()">
<h3>getComponentRealizationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/components/mdbasiccomponents/ComponentRealizationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealizationClass</a></span> <span class="element-name">getComponentRealizationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ComponentRealizationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConditionalNodeClass()">
<h3>getConditionalNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdstructuredactivities/ConditionalNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNodeClass</a></span> <span class="element-name">getConditionalNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ConditionalNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectableElementClass()">
<h3>getConnectableElementClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElementClass</a></span> <span class="element-name">getConnectableElementClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ConnectableElementClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectableElementTemplateParameterClass()">
<h3>getConnectableElementTemplateParameterClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameterClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameterClass</a></span> <span class="element-name">getConnectableElementTemplateParameterClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ConnectableElementTemplateParameterClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectionPointReferenceClass()">
<h3>getConnectionPointReferenceClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReferenceClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReferenceClass</a></span> <span class="element-name">getConnectionPointReferenceClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ConnectionPointReferenceClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectorClass()">
<h3>getConnectorClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorClass</a></span> <span class="element-name">getConnectorClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ConnectorClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectorEndClass()">
<h3>getConnectorEndClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEndClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEndClass</a></span> <span class="element-name">getConnectorEndClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ConnectorEndClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConsiderIgnoreFragmentClass()">
<h3>getConsiderIgnoreFragmentClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragmentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragmentClass</a></span> <span class="element-name">getConsiderIgnoreFragmentClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ConsiderIgnoreFragmentClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConstraintClass()">
<h3>getConstraintClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/ConstraintClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ConstraintClass</a></span> <span class="element-name">getConstraintClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ConstraintClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContinuationClass()">
<h3>getContinuationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/ContinuationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ContinuationClass</a></span> <span class="element-name">getContinuationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ContinuationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getControlFlowClass()">
<h3>getControlFlowClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdbasicactivities/ControlFlowClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlowClass</a></span> <span class="element-name">getControlFlowClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ControlFlowClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getControlNodeClass()">
<h3>getControlNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdbasicactivities/ControlNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlNodeClass</a></span> <span class="element-name">getControlNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ControlNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreateLinkActionClass()">
<h3>getCreateLinkActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/CreateLinkActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkActionClass</a></span> <span class="element-name">getCreateLinkActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type CreateLinkActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreateLinkObjectActionClass()">
<h3>getCreateLinkObjectActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectActionClass</a></span> <span class="element-name">getCreateLinkObjectActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type CreateLinkObjectActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreateObjectActionClass()">
<h3>getCreateObjectActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/CreateObjectActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectActionClass</a></span> <span class="element-name">getCreateObjectActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type CreateObjectActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDataStoreNodeClass()">
<h3>getDataStoreNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdcompleteactivities/DataStoreNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNodeClass</a></span> <span class="element-name">getDataStoreNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DataStoreNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDataTypeClass()">
<h3>getDataTypeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/DataTypeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataTypeClass</a></span> <span class="element-name">getDataTypeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DataTypeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDecisionNodeClass()">
<h3>getDecisionNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/DecisionNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNodeClass</a></span> <span class="element-name">getDecisionNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DecisionNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDependencyClass()">
<h3>getDependencyClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mddependencies/DependencyClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">DependencyClass</a></span> <span class="element-name">getDependencyClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DependencyClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeployedArtifactClass()">
<h3>getDeployedArtifactClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdnodes/DeployedArtifactClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeployedArtifactClass</a></span> <span class="element-name">getDeployedArtifactClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DeployedArtifactClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeploymentClass()">
<h3>getDeploymentClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdnodes/DeploymentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentClass</a></span> <span class="element-name">getDeploymentClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DeploymentClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeploymentSpecificationClass()">
<h3>getDeploymentSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecificationClass</a></span> <span class="element-name">getDeploymentSpecificationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DeploymentSpecificationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeploymentTargetClass()">
<h3>getDeploymentTargetClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdnodes/DeploymentTargetClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTargetClass</a></span> <span class="element-name">getDeploymentTargetClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DeploymentTargetClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDestroyLinkActionClass()">
<h3>getDestroyLinkActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/DestroyLinkActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkActionClass</a></span> <span class="element-name">getDestroyLinkActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DestroyLinkActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDestroyObjectActionClass()">
<h3>getDestroyObjectActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/DestroyObjectActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectActionClass</a></span> <span class="element-name">getDestroyObjectActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DestroyObjectActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDestructionOccurrenceSpecificationClass()">
<h3>getDestructionOccurrenceSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecificationClass</a></span> <span class="element-name">getDestructionOccurrenceSpecificationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DestructionOccurrenceSpecificationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeviceClass()">
<h3>getDeviceClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdnodes/DeviceClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeviceClass</a></span> <span class="element-name">getDeviceClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DeviceClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramClass()">
<h3>getDiagramClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/DiagramClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DiagramClass</a></span> <span class="element-name">getDiagramClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DiagramClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirectedRelationshipClass()">
<h3>getDirectedRelationshipClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/DirectedRelationshipClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationshipClass</a></span> <span class="element-name">getDirectedRelationshipClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DirectedRelationshipClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDurationClass()">
<h3>getDurationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationClass</a></span> <span class="element-name">getDurationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DurationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDurationConstraintClass()">
<h3>getDurationConstraintClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraintClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraintClass</a></span> <span class="element-name">getDurationConstraintClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DurationConstraintClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDurationIntervalClass()">
<h3>getDurationIntervalClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationIntervalClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationIntervalClass</a></span> <span class="element-name">getDurationIntervalClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DurationIntervalClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDurationObservationClass()">
<h3>getDurationObservationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservationClass</a></span> <span class="element-name">getDurationObservationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type DurationObservationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementClass()">
<h3>getElementClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/ElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementClass</a></span> <span class="element-name">getElementClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ElementClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementImportClass()">
<h3>getElementImportClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/ElementImportClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImportClass</a></span> <span class="element-name">getElementImportClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ElementImportClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementValueClass()">
<h3>getElementValueClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/ElementValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValueClass</a></span> <span class="element-name">getElementValueClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ElementValueClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEncapsulatedClassifierClass()">
<h3>getEncapsulatedClassifierClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/compositestructures/mdports/EncapsulatedClassifierClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifierClass</a></span> <span class="element-name">getEncapsulatedClassifierClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type EncapsulatedClassifierClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnumerationClass()">
<h3>getEnumerationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/EnumerationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationClass</a></span> <span class="element-name">getEnumerationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type EnumerationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnumerationLiteralClass()">
<h3>getEnumerationLiteralClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/EnumerationLiteralClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteralClass</a></span> <span class="element-name">getEnumerationLiteralClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type EnumerationLiteralClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEventClass()">
<h3>getEventClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/EventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">EventClass</a></span> <span class="element-name">getEventClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type EventClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExceptionHandlerClass()">
<h3>getExceptionHandlerClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandlerClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandlerClass</a></span> <span class="element-name">getExceptionHandlerClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ExceptionHandlerClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExecutableNodeClass()">
<h3>getExecutableNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdstructuredactivities/ExecutableNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNodeClass</a></span> <span class="element-name">getExecutableNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ExecutableNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExecutionEnvironmentClass()">
<h3>getExecutionEnvironmentClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdnodes/ExecutionEnvironmentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironmentClass</a></span> <span class="element-name">getExecutionEnvironmentClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ExecutionEnvironmentClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExecutionOccurrenceSpecificationClass()">
<h3>getExecutionOccurrenceSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionOccurrenceSpecificationClass</a></span> <span class="element-name">getExecutionOccurrenceSpecificationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ExecutionOccurrenceSpecificationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExecutionSpecificationClass()">
<h3>getExecutionSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionSpecificationClass</a></span> <span class="element-name">getExecutionSpecificationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ExecutionSpecificationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExpansionNodeClass()">
<h3>getExpansionNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNodeClass</a></span> <span class="element-name">getExpansionNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ExpansionNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExpansionRegionClass()">
<h3>getExpansionRegionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegionClass</a></span> <span class="element-name">getExpansionRegionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ExpansionRegionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExpressionClass()">
<h3>getExpressionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/ExpressionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ExpressionClass</a></span> <span class="element-name">getExpressionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ExpressionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtendClass()">
<h3>getExtendClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdusecases/ExtendClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtendClass</a></span> <span class="element-name">getExtendClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ExtendClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensionClass()">
<h3>getExtensionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdprofiles/ExtensionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionClass</a></span> <span class="element-name">getExtensionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ExtensionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensionEndClass()">
<h3>getExtensionEndClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdprofiles/ExtensionEndClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEndClass</a></span> <span class="element-name">getExtensionEndClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ExtensionEndClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensionPointClass()">
<h3>getExtensionPointClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdusecases/ExtensionPointClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPointClass</a></span> <span class="element-name">getExtensionPointClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ExtensionPointClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeatureClass()">
<h3>getFeatureClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/FeatureClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">FeatureClass</a></span> <span class="element-name">getFeatureClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type FeatureClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFinalNodeClass()">
<h3>getFinalNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/FinalNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FinalNodeClass</a></span> <span class="element-name">getFinalNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type FinalNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFinalStateClass()">
<h3>getFinalStateClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalStateClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalStateClass</a></span> <span class="element-name">getFinalStateClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type FinalStateClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFlowFinalNodeClass()">
<h3>getFlowFinalNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNodeClass</a></span> <span class="element-name">getFlowFinalNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type FlowFinalNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getForkNodeClass()">
<h3>getForkNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/ForkNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNodeClass</a></span> <span class="element-name">getForkNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ForkNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFunctionBehaviorClass()">
<h3>getFunctionBehaviorClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehaviorClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehaviorClass</a></span> <span class="element-name">getFunctionBehaviorClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type FunctionBehaviorClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGateClass()">
<h3>getGateClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/GateClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">GateClass</a></span> <span class="element-name">getGateClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type GateClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeneralOrderingClass()">
<h3>getGeneralOrderingClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrderingClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">GeneralOrderingClass</a></span> <span class="element-name">getGeneralOrderingClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type GeneralOrderingClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeneralizationClass()">
<h3>getGeneralizationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/GeneralizationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">GeneralizationClass</a></span> <span class="element-name">getGeneralizationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type GeneralizationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeneralizationSetClass()">
<h3>getGeneralizationSetClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdpowertypes/GeneralizationSetClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSetClass</a></span> <span class="element-name">getGeneralizationSetClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type GeneralizationSetClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImageClass()">
<h3>getImageClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdprofiles/ImageClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ImageClass</a></span> <span class="element-name">getImageClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ImageClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIncludeClass()">
<h3>getIncludeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdusecases/IncludeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">IncludeClass</a></span> <span class="element-name">getIncludeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type IncludeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInformationFlowClass()">
<h3>getInformationFlowClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlowClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlowClass</a></span> <span class="element-name">getInformationFlowClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InformationFlowClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInformationItemClass()">
<h3>getInformationItemClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItemClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItemClass</a></span> <span class="element-name">getInformationItemClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InformationItemClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInitialNodeClass()">
<h3>getInitialNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdbasicactivities/InitialNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNodeClass</a></span> <span class="element-name">getInitialNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InitialNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInputPinClass()">
<h3>getInputPinClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/InputPinClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPinClass</a></span> <span class="element-name">getInputPinClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InputPinClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstanceSpecificationClass()">
<h3>getInstanceSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/InstanceSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecificationClass</a></span> <span class="element-name">getInstanceSpecificationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InstanceSpecificationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstanceValueClass()">
<h3>getInstanceValueClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/InstanceValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValueClass</a></span> <span class="element-name">getInstanceValueClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InstanceValueClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInteractionClass()">
<h3>getInteractionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/InteractionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionClass</a></span> <span class="element-name">getInteractionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InteractionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInteractionConstraintClass()">
<h3>getInteractionConstraintClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/InteractionConstraintClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraintClass</a></span> <span class="element-name">getInteractionConstraintClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InteractionConstraintClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInteractionFragmentClass()">
<h3>getInteractionFragmentClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/InteractionFragmentClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragmentClass</a></span> <span class="element-name">getInteractionFragmentClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InteractionFragmentClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInteractionOperandClass()">
<h3>getInteractionOperandClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/InteractionOperandClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperandClass</a></span> <span class="element-name">getInteractionOperandClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InteractionOperandClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInteractionUseClass()">
<h3>getInteractionUseClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/InteractionUseClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUseClass</a></span> <span class="element-name">getInteractionUseClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InteractionUseClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInterfaceClass()">
<h3>getInterfaceClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdinterfaces/InterfaceClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceClass</a></span> <span class="element-name">getInterfaceClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InterfaceClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInterfaceRealizationClass()">
<h3>getInterfaceRealizationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdinterfaces/InterfaceRealizationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealizationClass</a></span> <span class="element-name">getInterfaceRealizationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InterfaceRealizationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInterruptibleActivityRegionClass()">
<h3>getInterruptibleActivityRegionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegionClass</a></span> <span class="element-name">getInterruptibleActivityRegionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InterruptibleActivityRegionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIntervalClass()">
<h3>getIntervalClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalClass</a></span> <span class="element-name">getIntervalClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type IntervalClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIntervalConstraintClass()">
<h3>getIntervalConstraintClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraintClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraintClass</a></span> <span class="element-name">getIntervalConstraintClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type IntervalConstraintClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInvocationActionClass()">
<h3>getInvocationActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/InvocationActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationActionClass</a></span> <span class="element-name">getInvocationActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type InvocationActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getJoinNodeClass()">
<h3>getJoinNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/JoinNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNodeClass</a></span> <span class="element-name">getJoinNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type JoinNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLifelineClass()">
<h3>getLifelineClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/LifelineClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">LifelineClass</a></span> <span class="element-name">getLifelineClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type LifelineClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLinkActionClass()">
<h3>getLinkActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/LinkActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkActionClass</a></span> <span class="element-name">getLinkActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type LinkActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLinkEndCreationDataClass()">
<h3>getLinkEndCreationDataClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationDataClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationDataClass</a></span> <span class="element-name">getLinkEndCreationDataClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type LinkEndCreationDataClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLinkEndDataClass()">
<h3>getLinkEndDataClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndDataClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDataClass</a></span> <span class="element-name">getLinkEndDataClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type LinkEndDataClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLinkEndDestructionDataClass()">
<h3>getLinkEndDestructionDataClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionDataClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionDataClass</a></span> <span class="element-name">getLinkEndDestructionDataClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type LinkEndDestructionDataClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLiteralBooleanClass()">
<h3>getLiteralBooleanClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/LiteralBooleanClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBooleanClass</a></span> <span class="element-name">getLiteralBooleanClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type LiteralBooleanClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLiteralIntegerClass()">
<h3>getLiteralIntegerClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/LiteralIntegerClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralIntegerClass</a></span> <span class="element-name">getLiteralIntegerClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type LiteralIntegerClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLiteralNullClass()">
<h3>getLiteralNullClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/LiteralNullClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNullClass</a></span> <span class="element-name">getLiteralNullClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type LiteralNullClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLiteralRealClass()">
<h3>getLiteralRealClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/LiteralRealClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralRealClass</a></span> <span class="element-name">getLiteralRealClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type LiteralRealClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLiteralSpecificationClass()">
<h3>getLiteralSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/LiteralSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralSpecificationClass</a></span> <span class="element-name">getLiteralSpecificationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type LiteralSpecificationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLiteralStringClass()">
<h3>getLiteralStringClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/LiteralStringClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralStringClass</a></span> <span class="element-name">getLiteralStringClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type LiteralStringClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLiteralUnlimitedNaturalClass()">
<h3>getLiteralUnlimitedNaturalClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNaturalClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNaturalClass</a></span> <span class="element-name">getLiteralUnlimitedNaturalClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type LiteralUnlimitedNaturalClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLoopNodeClass()">
<h3>getLoopNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdstructuredactivities/LoopNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNodeClass</a></span> <span class="element-name">getLoopNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type LoopNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManifestationClass()">
<h3>getManifestationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdartifacts/ManifestationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">ManifestationClass</a></span> <span class="element-name">getManifestationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ManifestationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMergeNodeClass()">
<h3>getMergeNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/MergeNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNodeClass</a></span> <span class="element-name">getMergeNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type MergeNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMessageClass()">
<h3>getMessageClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageClass</a></span> <span class="element-name">getMessageClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type MessageClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMessageEndClass()">
<h3>getMessageEndClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageEndClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEndClass</a></span> <span class="element-name">getMessageEndClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type MessageEndClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMessageEventClass()">
<h3>getMessageEventClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/MessageEventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">MessageEventClass</a></span> <span class="element-name">getMessageEventClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type MessageEventClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMessageOccurrenceSpecificationClass()">
<h3>getMessageOccurrenceSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecificationClass</a></span> <span class="element-name">getMessageOccurrenceSpecificationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type MessageOccurrenceSpecificationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModelClass()">
<h3>getModelClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdmodels/ModelClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">ModelClass</a></span> <span class="element-name">getModelClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ModelClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMultiplicityElementClass()">
<h3>getMultiplicityElementClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/MultiplicityElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElementClass</a></span> <span class="element-name">getMultiplicityElementClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type MultiplicityElementClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNamedElementClass()">
<h3>getNamedElementClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/NamedElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElementClass</a></span> <span class="element-name">getNamedElementClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type NamedElementClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNamespaceClass()">
<h3>getNamespaceClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/NamespaceClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamespaceClass</a></span> <span class="element-name">getNamespaceClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type NamespaceClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNodeClass()">
<h3>getNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdnodes/NodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">NodeClass</a></span> <span class="element-name">getNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type NodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectFlowClass()">
<h3>getObjectFlowClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdbasicactivities/ObjectFlowClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlowClass</a></span> <span class="element-name">getObjectFlowClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ObjectFlowClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectNodeClass()">
<h3>getObjectNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdbasicactivities/ObjectNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNodeClass</a></span> <span class="element-name">getObjectNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ObjectNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObservationClass()">
<h3>getObservationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/ObservationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">ObservationClass</a></span> <span class="element-name">getObservationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ObservationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOccurrenceSpecificationClass()">
<h3>getOccurrenceSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecificationClass</a></span> <span class="element-name">getOccurrenceSpecificationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type OccurrenceSpecificationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOpaqueActionClass()">
<h3>getOpaqueActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/OpaqueActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueActionClass</a></span> <span class="element-name">getOpaqueActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type OpaqueActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOpaqueBehaviorClass()">
<h3>getOpaqueBehaviorClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehaviorClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehaviorClass</a></span> <span class="element-name">getOpaqueBehaviorClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type OpaqueBehaviorClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOpaqueExpressionClass()">
<h3>getOpaqueExpressionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/OpaqueExpressionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpressionClass</a></span> <span class="element-name">getOpaqueExpressionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type OpaqueExpressionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOperationClass()">
<h3>getOperationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/OperationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OperationClass</a></span> <span class="element-name">getOperationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type OperationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOperationTemplateParameterClass()">
<h3>getOperationTemplateParameterClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameterClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameterClass</a></span> <span class="element-name">getOperationTemplateParameterClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type OperationTemplateParameterClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOutputPinClass()">
<h3>getOutputPinClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/OutputPinClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPinClass</a></span> <span class="element-name">getOutputPinClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type OutputPinClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageClass()">
<h3>getPackageClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/PackageClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageClass</a></span> <span class="element-name">getPackageClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type PackageClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageImportClass()">
<h3>getPackageImportClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/PackageImportClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImportClass</a></span> <span class="element-name">getPackageImportClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type PackageImportClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageMergeClass()">
<h3>getPackageMergeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/PackageMergeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageMergeClass</a></span> <span class="element-name">getPackageMergeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type PackageMergeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageableElementClass()">
<h3>getPackageableElementClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/PackageableElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElementClass</a></span> <span class="element-name">getPackageableElementClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type PackageableElementClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParameterClass()">
<h3>getParameterClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/ParameterClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterClass</a></span> <span class="element-name">getParameterClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ParameterClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParameterSetClass()">
<h3>getParameterSetClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdcompleteactivities/ParameterSetClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSetClass</a></span> <span class="element-name">getParameterSetClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ParameterSetClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParameterableElementClass()">
<h3>getParameterableElementClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElementClass</a></span> <span class="element-name">getParameterableElementClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ParameterableElementClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPartDecompositionClass()">
<h3>getPartDecompositionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/PartDecompositionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecompositionClass</a></span> <span class="element-name">getPartDecompositionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type PartDecompositionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPinClass()">
<h3>getPinClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/PinClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">PinClass</a></span> <span class="element-name">getPinClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type PinClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPortClass()">
<h3>getPortClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/compositestructures/mdports/PortClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">PortClass</a></span> <span class="element-name">getPortClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type PortClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrimitiveTypeClass()">
<h3>getPrimitiveTypeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/PrimitiveTypeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveTypeClass</a></span> <span class="element-name">getPrimitiveTypeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type PrimitiveTypeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProfileClass()">
<h3>getProfileClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdprofiles/ProfileClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileClass</a></span> <span class="element-name">getProfileClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ProfileClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProfileApplicationClass()">
<h3>getProfileApplicationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdprofiles/ProfileApplicationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplicationClass</a></span> <span class="element-name">getProfileApplicationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ProfileApplicationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyClass()">
<h3>getPropertyClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/PropertyClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PropertyClass</a></span> <span class="element-name">getPropertyClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type PropertyClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProtocolConformanceClass()">
<h3>getProtocolConformanceClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformanceClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolConformanceClass</a></span> <span class="element-name">getProtocolConformanceClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ProtocolConformanceClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProtocolStateMachineClass()">
<h3>getProtocolStateMachineClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachineClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachineClass</a></span> <span class="element-name">getProtocolStateMachineClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ProtocolStateMachineClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProtocolTransitionClass()">
<h3>getProtocolTransitionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransitionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransitionClass</a></span> <span class="element-name">getProtocolTransitionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ProtocolTransitionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPseudostateClass()">
<h3>getPseudostateClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/PseudostateClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">PseudostateClass</a></span> <span class="element-name">getPseudostateClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type PseudostateClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQualifierValueClass()">
<h3>getQualifierValueClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/QualifierValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValueClass</a></span> <span class="element-name">getQualifierValueClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type QualifierValueClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRaiseExceptionActionClass()">
<h3>getRaiseExceptionActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionActionClass</a></span> <span class="element-name">getRaiseExceptionActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type RaiseExceptionActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReadExtentActionClass()">
<h3>getReadExtentActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReadExtentActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentActionClass</a></span> <span class="element-name">getReadExtentActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ReadExtentActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReadIsClassifiedObjectActionClass()">
<h3>getReadIsClassifiedObjectActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectActionClass</a></span> <span class="element-name">getReadIsClassifiedObjectActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ReadIsClassifiedObjectActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReadLinkActionClass()">
<h3>getReadLinkActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/ReadLinkActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkActionClass</a></span> <span class="element-name">getReadLinkActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ReadLinkActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReadLinkObjectEndActionClass()">
<h3>getReadLinkObjectEndActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndActionClass</a></span> <span class="element-name">getReadLinkObjectEndActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ReadLinkObjectEndActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReadLinkObjectEndQualifierActionClass()">
<h3>getReadLinkObjectEndQualifierActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierActionClass</a></span> <span class="element-name">getReadLinkObjectEndQualifierActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ReadLinkObjectEndQualifierActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReadSelfActionClass()">
<h3>getReadSelfActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/ReadSelfActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfActionClass</a></span> <span class="element-name">getReadSelfActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ReadSelfActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReadStructuralFeatureActionClass()">
<h3>getReadStructuralFeatureActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureActionClass</a></span> <span class="element-name">getReadStructuralFeatureActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ReadStructuralFeatureActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReadVariableActionClass()">
<h3>getReadVariableActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/ReadVariableActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableActionClass</a></span> <span class="element-name">getReadVariableActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ReadVariableActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRealizationClass()">
<h3>getRealizationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mddependencies/RealizationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">RealizationClass</a></span> <span class="element-name">getRealizationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type RealizationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReceptionClass()">
<h3>getReceptionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/ReceptionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ReceptionClass</a></span> <span class="element-name">getReceptionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ReceptionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReclassifyObjectActionClass()">
<h3>getReclassifyObjectActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectActionClass</a></span> <span class="element-name">getReclassifyObjectActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ReclassifyObjectActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinableElementClass()">
<h3>getRedefinableElementClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/RedefinableElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElementClass</a></span> <span class="element-name">getRedefinableElementClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type RedefinableElementClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinableTemplateSignatureClass()">
<h3>getRedefinableTemplateSignatureClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignatureClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignatureClass</a></span> <span class="element-name">getRedefinableTemplateSignatureClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type RedefinableTemplateSignatureClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReduceActionClass()">
<h3>getReduceActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReduceActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceActionClass</a></span> <span class="element-name">getReduceActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ReduceActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRegionClass()">
<h3>getRegionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/RegionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">RegionClass</a></span> <span class="element-name">getRegionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type RegionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRelationshipClass()">
<h3>getRelationshipClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/RelationshipClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RelationshipClass</a></span> <span class="element-name">getRelationshipClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type RelationshipClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoveStructuralFeatureValueActionClass()">
<h3>getRemoveStructuralFeatureValueActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueActionClass</a></span> <span class="element-name">getRemoveStructuralFeatureValueActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type RemoveStructuralFeatureValueActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoveVariableValueActionClass()">
<h3>getRemoveVariableValueActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueActionClass</a></span> <span class="element-name">getRemoveVariableValueActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type RemoveVariableValueActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReplyActionClass()">
<h3>getReplyActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReplyActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyActionClass</a></span> <span class="element-name">getReplyActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ReplyActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSendObjectActionClass()">
<h3>getSendObjectActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/SendObjectActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectActionClass</a></span> <span class="element-name">getSendObjectActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type SendObjectActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSendSignalActionClass()">
<h3>getSendSignalActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/SendSignalActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalActionClass</a></span> <span class="element-name">getSendSignalActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type SendSignalActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSequenceNodeClass()">
<h3>getSequenceNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdstructuredactivities/SequenceNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNodeClass</a></span> <span class="element-name">getSequenceNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type SequenceNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignalClass()">
<h3>getSignalClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/SignalClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalClass</a></span> <span class="element-name">getSignalClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type SignalClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignalEventClass()">
<h3>getSignalEventClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/SignalEventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEventClass</a></span> <span class="element-name">getSignalEventClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type SignalEventClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSlotClass()">
<h3>getSlotClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/SlotClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">SlotClass</a></span> <span class="element-name">getSlotClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type SlotClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStartClassifierBehaviorActionClass()">
<h3>getStartClassifierBehaviorActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorActionClass</a></span> <span class="element-name">getStartClassifierBehaviorActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type StartClassifierBehaviorActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStartObjectBehaviorActionClass()">
<h3>getStartObjectBehaviorActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorActionClass</a></span> <span class="element-name">getStartObjectBehaviorActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type StartObjectBehaviorActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStateClass()">
<h3>getStateClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateClass</a></span> <span class="element-name">getStateClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type StateClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStateInvariantClass()">
<h3>getStateInvariantClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/StateInvariantClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariantClass</a></span> <span class="element-name">getStateInvariantClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type StateInvariantClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStateMachineClass()">
<h3>getStateMachineClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachineClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachineClass</a></span> <span class="element-name">getStateMachineClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type StateMachineClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypeClass()">
<h3>getStereotypeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdprofiles/StereotypeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">StereotypeClass</a></span> <span class="element-name">getStereotypeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type StereotypeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringExpressionClass()">
<h3>getStringExpressionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpressionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpressionClass</a></span> <span class="element-name">getStringExpressionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type StringExpressionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStructuralFeatureClass()">
<h3>getStructuralFeatureClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/StructuralFeatureClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeatureClass</a></span> <span class="element-name">getStructuralFeatureClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type StructuralFeatureClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStructuralFeatureActionClass()">
<h3>getStructuralFeatureActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/StructuralFeatureActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureActionClass</a></span> <span class="element-name">getStructuralFeatureActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type StructuralFeatureActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStructuredActivityNodeClass()">
<h3>getStructuredActivityNodeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNodeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNodeClass</a></span> <span class="element-name">getStructuredActivityNodeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type StructuredActivityNodeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStructuredClassifierClass()">
<h3>getStructuredClassifierClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifierClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifierClass</a></span> <span class="element-name">getStructuredClassifierClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type StructuredClassifierClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSubstitutionClass()">
<h3>getSubstitutionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mddependencies/SubstitutionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">SubstitutionClass</a></span> <span class="element-name">getSubstitutionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type SubstitutionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateBindingClass()">
<h3>getTemplateBindingClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBindingClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBindingClass</a></span> <span class="element-name">getTemplateBindingClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TemplateBindingClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateParameterClass()">
<h3>getTemplateParameterClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterClass</a></span> <span class="element-name">getTemplateParameterClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TemplateParameterClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateParameterSubstitutionClass()">
<h3>getTemplateParameterSubstitutionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitutionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitutionClass</a></span> <span class="element-name">getTemplateParameterSubstitutionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TemplateParameterSubstitutionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateSignatureClass()">
<h3>getTemplateSignatureClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignatureClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignatureClass</a></span> <span class="element-name">getTemplateSignatureClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TemplateSignatureClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateableElementClass()">
<h3>getTemplateableElementClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElementClass</a></span> <span class="element-name">getTemplateableElementClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TemplateableElementClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTestIdentityActionClass()">
<h3>getTestIdentityActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/TestIdentityActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityActionClass</a></span> <span class="element-name">getTestIdentityActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TestIdentityActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTimeConstraintClass()">
<h3>getTimeConstraintClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraintClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraintClass</a></span> <span class="element-name">getTimeConstraintClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TimeConstraintClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTimeEventClass()">
<h3>getTimeEventClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/TimeEventClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEventClass</a></span> <span class="element-name">getTimeEventClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TimeEventClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTimeExpressionClass()">
<h3>getTimeExpressionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpressionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpressionClass</a></span> <span class="element-name">getTimeExpressionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TimeExpressionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTimeIntervalClass()">
<h3>getTimeIntervalClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeIntervalClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeIntervalClass</a></span> <span class="element-name">getTimeIntervalClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TimeIntervalClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTimeObservationClass()">
<h3>getTimeObservationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservationClass</a></span> <span class="element-name">getTimeObservationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TimeObservationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTransitionClass()">
<h3>getTransitionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/TransitionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionClass</a></span> <span class="element-name">getTransitionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TransitionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTriggerClass()">
<h3>getTriggerClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/TriggerClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TriggerClass</a></span> <span class="element-name">getTriggerClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TriggerClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypeClass()">
<h3>getTypeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/TypeClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypeClass</a></span> <span class="element-name">getTypeClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TypeClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypedElementClass()">
<h3>getTypedElementClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/TypedElementClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElementClass</a></span> <span class="element-name">getTypedElementClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TypedElementClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUnmarshallActionClass()">
<h3>getUnmarshallActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/UnmarshallActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallActionClass</a></span> <span class="element-name">getUnmarshallActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type UnmarshallActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsageClass()">
<h3>getUsageClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mddependencies/UsageClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">UsageClass</a></span> <span class="element-name">getUsageClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type UsageClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUseCaseClass()">
<h3>getUseCaseClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdusecases/UseCaseClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCaseClass</a></span> <span class="element-name">getUseCaseClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type UseCaseClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValuePinClass()">
<h3>getValuePinClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/ValuePinClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePinClass</a></span> <span class="element-name">getValuePinClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ValuePinClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueSpecificationClass()">
<h3>getValueSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/ValueSpecificationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecificationClass</a></span> <span class="element-name">getValueSpecificationClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ValueSpecificationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueSpecificationActionClass()">
<h3>getValueSpecificationActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationActionClass</a></span> <span class="element-name">getValueSpecificationActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ValueSpecificationActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVariableClass()">
<h3>getVariableClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdstructuredactivities/VariableClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">VariableClass</a></span> <span class="element-name">getVariableClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type VariableClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVariableActionClass()">
<h3>getVariableActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/VariableActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">VariableActionClass</a></span> <span class="element-name">getVariableActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type VariableActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVertexClass()">
<h3>getVertexClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/VertexClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">VertexClass</a></span> <span class="element-name">getVertexClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type VertexClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWriteLinkActionClass()">
<h3>getWriteLinkActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/WriteLinkActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteLinkActionClass</a></span> <span class="element-name">getWriteLinkActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type WriteLinkActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWriteStructuralFeatureActionClass()">
<h3>getWriteStructuralFeatureActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureActionClass</a></span> <span class="element-name">getWriteStructuralFeatureActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type WriteStructuralFeatureActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWriteVariableActionClass()">
<h3>getWriteVariableActionClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/WriteVariableActionClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableActionClass</a></span> <span class="element-name">getWriteVariableActionClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type WriteVariableActionClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTaggedValueClass()">
<h3>getTaggedValueClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/TaggedValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValueClass</a></span> <span class="element-name">getTaggedValueClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type TaggedValueClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBooleanTaggedValueClass()">
<h3>getBooleanTaggedValueClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/BooleanTaggedValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BooleanTaggedValueClass</a></span> <span class="element-name">getBooleanTaggedValueClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type BooleanTaggedValueClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIntegerTaggedValueClass()">
<h3>getIntegerTaggedValueClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/IntegerTaggedValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">IntegerTaggedValueClass</a></span> <span class="element-name">getIntegerTaggedValueClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type IntegerTaggedValueClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRealTaggedValueClass()">
<h3>getRealTaggedValueClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/RealTaggedValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RealTaggedValueClass</a></span> <span class="element-name">getRealTaggedValueClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type RealTaggedValueClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringTaggedValueClass()">
<h3>getStringTaggedValueClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/StringTaggedValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StringTaggedValueClass</a></span> <span class="element-name">getStringTaggedValueClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type StringTaggedValueClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementTaggedValueClass()">
<h3>getElementTaggedValueClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/ElementTaggedValueClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementTaggedValueClass</a></span> <span class="element-name">getElementTaggedValueClass</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class of type ElementTaggedValueClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAbstractionInstance()">
<h3>createAbstractionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a></span> <span class="element-name">createAbstractionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Abstraction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAcceptCallActionInstance()">
<h3>createAcceptCallActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a></span> <span class="element-name">createAcceptCallActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type AcceptCallAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAcceptEventActionInstance()">
<h3>createAcceptEventActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></span> <span class="element-name">createAcceptEventActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type AcceptEventAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActionExecutionSpecificationInstance()">
<h3>createActionExecutionSpecificationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecification</a></span> <span class="element-name">createActionExecutionSpecificationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ActionExecutionSpecification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActionInputPinInstance()">
<h3>createActionInputPinInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a></span> <span class="element-name">createActionInputPinInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ActionInputPin</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityInstance()">
<h3>createActivityInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></span> <span class="element-name">createActivityInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Activity</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityFinalNodeInstance()">
<h3>createActivityFinalNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNode</a></span> <span class="element-name">createActivityFinalNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ActivityFinalNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityParameterNodeInstance()">
<h3>createActivityParameterNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a></span> <span class="element-name">createActivityParameterNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ActivityParameterNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityPartitionInstance()">
<h3>createActivityPartitionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a></span> <span class="element-name">createActivityPartitionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ActivityPartition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActorInstance()">
<h3>createActorInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a></span> <span class="element-name">createActorInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Actor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAddStructuralFeatureValueActionInstance()">
<h3>createAddStructuralFeatureValueActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a></span> <span class="element-name">createAddStructuralFeatureValueActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type AddStructuralFeatureValueAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAddVariableValueActionInstance()">
<h3>createAddVariableValueActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a></span> <span class="element-name">createAddVariableValueActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type AddVariableValueAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAnyReceiveEventInstance()">
<h3>createAnyReceiveEventInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEvent</a></span> <span class="element-name">createAnyReceiveEventInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type AnyReceiveEvent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createArtifactInstance()">
<h3>createArtifactInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></span> <span class="element-name">createArtifactInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Artifact</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAssociationInstance()">
<h3>createAssociationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></span> <span class="element-name">createAssociationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Association</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAssociationClassInstance()">
<h3>createAssociationClassInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a></span> <span class="element-name">createAssociationClassInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type AssociationClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBehaviorExecutionSpecificationInstance()">
<h3>createBehaviorExecutionSpecificationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecification</a></span> <span class="element-name">createBehaviorExecutionSpecificationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type BehaviorExecutionSpecification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBroadcastSignalActionInstance()">
<h3>createBroadcastSignalActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a></span> <span class="element-name">createBroadcastSignalActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type BroadcastSignalAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCallBehaviorActionInstance()">
<h3>createCallBehaviorActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a></span> <span class="element-name">createCallBehaviorActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type CallBehaviorAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCallEventInstance()">
<h3>createCallEventInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a></span> <span class="element-name">createCallEventInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type CallEvent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCallOperationActionInstance()">
<h3>createCallOperationActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a></span> <span class="element-name">createCallOperationActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type CallOperationAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCentralBufferNodeInstance()">
<h3>createCentralBufferNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNode</a></span> <span class="element-name">createCentralBufferNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type CentralBufferNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createChangeEventInstance()">
<h3>createChangeEventInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a></span> <span class="element-name">createChangeEventInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ChangeEvent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClassInstance()">
<h3>createClassInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">createClassInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Class</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClassifierTemplateParameterInstance()">
<h3>createClassifierTemplateParameterInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a></span> <span class="element-name">createClassifierTemplateParameterInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ClassifierTemplateParameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClauseInstance()">
<h3>createClauseInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a></span> <span class="element-name">createClauseInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Clause</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClearAssociationActionInstance()">
<h3>createClearAssociationActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a></span> <span class="element-name">createClearAssociationActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ClearAssociationAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClearStructuralFeatureActionInstance()">
<h3>createClearStructuralFeatureActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a></span> <span class="element-name">createClearStructuralFeatureActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ClearStructuralFeatureAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClearVariableActionInstance()">
<h3>createClearVariableActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a></span> <span class="element-name">createClearVariableActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ClearVariableAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCollaborationInstance()">
<h3>createCollaborationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a></span> <span class="element-name">createCollaborationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Collaboration</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCollaborationUseInstance()">
<h3>createCollaborationUseInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a></span> <span class="element-name">createCollaborationUseInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type CollaborationUse</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCombinedFragmentInstance()">
<h3>createCombinedFragmentInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a></span> <span class="element-name">createCombinedFragmentInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type CombinedFragment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCommentInstance()">
<h3>createCommentInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></span> <span class="element-name">createCommentInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Comment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCommunicationPathInstance()">
<h3>createCommunicationPathInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a></span> <span class="element-name">createCommunicationPathInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type CommunicationPath</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComponentInstance()">
<h3>createComponentInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a></span> <span class="element-name">createComponentInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Component</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComponentRealizationInstance()">
<h3>createComponentRealizationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a></span> <span class="element-name">createComponentRealizationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ComponentRealization</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConditionalNodeInstance()">
<h3>createConditionalNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></span> <span class="element-name">createConditionalNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ConditionalNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectableElementTemplateParameterInstance()">
<h3>createConnectableElementTemplateParameterInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a></span> <span class="element-name">createConnectableElementTemplateParameterInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ConnectableElementTemplateParameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectionPointReferenceInstance()">
<h3>createConnectionPointReferenceInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a></span> <span class="element-name">createConnectionPointReferenceInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ConnectionPointReference</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectorInstance()">
<h3>createConnectorInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a></span> <span class="element-name">createConnectorInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Connector</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectorEndInstance()">
<h3>createConnectorEndInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a></span> <span class="element-name">createConnectorEndInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ConnectorEnd</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConsiderIgnoreFragmentInstance()">
<h3>createConsiderIgnoreFragmentInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragment</a></span> <span class="element-name">createConsiderIgnoreFragmentInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ConsiderIgnoreFragment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConstraintInstance()">
<h3>createConstraintInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">createConstraintInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Constraint</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createContinuationInstance()">
<h3>createContinuationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Continuation</a></span> <span class="element-name">createContinuationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Continuation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createControlFlowInstance()">
<h3>createControlFlowInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a></span> <span class="element-name">createControlFlowInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ControlFlow</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCreateLinkActionInstance()">
<h3>createCreateLinkActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a></span> <span class="element-name">createCreateLinkActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type CreateLinkAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCreateLinkObjectActionInstance()">
<h3>createCreateLinkObjectActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a></span> <span class="element-name">createCreateLinkObjectActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type CreateLinkObjectAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCreateObjectActionInstance()">
<h3>createCreateObjectActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a></span> <span class="element-name">createCreateObjectActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type CreateObjectAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDataStoreNodeInstance()">
<h3>createDataStoreNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNode</a></span> <span class="element-name">createDataStoreNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type DataStoreNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDataTypeInstance()">
<h3>createDataTypeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></span> <span class="element-name">createDataTypeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type DataType</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDecisionNodeInstance()">
<h3>createDecisionNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a></span> <span class="element-name">createDecisionNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type DecisionNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDependencyInstance()">
<h3>createDependencyInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a></span> <span class="element-name">createDependencyInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Dependency</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDeploymentInstance()">
<h3>createDeploymentInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a></span> <span class="element-name">createDeploymentInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Deployment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDeploymentSpecificationInstance()">
<h3>createDeploymentSpecificationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a></span> <span class="element-name">createDeploymentSpecificationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type DeploymentSpecification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDestroyLinkActionInstance()">
<h3>createDestroyLinkActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a></span> <span class="element-name">createDestroyLinkActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type DestroyLinkAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDestroyObjectActionInstance()">
<h3>createDestroyObjectActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a></span> <span class="element-name">createDestroyObjectActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type DestroyObjectAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDestructionOccurrenceSpecificationInstance()">
<h3>createDestructionOccurrenceSpecificationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a></span> <span class="element-name">createDestructionOccurrenceSpecificationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type DestructionOccurrenceSpecification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDeviceInstance()">
<h3>createDeviceInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a></span> <span class="element-name">createDeviceInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Device</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDiagramInstance()">
<h3>createDiagramInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></span> <span class="element-name">createDiagramInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDurationInstance()">
<h3>createDurationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></span> <span class="element-name">createDurationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Duration</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDurationConstraintInstance()">
<h3>createDurationConstraintInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a></span> <span class="element-name">createDurationConstraintInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type DurationConstraint</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDurationIntervalInstance()">
<h3>createDurationIntervalInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a></span> <span class="element-name">createDurationIntervalInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type DurationInterval</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDurationObservationInstance()">
<h3>createDurationObservationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a></span> <span class="element-name">createDurationObservationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type DurationObservation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createElementImportInstance()">
<h3>createElementImportInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a></span> <span class="element-name">createElementImportInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ElementImport</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createElementValueInstance()">
<h3>createElementValueInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a></span> <span class="element-name">createElementValueInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ElementValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEnumerationInstance()">
<h3>createEnumerationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">createEnumerationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Enumeration</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEnumerationLiteralInstance()">
<h3>createEnumerationLiteralInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">createEnumerationLiteralInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type EnumerationLiteral</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExceptionHandlerInstance()">
<h3>createExceptionHandlerInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a></span> <span class="element-name">createExceptionHandlerInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ExceptionHandler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExecutionEnvironmentInstance()">
<h3>createExecutionEnvironmentInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a></span> <span class="element-name">createExecutionEnvironmentInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ExecutionEnvironment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExecutionOccurrenceSpecificationInstance()">
<h3>createExecutionOccurrenceSpecificationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionOccurrenceSpecification</a></span> <span class="element-name">createExecutionOccurrenceSpecificationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ExecutionOccurrenceSpecification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExpansionNodeInstance()">
<h3>createExpansionNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNode</a></span> <span class="element-name">createExpansionNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ExpansionNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExpansionRegionInstance()">
<h3>createExpansionRegionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a></span> <span class="element-name">createExpansionRegionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ExpansionRegion</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExpressionInstance()">
<h3>createExpressionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a></span> <span class="element-name">createExpressionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExtendInstance()">
<h3>createExtendInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a></span> <span class="element-name">createExtendInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Extend</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExtensionInstance()">
<h3>createExtensionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></span> <span class="element-name">createExtensionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Extension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExtensionEndInstance()">
<h3>createExtensionEndInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></span> <span class="element-name">createExtensionEndInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ExtensionEnd</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExtensionPointInstance()">
<h3>createExtensionPointInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPoint</a></span> <span class="element-name">createExtensionPointInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ExtensionPoint</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFinalStateInstance()">
<h3>createFinalStateInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a></span> <span class="element-name">createFinalStateInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type FinalState</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFlowFinalNodeInstance()">
<h3>createFlowFinalNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNode</a></span> <span class="element-name">createFlowFinalNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type FlowFinalNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createForkNodeInstance()">
<h3>createForkNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNode</a></span> <span class="element-name">createForkNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ForkNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFunctionBehaviorInstance()">
<h3>createFunctionBehaviorInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a></span> <span class="element-name">createFunctionBehaviorInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type FunctionBehavior</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGateInstance()">
<h3>createGateInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a></span> <span class="element-name">createGateInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Gate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGeneralOrderingInstance()">
<h3>createGeneralOrderingInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">GeneralOrdering</a></span> <span class="element-name">createGeneralOrderingInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type GeneralOrdering</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGeneralizationInstance()">
<h3>createGeneralizationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a></span> <span class="element-name">createGeneralizationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Generalization</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGeneralizationSetInstance()">
<h3>createGeneralizationSetInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a></span> <span class="element-name">createGeneralizationSetInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type GeneralizationSet</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImageInstance()">
<h3>createImageInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a></span> <span class="element-name">createImageInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIncludeInstance()">
<h3>createIncludeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Include</a></span> <span class="element-name">createIncludeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Include</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInformationFlowInstance()">
<h3>createInformationFlowInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a></span> <span class="element-name">createInformationFlowInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type InformationFlow</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInformationItemInstance()">
<h3>createInformationItemInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a></span> <span class="element-name">createInformationItemInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type InformationItem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInitialNodeInstance()">
<h3>createInitialNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNode</a></span> <span class="element-name">createInitialNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type InitialNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInputPinInstance()">
<h3>createInputPinInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></span> <span class="element-name">createInputPinInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type InputPin</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInstanceSpecificationInstance()">
<h3>createInstanceSpecificationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a></span> <span class="element-name">createInstanceSpecificationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type InstanceSpecification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInstanceValueInstance()">
<h3>createInstanceValueInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a></span> <span class="element-name">createInstanceValueInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type InstanceValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionInstance()">
<h3>createInteractionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></span> <span class="element-name">createInteractionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Interaction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionConstraintInstance()">
<h3>createInteractionConstraintInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></span> <span class="element-name">createInteractionConstraintInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type InteractionConstraint</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionOperandInstance()">
<h3>createInteractionOperandInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a></span> <span class="element-name">createInteractionOperandInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type InteractionOperand</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionUseInstance()">
<h3>createInteractionUseInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a></span> <span class="element-name">createInteractionUseInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type InteractionUse</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInterfaceInstance()">
<h3>createInterfaceInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></span> <span class="element-name">createInterfaceInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Interface</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInterfaceRealizationInstance()">
<h3>createInterfaceRealizationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a></span> <span class="element-name">createInterfaceRealizationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type InterfaceRealization</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInterruptibleActivityRegionInstance()">
<h3>createInterruptibleActivityRegionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a></span> <span class="element-name">createInterruptibleActivityRegionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type InterruptibleActivityRegion</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIntervalInstance()">
<h3>createIntervalInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></span> <span class="element-name">createIntervalInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Interval</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIntervalConstraintInstance()">
<h3>createIntervalConstraintInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a></span> <span class="element-name">createIntervalConstraintInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type IntervalConstraint</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createJoinNodeInstance()">
<h3>createJoinNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a></span> <span class="element-name">createJoinNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type JoinNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLifelineInstance()">
<h3>createLifelineInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a></span> <span class="element-name">createLifelineInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Lifeline</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLinkEndCreationDataInstance()">
<h3>createLinkEndCreationDataInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a></span> <span class="element-name">createLinkEndCreationDataInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type LinkEndCreationData</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLinkEndDataInstance()">
<h3>createLinkEndDataInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a></span> <span class="element-name">createLinkEndDataInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type LinkEndData</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLinkEndDestructionDataInstance()">
<h3>createLinkEndDestructionDataInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a></span> <span class="element-name">createLinkEndDestructionDataInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type LinkEndDestructionData</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralBooleanInstance()">
<h3>createLiteralBooleanInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBoolean</a></span> <span class="element-name">createLiteralBooleanInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type LiteralBoolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralIntegerInstance()">
<h3>createLiteralIntegerInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralInteger</a></span> <span class="element-name">createLiteralIntegerInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type LiteralInteger</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralNullInstance()">
<h3>createLiteralNullInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNull</a></span> <span class="element-name">createLiteralNullInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type LiteralNull</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralRealInstance()">
<h3>createLiteralRealInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralReal</a></span> <span class="element-name">createLiteralRealInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type LiteralReal</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralStringInstance()">
<h3>createLiteralStringInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralString</a></span> <span class="element-name">createLiteralStringInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type LiteralString</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralUnlimitedNaturalInstance()">
<h3>createLiteralUnlimitedNaturalInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNatural</a></span> <span class="element-name">createLiteralUnlimitedNaturalInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type LiteralUnlimitedNatural</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLoopNodeInstance()">
<h3>createLoopNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></span> <span class="element-name">createLoopNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type LoopNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createManifestationInstance()">
<h3>createManifestationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Manifestation</a></span> <span class="element-name">createManifestationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Manifestation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMergeNodeInstance()">
<h3>createMergeNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a></span> <span class="element-name">createMergeNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type MergeNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMessageInstance()">
<h3>createMessageInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></span> <span class="element-name">createMessageInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMessageOccurrenceSpecificationInstance()">
<h3>createMessageOccurrenceSpecificationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecification</a></span> <span class="element-name">createMessageOccurrenceSpecificationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type MessageOccurrenceSpecification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createModelInstance()">
<h3>createModelInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></span> <span class="element-name">createModelInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNodeInstance()">
<h3>createNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a></span> <span class="element-name">createNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createObjectFlowInstance()">
<h3>createObjectFlowInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a></span> <span class="element-name">createObjectFlowInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ObjectFlow</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOccurrenceSpecificationInstance()">
<h3>createOccurrenceSpecificationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecification</a></span> <span class="element-name">createOccurrenceSpecificationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type OccurrenceSpecification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOpaqueActionInstance()">
<h3>createOpaqueActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></span> <span class="element-name">createOpaqueActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type OpaqueAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOpaqueBehaviorInstance()">
<h3>createOpaqueBehaviorInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a></span> <span class="element-name">createOpaqueBehaviorInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type OpaqueBehavior</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOpaqueExpressionInstance()">
<h3>createOpaqueExpressionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a></span> <span class="element-name">createOpaqueExpressionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type OpaqueExpression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperationInstance()">
<h3>createOperationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></span> <span class="element-name">createOperationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Operation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperationTemplateParameterInstance()">
<h3>createOperationTemplateParameterInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a></span> <span class="element-name">createOperationTemplateParameterInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type OperationTemplateParameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOutputPinInstance()">
<h3>createOutputPinInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></span> <span class="element-name">createOutputPinInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type OutputPin</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackageInstance()">
<h3>createPackageInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">createPackageInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Package</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackageImportInstance()">
<h3>createPackageImportInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a></span> <span class="element-name">createPackageImportInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type PackageImport</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackageMergeInstance()">
<h3>createPackageMergeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageMerge</a></span> <span class="element-name">createPackageMergeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type PackageMerge</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameterInstance()">
<h3>createParameterInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></span> <span class="element-name">createParameterInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameterSetInstance()">
<h3>createParameterSetInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a></span> <span class="element-name">createParameterSetInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ParameterSet</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPartDecompositionInstance()">
<h3>createPartDecompositionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a></span> <span class="element-name">createPartDecompositionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type PartDecomposition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPortInstance()">
<h3>createPortInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a></span> <span class="element-name">createPortInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Port</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPrimitiveTypeInstance()">
<h3>createPrimitiveTypeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a></span> <span class="element-name">createPrimitiveTypeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type PrimitiveType</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProfileInstance()">
<h3>createProfileInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></span> <span class="element-name">createProfileInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Profile</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProfileApplicationInstance()">
<h3>createProfileApplicationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplication</a></span> <span class="element-name">createProfileApplicationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ProfileApplication</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPropertyInstance()">
<h3>createPropertyInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">createPropertyInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProtocolConformanceInstance()">
<h3>createProtocolConformanceInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolConformance</a></span> <span class="element-name">createProtocolConformanceInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ProtocolConformance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProtocolStateMachineInstance()">
<h3>createProtocolStateMachineInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></span> <span class="element-name">createProtocolStateMachineInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ProtocolStateMachine</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProtocolTransitionInstance()">
<h3>createProtocolTransitionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></span> <span class="element-name">createProtocolTransitionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ProtocolTransition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPseudostateInstance()">
<h3>createPseudostateInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a></span> <span class="element-name">createPseudostateInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Pseudostate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createQualifierValueInstance()">
<h3>createQualifierValueInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a></span> <span class="element-name">createQualifierValueInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type QualifierValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRaiseExceptionActionInstance()">
<h3>createRaiseExceptionActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a></span> <span class="element-name">createRaiseExceptionActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type RaiseExceptionAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadExtentActionInstance()">
<h3>createReadExtentActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a></span> <span class="element-name">createReadExtentActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ReadExtentAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadIsClassifiedObjectActionInstance()">
<h3>createReadIsClassifiedObjectActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></span> <span class="element-name">createReadIsClassifiedObjectActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ReadIsClassifiedObjectAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadLinkActionInstance()">
<h3>createReadLinkActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a></span> <span class="element-name">createReadLinkActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ReadLinkAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadLinkObjectEndActionInstance()">
<h3>createReadLinkObjectEndActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></span> <span class="element-name">createReadLinkObjectEndActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ReadLinkObjectEndAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadLinkObjectEndQualifierActionInstance()">
<h3>createReadLinkObjectEndQualifierActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></span> <span class="element-name">createReadLinkObjectEndQualifierActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ReadLinkObjectEndQualifierAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadSelfActionInstance()">
<h3>createReadSelfActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a></span> <span class="element-name">createReadSelfActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ReadSelfAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadStructuralFeatureActionInstance()">
<h3>createReadStructuralFeatureActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a></span> <span class="element-name">createReadStructuralFeatureActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ReadStructuralFeatureAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadVariableActionInstance()">
<h3>createReadVariableActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a></span> <span class="element-name">createReadVariableActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ReadVariableAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRealizationInstance()">
<h3>createRealizationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a></span> <span class="element-name">createRealizationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Realization</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReceptionInstance()">
<h3>createReceptionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a></span> <span class="element-name">createReceptionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Reception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReclassifyObjectActionInstance()">
<h3>createReclassifyObjectActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a></span> <span class="element-name">createReclassifyObjectActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ReclassifyObjectAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRedefinableTemplateSignatureInstance()">
<h3>createRedefinableTemplateSignatureInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a></span> <span class="element-name">createRedefinableTemplateSignatureInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type RedefinableTemplateSignature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReduceActionInstance()">
<h3>createReduceActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></span> <span class="element-name">createReduceActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ReduceAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRegionInstance()">
<h3>createRegionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a></span> <span class="element-name">createRegionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Region</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRemoveStructuralFeatureValueActionInstance()">
<h3>createRemoveStructuralFeatureValueActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a></span> <span class="element-name">createRemoveStructuralFeatureValueActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type RemoveStructuralFeatureValueAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRemoveVariableValueActionInstance()">
<h3>createRemoveVariableValueActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a></span> <span class="element-name">createRemoveVariableValueActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type RemoveVariableValueAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReplyActionInstance()">
<h3>createReplyActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></span> <span class="element-name">createReplyActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ReplyAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSendObjectActionInstance()">
<h3>createSendObjectActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></span> <span class="element-name">createSendObjectActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type SendObjectAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSendSignalActionInstance()">
<h3>createSendSignalActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a></span> <span class="element-name">createSendSignalActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type SendSignalAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSequenceNodeInstance()">
<h3>createSequenceNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></span> <span class="element-name">createSequenceNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type SequenceNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSignalInstance()">
<h3>createSignalInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></span> <span class="element-name">createSignalInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Signal</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSignalEventInstance()">
<h3>createSignalEventInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a></span> <span class="element-name">createSignalEventInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type SignalEvent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlotInstance()">
<h3>createSlotInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></span> <span class="element-name">createSlotInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Slot</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStartClassifierBehaviorActionInstance()">
<h3>createStartClassifierBehaviorActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a></span> <span class="element-name">createStartClassifierBehaviorActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type StartClassifierBehaviorAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStartObjectBehaviorActionInstance()">
<h3>createStartObjectBehaviorActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a></span> <span class="element-name">createStartObjectBehaviorActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type StartObjectBehaviorAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateInstance()">
<h3>createStateInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></span> <span class="element-name">createStateInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type State</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateInvariantInstance()">
<h3>createStateInvariantInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a></span> <span class="element-name">createStateInvariantInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type StateInvariant</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateMachineInstance()">
<h3>createStateMachineInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></span> <span class="element-name">createStateMachineInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type StateMachine</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotypeInstance()">
<h3>createStereotypeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">createStereotypeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStringExpressionInstance()">
<h3>createStringExpressionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a></span> <span class="element-name">createStringExpressionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type StringExpression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStructuredActivityNodeInstance()">
<h3>createStructuredActivityNodeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></span> <span class="element-name">createStructuredActivityNodeInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type StructuredActivityNode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSubstitutionInstance()">
<h3>createSubstitutionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a></span> <span class="element-name">createSubstitutionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Substitution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateBindingInstance()">
<h3>createTemplateBindingInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a></span> <span class="element-name">createTemplateBindingInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type TemplateBinding</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateParameterInstance()">
<h3>createTemplateParameterInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></span> <span class="element-name">createTemplateParameterInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type TemplateParameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateParameterSubstitutionInstance()">
<h3>createTemplateParameterSubstitutionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a></span> <span class="element-name">createTemplateParameterSubstitutionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type TemplateParameterSubstitution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateSignatureInstance()">
<h3>createTemplateSignatureInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a></span> <span class="element-name">createTemplateSignatureInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type TemplateSignature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTestIdentityActionInstance()">
<h3>createTestIdentityActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></span> <span class="element-name">createTestIdentityActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type TestIdentityAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeConstraintInstance()">
<h3>createTimeConstraintInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a></span> <span class="element-name">createTimeConstraintInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type TimeConstraint</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeEventInstance()">
<h3>createTimeEventInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEvent</a></span> <span class="element-name">createTimeEventInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type TimeEvent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeExpressionInstance()">
<h3>createTimeExpressionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></span> <span class="element-name">createTimeExpressionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type TimeExpression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeIntervalInstance()">
<h3>createTimeIntervalInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a></span> <span class="element-name">createTimeIntervalInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type TimeInterval</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeObservationInstance()">
<h3>createTimeObservationInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a></span> <span class="element-name">createTimeObservationInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type TimeObservation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTransitionInstance()">
<h3>createTransitionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></span> <span class="element-name">createTransitionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Transition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTriggerInstance()">
<h3>createTriggerInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a></span> <span class="element-name">createTriggerInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Trigger</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUnmarshallActionInstance()">
<h3>createUnmarshallActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></span> <span class="element-name">createUnmarshallActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type UnmarshallAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUsageInstance()">
<h3>createUsageInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Usage</a></span> <span class="element-name">createUsageInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUseCaseInstance()">
<h3>createUseCaseInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></span> <span class="element-name">createUseCaseInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type UseCase</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValuePinInstance()">
<h3>createValuePinInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a></span> <span class="element-name">createValuePinInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ValuePin</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueSpecificationActionInstance()">
<h3>createValueSpecificationActionInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></span> <span class="element-name">createValueSpecificationActionInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ValueSpecificationAction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createVariableInstance()">
<h3>createVariableInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a></span> <span class="element-name">createVariableInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type Variable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBooleanTaggedValueInstance()">
<h3>createBooleanTaggedValueInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BooleanTaggedValue</a></span> <span class="element-name">createBooleanTaggedValueInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type BooleanTaggedValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIntegerTaggedValueInstance()">
<h3>createIntegerTaggedValueInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">IntegerTaggedValue</a></span> <span class="element-name">createIntegerTaggedValueInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type IntegerTaggedValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRealTaggedValueInstance()">
<h3>createRealTaggedValueInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/RealTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RealTaggedValue</a></span> <span class="element-name">createRealTaggedValueInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type RealTaggedValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStringTaggedValueInstance()">
<h3>createStringTaggedValueInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/StringTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StringTaggedValue</a></span> <span class="element-name">createStringTaggedValueInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type StringTaggedValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createElementTaggedValueInstance()">
<h3>createElementTaggedValueInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ext/magicdraw/classes/mdkernel/ElementTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementTaggedValue</a></span> <span class="element-name">createElementTaggedValueInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created instance of type ElementTaggedValue</dd>
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
