# JAVA OPENAPI: UMLAdapterFactory (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/magicdraw/util/UMLAdapterFactory.html
- source_path: `com/nomagic/uml2/ext/magicdraw/util/UMLAdapterFactory.html`
- source_sha256: `dbd1e0b4974e54104a656451565e521fb3d7ffad4d651adc2631faa48ac52fe8`
- captured_utc: `2026-07-14T16:53:42.092963+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.util](package-summary.html)

## Class UMLAdapterFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.notify.impl.AdapterFactoryImpl
com.nomagic.uml2.ext.magicdraw.util.UMLAdapterFactory

All Implemented Interfaces:
`org.eclipse.emf.common.notify.AdapterFactory`

public classUMLAdapterFactory
extends org.eclipse.emf.common.notify.impl.AdapterFactoryImpl

begin-user-doc 
 The **Adapter Factory** for the model.
 It provides an adapter `createXXX` method for each class of the model.
 end-user-doc

See Also:
[`UMLPackage`](../metadata/UMLPackage.html)
Generated:

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected static [UMLPackage](../metadata/UMLPackage.html)`
`[modelPackage](#modelPackage)`
The cached model package.
`protected [UMLSwitch](UMLSwitch.html)<org.eclipse.emf.common.notify.Adapter>`
`[modelSwitch](#modelSwitch)`
The switch that delegates to the `createXXX` methods.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[UMLAdapterFactory](#%3Cinit%3E())()`
Creates an instance of the adapter factory.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`org.eclipse.emf.common.notify.Adapter`
`[createAbstractionAdapter](#createAbstractionAdapter())()`
Creates a new adapter for an object of class '[`*Abstraction*`](../classes/mddependencies/Abstraction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createAcceptCallActionAdapter](#createAcceptCallActionAdapter())()`
Creates a new adapter for an object of class '[`*Accept Call Action*`](../actions/mdcompleteactions/AcceptCallAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createAcceptEventActionAdapter](#createAcceptEventActionAdapter())()`
Creates a new adapter for an object of class '[`*Accept Event Action*`](../actions/mdcompleteactions/AcceptEventAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createActionAdapter](#createActionAdapter())()`
Creates a new adapter for an object of class '[`*Action*`](../actions/mdbasicactions/Action.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createActionExecutionSpecificationAdapter](#createActionExecutionSpecificationAdapter())()`
Creates a new adapter for an object of class
 '[`*Action Execution Specification*`](../interactions/mdbasicinteractions/ActionExecutionSpecification.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createActionInputPinAdapter](#createActionInputPinAdapter())()`
Creates a new adapter for an object of class '[`*Action Input Pin*`](../actions/mdstructuredactions/ActionInputPin.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createActivityAdapter](#createActivityAdapter())()`
Creates a new adapter for an object of class '[`*Activity*`](../activities/mdfundamentalactivities/Activity.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createActivityEdgeAdapter](#createActivityEdgeAdapter())()`
Creates a new adapter for an object of class '[`*Activity Edge*`](../activities/mdbasicactivities/ActivityEdge.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createActivityFinalNodeAdapter](#createActivityFinalNodeAdapter())()`
Creates a new adapter for an object of class '[`*Activity Final Node*`](../activities/mdbasicactivities/ActivityFinalNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createActivityGroupAdapter](#createActivityGroupAdapter())()`
Creates a new adapter for an object of class '[`*Activity Group*`](../activities/mdfundamentalactivities/ActivityGroup.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createActivityNodeAdapter](#createActivityNodeAdapter())()`
Creates a new adapter for an object of class '[`*Activity Node*`](../activities/mdfundamentalactivities/ActivityNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createActivityParameterNodeAdapter](#createActivityParameterNodeAdapter())()`
Creates a new adapter for an object of class
 '[`*Activity Parameter Node*`](../activities/mdbasicactivities/ActivityParameterNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createActivityPartitionAdapter](#createActivityPartitionAdapter())()`
Creates a new adapter for an object of class
 '[`*Activity Partition*`](../activities/mdintermediateactivities/ActivityPartition.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createActorAdapter](#createActorAdapter())()`
Creates a new adapter for an object of class '[`*Actor*`](../mdusecases/Actor.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createAdapter](#createAdapter(org.eclipse.emf.common.notify.Notifier))(org.eclipse.emf.common.notify.Notifier target)`
Creates an adapter for the `target`.
`org.eclipse.emf.common.notify.Adapter`
`[createAddStructuralFeatureValueActionAdapter](#createAddStructuralFeatureValueActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Add Structural Feature Value Action*`](../actions/mdintermediateactions/AddStructuralFeatureValueAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createAddVariableValueActionAdapter](#createAddVariableValueActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Add Variable Value Action*`](../actions/mdstructuredactions/AddVariableValueAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createAnyReceiveEventAdapter](#createAnyReceiveEventAdapter())()`
Creates a new adapter for an object of class '[`*Any Receive Event*`](../commonbehaviors/mdcommunications/AnyReceiveEvent.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createArtifactAdapter](#createArtifactAdapter())()`
Creates a new adapter for an object of class '[`*Artifact*`](../deployments/mdartifacts/Artifact.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createAssociationAdapter](#createAssociationAdapter())()`
Creates a new adapter for an object of class '[`*Association*`](../classes/mdkernel/Association.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createAssociationClassAdapter](#createAssociationClassAdapter())()`
Creates a new adapter for an object of class '[`*Association Class*`](../classes/mdassociationclasses/AssociationClass.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createBehaviorAdapter](#createBehaviorAdapter())()`
Creates a new adapter for an object of class '[`*Behavior*`](../commonbehaviors/mdbasicbehaviors/Behavior.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createBehavioralFeatureAdapter](#createBehavioralFeatureAdapter())()`
Creates a new adapter for an object of class '[`*Behavioral Feature*`](../classes/mdkernel/BehavioralFeature.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createBehavioredClassifierAdapter](#createBehavioredClassifierAdapter())()`
Creates a new adapter for an object of class
 '[`*Behaviored Classifier*`](../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createBehaviorExecutionSpecificationAdapter](#createBehaviorExecutionSpecificationAdapter())()`
Creates a new adapter for an object of class
 '[`*Behavior Execution Specification*`](../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createBroadcastSignalActionAdapter](#createBroadcastSignalActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Broadcast Signal Action*`](../actions/mdintermediateactions/BroadcastSignalAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createCallActionAdapter](#createCallActionAdapter())()`
Creates a new adapter for an object of class '[`*Call Action*`](../actions/mdbasicactions/CallAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createCallBehaviorActionAdapter](#createCallBehaviorActionAdapter())()`
Creates a new adapter for an object of class '[`*Call Behavior Action*`](../actions/mdbasicactions/CallBehaviorAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createCallEventAdapter](#createCallEventAdapter())()`
Creates a new adapter for an object of class '[`*Call Event*`](../commonbehaviors/mdcommunications/CallEvent.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createCallOperationActionAdapter](#createCallOperationActionAdapter())()`
Creates a new adapter for an object of class '[`*Call Operation Action*`](../actions/mdbasicactions/CallOperationAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createCentralBufferNodeAdapter](#createCentralBufferNodeAdapter())()`
Creates a new adapter for an object of class
 '[`*Central Buffer Node*`](../activities/mdintermediateactivities/CentralBufferNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createChangeEventAdapter](#createChangeEventAdapter())()`
Creates a new adapter for an object of class '[`*Change Event*`](../commonbehaviors/mdcommunications/ChangeEvent.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createClassAdapter](#createClassAdapter())()`
Creates a new adapter for an object of class '[`*Class*`](../classes/mdkernel/Class.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createClassifierAdapter](#createClassifierAdapter())()`
Creates a new adapter for an object of class '[`*Classifier*`](../classes/mdkernel/Classifier.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createClassifierTemplateParameterAdapter](#createClassifierTemplateParameterAdapter())()`
Creates a new adapter for an object of class
 '[`*Classifier Template Parameter*`](../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createClauseAdapter](#createClauseAdapter())()`
Creates a new adapter for an object of class '[`*Clause*`](../activities/mdstructuredactivities/Clause.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createClearAssociationActionAdapter](#createClearAssociationActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Clear Association Action*`](../actions/mdintermediateactions/ClearAssociationAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createClearStructuralFeatureActionAdapter](#createClearStructuralFeatureActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Clear Structural Feature Action*`](../actions/mdintermediateactions/ClearStructuralFeatureAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createClearVariableActionAdapter](#createClearVariableActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Clear Variable Action*`](../actions/mdstructuredactions/ClearVariableAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createCollaborationAdapter](#createCollaborationAdapter())()`
Creates a new adapter for an object of class '[`*Collaboration*`](../compositestructures/mdcollaborations/Collaboration.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createCollaborationUseAdapter](#createCollaborationUseAdapter())()`
Creates a new adapter for an object of class
 '[`*Collaboration Use*`](../compositestructures/mdcollaborations/CollaborationUse.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createCombinedFragmentAdapter](#createCombinedFragmentAdapter())()`
Creates a new adapter for an object of class '[`*Combined Fragment*`](../interactions/mdfragments/CombinedFragment.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createCommentAdapter](#createCommentAdapter())()`
Creates a new adapter for an object of class '[`*Comment*`](../classes/mdkernel/Comment.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createCommunicationPathAdapter](#createCommunicationPathAdapter())()`
Creates a new adapter for an object of class '[`*Communication Path*`](../deployments/mdnodes/CommunicationPath.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createComponentAdapter](#createComponentAdapter())()`
Creates a new adapter for an object of class '[`*Component*`](../components/mdbasiccomponents/Component.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createComponentRealizationAdapter](#createComponentRealizationAdapter())()`
Creates a new adapter for an object of class
 '[`*Component Realization*`](../components/mdbasiccomponents/ComponentRealization.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createConditionalNodeAdapter](#createConditionalNodeAdapter())()`
Creates a new adapter for an object of class '[`*Conditional Node*`](../activities/mdstructuredactivities/ConditionalNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createConnectableElementAdapter](#createConnectableElementAdapter())()`
Creates a new adapter for an object of class
 '[`*Connectable Element*`](../compositestructures/mdinternalstructures/ConnectableElement.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createConnectableElementTemplateParameterAdapter](#createConnectableElementTemplateParameterAdapter())()`
Creates a new adapter for an object of class '[`*Connectable Element Template Parameter*`](../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createConnectionPointReferenceAdapter](#createConnectionPointReferenceAdapter())()`
Creates a new adapter for an object of class
 '[`*Connection Point Reference*`](../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createConnectorAdapter](#createConnectorAdapter())()`
Creates a new adapter for an object of class '[`*Connector*`](../compositestructures/mdinternalstructures/Connector.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createConnectorEndAdapter](#createConnectorEndAdapter())()`
Creates a new adapter for an object of class
 '[`*Connector End*`](../compositestructures/mdinternalstructures/ConnectorEnd.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createConsiderIgnoreFragmentAdapter](#createConsiderIgnoreFragmentAdapter())()`
Creates a new adapter for an object of class
 '[`*Consider Ignore Fragment*`](../interactions/mdfragments/ConsiderIgnoreFragment.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createConstraintAdapter](#createConstraintAdapter())()`
Creates a new adapter for an object of class '[`*Constraint*`](../classes/mdkernel/Constraint.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createContinuationAdapter](#createContinuationAdapter())()`
Creates a new adapter for an object of class '[`*Continuation*`](../interactions/mdfragments/Continuation.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createControlFlowAdapter](#createControlFlowAdapter())()`
Creates a new adapter for an object of class '[`*Control Flow*`](../activities/mdbasicactivities/ControlFlow.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createControlNodeAdapter](#createControlNodeAdapter())()`
Creates a new adapter for an object of class '[`*Control Node*`](../activities/mdbasicactivities/ControlNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createCreateLinkActionAdapter](#createCreateLinkActionAdapter())()`
Creates a new adapter for an object of class '[`*Create Link Action*`](../actions/mdintermediateactions/CreateLinkAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createCreateLinkObjectActionAdapter](#createCreateLinkObjectActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Create Link Object Action*`](../actions/mdcompleteactions/CreateLinkObjectAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createCreateObjectActionAdapter](#createCreateObjectActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Create Object Action*`](../actions/mdintermediateactions/CreateObjectAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDataStoreNodeAdapter](#createDataStoreNodeAdapter())()`
Creates a new adapter for an object of class '[`*Data Store Node*`](../activities/mdcompleteactivities/DataStoreNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDataTypeAdapter](#createDataTypeAdapter())()`
Creates a new adapter for an object of class '[`*Data Type*`](../classes/mdkernel/DataType.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDecisionNodeAdapter](#createDecisionNodeAdapter())()`
Creates a new adapter for an object of class '[`*Decision Node*`](../activities/mdintermediateactivities/DecisionNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDependencyAdapter](#createDependencyAdapter())()`
Creates a new adapter for an object of class '[`*Dependency*`](../classes/mddependencies/Dependency.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDeployedArtifactAdapter](#createDeployedArtifactAdapter())()`
Creates a new adapter for an object of class '[`*Deployed Artifact*`](../deployments/mdnodes/DeployedArtifact.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDeploymentAdapter](#createDeploymentAdapter())()`
Creates a new adapter for an object of class '[`*Deployment*`](../deployments/mdnodes/Deployment.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDeploymentSpecificationAdapter](#createDeploymentSpecificationAdapter())()`
Creates a new adapter for an object of class
 '[`*Deployment Specification*`](../deployments/mdcomponentdeployments/DeploymentSpecification.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDeploymentTargetAdapter](#createDeploymentTargetAdapter())()`
Creates a new adapter for an object of class '[`*Deployment Target*`](../deployments/mdnodes/DeploymentTarget.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDestroyLinkActionAdapter](#createDestroyLinkActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Destroy Link Action*`](../actions/mdintermediateactions/DestroyLinkAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDestroyObjectActionAdapter](#createDestroyObjectActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Destroy Object Action*`](../actions/mdintermediateactions/DestroyObjectAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDestructionOccurrenceSpecificationAdapter](#createDestructionOccurrenceSpecificationAdapter())()`
Creates a new adapter for an object of class '[`*Destruction Occurrence Specification*`](../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDeviceAdapter](#createDeviceAdapter())()`
Creates a new adapter for an object of class '[`*Device*`](../deployments/mdnodes/Device.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDiagramAdapter](#createDiagramAdapter())()`
Creates a new adapter for an object of class '[`*Diagram*`](../classes/mdkernel/Diagram.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDirectedRelationshipAdapter](#createDirectedRelationshipAdapter())()`
Creates a new adapter for an object of class '[`*Directed Relationship*`](../classes/mdkernel/DirectedRelationship.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDurationAdapter](#createDurationAdapter())()`
Creates a new adapter for an object of class '[`*Duration*`](../commonbehaviors/mdsimpletime/Duration.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDurationConstraintAdapter](#createDurationConstraintAdapter())()`
Creates a new adapter for an object of class
 '[`*Duration Constraint*`](../commonbehaviors/mdsimpletime/DurationConstraint.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDurationIntervalAdapter](#createDurationIntervalAdapter())()`
Creates a new adapter for an object of class '[`*Duration Interval*`](../commonbehaviors/mdsimpletime/DurationInterval.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createDurationObservationAdapter](#createDurationObservationAdapter())()`
Creates a new adapter for an object of class
 '[`*Duration Observation*`](../commonbehaviors/mdsimpletime/DurationObservation.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createElementAdapter](#createElementAdapter())()`
Creates a new adapter for an object of class '[`*Element*`](../classes/mdkernel/Element.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createElementImportAdapter](#createElementImportAdapter())()`
Creates a new adapter for an object of class '[`*Element Import*`](../classes/mdkernel/ElementImport.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createElementValueAdapter](#createElementValueAdapter())()`
Creates a new adapter for an object of class '[`*Element Value*`](../classes/mdkernel/ElementValue.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createEncapsulatedClassifierAdapter](#createEncapsulatedClassifierAdapter())()`
Creates a new adapter for an object of class
 '[`*Encapsulated Classifier*`](../compositestructures/mdports/EncapsulatedClassifier.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createEnumerationAdapter](#createEnumerationAdapter())()`
Creates a new adapter for an object of class '[`*Enumeration*`](../classes/mdkernel/Enumeration.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createEnumerationLiteralAdapter](#createEnumerationLiteralAdapter())()`
Creates a new adapter for an object of class '[`*Enumeration Literal*`](../classes/mdkernel/EnumerationLiteral.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createEObjectAdapter](#createEObjectAdapter())()`
Creates a new adapter for the default case.
`org.eclipse.emf.common.notify.Adapter`
`[createEventAdapter](#createEventAdapter())()`
Creates a new adapter for an object of class '[`*Event*`](../commonbehaviors/mdcommunications/Event.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createExceptionHandlerAdapter](#createExceptionHandlerAdapter())()`
Creates a new adapter for an object of class
 '[`*Exception Handler*`](../activities/mdextrastructuredactivities/ExceptionHandler.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createExecutableNodeAdapter](#createExecutableNodeAdapter())()`
Creates a new adapter for an object of class '[`*Executable Node*`](../activities/mdstructuredactivities/ExecutableNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createExecutionEnvironmentAdapter](#createExecutionEnvironmentAdapter())()`
Creates a new adapter for an object of class '[`*Execution Environment*`](../deployments/mdnodes/ExecutionEnvironment.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createExecutionOccurrenceSpecificationAdapter](#createExecutionOccurrenceSpecificationAdapter())()`
Creates a new adapter for an object of class
 '[`*Execution Occurrence Specification*`](../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createExecutionSpecificationAdapter](#createExecutionSpecificationAdapter())()`
Creates a new adapter for an object of class
 '[`*Execution Specification*`](../interactions/mdbasicinteractions/ExecutionSpecification.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createExpansionNodeAdapter](#createExpansionNodeAdapter())()`
Creates a new adapter for an object of class
 '[`*Expansion Node*`](../activities/mdextrastructuredactivities/ExpansionNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createExpansionRegionAdapter](#createExpansionRegionAdapter())()`
Creates a new adapter for an object of class
 '[`*Expansion Region*`](../activities/mdextrastructuredactivities/ExpansionRegion.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createExpressionAdapter](#createExpressionAdapter())()`
Creates a new adapter for an object of class '[`*Expression*`](../classes/mdkernel/Expression.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createExtendAdapter](#createExtendAdapter())()`
Creates a new adapter for an object of class '[`*Extend*`](../mdusecases/Extend.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createExtensionAdapter](#createExtensionAdapter())()`
Creates a new adapter for an object of class '[`*Extension*`](../mdprofiles/Extension.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createExtensionEndAdapter](#createExtensionEndAdapter())()`
Creates a new adapter for an object of class '[`*Extension End*`](../mdprofiles/ExtensionEnd.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createExtensionPointAdapter](#createExtensionPointAdapter())()`
Creates a new adapter for an object of class '[`*Extension Point*`](../mdusecases/ExtensionPoint.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createFeatureAdapter](#createFeatureAdapter())()`
Creates a new adapter for an object of class '[`*Feature*`](../classes/mdkernel/Feature.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createFinalNodeAdapter](#createFinalNodeAdapter())()`
Creates a new adapter for an object of class '[`*Final Node*`](../activities/mdintermediateactivities/FinalNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createFinalStateAdapter](#createFinalStateAdapter())()`
Creates a new adapter for an object of class '[`*Final State*`](../statemachines/mdbehaviorstatemachines/FinalState.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createFlowFinalNodeAdapter](#createFlowFinalNodeAdapter())()`
Creates a new adapter for an object of class '[`*Flow Final Node*`](../activities/mdintermediateactivities/FlowFinalNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createForkNodeAdapter](#createForkNodeAdapter())()`
Creates a new adapter for an object of class '[`*Fork Node*`](../activities/mdintermediateactivities/ForkNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createFunctionBehaviorAdapter](#createFunctionBehaviorAdapter())()`
Creates a new adapter for an object of class
 '[`*Function Behavior*`](../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createGateAdapter](#createGateAdapter())()`
Creates a new adapter for an object of class '[`*Gate*`](../interactions/mdfragments/Gate.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createGeneralizationAdapter](#createGeneralizationAdapter())()`
Creates a new adapter for an object of class '[`*Generalization*`](../classes/mdkernel/Generalization.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createGeneralizationSetAdapter](#createGeneralizationSetAdapter())()`
Creates a new adapter for an object of class '[`*Generalization Set*`](../classes/mdpowertypes/GeneralizationSet.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createGeneralOrderingAdapter](#createGeneralOrderingAdapter())()`
Creates a new adapter for an object of class '[`*General Ordering*`](../interactions/mdbasicinteractions/GeneralOrdering.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createImageAdapter](#createImageAdapter())()`
Creates a new adapter for an object of class '[`*Image*`](../mdprofiles/Image.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createIncludeAdapter](#createIncludeAdapter())()`
Creates a new adapter for an object of class '[`*Include*`](../mdusecases/Include.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInformationFlowAdapter](#createInformationFlowAdapter())()`
Creates a new adapter for an object of class
 '[`*Information Flow*`](../auxiliaryconstructs/mdinformationflows/InformationFlow.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInformationItemAdapter](#createInformationItemAdapter())()`
Creates a new adapter for an object of class
 '[`*Information Item*`](../auxiliaryconstructs/mdinformationflows/InformationItem.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInitialNodeAdapter](#createInitialNodeAdapter())()`
Creates a new adapter for an object of class '[`*Initial Node*`](../activities/mdbasicactivities/InitialNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInputPinAdapter](#createInputPinAdapter())()`
Creates a new adapter for an object of class '[`*Input Pin*`](../actions/mdbasicactions/InputPin.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInstanceSpecificationAdapter](#createInstanceSpecificationAdapter())()`
Creates a new adapter for an object of class '[`*Instance Specification*`](../classes/mdkernel/InstanceSpecification.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInstanceValueAdapter](#createInstanceValueAdapter())()`
Creates a new adapter for an object of class '[`*Instance Value*`](../classes/mdkernel/InstanceValue.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInteractionAdapter](#createInteractionAdapter())()`
Creates a new adapter for an object of class '[`*Interaction*`](../interactions/mdbasicinteractions/Interaction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInteractionConstraintAdapter](#createInteractionConstraintAdapter())()`
Creates a new adapter for an object of class
 '[`*Interaction Constraint*`](../interactions/mdfragments/InteractionConstraint.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInteractionFragmentAdapter](#createInteractionFragmentAdapter())()`
Creates a new adapter for an object of class
 '[`*Interaction Fragment*`](../interactions/mdbasicinteractions/InteractionFragment.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInteractionOperandAdapter](#createInteractionOperandAdapter())()`
Creates a new adapter for an object of class '[`*Interaction Operand*`](../interactions/mdfragments/InteractionOperand.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInteractionUseAdapter](#createInteractionUseAdapter())()`
Creates a new adapter for an object of class '[`*Interaction Use*`](../interactions/mdfragments/InteractionUse.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInterfaceAdapter](#createInterfaceAdapter())()`
Creates a new adapter for an object of class '[`*Interface*`](../classes/mdinterfaces/Interface.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInterfaceRealizationAdapter](#createInterfaceRealizationAdapter())()`
Creates a new adapter for an object of class '[`*Interface Realization*`](../classes/mdinterfaces/InterfaceRealization.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInterruptibleActivityRegionAdapter](#createInterruptibleActivityRegionAdapter())()`
Creates a new adapter for an object of class
 '[`*Interruptible Activity Region*`](../activities/mdcompleteactivities/InterruptibleActivityRegion.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createIntervalAdapter](#createIntervalAdapter())()`
Creates a new adapter for an object of class '[`*Interval*`](../commonbehaviors/mdsimpletime/Interval.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createIntervalConstraintAdapter](#createIntervalConstraintAdapter())()`
Creates a new adapter for an object of class
 '[`*Interval Constraint*`](../commonbehaviors/mdsimpletime/IntervalConstraint.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createInvocationActionAdapter](#createInvocationActionAdapter())()`
Creates a new adapter for an object of class '[`*Invocation Action*`](../actions/mdbasicactions/InvocationAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createJoinNodeAdapter](#createJoinNodeAdapter())()`
Creates a new adapter for an object of class '[`*Join Node*`](../activities/mdintermediateactivities/JoinNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createLifelineAdapter](#createLifelineAdapter())()`
Creates a new adapter for an object of class '[`*Lifeline*`](../interactions/mdbasicinteractions/Lifeline.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createLinkActionAdapter](#createLinkActionAdapter())()`
Creates a new adapter for an object of class '[`*Link Action*`](../actions/mdintermediateactions/LinkAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createLinkEndCreationDataAdapter](#createLinkEndCreationDataAdapter())()`
Creates a new adapter for an object of class
 '[`*Link End Creation Data*`](../actions/mdintermediateactions/LinkEndCreationData.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createLinkEndDataAdapter](#createLinkEndDataAdapter())()`
Creates a new adapter for an object of class '[`*Link End Data*`](../actions/mdintermediateactions/LinkEndData.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createLinkEndDestructionDataAdapter](#createLinkEndDestructionDataAdapter())()`
Creates a new adapter for an object of class
 '[`*Link End Destruction Data*`](../actions/mdintermediateactions/LinkEndDestructionData.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createLiteralBooleanAdapter](#createLiteralBooleanAdapter())()`
Creates a new adapter for an object of class '[`*Literal Boolean*`](../classes/mdkernel/LiteralBoolean.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createLiteralIntegerAdapter](#createLiteralIntegerAdapter())()`
Creates a new adapter for an object of class '[`*Literal Integer*`](../classes/mdkernel/LiteralInteger.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createLiteralNullAdapter](#createLiteralNullAdapter())()`
Creates a new adapter for an object of class '[`*Literal Null*`](../classes/mdkernel/LiteralNull.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createLiteralRealAdapter](#createLiteralRealAdapter())()`
Creates a new adapter for an object of class '[`*Literal Real*`](../classes/mdkernel/LiteralReal.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createLiteralSpecificationAdapter](#createLiteralSpecificationAdapter())()`
Creates a new adapter for an object of class '[`*Literal Specification*`](../classes/mdkernel/LiteralSpecification.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createLiteralStringAdapter](#createLiteralStringAdapter())()`
Creates a new adapter for an object of class '[`*Literal String*`](../classes/mdkernel/LiteralString.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createLiteralUnlimitedNaturalAdapter](#createLiteralUnlimitedNaturalAdapter())()`
Creates a new adapter for an object of class '[`*Literal Unlimited Natural*`](../classes/mdkernel/LiteralUnlimitedNatural.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createLoopNodeAdapter](#createLoopNodeAdapter())()`
Creates a new adapter for an object of class '[`*Loop Node*`](../activities/mdstructuredactivities/LoopNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createManifestationAdapter](#createManifestationAdapter())()`
Creates a new adapter for an object of class '[`*Manifestation*`](../deployments/mdartifacts/Manifestation.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createMDObjectAdapter](#createMDObjectAdapter())()`
Creates a new adapter for an object of class '[`*MD Object*`](../../../../magicdraw/foundation/MDObject.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createMergeNodeAdapter](#createMergeNodeAdapter())()`
Creates a new adapter for an object of class '[`*Merge Node*`](../activities/mdintermediateactivities/MergeNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createMessageAdapter](#createMessageAdapter())()`
Creates a new adapter for an object of class '[`*Message*`](../interactions/mdbasicinteractions/Message.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createMessageEndAdapter](#createMessageEndAdapter())()`
Creates a new adapter for an object of class '[`*Message End*`](../interactions/mdbasicinteractions/MessageEnd.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createMessageEventAdapter](#createMessageEventAdapter())()`
Creates a new adapter for an object of class '[`*Message Event*`](../commonbehaviors/mdcommunications/MessageEvent.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createMessageOccurrenceSpecificationAdapter](#createMessageOccurrenceSpecificationAdapter())()`
Creates a new adapter for an object of class
 '[`*Message Occurrence Specification*`](../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createModelAdapter](#createModelAdapter())()`
Creates a new adapter for an object of class '[`*Model*`](../auxiliaryconstructs/mdmodels/Model.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createModelObjectAdapter](#createModelObjectAdapter())()`
Creates a new adapter for an object of class '[`*Model Object*`](../base/ModelObject.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createMultiplicityElementAdapter](#createMultiplicityElementAdapter())()`
Creates a new adapter for an object of class '[`*Multiplicity Element*`](../classes/mdkernel/MultiplicityElement.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createNamedElementAdapter](#createNamedElementAdapter())()`
Creates a new adapter for an object of class '[`*Named Element*`](../classes/mdkernel/NamedElement.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createNamespaceAdapter](#createNamespaceAdapter())()`
Creates a new adapter for an object of class '[`*Namespace*`](../classes/mdkernel/Namespace.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createNodeAdapter](#createNodeAdapter())()`
Creates a new adapter for an object of class '[`*Node*`](../deployments/mdnodes/Node.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createObjectFlowAdapter](#createObjectFlowAdapter())()`
Creates a new adapter for an object of class '[`*Object Flow*`](../activities/mdbasicactivities/ObjectFlow.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createObjectNodeAdapter](#createObjectNodeAdapter())()`
Creates a new adapter for an object of class '[`*Object Node*`](../activities/mdbasicactivities/ObjectNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createObservationAdapter](#createObservationAdapter())()`
Creates a new adapter for an object of class '[`*Observation*`](../commonbehaviors/mdsimpletime/Observation.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createOccurrenceSpecificationAdapter](#createOccurrenceSpecificationAdapter())()`
Creates a new adapter for an object of class
 '[`*Occurrence Specification*`](../interactions/mdbasicinteractions/OccurrenceSpecification.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createOpaqueActionAdapter](#createOpaqueActionAdapter())()`
Creates a new adapter for an object of class '[`*Opaque Action*`](../actions/mdbasicactions/OpaqueAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createOpaqueBehaviorAdapter](#createOpaqueBehaviorAdapter())()`
Creates a new adapter for an object of class '[`*Opaque Behavior*`](../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createOpaqueExpressionAdapter](#createOpaqueExpressionAdapter())()`
Creates a new adapter for an object of class '[`*Opaque Expression*`](../classes/mdkernel/OpaqueExpression.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createOperationAdapter](#createOperationAdapter())()`
Creates a new adapter for an object of class '[`*Operation*`](../classes/mdkernel/Operation.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createOperationTemplateParameterAdapter](#createOperationTemplateParameterAdapter())()`
Creates a new adapter for an object of class
 '[`*Operation Template Parameter*`](../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createOutputPinAdapter](#createOutputPinAdapter())()`
Creates a new adapter for an object of class '[`*Output Pin*`](../actions/mdbasicactions/OutputPin.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createPackageableElementAdapter](#createPackageableElementAdapter())()`
Creates a new adapter for an object of class '[`*Packageable Element*`](../classes/mdkernel/PackageableElement.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createPackageAdapter](#createPackageAdapter())()`
Creates a new adapter for an object of class '[`*Package*`](../classes/mdkernel/Package.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createPackageImportAdapter](#createPackageImportAdapter())()`
Creates a new adapter for an object of class '[`*Package Import*`](../classes/mdkernel/PackageImport.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createPackageMergeAdapter](#createPackageMergeAdapter())()`
Creates a new adapter for an object of class '[`*Package Merge*`](../classes/mdkernel/PackageMerge.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createParameterableElementAdapter](#createParameterableElementAdapter())()`
Creates a new adapter for an object of class
 '[`*Parameterable Element*`](../auxiliaryconstructs/mdtemplates/ParameterableElement.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createParameterAdapter](#createParameterAdapter())()`
Creates a new adapter for an object of class '[`*Parameter*`](../classes/mdkernel/Parameter.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createParameterSetAdapter](#createParameterSetAdapter())()`
Creates a new adapter for an object of class '[`*Parameter Set*`](../activities/mdcompleteactivities/ParameterSet.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createPartDecompositionAdapter](#createPartDecompositionAdapter())()`
Creates a new adapter for an object of class '[`*Part Decomposition*`](../interactions/mdfragments/PartDecomposition.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createPinAdapter](#createPinAdapter())()`
Creates a new adapter for an object of class '[`*Pin*`](../actions/mdbasicactions/Pin.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createPortAdapter](#createPortAdapter())()`
Creates a new adapter for an object of class '[`*Port*`](../compositestructures/mdports/Port.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createPrimitiveTypeAdapter](#createPrimitiveTypeAdapter())()`
Creates a new adapter for an object of class '[`*Primitive Type*`](../classes/mdkernel/PrimitiveType.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createProfileAdapter](#createProfileAdapter())()`
Creates a new adapter for an object of class '[`*Profile*`](../mdprofiles/Profile.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createProfileApplicationAdapter](#createProfileApplicationAdapter())()`
Creates a new adapter for an object of class '[`*Profile Application*`](../mdprofiles/ProfileApplication.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createPropertyAdapter](#createPropertyAdapter())()`
Creates a new adapter for an object of class '[`*Property*`](../classes/mdkernel/Property.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createProtocolConformanceAdapter](#createProtocolConformanceAdapter())()`
Creates a new adapter for an object of class
 '[`*Protocol Conformance*`](../statemachines/mdprotocolstatemachines/ProtocolConformance.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createProtocolStateMachineAdapter](#createProtocolStateMachineAdapter())()`
Creates a new adapter for an object of class
 '[`*Protocol State Machine*`](../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createProtocolTransitionAdapter](#createProtocolTransitionAdapter())()`
Creates a new adapter for an object of class
 '[`*Protocol Transition*`](../statemachines/mdprotocolstatemachines/ProtocolTransition.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createPseudostateAdapter](#createPseudostateAdapter())()`
Creates a new adapter for an object of class '[`*Pseudostate*`](../statemachines/mdbehaviorstatemachines/Pseudostate.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createQualifierValueAdapter](#createQualifierValueAdapter())()`
Creates a new adapter for an object of class '[`*Qualifier Value*`](../actions/mdcompleteactions/QualifierValue.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createRaiseExceptionActionAdapter](#createRaiseExceptionActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Raise Exception Action*`](../actions/mdstructuredactions/RaiseExceptionAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createReadExtentActionAdapter](#createReadExtentActionAdapter())()`
Creates a new adapter for an object of class '[`*Read Extent Action*`](../actions/mdcompleteactions/ReadExtentAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createReadIsClassifiedObjectActionAdapter](#createReadIsClassifiedObjectActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Read Is Classified Object Action*`](../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createReadLinkActionAdapter](#createReadLinkActionAdapter())()`
Creates a new adapter for an object of class '[`*Read Link Action*`](../actions/mdintermediateactions/ReadLinkAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createReadLinkObjectEndActionAdapter](#createReadLinkObjectEndActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Read Link Object End Action*`](../actions/mdcompleteactions/ReadLinkObjectEndAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createReadLinkObjectEndQualifierActionAdapter](#createReadLinkObjectEndQualifierActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Read Link Object End Qualifier Action*`](../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createReadSelfActionAdapter](#createReadSelfActionAdapter())()`
Creates a new adapter for an object of class '[`*Read Self Action*`](../actions/mdintermediateactions/ReadSelfAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createReadStructuralFeatureActionAdapter](#createReadStructuralFeatureActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Read Structural Feature Action*`](../actions/mdintermediateactions/ReadStructuralFeatureAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createReadVariableActionAdapter](#createReadVariableActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Read Variable Action*`](../actions/mdstructuredactions/ReadVariableAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createRealizationAdapter](#createRealizationAdapter())()`
Creates a new adapter for an object of class '[`*Realization*`](../classes/mddependencies/Realization.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createReceptionAdapter](#createReceptionAdapter())()`
Creates a new adapter for an object of class '[`*Reception*`](../commonbehaviors/mdcommunications/Reception.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createReclassifyObjectActionAdapter](#createReclassifyObjectActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Reclassify Object Action*`](../actions/mdcompleteactions/ReclassifyObjectAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createRedefinableElementAdapter](#createRedefinableElementAdapter())()`
Creates a new adapter for an object of class '[`*Redefinable Element*`](../classes/mdkernel/RedefinableElement.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createRedefinableTemplateSignatureAdapter](#createRedefinableTemplateSignatureAdapter())()`
Creates a new adapter for an object of class
 '[`*Redefinable Template Signature*`](../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createReduceActionAdapter](#createReduceActionAdapter())()`
Creates a new adapter for an object of class '[`*Reduce Action*`](../actions/mdcompleteactions/ReduceAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createRegionAdapter](#createRegionAdapter())()`
Creates a new adapter for an object of class '[`*Region*`](../statemachines/mdbehaviorstatemachines/Region.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createRelationshipAdapter](#createRelationshipAdapter())()`
Creates a new adapter for an object of class '[`*Relationship*`](../classes/mdkernel/Relationship.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createRemoveStructuralFeatureValueActionAdapter](#createRemoveStructuralFeatureValueActionAdapter())()`
Creates a new adapter for an object of class '[`*Remove
 Structural Feature Value Action*`](../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createRemoveVariableValueActionAdapter](#createRemoveVariableValueActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Remove Variable Value Action*`](../actions/mdstructuredactions/RemoveVariableValueAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createReplyActionAdapter](#createReplyActionAdapter())()`
Creates a new adapter for an object of class '[`*Reply Action*`](../actions/mdcompleteactions/ReplyAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createSendObjectActionAdapter](#createSendObjectActionAdapter())()`
Creates a new adapter for an object of class '[`*Send Object Action*`](../actions/mdintermediateactions/SendObjectAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createSendSignalActionAdapter](#createSendSignalActionAdapter())()`
Creates a new adapter for an object of class '[`*Send Signal Action*`](../actions/mdbasicactions/SendSignalAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createSequenceNodeAdapter](#createSequenceNodeAdapter())()`
Creates a new adapter for an object of class '[`*Sequence Node*`](../activities/mdstructuredactivities/SequenceNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createSignalAdapter](#createSignalAdapter())()`
Creates a new adapter for an object of class '[`*Signal*`](../commonbehaviors/mdcommunications/Signal.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createSignalEventAdapter](#createSignalEventAdapter())()`
Creates a new adapter for an object of class '[`*Signal Event*`](../commonbehaviors/mdcommunications/SignalEvent.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createSlotAdapter](#createSlotAdapter())()`
Creates a new adapter for an object of class '[`*Slot*`](../classes/mdkernel/Slot.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createStartClassifierBehaviorActionAdapter](#createStartClassifierBehaviorActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Start Classifier Behavior Action*`](../actions/mdcompleteactions/StartClassifierBehaviorAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createStartObjectBehaviorActionAdapter](#createStartObjectBehaviorActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Start Object Behavior Action*`](../actions/mdcompleteactions/StartObjectBehaviorAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createStateAdapter](#createStateAdapter())()`
Creates a new adapter for an object of class '[`*State*`](../statemachines/mdbehaviorstatemachines/State.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createStateInvariantAdapter](#createStateInvariantAdapter())()`
Creates a new adapter for an object of class '[`*State Invariant*`](../interactions/mdbasicinteractions/StateInvariant.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createStateMachineAdapter](#createStateMachineAdapter())()`
Creates a new adapter for an object of class '[`*State Machine*`](../statemachines/mdbehaviorstatemachines/StateMachine.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createStereotypeAdapter](#createStereotypeAdapter())()`
Creates a new adapter for an object of class '[`*Stereotype*`](../mdprofiles/Stereotype.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createStringExpressionAdapter](#createStringExpressionAdapter())()`
Creates a new adapter for an object of class '[`*String Expression*`](../auxiliaryconstructs/mdtemplates/StringExpression.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createStructuralFeatureActionAdapter](#createStructuralFeatureActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Structural Feature Action*`](../actions/mdintermediateactions/StructuralFeatureAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createStructuralFeatureAdapter](#createStructuralFeatureAdapter())()`
Creates a new adapter for an object of class '[`*Structural Feature*`](../classes/mdkernel/StructuralFeature.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createStructuredActivityNodeAdapter](#createStructuredActivityNodeAdapter())()`
Creates a new adapter for an object of class
 '[`*Structured Activity Node*`](../activities/mdstructuredactivities/StructuredActivityNode.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createStructuredClassifierAdapter](#createStructuredClassifierAdapter())()`
Creates a new adapter for an object of class
 '[`*Structured Classifier*`](../compositestructures/mdinternalstructures/StructuredClassifier.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createSubstitutionAdapter](#createSubstitutionAdapter())()`
Creates a new adapter for an object of class '[`*Substitution*`](../classes/mddependencies/Substitution.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTemplateableElementAdapter](#createTemplateableElementAdapter())()`
Creates a new adapter for an object of class
 '[`*Templateable Element*`](../auxiliaryconstructs/mdtemplates/TemplateableElement.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTemplateBindingAdapter](#createTemplateBindingAdapter())()`
Creates a new adapter for an object of class '[`*Template Binding*`](../auxiliaryconstructs/mdtemplates/TemplateBinding.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTemplateParameterAdapter](#createTemplateParameterAdapter())()`
Creates a new adapter for an object of class
 '[`*Template Parameter*`](../auxiliaryconstructs/mdtemplates/TemplateParameter.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTemplateParameterSubstitutionAdapter](#createTemplateParameterSubstitutionAdapter())()`
Creates a new adapter for an object of class
 '[`*Template Parameter Substitution*`](../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTemplateSignatureAdapter](#createTemplateSignatureAdapter())()`
Creates a new adapter for an object of class
 '[`*Template Signature*`](../auxiliaryconstructs/mdtemplates/TemplateSignature.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTestIdentityActionAdapter](#createTestIdentityActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Test Identity Action*`](../actions/mdintermediateactions/TestIdentityAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTimeConstraintAdapter](#createTimeConstraintAdapter())()`
Creates a new adapter for an object of class '[`*Time Constraint*`](../commonbehaviors/mdsimpletime/TimeConstraint.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTimeEventAdapter](#createTimeEventAdapter())()`
Creates a new adapter for an object of class '[`*Time Event*`](../commonbehaviors/mdcommunications/TimeEvent.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTimeExpressionAdapter](#createTimeExpressionAdapter())()`
Creates a new adapter for an object of class '[`*Time Expression*`](../commonbehaviors/mdsimpletime/TimeExpression.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTimeIntervalAdapter](#createTimeIntervalAdapter())()`
Creates a new adapter for an object of class '[`*Time Interval*`](../commonbehaviors/mdsimpletime/TimeInterval.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTimeObservationAdapter](#createTimeObservationAdapter())()`
Creates a new adapter for an object of class '[`*Time Observation*`](../commonbehaviors/mdsimpletime/TimeObservation.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTransitionAdapter](#createTransitionAdapter())()`
Creates a new adapter for an object of class '[`*Transition*`](../statemachines/mdbehaviorstatemachines/Transition.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTriggerAdapter](#createTriggerAdapter())()`
Creates a new adapter for an object of class '[`*Trigger*`](../commonbehaviors/mdcommunications/Trigger.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTypeAdapter](#createTypeAdapter())()`
Creates a new adapter for an object of class '[`*Type*`](../classes/mdkernel/Type.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createTypedElementAdapter](#createTypedElementAdapter())()`
Creates a new adapter for an object of class '[`*Typed Element*`](../classes/mdkernel/TypedElement.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createUnmarshallActionAdapter](#createUnmarshallActionAdapter())()`
Creates a new adapter for an object of class '[`*Unmarshall Action*`](../actions/mdcompleteactions/UnmarshallAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createUsageAdapter](#createUsageAdapter())()`
Creates a new adapter for an object of class '[`*Usage*`](../classes/mddependencies/Usage.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createUseCaseAdapter](#createUseCaseAdapter())()`
Creates a new adapter for an object of class '[`*Use Case*`](../mdusecases/UseCase.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createValuePinAdapter](#createValuePinAdapter())()`
Creates a new adapter for an object of class '[`*Value Pin*`](../actions/mdbasicactions/ValuePin.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createValueSpecificationActionAdapter](#createValueSpecificationActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Value Specification Action*`](../actions/mdintermediateactions/ValueSpecificationAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createValueSpecificationAdapter](#createValueSpecificationAdapter())()`
Creates a new adapter for an object of class '[`*Value Specification*`](../classes/mdkernel/ValueSpecification.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createVariableActionAdapter](#createVariableActionAdapter())()`
Creates a new adapter for an object of class '[`*Variable Action*`](../actions/mdstructuredactions/VariableAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createVariableAdapter](#createVariableAdapter())()`
Creates a new adapter for an object of class '[`*Variable*`](../activities/mdstructuredactivities/Variable.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createVertexAdapter](#createVertexAdapter())()`
Creates a new adapter for an object of class '[`*Vertex*`](../statemachines/mdbehaviorstatemachines/Vertex.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createWriteLinkActionAdapter](#createWriteLinkActionAdapter())()`
Creates a new adapter for an object of class '[`*Write Link Action*`](../actions/mdintermediateactions/WriteLinkAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createWriteStructuralFeatureActionAdapter](#createWriteStructuralFeatureActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Write Structural Feature Action*`](../actions/mdintermediateactions/WriteStructuralFeatureAction.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createWriteVariableActionAdapter](#createWriteVariableActionAdapter())()`
Creates a new adapter for an object of class
 '[`*Write Variable Action*`](../actions/mdstructuredactions/WriteVariableAction.html)'.
`boolean`
`[isFactoryForType](#isFactoryForType(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)`
Returns whether this factory is applicable for the type of the object.
Methods inherited from class org.eclipse.emf.common.notify.impl.AdapterFactoryImpl
`adapt, adapt, adaptAllNew, adaptNew, associate, createAdapter, resolve`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
modelPackage
protected static [UMLPackage](../metadata/UMLPackage.html) modelPackage
The cached model package.
 begin-user-doc 
 end-user-doc
Generated:
modelSwitch
protected [UMLSwitch](UMLSwitch.html)<org.eclipse.emf.common.notify.Adapter> modelSwitch
The switch that delegates to the `createXXX` methods.
 begin-user-doc 
 end-user-doc
Generated:
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
UMLAdapterFactory
public UMLAdapterFactory()
Creates an instance of the adapter factory.
 begin-user-doc 
 end-user-doc
Generated:
 ============ METHOD DETAIL ========== 
Method Details
isFactoryForType
public boolean isFactoryForType([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)
Returns whether this factory is applicable for the type of the object.
 begin-user-doc 
 This implementation returns `true` if the object is either the model's package or is an instance object of the model.
 end-user-doc
Specified by:
`isFactoryForType` in interface `org.eclipse.emf.common.notify.AdapterFactory`
Overrides:
`isFactoryForType` in class `org.eclipse.emf.common.notify.impl.AdapterFactoryImpl`
Returns:
whether this factory is applicable for the type of the object.
Generated:
createAdapter
public org.eclipse.emf.common.notify.Adapter createAdapter(org.eclipse.emf.common.notify.Notifier target)
Creates an adapter for the `target`.
 begin-user-doc 
 end-user-doc
Overrides:
`createAdapter` in class `org.eclipse.emf.common.notify.impl.AdapterFactoryImpl`
Parameters:
`target` - the object to adapt.
Returns:
the adapter for the `target`.
Generated:
createSendSignalActionAdapter
public org.eclipse.emf.common.notify.Adapter createSendSignalActionAdapter()
Creates a new adapter for an object of class '[`*Send Signal Action*`](../actions/mdbasicactions/SendSignalAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`SendSignalAction`](../actions/mdbasicactions/SendSignalAction.html)
Generated:
createInvocationActionAdapter
public org.eclipse.emf.common.notify.Adapter createInvocationActionAdapter()
Creates a new adapter for an object of class '[`*Invocation Action*`](../actions/mdbasicactions/InvocationAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`InvocationAction`](../actions/mdbasicactions/InvocationAction.html)
Generated:
createActionAdapter
public org.eclipse.emf.common.notify.Adapter createActionAdapter()
Creates a new adapter for an object of class '[`*Action*`](../actions/mdbasicactions/Action.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Action`](../actions/mdbasicactions/Action.html)
Generated:
createExecutableNodeAdapter
public org.eclipse.emf.common.notify.Adapter createExecutableNodeAdapter()
Creates a new adapter for an object of class '[`*Executable Node*`](../activities/mdstructuredactivities/ExecutableNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ExecutableNode`](../activities/mdstructuredactivities/ExecutableNode.html)
Generated:
createActivityNodeAdapter
public org.eclipse.emf.common.notify.Adapter createActivityNodeAdapter()
Creates a new adapter for an object of class '[`*Activity Node*`](../activities/mdfundamentalactivities/ActivityNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ActivityNode`](../activities/mdfundamentalactivities/ActivityNode.html)
Generated:
createRedefinableElementAdapter
public org.eclipse.emf.common.notify.Adapter createRedefinableElementAdapter()
Creates a new adapter for an object of class '[`*Redefinable Element*`](../classes/mdkernel/RedefinableElement.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`RedefinableElement`](../classes/mdkernel/RedefinableElement.html)
Generated:
createNamedElementAdapter
public org.eclipse.emf.common.notify.Adapter createNamedElementAdapter()
Creates a new adapter for an object of class '[`*Named Element*`](../classes/mdkernel/NamedElement.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`NamedElement`](../classes/mdkernel/NamedElement.html)
Generated:
createElementAdapter
public org.eclipse.emf.common.notify.Adapter createElementAdapter()
Creates a new adapter for an object of class '[`*Element*`](../classes/mdkernel/Element.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Element`](../classes/mdkernel/Element.html)
Generated:
createCommentAdapter
public org.eclipse.emf.common.notify.Adapter createCommentAdapter()
Creates a new adapter for an object of class '[`*Comment*`](../classes/mdkernel/Comment.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Comment`](../classes/mdkernel/Comment.html)
Generated:
createInstanceSpecificationAdapter
public org.eclipse.emf.common.notify.Adapter createInstanceSpecificationAdapter()
Creates a new adapter for an object of class '[`*Instance Specification*`](../classes/mdkernel/InstanceSpecification.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`InstanceSpecification`](../classes/mdkernel/InstanceSpecification.html)
Generated:
createPackageableElementAdapter
public org.eclipse.emf.common.notify.Adapter createPackageableElementAdapter()
Creates a new adapter for an object of class '[`*Packageable Element*`](../classes/mdkernel/PackageableElement.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`PackageableElement`](../classes/mdkernel/PackageableElement.html)
Generated:
createParameterableElementAdapter
public org.eclipse.emf.common.notify.Adapter createParameterableElementAdapter()
Creates a new adapter for an object of class
 '[`*Parameterable Element*`](../auxiliaryconstructs/mdtemplates/ParameterableElement.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ParameterableElement`](../auxiliaryconstructs/mdtemplates/ParameterableElement.html)
Generated:
createTemplateParameterAdapter
public org.eclipse.emf.common.notify.Adapter createTemplateParameterAdapter()
Creates a new adapter for an object of class
 '[`*Template Parameter*`](../auxiliaryconstructs/mdtemplates/TemplateParameter.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`TemplateParameter`](../auxiliaryconstructs/mdtemplates/TemplateParameter.html)
Generated:
createTemplateSignatureAdapter
public org.eclipse.emf.common.notify.Adapter createTemplateSignatureAdapter()
Creates a new adapter for an object of class
 '[`*Template Signature*`](../auxiliaryconstructs/mdtemplates/TemplateSignature.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`TemplateSignature`](../auxiliaryconstructs/mdtemplates/TemplateSignature.html)
Generated:
createTemplateableElementAdapter
public org.eclipse.emf.common.notify.Adapter createTemplateableElementAdapter()
Creates a new adapter for an object of class
 '[`*Templateable Element*`](../auxiliaryconstructs/mdtemplates/TemplateableElement.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`TemplateableElement`](../auxiliaryconstructs/mdtemplates/TemplateableElement.html)
Generated:
createTemplateBindingAdapter
public org.eclipse.emf.common.notify.Adapter createTemplateBindingAdapter()
Creates a new adapter for an object of class '[`*Template Binding*`](../auxiliaryconstructs/mdtemplates/TemplateBinding.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`TemplateBinding`](../auxiliaryconstructs/mdtemplates/TemplateBinding.html)
Generated:
createDirectedRelationshipAdapter
public org.eclipse.emf.common.notify.Adapter createDirectedRelationshipAdapter()
Creates a new adapter for an object of class '[`*Directed Relationship*`](../classes/mdkernel/DirectedRelationship.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DirectedRelationship`](../classes/mdkernel/DirectedRelationship.html)
Generated:
createRelationshipAdapter
public org.eclipse.emf.common.notify.Adapter createRelationshipAdapter()
Creates a new adapter for an object of class '[`*Relationship*`](../classes/mdkernel/Relationship.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Relationship`](../classes/mdkernel/Relationship.html)
Generated:
createInformationFlowAdapter
public org.eclipse.emf.common.notify.Adapter createInformationFlowAdapter()
Creates a new adapter for an object of class
 '[`*Information Flow*`](../auxiliaryconstructs/mdinformationflows/InformationFlow.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`InformationFlow`](../auxiliaryconstructs/mdinformationflows/InformationFlow.html)
Generated:
createClassifierAdapter
public org.eclipse.emf.common.notify.Adapter createClassifierAdapter()
Creates a new adapter for an object of class '[`*Classifier*`](../classes/mdkernel/Classifier.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Classifier`](../classes/mdkernel/Classifier.html)
Generated:
createNamespaceAdapter
public org.eclipse.emf.common.notify.Adapter createNamespaceAdapter()
Creates a new adapter for an object of class '[`*Namespace*`](../classes/mdkernel/Namespace.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Namespace`](../classes/mdkernel/Namespace.html)
Generated:
createElementImportAdapter
public org.eclipse.emf.common.notify.Adapter createElementImportAdapter()
Creates a new adapter for an object of class '[`*Element Import*`](../classes/mdkernel/ElementImport.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ElementImport`](../classes/mdkernel/ElementImport.html)
Generated:
createProfileAdapter
public org.eclipse.emf.common.notify.Adapter createProfileAdapter()
Creates a new adapter for an object of class '[`*Profile*`](../mdprofiles/Profile.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Profile`](../mdprofiles/Profile.html)
Generated:
createPackageAdapter
public org.eclipse.emf.common.notify.Adapter createPackageAdapter()
Creates a new adapter for an object of class '[`*Package*`](../classes/mdkernel/Package.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Package`](../classes/mdkernel/Package.html)
Generated:
createStereotypeAdapter
public org.eclipse.emf.common.notify.Adapter createStereotypeAdapter()
Creates a new adapter for an object of class '[`*Stereotype*`](../mdprofiles/Stereotype.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Stereotype`](../mdprofiles/Stereotype.html)
Generated:
createClassAdapter
public org.eclipse.emf.common.notify.Adapter createClassAdapter()
Creates a new adapter for an object of class '[`*Class*`](../classes/mdkernel/Class.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Class`](../classes/mdkernel/Class.html)
Generated:
createBehavioredClassifierAdapter
public org.eclipse.emf.common.notify.Adapter createBehavioredClassifierAdapter()
Creates a new adapter for an object of class
 '[`*Behaviored Classifier*`](../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`BehavioredClassifier`](../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)
Generated:
createBehaviorAdapter
public org.eclipse.emf.common.notify.Adapter createBehaviorAdapter()
Creates a new adapter for an object of class '[`*Behavior*`](../commonbehaviors/mdbasicbehaviors/Behavior.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Behavior`](../commonbehaviors/mdbasicbehaviors/Behavior.html)
Generated:
createParameterAdapter
public org.eclipse.emf.common.notify.Adapter createParameterAdapter()
Creates a new adapter for an object of class '[`*Parameter*`](../classes/mdkernel/Parameter.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Parameter`](../classes/mdkernel/Parameter.html)
Generated:
createMultiplicityElementAdapter
public org.eclipse.emf.common.notify.Adapter createMultiplicityElementAdapter()
Creates a new adapter for an object of class '[`*Multiplicity Element*`](../classes/mdkernel/MultiplicityElement.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`MultiplicityElement`](../classes/mdkernel/MultiplicityElement.html)
Generated:
createValueSpecificationAdapter
public org.eclipse.emf.common.notify.Adapter createValueSpecificationAdapter()
Creates a new adapter for an object of class '[`*Value Specification*`](../classes/mdkernel/ValueSpecification.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ValueSpecification`](../classes/mdkernel/ValueSpecification.html)
Generated:
createTypedElementAdapter
public org.eclipse.emf.common.notify.Adapter createTypedElementAdapter()
Creates a new adapter for an object of class '[`*Typed Element*`](../classes/mdkernel/TypedElement.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`TypedElement`](../classes/mdkernel/TypedElement.html)
Generated:
createTypeAdapter
public org.eclipse.emf.common.notify.Adapter createTypeAdapter()
Creates a new adapter for an object of class '[`*Type*`](../classes/mdkernel/Type.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Type`](../classes/mdkernel/Type.html)
Generated:
createAssociationAdapter
public org.eclipse.emf.common.notify.Adapter createAssociationAdapter()
Creates a new adapter for an object of class '[`*Association*`](../classes/mdkernel/Association.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Association`](../classes/mdkernel/Association.html)
Generated:
createPropertyAdapter
public org.eclipse.emf.common.notify.Adapter createPropertyAdapter()
Creates a new adapter for an object of class '[`*Property*`](../classes/mdkernel/Property.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Property`](../classes/mdkernel/Property.html)
Generated:
createStructuralFeatureAdapter
public org.eclipse.emf.common.notify.Adapter createStructuralFeatureAdapter()
Creates a new adapter for an object of class '[`*Structural Feature*`](../classes/mdkernel/StructuralFeature.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`StructuralFeature`](../classes/mdkernel/StructuralFeature.html)
Generated:
createFeatureAdapter
public org.eclipse.emf.common.notify.Adapter createFeatureAdapter()
Creates a new adapter for an object of class '[`*Feature*`](../classes/mdkernel/Feature.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Feature`](../classes/mdkernel/Feature.html)
Generated:
createSlotAdapter
public org.eclipse.emf.common.notify.Adapter createSlotAdapter()
Creates a new adapter for an object of class '[`*Slot*`](../classes/mdkernel/Slot.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Slot`](../classes/mdkernel/Slot.html)
Generated:
createStructuralFeatureActionAdapter
public org.eclipse.emf.common.notify.Adapter createStructuralFeatureActionAdapter()
Creates a new adapter for an object of class
 '[`*Structural Feature Action*`](../actions/mdintermediateactions/StructuralFeatureAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`StructuralFeatureAction`](../actions/mdintermediateactions/StructuralFeatureAction.html)
Generated:
createInputPinAdapter
public org.eclipse.emf.common.notify.Adapter createInputPinAdapter()
Creates a new adapter for an object of class '[`*Input Pin*`](../actions/mdbasicactions/InputPin.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`InputPin`](../actions/mdbasicactions/InputPin.html)
Generated:
createPinAdapter
public org.eclipse.emf.common.notify.Adapter createPinAdapter()
Creates a new adapter for an object of class '[`*Pin*`](../actions/mdbasicactions/Pin.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Pin`](../actions/mdbasicactions/Pin.html)
Generated:
createObjectNodeAdapter
public org.eclipse.emf.common.notify.Adapter createObjectNodeAdapter()
Creates a new adapter for an object of class '[`*Object Node*`](../activities/mdbasicactivities/ObjectNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ObjectNode`](../activities/mdbasicactivities/ObjectNode.html)
Generated:
createStateAdapter
public org.eclipse.emf.common.notify.Adapter createStateAdapter()
Creates a new adapter for an object of class '[`*State*`](../statemachines/mdbehaviorstatemachines/State.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`State`](../statemachines/mdbehaviorstatemachines/State.html)
Generated:
createVertexAdapter
public org.eclipse.emf.common.notify.Adapter createVertexAdapter()
Creates a new adapter for an object of class '[`*Vertex*`](../statemachines/mdbehaviorstatemachines/Vertex.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Vertex`](../statemachines/mdbehaviorstatemachines/Vertex.html)
Generated:
createRegionAdapter
public org.eclipse.emf.common.notify.Adapter createRegionAdapter()
Creates a new adapter for an object of class '[`*Region*`](../statemachines/mdbehaviorstatemachines/Region.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Region`](../statemachines/mdbehaviorstatemachines/Region.html)
Generated:
createStateMachineAdapter
public org.eclipse.emf.common.notify.Adapter createStateMachineAdapter()
Creates a new adapter for an object of class '[`*State Machine*`](../statemachines/mdbehaviorstatemachines/StateMachine.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`StateMachine`](../statemachines/mdbehaviorstatemachines/StateMachine.html)
Generated:
createPseudostateAdapter
public org.eclipse.emf.common.notify.Adapter createPseudostateAdapter()
Creates a new adapter for an object of class '[`*Pseudostate*`](../statemachines/mdbehaviorstatemachines/Pseudostate.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Pseudostate`](../statemachines/mdbehaviorstatemachines/Pseudostate.html)
Generated:
createConnectionPointReferenceAdapter
public org.eclipse.emf.common.notify.Adapter createConnectionPointReferenceAdapter()
Creates a new adapter for an object of class
 '[`*Connection Point Reference*`](../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ConnectionPointReference`](../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html)
Generated:
createTransitionAdapter
public org.eclipse.emf.common.notify.Adapter createTransitionAdapter()
Creates a new adapter for an object of class '[`*Transition*`](../statemachines/mdbehaviorstatemachines/Transition.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Transition`](../statemachines/mdbehaviorstatemachines/Transition.html)
Generated:
createConstraintAdapter
public org.eclipse.emf.common.notify.Adapter createConstraintAdapter()
Creates a new adapter for an object of class '[`*Constraint*`](../classes/mdkernel/Constraint.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Constraint`](../classes/mdkernel/Constraint.html)
Generated:
createOperationAdapter
public org.eclipse.emf.common.notify.Adapter createOperationAdapter()
Creates a new adapter for an object of class '[`*Operation*`](../classes/mdkernel/Operation.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Operation`](../classes/mdkernel/Operation.html)
Generated:
createBehavioralFeatureAdapter
public org.eclipse.emf.common.notify.Adapter createBehavioralFeatureAdapter()
Creates a new adapter for an object of class '[`*Behavioral Feature*`](../classes/mdkernel/BehavioralFeature.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`BehavioralFeature`](../classes/mdkernel/BehavioralFeature.html)
Generated:
createParameterSetAdapter
public org.eclipse.emf.common.notify.Adapter createParameterSetAdapter()
Creates a new adapter for an object of class '[`*Parameter Set*`](../activities/mdcompleteactivities/ParameterSet.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ParameterSet`](../activities/mdcompleteactivities/ParameterSet.html)
Generated:
createDataTypeAdapter
public org.eclipse.emf.common.notify.Adapter createDataTypeAdapter()
Creates a new adapter for an object of class '[`*Data Type*`](../classes/mdkernel/DataType.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DataType`](../classes/mdkernel/DataType.html)
Generated:
createInterfaceAdapter
public org.eclipse.emf.common.notify.Adapter createInterfaceAdapter()
Creates a new adapter for an object of class '[`*Interface*`](../classes/mdinterfaces/Interface.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Interface`](../classes/mdinterfaces/Interface.html)
Generated:
createReceptionAdapter
public org.eclipse.emf.common.notify.Adapter createReceptionAdapter()
Creates a new adapter for an object of class '[`*Reception*`](../commonbehaviors/mdcommunications/Reception.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Reception`](../commonbehaviors/mdcommunications/Reception.html)
Generated:
createSignalAdapter
public org.eclipse.emf.common.notify.Adapter createSignalAdapter()
Creates a new adapter for an object of class '[`*Signal*`](../commonbehaviors/mdcommunications/Signal.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Signal`](../commonbehaviors/mdcommunications/Signal.html)
Generated:
createBroadcastSignalActionAdapter
public org.eclipse.emf.common.notify.Adapter createBroadcastSignalActionAdapter()
Creates a new adapter for an object of class
 '[`*Broadcast Signal Action*`](../actions/mdintermediateactions/BroadcastSignalAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`BroadcastSignalAction`](../actions/mdintermediateactions/BroadcastSignalAction.html)
Generated:
createSignalEventAdapter
public org.eclipse.emf.common.notify.Adapter createSignalEventAdapter()
Creates a new adapter for an object of class '[`*Signal Event*`](../commonbehaviors/mdcommunications/SignalEvent.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`SignalEvent`](../commonbehaviors/mdcommunications/SignalEvent.html)
Generated:
createMessageEventAdapter
public org.eclipse.emf.common.notify.Adapter createMessageEventAdapter()
Creates a new adapter for an object of class '[`*Message Event*`](../commonbehaviors/mdcommunications/MessageEvent.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`MessageEvent`](../commonbehaviors/mdcommunications/MessageEvent.html)
Generated:
createEventAdapter
public org.eclipse.emf.common.notify.Adapter createEventAdapter()
Creates a new adapter for an object of class '[`*Event*`](../commonbehaviors/mdcommunications/Event.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Event`](../commonbehaviors/mdcommunications/Event.html)
Generated:
createTriggerAdapter
public org.eclipse.emf.common.notify.Adapter createTriggerAdapter()
Creates a new adapter for an object of class '[`*Trigger*`](../commonbehaviors/mdcommunications/Trigger.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Trigger`](../commonbehaviors/mdcommunications/Trigger.html)
Generated:
createPortAdapter
public org.eclipse.emf.common.notify.Adapter createPortAdapter()
Creates a new adapter for an object of class '[`*Port*`](../compositestructures/mdports/Port.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Port`](../compositestructures/mdports/Port.html)
Generated:
createProtocolStateMachineAdapter
public org.eclipse.emf.common.notify.Adapter createProtocolStateMachineAdapter()
Creates a new adapter for an object of class
 '[`*Protocol State Machine*`](../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ProtocolStateMachine`](../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)
Generated:
createProtocolConformanceAdapter
public org.eclipse.emf.common.notify.Adapter createProtocolConformanceAdapter()
Creates a new adapter for an object of class
 '[`*Protocol Conformance*`](../statemachines/mdprotocolstatemachines/ProtocolConformance.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ProtocolConformance`](../statemachines/mdprotocolstatemachines/ProtocolConformance.html)
Generated:
createEncapsulatedClassifierAdapter
public org.eclipse.emf.common.notify.Adapter createEncapsulatedClassifierAdapter()
Creates a new adapter for an object of class
 '[`*Encapsulated Classifier*`](../compositestructures/mdports/EncapsulatedClassifier.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`EncapsulatedClassifier`](../compositestructures/mdports/EncapsulatedClassifier.html)
Generated:
createStructuredClassifierAdapter
public org.eclipse.emf.common.notify.Adapter createStructuredClassifierAdapter()
Creates a new adapter for an object of class
 '[`*Structured Classifier*`](../compositestructures/mdinternalstructures/StructuredClassifier.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`StructuredClassifier`](../compositestructures/mdinternalstructures/StructuredClassifier.html)
Generated:
createConnectorAdapter
public org.eclipse.emf.common.notify.Adapter createConnectorAdapter()
Creates a new adapter for an object of class '[`*Connector*`](../compositestructures/mdinternalstructures/Connector.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Connector`](../compositestructures/mdinternalstructures/Connector.html)
Generated:
createConnectorEndAdapter
public org.eclipse.emf.common.notify.Adapter createConnectorEndAdapter()
Creates a new adapter for an object of class
 '[`*Connector End*`](../compositestructures/mdinternalstructures/ConnectorEnd.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ConnectorEnd`](../compositestructures/mdinternalstructures/ConnectorEnd.html)
Generated:
createConnectableElementAdapter
public org.eclipse.emf.common.notify.Adapter createConnectableElementAdapter()
Creates a new adapter for an object of class
 '[`*Connectable Element*`](../compositestructures/mdinternalstructures/ConnectableElement.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ConnectableElement`](../compositestructures/mdinternalstructures/ConnectableElement.html)
Generated:
createConnectableElementTemplateParameterAdapter
public org.eclipse.emf.common.notify.Adapter createConnectableElementTemplateParameterAdapter()
Creates a new adapter for an object of class '[`*Connectable Element Template Parameter*`](../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ConnectableElementTemplateParameter`](../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html)
Generated:
createCollaborationAdapter
public org.eclipse.emf.common.notify.Adapter createCollaborationAdapter()
Creates a new adapter for an object of class '[`*Collaboration*`](../compositestructures/mdcollaborations/Collaboration.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Collaboration`](../compositestructures/mdcollaborations/Collaboration.html)
Generated:
createCollaborationUseAdapter
public org.eclipse.emf.common.notify.Adapter createCollaborationUseAdapter()
Creates a new adapter for an object of class
 '[`*Collaboration Use*`](../compositestructures/mdcollaborations/CollaborationUse.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`CollaborationUse`](../compositestructures/mdcollaborations/CollaborationUse.html)
Generated:
createDependencyAdapter
public org.eclipse.emf.common.notify.Adapter createDependencyAdapter()
Creates a new adapter for an object of class '[`*Dependency*`](../classes/mddependencies/Dependency.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Dependency`](../classes/mddependencies/Dependency.html)
Generated:
createLifelineAdapter
public org.eclipse.emf.common.notify.Adapter createLifelineAdapter()
Creates a new adapter for an object of class '[`*Lifeline*`](../interactions/mdbasicinteractions/Lifeline.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Lifeline`](../interactions/mdbasicinteractions/Lifeline.html)
Generated:
createInteractionFragmentAdapter
public org.eclipse.emf.common.notify.Adapter createInteractionFragmentAdapter()
Creates a new adapter for an object of class
 '[`*Interaction Fragment*`](../interactions/mdbasicinteractions/InteractionFragment.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`InteractionFragment`](../interactions/mdbasicinteractions/InteractionFragment.html)
Generated:
createInteractionAdapter
public org.eclipse.emf.common.notify.Adapter createInteractionAdapter()
Creates a new adapter for an object of class '[`*Interaction*`](../interactions/mdbasicinteractions/Interaction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Interaction`](../interactions/mdbasicinteractions/Interaction.html)
Generated:
createGateAdapter
public org.eclipse.emf.common.notify.Adapter createGateAdapter()
Creates a new adapter for an object of class '[`*Gate*`](../interactions/mdfragments/Gate.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Gate`](../interactions/mdfragments/Gate.html)
Generated:
createMessageEndAdapter
public org.eclipse.emf.common.notify.Adapter createMessageEndAdapter()
Creates a new adapter for an object of class '[`*Message End*`](../interactions/mdbasicinteractions/MessageEnd.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`MessageEnd`](../interactions/mdbasicinteractions/MessageEnd.html)
Generated:
createMessageAdapter
public org.eclipse.emf.common.notify.Adapter createMessageAdapter()
Creates a new adapter for an object of class '[`*Message*`](../interactions/mdbasicinteractions/Message.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Message`](../interactions/mdbasicinteractions/Message.html)
Generated:
createInteractionUseAdapter
public org.eclipse.emf.common.notify.Adapter createInteractionUseAdapter()
Creates a new adapter for an object of class '[`*Interaction Use*`](../interactions/mdfragments/InteractionUse.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`InteractionUse`](../interactions/mdfragments/InteractionUse.html)
Generated:
createCombinedFragmentAdapter
public org.eclipse.emf.common.notify.Adapter createCombinedFragmentAdapter()
Creates a new adapter for an object of class '[`*Combined Fragment*`](../interactions/mdfragments/CombinedFragment.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`CombinedFragment`](../interactions/mdfragments/CombinedFragment.html)
Generated:
createInteractionOperandAdapter
public org.eclipse.emf.common.notify.Adapter createInteractionOperandAdapter()
Creates a new adapter for an object of class '[`*Interaction Operand*`](../interactions/mdfragments/InteractionOperand.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`InteractionOperand`](../interactions/mdfragments/InteractionOperand.html)
Generated:
createInteractionConstraintAdapter
public org.eclipse.emf.common.notify.Adapter createInteractionConstraintAdapter()
Creates a new adapter for an object of class
 '[`*Interaction Constraint*`](../interactions/mdfragments/InteractionConstraint.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`InteractionConstraint`](../interactions/mdfragments/InteractionConstraint.html)
Generated:
createGeneralOrderingAdapter
public org.eclipse.emf.common.notify.Adapter createGeneralOrderingAdapter()
Creates a new adapter for an object of class '[`*General Ordering*`](../interactions/mdbasicinteractions/GeneralOrdering.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`GeneralOrdering`](../interactions/mdbasicinteractions/GeneralOrdering.html)
Generated:
createOccurrenceSpecificationAdapter
public org.eclipse.emf.common.notify.Adapter createOccurrenceSpecificationAdapter()
Creates a new adapter for an object of class
 '[`*Occurrence Specification*`](../interactions/mdbasicinteractions/OccurrenceSpecification.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`OccurrenceSpecification`](../interactions/mdbasicinteractions/OccurrenceSpecification.html)
Generated:
createExecutionSpecificationAdapter
public org.eclipse.emf.common.notify.Adapter createExecutionSpecificationAdapter()
Creates a new adapter for an object of class
 '[`*Execution Specification*`](../interactions/mdbasicinteractions/ExecutionSpecification.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ExecutionSpecification`](../interactions/mdbasicinteractions/ExecutionSpecification.html)
Generated:
createExecutionOccurrenceSpecificationAdapter
public org.eclipse.emf.common.notify.Adapter createExecutionOccurrenceSpecificationAdapter()
Creates a new adapter for an object of class
 '[`*Execution Occurrence Specification*`](../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ExecutionOccurrenceSpecification`](../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html)
Generated:
createPartDecompositionAdapter
public org.eclipse.emf.common.notify.Adapter createPartDecompositionAdapter()
Creates a new adapter for an object of class '[`*Part Decomposition*`](../interactions/mdfragments/PartDecomposition.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`PartDecomposition`](../interactions/mdfragments/PartDecomposition.html)
Generated:
createStateInvariantAdapter
public org.eclipse.emf.common.notify.Adapter createStateInvariantAdapter()
Creates a new adapter for an object of class '[`*State Invariant*`](../interactions/mdbasicinteractions/StateInvariant.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`StateInvariant`](../interactions/mdbasicinteractions/StateInvariant.html)
Generated:
createReplyActionAdapter
public org.eclipse.emf.common.notify.Adapter createReplyActionAdapter()
Creates a new adapter for an object of class '[`*Reply Action*`](../actions/mdcompleteactions/ReplyAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ReplyAction`](../actions/mdcompleteactions/ReplyAction.html)
Generated:
createAcceptEventActionAdapter
public org.eclipse.emf.common.notify.Adapter createAcceptEventActionAdapter()
Creates a new adapter for an object of class '[`*Accept Event Action*`](../actions/mdcompleteactions/AcceptEventAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`AcceptEventAction`](../actions/mdcompleteactions/AcceptEventAction.html)
Generated:
createOutputPinAdapter
public org.eclipse.emf.common.notify.Adapter createOutputPinAdapter()
Creates a new adapter for an object of class '[`*Output Pin*`](../actions/mdbasicactions/OutputPin.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`OutputPin`](../actions/mdbasicactions/OutputPin.html)
Generated:
createClauseAdapter
public org.eclipse.emf.common.notify.Adapter createClauseAdapter()
Creates a new adapter for an object of class '[`*Clause*`](../activities/mdstructuredactivities/Clause.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Clause`](../activities/mdstructuredactivities/Clause.html)
Generated:
createConditionalNodeAdapter
public org.eclipse.emf.common.notify.Adapter createConditionalNodeAdapter()
Creates a new adapter for an object of class '[`*Conditional Node*`](../activities/mdstructuredactivities/ConditionalNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ConditionalNode`](../activities/mdstructuredactivities/ConditionalNode.html)
Generated:
createStructuredActivityNodeAdapter
public org.eclipse.emf.common.notify.Adapter createStructuredActivityNodeAdapter()
Creates a new adapter for an object of class
 '[`*Structured Activity Node*`](../activities/mdstructuredactivities/StructuredActivityNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`StructuredActivityNode`](../activities/mdstructuredactivities/StructuredActivityNode.html)
Generated:
createActivityGroupAdapter
public org.eclipse.emf.common.notify.Adapter createActivityGroupAdapter()
Creates a new adapter for an object of class '[`*Activity Group*`](../activities/mdfundamentalactivities/ActivityGroup.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ActivityGroup`](../activities/mdfundamentalactivities/ActivityGroup.html)
Generated:
createActivityEdgeAdapter
public org.eclipse.emf.common.notify.Adapter createActivityEdgeAdapter()
Creates a new adapter for an object of class '[`*Activity Edge*`](../activities/mdbasicactivities/ActivityEdge.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ActivityEdge`](../activities/mdbasicactivities/ActivityEdge.html)
Generated:
createActivityAdapter
public org.eclipse.emf.common.notify.Adapter createActivityAdapter()
Creates a new adapter for an object of class '[`*Activity*`](../activities/mdfundamentalactivities/Activity.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Activity`](../activities/mdfundamentalactivities/Activity.html)
Generated:
createActivityPartitionAdapter
public org.eclipse.emf.common.notify.Adapter createActivityPartitionAdapter()
Creates a new adapter for an object of class
 '[`*Activity Partition*`](../activities/mdintermediateactivities/ActivityPartition.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ActivityPartition`](../activities/mdintermediateactivities/ActivityPartition.html)
Generated:
createVariableAdapter
public org.eclipse.emf.common.notify.Adapter createVariableAdapter()
Creates a new adapter for an object of class '[`*Variable*`](../activities/mdstructuredactivities/Variable.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Variable`](../activities/mdstructuredactivities/Variable.html)
Generated:
createVariableActionAdapter
public org.eclipse.emf.common.notify.Adapter createVariableActionAdapter()
Creates a new adapter for an object of class '[`*Variable Action*`](../actions/mdstructuredactions/VariableAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`VariableAction`](../actions/mdstructuredactions/VariableAction.html)
Generated:
createInterruptibleActivityRegionAdapter
public org.eclipse.emf.common.notify.Adapter createInterruptibleActivityRegionAdapter()
Creates a new adapter for an object of class
 '[`*Interruptible Activity Region*`](../activities/mdcompleteactivities/InterruptibleActivityRegion.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`InterruptibleActivityRegion`](../activities/mdcompleteactivities/InterruptibleActivityRegion.html)
Generated:
createLoopNodeAdapter
public org.eclipse.emf.common.notify.Adapter createLoopNodeAdapter()
Creates a new adapter for an object of class '[`*Loop Node*`](../activities/mdstructuredactivities/LoopNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`LoopNode`](../activities/mdstructuredactivities/LoopNode.html)
Generated:
createOpaqueActionAdapter
public org.eclipse.emf.common.notify.Adapter createOpaqueActionAdapter()
Creates a new adapter for an object of class '[`*Opaque Action*`](../actions/mdbasicactions/OpaqueAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`OpaqueAction`](../actions/mdbasicactions/OpaqueAction.html)
Generated:
createCallActionAdapter
public org.eclipse.emf.common.notify.Adapter createCallActionAdapter()
Creates a new adapter for an object of class '[`*Call Action*`](../actions/mdbasicactions/CallAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`CallAction`](../actions/mdbasicactions/CallAction.html)
Generated:
createClearStructuralFeatureActionAdapter
public org.eclipse.emf.common.notify.Adapter createClearStructuralFeatureActionAdapter()
Creates a new adapter for an object of class
 '[`*Clear Structural Feature Action*`](../actions/mdintermediateactions/ClearStructuralFeatureAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ClearStructuralFeatureAction`](../actions/mdintermediateactions/ClearStructuralFeatureAction.html)
Generated:
createCreateLinkObjectActionAdapter
public org.eclipse.emf.common.notify.Adapter createCreateLinkObjectActionAdapter()
Creates a new adapter for an object of class
 '[`*Create Link Object Action*`](../actions/mdcompleteactions/CreateLinkObjectAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`CreateLinkObjectAction`](../actions/mdcompleteactions/CreateLinkObjectAction.html)
Generated:
createCreateLinkActionAdapter
public org.eclipse.emf.common.notify.Adapter createCreateLinkActionAdapter()
Creates a new adapter for an object of class '[`*Create Link Action*`](../actions/mdintermediateactions/CreateLinkAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`CreateLinkAction`](../actions/mdintermediateactions/CreateLinkAction.html)
Generated:
createWriteLinkActionAdapter
public org.eclipse.emf.common.notify.Adapter createWriteLinkActionAdapter()
Creates a new adapter for an object of class '[`*Write Link Action*`](../actions/mdintermediateactions/WriteLinkAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`WriteLinkAction`](../actions/mdintermediateactions/WriteLinkAction.html)
Generated:
createLinkActionAdapter
public org.eclipse.emf.common.notify.Adapter createLinkActionAdapter()
Creates a new adapter for an object of class '[`*Link Action*`](../actions/mdintermediateactions/LinkAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`LinkAction`](../actions/mdintermediateactions/LinkAction.html)
Generated:
createLinkEndDataAdapter
public org.eclipse.emf.common.notify.Adapter createLinkEndDataAdapter()
Creates a new adapter for an object of class '[`*Link End Data*`](../actions/mdintermediateactions/LinkEndData.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`LinkEndData`](../actions/mdintermediateactions/LinkEndData.html)
Generated:
createQualifierValueAdapter
public org.eclipse.emf.common.notify.Adapter createQualifierValueAdapter()
Creates a new adapter for an object of class '[`*Qualifier Value*`](../actions/mdcompleteactions/QualifierValue.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`QualifierValue`](../actions/mdcompleteactions/QualifierValue.html)
Generated:
createLinkEndCreationDataAdapter
public org.eclipse.emf.common.notify.Adapter createLinkEndCreationDataAdapter()
Creates a new adapter for an object of class
 '[`*Link End Creation Data*`](../actions/mdintermediateactions/LinkEndCreationData.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`LinkEndCreationData`](../actions/mdintermediateactions/LinkEndCreationData.html)
Generated:
createCreateObjectActionAdapter
public org.eclipse.emf.common.notify.Adapter createCreateObjectActionAdapter()
Creates a new adapter for an object of class
 '[`*Create Object Action*`](../actions/mdintermediateactions/CreateObjectAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`CreateObjectAction`](../actions/mdintermediateactions/CreateObjectAction.html)
Generated:
createReadExtentActionAdapter
public org.eclipse.emf.common.notify.Adapter createReadExtentActionAdapter()
Creates a new adapter for an object of class '[`*Read Extent Action*`](../actions/mdcompleteactions/ReadExtentAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ReadExtentAction`](../actions/mdcompleteactions/ReadExtentAction.html)
Generated:
createReadIsClassifiedObjectActionAdapter
public org.eclipse.emf.common.notify.Adapter createReadIsClassifiedObjectActionAdapter()
Creates a new adapter for an object of class
 '[`*Read Is Classified Object Action*`](../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ReadIsClassifiedObjectAction`](../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html)
Generated:
createReadLinkActionAdapter
public org.eclipse.emf.common.notify.Adapter createReadLinkActionAdapter()
Creates a new adapter for an object of class '[`*Read Link Action*`](../actions/mdintermediateactions/ReadLinkAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ReadLinkAction`](../actions/mdintermediateactions/ReadLinkAction.html)
Generated:
createReadLinkObjectEndActionAdapter
public org.eclipse.emf.common.notify.Adapter createReadLinkObjectEndActionAdapter()
Creates a new adapter for an object of class
 '[`*Read Link Object End Action*`](../actions/mdcompleteactions/ReadLinkObjectEndAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ReadLinkObjectEndAction`](../actions/mdcompleteactions/ReadLinkObjectEndAction.html)
Generated:
createReadLinkObjectEndQualifierActionAdapter
public org.eclipse.emf.common.notify.Adapter createReadLinkObjectEndQualifierActionAdapter()
Creates a new adapter for an object of class
 '[`*Read Link Object End Qualifier Action*`](../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ReadLinkObjectEndQualifierAction`](../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html)
Generated:
createReadSelfActionAdapter
public org.eclipse.emf.common.notify.Adapter createReadSelfActionAdapter()
Creates a new adapter for an object of class '[`*Read Self Action*`](../actions/mdintermediateactions/ReadSelfAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ReadSelfAction`](../actions/mdintermediateactions/ReadSelfAction.html)
Generated:
createReadStructuralFeatureActionAdapter
public org.eclipse.emf.common.notify.Adapter createReadStructuralFeatureActionAdapter()
Creates a new adapter for an object of class
 '[`*Read Structural Feature Action*`](../actions/mdintermediateactions/ReadStructuralFeatureAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ReadStructuralFeatureAction`](../actions/mdintermediateactions/ReadStructuralFeatureAction.html)
Generated:
createReadVariableActionAdapter
public org.eclipse.emf.common.notify.Adapter createReadVariableActionAdapter()
Creates a new adapter for an object of class
 '[`*Read Variable Action*`](../actions/mdstructuredactions/ReadVariableAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ReadVariableAction`](../actions/mdstructuredactions/ReadVariableAction.html)
Generated:
createReduceActionAdapter
public org.eclipse.emf.common.notify.Adapter createReduceActionAdapter()
Creates a new adapter for an object of class '[`*Reduce Action*`](../actions/mdcompleteactions/ReduceAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ReduceAction`](../actions/mdcompleteactions/ReduceAction.html)
Generated:
createTestIdentityActionAdapter
public org.eclipse.emf.common.notify.Adapter createTestIdentityActionAdapter()
Creates a new adapter for an object of class
 '[`*Test Identity Action*`](../actions/mdintermediateactions/TestIdentityAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`TestIdentityAction`](../actions/mdintermediateactions/TestIdentityAction.html)
Generated:
createUnmarshallActionAdapter
public org.eclipse.emf.common.notify.Adapter createUnmarshallActionAdapter()
Creates a new adapter for an object of class '[`*Unmarshall Action*`](../actions/mdcompleteactions/UnmarshallAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`UnmarshallAction`](../actions/mdcompleteactions/UnmarshallAction.html)
Generated:
createValueSpecificationActionAdapter
public org.eclipse.emf.common.notify.Adapter createValueSpecificationActionAdapter()
Creates a new adapter for an object of class
 '[`*Value Specification Action*`](../actions/mdintermediateactions/ValueSpecificationAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ValueSpecificationAction`](../actions/mdintermediateactions/ValueSpecificationAction.html)
Generated:
createWriteStructuralFeatureActionAdapter
public org.eclipse.emf.common.notify.Adapter createWriteStructuralFeatureActionAdapter()
Creates a new adapter for an object of class
 '[`*Write Structural Feature Action*`](../actions/mdintermediateactions/WriteStructuralFeatureAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`WriteStructuralFeatureAction`](../actions/mdintermediateactions/WriteStructuralFeatureAction.html)
Generated:
createAcceptCallActionAdapter
public org.eclipse.emf.common.notify.Adapter createAcceptCallActionAdapter()
Creates a new adapter for an object of class '[`*Accept Call Action*`](../actions/mdcompleteactions/AcceptCallAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`AcceptCallAction`](../actions/mdcompleteactions/AcceptCallAction.html)
Generated:
createInterfaceRealizationAdapter
public org.eclipse.emf.common.notify.Adapter createInterfaceRealizationAdapter()
Creates a new adapter for an object of class '[`*Interface Realization*`](../classes/mdinterfaces/InterfaceRealization.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`InterfaceRealization`](../classes/mdinterfaces/InterfaceRealization.html)
Generated:
createRealizationAdapter
public org.eclipse.emf.common.notify.Adapter createRealizationAdapter()
Creates a new adapter for an object of class '[`*Realization*`](../classes/mddependencies/Realization.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Realization`](../classes/mddependencies/Realization.html)
Generated:
createAbstractionAdapter
public org.eclipse.emf.common.notify.Adapter createAbstractionAdapter()
Creates a new adapter for an object of class '[`*Abstraction*`](../classes/mddependencies/Abstraction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Abstraction`](../classes/mddependencies/Abstraction.html)
Generated:
createOpaqueExpressionAdapter
public org.eclipse.emf.common.notify.Adapter createOpaqueExpressionAdapter()
Creates a new adapter for an object of class '[`*Opaque Expression*`](../classes/mdkernel/OpaqueExpression.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`OpaqueExpression`](../classes/mdkernel/OpaqueExpression.html)
Generated:
createComponentAdapter
public org.eclipse.emf.common.notify.Adapter createComponentAdapter()
Creates a new adapter for an object of class '[`*Component*`](../components/mdbasiccomponents/Component.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Component`](../components/mdbasiccomponents/Component.html)
Generated:
createComponentRealizationAdapter
public org.eclipse.emf.common.notify.Adapter createComponentRealizationAdapter()
Creates a new adapter for an object of class
 '[`*Component Realization*`](../components/mdbasiccomponents/ComponentRealization.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ComponentRealization`](../components/mdbasiccomponents/ComponentRealization.html)
Generated:
createOperationTemplateParameterAdapter
public org.eclipse.emf.common.notify.Adapter createOperationTemplateParameterAdapter()
Creates a new adapter for an object of class
 '[`*Operation Template Parameter*`](../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`OperationTemplateParameter`](../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html)
Generated:
createCallEventAdapter
public org.eclipse.emf.common.notify.Adapter createCallEventAdapter()
Creates a new adapter for an object of class '[`*Call Event*`](../commonbehaviors/mdcommunications/CallEvent.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`CallEvent`](../commonbehaviors/mdcommunications/CallEvent.html)
Generated:
createCallOperationActionAdapter
public org.eclipse.emf.common.notify.Adapter createCallOperationActionAdapter()
Creates a new adapter for an object of class '[`*Call Operation Action*`](../actions/mdbasicactions/CallOperationAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`CallOperationAction`](../actions/mdbasicactions/CallOperationAction.html)
Generated:
createArtifactAdapter
public org.eclipse.emf.common.notify.Adapter createArtifactAdapter()
Creates a new adapter for an object of class '[`*Artifact*`](../deployments/mdartifacts/Artifact.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Artifact`](../deployments/mdartifacts/Artifact.html)
Generated:
createDeployedArtifactAdapter
public org.eclipse.emf.common.notify.Adapter createDeployedArtifactAdapter()
Creates a new adapter for an object of class '[`*Deployed Artifact*`](../deployments/mdnodes/DeployedArtifact.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DeployedArtifact`](../deployments/mdnodes/DeployedArtifact.html)
Generated:
createDeploymentAdapter
public org.eclipse.emf.common.notify.Adapter createDeploymentAdapter()
Creates a new adapter for an object of class '[`*Deployment*`](../deployments/mdnodes/Deployment.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Deployment`](../deployments/mdnodes/Deployment.html)
Generated:
createDeploymentSpecificationAdapter
public org.eclipse.emf.common.notify.Adapter createDeploymentSpecificationAdapter()
Creates a new adapter for an object of class
 '[`*Deployment Specification*`](../deployments/mdcomponentdeployments/DeploymentSpecification.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DeploymentSpecification`](../deployments/mdcomponentdeployments/DeploymentSpecification.html)
Generated:
createDeploymentTargetAdapter
public org.eclipse.emf.common.notify.Adapter createDeploymentTargetAdapter()
Creates a new adapter for an object of class '[`*Deployment Target*`](../deployments/mdnodes/DeploymentTarget.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DeploymentTarget`](../deployments/mdnodes/DeploymentTarget.html)
Generated:
createManifestationAdapter
public org.eclipse.emf.common.notify.Adapter createManifestationAdapter()
Creates a new adapter for an object of class '[`*Manifestation*`](../deployments/mdartifacts/Manifestation.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Manifestation`](../deployments/mdartifacts/Manifestation.html)
Generated:
createProtocolTransitionAdapter
public org.eclipse.emf.common.notify.Adapter createProtocolTransitionAdapter()
Creates a new adapter for an object of class
 '[`*Protocol Transition*`](../statemachines/mdprotocolstatemachines/ProtocolTransition.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ProtocolTransition`](../statemachines/mdprotocolstatemachines/ProtocolTransition.html)
Generated:
createExtendAdapter
public org.eclipse.emf.common.notify.Adapter createExtendAdapter()
Creates a new adapter for an object of class '[`*Extend*`](../mdusecases/Extend.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Extend`](../mdusecases/Extend.html)
Generated:
createUseCaseAdapter
public org.eclipse.emf.common.notify.Adapter createUseCaseAdapter()
Creates a new adapter for an object of class '[`*Use Case*`](../mdusecases/UseCase.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`UseCase`](../mdusecases/UseCase.html)
Generated:
createExtensionPointAdapter
public org.eclipse.emf.common.notify.Adapter createExtensionPointAdapter()
Creates a new adapter for an object of class '[`*Extension Point*`](../mdusecases/ExtensionPoint.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ExtensionPoint`](../mdusecases/ExtensionPoint.html)
Generated:
createIncludeAdapter
public org.eclipse.emf.common.notify.Adapter createIncludeAdapter()
Creates a new adapter for an object of class '[`*Include*`](../mdusecases/Include.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Include`](../mdusecases/Include.html)
Generated:
createExceptionHandlerAdapter
public org.eclipse.emf.common.notify.Adapter createExceptionHandlerAdapter()
Creates a new adapter for an object of class
 '[`*Exception Handler*`](../activities/mdextrastructuredactivities/ExceptionHandler.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ExceptionHandler`](../activities/mdextrastructuredactivities/ExceptionHandler.html)
Generated:
createLinkEndDestructionDataAdapter
public org.eclipse.emf.common.notify.Adapter createLinkEndDestructionDataAdapter()
Creates a new adapter for an object of class
 '[`*Link End Destruction Data*`](../actions/mdintermediateactions/LinkEndDestructionData.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`LinkEndDestructionData`](../actions/mdintermediateactions/LinkEndDestructionData.html)
Generated:
createDestroyLinkActionAdapter
public org.eclipse.emf.common.notify.Adapter createDestroyLinkActionAdapter()
Creates a new adapter for an object of class
 '[`*Destroy Link Action*`](../actions/mdintermediateactions/DestroyLinkAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DestroyLinkAction`](../actions/mdintermediateactions/DestroyLinkAction.html)
Generated:
createRaiseExceptionActionAdapter
public org.eclipse.emf.common.notify.Adapter createRaiseExceptionActionAdapter()
Creates a new adapter for an object of class
 '[`*Raise Exception Action*`](../actions/mdstructuredactions/RaiseExceptionAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`RaiseExceptionAction`](../actions/mdstructuredactions/RaiseExceptionAction.html)
Generated:
createAddStructuralFeatureValueActionAdapter
public org.eclipse.emf.common.notify.Adapter createAddStructuralFeatureValueActionAdapter()
Creates a new adapter for an object of class
 '[`*Add Structural Feature Value Action*`](../actions/mdintermediateactions/AddStructuralFeatureValueAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`AddStructuralFeatureValueAction`](../actions/mdintermediateactions/AddStructuralFeatureValueAction.html)
Generated:
createAddVariableValueActionAdapter
public org.eclipse.emf.common.notify.Adapter createAddVariableValueActionAdapter()
Creates a new adapter for an object of class
 '[`*Add Variable Value Action*`](../actions/mdstructuredactions/AddVariableValueAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`AddVariableValueAction`](../actions/mdstructuredactions/AddVariableValueAction.html)
Generated:
createWriteVariableActionAdapter
public org.eclipse.emf.common.notify.Adapter createWriteVariableActionAdapter()
Creates a new adapter for an object of class
 '[`*Write Variable Action*`](../actions/mdstructuredactions/WriteVariableAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`WriteVariableAction`](../actions/mdstructuredactions/WriteVariableAction.html)
Generated:
createClearAssociationActionAdapter
public org.eclipse.emf.common.notify.Adapter createClearAssociationActionAdapter()
Creates a new adapter for an object of class
 '[`*Clear Association Action*`](../actions/mdintermediateactions/ClearAssociationAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ClearAssociationAction`](../actions/mdintermediateactions/ClearAssociationAction.html)
Generated:
createReclassifyObjectActionAdapter
public org.eclipse.emf.common.notify.Adapter createReclassifyObjectActionAdapter()
Creates a new adapter for an object of class
 '[`*Reclassify Object Action*`](../actions/mdcompleteactions/ReclassifyObjectAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ReclassifyObjectAction`](../actions/mdcompleteactions/ReclassifyObjectAction.html)
Generated:
createStartClassifierBehaviorActionAdapter
public org.eclipse.emf.common.notify.Adapter createStartClassifierBehaviorActionAdapter()
Creates a new adapter for an object of class
 '[`*Start Classifier Behavior Action*`](../actions/mdcompleteactions/StartClassifierBehaviorAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`StartClassifierBehaviorAction`](../actions/mdcompleteactions/StartClassifierBehaviorAction.html)
Generated:
createStartObjectBehaviorActionAdapter
public org.eclipse.emf.common.notify.Adapter createStartObjectBehaviorActionAdapter()
Creates a new adapter for an object of class
 '[`*Start Object Behavior Action*`](../actions/mdcompleteactions/StartObjectBehaviorAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`StartObjectBehaviorAction`](../actions/mdcompleteactions/StartObjectBehaviorAction.html)
Generated:
createRemoveStructuralFeatureValueActionAdapter
public org.eclipse.emf.common.notify.Adapter createRemoveStructuralFeatureValueActionAdapter()
Creates a new adapter for an object of class '[`*Remove
 Structural Feature Value Action*`](../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`RemoveStructuralFeatureValueAction`](../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html)
Generated:
createRemoveVariableValueActionAdapter
public org.eclipse.emf.common.notify.Adapter createRemoveVariableValueActionAdapter()
Creates a new adapter for an object of class
 '[`*Remove Variable Value Action*`](../actions/mdstructuredactions/RemoveVariableValueAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`RemoveVariableValueAction`](../actions/mdstructuredactions/RemoveVariableValueAction.html)
Generated:
createSendObjectActionAdapter
public org.eclipse.emf.common.notify.Adapter createSendObjectActionAdapter()
Creates a new adapter for an object of class '[`*Send Object Action*`](../actions/mdintermediateactions/SendObjectAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`SendObjectAction`](../actions/mdintermediateactions/SendObjectAction.html)
Generated:
createDestroyObjectActionAdapter
public org.eclipse.emf.common.notify.Adapter createDestroyObjectActionAdapter()
Creates a new adapter for an object of class
 '[`*Destroy Object Action*`](../actions/mdintermediateactions/DestroyObjectAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DestroyObjectAction`](../actions/mdintermediateactions/DestroyObjectAction.html)
Generated:
createChangeEventAdapter
public org.eclipse.emf.common.notify.Adapter createChangeEventAdapter()
Creates a new adapter for an object of class '[`*Change Event*`](../commonbehaviors/mdcommunications/ChangeEvent.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ChangeEvent`](../commonbehaviors/mdcommunications/ChangeEvent.html)
Generated:
createDurationAdapter
public org.eclipse.emf.common.notify.Adapter createDurationAdapter()
Creates a new adapter for an object of class '[`*Duration*`](../commonbehaviors/mdsimpletime/Duration.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Duration`](../commonbehaviors/mdsimpletime/Duration.html)
Generated:
createObservationAdapter
public org.eclipse.emf.common.notify.Adapter createObservationAdapter()
Creates a new adapter for an object of class '[`*Observation*`](../commonbehaviors/mdsimpletime/Observation.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Observation`](../commonbehaviors/mdsimpletime/Observation.html)
Generated:
createTimeExpressionAdapter
public org.eclipse.emf.common.notify.Adapter createTimeExpressionAdapter()
Creates a new adapter for an object of class '[`*Time Expression*`](../commonbehaviors/mdsimpletime/TimeExpression.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`TimeExpression`](../commonbehaviors/mdsimpletime/TimeExpression.html)
Generated:
createTimeIntervalAdapter
public org.eclipse.emf.common.notify.Adapter createTimeIntervalAdapter()
Creates a new adapter for an object of class '[`*Time Interval*`](../commonbehaviors/mdsimpletime/TimeInterval.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`TimeInterval`](../commonbehaviors/mdsimpletime/TimeInterval.html)
Generated:
createIntervalAdapter
public org.eclipse.emf.common.notify.Adapter createIntervalAdapter()
Creates a new adapter for an object of class '[`*Interval*`](../commonbehaviors/mdsimpletime/Interval.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Interval`](../commonbehaviors/mdsimpletime/Interval.html)
Generated:
createIntervalConstraintAdapter
public org.eclipse.emf.common.notify.Adapter createIntervalConstraintAdapter()
Creates a new adapter for an object of class
 '[`*Interval Constraint*`](../commonbehaviors/mdsimpletime/IntervalConstraint.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`IntervalConstraint`](../commonbehaviors/mdsimpletime/IntervalConstraint.html)
Generated:
createTimeConstraintAdapter
public org.eclipse.emf.common.notify.Adapter createTimeConstraintAdapter()
Creates a new adapter for an object of class '[`*Time Constraint*`](../commonbehaviors/mdsimpletime/TimeConstraint.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`TimeConstraint`](../commonbehaviors/mdsimpletime/TimeConstraint.html)
Generated:
createTimeEventAdapter
public org.eclipse.emf.common.notify.Adapter createTimeEventAdapter()
Creates a new adapter for an object of class '[`*Time Event*`](../commonbehaviors/mdcommunications/TimeEvent.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`TimeEvent`](../commonbehaviors/mdcommunications/TimeEvent.html)
Generated:
createDurationIntervalAdapter
public org.eclipse.emf.common.notify.Adapter createDurationIntervalAdapter()
Creates a new adapter for an object of class '[`*Duration Interval*`](../commonbehaviors/mdsimpletime/DurationInterval.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DurationInterval`](../commonbehaviors/mdsimpletime/DurationInterval.html)
Generated:
createDurationConstraintAdapter
public org.eclipse.emf.common.notify.Adapter createDurationConstraintAdapter()
Creates a new adapter for an object of class
 '[`*Duration Constraint*`](../commonbehaviors/mdsimpletime/DurationConstraint.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DurationConstraint`](../commonbehaviors/mdsimpletime/DurationConstraint.html)
Generated:
createJoinNodeAdapter
public org.eclipse.emf.common.notify.Adapter createJoinNodeAdapter()
Creates a new adapter for an object of class '[`*Join Node*`](../activities/mdintermediateactivities/JoinNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`JoinNode`](../activities/mdintermediateactivities/JoinNode.html)
Generated:
createControlNodeAdapter
public org.eclipse.emf.common.notify.Adapter createControlNodeAdapter()
Creates a new adapter for an object of class '[`*Control Node*`](../activities/mdbasicactivities/ControlNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ControlNode`](../activities/mdbasicactivities/ControlNode.html)
Generated:
createExpressionAdapter
public org.eclipse.emf.common.notify.Adapter createExpressionAdapter()
Creates a new adapter for an object of class '[`*Expression*`](../classes/mdkernel/Expression.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Expression`](../classes/mdkernel/Expression.html)
Generated:
createValuePinAdapter
public org.eclipse.emf.common.notify.Adapter createValuePinAdapter()
Creates a new adapter for an object of class '[`*Value Pin*`](../actions/mdbasicactions/ValuePin.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ValuePin`](../actions/mdbasicactions/ValuePin.html)
Generated:
createActivityParameterNodeAdapter
public org.eclipse.emf.common.notify.Adapter createActivityParameterNodeAdapter()
Creates a new adapter for an object of class
 '[`*Activity Parameter Node*`](../activities/mdbasicactivities/ActivityParameterNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ActivityParameterNode`](../activities/mdbasicactivities/ActivityParameterNode.html)
Generated:
createBehaviorExecutionSpecificationAdapter
public org.eclipse.emf.common.notify.Adapter createBehaviorExecutionSpecificationAdapter()
Creates a new adapter for an object of class
 '[`*Behavior Execution Specification*`](../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`BehaviorExecutionSpecification`](../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html)
Generated:
createCallBehaviorActionAdapter
public org.eclipse.emf.common.notify.Adapter createCallBehaviorActionAdapter()
Creates a new adapter for an object of class '[`*Call Behavior Action*`](../actions/mdbasicactions/CallBehaviorAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`CallBehaviorAction`](../actions/mdbasicactions/CallBehaviorAction.html)
Generated:
createDecisionNodeAdapter
public org.eclipse.emf.common.notify.Adapter createDecisionNodeAdapter()
Creates a new adapter for an object of class '[`*Decision Node*`](../activities/mdintermediateactivities/DecisionNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DecisionNode`](../activities/mdintermediateactivities/DecisionNode.html)
Generated:
createObjectFlowAdapter
public org.eclipse.emf.common.notify.Adapter createObjectFlowAdapter()
Creates a new adapter for an object of class '[`*Object Flow*`](../activities/mdbasicactivities/ObjectFlow.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ObjectFlow`](../activities/mdbasicactivities/ObjectFlow.html)
Generated:
createExtensionAdapter
public org.eclipse.emf.common.notify.Adapter createExtensionAdapter()
Creates a new adapter for an object of class '[`*Extension*`](../mdprofiles/Extension.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Extension`](../mdprofiles/Extension.html)
Generated:
createExtensionEndAdapter
public org.eclipse.emf.common.notify.Adapter createExtensionEndAdapter()
Creates a new adapter for an object of class '[`*Extension End*`](../mdprofiles/ExtensionEnd.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ExtensionEnd`](../mdprofiles/ExtensionEnd.html)
Generated:
createImageAdapter
public org.eclipse.emf.common.notify.Adapter createImageAdapter()
Creates a new adapter for an object of class '[`*Image*`](../mdprofiles/Image.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Image`](../mdprofiles/Image.html)
Generated:
createPackageMergeAdapter
public org.eclipse.emf.common.notify.Adapter createPackageMergeAdapter()
Creates a new adapter for an object of class '[`*Package Merge*`](../classes/mdkernel/PackageMerge.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`PackageMerge`](../classes/mdkernel/PackageMerge.html)
Generated:
createProfileApplicationAdapter
public org.eclipse.emf.common.notify.Adapter createProfileApplicationAdapter()
Creates a new adapter for an object of class '[`*Profile Application*`](../mdprofiles/ProfileApplication.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ProfileApplication`](../mdprofiles/ProfileApplication.html)
Generated:
createPackageImportAdapter
public org.eclipse.emf.common.notify.Adapter createPackageImportAdapter()
Creates a new adapter for an object of class '[`*Package Import*`](../classes/mdkernel/PackageImport.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`PackageImport`](../classes/mdkernel/PackageImport.html)
Generated:
createDiagramAdapter
public org.eclipse.emf.common.notify.Adapter createDiagramAdapter()
Creates a new adapter for an object of class '[`*Diagram*`](../classes/mdkernel/Diagram.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Diagram`](../classes/mdkernel/Diagram.html)
Generated:
createGeneralizationAdapter
public org.eclipse.emf.common.notify.Adapter createGeneralizationAdapter()
Creates a new adapter for an object of class '[`*Generalization*`](../classes/mdkernel/Generalization.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Generalization`](../classes/mdkernel/Generalization.html)
Generated:
createGeneralizationSetAdapter
public org.eclipse.emf.common.notify.Adapter createGeneralizationSetAdapter()
Creates a new adapter for an object of class '[`*Generalization Set*`](../classes/mdpowertypes/GeneralizationSet.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`GeneralizationSet`](../classes/mdpowertypes/GeneralizationSet.html)
Generated:
createRedefinableTemplateSignatureAdapter
public org.eclipse.emf.common.notify.Adapter createRedefinableTemplateSignatureAdapter()
Creates a new adapter for an object of class
 '[`*Redefinable Template Signature*`](../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`RedefinableTemplateSignature`](../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html)
Generated:
createSubstitutionAdapter
public org.eclipse.emf.common.notify.Adapter createSubstitutionAdapter()
Creates a new adapter for an object of class '[`*Substitution*`](../classes/mddependencies/Substitution.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Substitution`](../classes/mddependencies/Substitution.html)
Generated:
createClassifierTemplateParameterAdapter
public org.eclipse.emf.common.notify.Adapter createClassifierTemplateParameterAdapter()
Creates a new adapter for an object of class
 '[`*Classifier Template Parameter*`](../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ClassifierTemplateParameter`](../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html)
Generated:
createInformationItemAdapter
public org.eclipse.emf.common.notify.Adapter createInformationItemAdapter()
Creates a new adapter for an object of class
 '[`*Information Item*`](../auxiliaryconstructs/mdinformationflows/InformationItem.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`InformationItem`](../auxiliaryconstructs/mdinformationflows/InformationItem.html)
Generated:
createTemplateParameterSubstitutionAdapter
public org.eclipse.emf.common.notify.Adapter createTemplateParameterSubstitutionAdapter()
Creates a new adapter for an object of class
 '[`*Template Parameter Substitution*`](../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`TemplateParameterSubstitution`](../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html)
Generated:
createInstanceValueAdapter
public org.eclipse.emf.common.notify.Adapter createInstanceValueAdapter()
Creates a new adapter for an object of class '[`*Instance Value*`](../classes/mdkernel/InstanceValue.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`InstanceValue`](../classes/mdkernel/InstanceValue.html)
Generated:
createElementValueAdapter
public org.eclipse.emf.common.notify.Adapter createElementValueAdapter()
Creates a new adapter for an object of class '[`*Element Value*`](../classes/mdkernel/ElementValue.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ElementValue`](../classes/mdkernel/ElementValue.html)
Generated:
createStringExpressionAdapter
public org.eclipse.emf.common.notify.Adapter createStringExpressionAdapter()
Creates a new adapter for an object of class '[`*String Expression*`](../auxiliaryconstructs/mdtemplates/StringExpression.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`StringExpression`](../auxiliaryconstructs/mdtemplates/StringExpression.html)
Generated:
createDurationObservationAdapter
public org.eclipse.emf.common.notify.Adapter createDurationObservationAdapter()
Creates a new adapter for an object of class
 '[`*Duration Observation*`](../commonbehaviors/mdsimpletime/DurationObservation.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DurationObservation`](../commonbehaviors/mdsimpletime/DurationObservation.html)
Generated:
createTimeObservationAdapter
public org.eclipse.emf.common.notify.Adapter createTimeObservationAdapter()
Creates a new adapter for an object of class '[`*Time Observation*`](../commonbehaviors/mdsimpletime/TimeObservation.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`TimeObservation`](../commonbehaviors/mdsimpletime/TimeObservation.html)
Generated:
createConsiderIgnoreFragmentAdapter
public org.eclipse.emf.common.notify.Adapter createConsiderIgnoreFragmentAdapter()
Creates a new adapter for an object of class
 '[`*Consider Ignore Fragment*`](../interactions/mdfragments/ConsiderIgnoreFragment.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ConsiderIgnoreFragment`](../interactions/mdfragments/ConsiderIgnoreFragment.html)
Generated:
createSequenceNodeAdapter
public org.eclipse.emf.common.notify.Adapter createSequenceNodeAdapter()
Creates a new adapter for an object of class '[`*Sequence Node*`](../activities/mdstructuredactivities/SequenceNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`SequenceNode`](../activities/mdstructuredactivities/SequenceNode.html)
Generated:
createActionExecutionSpecificationAdapter
public org.eclipse.emf.common.notify.Adapter createActionExecutionSpecificationAdapter()
Creates a new adapter for an object of class
 '[`*Action Execution Specification*`](../interactions/mdbasicinteractions/ActionExecutionSpecification.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ActionExecutionSpecification`](../interactions/mdbasicinteractions/ActionExecutionSpecification.html)
Generated:
createActionInputPinAdapter
public org.eclipse.emf.common.notify.Adapter createActionInputPinAdapter()
Creates a new adapter for an object of class '[`*Action Input Pin*`](../actions/mdstructuredactions/ActionInputPin.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ActionInputPin`](../actions/mdstructuredactions/ActionInputPin.html)
Generated:
createLiteralStringAdapter
public org.eclipse.emf.common.notify.Adapter createLiteralStringAdapter()
Creates a new adapter for an object of class '[`*Literal String*`](../classes/mdkernel/LiteralString.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`LiteralString`](../classes/mdkernel/LiteralString.html)
Generated:
createLiteralSpecificationAdapter
public org.eclipse.emf.common.notify.Adapter createLiteralSpecificationAdapter()
Creates a new adapter for an object of class '[`*Literal Specification*`](../classes/mdkernel/LiteralSpecification.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`LiteralSpecification`](../classes/mdkernel/LiteralSpecification.html)
Generated:
createDataStoreNodeAdapter
public org.eclipse.emf.common.notify.Adapter createDataStoreNodeAdapter()
Creates a new adapter for an object of class '[`*Data Store Node*`](../activities/mdcompleteactivities/DataStoreNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DataStoreNode`](../activities/mdcompleteactivities/DataStoreNode.html)
Generated:
createCentralBufferNodeAdapter
public org.eclipse.emf.common.notify.Adapter createCentralBufferNodeAdapter()
Creates a new adapter for an object of class
 '[`*Central Buffer Node*`](../activities/mdintermediateactivities/CentralBufferNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`CentralBufferNode`](../activities/mdintermediateactivities/CentralBufferNode.html)
Generated:
createInitialNodeAdapter
public org.eclipse.emf.common.notify.Adapter createInitialNodeAdapter()
Creates a new adapter for an object of class '[`*Initial Node*`](../activities/mdbasicactivities/InitialNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`InitialNode`](../activities/mdbasicactivities/InitialNode.html)
Generated:
createDeviceAdapter
public org.eclipse.emf.common.notify.Adapter createDeviceAdapter()
Creates a new adapter for an object of class '[`*Device*`](../deployments/mdnodes/Device.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Device`](../deployments/mdnodes/Device.html)
Generated:
createNodeAdapter
public org.eclipse.emf.common.notify.Adapter createNodeAdapter()
Creates a new adapter for an object of class '[`*Node*`](../deployments/mdnodes/Node.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Node`](../deployments/mdnodes/Node.html)
Generated:
createAssociationClassAdapter
public org.eclipse.emf.common.notify.Adapter createAssociationClassAdapter()
Creates a new adapter for an object of class '[`*Association Class*`](../classes/mdassociationclasses/AssociationClass.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`AssociationClass`](../classes/mdassociationclasses/AssociationClass.html)
Generated:
createActorAdapter
public org.eclipse.emf.common.notify.Adapter createActorAdapter()
Creates a new adapter for an object of class '[`*Actor*`](../mdusecases/Actor.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Actor`](../mdusecases/Actor.html)
Generated:
createExecutionEnvironmentAdapter
public org.eclipse.emf.common.notify.Adapter createExecutionEnvironmentAdapter()
Creates a new adapter for an object of class '[`*Execution Environment*`](../deployments/mdnodes/ExecutionEnvironment.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ExecutionEnvironment`](../deployments/mdnodes/ExecutionEnvironment.html)
Generated:
createFunctionBehaviorAdapter
public org.eclipse.emf.common.notify.Adapter createFunctionBehaviorAdapter()
Creates a new adapter for an object of class
 '[`*Function Behavior*`](../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`FunctionBehavior`](../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html)
Generated:
createOpaqueBehaviorAdapter
public org.eclipse.emf.common.notify.Adapter createOpaqueBehaviorAdapter()
Creates a new adapter for an object of class '[`*Opaque Behavior*`](../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`OpaqueBehavior`](../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html)
Generated:
createFinalNodeAdapter
public org.eclipse.emf.common.notify.Adapter createFinalNodeAdapter()
Creates a new adapter for an object of class '[`*Final Node*`](../activities/mdintermediateactivities/FinalNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`FinalNode`](../activities/mdintermediateactivities/FinalNode.html)
Generated:
createActivityFinalNodeAdapter
public org.eclipse.emf.common.notify.Adapter createActivityFinalNodeAdapter()
Creates a new adapter for an object of class '[`*Activity Final Node*`](../activities/mdbasicactivities/ActivityFinalNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ActivityFinalNode`](../activities/mdbasicactivities/ActivityFinalNode.html)
Generated:
createFlowFinalNodeAdapter
public org.eclipse.emf.common.notify.Adapter createFlowFinalNodeAdapter()
Creates a new adapter for an object of class '[`*Flow Final Node*`](../activities/mdintermediateactivities/FlowFinalNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`FlowFinalNode`](../activities/mdintermediateactivities/FlowFinalNode.html)
Generated:
createLiteralRealAdapter
public org.eclipse.emf.common.notify.Adapter createLiteralRealAdapter()
Creates a new adapter for an object of class '[`*Literal Real*`](../classes/mdkernel/LiteralReal.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`LiteralReal`](../classes/mdkernel/LiteralReal.html)
Generated:
createForkNodeAdapter
public org.eclipse.emf.common.notify.Adapter createForkNodeAdapter()
Creates a new adapter for an object of class '[`*Fork Node*`](../activities/mdintermediateactivities/ForkNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ForkNode`](../activities/mdintermediateactivities/ForkNode.html)
Generated:
createControlFlowAdapter
public org.eclipse.emf.common.notify.Adapter createControlFlowAdapter()
Creates a new adapter for an object of class '[`*Control Flow*`](../activities/mdbasicactivities/ControlFlow.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ControlFlow`](../activities/mdbasicactivities/ControlFlow.html)
Generated:
createUsageAdapter
public org.eclipse.emf.common.notify.Adapter createUsageAdapter()
Creates a new adapter for an object of class '[`*Usage*`](../classes/mddependencies/Usage.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Usage`](../classes/mddependencies/Usage.html)
Generated:
createLiteralUnlimitedNaturalAdapter
public org.eclipse.emf.common.notify.Adapter createLiteralUnlimitedNaturalAdapter()
Creates a new adapter for an object of class '[`*Literal Unlimited Natural*`](../classes/mdkernel/LiteralUnlimitedNatural.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`LiteralUnlimitedNatural`](../classes/mdkernel/LiteralUnlimitedNatural.html)
Generated:
createLiteralIntegerAdapter
public org.eclipse.emf.common.notify.Adapter createLiteralIntegerAdapter()
Creates a new adapter for an object of class '[`*Literal Integer*`](../classes/mdkernel/LiteralInteger.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`LiteralInteger`](../classes/mdkernel/LiteralInteger.html)
Generated:
createEnumerationAdapter
public org.eclipse.emf.common.notify.Adapter createEnumerationAdapter()
Creates a new adapter for an object of class '[`*Enumeration*`](../classes/mdkernel/Enumeration.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Enumeration`](../classes/mdkernel/Enumeration.html)
Generated:
createEnumerationLiteralAdapter
public org.eclipse.emf.common.notify.Adapter createEnumerationLiteralAdapter()
Creates a new adapter for an object of class '[`*Enumeration Literal*`](../classes/mdkernel/EnumerationLiteral.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`EnumerationLiteral`](../classes/mdkernel/EnumerationLiteral.html)
Generated:
createExpansionNodeAdapter
public org.eclipse.emf.common.notify.Adapter createExpansionNodeAdapter()
Creates a new adapter for an object of class
 '[`*Expansion Node*`](../activities/mdextrastructuredactivities/ExpansionNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ExpansionNode`](../activities/mdextrastructuredactivities/ExpansionNode.html)
Generated:
createExpansionRegionAdapter
public org.eclipse.emf.common.notify.Adapter createExpansionRegionAdapter()
Creates a new adapter for an object of class
 '[`*Expansion Region*`](../activities/mdextrastructuredactivities/ExpansionRegion.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ExpansionRegion`](../activities/mdextrastructuredactivities/ExpansionRegion.html)
Generated:
createCommunicationPathAdapter
public org.eclipse.emf.common.notify.Adapter createCommunicationPathAdapter()
Creates a new adapter for an object of class '[`*Communication Path*`](../deployments/mdnodes/CommunicationPath.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`CommunicationPath`](../deployments/mdnodes/CommunicationPath.html)
Generated:
createPrimitiveTypeAdapter
public org.eclipse.emf.common.notify.Adapter createPrimitiveTypeAdapter()
Creates a new adapter for an object of class '[`*Primitive Type*`](../classes/mdkernel/PrimitiveType.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`PrimitiveType`](../classes/mdkernel/PrimitiveType.html)
Generated:
createFinalStateAdapter
public org.eclipse.emf.common.notify.Adapter createFinalStateAdapter()
Creates a new adapter for an object of class '[`*Final State*`](../statemachines/mdbehaviorstatemachines/FinalState.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`FinalState`](../statemachines/mdbehaviorstatemachines/FinalState.html)
Generated:
createAnyReceiveEventAdapter
public org.eclipse.emf.common.notify.Adapter createAnyReceiveEventAdapter()
Creates a new adapter for an object of class '[`*Any Receive Event*`](../commonbehaviors/mdcommunications/AnyReceiveEvent.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`AnyReceiveEvent`](../commonbehaviors/mdcommunications/AnyReceiveEvent.html)
Generated:
createMergeNodeAdapter
public org.eclipse.emf.common.notify.Adapter createMergeNodeAdapter()
Creates a new adapter for an object of class '[`*Merge Node*`](../activities/mdintermediateactivities/MergeNode.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`MergeNode`](../activities/mdintermediateactivities/MergeNode.html)
Generated:
createContinuationAdapter
public org.eclipse.emf.common.notify.Adapter createContinuationAdapter()
Creates a new adapter for an object of class '[`*Continuation*`](../interactions/mdfragments/Continuation.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Continuation`](../interactions/mdfragments/Continuation.html)
Generated:
createLiteralNullAdapter
public org.eclipse.emf.common.notify.Adapter createLiteralNullAdapter()
Creates a new adapter for an object of class '[`*Literal Null*`](../classes/mdkernel/LiteralNull.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`LiteralNull`](../classes/mdkernel/LiteralNull.html)
Generated:
createMessageOccurrenceSpecificationAdapter
public org.eclipse.emf.common.notify.Adapter createMessageOccurrenceSpecificationAdapter()
Creates a new adapter for an object of class
 '[`*Message Occurrence Specification*`](../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`MessageOccurrenceSpecification`](../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html)
Generated:
createLiteralBooleanAdapter
public org.eclipse.emf.common.notify.Adapter createLiteralBooleanAdapter()
Creates a new adapter for an object of class '[`*Literal Boolean*`](../classes/mdkernel/LiteralBoolean.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`LiteralBoolean`](../classes/mdkernel/LiteralBoolean.html)
Generated:
createDestructionOccurrenceSpecificationAdapter
public org.eclipse.emf.common.notify.Adapter createDestructionOccurrenceSpecificationAdapter()
Creates a new adapter for an object of class '[`*Destruction Occurrence Specification*`](../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DestructionOccurrenceSpecification`](../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html)
Generated:
createModelAdapter
public org.eclipse.emf.common.notify.Adapter createModelAdapter()
Creates a new adapter for an object of class '[`*Model*`](../auxiliaryconstructs/mdmodels/Model.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`Model`](../auxiliaryconstructs/mdmodels/Model.html)
Generated:
createClearVariableActionAdapter
public org.eclipse.emf.common.notify.Adapter createClearVariableActionAdapter()
Creates a new adapter for an object of class
 '[`*Clear Variable Action*`](../actions/mdstructuredactions/ClearVariableAction.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ClearVariableAction`](../actions/mdstructuredactions/ClearVariableAction.html)
Generated:
createModelObjectAdapter
public org.eclipse.emf.common.notify.Adapter createModelObjectAdapter()
Creates a new adapter for an object of class '[`*Model Object*`](../base/ModelObject.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`ModelObject`](../base/ModelObject.html)
Generated:
createMDObjectAdapter
public org.eclipse.emf.common.notify.Adapter createMDObjectAdapter()
Creates a new adapter for an object of class '[`*MD Object*`](../../../../magicdraw/foundation/MDObject.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`MDObject`](../../../../magicdraw/foundation/MDObject.html)
Generated:
createEObjectAdapter
public org.eclipse.emf.common.notify.Adapter createEObjectAdapter()
Creates a new adapter for the default case.
 begin-user-doc 
 This default implementation returns null.
 end-user-doc
Returns:
the new adapter.
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.util</a></div>
<h1 class="title" title="Class UMLAdapterFactory">Class UMLAdapterFactory</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.notify.impl.AdapterFactoryImpl
<div class="inheritance">com.nomagic.uml2.ext.magicdraw.util.UMLAdapterFactory</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>org.eclipse.emf.common.notify.AdapterFactory</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">UMLAdapterFactory</span>
<span class="extends-implements">extends org.eclipse.emf.common.notify.impl.AdapterFactoryImpl</span></div>
<div class="block"><!-- begin-user-doc -->
 The <b>Adapter Factory</b> for the model.
 It provides an adapter <code>createXXX</code> method for each class of the model.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../metadata/UMLPackage.html" title="interface in com.nomagic.uml2.ext.magicdraw.metadata"><code>UMLPackage</code></a></li>
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
<div class="col-first even-row-color"><code>protected static <a href="../metadata/UMLPackage.html" title="interface in com.nomagic.uml2.ext.magicdraw.metadata">UMLPackage</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#modelPackage">modelPackage</a></code></div>
<div class="col-last even-row-color">
<div class="block">The cached model package.</div>
</div>
<div class="col-first odd-row-color"><code>protected <a href="UMLSwitch.html" title="class in com.nomagic.uml2.ext.magicdraw.util">UMLSwitch</a>&lt;org.eclipse.emf.common.notify.Adapter&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#modelSwitch">modelSwitch</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The switch that delegates to the <code>createXXX</code> methods.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">UMLAdapterFactory</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an instance of the adapter factory.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAbstractionAdapter()">createAbstractionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code><em>Abstraction</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAcceptCallActionAdapter()">createAcceptCallActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Accept Call Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAcceptEventActionAdapter()">createAcceptEventActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Accept Event Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActionAdapter()">createActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActionExecutionSpecificationAdapter()">createActionExecutionSpecificationAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Action Execution Specification</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActionInputPinAdapter()">createActionInputPinAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Action Input Pin</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityAdapter()">createActivityAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code><em>Activity</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityEdgeAdapter()">createActivityEdgeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Activity Edge</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityFinalNodeAdapter()">createActivityFinalNodeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Activity Final Node</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityGroupAdapter()">createActivityGroupAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code><em>Activity Group</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityNodeAdapter()">createActivityNodeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code><em>Activity Node</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityParameterNodeAdapter()">createActivityParameterNodeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Activity Parameter Node</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityPartitionAdapter()">createActivityPartitionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Activity Partition</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActorAdapter()">createActorAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code><em>Actor</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAdapter(org.eclipse.emf.common.notify.Notifier)">createAdapter</a><wbr/>(org.eclipse.emf.common.notify.Notifier target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates an adapter for the <code>target</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAddStructuralFeatureValueActionAdapter()">createAddStructuralFeatureValueActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Add Structural Feature Value Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAddVariableValueActionAdapter()">createAddVariableValueActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Add Variable Value Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAnyReceiveEventAdapter()">createAnyReceiveEventAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Any Receive Event</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createArtifactAdapter()">createArtifactAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code><em>Artifact</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAssociationAdapter()">createAssociationAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Association</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAssociationClassAdapter()">createAssociationClassAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses"><code><em>Association Class</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createBehaviorAdapter()">createBehaviorAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code><em>Behavior</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createBehavioralFeatureAdapter()">createBehavioralFeatureAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Behavioral Feature</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createBehavioredClassifierAdapter()">createBehavioredClassifierAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code><em>Behaviored Classifier</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createBehaviorExecutionSpecificationAdapter()">createBehaviorExecutionSpecificationAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Behavior Execution Specification</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createBroadcastSignalActionAdapter()">createBroadcastSignalActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Broadcast Signal Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCallActionAdapter()">createCallActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Call Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCallBehaviorActionAdapter()">createCallBehaviorActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Call Behavior Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCallEventAdapter()">createCallEventAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Call Event</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCallOperationActionAdapter()">createCallOperationActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Call Operation Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCentralBufferNodeAdapter()">createCentralBufferNodeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Central Buffer Node</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createChangeEventAdapter()">createChangeEventAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Change Event</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClassAdapter()">createClassAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Class</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClassifierAdapter()">createClassifierAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Classifier</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClassifierTemplateParameterAdapter()">createClassifierTemplateParameterAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Classifier Template Parameter</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClauseAdapter()">createClauseAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Clause</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClearAssociationActionAdapter()">createClearAssociationActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Clear Association Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClearStructuralFeatureActionAdapter()">createClearStructuralFeatureActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Clear Structural Feature Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClearVariableActionAdapter()">createClearVariableActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Clear Variable Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCollaborationAdapter()">createCollaborationAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code><em>Collaboration</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCollaborationUseAdapter()">createCollaborationUseAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code><em>Collaboration Use</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCombinedFragmentAdapter()">createCombinedFragmentAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Combined Fragment</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCommentAdapter()">createCommentAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Comment</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCommunicationPathAdapter()">createCommunicationPathAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Communication Path</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createComponentAdapter()">createComponentAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code><em>Component</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createComponentRealizationAdapter()">createComponentRealizationAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code><em>Component Realization</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConditionalNodeAdapter()">createConditionalNodeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Conditional Node</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConnectableElementAdapter()">createConnectableElementAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code><em>Connectable Element</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConnectableElementTemplateParameterAdapter()">createConnectableElementTemplateParameterAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Connectable Element Template Parameter</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConnectionPointReferenceAdapter()">createConnectionPointReferenceAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>Connection Point Reference</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConnectorAdapter()">createConnectorAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code><em>Connector</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConnectorEndAdapter()">createConnectorEndAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code><em>Connector End</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConsiderIgnoreFragmentAdapter()">createConsiderIgnoreFragmentAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Consider Ignore Fragment</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createConstraintAdapter()">createConstraintAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Constraint</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createContinuationAdapter()">createContinuationAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Continuation</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createControlFlowAdapter()">createControlFlowAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Control Flow</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createControlNodeAdapter()">createControlNodeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Control Node</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCreateLinkActionAdapter()">createCreateLinkActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Create Link Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCreateLinkObjectActionAdapter()">createCreateLinkObjectActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Create Link Object Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCreateObjectActionAdapter()">createCreateObjectActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Create Object Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDataStoreNodeAdapter()">createDataStoreNodeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code><em>Data Store Node</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDataTypeAdapter()">createDataTypeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Data Type</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDecisionNodeAdapter()">createDecisionNodeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Decision Node</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDependencyAdapter()">createDependencyAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code><em>Dependency</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDeployedArtifactAdapter()">createDeployedArtifactAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Deployed Artifact</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDeploymentAdapter()">createDeploymentAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Deployment</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDeploymentSpecificationAdapter()">createDeploymentSpecificationAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments"><code><em>Deployment Specification</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDeploymentTargetAdapter()">createDeploymentTargetAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Deployment Target</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDestroyLinkActionAdapter()">createDestroyLinkActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Destroy Link Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDestroyObjectActionAdapter()">createDestroyObjectActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Destroy Object Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDestructionOccurrenceSpecificationAdapter()">createDestructionOccurrenceSpecificationAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Destruction Occurrence Specification</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDeviceAdapter()">createDeviceAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Device</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDiagramAdapter()">createDiagramAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Diagram</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDirectedRelationshipAdapter()">createDirectedRelationshipAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Directed Relationship</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDurationAdapter()">createDurationAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Duration</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDurationConstraintAdapter()">createDurationConstraintAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Duration Constraint</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDurationIntervalAdapter()">createDurationIntervalAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Duration Interval</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDurationObservationAdapter()">createDurationObservationAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Duration Observation</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createElementAdapter()">createElementAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Element</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createElementImportAdapter()">createElementImportAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Element Import</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createElementValueAdapter()">createElementValueAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Element Value</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createEncapsulatedClassifierAdapter()">createEncapsulatedClassifierAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code><em>Encapsulated Classifier</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createEnumerationAdapter()">createEnumerationAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Enumeration</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createEnumerationLiteralAdapter()">createEnumerationLiteralAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Enumeration Literal</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createEObjectAdapter()">createEObjectAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for the default case.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createEventAdapter()">createEventAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Event</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExceptionHandlerAdapter()">createExceptionHandlerAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code><em>Exception Handler</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExecutableNodeAdapter()">createExecutableNodeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Executable Node</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExecutionEnvironmentAdapter()">createExecutionEnvironmentAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Execution Environment</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExecutionOccurrenceSpecificationAdapter()">createExecutionOccurrenceSpecificationAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Execution Occurrence Specification</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExecutionSpecificationAdapter()">createExecutionSpecificationAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Execution Specification</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExpansionNodeAdapter()">createExpansionNodeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code><em>Expansion Node</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExpansionRegionAdapter()">createExpansionRegionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code><em>Expansion Region</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExpressionAdapter()">createExpressionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Expression</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExtendAdapter()">createExtendAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code><em>Extend</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExtensionAdapter()">createExtensionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code><em>Extension</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExtensionEndAdapter()">createExtensionEndAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code><em>Extension End</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExtensionPointAdapter()">createExtensionPointAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code><em>Extension Point</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createFeatureAdapter()">createFeatureAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Feature</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createFinalNodeAdapter()">createFinalNodeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Final Node</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createFinalStateAdapter()">createFinalStateAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>Final State</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createFlowFinalNodeAdapter()">createFlowFinalNodeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Flow Final Node</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createForkNodeAdapter()">createForkNodeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Fork Node</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createFunctionBehaviorAdapter()">createFunctionBehaviorAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code><em>Function Behavior</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createGateAdapter()">createGateAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Gate</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createGeneralizationAdapter()">createGeneralizationAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Generalization</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createGeneralizationSetAdapter()">createGeneralizationSetAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes"><code><em>Generalization Set</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createGeneralOrderingAdapter()">createGeneralOrderingAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>General Ordering</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createImageAdapter()">createImageAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code><em>Image</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createIncludeAdapter()">createIncludeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code><em>Include</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInformationFlowAdapter()">createInformationFlowAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code><em>Information Flow</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInformationItemAdapter()">createInformationItemAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code><em>Information Item</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInitialNodeAdapter()">createInitialNodeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Initial Node</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInputPinAdapter()">createInputPinAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Input Pin</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInstanceSpecificationAdapter()">createInstanceSpecificationAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Instance Specification</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInstanceValueAdapter()">createInstanceValueAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Instance Value</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInteractionAdapter()">createInteractionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Interaction</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInteractionConstraintAdapter()">createInteractionConstraintAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Interaction Constraint</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInteractionFragmentAdapter()">createInteractionFragmentAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Interaction Fragment</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInteractionOperandAdapter()">createInteractionOperandAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Interaction Operand</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInteractionUseAdapter()">createInteractionUseAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Interaction Use</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInterfaceAdapter()">createInterfaceAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code><em>Interface</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInterfaceRealizationAdapter()">createInterfaceRealizationAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code><em>Interface Realization</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInterruptibleActivityRegionAdapter()">createInterruptibleActivityRegionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code><em>Interruptible Activity Region</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createIntervalAdapter()">createIntervalAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Interval</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createIntervalConstraintAdapter()">createIntervalConstraintAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Interval Constraint</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInvocationActionAdapter()">createInvocationActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Invocation Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createJoinNodeAdapter()">createJoinNodeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Join Node</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLifelineAdapter()">createLifelineAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Lifeline</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLinkActionAdapter()">createLinkActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Link Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLinkEndCreationDataAdapter()">createLinkEndCreationDataAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Link End Creation Data</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLinkEndDataAdapter()">createLinkEndDataAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Link End Data</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLinkEndDestructionDataAdapter()">createLinkEndDestructionDataAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Link End Destruction Data</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLiteralBooleanAdapter()">createLiteralBooleanAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal Boolean</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLiteralIntegerAdapter()">createLiteralIntegerAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal Integer</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLiteralNullAdapter()">createLiteralNullAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal Null</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLiteralRealAdapter()">createLiteralRealAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal Real</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLiteralSpecificationAdapter()">createLiteralSpecificationAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal Specification</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLiteralStringAdapter()">createLiteralStringAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal String</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLiteralUnlimitedNaturalAdapter()">createLiteralUnlimitedNaturalAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal Unlimited Natural</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLoopNodeAdapter()">createLoopNodeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Loop Node</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createManifestationAdapter()">createManifestationAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code><em>Manifestation</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMDObjectAdapter()">createMDObjectAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation"><code><em>MD Object</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMergeNodeAdapter()">createMergeNodeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Merge Node</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMessageAdapter()">createMessageAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Message</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMessageEndAdapter()">createMessageEndAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Message End</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMessageEventAdapter()">createMessageEventAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Message Event</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMessageOccurrenceSpecificationAdapter()">createMessageOccurrenceSpecificationAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Message Occurrence Specification</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createModelAdapter()">createModelAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels"><code><em>Model</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createModelObjectAdapter()">createModelObjectAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base"><code><em>Model Object</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMultiplicityElementAdapter()">createMultiplicityElementAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Multiplicity Element</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createNamedElementAdapter()">createNamedElementAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Named Element</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createNamespaceAdapter()">createNamespaceAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Namespace</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createNodeAdapter()">createNodeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Node</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createObjectFlowAdapter()">createObjectFlowAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Object Flow</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createObjectNodeAdapter()">createObjectNodeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Object Node</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createObservationAdapter()">createObservationAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Observation</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOccurrenceSpecificationAdapter()">createOccurrenceSpecificationAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Occurrence Specification</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOpaqueActionAdapter()">createOpaqueActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Opaque Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOpaqueBehaviorAdapter()">createOpaqueBehaviorAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code><em>Opaque Behavior</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOpaqueExpressionAdapter()">createOpaqueExpressionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Opaque Expression</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOperationAdapter()">createOperationAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Operation</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOperationTemplateParameterAdapter()">createOperationTemplateParameterAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Operation Template Parameter</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOutputPinAdapter()">createOutputPinAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Output Pin</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPackageableElementAdapter()">createPackageableElementAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Packageable Element</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPackageAdapter()">createPackageAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Package</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPackageImportAdapter()">createPackageImportAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Package Import</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPackageMergeAdapter()">createPackageMergeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Package Merge</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createParameterableElementAdapter()">createParameterableElementAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Parameterable Element</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createParameterAdapter()">createParameterAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Parameter</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createParameterSetAdapter()">createParameterSetAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code><em>Parameter Set</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPartDecompositionAdapter()">createPartDecompositionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Part Decomposition</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPinAdapter()">createPinAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Pin</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPortAdapter()">createPortAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code><em>Port</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPrimitiveTypeAdapter()">createPrimitiveTypeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Primitive Type</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProfileAdapter()">createProfileAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code><em>Profile</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProfileApplicationAdapter()">createProfileApplicationAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code><em>Profile Application</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPropertyAdapter()">createPropertyAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Property</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProtocolConformanceAdapter()">createProtocolConformanceAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code><em>Protocol Conformance</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProtocolStateMachineAdapter()">createProtocolStateMachineAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code><em>Protocol State Machine</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProtocolTransitionAdapter()">createProtocolTransitionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code><em>Protocol Transition</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPseudostateAdapter()">createPseudostateAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>Pseudostate</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createQualifierValueAdapter()">createQualifierValueAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Qualifier Value</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRaiseExceptionActionAdapter()">createRaiseExceptionActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Raise Exception Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadExtentActionAdapter()">createReadExtentActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Read Extent Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadIsClassifiedObjectActionAdapter()">createReadIsClassifiedObjectActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Read Is Classified Object Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadLinkActionAdapter()">createReadLinkActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Read Link Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadLinkObjectEndActionAdapter()">createReadLinkObjectEndActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Read Link Object End Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadLinkObjectEndQualifierActionAdapter()">createReadLinkObjectEndQualifierActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Read Link Object End Qualifier Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadSelfActionAdapter()">createReadSelfActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Read Self Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadStructuralFeatureActionAdapter()">createReadStructuralFeatureActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Read Structural Feature Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReadVariableActionAdapter()">createReadVariableActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Read Variable Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRealizationAdapter()">createRealizationAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code><em>Realization</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReceptionAdapter()">createReceptionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Reception</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReclassifyObjectActionAdapter()">createReclassifyObjectActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Reclassify Object Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRedefinableElementAdapter()">createRedefinableElementAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Redefinable Element</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRedefinableTemplateSignatureAdapter()">createRedefinableTemplateSignatureAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Redefinable Template Signature</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReduceActionAdapter()">createReduceActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Reduce Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRegionAdapter()">createRegionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>Region</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRelationshipAdapter()">createRelationshipAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Relationship</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRemoveStructuralFeatureValueActionAdapter()">createRemoveStructuralFeatureValueActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Remove
 Structural Feature Value Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRemoveVariableValueActionAdapter()">createRemoveVariableValueActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Remove Variable Value Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createReplyActionAdapter()">createReplyActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Reply Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSendObjectActionAdapter()">createSendObjectActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Send Object Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSendSignalActionAdapter()">createSendSignalActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Send Signal Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSequenceNodeAdapter()">createSequenceNodeAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Sequence Node</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSignalAdapter()">createSignalAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Signal</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSignalEventAdapter()">createSignalEventAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Signal Event</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSlotAdapter()">createSlotAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Slot</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStartClassifierBehaviorActionAdapter()">createStartClassifierBehaviorActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Start Classifier Behavior Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStartObjectBehaviorActionAdapter()">createStartObjectBehaviorActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Start Object Behavior Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStateAdapter()">createStateAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>State</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStateInvariantAdapter()">createStateInvariantAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>State Invariant</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStateMachineAdapter()">createStateMachineAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>State Machine</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStereotypeAdapter()">createStereotypeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code><em>Stereotype</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStringExpressionAdapter()">createStringExpressionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>String Expression</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStructuralFeatureActionAdapter()">createStructuralFeatureActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Structural Feature Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStructuralFeatureAdapter()">createStructuralFeatureAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Structural Feature</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStructuredActivityNodeAdapter()">createStructuredActivityNodeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Structured Activity Node</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStructuredClassifierAdapter()">createStructuredClassifierAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code><em>Structured Classifier</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSubstitutionAdapter()">createSubstitutionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code><em>Substitution</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateableElementAdapter()">createTemplateableElementAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Templateable Element</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateBindingAdapter()">createTemplateBindingAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Template Binding</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateParameterAdapter()">createTemplateParameterAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Template Parameter</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateParameterSubstitutionAdapter()">createTemplateParameterSubstitutionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Template Parameter Substitution</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateSignatureAdapter()">createTemplateSignatureAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Template Signature</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTestIdentityActionAdapter()">createTestIdentityActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Test Identity Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTimeConstraintAdapter()">createTimeConstraintAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Time Constraint</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTimeEventAdapter()">createTimeEventAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Time Event</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTimeExpressionAdapter()">createTimeExpressionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Time Expression</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTimeIntervalAdapter()">createTimeIntervalAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Time Interval</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTimeObservationAdapter()">createTimeObservationAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Time Observation</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTransitionAdapter()">createTransitionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>Transition</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTriggerAdapter()">createTriggerAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Trigger</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTypeAdapter()">createTypeAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Type</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTypedElementAdapter()">createTypedElementAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Typed Element</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createUnmarshallActionAdapter()">createUnmarshallActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Unmarshall Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createUsageAdapter()">createUsageAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code><em>Usage</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createUseCaseAdapter()">createUseCaseAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code><em>Use Case</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createValuePinAdapter()">createValuePinAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Value Pin</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueSpecificationActionAdapter()">createValueSpecificationActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Value Specification Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueSpecificationAdapter()">createValueSpecificationAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Value Specification</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createVariableActionAdapter()">createVariableActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Variable Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createVariableAdapter()">createVariableAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Variable</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createVertexAdapter()">createVertexAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>Vertex</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createWriteLinkActionAdapter()">createWriteLinkActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Write Link Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createWriteStructuralFeatureActionAdapter()">createWriteStructuralFeatureActionAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Write Structural Feature Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createWriteVariableActionAdapter()">createWriteVariableActionAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Write Variable Action</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFactoryForType(java.lang.Object)">isFactoryForType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether this factory is applicable for the type of the object.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.impl.AdapterFactoryImpl">Methods inherited from class org.eclipse.emf.common.notify.impl.AdapterFactoryImpl</h3>
<code>adapt, adapt, adaptAllNew, adaptNew, associate, createAdapter, resolve</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="modelPackage">
<h3>modelPackage</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type"><a href="../metadata/UMLPackage.html" title="interface in com.nomagic.uml2.ext.magicdraw.metadata">UMLPackage</a></span> <span class="element-name">modelPackage</span></div>
<div class="block">The cached model package.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="modelSwitch">
<h3>modelSwitch</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="UMLSwitch.html" title="class in com.nomagic.uml2.ext.magicdraw.util">UMLSwitch</a>&lt;org.eclipse.emf.common.notify.Adapter&gt;</span> <span class="element-name">modelSwitch</span></div>
<div class="block">The switch that delegates to the <code>createXXX</code> methods.
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>UMLAdapterFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">UMLAdapterFactory</span>()</div>
<div class="block">Creates an instance of the adapter factory.
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
<section class="detail" id="isFactoryForType(java.lang.Object)">
<h3>isFactoryForType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFactoryForType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<div class="block">Returns whether this factory is applicable for the type of the object.
 <!-- begin-user-doc -->
 This implementation returns <code>true</code> if the object is either the model's package or is an instance object of the model.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isFactoryForType</code> in interface <code>org.eclipse.emf.common.notify.AdapterFactory</code></dd>
<dt>Overrides:</dt>
<dd><code>isFactoryForType</code> in class <code>org.eclipse.emf.common.notify.impl.AdapterFactoryImpl</code></dd>
<dt>Returns:</dt>
<dd>whether this factory is applicable for the type of the object.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAdapter(org.eclipse.emf.common.notify.Notifier)">
<h3>createAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createAdapter</span><wbr/><span class="parameters">(org.eclipse.emf.common.notify.Notifier target)</span></div>
<div class="block">Creates an adapter for the <code>target</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>createAdapter</code> in class <code>org.eclipse.emf.common.notify.impl.AdapterFactoryImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>target</code> - the object to adapt.</dd>
<dt>Returns:</dt>
<dd>the adapter for the <code>target</code>.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSendSignalActionAdapter()">
<h3>createSendSignalActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createSendSignalActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Send Signal Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>SendSignalAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInvocationActionAdapter()">
<h3>createInvocationActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInvocationActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Invocation Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>InvocationAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActionAdapter()">
<h3>createActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>Action</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExecutableNodeAdapter()">
<h3>createExecutableNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createExecutableNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Executable Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>ExecutableNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityNodeAdapter()">
<h3>createActivityNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createActivityNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code><em>Activity Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRedefinableElementAdapter()">
<h3>createRedefinableElementAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createRedefinableElementAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Redefinable Element</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>RedefinableElement</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNamedElementAdapter()">
<h3>createNamedElementAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createNamedElementAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Named Element</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>NamedElement</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createElementAdapter()">
<h3>createElementAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createElementAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Element</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCommentAdapter()">
<h3>createCommentAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createCommentAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Comment</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Comment</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInstanceSpecificationAdapter()">
<h3>createInstanceSpecificationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInstanceSpecificationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Instance Specification</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceSpecification</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackageableElementAdapter()">
<h3>createPackageableElementAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createPackageableElementAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Packageable Element</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageableElement</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameterableElementAdapter()">
<h3>createParameterableElementAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createParameterableElementAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Parameterable Element</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ParameterableElement</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateParameterAdapter()">
<h3>createTemplateParameterAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTemplateParameterAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Template Parameter</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameter</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateSignatureAdapter()">
<h3>createTemplateSignatureAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTemplateSignatureAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Template Signature</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateSignature</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateableElementAdapter()">
<h3>createTemplateableElementAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTemplateableElementAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Templateable Element</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateableElement</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateBindingAdapter()">
<h3>createTemplateBindingAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTemplateBindingAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Template Binding</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateBinding</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDirectedRelationshipAdapter()">
<h3>createDirectedRelationshipAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDirectedRelationshipAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Directed Relationship</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>DirectedRelationship</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRelationshipAdapter()">
<h3>createRelationshipAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createRelationshipAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Relationship</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Relationship</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInformationFlowAdapter()">
<h3>createInformationFlowAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInformationFlowAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code><em>Information Flow</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationFlow</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClassifierAdapter()">
<h3>createClassifierAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createClassifierAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Classifier</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNamespaceAdapter()">
<h3>createNamespaceAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createNamespaceAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Namespace</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Namespace</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createElementImportAdapter()">
<h3>createElementImportAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createElementImportAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Element Import</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementImport</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProfileAdapter()">
<h3>createProfileAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createProfileAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code><em>Profile</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Profile</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackageAdapter()">
<h3>createPackageAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createPackageAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Package</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Package</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotypeAdapter()">
<h3>createStereotypeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createStereotypeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code><em>Stereotype</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Stereotype</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClassAdapter()">
<h3>createClassAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createClassAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Class</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Class</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBehavioredClassifierAdapter()">
<h3>createBehavioredClassifierAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createBehavioredClassifierAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code><em>Behaviored Classifier</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>BehavioredClassifier</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBehaviorAdapter()">
<h3>createBehaviorAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createBehaviorAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code><em>Behavior</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>Behavior</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameterAdapter()">
<h3>createParameterAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createParameterAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Parameter</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Parameter</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityElementAdapter()">
<h3>createMultiplicityElementAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createMultiplicityElementAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Multiplicity Element</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>MultiplicityElement</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueSpecificationAdapter()">
<h3>createValueSpecificationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createValueSpecificationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Value Specification</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ValueSpecification</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTypedElementAdapter()">
<h3>createTypedElementAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTypedElementAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Typed Element</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>TypedElement</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTypeAdapter()">
<h3>createTypeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTypeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Type</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Type</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAssociationAdapter()">
<h3>createAssociationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createAssociationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Association</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Association</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPropertyAdapter()">
<h3>createPropertyAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createPropertyAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Property</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStructuralFeatureAdapter()">
<h3>createStructuralFeatureAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createStructuralFeatureAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Structural Feature</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>StructuralFeature</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFeatureAdapter()">
<h3>createFeatureAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createFeatureAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Feature</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Feature</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlotAdapter()">
<h3>createSlotAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createSlotAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Slot</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Slot</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStructuralFeatureActionAdapter()">
<h3>createStructuralFeatureActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createStructuralFeatureActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Structural Feature Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>StructuralFeatureAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInputPinAdapter()">
<h3>createInputPinAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInputPinAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Input Pin</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>InputPin</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPinAdapter()">
<h3>createPinAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createPinAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Pin</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>Pin</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createObjectNodeAdapter()">
<h3>createObjectNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createObjectNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Object Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateAdapter()">
<h3>createStateAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createStateAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>State</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>State</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createVertexAdapter()">
<h3>createVertexAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createVertexAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>Vertex</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Vertex</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRegionAdapter()">
<h3>createRegionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createRegionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>Region</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Region</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateMachineAdapter()">
<h3>createStateMachineAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createStateMachineAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>State Machine</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>StateMachine</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPseudostateAdapter()">
<h3>createPseudostateAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createPseudostateAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>Pseudostate</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Pseudostate</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectionPointReferenceAdapter()">
<h3>createConnectionPointReferenceAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createConnectionPointReferenceAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>Connection Point Reference</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>ConnectionPointReference</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTransitionAdapter()">
<h3>createTransitionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTransitionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>Transition</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Transition</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConstraintAdapter()">
<h3>createConstraintAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createConstraintAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Constraint</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperationAdapter()">
<h3>createOperationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createOperationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Operation</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Operation</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBehavioralFeatureAdapter()">
<h3>createBehavioralFeatureAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createBehavioralFeatureAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Behavioral Feature</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>BehavioralFeature</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameterSetAdapter()">
<h3>createParameterSetAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createParameterSetAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code><em>Parameter Set</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>ParameterSet</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDataTypeAdapter()">
<h3>createDataTypeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDataTypeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Data Type</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>DataType</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInterfaceAdapter()">
<h3>createInterfaceAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInterfaceAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code><em>Interface</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>Interface</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReceptionAdapter()">
<h3>createReceptionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createReceptionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Reception</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Reception</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSignalAdapter()">
<h3>createSignalAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createSignalAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Signal</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Signal</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBroadcastSignalActionAdapter()">
<h3>createBroadcastSignalActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createBroadcastSignalActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Broadcast Signal Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>BroadcastSignalAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSignalEventAdapter()">
<h3>createSignalEventAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createSignalEventAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Signal Event</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>SignalEvent</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMessageEventAdapter()">
<h3>createMessageEventAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createMessageEventAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Message Event</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>MessageEvent</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEventAdapter()">
<h3>createEventAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createEventAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Event</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Event</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTriggerAdapter()">
<h3>createTriggerAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTriggerAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Trigger</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Trigger</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPortAdapter()">
<h3>createPortAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createPortAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code><em>Port</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code>Port</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProtocolStateMachineAdapter()">
<h3>createProtocolStateMachineAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createProtocolStateMachineAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code><em>Protocol State Machine</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolStateMachine</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProtocolConformanceAdapter()">
<h3>createProtocolConformanceAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createProtocolConformanceAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code><em>Protocol Conformance</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolConformance</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEncapsulatedClassifierAdapter()">
<h3>createEncapsulatedClassifierAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createEncapsulatedClassifierAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code><em>Encapsulated Classifier</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code>EncapsulatedClassifier</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStructuredClassifierAdapter()">
<h3>createStructuredClassifierAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createStructuredClassifierAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code><em>Structured Classifier</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>StructuredClassifier</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectorAdapter()">
<h3>createConnectorAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createConnectorAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code><em>Connector</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>Connector</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectorEndAdapter()">
<h3>createConnectorEndAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createConnectorEndAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code><em>Connector End</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>ConnectorEnd</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectableElementAdapter()">
<h3>createConnectableElementAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createConnectableElementAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code><em>Connectable Element</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>ConnectableElement</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnectableElementTemplateParameterAdapter()">
<h3>createConnectableElementTemplateParameterAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createConnectableElementTemplateParameterAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Connectable Element Template Parameter</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ConnectableElementTemplateParameter</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCollaborationAdapter()">
<h3>createCollaborationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createCollaborationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code><em>Collaboration</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code>Collaboration</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCollaborationUseAdapter()">
<h3>createCollaborationUseAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createCollaborationUseAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code><em>Collaboration Use</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code>CollaborationUse</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDependencyAdapter()">
<h3>createDependencyAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDependencyAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code><em>Dependency</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Dependency</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLifelineAdapter()">
<h3>createLifelineAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createLifelineAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Lifeline</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Lifeline</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionFragmentAdapter()">
<h3>createInteractionFragmentAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInteractionFragmentAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Interaction Fragment</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>InteractionFragment</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionAdapter()">
<h3>createInteractionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInteractionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Interaction</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Interaction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGateAdapter()">
<h3>createGateAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createGateAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Gate</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>Gate</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMessageEndAdapter()">
<h3>createMessageEndAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createMessageEndAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Message End</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageEnd</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMessageAdapter()">
<h3>createMessageAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createMessageAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Message</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Message</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionUseAdapter()">
<h3>createInteractionUseAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInteractionUseAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Interaction Use</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionUse</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCombinedFragmentAdapter()">
<h3>createCombinedFragmentAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createCombinedFragmentAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Combined Fragment</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>CombinedFragment</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionOperandAdapter()">
<h3>createInteractionOperandAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInteractionOperandAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Interaction Operand</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionOperand</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionConstraintAdapter()">
<h3>createInteractionConstraintAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInteractionConstraintAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Interaction Constraint</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionConstraint</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGeneralOrderingAdapter()">
<h3>createGeneralOrderingAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createGeneralOrderingAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>General Ordering</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>GeneralOrdering</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOccurrenceSpecificationAdapter()">
<h3>createOccurrenceSpecificationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createOccurrenceSpecificationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Occurrence Specification</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>OccurrenceSpecification</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExecutionSpecificationAdapter()">
<h3>createExecutionSpecificationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createExecutionSpecificationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Execution Specification</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ExecutionSpecification</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExecutionOccurrenceSpecificationAdapter()">
<h3>createExecutionOccurrenceSpecificationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createExecutionOccurrenceSpecificationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Execution Occurrence Specification</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ExecutionOccurrenceSpecification</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPartDecompositionAdapter()">
<h3>createPartDecompositionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createPartDecompositionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Part Decomposition</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>PartDecomposition</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateInvariantAdapter()">
<h3>createStateInvariantAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createStateInvariantAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>State Invariant</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>StateInvariant</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReplyActionAdapter()">
<h3>createReplyActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createReplyActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Reply Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReplyAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAcceptEventActionAdapter()">
<h3>createAcceptEventActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createAcceptEventActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Accept Event Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>AcceptEventAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOutputPinAdapter()">
<h3>createOutputPinAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createOutputPinAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Output Pin</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>OutputPin</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClauseAdapter()">
<h3>createClauseAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createClauseAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Clause</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Clause</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConditionalNodeAdapter()">
<h3>createConditionalNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createConditionalNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Conditional Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>ConditionalNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStructuredActivityNodeAdapter()">
<h3>createStructuredActivityNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createStructuredActivityNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Structured Activity Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>StructuredActivityNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityGroupAdapter()">
<h3>createActivityGroupAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createActivityGroupAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code><em>Activity Group</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityGroup</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityEdgeAdapter()">
<h3>createActivityEdgeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createActivityEdgeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Activity Edge</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityEdge</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityAdapter()">
<h3>createActivityAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createActivityAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code><em>Activity</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>Activity</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityPartitionAdapter()">
<h3>createActivityPartitionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createActivityPartitionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Activity Partition</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ActivityPartition</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createVariableAdapter()">
<h3>createVariableAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createVariableAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Variable</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Variable</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createVariableActionAdapter()">
<h3>createVariableActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createVariableActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Variable Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>VariableAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInterruptibleActivityRegionAdapter()">
<h3>createInterruptibleActivityRegionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInterruptibleActivityRegionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code><em>Interruptible Activity Region</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>InterruptibleActivityRegion</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLoopNodeAdapter()">
<h3>createLoopNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createLoopNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Loop Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>LoopNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOpaqueActionAdapter()">
<h3>createOpaqueActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createOpaqueActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Opaque Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>OpaqueAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCallActionAdapter()">
<h3>createCallActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createCallActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Call Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClearStructuralFeatureActionAdapter()">
<h3>createClearStructuralFeatureActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createClearStructuralFeatureActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Clear Structural Feature Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ClearStructuralFeatureAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCreateLinkObjectActionAdapter()">
<h3>createCreateLinkObjectActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createCreateLinkObjectActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Create Link Object Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>CreateLinkObjectAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCreateLinkActionAdapter()">
<h3>createCreateLinkActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createCreateLinkActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Create Link Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>CreateLinkAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createWriteLinkActionAdapter()">
<h3>createWriteLinkActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createWriteLinkActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Write Link Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>WriteLinkAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLinkActionAdapter()">
<h3>createLinkActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createLinkActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Link Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLinkEndDataAdapter()">
<h3>createLinkEndDataAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createLinkEndDataAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Link End Data</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndData</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createQualifierValueAdapter()">
<h3>createQualifierValueAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createQualifierValueAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Qualifier Value</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>QualifierValue</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLinkEndCreationDataAdapter()">
<h3>createLinkEndCreationDataAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createLinkEndCreationDataAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Link End Creation Data</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndCreationData</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCreateObjectActionAdapter()">
<h3>createCreateObjectActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createCreateObjectActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Create Object Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>CreateObjectAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadExtentActionAdapter()">
<h3>createReadExtentActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createReadExtentActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Read Extent Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadExtentAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadIsClassifiedObjectActionAdapter()">
<h3>createReadIsClassifiedObjectActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createReadIsClassifiedObjectActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Read Is Classified Object Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadIsClassifiedObjectAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadLinkActionAdapter()">
<h3>createReadLinkActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createReadLinkActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Read Link Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadLinkAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadLinkObjectEndActionAdapter()">
<h3>createReadLinkObjectEndActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createReadLinkObjectEndActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Read Link Object End Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadLinkObjectEndAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadLinkObjectEndQualifierActionAdapter()">
<h3>createReadLinkObjectEndQualifierActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createReadLinkObjectEndQualifierActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Read Link Object End Qualifier Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadLinkObjectEndQualifierAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadSelfActionAdapter()">
<h3>createReadSelfActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createReadSelfActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Read Self Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadSelfAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadStructuralFeatureActionAdapter()">
<h3>createReadStructuralFeatureActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createReadStructuralFeatureActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Read Structural Feature Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadStructuralFeatureAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReadVariableActionAdapter()">
<h3>createReadVariableActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createReadVariableActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Read Variable Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ReadVariableAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReduceActionAdapter()">
<h3>createReduceActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createReduceActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Reduce Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReduceAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTestIdentityActionAdapter()">
<h3>createTestIdentityActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTestIdentityActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Test Identity Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>TestIdentityAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUnmarshallActionAdapter()">
<h3>createUnmarshallActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createUnmarshallActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Unmarshall Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>UnmarshallAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueSpecificationActionAdapter()">
<h3>createValueSpecificationActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createValueSpecificationActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Value Specification Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ValueSpecificationAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createWriteStructuralFeatureActionAdapter()">
<h3>createWriteStructuralFeatureActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createWriteStructuralFeatureActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Write Structural Feature Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>WriteStructuralFeatureAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAcceptCallActionAdapter()">
<h3>createAcceptCallActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createAcceptCallActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Accept Call Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>AcceptCallAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInterfaceRealizationAdapter()">
<h3>createInterfaceRealizationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInterfaceRealizationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code><em>Interface Realization</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>InterfaceRealization</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRealizationAdapter()">
<h3>createRealizationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createRealizationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code><em>Realization</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Realization</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAbstractionAdapter()">
<h3>createAbstractionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createAbstractionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code><em>Abstraction</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Abstraction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOpaqueExpressionAdapter()">
<h3>createOpaqueExpressionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createOpaqueExpressionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Opaque Expression</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>OpaqueExpression</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComponentAdapter()">
<h3>createComponentAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createComponentAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code><em>Component</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>Component</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComponentRealizationAdapter()">
<h3>createComponentRealizationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createComponentRealizationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code><em>Component Realization</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>ComponentRealization</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperationTemplateParameterAdapter()">
<h3>createOperationTemplateParameterAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createOperationTemplateParameterAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Operation Template Parameter</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>OperationTemplateParameter</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCallEventAdapter()">
<h3>createCallEventAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createCallEventAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Call Event</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>CallEvent</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCallOperationActionAdapter()">
<h3>createCallOperationActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createCallOperationActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Call Operation Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallOperationAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createArtifactAdapter()">
<h3>createArtifactAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createArtifactAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code><em>Artifact</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code>Artifact</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDeployedArtifactAdapter()">
<h3>createDeployedArtifactAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDeployedArtifactAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Deployed Artifact</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>DeployedArtifact</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDeploymentAdapter()">
<h3>createDeploymentAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDeploymentAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Deployment</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Deployment</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDeploymentSpecificationAdapter()">
<h3>createDeploymentSpecificationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDeploymentSpecificationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments"><code><em>Deployment Specification</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments"><code>DeploymentSpecification</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDeploymentTargetAdapter()">
<h3>createDeploymentTargetAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDeploymentTargetAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Deployment Target</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>DeploymentTarget</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createManifestationAdapter()">
<h3>createManifestationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createManifestationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code><em>Manifestation</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code>Manifestation</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProtocolTransitionAdapter()">
<h3>createProtocolTransitionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createProtocolTransitionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code><em>Protocol Transition</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolTransition</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExtendAdapter()">
<h3>createExtendAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createExtendAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code><em>Extend</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Extend</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUseCaseAdapter()">
<h3>createUseCaseAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createUseCaseAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code><em>Use Case</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>UseCase</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExtensionPointAdapter()">
<h3>createExtensionPointAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createExtensionPointAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code><em>Extension Point</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>ExtensionPoint</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIncludeAdapter()">
<h3>createIncludeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createIncludeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code><em>Include</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Include</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExceptionHandlerAdapter()">
<h3>createExceptionHandlerAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createExceptionHandlerAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code><em>Exception Handler</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExceptionHandler</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLinkEndDestructionDataAdapter()">
<h3>createLinkEndDestructionDataAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createLinkEndDestructionDataAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Link End Destruction Data</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndDestructionData</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDestroyLinkActionAdapter()">
<h3>createDestroyLinkActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDestroyLinkActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Destroy Link Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>DestroyLinkAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRaiseExceptionActionAdapter()">
<h3>createRaiseExceptionActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createRaiseExceptionActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Raise Exception Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>RaiseExceptionAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAddStructuralFeatureValueActionAdapter()">
<h3>createAddStructuralFeatureValueActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createAddStructuralFeatureValueActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Add Structural Feature Value Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>AddStructuralFeatureValueAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAddVariableValueActionAdapter()">
<h3>createAddVariableValueActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createAddVariableValueActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Add Variable Value Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>AddVariableValueAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createWriteVariableActionAdapter()">
<h3>createWriteVariableActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createWriteVariableActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Write Variable Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>WriteVariableAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClearAssociationActionAdapter()">
<h3>createClearAssociationActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createClearAssociationActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Clear Association Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ClearAssociationAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReclassifyObjectActionAdapter()">
<h3>createReclassifyObjectActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createReclassifyObjectActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Reclassify Object Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReclassifyObjectAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStartClassifierBehaviorActionAdapter()">
<h3>createStartClassifierBehaviorActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createStartClassifierBehaviorActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Start Classifier Behavior Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>StartClassifierBehaviorAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStartObjectBehaviorActionAdapter()">
<h3>createStartObjectBehaviorActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createStartObjectBehaviorActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code><em>Start Object Behavior Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>StartObjectBehaviorAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRemoveStructuralFeatureValueActionAdapter()">
<h3>createRemoveStructuralFeatureValueActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createRemoveStructuralFeatureValueActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Remove
 Structural Feature Value Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>RemoveStructuralFeatureValueAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRemoveVariableValueActionAdapter()">
<h3>createRemoveVariableValueActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createRemoveVariableValueActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Remove Variable Value Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>RemoveVariableValueAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSendObjectActionAdapter()">
<h3>createSendObjectActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createSendObjectActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Send Object Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>SendObjectAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDestroyObjectActionAdapter()">
<h3>createDestroyObjectActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDestroyObjectActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code><em>Destroy Object Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>DestroyObjectAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createChangeEventAdapter()">
<h3>createChangeEventAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createChangeEventAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Change Event</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>ChangeEvent</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDurationAdapter()">
<h3>createDurationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDurationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Duration</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Duration</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createObservationAdapter()">
<h3>createObservationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createObservationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Observation</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Observation</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeExpressionAdapter()">
<h3>createTimeExpressionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTimeExpressionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Time Expression</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeExpression</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeIntervalAdapter()">
<h3>createTimeIntervalAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTimeIntervalAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Time Interval</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeInterval</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIntervalAdapter()">
<h3>createIntervalAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createIntervalAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Interval</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Interval</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIntervalConstraintAdapter()">
<h3>createIntervalConstraintAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createIntervalConstraintAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Interval Constraint</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>IntervalConstraint</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeConstraintAdapter()">
<h3>createTimeConstraintAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTimeConstraintAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Time Constraint</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeConstraint</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeEventAdapter()">
<h3>createTimeEventAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTimeEventAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Time Event</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>TimeEvent</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDurationIntervalAdapter()">
<h3>createDurationIntervalAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDurationIntervalAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Duration Interval</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationInterval</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDurationConstraintAdapter()">
<h3>createDurationConstraintAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDurationConstraintAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Duration Constraint</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationConstraint</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createJoinNodeAdapter()">
<h3>createJoinNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createJoinNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Join Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>JoinNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createControlNodeAdapter()">
<h3>createControlNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createControlNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Control Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ControlNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExpressionAdapter()">
<h3>createExpressionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createExpressionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Expression</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Expression</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValuePinAdapter()">
<h3>createValuePinAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createValuePinAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Value Pin</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>ValuePin</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityParameterNodeAdapter()">
<h3>createActivityParameterNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createActivityParameterNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Activity Parameter Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityParameterNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBehaviorExecutionSpecificationAdapter()">
<h3>createBehaviorExecutionSpecificationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createBehaviorExecutionSpecificationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Behavior Execution Specification</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>BehaviorExecutionSpecification</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCallBehaviorActionAdapter()">
<h3>createCallBehaviorActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createCallBehaviorActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code><em>Call Behavior Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallBehaviorAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDecisionNodeAdapter()">
<h3>createDecisionNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDecisionNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Decision Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>DecisionNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createObjectFlowAdapter()">
<h3>createObjectFlowAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createObjectFlowAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Object Flow</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectFlow</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExtensionAdapter()">
<h3>createExtensionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createExtensionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code><em>Extension</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Extension</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExtensionEndAdapter()">
<h3>createExtensionEndAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createExtensionEndAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code><em>Extension End</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>ExtensionEnd</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImageAdapter()">
<h3>createImageAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createImageAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code><em>Image</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Image</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackageMergeAdapter()">
<h3>createPackageMergeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createPackageMergeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Package Merge</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageMerge</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProfileApplicationAdapter()">
<h3>createProfileApplicationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createProfileApplicationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code><em>Profile Application</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>ProfileApplication</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackageImportAdapter()">
<h3>createPackageImportAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createPackageImportAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Package Import</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageImport</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDiagramAdapter()">
<h3>createDiagramAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDiagramAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Diagram</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Diagram</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGeneralizationAdapter()">
<h3>createGeneralizationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createGeneralizationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Generalization</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Generalization</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGeneralizationSetAdapter()">
<h3>createGeneralizationSetAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createGeneralizationSetAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes"><code><em>Generalization Set</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes"><code>GeneralizationSet</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRedefinableTemplateSignatureAdapter()">
<h3>createRedefinableTemplateSignatureAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createRedefinableTemplateSignatureAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Redefinable Template Signature</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>RedefinableTemplateSignature</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSubstitutionAdapter()">
<h3>createSubstitutionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createSubstitutionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code><em>Substitution</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Substitution</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClassifierTemplateParameterAdapter()">
<h3>createClassifierTemplateParameterAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createClassifierTemplateParameterAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Classifier Template Parameter</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ClassifierTemplateParameter</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInformationItemAdapter()">
<h3>createInformationItemAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInformationItemAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code><em>Information Item</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationItem</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateParameterSubstitutionAdapter()">
<h3>createTemplateParameterSubstitutionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTemplateParameterSubstitutionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>Template Parameter Substitution</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameterSubstitution</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInstanceValueAdapter()">
<h3>createInstanceValueAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInstanceValueAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Instance Value</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceValue</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createElementValueAdapter()">
<h3>createElementValueAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createElementValueAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Element Value</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementValue</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStringExpressionAdapter()">
<h3>createStringExpressionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createStringExpressionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code><em>String Expression</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>StringExpression</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDurationObservationAdapter()">
<h3>createDurationObservationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDurationObservationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Duration Observation</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationObservation</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeObservationAdapter()">
<h3>createTimeObservationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createTimeObservationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code><em>Time Observation</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeObservation</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConsiderIgnoreFragmentAdapter()">
<h3>createConsiderIgnoreFragmentAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createConsiderIgnoreFragmentAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Consider Ignore Fragment</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>ConsiderIgnoreFragment</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSequenceNodeAdapter()">
<h3>createSequenceNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createSequenceNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code><em>Sequence Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>SequenceNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActionExecutionSpecificationAdapter()">
<h3>createActionExecutionSpecificationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createActionExecutionSpecificationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Action Execution Specification</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ActionExecutionSpecification</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActionInputPinAdapter()">
<h3>createActionInputPinAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createActionInputPinAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Action Input Pin</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ActionInputPin</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralStringAdapter()">
<h3>createLiteralStringAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createLiteralStringAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal String</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralString</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralSpecificationAdapter()">
<h3>createLiteralSpecificationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createLiteralSpecificationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal Specification</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralSpecification</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDataStoreNodeAdapter()">
<h3>createDataStoreNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDataStoreNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code><em>Data Store Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>DataStoreNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCentralBufferNodeAdapter()">
<h3>createCentralBufferNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createCentralBufferNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Central Buffer Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>CentralBufferNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInitialNodeAdapter()">
<h3>createInitialNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createInitialNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Initial Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>InitialNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDeviceAdapter()">
<h3>createDeviceAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDeviceAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Device</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Device</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNodeAdapter()">
<h3>createNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Node</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAssociationClassAdapter()">
<h3>createAssociationClassAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createAssociationClassAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses"><code><em>Association Class</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses"><code>AssociationClass</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActorAdapter()">
<h3>createActorAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createActorAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code><em>Actor</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Actor</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExecutionEnvironmentAdapter()">
<h3>createExecutionEnvironmentAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createExecutionEnvironmentAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Execution Environment</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>ExecutionEnvironment</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFunctionBehaviorAdapter()">
<h3>createFunctionBehaviorAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createFunctionBehaviorAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code><em>Function Behavior</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>FunctionBehavior</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOpaqueBehaviorAdapter()">
<h3>createOpaqueBehaviorAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createOpaqueBehaviorAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code><em>Opaque Behavior</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>OpaqueBehavior</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFinalNodeAdapter()">
<h3>createFinalNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createFinalNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Final Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>FinalNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityFinalNodeAdapter()">
<h3>createActivityFinalNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createActivityFinalNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Activity Final Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityFinalNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFlowFinalNodeAdapter()">
<h3>createFlowFinalNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createFlowFinalNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Flow Final Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>FlowFinalNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralRealAdapter()">
<h3>createLiteralRealAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createLiteralRealAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal Real</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralReal</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createForkNodeAdapter()">
<h3>createForkNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createForkNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Fork Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ForkNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createControlFlowAdapter()">
<h3>createControlFlowAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createControlFlowAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code><em>Control Flow</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ControlFlow</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUsageAdapter()">
<h3>createUsageAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createUsageAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code><em>Usage</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Usage</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralUnlimitedNaturalAdapter()">
<h3>createLiteralUnlimitedNaturalAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createLiteralUnlimitedNaturalAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal Unlimited Natural</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralUnlimitedNatural</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralIntegerAdapter()">
<h3>createLiteralIntegerAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createLiteralIntegerAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal Integer</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralInteger</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEnumerationAdapter()">
<h3>createEnumerationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createEnumerationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Enumeration</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Enumeration</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEnumerationLiteralAdapter()">
<h3>createEnumerationLiteralAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createEnumerationLiteralAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Enumeration Literal</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>EnumerationLiteral</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExpansionNodeAdapter()">
<h3>createExpansionNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createExpansionNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code><em>Expansion Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExpansionNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExpansionRegionAdapter()">
<h3>createExpansionRegionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createExpansionRegionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code><em>Expansion Region</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExpansionRegion</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCommunicationPathAdapter()">
<h3>createCommunicationPathAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createCommunicationPathAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code><em>Communication Path</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>CommunicationPath</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPrimitiveTypeAdapter()">
<h3>createPrimitiveTypeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createPrimitiveTypeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Primitive Type</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PrimitiveType</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFinalStateAdapter()">
<h3>createFinalStateAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createFinalStateAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code><em>Final State</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>FinalState</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAnyReceiveEventAdapter()">
<h3>createAnyReceiveEventAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createAnyReceiveEventAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code><em>Any Receive Event</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>AnyReceiveEvent</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMergeNodeAdapter()">
<h3>createMergeNodeAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createMergeNodeAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code><em>Merge Node</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>MergeNode</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createContinuationAdapter()">
<h3>createContinuationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createContinuationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code><em>Continuation</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>Continuation</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralNullAdapter()">
<h3>createLiteralNullAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createLiteralNullAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal Null</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralNull</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMessageOccurrenceSpecificationAdapter()">
<h3>createMessageOccurrenceSpecificationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createMessageOccurrenceSpecificationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Message Occurrence Specification</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageOccurrenceSpecification</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralBooleanAdapter()">
<h3>createLiteralBooleanAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createLiteralBooleanAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code><em>Literal Boolean</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralBoolean</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDestructionOccurrenceSpecificationAdapter()">
<h3>createDestructionOccurrenceSpecificationAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDestructionOccurrenceSpecificationAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code><em>Destruction Occurrence Specification</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>DestructionOccurrenceSpecification</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createModelAdapter()">
<h3>createModelAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createModelAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels"><code><em>Model</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels"><code>Model</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClearVariableActionAdapter()">
<h3>createClearVariableActionAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createClearVariableActionAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class
 '<a href="../actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code><em>Clear Variable Action</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ClearVariableAction</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createModelObjectAdapter()">
<h3>createModelObjectAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createModelObjectAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base"><code><em>Model Object</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base"><code>ModelObject</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMDObjectAdapter()">
<h3>createMDObjectAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createMDObjectAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation"><code><em>MD Object</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation"><code>MDObject</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEObjectAdapter()">
<h3>createEObjectAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createEObjectAdapter</span>()</div>
<div class="block">Creates a new adapter for the default case.
 <!-- begin-user-doc -->
 This default implementation returns null.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>Generated:</dt>
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
