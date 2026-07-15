# JAVA OPENAPI: BaseElement (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/BaseElement.html
- source_path: `com/nomagic/magicdraw/uml/BaseElement.html`
- source_sha256: `b4a00c82a7e7fb8492fa6efc006d4c56056c22e8b8d749e5f64246d7431fcd89`
- captured_utc: `2026-07-14T16:55:55.138454+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Interface BaseElement

All Superinterfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`

All Known Subinterfaces:
`[Abstraction](../../uml2/ext/magicdraw/classes/mddependencies/Abstraction.html)`, `[AcceptCallAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html)`, `[AcceptEventAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html)`, `[Action](../../uml2/ext/magicdraw/actions/mdbasicactions/Action.html)`, `[ActionExecutionSpecification](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html)`, `[ActionInputPin](../../uml2/ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html)`, `[Activity](../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html)`, `[ActivityEdge](../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html)`, `[ActivityFinalNode](../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html)`, `[ActivityGroup](../../uml2/ext/magicdraw/activities/mdfundamentalactivities/ActivityGroup.html)`, `[ActivityNode](../../uml2/ext/magicdraw/activities/mdfundamentalactivities/ActivityNode.html)`, `[ActivityParameterNode](../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html)`, `[ActivityPartition](../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html)`, `[Actor](../../uml2/ext/magicdraw/mdusecases/Actor.html)`, `[AddStructuralFeatureValueAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html)`, `[AddVariableValueAction](../../uml2/ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html)`, `[AnyReceiveEvent](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html)`, `[Artifact](../../uml2/ext/magicdraw/deployments/mdartifacts/Artifact.html)`, `[Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html)`, `[AssociationClass](../../uml2/ext/magicdraw/classes/mdassociationclasses/AssociationClass.html)`, `[Behavior](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html)`, `[BehavioralFeature](../../uml2/ext/magicdraw/classes/mdkernel/BehavioralFeature.html)`, `[BehavioredClassifier](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)`, `[BehaviorExecutionSpecification](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html)`, `[BooleanTaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html)`, `[BroadcastSignalAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html)`, `[CallAction](../../uml2/ext/magicdraw/actions/mdbasicactions/CallAction.html)`, `[CallBehaviorAction](../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html)`, `[CallEvent](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html)`, `[CallOperationAction](../../uml2/ext/magicdraw/actions/mdbasicactions/CallOperationAction.html)`, `[CentralBufferNode](../../uml2/ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html)`, `[ChangeEvent](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html)`, `[Class](../../uml2/ext/magicdraw/classes/mdkernel/Class.html)`, `[Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`, `[ClassifierTemplateParameter](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html)`, `[Clause](../../uml2/ext/magicdraw/activities/mdstructuredactivities/Clause.html)`, `[ClearAssociationAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html)`, `[ClearStructuralFeatureAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html)`, `[ClearVariableAction](../../uml2/ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html)`, `[Collaboration](../../uml2/ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html)`, `[CollaborationUse](../../uml2/ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html)`, `[CombinedFragment](../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html)`, `[Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html)`, `[CommunicationPath](../../uml2/ext/magicdraw/deployments/mdnodes/CommunicationPath.html)`, `[Component](../../uml2/ext/magicdraw/components/mdbasiccomponents/Component.html)`, `[ComponentRealization](../../uml2/ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html)`, `[ConditionalNode](../../uml2/ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html)`, `[ConnectableElement](../../uml2/ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html)`, `[ConnectableElementTemplateParameter](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html)`, `[ConnectionPointReference](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html)`, `[Connector](../../uml2/ext/magicdraw/compositestructures/mdinternalstructures/Connector.html)`, `[ConnectorEnd](../../uml2/ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html)`, `[ConsiderIgnoreFragment](../../uml2/ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html)`, `[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)`, `[Continuation](../../uml2/ext/magicdraw/interactions/mdfragments/Continuation.html)`, `[ControlFlow](../../uml2/ext/magicdraw/activities/mdbasicactivities/ControlFlow.html)`, `[ControlNode](../../uml2/ext/magicdraw/activities/mdbasicactivities/ControlNode.html)`, `[CreateLinkAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html)`, `[CreateLinkObjectAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html)`, `[CreateObjectAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html)`, `[DataStoreNode](../../uml2/ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html)`, `[DataType](../../uml2/ext/magicdraw/classes/mdkernel/DataType.html)`, `[DecisionNode](../../uml2/ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html)`, `[Dependency](../../uml2/ext/magicdraw/classes/mddependencies/Dependency.html)`, `[DeployedArtifact](../../uml2/ext/magicdraw/deployments/mdnodes/DeployedArtifact.html)`, `[Deployment](../../uml2/ext/magicdraw/deployments/mdnodes/Deployment.html)`, `[DeploymentSpecification](../../uml2/ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html)`, `[DeploymentTarget](../../uml2/ext/magicdraw/deployments/mdnodes/DeploymentTarget.html)`, `[DestroyLinkAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html)`, `[DestroyObjectAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html)`, `[DestructionOccurrenceSpecification](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html)`, `[Device](../../uml2/ext/magicdraw/deployments/mdnodes/Device.html)`, `[Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)`, `[DirectedRelationship](../../uml2/ext/magicdraw/classes/mdkernel/DirectedRelationship.html)`, `[Duration](../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html)`, `[DurationConstraint](../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html)`, `[DurationInterval](../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html)`, `[DurationObservation](../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html)`, `[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`, `[ElementImport](../../uml2/ext/magicdraw/classes/mdkernel/ElementImport.html)`, `[ElementTaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/ElementTaggedValue.html)`, `[ElementValue](../../uml2/ext/magicdraw/classes/mdkernel/ElementValue.html)`, `[EncapsulatedClassifier](../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html)`, `[Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html)`, `[EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`, `[Event](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html)`, `[ExceptionHandler](../../uml2/ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html)`, `[ExecutableNode](../../uml2/ext/magicdraw/activities/mdstructuredactivities/ExecutableNode.html)`, `[ExecutionEnvironment](../../uml2/ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html)`, `[ExecutionOccurrenceSpecification](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html)`, `[ExecutionSpecification](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html)`, `[ExpansionNode](../../uml2/ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html)`, `[ExpansionRegion](../../uml2/ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html)`, `[Expression](../../uml2/ext/magicdraw/classes/mdkernel/Expression.html)`, `[Extend](../../uml2/ext/magicdraw/mdusecases/Extend.html)`, `[Extension](../../uml2/ext/magicdraw/mdprofiles/Extension.html)`, `[ExtensionEnd](../../uml2/ext/magicdraw/mdprofiles/ExtensionEnd.html)`, `[ExtensionPoint](../../uml2/ext/magicdraw/mdusecases/ExtensionPoint.html)`, `[Feature](../../uml2/ext/magicdraw/classes/mdkernel/Feature.html)`, `[FinalNode](../../uml2/ext/magicdraw/activities/mdintermediateactivities/FinalNode.html)`, `[FinalState](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html)`, `[FlowFinalNode](../../uml2/ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html)`, `[ForkNode](../../uml2/ext/magicdraw/activities/mdintermediateactivities/ForkNode.html)`, `[FunctionBehavior](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html)`, `[Gate](../../uml2/ext/magicdraw/interactions/mdfragments/Gate.html)`, `[Generalization](../../uml2/ext/magicdraw/classes/mdkernel/Generalization.html)`, `[GeneralizationSet](../../uml2/ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html)`, `[GeneralOrdering](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html)`, `[Image](../../uml2/ext/magicdraw/mdprofiles/Image.html)`, `[Include](../../uml2/ext/magicdraw/mdusecases/Include.html)`, `[InformationFlow](../../uml2/ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html)`, `[InformationItem](../../uml2/ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html)`, `[InitialNode](../../uml2/ext/magicdraw/activities/mdbasicactivities/InitialNode.html)`, `[InputPin](../../uml2/ext/magicdraw/actions/mdbasicactions/InputPin.html)`, `[InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html)`, `[InstanceValue](../../uml2/ext/magicdraw/classes/mdkernel/InstanceValue.html)`, `[IntegerTaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html)`, `[Interaction](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Interaction.html)`, `[InteractionConstraint](../../uml2/ext/magicdraw/interactions/mdfragments/InteractionConstraint.html)`, `[InteractionFragment](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/InteractionFragment.html)`, `[InteractionOperand](../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html)`, `[InteractionUse](../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html)`, `[Interface](../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html)`, `[InterfaceRealization](../../uml2/ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html)`, `[InterruptibleActivityRegion](../../uml2/ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html)`, `[Interval](../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html)`, `[IntervalConstraint](../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html)`, `[InvocationAction](../../uml2/ext/magicdraw/actions/mdbasicactions/InvocationAction.html)`, `[JoinNode](../../uml2/ext/magicdraw/activities/mdintermediateactivities/JoinNode.html)`, `[Lifeline](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html)`, `[LinkAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/LinkAction.html)`, `[LinkEndCreationData](../../uml2/ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html)`, `[LinkEndData](../../uml2/ext/magicdraw/actions/mdintermediateactions/LinkEndData.html)`, `[LinkEndDestructionData](../../uml2/ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html)`, `[LiteralBoolean](../../uml2/ext/magicdraw/classes/mdkernel/LiteralBoolean.html)`, `[LiteralInteger](../../uml2/ext/magicdraw/classes/mdkernel/LiteralInteger.html)`, `[LiteralNull](../../uml2/ext/magicdraw/classes/mdkernel/LiteralNull.html)`, `[LiteralReal](../../uml2/ext/magicdraw/classes/mdkernel/LiteralReal.html)`, `[LiteralSpecification](../../uml2/ext/magicdraw/classes/mdkernel/LiteralSpecification.html)`, `[LiteralString](../../uml2/ext/magicdraw/classes/mdkernel/LiteralString.html)`, `[LiteralUnlimitedNatural](../../uml2/ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html)`, `[LoopNode](../../uml2/ext/magicdraw/activities/mdstructuredactivities/LoopNode.html)`, `[Manifestation](../../uml2/ext/magicdraw/deployments/mdartifacts/Manifestation.html)`, `[MDElement](MDElement.html)`, `[MDObject](../foundation/MDObject.html)`, `[MergeNode](../../uml2/ext/magicdraw/activities/mdintermediateactivities/MergeNode.html)`, `[Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html)`, `[MessageEnd](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageEnd.html)`, `[MessageEvent](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/MessageEvent.html)`, `[MessageOccurrenceSpecification](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html)`, `[Model](../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../uml2/ext/magicdraw/base/ModelObject.html)`, `[MultiplicityElement](../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html)`, `[NamedElement](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)`, `[Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html)`, `[Node](../../uml2/ext/magicdraw/deployments/mdnodes/Node.html)`, `[ObjectFlow](../../uml2/ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html)`, `[ObjectNode](../../uml2/ext/magicdraw/activities/mdbasicactivities/ObjectNode.html)`, `[Observation](../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/Observation.html)`, `[OccurrenceSpecification](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html)`, `[OpaqueAction](../../uml2/ext/magicdraw/actions/mdbasicactions/OpaqueAction.html)`, `[OpaqueBehavior](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html)`, `[OpaqueExpression](../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html)`, `[Operation](../../uml2/ext/magicdraw/classes/mdkernel/Operation.html)`, `[OperationTemplateParameter](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html)`, `[OutputPin](../../uml2/ext/magicdraw/actions/mdbasicactions/OutputPin.html)`, `[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)`, `[PackageableElement](../../uml2/ext/magicdraw/classes/mdkernel/PackageableElement.html)`, `[PackageImport](../../uml2/ext/magicdraw/classes/mdkernel/PackageImport.html)`, `[PackageMerge](../../uml2/ext/magicdraw/classes/mdkernel/PackageMerge.html)`, `[Parameter](../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html)`, `[ParameterableElement](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[ParameterSet](../../uml2/ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html)`, `[PartDecomposition](../../uml2/ext/magicdraw/interactions/mdfragments/PartDecomposition.html)`, `[Pin](../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html)`, `[Port](../../uml2/ext/magicdraw/compositestructures/mdports/Port.html)`, `[PrimitiveType](../../uml2/ext/magicdraw/classes/mdkernel/PrimitiveType.html)`, `[Profile](../../uml2/ext/magicdraw/mdprofiles/Profile.html)`, `[ProfileApplication](../../uml2/ext/magicdraw/mdprofiles/ProfileApplication.html)`, `[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`, `[ProtocolConformance](../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html)`, `[ProtocolStateMachine](../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)`, `[ProtocolTransition](../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html)`, `[Pseudostate](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html)`, `[QualifierValue](../../uml2/ext/magicdraw/actions/mdcompleteactions/QualifierValue.html)`, `[RaiseExceptionAction](../../uml2/ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html)`, `[ReadExtentAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html)`, `[ReadIsClassifiedObjectAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html)`, `[ReadLinkAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html)`, `[ReadLinkObjectEndAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html)`, `[ReadLinkObjectEndQualifierAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html)`, `[ReadSelfAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html)`, `[ReadStructuralFeatureAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html)`, `[ReadVariableAction](../../uml2/ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html)`, `[Realization](../../uml2/ext/magicdraw/classes/mddependencies/Realization.html)`, `[RealTaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/RealTaggedValue.html)`, `[Reception](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html)`, `[ReclassifyObjectAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html)`, `[RedefinableElement](../../uml2/ext/magicdraw/classes/mdkernel/RedefinableElement.html)`, `[RedefinableTemplateSignature](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html)`, `[ReduceAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/ReduceAction.html)`, `[Region](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html)`, `[Relationship](../../uml2/ext/magicdraw/classes/mdkernel/Relationship.html)`, `[RemoveStructuralFeatureValueAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html)`, `[RemoveVariableValueAction](../../uml2/ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html)`, `[ReplyAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/ReplyAction.html)`, `[SendObjectAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html)`, `[SendSignalAction](../../uml2/ext/magicdraw/actions/mdbasicactions/SendSignalAction.html)`, `[SequenceNode](../../uml2/ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html)`, `[Signal](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html)`, `[SignalEvent](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html)`, `[Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html)`, `[StartClassifierBehaviorAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html)`, `[StartObjectBehaviorAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html)`, `[State](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html)`, `[StateInvariant](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html)`, `[StateMachine](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html)`, `[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`, `[StringExpression](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html)`, `[StringTaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/StringTaggedValue.html)`, `[StructuralFeature](../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html)`, `[StructuralFeatureAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html)`, `[StructuredActivityNode](../../uml2/ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html)`, `[StructuredClassifier](../../uml2/ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html)`, `[Substitution](../../uml2/ext/magicdraw/classes/mddependencies/Substitution.html)`, `[TaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html)`, `[TemplateableElement](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html)`, `[TemplateBinding](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html)`, `[TemplateParameter](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html)`, `[TemplateParameterSubstitution](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html)`, `[TemplateSignature](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html)`, `[TestIdentityAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html)`, `[TimeConstraint](../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html)`, `[TimeEvent](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html)`, `[TimeExpression](../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html)`, `[TimeInterval](../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html)`, `[TimeObservation](../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html)`, `[Transition](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html)`, `[Trigger](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html)`, `[Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html)`, `[TypedElement](../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html)`, `[UnmarshallAction](../../uml2/ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html)`, `[Usage](../../uml2/ext/magicdraw/classes/mddependencies/Usage.html)`, `[UseCase](../../uml2/ext/magicdraw/mdusecases/UseCase.html)`, `[ValuePin](../../uml2/ext/magicdraw/actions/mdbasicactions/ValuePin.html)`, `[ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html)`, `[ValueSpecificationAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html)`, `[Variable](../../uml2/ext/magicdraw/activities/mdstructuredactivities/Variable.html)`, `[VariableAction](../../uml2/ext/magicdraw/actions/mdstructuredactions/VariableAction.html)`, `[Vertex](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html)`, `[WriteLinkAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/WriteLinkAction.html)`, `[WriteStructuralFeatureAction](../../uml2/ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html)`, `[WriteVariableAction](../../uml2/ext/magicdraw/actions/mdstructuredactions/WriteVariableAction.html)`

