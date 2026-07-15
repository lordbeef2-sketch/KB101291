# JAVA OPENAPI: UMLFactory (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/magicdraw/metadata/UMLFactory.html
- source_path: `com/nomagic/uml2/ext/magicdraw/metadata/UMLFactory.html`
- source_sha256: `18ded8d200597cd91894a49effa820ee92ecd65b7cb33ac549e4bc233382847a`
- captured_utc: `2026-07-14T16:53:05.138551+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.metadata](package-summary.html)

## Interface UMLFactory

All Superinterfaces:
`org.eclipse.emf.ecore.EFactory`, `org.eclipse.emf.ecore.EModelElement`, `org.eclipse.emf.ecore.EObject`, `org.eclipse.emf.common.notify.Notifier`

public interfaceUMLFactoryextends org.eclipse.emf.ecore.EFactory

begin-user-doc 
 The **Factory** for the model.
 It provides a create method for each non-abstract class of the model.
 end-user-doc

See Also:
[`UMLPackage`](UMLPackage.html)
Generated:

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [UMLFactory](UMLFactory.html)`
`[eINSTANCE](#eINSTANCE)`
The singleton instance of the factory.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDeprecated Methods
Modifier and Type
Method
Description
`[Abstraction](../classes/mddependencies/Abstraction.html)`
`[createAbstraction](#createAbstraction())()`
Returns a new object of class '*Abstraction*'.
`[AcceptCallAction](../actions/mdcompleteactions/AcceptCallAction.html)`
`[createAcceptCallAction](#createAcceptCallAction())()`
Returns a new object of class '*Accept Call Action*'.
`[AcceptEventAction](../actions/mdcompleteactions/AcceptEventAction.html)`
`[createAcceptEventAction](#createAcceptEventAction())()`
Returns a new object of class '*Accept Event Action*'.
`[ActionExecutionSpecification](../interactions/mdbasicinteractions/ActionExecutionSpecification.html)`
`[createActionExecutionSpecification](#createActionExecutionSpecification())()`
Returns a new object of class '*Action Execution Specification*'.
`[ActionInputPin](../actions/mdstructuredactions/ActionInputPin.html)`
`[createActionInputPin](#createActionInputPin())()`
Returns a new object of class '*Action Input Pin*'.
`[Activity](../activities/mdfundamentalactivities/Activity.html)`
`[createActivity](#createActivity())()`
Returns a new object of class '*Activity*'.
`[ActivityFinalNode](../activities/mdbasicactivities/ActivityFinalNode.html)`
`[createActivityFinalNode](#createActivityFinalNode())()`
Returns a new object of class '*Activity Final Node*'.
`[ActivityParameterNode](../activities/mdbasicactivities/ActivityParameterNode.html)`
`[createActivityParameterNode](#createActivityParameterNode())()`
Returns a new object of class '*Activity Parameter Node*'.
`[ActivityPartition](../activities/mdintermediateactivities/ActivityPartition.html)`
`[createActivityPartition](#createActivityPartition())()`
Returns a new object of class '*Activity Partition*'.
`[Actor](../mdusecases/Actor.html)`
`[createActor](#createActor())()`
Returns a new object of class '*Actor*'.
`[AddStructuralFeatureValueAction](../actions/mdintermediateactions/AddStructuralFeatureValueAction.html)`
`[createAddStructuralFeatureValueAction](#createAddStructuralFeatureValueAction())()`
Returns a new object of class '*Add Structural Feature Value Action*'.
`[AddVariableValueAction](../actions/mdstructuredactions/AddVariableValueAction.html)`
`[createAddVariableValueAction](#createAddVariableValueAction())()`
Returns a new object of class '*Add Variable Value Action*'.
`[AnyReceiveEvent](../commonbehaviors/mdcommunications/AnyReceiveEvent.html)`
`[createAnyReceiveEvent](#createAnyReceiveEvent())()`
Returns a new object of class '*Any Receive Event*'.
`[Artifact](../deployments/mdartifacts/Artifact.html)`
`[createArtifact](#createArtifact())()`
Returns a new object of class '*Artifact*'.
`[Association](../classes/mdkernel/Association.html)`
`[createAssociation](#createAssociation())()`
Returns a new object of class '*Association*'.
`[AssociationClass](../classes/mdassociationclasses/AssociationClass.html)`
`[createAssociationClass](#createAssociationClass())()`
Returns a new object of class '*Association Class*'.
`[BehaviorExecutionSpecification](../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html)`
`[createBehaviorExecutionSpecification](#createBehaviorExecutionSpecification())()`
Returns a new object of class '*Behavior Execution Specification*'.
`[BooleanTaggedValue](../classes/mdkernel/BooleanTaggedValue.html)`
`[createBooleanTaggedValue](#createBooleanTaggedValue())()`
Returns a new object of class '*Boolean Tagged Value*'.
`[BroadcastSignalAction](../actions/mdintermediateactions/BroadcastSignalAction.html)`
`[createBroadcastSignalAction](#createBroadcastSignalAction())()`
Returns a new object of class '*Broadcast Signal Action*'.
`[CallBehaviorAction](../actions/mdbasicactions/CallBehaviorAction.html)`
`[createCallBehaviorAction](#createCallBehaviorAction())()`
Returns a new object of class '*Call Behavior Action*'.
`[CallEvent](../commonbehaviors/mdcommunications/CallEvent.html)`
`[createCallEvent](#createCallEvent())()`
Returns a new object of class '*Call Event*'.
`[CallOperationAction](../actions/mdbasicactions/CallOperationAction.html)`
`[createCallOperationAction](#createCallOperationAction())()`
Returns a new object of class '*Call Operation Action*'.
`[CentralBufferNode](../activities/mdintermediateactivities/CentralBufferNode.html)`
`[createCentralBufferNode](#createCentralBufferNode())()`
Returns a new object of class '*Central Buffer Node*'.
`[ChangeEvent](../commonbehaviors/mdcommunications/ChangeEvent.html)`
`[createChangeEvent](#createChangeEvent())()`
Returns a new object of class '*Change Event*'.
`[Class](../classes/mdkernel/Class.html)`
`[createClass](#createClass())()`
Returns a new object of class '*Class*'.
`[ClassifierTemplateParameter](../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html)`
`[createClassifierTemplateParameter](#createClassifierTemplateParameter())()`
Returns a new object of class '*Classifier Template Parameter*'.
`[Clause](../activities/mdstructuredactivities/Clause.html)`
`[createClause](#createClause())()`
Returns a new object of class '*Clause*'.
`[ClearAssociationAction](../actions/mdintermediateactions/ClearAssociationAction.html)`
`[createClearAssociationAction](#createClearAssociationAction())()`
Returns a new object of class '*Clear Association Action*'.
`[ClearStructuralFeatureAction](../actions/mdintermediateactions/ClearStructuralFeatureAction.html)`
`[createClearStructuralFeatureAction](#createClearStructuralFeatureAction())()`
Returns a new object of class '*Clear Structural Feature Action*'.
`[ClearVariableAction](../actions/mdstructuredactions/ClearVariableAction.html)`
`[createClearVariableAction](#createClearVariableAction())()`
Returns a new object of class '*Clear Variable Action*'.
`[Collaboration](../compositestructures/mdcollaborations/Collaboration.html)`
`[createCollaboration](#createCollaboration())()`
Returns a new object of class '*Collaboration*'.
`[CollaborationUse](../compositestructures/mdcollaborations/CollaborationUse.html)`
`[createCollaborationUse](#createCollaborationUse())()`
Returns a new object of class '*Collaboration Use*'.
`[CombinedFragment](../interactions/mdfragments/CombinedFragment.html)`
`[createCombinedFragment](#createCombinedFragment())()`
Returns a new object of class '*Combined Fragment*'.
`[Comment](../classes/mdkernel/Comment.html)`
`[createComment](#createComment())()`
Returns a new object of class '*Comment*'.
`[CommunicationPath](../deployments/mdnodes/CommunicationPath.html)`
`[createCommunicationPath](#createCommunicationPath())()`
Returns a new object of class '*Communication Path*'.
`[Component](../components/mdbasiccomponents/Component.html)`
`[createComponent](#createComponent())()`
Returns a new object of class '*Component*'.
`[ComponentRealization](../components/mdbasiccomponents/ComponentRealization.html)`
`[createComponentRealization](#createComponentRealization())()`
Returns a new object of class '*Component Realization*'.
`[ConditionalNode](../activities/mdstructuredactivities/ConditionalNode.html)`
`[createConditionalNode](#createConditionalNode())()`
Returns a new object of class '*Conditional Node*'.
`[ConnectableElementTemplateParameter](../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html)`
`[createConnectableElementTemplateParameter](#createConnectableElementTemplateParameter())()`
Returns a new object of class '*Connectable Element Template Parameter*'.
`[ConnectionPointReference](../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html)`
`[createConnectionPointReference](#createConnectionPointReference())()`
Returns a new object of class '*Connection Point Reference*'.
`[Connector](../compositestructures/mdinternalstructures/Connector.html)`
`[createConnector](#createConnector())()`
Returns a new object of class '*Connector*'.
`[ConnectorEnd](../compositestructures/mdinternalstructures/ConnectorEnd.html)`
`[createConnectorEnd](#createConnectorEnd())()`
Returns a new object of class '*Connector End*'.
`[ConsiderIgnoreFragment](../interactions/mdfragments/ConsiderIgnoreFragment.html)`
`[createConsiderIgnoreFragment](#createConsiderIgnoreFragment())()`
Returns a new object of class '*Consider Ignore Fragment*'.
`[Constraint](../classes/mdkernel/Constraint.html)`
`[createConstraint](#createConstraint())()`
Returns a new object of class '*Constraint*'.
`[Continuation](../interactions/mdfragments/Continuation.html)`
`[createContinuation](#createContinuation())()`
Returns a new object of class '*Continuation*'.
`[ControlFlow](../activities/mdbasicactivities/ControlFlow.html)`
`[createControlFlow](#createControlFlow())()`
Returns a new object of class '*Control Flow*'.
`[CreateLinkAction](../actions/mdintermediateactions/CreateLinkAction.html)`
`[createCreateLinkAction](#createCreateLinkAction())()`
Returns a new object of class '*Create Link Action*'.
`[CreateLinkObjectAction](../actions/mdcompleteactions/CreateLinkObjectAction.html)`
`[createCreateLinkObjectAction](#createCreateLinkObjectAction())()`
Returns a new object of class '*Create Link Object Action*'.
`[CreateObjectAction](../actions/mdintermediateactions/CreateObjectAction.html)`
`[createCreateObjectAction](#createCreateObjectAction())()`
Returns a new object of class '*Create Object Action*'.
`[DataStoreNode](../activities/mdcompleteactivities/DataStoreNode.html)`
`[createDataStoreNode](#createDataStoreNode())()`
Returns a new object of class '*Data Store Node*'.
`[DataType](../classes/mdkernel/DataType.html)`
`[createDataType](#createDataType())()`
Returns a new object of class '*Data Type*'.
`[DecisionNode](../activities/mdintermediateactivities/DecisionNode.html)`
`[createDecisionNode](#createDecisionNode())()`
Returns a new object of class '*Decision Node*'.
`[Dependency](../classes/mddependencies/Dependency.html)`
`[createDependency](#createDependency())()`
Returns a new object of class '*Dependency*'.
`[Deployment](../deployments/mdnodes/Deployment.html)`
`[createDeployment](#createDeployment())()`
Returns a new object of class '*Deployment*'.
`[DeploymentSpecification](../deployments/mdcomponentdeployments/DeploymentSpecification.html)`
`[createDeploymentSpecification](#createDeploymentSpecification())()`
Returns a new object of class '*Deployment Specification*'.
`[DestroyLinkAction](../actions/mdintermediateactions/DestroyLinkAction.html)`
`[createDestroyLinkAction](#createDestroyLinkAction())()`
Returns a new object of class '*Destroy Link Action*'.
`[DestroyObjectAction](../actions/mdintermediateactions/DestroyObjectAction.html)`
`[createDestroyObjectAction](#createDestroyObjectAction())()`
Returns a new object of class '*Destroy Object Action*'.
`[DestructionOccurrenceSpecification](../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html)`
`[createDestructionOccurrenceSpecification](#createDestructionOccurrenceSpecification())()`
Returns a new object of class '*Destruction Occurrence Specification*'.
`[Device](../deployments/mdnodes/Device.html)`
`[createDevice](#createDevice())()`
Returns a new object of class '*Device*'.
`[Diagram](../classes/mdkernel/Diagram.html)`
`[createDiagram](#createDiagram())()`
Returns a new object of class '*Diagram*'.
`[Duration](../commonbehaviors/mdsimpletime/Duration.html)`
`[createDuration](#createDuration())()`
Returns a new object of class '*Duration*'.
`[DurationConstraint](../commonbehaviors/mdsimpletime/DurationConstraint.html)`
`[createDurationConstraint](#createDurationConstraint())()`
Returns a new object of class '*Duration Constraint*'.
`[DurationInterval](../commonbehaviors/mdsimpletime/DurationInterval.html)`
`[createDurationInterval](#createDurationInterval())()`
Returns a new object of class '*Duration Interval*'.
`[DurationObservation](../commonbehaviors/mdsimpletime/DurationObservation.html)`
`[createDurationObservation](#createDurationObservation())()`
Returns a new object of class '*Duration Observation*'.
`[ElementImport](../classes/mdkernel/ElementImport.html)`
`[createElementImport](#createElementImport())()`
Returns a new object of class '*Element Import*'.
`[ElementTaggedValue](../classes/mdkernel/ElementTaggedValue.html)`
`[createElementTaggedValue](#createElementTaggedValue())()`
Returns a new object of class '*Element Tagged Value*'.
`[ElementValue](../classes/mdkernel/ElementValue.html)`
`[createElementValue](#createElementValue())()`
Returns a new object of class '*Element Value*'.
`[Enumeration](../classes/mdkernel/Enumeration.html)`
`[createEnumeration](#createEnumeration())()`
Returns a new object of class '*Enumeration*'.
`[EnumerationLiteral](../classes/mdkernel/EnumerationLiteral.html)`
`[createEnumerationLiteral](#createEnumerationLiteral())()`
Returns a new object of class '*Enumeration Literal*'.
`[ExceptionHandler](../activities/mdextrastructuredactivities/ExceptionHandler.html)`
`[createExceptionHandler](#createExceptionHandler())()`
Returns a new object of class '*Exception Handler*'.
`[ExecutionEnvironment](../deployments/mdnodes/ExecutionEnvironment.html)`
`[createExecutionEnvironment](#createExecutionEnvironment())()`
Returns a new object of class '*Execution Environment*'.
`[ExecutionOccurrenceSpecification](../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html)`
`[createExecutionOccurrenceSpecification](#createExecutionOccurrenceSpecification())()`
Returns a new object of class '*Execution Occurrence Specification*'.
`[ExpansionNode](../activities/mdextrastructuredactivities/ExpansionNode.html)`
`[createExpansionNode](#createExpansionNode())()`
Returns a new object of class '*Expansion Node*'.
`[ExpansionRegion](../activities/mdextrastructuredactivities/ExpansionRegion.html)`
`[createExpansionRegion](#createExpansionRegion())()`
Returns a new object of class '*Expansion Region*'.
`[Expression](../classes/mdkernel/Expression.html)`
`[createExpression](#createExpression())()`
Returns a new object of class '*Expression*'.
`[Extend](../mdusecases/Extend.html)`
`[createExtend](#createExtend())()`
Returns a new object of class '*Extend*'.
`[Extension](../mdprofiles/Extension.html)`
`[createExtension](#createExtension())()`
Returns a new object of class '*Extension*'.
`[ExtensionEnd](../mdprofiles/ExtensionEnd.html)`
`[createExtensionEnd](#createExtensionEnd())()`
Returns a new object of class '*Extension End*'.
`[ExtensionPoint](../mdusecases/ExtensionPoint.html)`
`[createExtensionPoint](#createExtensionPoint())()`
Returns a new object of class '*Extension Point*'.
`[FinalState](../statemachines/mdbehaviorstatemachines/FinalState.html)`
`[createFinalState](#createFinalState())()`
Returns a new object of class '*Final State*'.
`[FlowFinalNode](../activities/mdintermediateactivities/FlowFinalNode.html)`
`[createFlowFinalNode](#createFlowFinalNode())()`
Returns a new object of class '*Flow Final Node*'.
`[ForkNode](../activities/mdintermediateactivities/ForkNode.html)`
`[createForkNode](#createForkNode())()`
Returns a new object of class '*Fork Node*'.
`[FunctionBehavior](../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html)`
`[createFunctionBehavior](#createFunctionBehavior())()`
Returns a new object of class '*Function Behavior*'.
`[Gate](../interactions/mdfragments/Gate.html)`
`[createGate](#createGate())()`
Returns a new object of class '*Gate*'.
`[Generalization](../classes/mdkernel/Generalization.html)`
`[createGeneralization](#createGeneralization())()`
Returns a new object of class '*Generalization*'.
`[GeneralizationSet](../classes/mdpowertypes/GeneralizationSet.html)`
`[createGeneralizationSet](#createGeneralizationSet())()`
Returns a new object of class '*Generalization Set*'.
`[GeneralOrdering](../interactions/mdbasicinteractions/GeneralOrdering.html)`
`[createGeneralOrdering](#createGeneralOrdering())()`
Returns a new object of class '*General Ordering*'.
`[Image](../mdprofiles/Image.html)`
`[createImage](#createImage())()`
Returns a new object of class '*Image*'.
`[Include](../mdusecases/Include.html)`
`[createInclude](#createInclude())()`
Returns a new object of class '*Include*'.
`[InformationFlow](../auxiliaryconstructs/mdinformationflows/InformationFlow.html)`
`[createInformationFlow](#createInformationFlow())()`
Returns a new object of class '*Information Flow*'.
`[InformationItem](../auxiliaryconstructs/mdinformationflows/InformationItem.html)`
`[createInformationItem](#createInformationItem())()`
Returns a new object of class '*Information Item*'.
`[InitialNode](../activities/mdbasicactivities/InitialNode.html)`
`[createInitialNode](#createInitialNode())()`
Returns a new object of class '*Initial Node*'.
`[InputPin](../actions/mdbasicactions/InputPin.html)`
`[createInputPin](#createInputPin())()`
Returns a new object of class '*Input Pin*'.
`[InstanceSpecification](../classes/mdkernel/InstanceSpecification.html)`
`[createInstanceSpecification](#createInstanceSpecification())()`
Returns a new object of class '*Instance Specification*'.
`[InstanceValue](../classes/mdkernel/InstanceValue.html)`
`[createInstanceValue](#createInstanceValue())()`
Returns a new object of class '*Instance Value*'.
`[IntegerTaggedValue](../classes/mdkernel/IntegerTaggedValue.html)`
`[createIntegerTaggedValue](#createIntegerTaggedValue())()`
Returns a new object of class '*Integer Tagged Value*'.
`[Interaction](../interactions/mdbasicinteractions/Interaction.html)`
`[createInteraction](#createInteraction())()`
Returns a new object of class '*Interaction*'.
`[InteractionConstraint](../interactions/mdfragments/InteractionConstraint.html)`
`[createInteractionConstraint](#createInteractionConstraint())()`
Returns a new object of class '*Interaction Constraint*'.
`[InteractionOperand](../interactions/mdfragments/InteractionOperand.html)`
`[createInteractionOperand](#createInteractionOperand())()`
Returns a new object of class '*Interaction Operand*'.
`[InteractionUse](../interactions/mdfragments/InteractionUse.html)`
`[createInteractionUse](#createInteractionUse())()`
Returns a new object of class '*Interaction Use*'.
`[Interface](../classes/mdinterfaces/Interface.html)`
`[createInterface](#createInterface())()`
Returns a new object of class '*Interface*'.
`[InterfaceRealization](../classes/mdinterfaces/InterfaceRealization.html)`
`[createInterfaceRealization](#createInterfaceRealization())()`
Returns a new object of class '*Interface Realization*'.
`[InterruptibleActivityRegion](../activities/mdcompleteactivities/InterruptibleActivityRegion.html)`
`[createInterruptibleActivityRegion](#createInterruptibleActivityRegion())()`
Returns a new object of class '*Interruptible Activity Region*'.
`[Interval](../commonbehaviors/mdsimpletime/Interval.html)`
`[createInterval](#createInterval())()`
Returns a new object of class '*Interval*'.
`[IntervalConstraint](../commonbehaviors/mdsimpletime/IntervalConstraint.html)`
`[createIntervalConstraint](#createIntervalConstraint())()`
Returns a new object of class '*Interval Constraint*'.
`[JoinNode](../activities/mdintermediateactivities/JoinNode.html)`
`[createJoinNode](#createJoinNode())()`
Returns a new object of class '*Join Node*'.
`[Lifeline](../interactions/mdbasicinteractions/Lifeline.html)`
`[createLifeline](#createLifeline())()`
Returns a new object of class '*Lifeline*'.
`[LinkEndCreationData](../actions/mdintermediateactions/LinkEndCreationData.html)`
`[createLinkEndCreationData](#createLinkEndCreationData())()`
Returns a new object of class '*Link End Creation Data*'.
`[LinkEndData](../actions/mdintermediateactions/LinkEndData.html)`
`[createLinkEndData](#createLinkEndData())()`
Returns a new object of class '*Link End Data*'.
`[LinkEndDestructionData](../actions/mdintermediateactions/LinkEndDestructionData.html)`
`[createLinkEndDestructionData](#createLinkEndDestructionData())()`
Returns a new object of class '*Link End Destruction Data*'.
`[LiteralBoolean](../classes/mdkernel/LiteralBoolean.html)`
`[createLiteralBoolean](#createLiteralBoolean())()`
Returns a new object of class '*Literal Boolean*'.
`[LiteralInteger](../classes/mdkernel/LiteralInteger.html)`
`[createLiteralInteger](#createLiteralInteger())()`
Returns a new object of class '*Literal Integer*'.
`[LiteralNull](../classes/mdkernel/LiteralNull.html)`
`[createLiteralNull](#createLiteralNull())()`
Returns a new object of class '*Literal Null*'.
`[LiteralReal](../classes/mdkernel/LiteralReal.html)`
`[createLiteralReal](#createLiteralReal())()`
Returns a new object of class '*Literal Real*'.
`[LiteralString](../classes/mdkernel/LiteralString.html)`
`[createLiteralString](#createLiteralString())()`
Returns a new object of class '*Literal String*'.
`[LiteralUnlimitedNatural](../classes/mdkernel/LiteralUnlimitedNatural.html)`
`[createLiteralUnlimitedNatural](#createLiteralUnlimitedNatural())()`
Returns a new object of class '*Literal Unlimited Natural*'.
`[LoopNode](../activities/mdstructuredactivities/LoopNode.html)`
`[createLoopNode](#createLoopNode())()`
Returns a new object of class '*Loop Node*'.
`[Manifestation](../deployments/mdartifacts/Manifestation.html)`
`[createManifestation](#createManifestation())()`
Returns a new object of class '*Manifestation*'.
`[MergeNode](../activities/mdintermediateactivities/MergeNode.html)`
`[createMergeNode](#createMergeNode())()`
Returns a new object of class '*Merge Node*'.
`[Message](../interactions/mdbasicinteractions/Message.html)`
`[createMessage](#createMessage())()`
Returns a new object of class '*Message*'.
`[MessageOccurrenceSpecification](../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html)`
`[createMessageOccurrenceSpecification](#createMessageOccurrenceSpecification())()`
Returns a new object of class '*Message Occurrence Specification*'.
`[Model](../auxiliaryconstructs/mdmodels/Model.html)`
`[createModel](#createModel())()`
Returns a new object of class '*Model*'.
`[Node](../deployments/mdnodes/Node.html)`
`[createNode](#createNode())()`
Returns a new object of class '*Node*'.
`[ObjectFlow](../activities/mdbasicactivities/ObjectFlow.html)`
`[createObjectFlow](#createObjectFlow())()`
Returns a new object of class '*Object Flow*'.
`[OccurrenceSpecification](../interactions/mdbasicinteractions/OccurrenceSpecification.html)`
`[createOccurrenceSpecification](#createOccurrenceSpecification())()`
Returns a new object of class '*Occurrence Specification*'.
`[OpaqueAction](../actions/mdbasicactions/OpaqueAction.html)`
`[createOpaqueAction](#createOpaqueAction())()`
Returns a new object of class '*Opaque Action*'.
`[OpaqueBehavior](../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html)`
`[createOpaqueBehavior](#createOpaqueBehavior())()`
Returns a new object of class '*Opaque Behavior*'.
`[OpaqueExpression](../classes/mdkernel/OpaqueExpression.html)`
`[createOpaqueExpression](#createOpaqueExpression())()`
Returns a new object of class '*Opaque Expression*'.
`[Operation](../classes/mdkernel/Operation.html)`
`[createOperation](#createOperation())()`
Returns a new object of class '*Operation*'.
`[OperationTemplateParameter](../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html)`
`[createOperationTemplateParameter](#createOperationTemplateParameter())()`
Returns a new object of class '*Operation Template Parameter*'.
`[OutputPin](../actions/mdbasicactions/OutputPin.html)`
`[createOutputPin](#createOutputPin())()`
Returns a new object of class '*Output Pin*'.
`[Package](../classes/mdkernel/Package.html)`
`[createPackage](#createPackage())()`
Returns a new object of class '*Package*'.
`[PackageImport](../classes/mdkernel/PackageImport.html)`
`[createPackageImport](#createPackageImport())()`
Returns a new object of class '*Package Import*'.
`[PackageMerge](../classes/mdkernel/PackageMerge.html)`
`[createPackageMerge](#createPackageMerge())()`
Returns a new object of class '*Package Merge*'.
`[Parameter](../classes/mdkernel/Parameter.html)`
`[createParameter](#createParameter())()`
Returns a new object of class '*Parameter*'.
`[ParameterSet](../activities/mdcompleteactivities/ParameterSet.html)`
`[createParameterSet](#createParameterSet())()`
Returns a new object of class '*Parameter Set*'.
`[PartDecomposition](../interactions/mdfragments/PartDecomposition.html)`
`[createPartDecomposition](#createPartDecomposition())()`
Returns a new object of class '*Part Decomposition*'.
`[Port](../compositestructures/mdports/Port.html)`
`[createPort](#createPort())()`
Returns a new object of class '*Port*'.
`[PrimitiveType](../classes/mdkernel/PrimitiveType.html)`
`[createPrimitiveType](#createPrimitiveType())()`
Returns a new object of class '*Primitive Type*'.
`[Profile](../mdprofiles/Profile.html)`
`[createProfile](#createProfile())()`
Returns a new object of class '*Profile*'.
`[ProfileApplication](../mdprofiles/ProfileApplication.html)`
`[createProfileApplication](#createProfileApplication())()`
Returns a new object of class '*Profile Application*'.
`[Property](../classes/mdkernel/Property.html)`
`[createProperty](#createProperty())()`
Returns a new object of class '*Property*'.
`[ProtocolConformance](../statemachines/mdprotocolstatemachines/ProtocolConformance.html)`
`[createProtocolConformance](#createProtocolConformance())()`
Returns a new object of class '*Protocol Conformance*'.
`[ProtocolStateMachine](../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)`
`[createProtocolStateMachine](#createProtocolStateMachine())()`
Returns a new object of class '*Protocol State Machine*'.
`[ProtocolTransition](../statemachines/mdprotocolstatemachines/ProtocolTransition.html)`
`[createProtocolTransition](#createProtocolTransition())()`
Returns a new object of class '*Protocol Transition*'.
`[Pseudostate](../statemachines/mdbehaviorstatemachines/Pseudostate.html)`
`[createPseudostate](#createPseudostate())()`
Returns a new object of class '*Pseudostate*'.
`[QualifierValue](../actions/mdcompleteactions/QualifierValue.html)`
`[createQualifierValue](#createQualifierValue())()`
Returns a new object of class '*Qualifier Value*'.
`[RaiseExceptionAction](../actions/mdstructuredactions/RaiseExceptionAction.html)`
`[createRaiseExceptionAction](#createRaiseExceptionAction())()`
Returns a new object of class '*Raise Exception Action*'.
`[ReadExtentAction](../actions/mdcompleteactions/ReadExtentAction.html)`
`[createReadExtentAction](#createReadExtentAction())()`
Returns a new object of class '*Read Extent Action*'.
`[ReadIsClassifiedObjectAction](../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html)`
`[createReadIsClassifiedObjectAction](#createReadIsClassifiedObjectAction())()`
Returns a new object of class '*Read Is Classified Object Action*'.
`[ReadLinkAction](../actions/mdintermediateactions/ReadLinkAction.html)`
`[createReadLinkAction](#createReadLinkAction())()`
Returns a new object of class '*Read Link Action*'.
`[ReadLinkObjectEndAction](../actions/mdcompleteactions/ReadLinkObjectEndAction.html)`
`[createReadLinkObjectEndAction](#createReadLinkObjectEndAction())()`
Returns a new object of class '*Read Link Object End Action*'.
`[ReadLinkObjectEndQualifierAction](../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html)`
`[createReadLinkObjectEndQualifierAction](#createReadLinkObjectEndQualifierAction())()`
Returns a new object of class '*Read Link Object End Qualifier Action*'.
`[ReadSelfAction](../actions/mdintermediateactions/ReadSelfAction.html)`
`[createReadSelfAction](#createReadSelfAction())()`
Returns a new object of class '*Read Self Action*'.
`[ReadStructuralFeatureAction](../actions/mdintermediateactions/ReadStructuralFeatureAction.html)`
`[createReadStructuralFeatureAction](#createReadStructuralFeatureAction())()`
Returns a new object of class '*Read Structural Feature Action*'.
`[ReadVariableAction](../actions/mdstructuredactions/ReadVariableAction.html)`
`[createReadVariableAction](#createReadVariableAction())()`
Returns a new object of class '*Read Variable Action*'.
`[Realization](../classes/mddependencies/Realization.html)`
`[createRealization](#createRealization())()`
Returns a new object of class '*Realization*'.
`[RealTaggedValue](../classes/mdkernel/RealTaggedValue.html)`
`[createRealTaggedValue](#createRealTaggedValue())()`
Returns a new object of class '*Real Tagged Value*'.
`[Reception](../commonbehaviors/mdcommunications/Reception.html)`
`[createReception](#createReception())()`
Returns a new object of class '*Reception*'.
`[ReclassifyObjectAction](../actions/mdcompleteactions/ReclassifyObjectAction.html)`
`[createReclassifyObjectAction](#createReclassifyObjectAction())()`
Returns a new object of class '*Reclassify Object Action*'.
`[RedefinableTemplateSignature](../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html)`
`[createRedefinableTemplateSignature](#createRedefinableTemplateSignature())()`
Returns a new object of class '*Redefinable Template Signature*'.
`[ReduceAction](../actions/mdcompleteactions/ReduceAction.html)`
`[createReduceAction](#createReduceAction())()`
Returns a new object of class '*Reduce Action*'.
`[Region](../statemachines/mdbehaviorstatemachines/Region.html)`
`[createRegion](#createRegion())()`
Returns a new object of class '*Region*'.
`[RemoveStructuralFeatureValueAction](../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html)`
`[createRemoveStructuralFeatureValueAction](#createRemoveStructuralFeatureValueAction())()`
Returns a new object of class '*Remove Structural Feature Value Action*'.
`[RemoveVariableValueAction](../actions/mdstructuredactions/RemoveVariableValueAction.html)`
`[createRemoveVariableValueAction](#createRemoveVariableValueAction())()`
Returns a new object of class '*Remove Variable Value Action*'.
`[ReplyAction](../actions/mdcompleteactions/ReplyAction.html)`
`[createReplyAction](#createReplyAction())()`
Returns a new object of class '*Reply Action*'.
`[SendObjectAction](../actions/mdintermediateactions/SendObjectAction.html)`
`[createSendObjectAction](#createSendObjectAction())()`
Returns a new object of class '*Send Object Action*'.
`[SendSignalAction](../actions/mdbasicactions/SendSignalAction.html)`
`[createSendSignalAction](#createSendSignalAction())()`
Returns a new object of class '*Send Signal Action*'.
`[SequenceNode](../activities/mdstructuredactivities/SequenceNode.html)`
`[createSequenceNode](#createSequenceNode())()`
Returns a new object of class '*Sequence Node*'.
`[Signal](../commonbehaviors/mdcommunications/Signal.html)`
`[createSignal](#createSignal())()`
Returns a new object of class '*Signal*'.
`[SignalEvent](../commonbehaviors/mdcommunications/SignalEvent.html)`
`[createSignalEvent](#createSignalEvent())()`
Returns a new object of class '*Signal Event*'.
`[Slot](../classes/mdkernel/Slot.html)`
`[createSlot](#createSlot())()`
Returns a new object of class '*Slot*'.
`[StartClassifierBehaviorAction](../actions/mdcompleteactions/StartClassifierBehaviorAction.html)`
`[createStartClassifierBehaviorAction](#createStartClassifierBehaviorAction())()`
Returns a new object of class '*Start Classifier Behavior Action*'.
`[StartObjectBehaviorAction](../actions/mdcompleteactions/StartObjectBehaviorAction.html)`
`[createStartObjectBehaviorAction](#createStartObjectBehaviorAction())()`
Returns a new object of class '*Start Object Behavior Action*'.
`[State](../statemachines/mdbehaviorstatemachines/State.html)`
`[createState](#createState())()`
Returns a new object of class '*State*'.
`[StateInvariant](../interactions/mdbasicinteractions/StateInvariant.html)`
`[createStateInvariant](#createStateInvariant())()`
Returns a new object of class '*State Invariant*'.
`[StateMachine](../statemachines/mdbehaviorstatemachines/StateMachine.html)`
`[createStateMachine](#createStateMachine())()`
Returns a new object of class '*State Machine*'.
`[Stereotype](../mdprofiles/Stereotype.html)`
`[createStereotype](#createStereotype())()`
Returns a new object of class '*Stereotype*'.
`[StringExpression](../auxiliaryconstructs/mdtemplates/StringExpression.html)`
`[createStringExpression](#createStringExpression())()`
Returns a new object of class '*String Expression*'.
`[StringTaggedValue](../classes/mdkernel/StringTaggedValue.html)`
`[createStringTaggedValue](#createStringTaggedValue())()`
Returns a new object of class '*String Tagged Value*'.
`[StructuredActivityNode](../activities/mdstructuredactivities/StructuredActivityNode.html)`
`[createStructuredActivityNode](#createStructuredActivityNode())()`
Returns a new object of class '*Structured Activity Node*'.
`[Substitution](../classes/mddependencies/Substitution.html)`
`[createSubstitution](#createSubstitution())()`
Returns a new object of class '*Substitution*'.
`[TemplateBinding](../auxiliaryconstructs/mdtemplates/TemplateBinding.html)`
`[createTemplateBinding](#createTemplateBinding())()`
Returns a new object of class '*Template Binding*'.
`[TemplateParameter](../auxiliaryconstructs/mdtemplates/TemplateParameter.html)`
`[createTemplateParameter](#createTemplateParameter())()`
Returns a new object of class '*Template Parameter*'.
`[TemplateParameterSubstitution](../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html)`
`[createTemplateParameterSubstitution](#createTemplateParameterSubstitution())()`
Returns a new object of class '*Template Parameter Substitution*'.
`[TemplateSignature](../auxiliaryconstructs/mdtemplates/TemplateSignature.html)`
`[createTemplateSignature](#createTemplateSignature())()`
Returns a new object of class '*Template Signature*'.
`[TestIdentityAction](../actions/mdintermediateactions/TestIdentityAction.html)`
`[createTestIdentityAction](#createTestIdentityAction())()`
Returns a new object of class '*Test Identity Action*'.
`[TimeConstraint](../commonbehaviors/mdsimpletime/TimeConstraint.html)`
`[createTimeConstraint](#createTimeConstraint())()`
Returns a new object of class '*Time Constraint*'.
`[TimeEvent](../commonbehaviors/mdcommunications/TimeEvent.html)`
`[createTimeEvent](#createTimeEvent())()`
Returns a new object of class '*Time Event*'.
`[TimeExpression](../commonbehaviors/mdsimpletime/TimeExpression.html)`
`[createTimeExpression](#createTimeExpression())()`
Returns a new object of class '*Time Expression*'.
`[TimeInterval](../commonbehaviors/mdsimpletime/TimeInterval.html)`
`[createTimeInterval](#createTimeInterval())()`
Returns a new object of class '*Time Interval*'.
`[TimeObservation](../commonbehaviors/mdsimpletime/TimeObservation.html)`
`[createTimeObservation](#createTimeObservation())()`
Returns a new object of class '*Time Observation*'.
`[Transition](../statemachines/mdbehaviorstatemachines/Transition.html)`
`[createTransition](#createTransition())()`
Returns a new object of class '*Transition*'.
`[Trigger](../commonbehaviors/mdcommunications/Trigger.html)`
`[createTrigger](#createTrigger())()`
Returns a new object of class '*Trigger*'.
`[UnmarshallAction](../actions/mdcompleteactions/UnmarshallAction.html)`
`[createUnmarshallAction](#createUnmarshallAction())()`
Returns a new object of class '*Unmarshall Action*'.
`[Usage](../classes/mddependencies/Usage.html)`
`[createUsage](#createUsage())()`
Returns a new object of class '*Usage*'.
`[UseCase](../mdusecases/UseCase.html)`
`[createUseCase](#createUseCase())()`
Returns a new object of class '*Use Case*'.
`[ValuePin](../actions/mdbasicactions/ValuePin.html)`
`[createValuePin](#createValuePin())()`
Returns a new object of class '*Value Pin*'.
`[ValueSpecificationAction](../actions/mdintermediateactions/ValueSpecificationAction.html)`
`[createValueSpecificationAction](#createValueSpecificationAction())()`
Returns a new object of class '*Value Specification Action*'.
`[Variable](../activities/mdstructuredactivities/Variable.html)`
`[createVariable](#createVariable())()`
Returns a new object of class '*Variable*'.
`[UMLPackage](UMLPackage.html)`
`[getUMLPackage](#getUMLPackage())()`
Returns the package supported by this factory.
`void`
`[setRepository](#setRepository(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository))([AbstractRepository](../../jmi/reflect/AbstractRepository.html) repository)`
Deprecated.
The method should not be used.
Methods inherited from interface org.eclipse.emf.ecore.EFactory
`convertToString, create, createFromString, getEPackage, setEPackage`
Methods inherited from interface org.eclipse.emf.ecore.EModelElement
`getEAnnotation, getEAnnotations`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`

============ FIELD DETAIL =========== 
Field Details
eINSTANCE
static final [UMLFactory](UMLFactory.html) eINSTANCE
The singleton instance of the factory.
 begin-user-doc 
 end-user-doc
Generated:
 ============ METHOD DETAIL ========== 
Method Details
createSendSignalAction
[SendSignalAction](../actions/mdbasicactions/SendSignalAction.html) createSendSignalAction()
Returns a new object of class '*Send Signal Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Send Signal Action*'.
Generated:
createComment
[Comment](../classes/mdkernel/Comment.html) createComment()
Returns a new object of class '*Comment*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Comment*'.
Generated:
createInstanceSpecification
[InstanceSpecification](../classes/mdkernel/InstanceSpecification.html) createInstanceSpecification()
Returns a new object of class '*Instance Specification*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Instance Specification*'.
Generated:
createTemplateParameter
[TemplateParameter](../auxiliaryconstructs/mdtemplates/TemplateParameter.html) createTemplateParameter()
Returns a new object of class '*Template Parameter*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Template Parameter*'.
Generated:
createTemplateSignature
[TemplateSignature](../auxiliaryconstructs/mdtemplates/TemplateSignature.html) createTemplateSignature()
Returns a new object of class '*Template Signature*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Template Signature*'.
Generated:
createTemplateBinding
[TemplateBinding](../auxiliaryconstructs/mdtemplates/TemplateBinding.html) createTemplateBinding()
Returns a new object of class '*Template Binding*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Template Binding*'.
Generated:
createInformationFlow
[InformationFlow](../auxiliaryconstructs/mdinformationflows/InformationFlow.html) createInformationFlow()
Returns a new object of class '*Information Flow*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Information Flow*'.
Generated:
createElementImport
[ElementImport](../classes/mdkernel/ElementImport.html) createElementImport()
Returns a new object of class '*Element Import*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Element Import*'.
Generated:
createProfile
[Profile](../mdprofiles/Profile.html) createProfile()
Returns a new object of class '*Profile*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Profile*'.
Generated:
createPackage
[Package](../classes/mdkernel/Package.html) createPackage()
Returns a new object of class '*Package*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Package*'.
Generated:
createStereotype
[Stereotype](../mdprofiles/Stereotype.html) createStereotype()
Returns a new object of class '*Stereotype*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Stereotype*'.
Generated:
createClass
[Class](../classes/mdkernel/Class.html) createClass()
Returns a new object of class '*Class*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Class*'.
Generated:
createParameter
[Parameter](../classes/mdkernel/Parameter.html) createParameter()
Returns a new object of class '*Parameter*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Parameter*'.
Generated:
createAssociation
[Association](../classes/mdkernel/Association.html) createAssociation()
Returns a new object of class '*Association*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Association*'.
Generated:
createProperty
[Property](../classes/mdkernel/Property.html) createProperty()
Returns a new object of class '*Property*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Property*'.
Generated:
createSlot
[Slot](../classes/mdkernel/Slot.html) createSlot()
Returns a new object of class '*Slot*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Slot*'.
Generated:
createInputPin
[InputPin](../actions/mdbasicactions/InputPin.html) createInputPin()
Returns a new object of class '*Input Pin*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Input Pin*'.
Generated:
createState
[State](../statemachines/mdbehaviorstatemachines/State.html) createState()
Returns a new object of class '*State*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*State*'.
Generated:
createRegion
[Region](../statemachines/mdbehaviorstatemachines/Region.html) createRegion()
Returns a new object of class '*Region*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Region*'.
Generated:
createStateMachine
[StateMachine](../statemachines/mdbehaviorstatemachines/StateMachine.html) createStateMachine()
Returns a new object of class '*State Machine*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*State Machine*'.
Generated:
createPseudostate
[Pseudostate](../statemachines/mdbehaviorstatemachines/Pseudostate.html) createPseudostate()
Returns a new object of class '*Pseudostate*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Pseudostate*'.
Generated:
createConnectionPointReference
[ConnectionPointReference](../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html) createConnectionPointReference()
Returns a new object of class '*Connection Point Reference*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Connection Point Reference*'.
Generated:
createTransition
[Transition](../statemachines/mdbehaviorstatemachines/Transition.html) createTransition()
Returns a new object of class '*Transition*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Transition*'.
Generated:
createConstraint
[Constraint](../classes/mdkernel/Constraint.html) createConstraint()
Returns a new object of class '*Constraint*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Constraint*'.
Generated:
createOperation
[Operation](../classes/mdkernel/Operation.html) createOperation()
Returns a new object of class '*Operation*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Operation*'.
Generated:
createParameterSet
[ParameterSet](../activities/mdcompleteactivities/ParameterSet.html) createParameterSet()
Returns a new object of class '*Parameter Set*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Parameter Set*'.
Generated:
createDataType
[DataType](../classes/mdkernel/DataType.html) createDataType()
Returns a new object of class '*Data Type*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Data Type*'.
Generated:
createInterface
[Interface](../classes/mdinterfaces/Interface.html) createInterface()
Returns a new object of class '*Interface*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Interface*'.
Generated:
createReception
[Reception](../commonbehaviors/mdcommunications/Reception.html) createReception()
Returns a new object of class '*Reception*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Reception*'.
Generated:
createSignal
[Signal](../commonbehaviors/mdcommunications/Signal.html) createSignal()
Returns a new object of class '*Signal*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Signal*'.
Generated:
createBroadcastSignalAction
[BroadcastSignalAction](../actions/mdintermediateactions/BroadcastSignalAction.html) createBroadcastSignalAction()
Returns a new object of class '*Broadcast Signal Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Broadcast Signal Action*'.
Generated:
createSignalEvent
[SignalEvent](../commonbehaviors/mdcommunications/SignalEvent.html) createSignalEvent()
Returns a new object of class '*Signal Event*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Signal Event*'.
Generated:
createTrigger
[Trigger](../commonbehaviors/mdcommunications/Trigger.html) createTrigger()
Returns a new object of class '*Trigger*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Trigger*'.
Generated:
createPort
[Port](../compositestructures/mdports/Port.html) createPort()
Returns a new object of class '*Port*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Port*'.
Generated:
createProtocolStateMachine
[ProtocolStateMachine](../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html) createProtocolStateMachine()
Returns a new object of class '*Protocol State Machine*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Protocol State Machine*'.
Generated:
createProtocolConformance
[ProtocolConformance](../statemachines/mdprotocolstatemachines/ProtocolConformance.html) createProtocolConformance()
Returns a new object of class '*Protocol Conformance*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Protocol Conformance*'.
Generated:
createConnector
[Connector](../compositestructures/mdinternalstructures/Connector.html) createConnector()
Returns a new object of class '*Connector*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Connector*'.
Generated:
createConnectorEnd
[ConnectorEnd](../compositestructures/mdinternalstructures/ConnectorEnd.html) createConnectorEnd()
Returns a new object of class '*Connector End*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Connector End*'.
Generated:
createConnectableElementTemplateParameter
[ConnectableElementTemplateParameter](../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html) createConnectableElementTemplateParameter()
Returns a new object of class '*Connectable Element Template Parameter*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Connectable Element Template Parameter*'.
Generated:
createCollaboration
[Collaboration](../compositestructures/mdcollaborations/Collaboration.html) createCollaboration()
Returns a new object of class '*Collaboration*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Collaboration*'.
Generated:
createCollaborationUse
[CollaborationUse](../compositestructures/mdcollaborations/CollaborationUse.html) createCollaborationUse()
Returns a new object of class '*Collaboration Use*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Collaboration Use*'.
Generated:
createDependency
[Dependency](../classes/mddependencies/Dependency.html) createDependency()
Returns a new object of class '*Dependency*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Dependency*'.
Generated:
createLifeline
[Lifeline](../interactions/mdbasicinteractions/Lifeline.html) createLifeline()
Returns a new object of class '*Lifeline*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Lifeline*'.
Generated:
createInteraction
[Interaction](../interactions/mdbasicinteractions/Interaction.html) createInteraction()
Returns a new object of class '*Interaction*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Interaction*'.
Generated:
createGate
[Gate](../interactions/mdfragments/Gate.html) createGate()
Returns a new object of class '*Gate*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Gate*'.
Generated:
createMessage
[Message](../interactions/mdbasicinteractions/Message.html) createMessage()
Returns a new object of class '*Message*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Message*'.
Generated:
createInteractionUse
[InteractionUse](../interactions/mdfragments/InteractionUse.html) createInteractionUse()
Returns a new object of class '*Interaction Use*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Interaction Use*'.
Generated:
createCombinedFragment
[CombinedFragment](../interactions/mdfragments/CombinedFragment.html) createCombinedFragment()
Returns a new object of class '*Combined Fragment*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Combined Fragment*'.
Generated:
createInteractionOperand
[InteractionOperand](../interactions/mdfragments/InteractionOperand.html) createInteractionOperand()
Returns a new object of class '*Interaction Operand*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Interaction Operand*'.
Generated:
createInteractionConstraint
[InteractionConstraint](../interactions/mdfragments/InteractionConstraint.html) createInteractionConstraint()
Returns a new object of class '*Interaction Constraint*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Interaction Constraint*'.
Generated:
createGeneralOrdering
[GeneralOrdering](../interactions/mdbasicinteractions/GeneralOrdering.html) createGeneralOrdering()
Returns a new object of class '*General Ordering*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*General Ordering*'.
Generated:
createOccurrenceSpecification
[OccurrenceSpecification](../interactions/mdbasicinteractions/OccurrenceSpecification.html) createOccurrenceSpecification()
Returns a new object of class '*Occurrence Specification*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Occurrence Specification*'.
Generated:
createExecutionOccurrenceSpecification
[ExecutionOccurrenceSpecification](../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html) createExecutionOccurrenceSpecification()
Returns a new object of class '*Execution Occurrence Specification*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Execution Occurrence Specification*'.
Generated:
createPartDecomposition
[PartDecomposition](../interactions/mdfragments/PartDecomposition.html) createPartDecomposition()
Returns a new object of class '*Part Decomposition*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Part Decomposition*'.
Generated:
createStateInvariant
[StateInvariant](../interactions/mdbasicinteractions/StateInvariant.html) createStateInvariant()
Returns a new object of class '*State Invariant*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*State Invariant*'.
Generated:
createReplyAction
[ReplyAction](../actions/mdcompleteactions/ReplyAction.html) createReplyAction()
Returns a new object of class '*Reply Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Reply Action*'.
Generated:
createAcceptEventAction
[AcceptEventAction](../actions/mdcompleteactions/AcceptEventAction.html) createAcceptEventAction()
Returns a new object of class '*Accept Event Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Accept Event Action*'.
Generated:
createOutputPin
[OutputPin](../actions/mdbasicactions/OutputPin.html) createOutputPin()
Returns a new object of class '*Output Pin*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Output Pin*'.
Generated:
createClause
[Clause](../activities/mdstructuredactivities/Clause.html) createClause()
Returns a new object of class '*Clause*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Clause*'.
Generated:
createConditionalNode
[ConditionalNode](../activities/mdstructuredactivities/ConditionalNode.html) createConditionalNode()
Returns a new object of class '*Conditional Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Conditional Node*'.
Generated:
createStructuredActivityNode
[StructuredActivityNode](../activities/mdstructuredactivities/StructuredActivityNode.html) createStructuredActivityNode()
Returns a new object of class '*Structured Activity Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Structured Activity Node*'.
Generated:
createActivity
[Activity](../activities/mdfundamentalactivities/Activity.html) createActivity()
Returns a new object of class '*Activity*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Activity*'.
Generated:
createActivityPartition
[ActivityPartition](../activities/mdintermediateactivities/ActivityPartition.html) createActivityPartition()
Returns a new object of class '*Activity Partition*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Activity Partition*'.
Generated:
createVariable
[Variable](../activities/mdstructuredactivities/Variable.html) createVariable()
Returns a new object of class '*Variable*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Variable*'.
Generated:
createInterruptibleActivityRegion
[InterruptibleActivityRegion](../activities/mdcompleteactivities/InterruptibleActivityRegion.html) createInterruptibleActivityRegion()
Returns a new object of class '*Interruptible Activity Region*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Interruptible Activity Region*'.
Generated:
createLoopNode
[LoopNode](../activities/mdstructuredactivities/LoopNode.html) createLoopNode()
Returns a new object of class '*Loop Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Loop Node*'.
Generated:
createOpaqueAction
[OpaqueAction](../actions/mdbasicactions/OpaqueAction.html) createOpaqueAction()
Returns a new object of class '*Opaque Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Opaque Action*'.
Generated:
createClearStructuralFeatureAction
[ClearStructuralFeatureAction](../actions/mdintermediateactions/ClearStructuralFeatureAction.html) createClearStructuralFeatureAction()
Returns a new object of class '*Clear Structural Feature Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Clear Structural Feature Action*'.
Generated:
createCreateLinkObjectAction
[CreateLinkObjectAction](../actions/mdcompleteactions/CreateLinkObjectAction.html) createCreateLinkObjectAction()
Returns a new object of class '*Create Link Object Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Create Link Object Action*'.
Generated:
createCreateLinkAction
[CreateLinkAction](../actions/mdintermediateactions/CreateLinkAction.html) createCreateLinkAction()
Returns a new object of class '*Create Link Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Create Link Action*'.
Generated:
createLinkEndData
[LinkEndData](../actions/mdintermediateactions/LinkEndData.html) createLinkEndData()
Returns a new object of class '*Link End Data*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Link End Data*'.
Generated:
createQualifierValue
[QualifierValue](../actions/mdcompleteactions/QualifierValue.html) createQualifierValue()
Returns a new object of class '*Qualifier Value*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Qualifier Value*'.
Generated:
createLinkEndCreationData
[LinkEndCreationData](../actions/mdintermediateactions/LinkEndCreationData.html) createLinkEndCreationData()
Returns a new object of class '*Link End Creation Data*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Link End Creation Data*'.
Generated:
createCreateObjectAction
[CreateObjectAction](../actions/mdintermediateactions/CreateObjectAction.html) createCreateObjectAction()
Returns a new object of class '*Create Object Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Create Object Action*'.
Generated:
createReadExtentAction
[ReadExtentAction](../actions/mdcompleteactions/ReadExtentAction.html) createReadExtentAction()
Returns a new object of class '*Read Extent Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Read Extent Action*'.
Generated:
createReadIsClassifiedObjectAction
[ReadIsClassifiedObjectAction](../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html) createReadIsClassifiedObjectAction()
Returns a new object of class '*Read Is Classified Object Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Read Is Classified Object Action*'.
Generated:
createReadLinkAction
[ReadLinkAction](../actions/mdintermediateactions/ReadLinkAction.html) createReadLinkAction()
Returns a new object of class '*Read Link Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Read Link Action*'.
Generated:
createReadLinkObjectEndAction
[ReadLinkObjectEndAction](../actions/mdcompleteactions/ReadLinkObjectEndAction.html) createReadLinkObjectEndAction()
Returns a new object of class '*Read Link Object End Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Read Link Object End Action*'.
Generated:
createReadLinkObjectEndQualifierAction
[ReadLinkObjectEndQualifierAction](../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html) createReadLinkObjectEndQualifierAction()
Returns a new object of class '*Read Link Object End Qualifier Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Read Link Object End Qualifier Action*'.
Generated:
createReadSelfAction
[ReadSelfAction](../actions/mdintermediateactions/ReadSelfAction.html) createReadSelfAction()
Returns a new object of class '*Read Self Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Read Self Action*'.
Generated:
createReadStructuralFeatureAction
[ReadStructuralFeatureAction](../actions/mdintermediateactions/ReadStructuralFeatureAction.html) createReadStructuralFeatureAction()
Returns a new object of class '*Read Structural Feature Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Read Structural Feature Action*'.
Generated:
createReadVariableAction
[ReadVariableAction](../actions/mdstructuredactions/ReadVariableAction.html) createReadVariableAction()
Returns a new object of class '*Read Variable Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Read Variable Action*'.
Generated:
createReduceAction
[ReduceAction](../actions/mdcompleteactions/ReduceAction.html) createReduceAction()
Returns a new object of class '*Reduce Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Reduce Action*'.
Generated:
createTestIdentityAction
[TestIdentityAction](../actions/mdintermediateactions/TestIdentityAction.html) createTestIdentityAction()
Returns a new object of class '*Test Identity Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Test Identity Action*'.
Generated:
createUnmarshallAction
[UnmarshallAction](../actions/mdcompleteactions/UnmarshallAction.html) createUnmarshallAction()
Returns a new object of class '*Unmarshall Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Unmarshall Action*'.
Generated:
createValueSpecificationAction
[ValueSpecificationAction](../actions/mdintermediateactions/ValueSpecificationAction.html) createValueSpecificationAction()
Returns a new object of class '*Value Specification Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Value Specification Action*'.
Generated:
createAcceptCallAction
[AcceptCallAction](../actions/mdcompleteactions/AcceptCallAction.html) createAcceptCallAction()
Returns a new object of class '*Accept Call Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Accept Call Action*'.
Generated:
createInterfaceRealization
[InterfaceRealization](../classes/mdinterfaces/InterfaceRealization.html) createInterfaceRealization()
Returns a new object of class '*Interface Realization*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Interface Realization*'.
Generated:
createRealization
[Realization](../classes/mddependencies/Realization.html) createRealization()
Returns a new object of class '*Realization*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Realization*'.
Generated:
createAbstraction
[Abstraction](../classes/mddependencies/Abstraction.html) createAbstraction()
Returns a new object of class '*Abstraction*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Abstraction*'.
Generated:
createOpaqueExpression
[OpaqueExpression](../classes/mdkernel/OpaqueExpression.html) createOpaqueExpression()
Returns a new object of class '*Opaque Expression*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Opaque Expression*'.
Generated:
createComponent
[Component](../components/mdbasiccomponents/Component.html) createComponent()
Returns a new object of class '*Component*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Component*'.
Generated:
createComponentRealization
[ComponentRealization](../components/mdbasiccomponents/ComponentRealization.html) createComponentRealization()
Returns a new object of class '*Component Realization*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Component Realization*'.
Generated:
createOperationTemplateParameter
[OperationTemplateParameter](../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html) createOperationTemplateParameter()
Returns a new object of class '*Operation Template Parameter*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Operation Template Parameter*'.
Generated:
createCallEvent
[CallEvent](../commonbehaviors/mdcommunications/CallEvent.html) createCallEvent()
Returns a new object of class '*Call Event*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Call Event*'.
Generated:
createCallOperationAction
[CallOperationAction](../actions/mdbasicactions/CallOperationAction.html) createCallOperationAction()
Returns a new object of class '*Call Operation Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Call Operation Action*'.
Generated:
createArtifact
[Artifact](../deployments/mdartifacts/Artifact.html) createArtifact()
Returns a new object of class '*Artifact*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Artifact*'.
Generated:
createDeployment
[Deployment](../deployments/mdnodes/Deployment.html) createDeployment()
Returns a new object of class '*Deployment*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Deployment*'.
Generated:
createDeploymentSpecification
[DeploymentSpecification](../deployments/mdcomponentdeployments/DeploymentSpecification.html) createDeploymentSpecification()
Returns a new object of class '*Deployment Specification*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Deployment Specification*'.
Generated:
createManifestation
[Manifestation](../deployments/mdartifacts/Manifestation.html) createManifestation()
Returns a new object of class '*Manifestation*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Manifestation*'.
Generated:
createProtocolTransition
[ProtocolTransition](../statemachines/mdprotocolstatemachines/ProtocolTransition.html) createProtocolTransition()
Returns a new object of class '*Protocol Transition*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Protocol Transition*'.
Generated:
createExtend
[Extend](../mdusecases/Extend.html) createExtend()
Returns a new object of class '*Extend*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Extend*'.
Generated:
createUseCase
[UseCase](../mdusecases/UseCase.html) createUseCase()
Returns a new object of class '*Use Case*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Use Case*'.
Generated:
createExtensionPoint
[ExtensionPoint](../mdusecases/ExtensionPoint.html) createExtensionPoint()
Returns a new object of class '*Extension Point*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Extension Point*'.
Generated:
createInclude
[Include](../mdusecases/Include.html) createInclude()
Returns a new object of class '*Include*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Include*'.
Generated:
createExceptionHandler
[ExceptionHandler](../activities/mdextrastructuredactivities/ExceptionHandler.html) createExceptionHandler()
Returns a new object of class '*Exception Handler*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Exception Handler*'.
Generated:
createLinkEndDestructionData
[LinkEndDestructionData](../actions/mdintermediateactions/LinkEndDestructionData.html) createLinkEndDestructionData()
Returns a new object of class '*Link End Destruction Data*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Link End Destruction Data*'.
Generated:
createDestroyLinkAction
[DestroyLinkAction](../actions/mdintermediateactions/DestroyLinkAction.html) createDestroyLinkAction()
Returns a new object of class '*Destroy Link Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Destroy Link Action*'.
Generated:
createRaiseExceptionAction
[RaiseExceptionAction](../actions/mdstructuredactions/RaiseExceptionAction.html) createRaiseExceptionAction()
Returns a new object of class '*Raise Exception Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Raise Exception Action*'.
Generated:
createAddStructuralFeatureValueAction
[AddStructuralFeatureValueAction](../actions/mdintermediateactions/AddStructuralFeatureValueAction.html) createAddStructuralFeatureValueAction()
Returns a new object of class '*Add Structural Feature Value Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Add Structural Feature Value Action*'.
Generated:
createAddVariableValueAction
[AddVariableValueAction](../actions/mdstructuredactions/AddVariableValueAction.html) createAddVariableValueAction()
Returns a new object of class '*Add Variable Value Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Add Variable Value Action*'.
Generated:
createClearAssociationAction
[ClearAssociationAction](../actions/mdintermediateactions/ClearAssociationAction.html) createClearAssociationAction()
Returns a new object of class '*Clear Association Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Clear Association Action*'.
Generated:
createReclassifyObjectAction
[ReclassifyObjectAction](../actions/mdcompleteactions/ReclassifyObjectAction.html) createReclassifyObjectAction()
Returns a new object of class '*Reclassify Object Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Reclassify Object Action*'.
Generated:
createStartClassifierBehaviorAction
[StartClassifierBehaviorAction](../actions/mdcompleteactions/StartClassifierBehaviorAction.html) createStartClassifierBehaviorAction()
Returns a new object of class '*Start Classifier Behavior Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Start Classifier Behavior Action*'.
Generated:
createStartObjectBehaviorAction
[StartObjectBehaviorAction](../actions/mdcompleteactions/StartObjectBehaviorAction.html) createStartObjectBehaviorAction()
Returns a new object of class '*Start Object Behavior Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Start Object Behavior Action*'.
Generated:
createRemoveStructuralFeatureValueAction
[RemoveStructuralFeatureValueAction](../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html) createRemoveStructuralFeatureValueAction()
Returns a new object of class '*Remove Structural Feature Value Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Remove Structural Feature Value Action*'.
Generated:
createRemoveVariableValueAction
[RemoveVariableValueAction](../actions/mdstructuredactions/RemoveVariableValueAction.html) createRemoveVariableValueAction()
Returns a new object of class '*Remove Variable Value Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Remove Variable Value Action*'.
Generated:
createSendObjectAction
[SendObjectAction](../actions/mdintermediateactions/SendObjectAction.html) createSendObjectAction()
Returns a new object of class '*Send Object Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Send Object Action*'.
Generated:
createDestroyObjectAction
[DestroyObjectAction](../actions/mdintermediateactions/DestroyObjectAction.html) createDestroyObjectAction()
Returns a new object of class '*Destroy Object Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Destroy Object Action*'.
Generated:
createChangeEvent
[ChangeEvent](../commonbehaviors/mdcommunications/ChangeEvent.html) createChangeEvent()
Returns a new object of class '*Change Event*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Change Event*'.
Generated:
createDuration
[Duration](../commonbehaviors/mdsimpletime/Duration.html) createDuration()
Returns a new object of class '*Duration*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Duration*'.
Generated:
createTimeExpression
[TimeExpression](../commonbehaviors/mdsimpletime/TimeExpression.html) createTimeExpression()
Returns a new object of class '*Time Expression*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Time Expression*'.
Generated:
createTimeInterval
[TimeInterval](../commonbehaviors/mdsimpletime/TimeInterval.html) createTimeInterval()
Returns a new object of class '*Time Interval*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Time Interval*'.
Generated:
createInterval
[Interval](../commonbehaviors/mdsimpletime/Interval.html) createInterval()
Returns a new object of class '*Interval*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Interval*'.
Generated:
createIntervalConstraint
[IntervalConstraint](../commonbehaviors/mdsimpletime/IntervalConstraint.html) createIntervalConstraint()
Returns a new object of class '*Interval Constraint*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Interval Constraint*'.
Generated:
createTimeConstraint
[TimeConstraint](../commonbehaviors/mdsimpletime/TimeConstraint.html) createTimeConstraint()
Returns a new object of class '*Time Constraint*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Time Constraint*'.
Generated:
createTimeEvent
[TimeEvent](../commonbehaviors/mdcommunications/TimeEvent.html) createTimeEvent()
Returns a new object of class '*Time Event*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Time Event*'.
Generated:
createDurationInterval
[DurationInterval](../commonbehaviors/mdsimpletime/DurationInterval.html) createDurationInterval()
Returns a new object of class '*Duration Interval*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Duration Interval*'.
Generated:
createDurationConstraint
[DurationConstraint](../commonbehaviors/mdsimpletime/DurationConstraint.html) createDurationConstraint()
Returns a new object of class '*Duration Constraint*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Duration Constraint*'.
Generated:
createJoinNode
[JoinNode](../activities/mdintermediateactivities/JoinNode.html) createJoinNode()
Returns a new object of class '*Join Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Join Node*'.
Generated:
createExpression
[Expression](../classes/mdkernel/Expression.html) createExpression()
Returns a new object of class '*Expression*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Expression*'.
Generated:
createValuePin
[ValuePin](../actions/mdbasicactions/ValuePin.html) createValuePin()
Returns a new object of class '*Value Pin*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Value Pin*'.
Generated:
createActivityParameterNode
[ActivityParameterNode](../activities/mdbasicactivities/ActivityParameterNode.html) createActivityParameterNode()
Returns a new object of class '*Activity Parameter Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Activity Parameter Node*'.
Generated:
createBehaviorExecutionSpecification
[BehaviorExecutionSpecification](../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html) createBehaviorExecutionSpecification()
Returns a new object of class '*Behavior Execution Specification*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Behavior Execution Specification*'.
Generated:
createCallBehaviorAction
[CallBehaviorAction](../actions/mdbasicactions/CallBehaviorAction.html) createCallBehaviorAction()
Returns a new object of class '*Call Behavior Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Call Behavior Action*'.
Generated:
createDecisionNode
[DecisionNode](../activities/mdintermediateactivities/DecisionNode.html) createDecisionNode()
Returns a new object of class '*Decision Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Decision Node*'.
Generated:
createObjectFlow
[ObjectFlow](../activities/mdbasicactivities/ObjectFlow.html) createObjectFlow()
Returns a new object of class '*Object Flow*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Object Flow*'.
Generated:
createExtension
[Extension](../mdprofiles/Extension.html) createExtension()
Returns a new object of class '*Extension*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Extension*'.
Generated:
createExtensionEnd
[ExtensionEnd](../mdprofiles/ExtensionEnd.html) createExtensionEnd()
Returns a new object of class '*Extension End*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Extension End*'.
Generated:
createImage
[Image](../mdprofiles/Image.html) createImage()
Returns a new object of class '*Image*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Image*'.
Generated:
createPackageMerge
[PackageMerge](../classes/mdkernel/PackageMerge.html) createPackageMerge()
Returns a new object of class '*Package Merge*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Package Merge*'.
Generated:
createProfileApplication
[ProfileApplication](../mdprofiles/ProfileApplication.html) createProfileApplication()
Returns a new object of class '*Profile Application*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Profile Application*'.
Generated:
createPackageImport
[PackageImport](../classes/mdkernel/PackageImport.html) createPackageImport()
Returns a new object of class '*Package Import*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Package Import*'.
Generated:
createDiagram
[Diagram](../classes/mdkernel/Diagram.html) createDiagram()
Returns a new object of class '*Diagram*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Diagram*'.
Generated:
createGeneralization
[Generalization](../classes/mdkernel/Generalization.html) createGeneralization()
Returns a new object of class '*Generalization*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Generalization*'.
Generated:
createGeneralizationSet
[GeneralizationSet](../classes/mdpowertypes/GeneralizationSet.html) createGeneralizationSet()
Returns a new object of class '*Generalization Set*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Generalization Set*'.
Generated:
createRedefinableTemplateSignature
[RedefinableTemplateSignature](../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html) createRedefinableTemplateSignature()
Returns a new object of class '*Redefinable Template Signature*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Redefinable Template Signature*'.
Generated:
createSubstitution
[Substitution](../classes/mddependencies/Substitution.html) createSubstitution()
Returns a new object of class '*Substitution*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Substitution*'.
Generated:
createClassifierTemplateParameter
[ClassifierTemplateParameter](../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html) createClassifierTemplateParameter()
Returns a new object of class '*Classifier Template Parameter*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Classifier Template Parameter*'.
Generated:
createInformationItem
[InformationItem](../auxiliaryconstructs/mdinformationflows/InformationItem.html) createInformationItem()
Returns a new object of class '*Information Item*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Information Item*'.
Generated:
createTemplateParameterSubstitution
[TemplateParameterSubstitution](../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html) createTemplateParameterSubstitution()
Returns a new object of class '*Template Parameter Substitution*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Template Parameter Substitution*'.
Generated:
createInstanceValue
[InstanceValue](../classes/mdkernel/InstanceValue.html) createInstanceValue()
Returns a new object of class '*Instance Value*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Instance Value*'.
Generated:
createElementValue
[ElementValue](../classes/mdkernel/ElementValue.html) createElementValue()
Returns a new object of class '*Element Value*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Element Value*'.
Generated:
createStringExpression
[StringExpression](../auxiliaryconstructs/mdtemplates/StringExpression.html) createStringExpression()
Returns a new object of class '*String Expression*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*String Expression*'.
Generated:
createDurationObservation
[DurationObservation](../commonbehaviors/mdsimpletime/DurationObservation.html) createDurationObservation()
Returns a new object of class '*Duration Observation*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Duration Observation*'.
Generated:
createTimeObservation
[TimeObservation](../commonbehaviors/mdsimpletime/TimeObservation.html) createTimeObservation()
Returns a new object of class '*Time Observation*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Time Observation*'.
Generated:
createConsiderIgnoreFragment
[ConsiderIgnoreFragment](../interactions/mdfragments/ConsiderIgnoreFragment.html) createConsiderIgnoreFragment()
Returns a new object of class '*Consider Ignore Fragment*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Consider Ignore Fragment*'.
Generated:
createSequenceNode
[SequenceNode](../activities/mdstructuredactivities/SequenceNode.html) createSequenceNode()
Returns a new object of class '*Sequence Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Sequence Node*'.
Generated:
createActionExecutionSpecification
[ActionExecutionSpecification](../interactions/mdbasicinteractions/ActionExecutionSpecification.html) createActionExecutionSpecification()
Returns a new object of class '*Action Execution Specification*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Action Execution Specification*'.
Generated:
createActionInputPin
[ActionInputPin](../actions/mdstructuredactions/ActionInputPin.html) createActionInputPin()
Returns a new object of class '*Action Input Pin*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Action Input Pin*'.
Generated:
createLiteralString
[LiteralString](../classes/mdkernel/LiteralString.html) createLiteralString()
Returns a new object of class '*Literal String*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Literal String*'.
Generated:
createDataStoreNode
[DataStoreNode](../activities/mdcompleteactivities/DataStoreNode.html) createDataStoreNode()
Returns a new object of class '*Data Store Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Data Store Node*'.
Generated:
createCentralBufferNode
[CentralBufferNode](../activities/mdintermediateactivities/CentralBufferNode.html) createCentralBufferNode()
Returns a new object of class '*Central Buffer Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Central Buffer Node*'.
Generated:
createInitialNode
[InitialNode](../activities/mdbasicactivities/InitialNode.html) createInitialNode()
Returns a new object of class '*Initial Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Initial Node*'.
Generated:
createDevice
[Device](../deployments/mdnodes/Device.html) createDevice()
Returns a new object of class '*Device*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Device*'.
Generated:
createNode
[Node](../deployments/mdnodes/Node.html) createNode()
Returns a new object of class '*Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Node*'.
Generated:
createAssociationClass
[AssociationClass](../classes/mdassociationclasses/AssociationClass.html) createAssociationClass()
Returns a new object of class '*Association Class*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Association Class*'.
Generated:
createActor
[Actor](../mdusecases/Actor.html) createActor()
Returns a new object of class '*Actor*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Actor*'.
Generated:
createExecutionEnvironment
[ExecutionEnvironment](../deployments/mdnodes/ExecutionEnvironment.html) createExecutionEnvironment()
Returns a new object of class '*Execution Environment*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Execution Environment*'.
Generated:
createFunctionBehavior
[FunctionBehavior](../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html) createFunctionBehavior()
Returns a new object of class '*Function Behavior*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Function Behavior*'.
Generated:
createOpaqueBehavior
[OpaqueBehavior](../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html) createOpaqueBehavior()
Returns a new object of class '*Opaque Behavior*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Opaque Behavior*'.
Generated:
createActivityFinalNode
[ActivityFinalNode](../activities/mdbasicactivities/ActivityFinalNode.html) createActivityFinalNode()
Returns a new object of class '*Activity Final Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Activity Final Node*'.
Generated:
createFlowFinalNode
[FlowFinalNode](../activities/mdintermediateactivities/FlowFinalNode.html) createFlowFinalNode()
Returns a new object of class '*Flow Final Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Flow Final Node*'.
Generated:
createLiteralReal
[LiteralReal](../classes/mdkernel/LiteralReal.html) createLiteralReal()
Returns a new object of class '*Literal Real*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Literal Real*'.
Generated:
createForkNode
[ForkNode](../activities/mdintermediateactivities/ForkNode.html) createForkNode()
Returns a new object of class '*Fork Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Fork Node*'.
Generated:
createControlFlow
[ControlFlow](../activities/mdbasicactivities/ControlFlow.html) createControlFlow()
Returns a new object of class '*Control Flow*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Control Flow*'.
Generated:
createUsage
[Usage](../classes/mddependencies/Usage.html) createUsage()
Returns a new object of class '*Usage*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Usage*'.
Generated:
createLiteralUnlimitedNatural
[LiteralUnlimitedNatural](../classes/mdkernel/LiteralUnlimitedNatural.html) createLiteralUnlimitedNatural()
Returns a new object of class '*Literal Unlimited Natural*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Literal Unlimited Natural*'.
Generated:
createLiteralInteger
[LiteralInteger](../classes/mdkernel/LiteralInteger.html) createLiteralInteger()
Returns a new object of class '*Literal Integer*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Literal Integer*'.
Generated:
createEnumeration
[Enumeration](../classes/mdkernel/Enumeration.html) createEnumeration()
Returns a new object of class '*Enumeration*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Enumeration*'.
Generated:
createEnumerationLiteral
[EnumerationLiteral](../classes/mdkernel/EnumerationLiteral.html) createEnumerationLiteral()
Returns a new object of class '*Enumeration Literal*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Enumeration Literal*'.
Generated:
createExpansionNode
[ExpansionNode](../activities/mdextrastructuredactivities/ExpansionNode.html) createExpansionNode()
Returns a new object of class '*Expansion Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Expansion Node*'.
Generated:
createExpansionRegion
[ExpansionRegion](../activities/mdextrastructuredactivities/ExpansionRegion.html) createExpansionRegion()
Returns a new object of class '*Expansion Region*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Expansion Region*'.
Generated:
createCommunicationPath
[CommunicationPath](../deployments/mdnodes/CommunicationPath.html) createCommunicationPath()
Returns a new object of class '*Communication Path*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Communication Path*'.
Generated:
createPrimitiveType
[PrimitiveType](../classes/mdkernel/PrimitiveType.html) createPrimitiveType()
Returns a new object of class '*Primitive Type*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Primitive Type*'.
Generated:
createFinalState
[FinalState](../statemachines/mdbehaviorstatemachines/FinalState.html) createFinalState()
Returns a new object of class '*Final State*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Final State*'.
Generated:
createAnyReceiveEvent
[AnyReceiveEvent](../commonbehaviors/mdcommunications/AnyReceiveEvent.html) createAnyReceiveEvent()
Returns a new object of class '*Any Receive Event*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Any Receive Event*'.
Generated:
createMergeNode
[MergeNode](../activities/mdintermediateactivities/MergeNode.html) createMergeNode()
Returns a new object of class '*Merge Node*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Merge Node*'.
Generated:
createContinuation
[Continuation](../interactions/mdfragments/Continuation.html) createContinuation()
Returns a new object of class '*Continuation*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Continuation*'.
Generated:
createLiteralNull
[LiteralNull](../classes/mdkernel/LiteralNull.html) createLiteralNull()
Returns a new object of class '*Literal Null*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Literal Null*'.
Generated:
createMessageOccurrenceSpecification
[MessageOccurrenceSpecification](../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html) createMessageOccurrenceSpecification()
Returns a new object of class '*Message Occurrence Specification*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Message Occurrence Specification*'.
Generated:
createLiteralBoolean
[LiteralBoolean](../classes/mdkernel/LiteralBoolean.html) createLiteralBoolean()
Returns a new object of class '*Literal Boolean*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Literal Boolean*'.
Generated:
createDestructionOccurrenceSpecification
[DestructionOccurrenceSpecification](../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html) createDestructionOccurrenceSpecification()
Returns a new object of class '*Destruction Occurrence Specification*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Destruction Occurrence Specification*'.
Generated:
createModel
[Model](../auxiliaryconstructs/mdmodels/Model.html) createModel()
Returns a new object of class '*Model*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Model*'.
Generated:
createClearVariableAction
[ClearVariableAction](../actions/mdstructuredactions/ClearVariableAction.html) createClearVariableAction()
Returns a new object of class '*Clear Variable Action*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Clear Variable Action*'.
Generated:
createBooleanTaggedValue
[BooleanTaggedValue](../classes/mdkernel/BooleanTaggedValue.html) createBooleanTaggedValue()
Returns a new object of class '*Boolean Tagged Value*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Boolean Tagged Value*'.
Generated:
createIntegerTaggedValue
[IntegerTaggedValue](../classes/mdkernel/IntegerTaggedValue.html) createIntegerTaggedValue()
Returns a new object of class '*Integer Tagged Value*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Integer Tagged Value*'.
Generated:
createRealTaggedValue
[RealTaggedValue](../classes/mdkernel/RealTaggedValue.html) createRealTaggedValue()
Returns a new object of class '*Real Tagged Value*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Real Tagged Value*'.
Generated:
createStringTaggedValue
[StringTaggedValue](../classes/mdkernel/StringTaggedValue.html) createStringTaggedValue()
Returns a new object of class '*String Tagged Value*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*String Tagged Value*'.
Generated:
createElementTaggedValue
[ElementTaggedValue](../classes/mdkernel/ElementTaggedValue.html) createElementTaggedValue()
Returns a new object of class '*Element Tagged Value*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Element Tagged Value*'.
Generated:
getUMLPackage
[UMLPackage](UMLPackage.html) getUMLPackage()
Returns the package supported by this factory.
 begin-user-doc 
 end-user-doc
Returns:
the package supported by this factory.
Generated:
setRepository
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)void setRepository([AbstractRepository](../../jmi/reflect/AbstractRepository.html) repository)
Deprecated.
The method should not be used. The method allows to set a project's repository to the factory
 and the factory creates elements in the project's repository. This creates following unwanted consequences:
 UMLFactory.eINSTANCE object overlives a project's repository instance.
 So after a project's closing it might be used to create elements in already closed project.
If a code sets a project's repository and forgets to change it then after switch
 to another project all elements will be created in the previous project.
It allows to create a deadlock condition. The code that sets the project's repository must take care that
 all elements in the project are already loaded and to assure that no elements can be unloaded.
 It makes the code difficult to implement.
Sets repository to the factory. All objects that will be created will be created in the
 specified repository.
Parameters:
`repository` - model objects repository.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.metadata</a></div>
<h1 class="title" title="Interface UMLFactory">Interface UMLFactory</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>org.eclipse.emf.ecore.EFactory</code>, <code>org.eclipse.emf.ecore.EModelElement</code>, <code>org.eclipse.emf.ecore.EObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">UMLFactory</span><span class="extends-implements">
extends org.eclipse.emf.ecore.EFactory</span></div>
<div class="block"><!-- begin-user-doc -->
 The <b>Factory</b> for the model.
 It provides a create method for each non-abstract class of the model.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="UMLPackage.html" title="interface in com.nomagic.uml2.ext.magicdraw.metadata"><code>UMLPackage</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a href="UMLFactory.html" title="interface in com.nomagic.uml2.ext.magicdraw.metadata">UMLFactory</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#eINSTANCE">eINSTANCE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The singleton instance of the factory.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createAbstraction()">createAbstraction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Abstraction</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createAcceptCallAction()">createAcceptCallAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Accept Call Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createAcceptEventAction()">createAcceptEventAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Accept Event Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createActionExecutionSpecification()">createActionExecutionSpecification</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Action Execution Specification</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createActionInputPin()">createActionInputPin</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Action Input Pin</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createActivity()">createActivity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Activity</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createActivityFinalNode()">createActivityFinalNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Activity Final Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createActivityParameterNode()">createActivityParameterNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Activity Parameter Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createActivityPartition()">createActivityPartition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Activity Partition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createActor()">createActor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Actor</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createAddStructuralFeatureValueAction()">createAddStructuralFeatureValueAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Add Structural Feature Value Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createAddVariableValueAction()">createAddVariableValueAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Add Variable Value Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEvent</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createAnyReceiveEvent()">createAnyReceiveEvent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Any Receive Event</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createArtifact()">createArtifact</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Artifact</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createAssociation()">createAssociation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Association</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createAssociationClass()">createAssociationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Association Class</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createBehaviorExecutionSpecification()">createBehaviorExecutionSpecification</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Behavior Execution Specification</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/BooleanTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BooleanTaggedValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createBooleanTaggedValue()">createBooleanTaggedValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Boolean Tagged Value</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createBroadcastSignalAction()">createBroadcastSignalAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Broadcast Signal Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCallBehaviorAction()">createCallBehaviorAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Call Behavior Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCallEvent()">createCallEvent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Call Event</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCallOperationAction()">createCallOperationAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Call Operation Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCentralBufferNode()">createCentralBufferNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Central Buffer Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createChangeEvent()">createChangeEvent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Change Event</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createClass()">createClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Class</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createClassifierTemplateParameter()">createClassifierTemplateParameter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Classifier Template Parameter</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createClause()">createClause</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Clause</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createClearAssociationAction()">createClearAssociationAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Clear Association Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createClearStructuralFeatureAction()">createClearStructuralFeatureAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Clear Structural Feature Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createClearVariableAction()">createClearVariableAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Clear Variable Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCollaboration()">createCollaboration</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Collaboration</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCollaborationUse()">createCollaborationUse</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Collaboration Use</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCombinedFragment()">createCombinedFragment</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Combined Fragment</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createComment()">createComment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Comment</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCommunicationPath()">createCommunicationPath</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Communication Path</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createComponent()">createComponent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Component</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createComponentRealization()">createComponentRealization</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Component Realization</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createConditionalNode()">createConditionalNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Conditional Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createConnectableElementTemplateParameter()">createConnectableElementTemplateParameter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Connectable Element Template Parameter</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createConnectionPointReference()">createConnectionPointReference</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Connection Point Reference</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createConnector()">createConnector</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Connector</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createConnectorEnd()">createConnectorEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Connector End</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragment</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createConsiderIgnoreFragment()">createConsiderIgnoreFragment</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Consider Ignore Fragment</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createConstraint()">createConstraint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Constraint</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Continuation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createContinuation()">createContinuation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Continuation</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createControlFlow()">createControlFlow</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Control Flow</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCreateLinkAction()">createCreateLinkAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Create Link Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCreateLinkObjectAction()">createCreateLinkObjectAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Create Link Object Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCreateObjectAction()">createCreateObjectAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Create Object Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDataStoreNode()">createDataStoreNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Data Store Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDataType()">createDataType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Data Type</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDecisionNode()">createDecisionNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Decision Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDependency()">createDependency</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Dependency</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDeployment()">createDeployment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Deployment</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDeploymentSpecification()">createDeploymentSpecification</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Deployment Specification</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDestroyLinkAction()">createDestroyLinkAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Destroy Link Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDestroyObjectAction()">createDestroyObjectAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Destroy Object Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDestructionOccurrenceSpecification()">createDestructionOccurrenceSpecification</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Destruction Occurrence Specification</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDevice()">createDevice</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Device</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDiagram()">createDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Diagram</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDuration()">createDuration</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Duration</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDurationConstraint()">createDurationConstraint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Duration Constraint</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDurationInterval()">createDurationInterval</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Duration Interval</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDurationObservation()">createDurationObservation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Duration Observation</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createElementImport()">createElementImport</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Element Import</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/ElementTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementTaggedValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createElementTaggedValue()">createElementTaggedValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Element Tagged Value</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createElementValue()">createElementValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Element Value</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createEnumeration()">createEnumeration</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Enumeration</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createEnumerationLiteral()">createEnumerationLiteral</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Enumeration Literal</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createExceptionHandler()">createExceptionHandler</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Exception Handler</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createExecutionEnvironment()">createExecutionEnvironment</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Execution Environment</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionOccurrenceSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createExecutionOccurrenceSpecification()">createExecutionOccurrenceSpecification</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Execution Occurrence Specification</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createExpansionNode()">createExpansionNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Expansion Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createExpansionRegion()">createExpansionRegion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Expansion Region</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createExpression()">createExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Expression</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createExtend()">createExtend</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Extend</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createExtension()">createExtension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Extension</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createExtensionEnd()">createExtensionEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Extension End</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPoint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createExtensionPoint()">createExtensionPoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Extension Point</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createFinalState()">createFinalState</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Final State</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createFlowFinalNode()">createFlowFinalNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Flow Final Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createForkNode()">createForkNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Fork Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createFunctionBehavior()">createFunctionBehavior</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Function Behavior</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createGate()">createGate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Gate</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createGeneralization()">createGeneralization</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Generalization</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createGeneralizationSet()">createGeneralizationSet</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Generalization Set</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">GeneralOrdering</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createGeneralOrdering()">createGeneralOrdering</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>General Ordering</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createImage()">createImage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Image</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Include</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInclude()">createInclude</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Include</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInformationFlow()">createInformationFlow</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Information Flow</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInformationItem()">createInformationItem</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Information Item</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInitialNode()">createInitialNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Initial Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInputPin()">createInputPin</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Input Pin</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInstanceSpecification()">createInstanceSpecification</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Instance Specification</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInstanceValue()">createInstanceValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Instance Value</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/IntegerTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">IntegerTaggedValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createIntegerTaggedValue()">createIntegerTaggedValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Integer Tagged Value</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInteraction()">createInteraction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Interaction</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInteractionConstraint()">createInteractionConstraint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Interaction Constraint</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInteractionOperand()">createInteractionOperand</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Interaction Operand</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInteractionUse()">createInteractionUse</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Interaction Use</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInterface()">createInterface</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Interface</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInterfaceRealization()">createInterfaceRealization</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Interface Realization</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInterruptibleActivityRegion()">createInterruptibleActivityRegion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Interruptible Activity Region</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createInterval()">createInterval</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Interval</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createIntervalConstraint()">createIntervalConstraint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Interval Constraint</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createJoinNode()">createJoinNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Join Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createLifeline()">createLifeline</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Lifeline</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createLinkEndCreationData()">createLinkEndCreationData</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Link End Creation Data</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createLinkEndData()">createLinkEndData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Link End Data</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createLinkEndDestructionData()">createLinkEndDestructionData</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Link End Destruction Data</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBoolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createLiteralBoolean()">createLiteralBoolean</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Literal Boolean</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralInteger</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createLiteralInteger()">createLiteralInteger</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Literal Integer</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNull</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createLiteralNull()">createLiteralNull</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Literal Null</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralReal</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createLiteralReal()">createLiteralReal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Literal Real</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralString</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createLiteralString()">createLiteralString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Literal String</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNatural</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createLiteralUnlimitedNatural()">createLiteralUnlimitedNatural</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Literal Unlimited Natural</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createLoopNode()">createLoopNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Loop Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Manifestation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createManifestation()">createManifestation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Manifestation</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createMergeNode()">createMergeNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Merge Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createMessage()">createMessage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Message</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createMessageOccurrenceSpecification()">createMessageOccurrenceSpecification</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Message Occurrence Specification</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createModel()">createModel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Model</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createNode()">createNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createObjectFlow()">createObjectFlow</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Object Flow</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createOccurrenceSpecification()">createOccurrenceSpecification</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Occurrence Specification</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createOpaqueAction()">createOpaqueAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Opaque Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createOpaqueBehavior()">createOpaqueBehavior</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Opaque Behavior</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createOpaqueExpression()">createOpaqueExpression</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Opaque Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createOperation()">createOperation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Operation</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createOperationTemplateParameter()">createOperationTemplateParameter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Operation Template Parameter</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createOutputPin()">createOutputPin</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Output Pin</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createPackage()">createPackage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Package</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createPackageImport()">createPackageImport</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Package Import</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageMerge</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createPackageMerge()">createPackageMerge</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Package Merge</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createParameter()">createParameter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Parameter</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createParameterSet()">createParameterSet</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Parameter Set</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createPartDecomposition()">createPartDecomposition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Part Decomposition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createPort()">createPort</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Port</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createPrimitiveType()">createPrimitiveType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Primitive Type</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createProfile()">createProfile</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Profile</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplication</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createProfileApplication()">createProfileApplication</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Profile Application</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createProperty()">createProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Property</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolConformance</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createProtocolConformance()">createProtocolConformance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Protocol Conformance</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createProtocolStateMachine()">createProtocolStateMachine</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Protocol State Machine</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createProtocolTransition()">createProtocolTransition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Protocol Transition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createPseudostate()">createPseudostate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Pseudostate</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createQualifierValue()">createQualifierValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Qualifier Value</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createRaiseExceptionAction()">createRaiseExceptionAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Raise Exception Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createReadExtentAction()">createReadExtentAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Read Extent Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createReadIsClassifiedObjectAction()">createReadIsClassifiedObjectAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Read Is Classified Object Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createReadLinkAction()">createReadLinkAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Read Link Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createReadLinkObjectEndAction()">createReadLinkObjectEndAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Read Link Object End Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createReadLinkObjectEndQualifierAction()">createReadLinkObjectEndQualifierAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Read Link Object End Qualifier Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createReadSelfAction()">createReadSelfAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Read Self Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createReadStructuralFeatureAction()">createReadStructuralFeatureAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Read Structural Feature Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createReadVariableAction()">createReadVariableAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Read Variable Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createRealization()">createRealization</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Realization</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/RealTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RealTaggedValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createRealTaggedValue()">createRealTaggedValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Real Tagged Value</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createReception()">createReception</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Reception</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createReclassifyObjectAction()">createReclassifyObjectAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Reclassify Object Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createRedefinableTemplateSignature()">createRedefinableTemplateSignature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Redefinable Template Signature</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createReduceAction()">createReduceAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Reduce Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createRegion()">createRegion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Region</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createRemoveStructuralFeatureValueAction()">createRemoveStructuralFeatureValueAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Remove Structural Feature Value Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createRemoveVariableValueAction()">createRemoveVariableValueAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Remove Variable Value Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createReplyAction()">createReplyAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Reply Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createSendObjectAction()">createSendObjectAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Send Object Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createSendSignalAction()">createSendSignalAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Send Signal Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createSequenceNode()">createSequenceNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Sequence Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createSignal()">createSignal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Signal</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createSignalEvent()">createSignalEvent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Signal Event</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createSlot()">createSlot</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Slot</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createStartClassifierBehaviorAction()">createStartClassifierBehaviorAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Start Classifier Behavior Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createStartObjectBehaviorAction()">createStartObjectBehaviorAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Start Object Behavior Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createState()">createState</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>State</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createStateInvariant()">createStateInvariant</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>State Invariant</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createStateMachine()">createStateMachine</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>State Machine</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createStereotype()">createStereotype</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Stereotype</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createStringExpression()">createStringExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>String Expression</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/StringTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StringTaggedValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createStringTaggedValue()">createStringTaggedValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>String Tagged Value</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createStructuredActivityNode()">createStructuredActivityNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Structured Activity Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createSubstitution()">createSubstitution</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Substitution</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTemplateBinding()">createTemplateBinding</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Template Binding</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTemplateParameter()">createTemplateParameter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Template Parameter</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTemplateParameterSubstitution()">createTemplateParameterSubstitution</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Template Parameter Substitution</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTemplateSignature()">createTemplateSignature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Template Signature</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTestIdentityAction()">createTestIdentityAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Test Identity Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTimeConstraint()">createTimeConstraint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Time Constraint</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEvent</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTimeEvent()">createTimeEvent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Time Event</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTimeExpression()">createTimeExpression</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Time Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTimeInterval()">createTimeInterval</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Time Interval</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTimeObservation()">createTimeObservation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Time Observation</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTransition()">createTransition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Transition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTrigger()">createTrigger</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Trigger</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createUnmarshallAction()">createUnmarshallAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Unmarshall Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Usage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createUsage()">createUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createUseCase()">createUseCase</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Use Case</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createValuePin()">createValuePin</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Value Pin</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createValueSpecificationAction()">createValueSpecificationAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Value Specification Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createVariable()">createVariable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Variable</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="UMLPackage.html" title="interface in com.nomagic.uml2.ext.magicdraw.metadata">UMLPackage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUMLPackage()">getUMLPackage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the package supported by this factory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#setRepository(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository)">setRepository</a><wbr/>(<a href="../../jmi/reflect/AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> repository)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">The method should not be used.</div>
</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EFactory">Methods inherited from interface org.eclipse.emf.ecore.EFactory</h3>
<code>convertToString, create, createFromString, getEPackage, setEPackage</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EModelElement">Methods inherited from interface org.eclipse.emf.ecore.EModelElement</h3>
<code>getEAnnotation, getEAnnotations</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="eINSTANCE">
<h3>eINSTANCE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a href="UMLFactory.html" title="interface in com.nomagic.uml2.ext.magicdraw.metadata">UMLFactory</a></span> <span class="element-name">eINSTANCE</span></div>
<div class="block">The singleton instance of the factory.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Generated:</dt>
</dl>
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
<section class="detail" id="createSendSignalAction()">
<h3>createSendSignalAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a></span> <span class="element-name">createSendSignalAction</span>()</div>
<div class="block">Returns a new object of class '<em>Send Signal Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Send Signal Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComment()">
<h3>createComment</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></span> <span class="element-name">createComment</span>()</div>
<div class="block">Returns a new object of class '<em>Comment</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Comment</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInstanceSpecification()">
<h3>createInstanceSpecification</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a></span> <span class="element-name">createInstanceSpecification</span>()</div>
<div class="block">Returns a new object of class '<em>Instance Specification</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Instance Specification</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateParameter()">
<h3>createTemplateParameter</h3>
<div class="member-signature"><span class="return-type"><a href="../auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></span> <span class="element-name">createTemplateParameter</span>()</div>
<div class="block">Returns a new object of class '<em>Template Parameter</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Template Parameter</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateSignature()">
<h3>createTemplateSignature</h3>
<div class="member-signature"><span class="return-type"><a href="../auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a></span> <span class="element-name">createTemplateSignature</span>()</div>
<div class="block">Returns a new object of class '<em>Template Signature</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Template Signature</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateBinding()">
<h3>createTemplateBinding</h3>
<div class="member-signature"><span class="return-type"><a href="../auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a></span> <span class="element-name">createTemplateBinding</span>()</div>
<div class="block">Returns a new object of class '<em>Template Binding</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Template Binding</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInformationFlow()">
<h3>createInformationFlow</h3>
<div class="member-signature"><span class="return-type"><a href="../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a></span> <span class="element-name">createInformationFlow</span>()</div>
<div class="block">Returns a new object of class '<em>Information Flow</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Information Flow</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createElementImport()">
<h3>createElementImport</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a></span> <span class="element-name">createElementImport</span>()</div>
<div class="block">Returns a new object of class '<em>Element Import</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Element Import</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProfile()">
<h3>createProfile</h3>
<div class="member-signature"><span class="return-type"><a href="../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></span> <span class="element-name">createProfile</span>()</div>
<div class="block">Returns a new object of class '<em>Profile</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Profile</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackage()">
<h3>createPackage</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">createPackage</span>()</div>
<div class="block">Returns a new object of class '<em>Package</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Package</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotype()">
<h3>createStereotype</h3>
<div class="member-signature"><span class="return-type"><a href="../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">createStereotype</span>()</div>
<div class="block">Returns a new object of class '<em>Stereotype</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Stereotype</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClass()">
<h3>createClass</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">createClass</span>()</div>
<div class="block">Returns a new object of class '<em>Class</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Class</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameter()">
<h3>createParameter</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></span> <span class="element-name">createParameter</span>()</div>
<div class="block">Returns a new object of class '<em>Parameter</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Parameter</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAssociation()">
<h3>createAssociation</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></span> <span class="element-name">createAssociation</span>()</div>
<div class="block">Returns a new object of class '<em>Association</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Association</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProperty()">
<h3>createProperty</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">createProperty</span>()</div>
<div class="block">Returns a new object of class '<em>Property</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Property</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlot()">
<h3>createSlot</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></span> <span class="element-name">createSlot</span>()</div>
<div class="block">Returns a new object of class '<em>Slot</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Slot</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInputPin()">
<h3>createInputPin</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></span> <span class="element-name">createInputPin</span>()</div>
<div class="block">Returns a new object of class '<em>Input Pin</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Input Pin</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createState()">
<h3>createState</h3>
<div class="member-signature"><span class="return-type"><a href="../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></span> <span class="element-name">createState</span>()</div>
<div class="block">Returns a new object of class '<em>State</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>State</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRegion()">
<h3>createRegion</h3>
<div class="member-signature"><span class="return-type"><a href="../statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a></span> <span class="element-name">createRegion</span>()</div>
<div class="block">Returns a new object of class '<em>Region</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Region</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateMachine()">
<h3>createStateMachine</h3>
<div class="member-signature"><span class="return-type"><a href="../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></span> <span class="element-name">createStateMachine</span>()</div>
<div class="block">Returns a new object of class '<em>State Machine</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>State Machine</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPseudostate()">
<h3>createPseudostate</h3>
<div class="member-signature"><span class="return-type"><a href="../statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a></span> <span class="element-name">createPseudostate</span>()</div>
<div class="block">Returns a new object of class '<em>Pseudostate</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Pseudostate</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectionPointReference()">
<h3>createConnectionPointReference</h3>
<div class="member-signature"><span class="return-type"><a href="../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a></span> <span class="element-name">createConnectionPointReference</span>()</div>
<div class="block">Returns a new object of class '<em>Connection Point Reference</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Connection Point Reference</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTransition()">
<h3>createTransition</h3>
<div class="member-signature"><span class="return-type"><a href="../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></span> <span class="element-name">createTransition</span>()</div>
<div class="block">Returns a new object of class '<em>Transition</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Transition</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConstraint()">
<h3>createConstraint</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">createConstraint</span>()</div>
<div class="block">Returns a new object of class '<em>Constraint</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Constraint</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperation()">
<h3>createOperation</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></span> <span class="element-name">createOperation</span>()</div>
<div class="block">Returns a new object of class '<em>Operation</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Operation</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameterSet()">
<h3>createParameterSet</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a></span> <span class="element-name">createParameterSet</span>()</div>
<div class="block">Returns a new object of class '<em>Parameter Set</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Parameter Set</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDataType()">
<h3>createDataType</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></span> <span class="element-name">createDataType</span>()</div>
<div class="block">Returns a new object of class '<em>Data Type</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Data Type</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInterface()">
<h3>createInterface</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></span> <span class="element-name">createInterface</span>()</div>
<div class="block">Returns a new object of class '<em>Interface</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Interface</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReception()">
<h3>createReception</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a></span> <span class="element-name">createReception</span>()</div>
<div class="block">Returns a new object of class '<em>Reception</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Reception</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSignal()">
<h3>createSignal</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></span> <span class="element-name">createSignal</span>()</div>
<div class="block">Returns a new object of class '<em>Signal</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Signal</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBroadcastSignalAction()">
<h3>createBroadcastSignalAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a></span> <span class="element-name">createBroadcastSignalAction</span>()</div>
<div class="block">Returns a new object of class '<em>Broadcast Signal Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Broadcast Signal Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSignalEvent()">
<h3>createSignalEvent</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a></span> <span class="element-name">createSignalEvent</span>()</div>
<div class="block">Returns a new object of class '<em>Signal Event</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Signal Event</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTrigger()">
<h3>createTrigger</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a></span> <span class="element-name">createTrigger</span>()</div>
<div class="block">Returns a new object of class '<em>Trigger</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Trigger</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPort()">
<h3>createPort</h3>
<div class="member-signature"><span class="return-type"><a href="../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a></span> <span class="element-name">createPort</span>()</div>
<div class="block">Returns a new object of class '<em>Port</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Port</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProtocolStateMachine()">
<h3>createProtocolStateMachine</h3>
<div class="member-signature"><span class="return-type"><a href="../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></span> <span class="element-name">createProtocolStateMachine</span>()</div>
<div class="block">Returns a new object of class '<em>Protocol State Machine</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Protocol State Machine</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProtocolConformance()">
<h3>createProtocolConformance</h3>
<div class="member-signature"><span class="return-type"><a href="../statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolConformance</a></span> <span class="element-name">createProtocolConformance</span>()</div>
<div class="block">Returns a new object of class '<em>Protocol Conformance</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Protocol Conformance</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnector()">
<h3>createConnector</h3>
<div class="member-signature"><span class="return-type"><a href="../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a></span> <span class="element-name">createConnector</span>()</div>
<div class="block">Returns a new object of class '<em>Connector</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Connector</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectorEnd()">
<h3>createConnectorEnd</h3>
<div class="member-signature"><span class="return-type"><a href="../compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a></span> <span class="element-name">createConnectorEnd</span>()</div>
<div class="block">Returns a new object of class '<em>Connector End</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Connector End</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectableElementTemplateParameter()">
<h3>createConnectableElementTemplateParameter</h3>
<div class="member-signature"><span class="return-type"><a href="../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a></span> <span class="element-name">createConnectableElementTemplateParameter</span>()</div>
<div class="block">Returns a new object of class '<em>Connectable Element Template Parameter</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Connectable Element Template Parameter</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCollaboration()">
<h3>createCollaboration</h3>
<div class="member-signature"><span class="return-type"><a href="../compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a></span> <span class="element-name">createCollaboration</span>()</div>
<div class="block">Returns a new object of class '<em>Collaboration</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Collaboration</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCollaborationUse()">
<h3>createCollaborationUse</h3>
<div class="member-signature"><span class="return-type"><a href="../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a></span> <span class="element-name">createCollaborationUse</span>()</div>
<div class="block">Returns a new object of class '<em>Collaboration Use</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Collaboration Use</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDependency()">
<h3>createDependency</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a></span> <span class="element-name">createDependency</span>()</div>
<div class="block">Returns a new object of class '<em>Dependency</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Dependency</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLifeline()">
<h3>createLifeline</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a></span> <span class="element-name">createLifeline</span>()</div>
<div class="block">Returns a new object of class '<em>Lifeline</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Lifeline</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteraction()">
<h3>createInteraction</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></span> <span class="element-name">createInteraction</span>()</div>
<div class="block">Returns a new object of class '<em>Interaction</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Interaction</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGate()">
<h3>createGate</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a></span> <span class="element-name">createGate</span>()</div>
<div class="block">Returns a new object of class '<em>Gate</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Gate</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMessage()">
<h3>createMessage</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></span> <span class="element-name">createMessage</span>()</div>
<div class="block">Returns a new object of class '<em>Message</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Message</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionUse()">
<h3>createInteractionUse</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a></span> <span class="element-name">createInteractionUse</span>()</div>
<div class="block">Returns a new object of class '<em>Interaction Use</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Interaction Use</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCombinedFragment()">
<h3>createCombinedFragment</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a></span> <span class="element-name">createCombinedFragment</span>()</div>
<div class="block">Returns a new object of class '<em>Combined Fragment</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Combined Fragment</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionOperand()">
<h3>createInteractionOperand</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a></span> <span class="element-name">createInteractionOperand</span>()</div>
<div class="block">Returns a new object of class '<em>Interaction Operand</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Interaction Operand</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionConstraint()">
<h3>createInteractionConstraint</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></span> <span class="element-name">createInteractionConstraint</span>()</div>
<div class="block">Returns a new object of class '<em>Interaction Constraint</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Interaction Constraint</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGeneralOrdering()">
<h3>createGeneralOrdering</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">GeneralOrdering</a></span> <span class="element-name">createGeneralOrdering</span>()</div>
<div class="block">Returns a new object of class '<em>General Ordering</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>General Ordering</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOccurrenceSpecification()">
<h3>createOccurrenceSpecification</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecification</a></span> <span class="element-name">createOccurrenceSpecification</span>()</div>
<div class="block">Returns a new object of class '<em>Occurrence Specification</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Occurrence Specification</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExecutionOccurrenceSpecification()">
<h3>createExecutionOccurrenceSpecification</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionOccurrenceSpecification</a></span> <span class="element-name">createExecutionOccurrenceSpecification</span>()</div>
<div class="block">Returns a new object of class '<em>Execution Occurrence Specification</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Execution Occurrence Specification</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPartDecomposition()">
<h3>createPartDecomposition</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a></span> <span class="element-name">createPartDecomposition</span>()</div>
<div class="block">Returns a new object of class '<em>Part Decomposition</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Part Decomposition</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateInvariant()">
<h3>createStateInvariant</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a></span> <span class="element-name">createStateInvariant</span>()</div>
<div class="block">Returns a new object of class '<em>State Invariant</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>State Invariant</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReplyAction()">
<h3>createReplyAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></span> <span class="element-name">createReplyAction</span>()</div>
<div class="block">Returns a new object of class '<em>Reply Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Reply Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAcceptEventAction()">
<h3>createAcceptEventAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></span> <span class="element-name">createAcceptEventAction</span>()</div>
<div class="block">Returns a new object of class '<em>Accept Event Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Accept Event Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOutputPin()">
<h3>createOutputPin</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></span> <span class="element-name">createOutputPin</span>()</div>
<div class="block">Returns a new object of class '<em>Output Pin</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Output Pin</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClause()">
<h3>createClause</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a></span> <span class="element-name">createClause</span>()</div>
<div class="block">Returns a new object of class '<em>Clause</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Clause</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConditionalNode()">
<h3>createConditionalNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></span> <span class="element-name">createConditionalNode</span>()</div>
<div class="block">Returns a new object of class '<em>Conditional Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Conditional Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStructuredActivityNode()">
<h3>createStructuredActivityNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></span> <span class="element-name">createStructuredActivityNode</span>()</div>
<div class="block">Returns a new object of class '<em>Structured Activity Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Structured Activity Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivity()">
<h3>createActivity</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></span> <span class="element-name">createActivity</span>()</div>
<div class="block">Returns a new object of class '<em>Activity</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Activity</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityPartition()">
<h3>createActivityPartition</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a></span> <span class="element-name">createActivityPartition</span>()</div>
<div class="block">Returns a new object of class '<em>Activity Partition</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Activity Partition</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createVariable()">
<h3>createVariable</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a></span> <span class="element-name">createVariable</span>()</div>
<div class="block">Returns a new object of class '<em>Variable</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Variable</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInterruptibleActivityRegion()">
<h3>createInterruptibleActivityRegion</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a></span> <span class="element-name">createInterruptibleActivityRegion</span>()</div>
<div class="block">Returns a new object of class '<em>Interruptible Activity Region</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Interruptible Activity Region</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLoopNode()">
<h3>createLoopNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></span> <span class="element-name">createLoopNode</span>()</div>
<div class="block">Returns a new object of class '<em>Loop Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Loop Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOpaqueAction()">
<h3>createOpaqueAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></span> <span class="element-name">createOpaqueAction</span>()</div>
<div class="block">Returns a new object of class '<em>Opaque Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Opaque Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClearStructuralFeatureAction()">
<h3>createClearStructuralFeatureAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a></span> <span class="element-name">createClearStructuralFeatureAction</span>()</div>
<div class="block">Returns a new object of class '<em>Clear Structural Feature Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Clear Structural Feature Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCreateLinkObjectAction()">
<h3>createCreateLinkObjectAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a></span> <span class="element-name">createCreateLinkObjectAction</span>()</div>
<div class="block">Returns a new object of class '<em>Create Link Object Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Create Link Object Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCreateLinkAction()">
<h3>createCreateLinkAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a></span> <span class="element-name">createCreateLinkAction</span>()</div>
<div class="block">Returns a new object of class '<em>Create Link Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Create Link Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLinkEndData()">
<h3>createLinkEndData</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a></span> <span class="element-name">createLinkEndData</span>()</div>
<div class="block">Returns a new object of class '<em>Link End Data</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Link End Data</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createQualifierValue()">
<h3>createQualifierValue</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a></span> <span class="element-name">createQualifierValue</span>()</div>
<div class="block">Returns a new object of class '<em>Qualifier Value</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Qualifier Value</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLinkEndCreationData()">
<h3>createLinkEndCreationData</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a></span> <span class="element-name">createLinkEndCreationData</span>()</div>
<div class="block">Returns a new object of class '<em>Link End Creation Data</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Link End Creation Data</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCreateObjectAction()">
<h3>createCreateObjectAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a></span> <span class="element-name">createCreateObjectAction</span>()</div>
<div class="block">Returns a new object of class '<em>Create Object Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Create Object Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadExtentAction()">
<h3>createReadExtentAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a></span> <span class="element-name">createReadExtentAction</span>()</div>
<div class="block">Returns a new object of class '<em>Read Extent Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Read Extent Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadIsClassifiedObjectAction()">
<h3>createReadIsClassifiedObjectAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></span> <span class="element-name">createReadIsClassifiedObjectAction</span>()</div>
<div class="block">Returns a new object of class '<em>Read Is Classified Object Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Read Is Classified Object Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadLinkAction()">
<h3>createReadLinkAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a></span> <span class="element-name">createReadLinkAction</span>()</div>
<div class="block">Returns a new object of class '<em>Read Link Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Read Link Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadLinkObjectEndAction()">
<h3>createReadLinkObjectEndAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></span> <span class="element-name">createReadLinkObjectEndAction</span>()</div>
<div class="block">Returns a new object of class '<em>Read Link Object End Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Read Link Object End Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadLinkObjectEndQualifierAction()">
<h3>createReadLinkObjectEndQualifierAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></span> <span class="element-name">createReadLinkObjectEndQualifierAction</span>()</div>
<div class="block">Returns a new object of class '<em>Read Link Object End Qualifier Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Read Link Object End Qualifier Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadSelfAction()">
<h3>createReadSelfAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a></span> <span class="element-name">createReadSelfAction</span>()</div>
<div class="block">Returns a new object of class '<em>Read Self Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Read Self Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadStructuralFeatureAction()">
<h3>createReadStructuralFeatureAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a></span> <span class="element-name">createReadStructuralFeatureAction</span>()</div>
<div class="block">Returns a new object of class '<em>Read Structural Feature Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Read Structural Feature Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadVariableAction()">
<h3>createReadVariableAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a></span> <span class="element-name">createReadVariableAction</span>()</div>
<div class="block">Returns a new object of class '<em>Read Variable Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Read Variable Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReduceAction()">
<h3>createReduceAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></span> <span class="element-name">createReduceAction</span>()</div>
<div class="block">Returns a new object of class '<em>Reduce Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Reduce Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTestIdentityAction()">
<h3>createTestIdentityAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></span> <span class="element-name">createTestIdentityAction</span>()</div>
<div class="block">Returns a new object of class '<em>Test Identity Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Test Identity Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUnmarshallAction()">
<h3>createUnmarshallAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></span> <span class="element-name">createUnmarshallAction</span>()</div>
<div class="block">Returns a new object of class '<em>Unmarshall Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Unmarshall Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueSpecificationAction()">
<h3>createValueSpecificationAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></span> <span class="element-name">createValueSpecificationAction</span>()</div>
<div class="block">Returns a new object of class '<em>Value Specification Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Value Specification Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAcceptCallAction()">
<h3>createAcceptCallAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a></span> <span class="element-name">createAcceptCallAction</span>()</div>
<div class="block">Returns a new object of class '<em>Accept Call Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Accept Call Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInterfaceRealization()">
<h3>createInterfaceRealization</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a></span> <span class="element-name">createInterfaceRealization</span>()</div>
<div class="block">Returns a new object of class '<em>Interface Realization</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Interface Realization</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRealization()">
<h3>createRealization</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a></span> <span class="element-name">createRealization</span>()</div>
<div class="block">Returns a new object of class '<em>Realization</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Realization</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAbstraction()">
<h3>createAbstraction</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a></span> <span class="element-name">createAbstraction</span>()</div>
<div class="block">Returns a new object of class '<em>Abstraction</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Abstraction</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOpaqueExpression()">
<h3>createOpaqueExpression</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a></span> <span class="element-name">createOpaqueExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Opaque Expression</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Opaque Expression</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComponent()">
<h3>createComponent</h3>
<div class="member-signature"><span class="return-type"><a href="../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a></span> <span class="element-name">createComponent</span>()</div>
<div class="block">Returns a new object of class '<em>Component</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Component</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComponentRealization()">
<h3>createComponentRealization</h3>
<div class="member-signature"><span class="return-type"><a href="../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a></span> <span class="element-name">createComponentRealization</span>()</div>
<div class="block">Returns a new object of class '<em>Component Realization</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Component Realization</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperationTemplateParameter()">
<h3>createOperationTemplateParameter</h3>
<div class="member-signature"><span class="return-type"><a href="../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a></span> <span class="element-name">createOperationTemplateParameter</span>()</div>
<div class="block">Returns a new object of class '<em>Operation Template Parameter</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Operation Template Parameter</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCallEvent()">
<h3>createCallEvent</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a></span> <span class="element-name">createCallEvent</span>()</div>
<div class="block">Returns a new object of class '<em>Call Event</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Call Event</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCallOperationAction()">
<h3>createCallOperationAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a></span> <span class="element-name">createCallOperationAction</span>()</div>
<div class="block">Returns a new object of class '<em>Call Operation Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Call Operation Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createArtifact()">
<h3>createArtifact</h3>
<div class="member-signature"><span class="return-type"><a href="../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></span> <span class="element-name">createArtifact</span>()</div>
<div class="block">Returns a new object of class '<em>Artifact</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Artifact</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDeployment()">
<h3>createDeployment</h3>
<div class="member-signature"><span class="return-type"><a href="../deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a></span> <span class="element-name">createDeployment</span>()</div>
<div class="block">Returns a new object of class '<em>Deployment</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Deployment</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDeploymentSpecification()">
<h3>createDeploymentSpecification</h3>
<div class="member-signature"><span class="return-type"><a href="../deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a></span> <span class="element-name">createDeploymentSpecification</span>()</div>
<div class="block">Returns a new object of class '<em>Deployment Specification</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Deployment Specification</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createManifestation()">
<h3>createManifestation</h3>
<div class="member-signature"><span class="return-type"><a href="../deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Manifestation</a></span> <span class="element-name">createManifestation</span>()</div>
<div class="block">Returns a new object of class '<em>Manifestation</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Manifestation</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProtocolTransition()">
<h3>createProtocolTransition</h3>
<div class="member-signature"><span class="return-type"><a href="../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></span> <span class="element-name">createProtocolTransition</span>()</div>
<div class="block">Returns a new object of class '<em>Protocol Transition</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Protocol Transition</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExtend()">
<h3>createExtend</h3>
<div class="member-signature"><span class="return-type"><a href="../mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a></span> <span class="element-name">createExtend</span>()</div>
<div class="block">Returns a new object of class '<em>Extend</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Extend</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUseCase()">
<h3>createUseCase</h3>
<div class="member-signature"><span class="return-type"><a href="../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></span> <span class="element-name">createUseCase</span>()</div>
<div class="block">Returns a new object of class '<em>Use Case</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Use Case</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExtensionPoint()">
<h3>createExtensionPoint</h3>
<div class="member-signature"><span class="return-type"><a href="../mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPoint</a></span> <span class="element-name">createExtensionPoint</span>()</div>
<div class="block">Returns a new object of class '<em>Extension Point</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Extension Point</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInclude()">
<h3>createInclude</h3>
<div class="member-signature"><span class="return-type"><a href="../mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Include</a></span> <span class="element-name">createInclude</span>()</div>
<div class="block">Returns a new object of class '<em>Include</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Include</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExceptionHandler()">
<h3>createExceptionHandler</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a></span> <span class="element-name">createExceptionHandler</span>()</div>
<div class="block">Returns a new object of class '<em>Exception Handler</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Exception Handler</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLinkEndDestructionData()">
<h3>createLinkEndDestructionData</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a></span> <span class="element-name">createLinkEndDestructionData</span>()</div>
<div class="block">Returns a new object of class '<em>Link End Destruction Data</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Link End Destruction Data</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDestroyLinkAction()">
<h3>createDestroyLinkAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a></span> <span class="element-name">createDestroyLinkAction</span>()</div>
<div class="block">Returns a new object of class '<em>Destroy Link Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Destroy Link Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRaiseExceptionAction()">
<h3>createRaiseExceptionAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a></span> <span class="element-name">createRaiseExceptionAction</span>()</div>
<div class="block">Returns a new object of class '<em>Raise Exception Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Raise Exception Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAddStructuralFeatureValueAction()">
<h3>createAddStructuralFeatureValueAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a></span> <span class="element-name">createAddStructuralFeatureValueAction</span>()</div>
<div class="block">Returns a new object of class '<em>Add Structural Feature Value Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Add Structural Feature Value Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAddVariableValueAction()">
<h3>createAddVariableValueAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a></span> <span class="element-name">createAddVariableValueAction</span>()</div>
<div class="block">Returns a new object of class '<em>Add Variable Value Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Add Variable Value Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClearAssociationAction()">
<h3>createClearAssociationAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a></span> <span class="element-name">createClearAssociationAction</span>()</div>
<div class="block">Returns a new object of class '<em>Clear Association Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Clear Association Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReclassifyObjectAction()">
<h3>createReclassifyObjectAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a></span> <span class="element-name">createReclassifyObjectAction</span>()</div>
<div class="block">Returns a new object of class '<em>Reclassify Object Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Reclassify Object Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStartClassifierBehaviorAction()">
<h3>createStartClassifierBehaviorAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a></span> <span class="element-name">createStartClassifierBehaviorAction</span>()</div>
<div class="block">Returns a new object of class '<em>Start Classifier Behavior Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Start Classifier Behavior Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStartObjectBehaviorAction()">
<h3>createStartObjectBehaviorAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a></span> <span class="element-name">createStartObjectBehaviorAction</span>()</div>
<div class="block">Returns a new object of class '<em>Start Object Behavior Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Start Object Behavior Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRemoveStructuralFeatureValueAction()">
<h3>createRemoveStructuralFeatureValueAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a></span> <span class="element-name">createRemoveStructuralFeatureValueAction</span>()</div>
<div class="block">Returns a new object of class '<em>Remove Structural Feature Value Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Remove Structural Feature Value Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRemoveVariableValueAction()">
<h3>createRemoveVariableValueAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a></span> <span class="element-name">createRemoveVariableValueAction</span>()</div>
<div class="block">Returns a new object of class '<em>Remove Variable Value Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Remove Variable Value Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSendObjectAction()">
<h3>createSendObjectAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></span> <span class="element-name">createSendObjectAction</span>()</div>
<div class="block">Returns a new object of class '<em>Send Object Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Send Object Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDestroyObjectAction()">
<h3>createDestroyObjectAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a></span> <span class="element-name">createDestroyObjectAction</span>()</div>
<div class="block">Returns a new object of class '<em>Destroy Object Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Destroy Object Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createChangeEvent()">
<h3>createChangeEvent</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a></span> <span class="element-name">createChangeEvent</span>()</div>
<div class="block">Returns a new object of class '<em>Change Event</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Change Event</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDuration()">
<h3>createDuration</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></span> <span class="element-name">createDuration</span>()</div>
<div class="block">Returns a new object of class '<em>Duration</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Duration</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeExpression()">
<h3>createTimeExpression</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></span> <span class="element-name">createTimeExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Time Expression</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Time Expression</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeInterval()">
<h3>createTimeInterval</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a></span> <span class="element-name">createTimeInterval</span>()</div>
<div class="block">Returns a new object of class '<em>Time Interval</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Time Interval</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInterval()">
<h3>createInterval</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></span> <span class="element-name">createInterval</span>()</div>
<div class="block">Returns a new object of class '<em>Interval</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Interval</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIntervalConstraint()">
<h3>createIntervalConstraint</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a></span> <span class="element-name">createIntervalConstraint</span>()</div>
<div class="block">Returns a new object of class '<em>Interval Constraint</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Interval Constraint</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeConstraint()">
<h3>createTimeConstraint</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a></span> <span class="element-name">createTimeConstraint</span>()</div>
<div class="block">Returns a new object of class '<em>Time Constraint</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Time Constraint</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeEvent()">
<h3>createTimeEvent</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEvent</a></span> <span class="element-name">createTimeEvent</span>()</div>
<div class="block">Returns a new object of class '<em>Time Event</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Time Event</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDurationInterval()">
<h3>createDurationInterval</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a></span> <span class="element-name">createDurationInterval</span>()</div>
<div class="block">Returns a new object of class '<em>Duration Interval</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Duration Interval</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDurationConstraint()">
<h3>createDurationConstraint</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a></span> <span class="element-name">createDurationConstraint</span>()</div>
<div class="block">Returns a new object of class '<em>Duration Constraint</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Duration Constraint</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createJoinNode()">
<h3>createJoinNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a></span> <span class="element-name">createJoinNode</span>()</div>
<div class="block">Returns a new object of class '<em>Join Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Join Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExpression()">
<h3>createExpression</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a></span> <span class="element-name">createExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Expression</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Expression</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValuePin()">
<h3>createValuePin</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a></span> <span class="element-name">createValuePin</span>()</div>
<div class="block">Returns a new object of class '<em>Value Pin</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Value Pin</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityParameterNode()">
<h3>createActivityParameterNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a></span> <span class="element-name">createActivityParameterNode</span>()</div>
<div class="block">Returns a new object of class '<em>Activity Parameter Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Activity Parameter Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBehaviorExecutionSpecification()">
<h3>createBehaviorExecutionSpecification</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecification</a></span> <span class="element-name">createBehaviorExecutionSpecification</span>()</div>
<div class="block">Returns a new object of class '<em>Behavior Execution Specification</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Behavior Execution Specification</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCallBehaviorAction()">
<h3>createCallBehaviorAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a></span> <span class="element-name">createCallBehaviorAction</span>()</div>
<div class="block">Returns a new object of class '<em>Call Behavior Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Call Behavior Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDecisionNode()">
<h3>createDecisionNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a></span> <span class="element-name">createDecisionNode</span>()</div>
<div class="block">Returns a new object of class '<em>Decision Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Decision Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createObjectFlow()">
<h3>createObjectFlow</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a></span> <span class="element-name">createObjectFlow</span>()</div>
<div class="block">Returns a new object of class '<em>Object Flow</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Object Flow</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExtension()">
<h3>createExtension</h3>
<div class="member-signature"><span class="return-type"><a href="../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></span> <span class="element-name">createExtension</span>()</div>
<div class="block">Returns a new object of class '<em>Extension</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Extension</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExtensionEnd()">
<h3>createExtensionEnd</h3>
<div class="member-signature"><span class="return-type"><a href="../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></span> <span class="element-name">createExtensionEnd</span>()</div>
<div class="block">Returns a new object of class '<em>Extension End</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Extension End</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImage()">
<h3>createImage</h3>
<div class="member-signature"><span class="return-type"><a href="../mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a></span> <span class="element-name">createImage</span>()</div>
<div class="block">Returns a new object of class '<em>Image</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Image</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackageMerge()">
<h3>createPackageMerge</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageMerge</a></span> <span class="element-name">createPackageMerge</span>()</div>
<div class="block">Returns a new object of class '<em>Package Merge</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Package Merge</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProfileApplication()">
<h3>createProfileApplication</h3>
<div class="member-signature"><span class="return-type"><a href="../mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplication</a></span> <span class="element-name">createProfileApplication</span>()</div>
<div class="block">Returns a new object of class '<em>Profile Application</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Profile Application</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackageImport()">
<h3>createPackageImport</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a></span> <span class="element-name">createPackageImport</span>()</div>
<div class="block">Returns a new object of class '<em>Package Import</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Package Import</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDiagram()">
<h3>createDiagram</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></span> <span class="element-name">createDiagram</span>()</div>
<div class="block">Returns a new object of class '<em>Diagram</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Diagram</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGeneralization()">
<h3>createGeneralization</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a></span> <span class="element-name">createGeneralization</span>()</div>
<div class="block">Returns a new object of class '<em>Generalization</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Generalization</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGeneralizationSet()">
<h3>createGeneralizationSet</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a></span> <span class="element-name">createGeneralizationSet</span>()</div>
<div class="block">Returns a new object of class '<em>Generalization Set</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Generalization Set</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRedefinableTemplateSignature()">
<h3>createRedefinableTemplateSignature</h3>
<div class="member-signature"><span class="return-type"><a href="../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a></span> <span class="element-name">createRedefinableTemplateSignature</span>()</div>
<div class="block">Returns a new object of class '<em>Redefinable Template Signature</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Redefinable Template Signature</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSubstitution()">
<h3>createSubstitution</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a></span> <span class="element-name">createSubstitution</span>()</div>
<div class="block">Returns a new object of class '<em>Substitution</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Substitution</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClassifierTemplateParameter()">
<h3>createClassifierTemplateParameter</h3>
<div class="member-signature"><span class="return-type"><a href="../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a></span> <span class="element-name">createClassifierTemplateParameter</span>()</div>
<div class="block">Returns a new object of class '<em>Classifier Template Parameter</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Classifier Template Parameter</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInformationItem()">
<h3>createInformationItem</h3>
<div class="member-signature"><span class="return-type"><a href="../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a></span> <span class="element-name">createInformationItem</span>()</div>
<div class="block">Returns a new object of class '<em>Information Item</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Information Item</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateParameterSubstitution()">
<h3>createTemplateParameterSubstitution</h3>
<div class="member-signature"><span class="return-type"><a href="../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a></span> <span class="element-name">createTemplateParameterSubstitution</span>()</div>
<div class="block">Returns a new object of class '<em>Template Parameter Substitution</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Template Parameter Substitution</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInstanceValue()">
<h3>createInstanceValue</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a></span> <span class="element-name">createInstanceValue</span>()</div>
<div class="block">Returns a new object of class '<em>Instance Value</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Instance Value</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createElementValue()">
<h3>createElementValue</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a></span> <span class="element-name">createElementValue</span>()</div>
<div class="block">Returns a new object of class '<em>Element Value</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Element Value</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStringExpression()">
<h3>createStringExpression</h3>
<div class="member-signature"><span class="return-type"><a href="../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a></span> <span class="element-name">createStringExpression</span>()</div>
<div class="block">Returns a new object of class '<em>String Expression</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>String Expression</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDurationObservation()">
<h3>createDurationObservation</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a></span> <span class="element-name">createDurationObservation</span>()</div>
<div class="block">Returns a new object of class '<em>Duration Observation</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Duration Observation</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeObservation()">
<h3>createTimeObservation</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a></span> <span class="element-name">createTimeObservation</span>()</div>
<div class="block">Returns a new object of class '<em>Time Observation</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Time Observation</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConsiderIgnoreFragment()">
<h3>createConsiderIgnoreFragment</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragment</a></span> <span class="element-name">createConsiderIgnoreFragment</span>()</div>
<div class="block">Returns a new object of class '<em>Consider Ignore Fragment</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Consider Ignore Fragment</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSequenceNode()">
<h3>createSequenceNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></span> <span class="element-name">createSequenceNode</span>()</div>
<div class="block">Returns a new object of class '<em>Sequence Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Sequence Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActionExecutionSpecification()">
<h3>createActionExecutionSpecification</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecification</a></span> <span class="element-name">createActionExecutionSpecification</span>()</div>
<div class="block">Returns a new object of class '<em>Action Execution Specification</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Action Execution Specification</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActionInputPin()">
<h3>createActionInputPin</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a></span> <span class="element-name">createActionInputPin</span>()</div>
<div class="block">Returns a new object of class '<em>Action Input Pin</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Action Input Pin</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralString()">
<h3>createLiteralString</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralString</a></span> <span class="element-name">createLiteralString</span>()</div>
<div class="block">Returns a new object of class '<em>Literal String</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Literal String</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDataStoreNode()">
<h3>createDataStoreNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNode</a></span> <span class="element-name">createDataStoreNode</span>()</div>
<div class="block">Returns a new object of class '<em>Data Store Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Data Store Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCentralBufferNode()">
<h3>createCentralBufferNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNode</a></span> <span class="element-name">createCentralBufferNode</span>()</div>
<div class="block">Returns a new object of class '<em>Central Buffer Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Central Buffer Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInitialNode()">
<h3>createInitialNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNode</a></span> <span class="element-name">createInitialNode</span>()</div>
<div class="block">Returns a new object of class '<em>Initial Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Initial Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDevice()">
<h3>createDevice</h3>
<div class="member-signature"><span class="return-type"><a href="../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a></span> <span class="element-name">createDevice</span>()</div>
<div class="block">Returns a new object of class '<em>Device</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Device</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNode()">
<h3>createNode</h3>
<div class="member-signature"><span class="return-type"><a href="../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a></span> <span class="element-name">createNode</span>()</div>
<div class="block">Returns a new object of class '<em>Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAssociationClass()">
<h3>createAssociationClass</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a></span> <span class="element-name">createAssociationClass</span>()</div>
<div class="block">Returns a new object of class '<em>Association Class</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Association Class</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActor()">
<h3>createActor</h3>
<div class="member-signature"><span class="return-type"><a href="../mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a></span> <span class="element-name">createActor</span>()</div>
<div class="block">Returns a new object of class '<em>Actor</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Actor</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExecutionEnvironment()">
<h3>createExecutionEnvironment</h3>
<div class="member-signature"><span class="return-type"><a href="../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a></span> <span class="element-name">createExecutionEnvironment</span>()</div>
<div class="block">Returns a new object of class '<em>Execution Environment</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Execution Environment</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFunctionBehavior()">
<h3>createFunctionBehavior</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a></span> <span class="element-name">createFunctionBehavior</span>()</div>
<div class="block">Returns a new object of class '<em>Function Behavior</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Function Behavior</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOpaqueBehavior()">
<h3>createOpaqueBehavior</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a></span> <span class="element-name">createOpaqueBehavior</span>()</div>
<div class="block">Returns a new object of class '<em>Opaque Behavior</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Opaque Behavior</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityFinalNode()">
<h3>createActivityFinalNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNode</a></span> <span class="element-name">createActivityFinalNode</span>()</div>
<div class="block">Returns a new object of class '<em>Activity Final Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Activity Final Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFlowFinalNode()">
<h3>createFlowFinalNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNode</a></span> <span class="element-name">createFlowFinalNode</span>()</div>
<div class="block">Returns a new object of class '<em>Flow Final Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Flow Final Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralReal()">
<h3>createLiteralReal</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralReal</a></span> <span class="element-name">createLiteralReal</span>()</div>
<div class="block">Returns a new object of class '<em>Literal Real</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Literal Real</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createForkNode()">
<h3>createForkNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNode</a></span> <span class="element-name">createForkNode</span>()</div>
<div class="block">Returns a new object of class '<em>Fork Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Fork Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createControlFlow()">
<h3>createControlFlow</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a></span> <span class="element-name">createControlFlow</span>()</div>
<div class="block">Returns a new object of class '<em>Control Flow</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Control Flow</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUsage()">
<h3>createUsage</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Usage</a></span> <span class="element-name">createUsage</span>()</div>
<div class="block">Returns a new object of class '<em>Usage</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Usage</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralUnlimitedNatural()">
<h3>createLiteralUnlimitedNatural</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNatural</a></span> <span class="element-name">createLiteralUnlimitedNatural</span>()</div>
<div class="block">Returns a new object of class '<em>Literal Unlimited Natural</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Literal Unlimited Natural</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralInteger()">
<h3>createLiteralInteger</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralInteger</a></span> <span class="element-name">createLiteralInteger</span>()</div>
<div class="block">Returns a new object of class '<em>Literal Integer</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Literal Integer</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEnumeration()">
<h3>createEnumeration</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">createEnumeration</span>()</div>
<div class="block">Returns a new object of class '<em>Enumeration</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Enumeration</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEnumerationLiteral()">
<h3>createEnumerationLiteral</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">createEnumerationLiteral</span>()</div>
<div class="block">Returns a new object of class '<em>Enumeration Literal</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Enumeration Literal</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExpansionNode()">
<h3>createExpansionNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNode</a></span> <span class="element-name">createExpansionNode</span>()</div>
<div class="block">Returns a new object of class '<em>Expansion Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Expansion Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExpansionRegion()">
<h3>createExpansionRegion</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a></span> <span class="element-name">createExpansionRegion</span>()</div>
<div class="block">Returns a new object of class '<em>Expansion Region</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Expansion Region</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCommunicationPath()">
<h3>createCommunicationPath</h3>
<div class="member-signature"><span class="return-type"><a href="../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a></span> <span class="element-name">createCommunicationPath</span>()</div>
<div class="block">Returns a new object of class '<em>Communication Path</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Communication Path</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPrimitiveType()">
<h3>createPrimitiveType</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a></span> <span class="element-name">createPrimitiveType</span>()</div>
<div class="block">Returns a new object of class '<em>Primitive Type</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Primitive Type</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFinalState()">
<h3>createFinalState</h3>
<div class="member-signature"><span class="return-type"><a href="../statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a></span> <span class="element-name">createFinalState</span>()</div>
<div class="block">Returns a new object of class '<em>Final State</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Final State</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAnyReceiveEvent()">
<h3>createAnyReceiveEvent</h3>
<div class="member-signature"><span class="return-type"><a href="../commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEvent</a></span> <span class="element-name">createAnyReceiveEvent</span>()</div>
<div class="block">Returns a new object of class '<em>Any Receive Event</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Any Receive Event</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMergeNode()">
<h3>createMergeNode</h3>
<div class="member-signature"><span class="return-type"><a href="../activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a></span> <span class="element-name">createMergeNode</span>()</div>
<div class="block">Returns a new object of class '<em>Merge Node</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Merge Node</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createContinuation()">
<h3>createContinuation</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Continuation</a></span> <span class="element-name">createContinuation</span>()</div>
<div class="block">Returns a new object of class '<em>Continuation</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Continuation</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralNull()">
<h3>createLiteralNull</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNull</a></span> <span class="element-name">createLiteralNull</span>()</div>
<div class="block">Returns a new object of class '<em>Literal Null</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Literal Null</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMessageOccurrenceSpecification()">
<h3>createMessageOccurrenceSpecification</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecification</a></span> <span class="element-name">createMessageOccurrenceSpecification</span>()</div>
<div class="block">Returns a new object of class '<em>Message Occurrence Specification</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Message Occurrence Specification</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralBoolean()">
<h3>createLiteralBoolean</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBoolean</a></span> <span class="element-name">createLiteralBoolean</span>()</div>
<div class="block">Returns a new object of class '<em>Literal Boolean</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Literal Boolean</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDestructionOccurrenceSpecification()">
<h3>createDestructionOccurrenceSpecification</h3>
<div class="member-signature"><span class="return-type"><a href="../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a></span> <span class="element-name">createDestructionOccurrenceSpecification</span>()</div>
<div class="block">Returns a new object of class '<em>Destruction Occurrence Specification</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Destruction Occurrence Specification</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createModel()">
<h3>createModel</h3>
<div class="member-signature"><span class="return-type"><a href="../auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></span> <span class="element-name">createModel</span>()</div>
<div class="block">Returns a new object of class '<em>Model</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Model</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClearVariableAction()">
<h3>createClearVariableAction</h3>
<div class="member-signature"><span class="return-type"><a href="../actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a></span> <span class="element-name">createClearVariableAction</span>()</div>
<div class="block">Returns a new object of class '<em>Clear Variable Action</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Clear Variable Action</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBooleanTaggedValue()">
<h3>createBooleanTaggedValue</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/BooleanTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BooleanTaggedValue</a></span> <span class="element-name">createBooleanTaggedValue</span>()</div>
<div class="block">Returns a new object of class '<em>Boolean Tagged Value</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Boolean Tagged Value</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIntegerTaggedValue()">
<h3>createIntegerTaggedValue</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/IntegerTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">IntegerTaggedValue</a></span> <span class="element-name">createIntegerTaggedValue</span>()</div>
<div class="block">Returns a new object of class '<em>Integer Tagged Value</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Integer Tagged Value</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRealTaggedValue()">
<h3>createRealTaggedValue</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/RealTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RealTaggedValue</a></span> <span class="element-name">createRealTaggedValue</span>()</div>
<div class="block">Returns a new object of class '<em>Real Tagged Value</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Real Tagged Value</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStringTaggedValue()">
<h3>createStringTaggedValue</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/StringTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StringTaggedValue</a></span> <span class="element-name">createStringTaggedValue</span>()</div>
<div class="block">Returns a new object of class '<em>String Tagged Value</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>String Tagged Value</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createElementTaggedValue()">
<h3>createElementTaggedValue</h3>
<div class="member-signature"><span class="return-type"><a href="../classes/mdkernel/ElementTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementTaggedValue</a></span> <span class="element-name">createElementTaggedValue</span>()</div>
<div class="block">Returns a new object of class '<em>Element Tagged Value</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Element Tagged Value</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUMLPackage()">
<h3>getUMLPackage</h3>
<div class="member-signature"><span class="return-type"><a href="UMLPackage.html" title="interface in com.nomagic.uml2.ext.magicdraw.metadata">UMLPackage</a></span> <span class="element-name">getUMLPackage</span>()</div>
<div class="block">Returns the package supported by this factory.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the package supported by this factory.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRepository(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository)">
<h3>setRepository</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="return-type">void</span> <span class="element-name">setRepository</span><wbr/><span class="parameters">(<a href="../../jmi/reflect/AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> repository)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">The method should not be used. The method allows to set a project's repository to the factory
 and the factory creates elements in the project's repository. This creates following unwanted consequences:
 <ol>
<li>UMLFactory.eINSTANCE object overlives a project's repository instance.
     So after a project's closing it might be used to create elements in already closed project. </li>
<li>If a code sets a project's repository and forgets to change it then after switch
     to another project all elements    will be created in the previous project.</li>
<li>It allows to create a deadlock condition. The code that sets the project's repository must take care that
     all elements in the project are already loaded and to assure that no elements can be unloaded.
     It makes the code difficult to implement.</li>
</ol></div>
</div>
<div class="block">Sets repository to the factory. All objects that will be created will be created in the
 specified repository.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>repository</code> - model objects repository.</dd>
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