All Known Implementing Classes:
`[AbstractDiagramPresentationElement](symbols/AbstractDiagramPresentationElement.html)`, `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`, `com.nomagic.magicdraw.uml.symbols.shapes.AbstractImageShapeView`, `com.nomagic.magicdraw.uml.symbols.shapes.AbstractSeparatorView`, `com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels`, `com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabelsInside`, `com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView`, `[ActionView](symbols/shapes/ActionView.html)`, `[ActivationView](symbols/shapes/ActivationView.html)`, `com.nomagic.magicdraw.uml.symbols.shapes.ActivityGroupView`, `[ActorView](symbols/shapes/ActorView.html)`, `[ArtifactView](symbols/shapes/ArtifactView.html)`, `[AssociationClassView](symbols/paths/AssociationClassView.html)`, `[AssociationView](symbols/paths/AssociationView.html)`, `[BarView](symbols/shapes/BarView.html)`, `com.nomagic.magicdraw.uml.symbols.paths.BaseFlowView`, `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`, `com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineView`, `com.nomagic.magicdraw.uml.symbols.paths.BaseRealizationView`, `com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape`, `[CallBehaviorActionView](symbols/shapes/CallBehaviorActionView.html)`, `[CallOperationActionView](symbols/shapes/CallOperationActionView.html)`, `[ClassifierView](symbols/shapes/ClassifierView.html)`, `[ClassView](symbols/shapes/ClassView.html)`, `[CollaborationUseView](symbols/shapes/CollaborationUseView.html)`, `[CollaborationView](symbols/shapes/CollaborationView.html)`, `[CombinedFragmentView](symbols/shapes/CombinedFragmentView.html)`, `[CommentView](symbols/shapes/CommentView.html)`, `[CommunicationPathView](symbols/paths/CommunicationPathView.html)`, `[ComponentView](symbols/shapes/ComponentView.html)`, `[ConditionalNodeView](symbols/shapes/ConditionalNodeView.html)`, `[ConnectorToSelfView](symbols/paths/ConnectorToSelfView.html)`, `[ConnectorView](symbols/paths/ConnectorView.html)`, `[ConstraintLinkView](symbols/paths/ConstraintLinkView.html)`, `com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView`, `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`, `[ContainmentLinkView](symbols/paths/ContainmentLinkView.html)`, `[ContentShape](symbols/shapes/ContentShape.html)`, `[ControlFlowView](symbols/paths/ControlFlowView.html)`, `[DataTypeView](symbols/shapes/DataTypeView.html)`, `[DecisionView](symbols/shapes/DecisionView.html)`, `[DependencyView](symbols/paths/DependencyView.html)`, `[DeploymentView](symbols/paths/DeploymentView.html)`, `[DiagramFrameView](symbols/shapes/DiagramFrameView.html)`, `[DiagramLegendShape](symbols/shapes/DiagramLegendShape.html)`, `[DiagramPresentationElement](symbols/DiagramPresentationElement.html)`, `[DiagramPropertiesShape](symbols/shapes/DiagramPropertiesShape.html)`, `[DiagramShape](symbols/shapes/DiagramShape.html)`, `[DurationConstraintView](symbols/paths/DurationConstraintView.html)`, `[ElementImportView](symbols/paths/ElementImportView.html)`, `com.nomagic.magicdraw.uml.symbols.shapes.EmbeddedImageShapeView`, `[EnumerationView](symbols/shapes/EnumerationView.html)`, `[ExceptionHandlerView](symbols/paths/ExceptionHandlerView.html)`, `[ExpansionNodeView](symbols/shapes/ExpansionNodeView.html)`, `[ExpansionRegionView](symbols/shapes/ExpansionRegionView.html)`, `[ExtendView](symbols/paths/ExtendView.html)`, `[ExtensionView](symbols/paths/ExtensionView.html)`, `[FlowConnectorView](symbols/shapes/FlowConnectorView.html)`, `[FoundMessageView](symbols/paths/FoundMessageView.html)`, `com.nomagic.magicdraw.uml.symbols.shapes.FragmentView`, `com.nomagic.magicdraw.uml.symbols.shapes.FrameView`, `[GeneralizationSetView](symbols/shapes/GeneralizationSetView.html)`, `[GeneralizationView](symbols/paths/GeneralizationView.html)`, `[GenericView](symbols/shapes/GenericView.html)`, `com.dassault_systemes.modeler.magic.kerml.diagram.HeaderShape`, `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`, `[ImageShapeView](symbols/shapes/ImageShapeView.html)`, `[IncludeView](symbols/paths/IncludeView.html)`, `[InformationFlowView](symbols/paths/InformationFlowView.html)`, `[InformationItemView](symbols/shapes/InformationItemView.html)`, `[InstanceSpecificationView](symbols/shapes/InstanceSpecificationView.html)`, `[InteractionUseOverviewView](symbols/shapes/InteractionUseOverviewView.html)`, `[InteractionUseView](symbols/shapes/InteractionUseView.html)`, `[InterfaceRealizationView](symbols/paths/InterfaceRealizationView.html)`, `[InterfaceView](symbols/shapes/InterfaceView.html)`, `[InterruptibleActivityRegionView](symbols/shapes/InterruptibleActivityRegionView.html)`, `[LifeLineLineView](symbols/shapes/LifeLineLineView.html)`, `[LifelineView](symbols/shapes/LifelineView.html)`, `[LinkAttributeView](symbols/paths/LinkAttributeView.html)`, `[LinkView](symbols/paths/LinkView.html)`, `com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView`, `com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView`, `com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype`, `[LoopNodeView](symbols/shapes/LoopNodeView.html)`, `com.nomagic.magicdraw.uml.symbols.paths.LostFoundMessageView`, `[LostMessageView](symbols/paths/LostMessageView.html)`, `com.nomagic.magicdraw.uml.MDElementImpl`, `[MessageView](symbols/shapes/MessageView.html)`, `[NNaryAssociationView](symbols/shapes/NNaryAssociationView.html)`, `[NodeInstanceSpecificationView](symbols/shapes/NodeInstanceSpecificationView.html)`, `[NodeView](symbols/shapes/NodeView.html)`, `[NoteAnchorView](symbols/paths/NoteAnchorView.html)`, `[NoteView](symbols/shapes/NoteView.html)`, `[ObjectFlowView](symbols/paths/ObjectFlowView.html)`, `[ObjectNodeView](symbols/shapes/ObjectNodeView.html)`, `[OpaqueActionView](symbols/shapes/OpaqueActionView.html)`, `[PackageImportView](symbols/paths/PackageImportView.html)`, `[PackageMergeView](symbols/paths/PackageMergeView.html)`, `[PackageShape](../../../dassault_systemes/modeler/magic/sysml/diagram/PackageShape.html)`, `[PackageView](symbols/shapes/PackageView.html)`, `[PartView](symbols/shapes/PartView.html)`, `[PathConnector](symbols/paths/PathConnector.html)`, `[PathElement](symbols/paths/PathElement.html)`, `com.nomagic.magicdraw.uml.symbols.shapes.PathToSelfShape`, `[PinView](symbols/shapes/PinView.html)`, `[PortView](symbols/shapes/PortView.html)`, `[PresentationElement](symbols/PresentationElement.html)`, `[PrimitiveTypeView](symbols/shapes/PrimitiveTypeView.html)`, `[ProfileApplicationView](symbols/paths/ProfileApplicationView.html)`, `[Project](../core/Project.html)`, `[ProjectOptions](../core/options/ProjectOptions.html)`, `[PseudoNodeView](symbols/shapes/PseudoNodeView.html)`, `[PseudoStateView](symbols/shapes/PseudoStateView.html)`, `[RealizationView](symbols/paths/RealizationView.html)`, `[RectangularShape](symbols/shapes/RectangularShape.html)`, `[RoleBindingView](symbols/paths/RoleBindingView.html)`, `[SeparatorView](symbols/shapes/SeparatorView.html)`, `com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView`, `[SeqMessageView](symbols/paths/SeqMessageView.html)`, `[SeqSelfMessageView](symbols/paths/SeqSelfMessageView.html)`, `[SequenceLifelineView](symbols/shapes/SequenceLifelineView.html)`, `[SequenceNodeView](symbols/shapes/SequenceNodeView.html)`, `[ShapeElement](symbols/shapes/ShapeElement.html)`, `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`, `[SignalActionView](symbols/shapes/SignalActionView.html)`, `[SignalView](symbols/shapes/SignalView.html)`, `[StateInvariantView](symbols/shapes/StateInvariantView.html)`, `[StateView](symbols/shapes/StateView.html)`, `[StereotypeView](symbols/shapes/StereotypeView.html)`, `[StructuredActivityNodeView](symbols/shapes/StructuredActivityNodeView.html)`, `[SwimlaneCellView](symbols/shapes/SwimlaneCellView.html)`, `[SwimlaneView](symbols/shapes/SwimlaneView.html)`, `com.nomagic.magicdraw.uml.symbols.shapes.TableCellView`, `com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView`, `[TemplateBindingView](symbols/paths/TemplateBindingView.html)`, `[TextBoxView](symbols/shapes/TextBoxView.html)`, `com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView`, `[TimeConstraintView](symbols/paths/TimeConstraintView.html)`, `[TransitionToSelfView](symbols/shapes/TransitionToSelfView.html)`, `[TransitionView](symbols/paths/TransitionView.html)`, `[TreeView](symbols/shapes/TreeView.html)`, `com.nomagic.magicdraw.uml.symbols.shapes.TypedElementView`, `com.nomagic.magicdraw.uml.symbols.shapes.TypedElementWithLabels`, `[UsageView](symbols/paths/UsageView.html)`, `[UseCaseView](symbols/shapes/UseCaseView.html)`, `[VirtualRelationView](symbols/paths/VirtualRelationView.html)`

@OpenApipublic interfaceBaseElementextends [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html), [Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.AbstractVisitor))([AbstractVisitor](AbstractVisitor.html) visitor)`
Method accepts a visitor, and calls method visit < class name > (this) of visitor.
`void`
`[addPropertyChangeListener](#addPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Registers the listener to the element.
`void`
`[atInsert](#atInsert())()`
This method is called then this element is added into the project.
`default boolean`
`[canAdd](#canAdd(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](BaseElement.html) element)`
Checks if this element can add a given element.
`boolean`
`[canAdd](#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean))([BaseElement](BaseElement.html) element,
 boolean checkPermissions)`
Checks if this element can add a given element.
`boolean`
`[canAddChild](#canAddChild())()`
Checks if new elements can be added to this element
`boolean`
`[canAddInstance](#canAddInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](BaseElement.html) o)`
Checks if this object can add element of given type.
`boolean`
`[canBeDeleted](#canBeDeleted())()`
Checks if an element can be deleted from a project.
`boolean`
`[canChangeParent](#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) elements,
 [BaseElement](BaseElement.html) newParent)`
Returns true, if element can change parent.
`boolean`
`[canDeleteChild](#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](BaseElement.html) child)`
Checks if given element can be deleted from this element.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[clone](#clone())()`

`void`
`[dispose](#dispose())()`
This method is called when an element is removed from the project.
`void`
`[firePropertyChange](#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)`
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
`[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)`
`[getClassType](#getClassType())()`
Gets the type of the element class.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHumanName](#getHumanName())()`
Returns human representation of the element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHumanType](#getHumanType())()`
Returns human representation of the element type.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getID](#getID())()`
Returns the ID of the `Element`.
`[BaseElement](BaseElement.html)`
`[getObjectParent](#getObjectParent())()`
Returns the element parent.
`boolean`
`[isEditable](#isEditable())()`
Checks if an element can be edited.
`boolean`
`[isParentOf](#isParentOf(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](BaseElement.html) obj)`
Returns true, if current element is parent of given element.
`default boolean`
`[isSelfChangeable](#isSelfChangeable())()`
Checks if properties of an element can be changes (like name, for example).
`void`
`[removeAllPropertyChangeListeners](#removeAllPropertyChangeListeners())()`
Removes all property change listeners from this element.
`void`
`[removePropertyChangeListener](#removePropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Unregisters the given listener from the element.
`void`
`[setID](#setID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Sets the specified ID to the `Element`.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[sGetID](#sGetID())()`
Returns the actual ID of the `Element`.
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`

============ METHOD DETAIL ========== 
Method Details
getID
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getID()
Returns the ID of the `Element`.
 If the ID is `null`, new id for an element is generated.
 Element id is persistence and does not change during project save/load.
Returns:
the ID of the `Element`.
sGetID
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sGetID()
Returns the actual ID of the `Element`. May return null if ID was not generated
 or set for this element.
Returns:
the ID of the `Element`.
See Also:
[`getID()`](#getID())
setID
@OpenApivoid setID([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Sets the specified ID to the `Element`.
Parameters:
`id` - the id to be set.
getClassType
@OpenApi[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) getClassType()
Gets the type of the element class.
 Every element has its own ClassType.
 Usually this class type is class of element or class interface of an element.
 All types are registered in ClassTypes.
Returns:
the type of the element.
addPropertyChangeListener
@OpenApivoid addPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Registers the listener to the element. The given listener will get notifications about
 property changes in this element.
Parameters:
`listener` - the `PropertyChangeListener` to be added.
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
removePropertyChangeListener
@OpenApivoid removePropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Unregisters the given listener from the element. The given listener will not get any notifications about
 property changes in this element.
Parameters:
`listener` - the PropertyChangeListener to be removed.
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
removeAllPropertyChangeListeners
void removeAllPropertyChangeListeners()
Removes all property change listeners from this element.
firePropertyChange
@OpenApivoid firePropertyChange([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new values are equal or null.
Parameters:
`propertyName` - the programmatic name of the property that was changed.
`oldValue` - the old value of the property
`newValue` - the new value of the property
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
atInsert
void atInsert()
This method is called then this element is added into the project.
dispose
@OpenApivoid dispose()
This method is called when an element is removed from the project.
accept
@OpenApivoid accept([AbstractVisitor](AbstractVisitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method accepts a visitor, and calls method visit < class name > (this) of visitor.
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
getHumanName
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHumanName()
Returns human representation of the element. Usually human name is constructed from element class type
 and name.
Returns:
the human name of the element.
getHumanType
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHumanType()
Returns human representation of the element type. Contains only element type without element name.
Returns:
the human type of the element.
canAdd
@OpenApidefault boolean canAdd([BaseElement](BaseElement.html) element)
Checks if this element can add a given element.
Parameters:
`element` - the given element.
Returns:
true if this element can add a given element.
See Also:
[`canAdd(BaseElement, boolean)`](#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean))
canAdd
@OpenApiboolean canAdd([BaseElement](BaseElement.html) element,
 boolean checkPermissions)
Checks if this element can add a given element.
 

 Following rules must be true to have result true: 

 1.if checkTeamworkLock == true, this element must be locked for edit. 

 2.element can add given element as instance (class types are checked). 

 3.element can add given element as child (a given element is not a parent of current element etc.).
Parameters:
`element` - the element to add.
`checkPermissions` - check or not permissions.
Returns:
true if an element can add the given element as a child.
canDeleteChild
boolean canDeleteChild([BaseElement](BaseElement.html) child)
Checks if given element can be deleted from this element.
 Following rules must be true to have result true:
 1.this element must be editable.
 2.project must be editable.
 3.the type of given child must be valid for teamwork lock for edit operation
 (for example, class, package etc., not Attribute).
Parameters:
`child` - a given child
Returns:
true, if the given element can be deleted from the current element.
canBeDeleted
@OpenApiboolean canBeDeleted()
Checks if an element can be deleted from a project.
 Element cannot be deleted if it is not isEditable(),
 parent is not set, or parent does not allow to remove this element.
Returns:
true, if an element can be deleted from a project.
See Also:
[`isEditable()`](#isEditable())
canAddInstance
boolean canAddInstance([BaseElement](BaseElement.html) o)
Checks if this object can add element of given type.
 Current implementation returns false.
Returns:
true if this object can elements of a given type.
isSelfChangeable
@OpenApidefault boolean isSelfChangeable()
Checks if properties of an element can be changes (like name, for example).
 Element can be [`isEditable()`](#isEditable()), but not @isSelfChangeable.
 It means that element can be deleted, for example, but element's owner or properties cannot be changed.
Returns:
true, if an element can be changed
See Also:
[`isEditable()`](#isEditable())
isEditable
@OpenApiboolean isEditable()
Checks if an element can be edited.
Returns:
true, if an element can be edited.
canAddChild
@OpenApiboolean canAddChild()
Checks if new elements can be added to this element
Returns:
true, if new sub elements can be added.
getObjectParent
@OpenApi
@CheckForNull[BaseElement](BaseElement.html) getObjectParent()
Returns the element parent.
 This implementation returns null. Should be overridden in subclasses.
Returns:
the parent of the element.
isParentOf
boolean isParentOf([BaseElement](BaseElement.html) obj)
Returns true, if current element is parent of given element.
 Return false in this implementation.
Parameters:
`obj` - the given element(possible child).
Returns:
true if obj is the parent of this object.
canChangeParent
boolean canChangeParent([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) elements,
 [BaseElement](BaseElement.html) newParent)
Returns true, if element can change parent.
Parameters:
`elements` - collection of the elements, whose will change the parent together with this.
`newParent` - new parent object.
Returns:
true if an element can change parent.
clone
[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) clone()
 throws [CloneNotSupportedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CloneNotSupportedException.html)
Throws:
`[CloneNotSupportedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CloneNotSupportedException.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Interface BaseElement">Interface BaseElement</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../uml2/ext/magicdraw/classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecification</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNode</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a></code>, <code><a href="../../uml2/ext/magicdraw/mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEvent</a></code>, <code><a href="../../uml2/ext/magicdraw/deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecification</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BooleanTaggedValue</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNode</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a></code>, <code><a href="../../uml2/ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a></code>, <code><a href="../../uml2/ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></code>, <code><a href="../../uml2/ext/magicdraw/deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a></code>, <code><a href="../../uml2/ext/magicdraw/components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a></code>, <code><a href="../../uml2/ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></code>, <code><a href="../../uml2/ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a></code>, <code><a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a></code>, <code><a href="../../uml2/ext/magicdraw/compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a></code>, <code><a href="../../uml2/ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragment</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Continuation</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlNode</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNode</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a></code>, <code><a href="../../uml2/ext/magicdraw/deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeployedArtifact</a></code>, <code><a href="../../uml2/ext/magicdraw/deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a></code>, <code><a href="../../uml2/ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a></code>, <code><a href="../../uml2/ext/magicdraw/deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a></code>, <code><a href="../../uml2/ext/magicdraw/deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/ElementTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementTaggedValue</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a></code>, <code><a href="../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a></code>, <code><a href="../../uml2/ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionOccurrenceSpecification</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionSpecification</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNode</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a></code>, <code><a href="../../uml2/ext/magicdraw/mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a></code>, <code><a href="../../uml2/ext/magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></code>, <code><a href="../../uml2/ext/magicdraw/mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></code>, <code><a href="../../uml2/ext/magicdraw/mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPoint</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FinalNode</a></code>, <code><a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNode</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNode</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">GeneralOrdering</a></code>, <code><a href="../../uml2/ext/magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a></code>, <code><a href="../../uml2/ext/magicdraw/mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Include</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNode</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">IntegerTaggedValue</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBoolean</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralInteger</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNull</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralReal</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralSpecification</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralString</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNatural</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code>, <code><a href="../../uml2/ext/magicdraw/deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Manifestation</a></code>, <code><a href="MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">MessageEvent</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecification</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../uml2/ext/magicdraw/base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code><a href="../../uml2/ext/magicdraw/deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Observation</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecification</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageMerge</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a></code>, <code><a href="../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a></code>, <code><a href="../../uml2/ext/magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></code>, <code><a href="../../uml2/ext/magicdraw/mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplication</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code>, <code><a href="../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolConformance</a></code>, <code><a href="../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></code>, <code><a href="../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></code>, <code><a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/RealTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RealTaggedValue</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></code>, <code><a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a></code>, <code><a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code>, <code><a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a></code>, <code><a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></code>, <code><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/StringTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StringTaggedValue</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code>, <code><a href="../../uml2/ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a></code>, <code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEvent</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a></code>, <code><a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></code>, <code><a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Usage</a></code>, <code><a href="../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a></code>, <code><a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></code>, <code><a href="../../uml2/ext/magicdraw/activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">VariableAction</a></code>, <code><a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteLinkAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a></code>, <code><a href="../../uml2/ext/magicdraw/actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractImageShapeView</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractSeparatorView</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabelsInside</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView</code>, <code><a href="symbols/shapes/ActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActionView</a></code>, <code><a href="symbols/shapes/ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.ActivityGroupView</code>, <code><a href="symbols/shapes/ActorView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActorView</a></code>, <code><a href="symbols/shapes/ArtifactView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ArtifactView</a></code>, <code><a href="symbols/paths/AssociationClassView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">AssociationClassView</a></code>, <code><a href="symbols/paths/AssociationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">AssociationView</a></code>, <code><a href="symbols/shapes/BarView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">BarView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.paths.BaseFlowView</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineView</code>, <code>com.nomagic.magicdraw.uml.symbols.paths.BaseRealizationView</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape</code>, <code><a href="symbols/shapes/CallBehaviorActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CallBehaviorActionView</a></code>, <code><a href="symbols/shapes/CallOperationActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CallOperationActionView</a></code>, <code><a href="symbols/shapes/ClassifierView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ClassifierView</a></code>, <code><a href="symbols/shapes/ClassView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ClassView</a></code>, <code><a href="symbols/shapes/CollaborationUseView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CollaborationUseView</a></code>, <code><a href="symbols/shapes/CollaborationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CollaborationView</a></code>, <code><a href="symbols/shapes/CombinedFragmentView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CombinedFragmentView</a></code>, <code><a href="symbols/shapes/CommentView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CommentView</a></code>, <code><a href="symbols/paths/CommunicationPathView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">CommunicationPathView</a></code>, <code><a href="symbols/shapes/ComponentView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ComponentView</a></code>, <code><a href="symbols/shapes/ConditionalNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ConditionalNodeView</a></code>, <code><a href="symbols/paths/ConnectorToSelfView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ConnectorToSelfView</a></code>, <code><a href="symbols/paths/ConnectorView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ConnectorView</a></code>, <code><a href="symbols/paths/ConstraintLinkView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ConstraintLinkView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code>, <code><a href="symbols/paths/ContainmentLinkView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ContainmentLinkView</a></code>, <code><a href="symbols/shapes/ContentShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ContentShape</a></code>, <code><a href="symbols/paths/ControlFlowView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ControlFlowView</a></code>, <code><a href="symbols/shapes/DataTypeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DataTypeView</a></code>, <code><a href="symbols/shapes/DecisionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DecisionView</a></code>, <code><a href="symbols/paths/DependencyView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">DependencyView</a></code>, <code><a href="symbols/paths/DeploymentView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">DeploymentView</a></code>, <code><a href="symbols/shapes/DiagramFrameView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramFrameView</a></code>, <code><a href="symbols/shapes/DiagramLegendShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramLegendShape</a></code>, <code><a href="symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></code>, <code><a href="symbols/shapes/DiagramPropertiesShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramPropertiesShape</a></code>, <code><a href="symbols/shapes/DiagramShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramShape</a></code>, <code><a href="symbols/paths/DurationConstraintView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">DurationConstraintView</a></code>, <code><a href="symbols/paths/ElementImportView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ElementImportView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.EmbeddedImageShapeView</code>, <code><a href="symbols/shapes/EnumerationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">EnumerationView</a></code>, <code><a href="symbols/paths/ExceptionHandlerView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ExceptionHandlerView</a></code>, <code><a href="symbols/shapes/ExpansionNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ExpansionNodeView</a></code>, <code><a href="symbols/shapes/ExpansionRegionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ExpansionRegionView</a></code>, <code><a href="symbols/paths/ExtendView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ExtendView</a></code>, <code><a href="symbols/paths/ExtensionView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ExtensionView</a></code>, <code><a href="symbols/shapes/FlowConnectorView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">FlowConnectorView</a></code>, <code><a href="symbols/paths/FoundMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">FoundMessageView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.FragmentView</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.FrameView</code>, <code><a href="symbols/shapes/GeneralizationSetView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">GeneralizationSetView</a></code>, <code><a href="symbols/paths/GeneralizationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">GeneralizationView</a></code>, <code><a href="symbols/shapes/GenericView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">GenericView</a></code>, <code>com.dassault_systemes.modeler.magic.kerml.diagram.HeaderShape</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code>, <code><a href="symbols/shapes/ImageShapeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ImageShapeView</a></code>, <code><a href="symbols/paths/IncludeView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">IncludeView</a></code>, <code><a href="symbols/paths/InformationFlowView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">InformationFlowView</a></code>, <code><a href="symbols/shapes/InformationItemView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InformationItemView</a></code>, <code><a href="symbols/shapes/InstanceSpecificationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InstanceSpecificationView</a></code>, <code><a href="symbols/shapes/InteractionUseOverviewView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InteractionUseOverviewView</a></code>, <code><a href="symbols/shapes/InteractionUseView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InteractionUseView</a></code>, <code><a href="symbols/paths/InterfaceRealizationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">InterfaceRealizationView</a></code>, <code><a href="symbols/shapes/InterfaceView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InterfaceView</a></code>, <code><a href="symbols/shapes/InterruptibleActivityRegionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InterruptibleActivityRegionView</a></code>, <code><a href="symbols/shapes/LifeLineLineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LifeLineLineView</a></code>, <code><a href="symbols/shapes/LifelineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LifelineView</a></code>, <code><a href="symbols/paths/LinkAttributeView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">LinkAttributeView</a></code>, <code><a href="symbols/paths/LinkView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">LinkView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView</code>, <code>com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView</code>, <code>com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype</code>, <code><a href="symbols/shapes/LoopNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LoopNodeView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.paths.LostFoundMessageView</code>, <code><a href="symbols/paths/LostMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">LostMessageView</a></code>, <code>com.nomagic.magicdraw.uml.MDElementImpl</code>, <code><a href="symbols/shapes/MessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">MessageView</a></code>, <code><a href="symbols/shapes/NNaryAssociationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">NNaryAssociationView</a></code>, <code><a href="symbols/shapes/NodeInstanceSpecificationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">NodeInstanceSpecificationView</a></code>, <code><a href="symbols/shapes/NodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">NodeView</a></code>, <code><a href="symbols/paths/NoteAnchorView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">NoteAnchorView</a></code>, <code><a href="symbols/shapes/NoteView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">NoteView</a></code>, <code><a href="symbols/paths/ObjectFlowView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ObjectFlowView</a></code>, <code><a href="symbols/shapes/ObjectNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ObjectNodeView</a></code>, <code><a href="symbols/shapes/OpaqueActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">OpaqueActionView</a></code>, <code><a href="symbols/paths/PackageImportView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PackageImportView</a></code>, <code><a href="symbols/paths/PackageMergeView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PackageMergeView</a></code>, <code><a href="../../../dassault_systemes/modeler/magic/sysml/diagram/PackageShape.html" title="class in com.dassault_systemes.modeler.magic.sysml.diagram">PackageShape</a></code>, <code><a href="symbols/shapes/PackageView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PackageView</a></code>, <code><a href="symbols/shapes/PartView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PartView</a></code>, <code><a href="symbols/paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code>, <code><a href="symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.PathToSelfShape</code>, <code><a href="symbols/shapes/PinView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PinView</a></code>, <code><a href="symbols/shapes/PortView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PortView</a></code>, <code><a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code>, <code><a href="symbols/shapes/PrimitiveTypeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PrimitiveTypeView</a></code>, <code><a href="symbols/paths/ProfileApplicationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ProfileApplicationView</a></code>, <code><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code>, <code><a href="../core/options/ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a></code>, <code><a href="symbols/shapes/PseudoNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PseudoNodeView</a></code>, <code><a href="symbols/shapes/PseudoStateView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PseudoStateView</a></code>, <code><a href="symbols/paths/RealizationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">RealizationView</a></code>, <code><a href="symbols/shapes/RectangularShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">RectangularShape</a></code>, <code><a href="symbols/paths/RoleBindingView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">RoleBindingView</a></code>, <code><a href="symbols/shapes/SeparatorView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SeparatorView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView</code>, <code><a href="symbols/paths/SeqMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">SeqMessageView</a></code>, <code><a href="symbols/paths/SeqSelfMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">SeqSelfMessageView</a></code>, <code><a href="symbols/shapes/SequenceLifelineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SequenceLifelineView</a></code>, <code><a href="symbols/shapes/SequenceNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SequenceNodeView</a></code>, <code><a href="symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</code>, <code><a href="symbols/shapes/SignalActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SignalActionView</a></code>, <code><a href="symbols/shapes/SignalView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SignalView</a></code>, <code><a href="symbols/shapes/StateInvariantView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StateInvariantView</a></code>, <code><a href="symbols/shapes/StateView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StateView</a></code>, <code><a href="symbols/shapes/StereotypeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StereotypeView</a></code>, <code><a href="symbols/shapes/StructuredActivityNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StructuredActivityNodeView</a></code>, <code><a href="symbols/shapes/SwimlaneCellView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SwimlaneCellView</a></code>, <code><a href="symbols/shapes/SwimlaneView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SwimlaneView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.TableCellView</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView</code>, <code><a href="symbols/paths/TemplateBindingView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">TemplateBindingView</a></code>, <code><a href="symbols/shapes/TextBoxView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TextBoxView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView</code>, <code><a href="symbols/paths/TimeConstraintView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">TimeConstraintView</a></code>, <code><a href="symbols/shapes/TransitionToSelfView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TransitionToSelfView</a></code>, <code><a href="symbols/paths/TransitionView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">TransitionView</a></code>, <code><a href="symbols/shapes/TreeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TreeView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.TypedElementView</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.TypedElementWithLabels</code>, <code><a href="symbols/paths/UsageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">UsageView</a></code>, <code><a href="symbols/shapes/UseCaseView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">UseCaseView</a></code>, <code><a href="symbols/paths/VirtualRelationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">VirtualRelationView</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">BaseElement</span><span class="extends-implements">
extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a><wbr/>(<a href="AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml">AbstractVisitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method accepts a visitor, and calls method visit &lt; class name &gt; (this) of visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Registers the listener to the element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#atInsert()">atInsert</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method is called then this element is added into the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Checks if this element can add a given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean checkPermissions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if this element can add a given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canAddChild()">canAddChild</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if new elements can be added to this element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if this object can add element of given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canBeDeleted()">canBeDeleted</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if an element can be deleted from a project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> elements,
 <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> newParent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns true, if element can change parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">canDeleteChild</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if given element can be deleted from this element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method is called when an element is removed from the project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the type of the element class.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getHumanName()">getHumanName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns human representation of the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getHumanType()">getHumanType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns human representation of the element type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the ID of the <code>Element</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getObjectParent()">getObjectParent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the element parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isEditable()">isEditable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if an element can be edited.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns true, if current element is parent of given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isSelfChangeable()">isSelfChangeable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Checks if properties of an element can be changes (like name, for example).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeAllPropertyChangeListeners()">removeAllPropertyChangeListeners</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes all property change listeners from this element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Unregisters the given listener from the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setID(java.lang.String)">setID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the specified ID to the <code>Element</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#sGetID()">sGetID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the actual ID of the <code>Element</code>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
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
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<div class="block">Returns the ID of the <code>Element</code>.
 If the ID is <code>null</code>, new id for an element is generated.
 Element id is persistence and does not change during project save/load.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ID of the <code>Element</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sGetID()">
<h3>sGetID</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">sGetID</span>()</div>
<div class="block">Returns the actual ID of the <code>Element</code>. May return null if ID was not generated
 or set for this element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ID of the <code>Element</code>.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getID()"><code>getID()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setID(java.lang.String)">
<h3>setID</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">setID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Sets the specified ID to the <code>Element</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the id to be set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassType()">
<h3>getClassType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a></span> <span class="element-name">getClassType</span>()</div>
<div class="block">Gets the type of the element class.
 Every element has its own ClassType.
 Usually this class type is class of element or class interface of an element.
 All types are registered in ClassTypes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the type of the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>addPropertyChangeListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">addPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Registers the listener to the element. The given listener will get notifications about
 property changes in this element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the <code>PropertyChangeListener</code> to be added.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>removePropertyChangeListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">removePropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Unregisters the given listener from the element. The given listener will not get any notifications about
 property changes in this element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the PropertyChangeListener to be removed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAllPropertyChangeListeners()">
<h3>removeAllPropertyChangeListeners</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeAllPropertyChangeListeners</span>()</div>
<div class="block">Removes all property change listeners from this element.</div>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new values are equal or null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyName</code> - the programmatic name of the property that was changed.</dd>
<dd><code>oldValue</code> - the old value of the property</dd>
<dd><code>newValue</code> - the new value of the property</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="atInsert()">
<h3>atInsert</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">atInsert</span>()</div>
<div class="block">This method is called then this element is added into the project.</div>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">This method is called when an element is removed from the project.</div>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.AbstractVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml">AbstractVisitor</a> visitor)</span>
     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method accepts a visitor, and calls method visit &lt; class name &gt; (this) of visitor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHumanName()">
<h3>getHumanName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHumanName</span>()</div>
<div class="block">Returns human representation of the element. Usually human name is constructed from element class type
 and name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the human name of the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHumanType()">
<h3>getHumanType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHumanType</span>()</div>
<div class="block">Returns human representation of the element type. Contains only element type without element name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the human type of the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAdd(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canAdd</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">canAdd</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Checks if this element can add a given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element.</dd>
<dt>Returns:</dt>
<dd>true if this element can add a given element.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)"><code>canAdd(BaseElement, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">
<h3>canAdd</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">canAdd</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean checkPermissions)</span></div>
<div class="block">Checks if this element can add a given element.
 <br/>
 Following rules must be true to have result true:<br/>
 1.if checkTeamworkLock == true, this element must be locked for edit.<br/>
 2.element can add given element as instance (class types are checked).<br/>
 3.element can add given element as child (a given element is not a parent of current element etc.).<br/></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to add.</dd>
<dd><code>checkPermissions</code> - check or not permissions.</dd>
<dt>Returns:</dt>
<dd>true if an element can add the given element as a child.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canDeleteChild</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canDeleteChild</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> child)</span></div>
<div class="block">Checks if given element can be deleted from this element.
 Following rules must be true to have result true:
 1.this element must be editable.
 2.project must be editable.
 3.the type of given child must be valid for teamwork lock for edit operation
 (for example, class, package etc., not Attribute).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>child</code> - a given child</dd>
<dt>Returns:</dt>
<dd>true, if the given element can be deleted from the current element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeDeleted()">
<h3>canBeDeleted</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">canBeDeleted</span>()</div>
<div class="block">Checks if an element can be deleted from a project.
 Element cannot be deleted if it is not isEditable(),
 parent is not set, or parent does not allow to remove this element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if an element can be deleted from a project.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isEditable()"><code>isEditable()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canAddInstance</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canAddInstance</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> o)</span></div>
<div class="block">Checks if this object can add element of given type.
 Current implementation returns false.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this object can elements of a given type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSelfChangeable()">
<h3>isSelfChangeable</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isSelfChangeable</span>()</div>
<div class="block">Checks if properties of an element can be changes (like name, for example).
 Element can be <a href="#isEditable()"><code>isEditable()</code></a>, but not @isSelfChangeable.
 It means that element can be deleted, for example, but element's owner or properties cannot be changed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if an element can be changed</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isEditable()"><code>isEditable()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEditable()">
<h3>isEditable</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isEditable</span>()</div>
<div class="block">Checks if an element can be edited.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if an element can be edited.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddChild()">
<h3>canAddChild</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">canAddChild</span>()</div>
<div class="block">Checks if new elements can be added to this element</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if new sub elements can be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectParent()">
<h3>getObjectParent</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="return-type"><a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getObjectParent</span>()</div>
<div class="block">Returns the element parent.
 This implementation returns null. Should be overridden in subclasses.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the parent of the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParentOf(com.nomagic.magicdraw.uml.BaseElement)">
<h3>isParentOf</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isParentOf</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</span></div>
<div class="block">Returns true, if current element is parent of given element.
 Return false in this implementation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - the given element(possible child).</dd>
<dt>Returns:</dt>
<dd>true if obj is the parent of this object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">
<h3>canChangeParent</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canChangeParent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> elements,
 <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> newParent)</span></div>
<div class="block">Returns true, if element can change parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - collection of the elements, whose will change the parent together with this.</dd>
<dd><code>newParent</code> - new parent object.</dd>
<dt>Returns:</dt>
<dd>true if an element can change parent.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">clone</span>()
      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CloneNotSupportedException.html" title="class or interface in java.lang">CloneNotSupportedException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/CloneNotSupportedException.html" title="class or interface in java.lang">CloneNotSupportedException</a></code></dd>
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
