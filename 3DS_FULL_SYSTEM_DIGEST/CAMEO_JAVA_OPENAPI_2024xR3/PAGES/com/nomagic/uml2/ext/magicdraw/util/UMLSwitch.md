# JAVA OPENAPI: UMLSwitch (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/magicdraw/util/UMLSwitch.html
- source_path: `com/nomagic/uml2/ext/magicdraw/util/UMLSwitch.html`
- source_sha256: `1113d00adbe071b859af13c983bc3539cae5e54833ccc8f45990a04f34990979`
- captured_utc: `2026-07-14T16:56:29.453837+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.util](package-summary.html)

## Class UMLSwitch<T>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.magicdraw.util.UMLSwitch<T>

public classUMLSwitch<T>
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

begin-user-doc 
 The **Switch** for the model's inheritance hierarchy.
 It supports the call [`doSwitch(object)`](#doSwitch(org.eclipse.emf.ecore.EObject))
 to invoke the `caseXXX` method for each class of the model,
 starting with the actual class of the object
 and proceeding up the inheritance hierarchy
 until a non-null result is returned,
 which is the result of the switch.
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
The cached model package
 begin-user-doc 
 end-user-doc
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[UMLSwitch](#%3Cinit%3E())()`
Creates an instance of the switch.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[T](UMLSwitch.html)`
`[caseAbstraction](#caseAbstraction(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Abstraction))([Abstraction](../classes/mddependencies/Abstraction.html) object)`
Returns the result of interpreting the object as an instance of '*Abstraction*'.
`[T](UMLSwitch.html)`
`[caseAcceptCallAction](#caseAcceptCallAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptCallAction))([AcceptCallAction](../actions/mdcompleteactions/AcceptCallAction.html) object)`
Returns the result of interpreting the object as an instance of '*Accept Call Action*'.
`[T](UMLSwitch.html)`
`[caseAcceptEventAction](#caseAcceptEventAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction))([AcceptEventAction](../actions/mdcompleteactions/AcceptEventAction.html) object)`
Returns the result of interpreting the object as an instance of '*Accept Event Action*'.
`[T](UMLSwitch.html)`
`[caseAction](#caseAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action))([Action](../actions/mdbasicactions/Action.html) object)`
Returns the result of interpreting the object as an instance of '*Action*'.
`[T](UMLSwitch.html)`
`[caseActionExecutionSpecification](#caseActionExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ActionExecutionSpecification))([ActionExecutionSpecification](../interactions/mdbasicinteractions/ActionExecutionSpecification.html) object)`
Returns the result of interpreting the object as an instance of '*Action Execution Specification*'.
`[T](UMLSwitch.html)`
`[caseActionInputPin](#caseActionInputPin(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin))([ActionInputPin](../actions/mdstructuredactions/ActionInputPin.html) object)`
Returns the result of interpreting the object as an instance of '*Action Input Pin*'.
`[T](UMLSwitch.html)`
`[caseActivity](#caseActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity))([Activity](../activities/mdfundamentalactivities/Activity.html) object)`
Returns the result of interpreting the object as an instance of '*Activity*'.
`[T](UMLSwitch.html)`
`[caseActivityEdge](#caseActivityEdge(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge))([ActivityEdge](../activities/mdbasicactivities/ActivityEdge.html) object)`
Returns the result of interpreting the object as an instance of '*Activity Edge*'.
`[T](UMLSwitch.html)`
`[caseActivityFinalNode](#caseActivityFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityFinalNode))([ActivityFinalNode](../activities/mdbasicactivities/ActivityFinalNode.html) object)`
Returns the result of interpreting the object as an instance of '*Activity Final Node*'.
`[T](UMLSwitch.html)`
`[caseActivityGroup](#caseActivityGroup(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup))([ActivityGroup](../activities/mdfundamentalactivities/ActivityGroup.html) object)`
Returns the result of interpreting the object as an instance of '*Activity Group*'.
`[T](UMLSwitch.html)`
`[caseActivityNode](#caseActivityNode(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode))([ActivityNode](../activities/mdfundamentalactivities/ActivityNode.html) object)`
Returns the result of interpreting the object as an instance of '*Activity Node*'.
`[T](UMLSwitch.html)`
`[caseActivityParameterNode](#caseActivityParameterNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode))([ActivityParameterNode](../activities/mdbasicactivities/ActivityParameterNode.html) object)`
Returns the result of interpreting the object as an instance of '*Activity Parameter Node*'.
`[T](UMLSwitch.html)`
`[caseActivityPartition](#caseActivityPartition(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ActivityPartition))([ActivityPartition](../activities/mdintermediateactivities/ActivityPartition.html) object)`
Returns the result of interpreting the object as an instance of '*Activity Partition*'.
`[T](UMLSwitch.html)`
`[caseActor](#caseActor(com.nomagic.uml2.ext.magicdraw.mdusecases.Actor))([Actor](../mdusecases/Actor.html) object)`
Returns the result of interpreting the object as an instance of '*Actor*'.
`[T](UMLSwitch.html)`
`[caseAddStructuralFeatureValueAction](#caseAddStructuralFeatureValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.AddStructuralFeatureValueAction))([AddStructuralFeatureValueAction](../actions/mdintermediateactions/AddStructuralFeatureValueAction.html) object)`
Returns the result of interpreting the object as an instance of '*Add Structural Feature Value Action*'.
`[T](UMLSwitch.html)`
`[caseAddVariableValueAction](#caseAddVariableValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.AddVariableValueAction))([AddVariableValueAction](../actions/mdstructuredactions/AddVariableValueAction.html) object)`
Returns the result of interpreting the object as an instance of '*Add Variable Value Action*'.
`[T](UMLSwitch.html)`
`[caseAnyReceiveEvent](#caseAnyReceiveEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.AnyReceiveEvent))([AnyReceiveEvent](../commonbehaviors/mdcommunications/AnyReceiveEvent.html) object)`
Returns the result of interpreting the object as an instance of '*Any Receive Event*'.
`[T](UMLSwitch.html)`
`[caseArtifact](#caseArtifact(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact))([Artifact](../deployments/mdartifacts/Artifact.html) object)`
Returns the result of interpreting the object as an instance of '*Artifact*'.
`[T](UMLSwitch.html)`
`[caseAssociation](#caseAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](../classes/mdkernel/Association.html) object)`
Returns the result of interpreting the object as an instance of '*Association*'.
`[T](UMLSwitch.html)`
`[caseAssociationClass](#caseAssociationClass(com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses.AssociationClass))([AssociationClass](../classes/mdassociationclasses/AssociationClass.html) object)`
Returns the result of interpreting the object as an instance of '*Association Class*'.
`[T](UMLSwitch.html)`
`[caseBehavior](#caseBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))([Behavior](../commonbehaviors/mdbasicbehaviors/Behavior.html) object)`
Returns the result of interpreting the object as an instance of '*Behavior*'.
`[T](UMLSwitch.html)`
`[caseBehavioralFeature](#caseBehavioralFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature))([BehavioralFeature](../classes/mdkernel/BehavioralFeature.html) object)`
Returns the result of interpreting the object as an instance of '*Behavioral Feature*'.
`[T](UMLSwitch.html)`
`[caseBehavioredClassifier](#caseBehavioredClassifier(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier))([BehavioredClassifier](../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) object)`
Returns the result of interpreting the object as an instance of '*Behaviored Classifier*'.
`[T](UMLSwitch.html)`
`[caseBehaviorExecutionSpecification](#caseBehaviorExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.BehaviorExecutionSpecification))([BehaviorExecutionSpecification](../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html) object)`
Returns the result of interpreting the object as an instance of '*Behavior Execution Specification*'.
`[T](UMLSwitch.html)`
`[caseBroadcastSignalAction](#caseBroadcastSignalAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.BroadcastSignalAction))([BroadcastSignalAction](../actions/mdintermediateactions/BroadcastSignalAction.html) object)`
Returns the result of interpreting the object as an instance of '*Broadcast Signal Action*'.
`[T](UMLSwitch.html)`
`[caseCallAction](#caseCallAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallAction))([CallAction](../actions/mdbasicactions/CallAction.html) object)`
Returns the result of interpreting the object as an instance of '*Call Action*'.
`[T](UMLSwitch.html)`
`[caseCallBehaviorAction](#caseCallBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction))([CallBehaviorAction](../actions/mdbasicactions/CallBehaviorAction.html) object)`
Returns the result of interpreting the object as an instance of '*Call Behavior Action*'.
`[T](UMLSwitch.html)`
`[caseCallEvent](#caseCallEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallEvent))([CallEvent](../commonbehaviors/mdcommunications/CallEvent.html) object)`
Returns the result of interpreting the object as an instance of '*Call Event*'.
`[T](UMLSwitch.html)`
`[caseCallOperationAction](#caseCallOperationAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallOperationAction))([CallOperationAction](../actions/mdbasicactions/CallOperationAction.html) object)`
Returns the result of interpreting the object as an instance of '*Call Operation Action*'.
`[T](UMLSwitch.html)`
`[caseCentralBufferNode](#caseCentralBufferNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.CentralBufferNode))([CentralBufferNode](../activities/mdintermediateactivities/CentralBufferNode.html) object)`
Returns the result of interpreting the object as an instance of '*Central Buffer Node*'.
`[T](UMLSwitch.html)`
`[caseChangeEvent](#caseChangeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent))([ChangeEvent](../commonbehaviors/mdcommunications/ChangeEvent.html) object)`
Returns the result of interpreting the object as an instance of '*Change Event*'.
`[T](UMLSwitch.html)`
`[caseClass](#caseClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](../classes/mdkernel/Class.html) object)`
Returns the result of interpreting the object as an instance of '*Class*'.
`[T](UMLSwitch.html)`
`[caseClassifier](#caseClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../classes/mdkernel/Classifier.html) object)`
Returns the result of interpreting the object as an instance of '*Classifier*'.
`[T](UMLSwitch.html)`
`[caseClassifierTemplateParameter](#caseClassifierTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter))([ClassifierTemplateParameter](../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html) object)`
Returns the result of interpreting the object as an instance of '*Classifier Template Parameter*'.
`[T](UMLSwitch.html)`
`[caseClause](#caseClause(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause))([Clause](../activities/mdstructuredactivities/Clause.html) object)`
Returns the result of interpreting the object as an instance of '*Clause*'.
`[T](UMLSwitch.html)`
`[caseClearAssociationAction](#caseClearAssociationAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearAssociationAction))([ClearAssociationAction](../actions/mdintermediateactions/ClearAssociationAction.html) object)`
Returns the result of interpreting the object as an instance of '*Clear Association Action*'.
`[T](UMLSwitch.html)`
`[caseClearStructuralFeatureAction](#caseClearStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearStructuralFeatureAction))([ClearStructuralFeatureAction](../actions/mdintermediateactions/ClearStructuralFeatureAction.html) object)`
Returns the result of interpreting the object as an instance of '*Clear Structural Feature Action*'.
`[T](UMLSwitch.html)`
`[caseClearVariableAction](#caseClearVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ClearVariableAction))([ClearVariableAction](../actions/mdstructuredactions/ClearVariableAction.html) object)`
Returns the result of interpreting the object as an instance of '*Clear Variable Action*'.
`[T](UMLSwitch.html)`
`[caseCollaboration](#caseCollaboration(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.Collaboration))([Collaboration](../compositestructures/mdcollaborations/Collaboration.html) object)`
Returns the result of interpreting the object as an instance of '*Collaboration*'.
`[T](UMLSwitch.html)`
`[caseCollaborationUse](#caseCollaborationUse(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse))([CollaborationUse](../compositestructures/mdcollaborations/CollaborationUse.html) object)`
Returns the result of interpreting the object as an instance of '*Collaboration Use*'.
`[T](UMLSwitch.html)`
`[caseCombinedFragment](#caseCombinedFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment))([CombinedFragment](../interactions/mdfragments/CombinedFragment.html) object)`
Returns the result of interpreting the object as an instance of '*Combined Fragment*'.
`[T](UMLSwitch.html)`
`[caseComment](#caseComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment))([Comment](../classes/mdkernel/Comment.html) object)`
Returns the result of interpreting the object as an instance of '*Comment*'.
`[T](UMLSwitch.html)`
`[caseCommunicationPath](#caseCommunicationPath(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.CommunicationPath))([CommunicationPath](../deployments/mdnodes/CommunicationPath.html) object)`
Returns the result of interpreting the object as an instance of '*Communication Path*'.
`[T](UMLSwitch.html)`
`[caseComponent](#caseComponent(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component))([Component](../components/mdbasiccomponents/Component.html) object)`
Returns the result of interpreting the object as an instance of '*Component*'.
`[T](UMLSwitch.html)`
`[caseComponentRealization](#caseComponentRealization(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.ComponentRealization))([ComponentRealization](../components/mdbasiccomponents/ComponentRealization.html) object)`
Returns the result of interpreting the object as an instance of '*Component Realization*'.
`[T](UMLSwitch.html)`
`[caseConditionalNode](#caseConditionalNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode))([ConditionalNode](../activities/mdstructuredactivities/ConditionalNode.html) object)`
Returns the result of interpreting the object as an instance of '*Conditional Node*'.
`[T](UMLSwitch.html)`
`[caseConnectableElement](#caseConnectableElement(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement))([ConnectableElement](../compositestructures/mdinternalstructures/ConnectableElement.html) object)`
Returns the result of interpreting the object as an instance of '*Connectable Element*'.
`[T](UMLSwitch.html)`
`[caseConnectableElementTemplateParameter](#caseConnectableElementTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter))([ConnectableElementTemplateParameter](../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html) object)`
Returns the result of interpreting the object as an instance of '*Connectable Element Template Parameter*'.
`[T](UMLSwitch.html)`
`[caseConnectionPointReference](#caseConnectionPointReference(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.ConnectionPointReference))([ConnectionPointReference](../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html) object)`
Returns the result of interpreting the object as an instance of '*Connection Point Reference*'.
`[T](UMLSwitch.html)`
`[caseConnector](#caseConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector))([Connector](../compositestructures/mdinternalstructures/Connector.html) object)`
Returns the result of interpreting the object as an instance of '*Connector*'.
`[T](UMLSwitch.html)`
`[caseConnectorEnd](#caseConnectorEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectorEnd))([ConnectorEnd](../compositestructures/mdinternalstructures/ConnectorEnd.html) object)`
Returns the result of interpreting the object as an instance of '*Connector End*'.
`[T](UMLSwitch.html)`
`[caseConsiderIgnoreFragment](#caseConsiderIgnoreFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.ConsiderIgnoreFragment))([ConsiderIgnoreFragment](../interactions/mdfragments/ConsiderIgnoreFragment.html) object)`
Returns the result of interpreting the object as an instance of '*Consider Ignore Fragment*'.
`[T](UMLSwitch.html)`
`[caseConstraint](#caseConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Constraint](../classes/mdkernel/Constraint.html) object)`
Returns the result of interpreting the object as an instance of '*Constraint*'.
`[T](UMLSwitch.html)`
`[caseContinuation](#caseContinuation(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Continuation))([Continuation](../interactions/mdfragments/Continuation.html) object)`
Returns the result of interpreting the object as an instance of '*Continuation*'.
`[T](UMLSwitch.html)`
`[caseControlFlow](#caseControlFlow(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ControlFlow))([ControlFlow](../activities/mdbasicactivities/ControlFlow.html) object)`
Returns the result of interpreting the object as an instance of '*Control Flow*'.
`[T](UMLSwitch.html)`
`[caseControlNode](#caseControlNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ControlNode))([ControlNode](../activities/mdbasicactivities/ControlNode.html) object)`
Returns the result of interpreting the object as an instance of '*Control Node*'.
`[T](UMLSwitch.html)`
`[caseCreateLinkAction](#caseCreateLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateLinkAction))([CreateLinkAction](../actions/mdintermediateactions/CreateLinkAction.html) object)`
Returns the result of interpreting the object as an instance of '*Create Link Action*'.
`[T](UMLSwitch.html)`
`[caseCreateLinkObjectAction](#caseCreateLinkObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.CreateLinkObjectAction))([CreateLinkObjectAction](../actions/mdcompleteactions/CreateLinkObjectAction.html) object)`
Returns the result of interpreting the object as an instance of '*Create Link Object Action*'.
`[T](UMLSwitch.html)`
`[caseCreateObjectAction](#caseCreateObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateObjectAction))([CreateObjectAction](../actions/mdintermediateactions/CreateObjectAction.html) object)`
Returns the result of interpreting the object as an instance of '*Create Object Action*'.
`[T](UMLSwitch.html)`
`[caseDataStoreNode](#caseDataStoreNode(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.DataStoreNode))([DataStoreNode](../activities/mdcompleteactivities/DataStoreNode.html) object)`
Returns the result of interpreting the object as an instance of '*Data Store Node*'.
`[T](UMLSwitch.html)`
`[caseDataType](#caseDataType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType))([DataType](../classes/mdkernel/DataType.html) object)`
Returns the result of interpreting the object as an instance of '*Data Type*'.
`[T](UMLSwitch.html)`
`[caseDecisionNode](#caseDecisionNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.DecisionNode))([DecisionNode](../activities/mdintermediateactivities/DecisionNode.html) object)`
Returns the result of interpreting the object as an instance of '*Decision Node*'.
`[T](UMLSwitch.html)`
`[caseDependency](#caseDependency(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Dependency))([Dependency](../classes/mddependencies/Dependency.html) object)`
Returns the result of interpreting the object as an instance of '*Dependency*'.
`[T](UMLSwitch.html)`
`[caseDeployedArtifact](#caseDeployedArtifact(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeployedArtifact))([DeployedArtifact](../deployments/mdnodes/DeployedArtifact.html) object)`
Returns the result of interpreting the object as an instance of '*Deployed Artifact*'.
`[T](UMLSwitch.html)`
`[caseDeployment](#caseDeployment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Deployment))([Deployment](../deployments/mdnodes/Deployment.html) object)`
Returns the result of interpreting the object as an instance of '*Deployment*'.
`[T](UMLSwitch.html)`
`[caseDeploymentSpecification](#caseDeploymentSpecification(com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments.DeploymentSpecification))([DeploymentSpecification](../deployments/mdcomponentdeployments/DeploymentSpecification.html) object)`
Returns the result of interpreting the object as an instance of '*Deployment Specification*'.
`[T](UMLSwitch.html)`
`[caseDeploymentTarget](#caseDeploymentTarget(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeploymentTarget))([DeploymentTarget](../deployments/mdnodes/DeploymentTarget.html) object)`
Returns the result of interpreting the object as an instance of '*Deployment Target*'.
`[T](UMLSwitch.html)`
`[caseDestroyLinkAction](#caseDestroyLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyLinkAction))([DestroyLinkAction](../actions/mdintermediateactions/DestroyLinkAction.html) object)`
Returns the result of interpreting the object as an instance of '*Destroy Link Action*'.
`[T](UMLSwitch.html)`
`[caseDestroyObjectAction](#caseDestroyObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyObjectAction))([DestroyObjectAction](../actions/mdintermediateactions/DestroyObjectAction.html) object)`
Returns the result of interpreting the object as an instance of '*Destroy Object Action*'.
`[T](UMLSwitch.html)`
`[caseDestructionOccurrenceSpecification](#caseDestructionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.DestructionOccurrenceSpecification))([DestructionOccurrenceSpecification](../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html) object)`
Returns the result of interpreting the object as an instance of '*Destruction Occurrence Specification*'.
`[T](UMLSwitch.html)`
`[caseDevice](#caseDevice(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Device))([Device](../deployments/mdnodes/Device.html) object)`
Returns the result of interpreting the object as an instance of '*Device*'.
`[T](UMLSwitch.html)`
`[caseDiagram](#caseDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../classes/mdkernel/Diagram.html) object)`
Returns the result of interpreting the object as an instance of '*Diagram*'.
`[T](UMLSwitch.html)`
`[caseDirectedRelationship](#caseDirectedRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DirectedRelationship))([DirectedRelationship](../classes/mdkernel/DirectedRelationship.html) object)`
Returns the result of interpreting the object as an instance of '*Directed Relationship*'.
`[T](UMLSwitch.html)`
`[caseDuration](#caseDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration))([Duration](../commonbehaviors/mdsimpletime/Duration.html) object)`
Returns the result of interpreting the object as an instance of '*Duration*'.
`[T](UMLSwitch.html)`
`[caseDurationConstraint](#caseDurationConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint))([DurationConstraint](../commonbehaviors/mdsimpletime/DurationConstraint.html) object)`
Returns the result of interpreting the object as an instance of '*Duration Constraint*'.
`[T](UMLSwitch.html)`
`[caseDurationInterval](#caseDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval))([DurationInterval](../commonbehaviors/mdsimpletime/DurationInterval.html) object)`
Returns the result of interpreting the object as an instance of '*Duration Interval*'.
`[T](UMLSwitch.html)`
`[caseDurationObservation](#caseDurationObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationObservation))([DurationObservation](../commonbehaviors/mdsimpletime/DurationObservation.html) object)`
Returns the result of interpreting the object as an instance of '*Duration Observation*'.
`[T](UMLSwitch.html)`
`[caseElement](#caseElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../classes/mdkernel/Element.html) object)`
Returns the result of interpreting the object as an instance of '*Element*'.
`[T](UMLSwitch.html)`
`[caseElementImport](#caseElementImport(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementImport))([ElementImport](../classes/mdkernel/ElementImport.html) object)`
Returns the result of interpreting the object as an instance of '*Element Import*'.
`[T](UMLSwitch.html)`
`[caseElementValue](#caseElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementValue))([ElementValue](../classes/mdkernel/ElementValue.html) object)`
Returns the result of interpreting the object as an instance of '*Element Value*'.
`[T](UMLSwitch.html)`
`[caseEncapsulatedClassifier](#caseEncapsulatedClassifier(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier))([EncapsulatedClassifier](../compositestructures/mdports/EncapsulatedClassifier.html) object)`
Returns the result of interpreting the object as an instance of '*Encapsulated Classifier*'.
`[T](UMLSwitch.html)`
`[caseEnumeration](#caseEnumeration(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration))([Enumeration](../classes/mdkernel/Enumeration.html) object)`
Returns the result of interpreting the object as an instance of '*Enumeration*'.
`[T](UMLSwitch.html)`
`[caseEnumerationLiteral](#caseEnumerationLiteral(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([EnumerationLiteral](../classes/mdkernel/EnumerationLiteral.html) object)`
Returns the result of interpreting the object as an instance of '*Enumeration Literal*'.
`[T](UMLSwitch.html)`
`[caseEvent](#caseEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event))([Event](../commonbehaviors/mdcommunications/Event.html) object)`
Returns the result of interpreting the object as an instance of '*Event*'.
`[T](UMLSwitch.html)`
`[caseExceptionHandler](#caseExceptionHandler(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExceptionHandler))([ExceptionHandler](../activities/mdextrastructuredactivities/ExceptionHandler.html) object)`
Returns the result of interpreting the object as an instance of '*Exception Handler*'.
`[T](UMLSwitch.html)`
`[caseExecutableNode](#caseExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ExecutableNode))([ExecutableNode](../activities/mdstructuredactivities/ExecutableNode.html) object)`
Returns the result of interpreting the object as an instance of '*Executable Node*'.
`[T](UMLSwitch.html)`
`[caseExecutionEnvironment](#caseExecutionEnvironment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.ExecutionEnvironment))([ExecutionEnvironment](../deployments/mdnodes/ExecutionEnvironment.html) object)`
Returns the result of interpreting the object as an instance of '*Execution Environment*'.
`[T](UMLSwitch.html)`
`[caseExecutionOccurrenceSpecification](#caseExecutionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ExecutionOccurrenceSpecification))([ExecutionOccurrenceSpecification](../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html) object)`
Returns the result of interpreting the object as an instance of '*Execution Occurrence Specification*'.
`[T](UMLSwitch.html)`
`[caseExecutionSpecification](#caseExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ExecutionSpecification))([ExecutionSpecification](../interactions/mdbasicinteractions/ExecutionSpecification.html) object)`
Returns the result of interpreting the object as an instance of '*Execution Specification*'.
`[T](UMLSwitch.html)`
`[caseExpansionNode](#caseExpansionNode(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExpansionNode))([ExpansionNode](../activities/mdextrastructuredactivities/ExpansionNode.html) object)`
Returns the result of interpreting the object as an instance of '*Expansion Node*'.
`[T](UMLSwitch.html)`
`[caseExpansionRegion](#caseExpansionRegion(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExpansionRegion))([ExpansionRegion](../activities/mdextrastructuredactivities/ExpansionRegion.html) object)`
Returns the result of interpreting the object as an instance of '*Expansion Region*'.
`[T](UMLSwitch.html)`
`[caseExpression](#caseExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression))([Expression](../classes/mdkernel/Expression.html) object)`
Returns the result of interpreting the object as an instance of '*Expression*'.
`[T](UMLSwitch.html)`
`[caseExtend](#caseExtend(com.nomagic.uml2.ext.magicdraw.mdusecases.Extend))([Extend](../mdusecases/Extend.html) object)`
Returns the result of interpreting the object as an instance of '*Extend*'.
`[T](UMLSwitch.html)`
`[caseExtension](#caseExtension(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension))([Extension](../mdprofiles/Extension.html) object)`
Returns the result of interpreting the object as an instance of '*Extension*'.
`[T](UMLSwitch.html)`
`[caseExtensionEnd](#caseExtensionEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.ExtensionEnd))([ExtensionEnd](../mdprofiles/ExtensionEnd.html) object)`
Returns the result of interpreting the object as an instance of '*Extension End*'.
`[T](UMLSwitch.html)`
`[caseExtensionPoint](#caseExtensionPoint(com.nomagic.uml2.ext.magicdraw.mdusecases.ExtensionPoint))([ExtensionPoint](../mdusecases/ExtensionPoint.html) object)`
Returns the result of interpreting the object as an instance of '*Extension Point*'.
`[T](UMLSwitch.html)`
`[caseFeature](#caseFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Feature))([Feature](../classes/mdkernel/Feature.html) object)`
Returns the result of interpreting the object as an instance of '*Feature*'.
`[T](UMLSwitch.html)`
`[caseFinalNode](#caseFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.FinalNode))([FinalNode](../activities/mdintermediateactivities/FinalNode.html) object)`
Returns the result of interpreting the object as an instance of '*Final Node*'.
`[T](UMLSwitch.html)`
`[caseFinalState](#caseFinalState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.FinalState))([FinalState](../statemachines/mdbehaviorstatemachines/FinalState.html) object)`
Returns the result of interpreting the object as an instance of '*Final State*'.
`[T](UMLSwitch.html)`
`[caseFlowFinalNode](#caseFlowFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.FlowFinalNode))([FlowFinalNode](../activities/mdintermediateactivities/FlowFinalNode.html) object)`
Returns the result of interpreting the object as an instance of '*Flow Final Node*'.
`[T](UMLSwitch.html)`
`[caseForkNode](#caseForkNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ForkNode))([ForkNode](../activities/mdintermediateactivities/ForkNode.html) object)`
Returns the result of interpreting the object as an instance of '*Fork Node*'.
`[T](UMLSwitch.html)`
`[caseFunctionBehavior](#caseFunctionBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.FunctionBehavior))([FunctionBehavior](../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html) object)`
Returns the result of interpreting the object as an instance of '*Function Behavior*'.
`[T](UMLSwitch.html)`
`[caseGate](#caseGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate))([Gate](../interactions/mdfragments/Gate.html) object)`
Returns the result of interpreting the object as an instance of '*Gate*'.
`[T](UMLSwitch.html)`
`[caseGeneralization](#caseGeneralization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Generalization))([Generalization](../classes/mdkernel/Generalization.html) object)`
Returns the result of interpreting the object as an instance of '*Generalization*'.
`[T](UMLSwitch.html)`
`[caseGeneralizationSet](#caseGeneralizationSet(com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes.GeneralizationSet))([GeneralizationSet](../classes/mdpowertypes/GeneralizationSet.html) object)`
Returns the result of interpreting the object as an instance of '*Generalization Set*'.
`[T](UMLSwitch.html)`
`[caseGeneralOrdering](#caseGeneralOrdering(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.GeneralOrdering))([GeneralOrdering](../interactions/mdbasicinteractions/GeneralOrdering.html) object)`
Returns the result of interpreting the object as an instance of '*General Ordering*'.
`[T](UMLSwitch.html)`
`[caseImage](#caseImage(com.nomagic.uml2.ext.magicdraw.mdprofiles.Image))([Image](../mdprofiles/Image.html) object)`
Returns the result of interpreting the object as an instance of '*Image*'.
`[T](UMLSwitch.html)`
`[caseInclude](#caseInclude(com.nomagic.uml2.ext.magicdraw.mdusecases.Include))([Include](../mdusecases/Include.html) object)`
Returns the result of interpreting the object as an instance of '*Include*'.
`[T](UMLSwitch.html)`
`[caseInformationFlow](#caseInformationFlow(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows.InformationFlow))([InformationFlow](../auxiliaryconstructs/mdinformationflows/InformationFlow.html) object)`
Returns the result of interpreting the object as an instance of '*Information Flow*'.
`[T](UMLSwitch.html)`
`[caseInformationItem](#caseInformationItem(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows.InformationItem))([InformationItem](../auxiliaryconstructs/mdinformationflows/InformationItem.html) object)`
Returns the result of interpreting the object as an instance of '*Information Item*'.
`[T](UMLSwitch.html)`
`[caseInitialNode](#caseInitialNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.InitialNode))([InitialNode](../activities/mdbasicactivities/InitialNode.html) object)`
Returns the result of interpreting the object as an instance of '*Initial Node*'.
`[T](UMLSwitch.html)`
`[caseInputPin](#caseInputPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin))([InputPin](../actions/mdbasicactions/InputPin.html) object)`
Returns the result of interpreting the object as an instance of '*Input Pin*'.
`[T](UMLSwitch.html)`
`[caseInstanceSpecification](#caseInstanceSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([InstanceSpecification](../classes/mdkernel/InstanceSpecification.html) object)`
Returns the result of interpreting the object as an instance of '*Instance Specification*'.
`[T](UMLSwitch.html)`
`[caseInstanceValue](#caseInstanceValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceValue))([InstanceValue](../classes/mdkernel/InstanceValue.html) object)`
Returns the result of interpreting the object as an instance of '*Instance Value*'.
`[T](UMLSwitch.html)`
`[caseInteraction](#caseInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction))([Interaction](../interactions/mdbasicinteractions/Interaction.html) object)`
Returns the result of interpreting the object as an instance of '*Interaction*'.
`[T](UMLSwitch.html)`
`[caseInteractionConstraint](#caseInteractionConstraint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint))([InteractionConstraint](../interactions/mdfragments/InteractionConstraint.html) object)`
Returns the result of interpreting the object as an instance of '*Interaction Constraint*'.
`[T](UMLSwitch.html)`
`[caseInteractionFragment](#caseInteractionFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.InteractionFragment))([InteractionFragment](../interactions/mdbasicinteractions/InteractionFragment.html) object)`
Returns the result of interpreting the object as an instance of '*Interaction Fragment*'.
`[T](UMLSwitch.html)`
`[caseInteractionOperand](#caseInteractionOperand(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand))([InteractionOperand](../interactions/mdfragments/InteractionOperand.html) object)`
Returns the result of interpreting the object as an instance of '*Interaction Operand*'.
`[T](UMLSwitch.html)`
`[caseInteractionUse](#caseInteractionUse(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse))([InteractionUse](../interactions/mdfragments/InteractionUse.html) object)`
Returns the result of interpreting the object as an instance of '*Interaction Use*'.
`[T](UMLSwitch.html)`
`[caseInterface](#caseInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface))([Interface](../classes/mdinterfaces/Interface.html) object)`
Returns the result of interpreting the object as an instance of '*Interface*'.
`[T](UMLSwitch.html)`
`[caseInterfaceRealization](#caseInterfaceRealization(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.InterfaceRealization))([InterfaceRealization](../classes/mdinterfaces/InterfaceRealization.html) object)`
Returns the result of interpreting the object as an instance of '*Interface Realization*'.
`[T](UMLSwitch.html)`
`[caseInterruptibleActivityRegion](#caseInterruptibleActivityRegion(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.InterruptibleActivityRegion))([InterruptibleActivityRegion](../activities/mdcompleteactivities/InterruptibleActivityRegion.html) object)`
Returns the result of interpreting the object as an instance of '*Interruptible Activity Region*'.
`[T](UMLSwitch.html)`
`[caseInterval](#caseInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Interval))([Interval](../commonbehaviors/mdsimpletime/Interval.html) object)`
Returns the result of interpreting the object as an instance of '*Interval*'.
`[T](UMLSwitch.html)`
`[caseIntervalConstraint](#caseIntervalConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint))([IntervalConstraint](../commonbehaviors/mdsimpletime/IntervalConstraint.html) object)`
Returns the result of interpreting the object as an instance of '*Interval Constraint*'.
`[T](UMLSwitch.html)`
`[caseInvocationAction](#caseInvocationAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction))([InvocationAction](../actions/mdbasicactions/InvocationAction.html) object)`
Returns the result of interpreting the object as an instance of '*Invocation Action*'.
`[T](UMLSwitch.html)`
`[caseJoinNode](#caseJoinNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode))([JoinNode](../activities/mdintermediateactivities/JoinNode.html) object)`
Returns the result of interpreting the object as an instance of '*Join Node*'.
`[T](UMLSwitch.html)`
`[caseLifeline](#caseLifeline(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline))([Lifeline](../interactions/mdbasicinteractions/Lifeline.html) object)`
Returns the result of interpreting the object as an instance of '*Lifeline*'.
`[T](UMLSwitch.html)`
`[caseLinkAction](#caseLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction))([LinkAction](../actions/mdintermediateactions/LinkAction.html) object)`
Returns the result of interpreting the object as an instance of '*Link Action*'.
`[T](UMLSwitch.html)`
`[caseLinkEndCreationData](#caseLinkEndCreationData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndCreationData))([LinkEndCreationData](../actions/mdintermediateactions/LinkEndCreationData.html) object)`
Returns the result of interpreting the object as an instance of '*Link End Creation Data*'.
`[T](UMLSwitch.html)`
`[caseLinkEndData](#caseLinkEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndData))([LinkEndData](../actions/mdintermediateactions/LinkEndData.html) object)`
Returns the result of interpreting the object as an instance of '*Link End Data*'.
`[T](UMLSwitch.html)`
`[caseLinkEndDestructionData](#caseLinkEndDestructionData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndDestructionData))([LinkEndDestructionData](../actions/mdintermediateactions/LinkEndDestructionData.html) object)`
Returns the result of interpreting the object as an instance of '*Link End Destruction Data*'.
`[T](UMLSwitch.html)`
`[caseLiteralBoolean](#caseLiteralBoolean(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralBoolean))([LiteralBoolean](../classes/mdkernel/LiteralBoolean.html) object)`
Returns the result of interpreting the object as an instance of '*Literal Boolean*'.
`[T](UMLSwitch.html)`
`[caseLiteralInteger](#caseLiteralInteger(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralInteger))([LiteralInteger](../classes/mdkernel/LiteralInteger.html) object)`
Returns the result of interpreting the object as an instance of '*Literal Integer*'.
`[T](UMLSwitch.html)`
`[caseLiteralNull](#caseLiteralNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralNull))([LiteralNull](../classes/mdkernel/LiteralNull.html) object)`
Returns the result of interpreting the object as an instance of '*Literal Null*'.
`[T](UMLSwitch.html)`
`[caseLiteralReal](#caseLiteralReal(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralReal))([LiteralReal](../classes/mdkernel/LiteralReal.html) object)`
Returns the result of interpreting the object as an instance of '*Literal Real*'.
`[T](UMLSwitch.html)`
`[caseLiteralSpecification](#caseLiteralSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralSpecification))([LiteralSpecification](../classes/mdkernel/LiteralSpecification.html) object)`
Returns the result of interpreting the object as an instance of '*Literal Specification*'.
`[T](UMLSwitch.html)`
`[caseLiteralString](#caseLiteralString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralString))([LiteralString](../classes/mdkernel/LiteralString.html) object)`
Returns the result of interpreting the object as an instance of '*Literal String*'.
`[T](UMLSwitch.html)`
`[caseLiteralUnlimitedNatural](#caseLiteralUnlimitedNatural(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralUnlimitedNatural))([LiteralUnlimitedNatural](../classes/mdkernel/LiteralUnlimitedNatural.html) object)`
Returns the result of interpreting the object as an instance of '*Literal Unlimited Natural*'.
`[T](UMLSwitch.html)`
`[caseLoopNode](#caseLoopNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))([LoopNode](../activities/mdstructuredactivities/LoopNode.html) object)`
Returns the result of interpreting the object as an instance of '*Loop Node*'.
`[T](UMLSwitch.html)`
`[caseManifestation](#caseManifestation(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Manifestation))([Manifestation](../deployments/mdartifacts/Manifestation.html) object)`
Returns the result of interpreting the object as an instance of '*Manifestation*'.
`[T](UMLSwitch.html)`
`[caseMDObject](#caseMDObject(com.nomagic.magicdraw.foundation.MDObject))([MDObject](../../../../magicdraw/foundation/MDObject.html) object)`
Returns the result of interpreting the object as an instance of '*MD Object*'.
`[T](UMLSwitch.html)`
`[caseMergeNode](#caseMergeNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.MergeNode))([MergeNode](../activities/mdintermediateactivities/MergeNode.html) object)`
Returns the result of interpreting the object as an instance of '*Merge Node*'.
`[T](UMLSwitch.html)`
`[caseMessage](#caseMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../interactions/mdbasicinteractions/Message.html) object)`
Returns the result of interpreting the object as an instance of '*Message*'.
`[T](UMLSwitch.html)`
`[caseMessageEnd](#caseMessageEnd(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd))([MessageEnd](../interactions/mdbasicinteractions/MessageEnd.html) object)`
Returns the result of interpreting the object as an instance of '*Message End*'.
`[T](UMLSwitch.html)`
`[caseMessageEvent](#caseMessageEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.MessageEvent))([MessageEvent](../commonbehaviors/mdcommunications/MessageEvent.html) object)`
Returns the result of interpreting the object as an instance of '*Message Event*'.
`[T](UMLSwitch.html)`
`[caseMessageOccurrenceSpecification](#caseMessageOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageOccurrenceSpecification))([MessageOccurrenceSpecification](../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html) object)`
Returns the result of interpreting the object as an instance of '*Message Occurrence Specification*'.
`[T](UMLSwitch.html)`
`[caseModel](#caseModel(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model))([Model](../auxiliaryconstructs/mdmodels/Model.html) object)`
Returns the result of interpreting the object as an instance of '*Model*'.
`[T](UMLSwitch.html)`
`[caseModelObject](#caseModelObject(com.nomagic.uml2.ext.magicdraw.base.ModelObject))([ModelObject](../base/ModelObject.html) object)`
Returns the result of interpreting the object as an instance of '*Model Object*'.
`[T](UMLSwitch.html)`
`[caseMultiplicityElement](#caseMultiplicityElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement))([MultiplicityElement](../classes/mdkernel/MultiplicityElement.html) object)`
Returns the result of interpreting the object as an instance of '*Multiplicity Element*'.
`[T](UMLSwitch.html)`
`[caseNamedElement](#caseNamedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement))([NamedElement](../classes/mdkernel/NamedElement.html) object)`
Returns the result of interpreting the object as an instance of '*Named Element*'.
`[T](UMLSwitch.html)`
`[caseNamespace](#caseNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([Namespace](../classes/mdkernel/Namespace.html) object)`
Returns the result of interpreting the object as an instance of '*Namespace*'.
`[T](UMLSwitch.html)`
`[caseNode](#caseNode(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Node))([Node](../deployments/mdnodes/Node.html) object)`
Returns the result of interpreting the object as an instance of '*Node*'.
`[T](UMLSwitch.html)`
`[caseObjectFlow](#caseObjectFlow(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectFlow))([ObjectFlow](../activities/mdbasicactivities/ObjectFlow.html) object)`
Returns the result of interpreting the object as an instance of '*Object Flow*'.
`[T](UMLSwitch.html)`
`[caseObjectNode](#caseObjectNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode))([ObjectNode](../activities/mdbasicactivities/ObjectNode.html) object)`
Returns the result of interpreting the object as an instance of '*Object Node*'.
`[T](UMLSwitch.html)`
`[caseObservation](#caseObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Observation))([Observation](../commonbehaviors/mdsimpletime/Observation.html) object)`
Returns the result of interpreting the object as an instance of '*Observation*'.
`[T](UMLSwitch.html)`
`[caseOccurrenceSpecification](#caseOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.OccurrenceSpecification))([OccurrenceSpecification](../interactions/mdbasicinteractions/OccurrenceSpecification.html) object)`
Returns the result of interpreting the object as an instance of '*Occurrence Specification*'.
`[T](UMLSwitch.html)`
`[caseOpaqueAction](#caseOpaqueAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction))([OpaqueAction](../actions/mdbasicactions/OpaqueAction.html) object)`
Returns the result of interpreting the object as an instance of '*Opaque Action*'.
`[T](UMLSwitch.html)`
`[caseOpaqueBehavior](#caseOpaqueBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.OpaqueBehavior))([OpaqueBehavior](../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html) object)`
Returns the result of interpreting the object as an instance of '*Opaque Behavior*'.
`[T](UMLSwitch.html)`
`[caseOpaqueExpression](#caseOpaqueExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression))([OpaqueExpression](../classes/mdkernel/OpaqueExpression.html) object)`
Returns the result of interpreting the object as an instance of '*Opaque Expression*'.
`[T](UMLSwitch.html)`
`[caseOperation](#caseOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation))([Operation](../classes/mdkernel/Operation.html) object)`
Returns the result of interpreting the object as an instance of '*Operation*'.
`[T](UMLSwitch.html)`
`[caseOperationTemplateParameter](#caseOperationTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.OperationTemplateParameter))([OperationTemplateParameter](../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html) object)`
Returns the result of interpreting the object as an instance of '*Operation Template Parameter*'.
`[T](UMLSwitch.html)`
`[caseOutputPin](#caseOutputPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin))([OutputPin](../actions/mdbasicactions/OutputPin.html) object)`
Returns the result of interpreting the object as an instance of '*Output Pin*'.
`[T](UMLSwitch.html)`
`[casePackage](#casePackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../classes/mdkernel/Package.html) object)`
Returns the result of interpreting the object as an instance of '*Package*'.
`[T](UMLSwitch.html)`
`[casePackageableElement](#casePackageableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement))([PackageableElement](../classes/mdkernel/PackageableElement.html) object)`
Returns the result of interpreting the object as an instance of '*Packageable Element*'.
`[T](UMLSwitch.html)`
`[casePackageImport](#casePackageImport(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageImport))([PackageImport](../classes/mdkernel/PackageImport.html) object)`
Returns the result of interpreting the object as an instance of '*Package Import*'.
`[T](UMLSwitch.html)`
`[casePackageMerge](#casePackageMerge(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageMerge))([PackageMerge](../classes/mdkernel/PackageMerge.html) object)`
Returns the result of interpreting the object as an instance of '*Package Merge*'.
`[T](UMLSwitch.html)`
`[caseParameter](#caseParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter))([Parameter](../classes/mdkernel/Parameter.html) object)`
Returns the result of interpreting the object as an instance of '*Parameter*'.
`[T](UMLSwitch.html)`
`[caseParameterableElement](#caseParameterableElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement))([ParameterableElement](../auxiliaryconstructs/mdtemplates/ParameterableElement.html) object)`
Returns the result of interpreting the object as an instance of '*Parameterable Element*'.
`[T](UMLSwitch.html)`
`[caseParameterSet](#caseParameterSet(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterSet))([ParameterSet](../activities/mdcompleteactivities/ParameterSet.html) object)`
Returns the result of interpreting the object as an instance of '*Parameter Set*'.
`[T](UMLSwitch.html)`
`[casePartDecomposition](#casePartDecomposition(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.PartDecomposition))([PartDecomposition](../interactions/mdfragments/PartDecomposition.html) object)`
Returns the result of interpreting the object as an instance of '*Part Decomposition*'.
`[T](UMLSwitch.html)`
`[casePin](#casePin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin))([Pin](../actions/mdbasicactions/Pin.html) object)`
Returns the result of interpreting the object as an instance of '*Pin*'.
`[T](UMLSwitch.html)`
`[casePort](#casePort(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port))([Port](../compositestructures/mdports/Port.html) object)`
Returns the result of interpreting the object as an instance of '*Port*'.
`[T](UMLSwitch.html)`
`[casePrimitiveType](#casePrimitiveType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PrimitiveType))([PrimitiveType](../classes/mdkernel/PrimitiveType.html) object)`
Returns the result of interpreting the object as an instance of '*Primitive Type*'.
`[T](UMLSwitch.html)`
`[caseProfile](#caseProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))([Profile](../mdprofiles/Profile.html) object)`
Returns the result of interpreting the object as an instance of '*Profile*'.
`[T](UMLSwitch.html)`
`[caseProfileApplication](#caseProfileApplication(com.nomagic.uml2.ext.magicdraw.mdprofiles.ProfileApplication))([ProfileApplication](../mdprofiles/ProfileApplication.html) object)`
Returns the result of interpreting the object as an instance of '*Profile Application*'.
`[T](UMLSwitch.html)`
`[caseProperty](#caseProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Property](../classes/mdkernel/Property.html) object)`
Returns the result of interpreting the object as an instance of '*Property*'.
`[T](UMLSwitch.html)`
`[caseProtocolConformance](#caseProtocolConformance(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolConformance))([ProtocolConformance](../statemachines/mdprotocolstatemachines/ProtocolConformance.html) object)`
Returns the result of interpreting the object as an instance of '*Protocol Conformance*'.
`[T](UMLSwitch.html)`
`[caseProtocolStateMachine](#caseProtocolStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine))([ProtocolStateMachine](../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html) object)`
Returns the result of interpreting the object as an instance of '*Protocol State Machine*'.
`[T](UMLSwitch.html)`
`[caseProtocolTransition](#caseProtocolTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition))([ProtocolTransition](../statemachines/mdprotocolstatemachines/ProtocolTransition.html) object)`
Returns the result of interpreting the object as an instance of '*Protocol Transition*'.
`[T](UMLSwitch.html)`
`[casePseudostate](#casePseudostate(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Pseudostate))([Pseudostate](../statemachines/mdbehaviorstatemachines/Pseudostate.html) object)`
Returns the result of interpreting the object as an instance of '*Pseudostate*'.
`[T](UMLSwitch.html)`
`[caseQualifierValue](#caseQualifierValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.QualifierValue))([QualifierValue](../actions/mdcompleteactions/QualifierValue.html) object)`
Returns the result of interpreting the object as an instance of '*Qualifier Value*'.
`[T](UMLSwitch.html)`
`[caseRaiseExceptionAction](#caseRaiseExceptionAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RaiseExceptionAction))([RaiseExceptionAction](../actions/mdstructuredactions/RaiseExceptionAction.html) object)`
Returns the result of interpreting the object as an instance of '*Raise Exception Action*'.
`[T](UMLSwitch.html)`
`[caseReadExtentAction](#caseReadExtentAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadExtentAction))([ReadExtentAction](../actions/mdcompleteactions/ReadExtentAction.html) object)`
Returns the result of interpreting the object as an instance of '*Read Extent Action*'.
`[T](UMLSwitch.html)`
`[caseReadIsClassifiedObjectAction](#caseReadIsClassifiedObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction))([ReadIsClassifiedObjectAction](../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html) object)`
Returns the result of interpreting the object as an instance of '*Read Is Classified Object Action*'.
`[T](UMLSwitch.html)`
`[caseReadLinkAction](#caseReadLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadLinkAction))([ReadLinkAction](../actions/mdintermediateactions/ReadLinkAction.html) object)`
Returns the result of interpreting the object as an instance of '*Read Link Action*'.
`[T](UMLSwitch.html)`
`[caseReadLinkObjectEndAction](#caseReadLinkObjectEndAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction))([ReadLinkObjectEndAction](../actions/mdcompleteactions/ReadLinkObjectEndAction.html) object)`
Returns the result of interpreting the object as an instance of '*Read Link Object End Action*'.
`[T](UMLSwitch.html)`
`[caseReadLinkObjectEndQualifierAction](#caseReadLinkObjectEndQualifierAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction))([ReadLinkObjectEndQualifierAction](../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html) object)`
Returns the result of interpreting the object as an instance of '*Read Link Object End Qualifier Action*'.
`[T](UMLSwitch.html)`
`[caseReadSelfAction](#caseReadSelfAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadSelfAction))([ReadSelfAction](../actions/mdintermediateactions/ReadSelfAction.html) object)`
Returns the result of interpreting the object as an instance of '*Read Self Action*'.
`[T](UMLSwitch.html)`
`[caseReadStructuralFeatureAction](#caseReadStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadStructuralFeatureAction))([ReadStructuralFeatureAction](../actions/mdintermediateactions/ReadStructuralFeatureAction.html) object)`
Returns the result of interpreting the object as an instance of '*Read Structural Feature Action*'.
`[T](UMLSwitch.html)`
`[caseReadVariableAction](#caseReadVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ReadVariableAction))([ReadVariableAction](../actions/mdstructuredactions/ReadVariableAction.html) object)`
Returns the result of interpreting the object as an instance of '*Read Variable Action*'.
`[T](UMLSwitch.html)`
`[caseRealization](#caseRealization(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Realization))([Realization](../classes/mddependencies/Realization.html) object)`
Returns the result of interpreting the object as an instance of '*Realization*'.
`[T](UMLSwitch.html)`
`[caseReception](#caseReception(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception))([Reception](../commonbehaviors/mdcommunications/Reception.html) object)`
Returns the result of interpreting the object as an instance of '*Reception*'.
`[T](UMLSwitch.html)`
`[caseReclassifyObjectAction](#caseReclassifyObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReclassifyObjectAction))([ReclassifyObjectAction](../actions/mdcompleteactions/ReclassifyObjectAction.html) object)`
Returns the result of interpreting the object as an instance of '*Reclassify Object Action*'.
`[T](UMLSwitch.html)`
`[caseRedefinableElement](#caseRedefinableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement))([RedefinableElement](../classes/mdkernel/RedefinableElement.html) object)`
Returns the result of interpreting the object as an instance of '*Redefinable Element*'.
`[T](UMLSwitch.html)`
`[caseRedefinableTemplateSignature](#caseRedefinableTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature))([RedefinableTemplateSignature](../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html) object)`
Returns the result of interpreting the object as an instance of '*Redefinable Template Signature*'.
`[T](UMLSwitch.html)`
`[caseReduceAction](#caseReduceAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction))([ReduceAction](../actions/mdcompleteactions/ReduceAction.html) object)`
Returns the result of interpreting the object as an instance of '*Reduce Action*'.
`[T](UMLSwitch.html)`
`[caseRegion](#caseRegion(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region))([Region](../statemachines/mdbehaviorstatemachines/Region.html) object)`
Returns the result of interpreting the object as an instance of '*Region*'.
`[T](UMLSwitch.html)`
`[caseRelationship](#caseRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Relationship))([Relationship](../classes/mdkernel/Relationship.html) object)`
Returns the result of interpreting the object as an instance of '*Relationship*'.
`[T](UMLSwitch.html)`
`[caseRemoveStructuralFeatureValueAction](#caseRemoveStructuralFeatureValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.RemoveStructuralFeatureValueAction))([RemoveStructuralFeatureValueAction](../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html) object)`
Returns the result of interpreting the object as an instance of '*Remove Structural Feature Value Action*'.
`[T](UMLSwitch.html)`
`[caseRemoveVariableValueAction](#caseRemoveVariableValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RemoveVariableValueAction))([RemoveVariableValueAction](../actions/mdstructuredactions/RemoveVariableValueAction.html) object)`
Returns the result of interpreting the object as an instance of '*Remove Variable Value Action*'.
`[T](UMLSwitch.html)`
`[caseReplyAction](#caseReplyAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction))([ReplyAction](../actions/mdcompleteactions/ReplyAction.html) object)`
Returns the result of interpreting the object as an instance of '*Reply Action*'.
`[T](UMLSwitch.html)`
`[caseSendObjectAction](#caseSendObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction))([SendObjectAction](../actions/mdintermediateactions/SendObjectAction.html) object)`
Returns the result of interpreting the object as an instance of '*Send Object Action*'.
`[T](UMLSwitch.html)`
`[caseSendSignalAction](#caseSendSignalAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.SendSignalAction))([SendSignalAction](../actions/mdbasicactions/SendSignalAction.html) object)`
Returns the result of interpreting the object as an instance of '*Send Signal Action*'.
`[T](UMLSwitch.html)`
`[caseSequenceNode](#caseSequenceNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode))([SequenceNode](../activities/mdstructuredactivities/SequenceNode.html) object)`
Returns the result of interpreting the object as an instance of '*Sequence Node*'.
`[T](UMLSwitch.html)`
`[caseSignal](#caseSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal))([Signal](../commonbehaviors/mdcommunications/Signal.html) object)`
Returns the result of interpreting the object as an instance of '*Signal*'.
`[T](UMLSwitch.html)`
`[caseSignalEvent](#caseSignalEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.SignalEvent))([SignalEvent](../commonbehaviors/mdcommunications/SignalEvent.html) object)`
Returns the result of interpreting the object as an instance of '*Signal Event*'.
`[T](UMLSwitch.html)`
`[caseSlot](#caseSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot))([Slot](../classes/mdkernel/Slot.html) object)`
Returns the result of interpreting the object as an instance of '*Slot*'.
`[T](UMLSwitch.html)`
`[caseStartClassifierBehaviorAction](#caseStartClassifierBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartClassifierBehaviorAction))([StartClassifierBehaviorAction](../actions/mdcompleteactions/StartClassifierBehaviorAction.html) object)`
Returns the result of interpreting the object as an instance of '*Start Classifier Behavior Action*'.
`[T](UMLSwitch.html)`
`[caseStartObjectBehaviorAction](#caseStartObjectBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartObjectBehaviorAction))([StartObjectBehaviorAction](../actions/mdcompleteactions/StartObjectBehaviorAction.html) object)`
Returns the result of interpreting the object as an instance of '*Start Object Behavior Action*'.
`[T](UMLSwitch.html)`
`[caseState](#caseState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))([State](../statemachines/mdbehaviorstatemachines/State.html) object)`
Returns the result of interpreting the object as an instance of '*State*'.
`[T](UMLSwitch.html)`
`[caseStateInvariant](#caseStateInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant))([StateInvariant](../interactions/mdbasicinteractions/StateInvariant.html) object)`
Returns the result of interpreting the object as an instance of '*State Invariant*'.
`[T](UMLSwitch.html)`
`[caseStateMachine](#caseStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine))([StateMachine](../statemachines/mdbehaviorstatemachines/StateMachine.html) object)`
Returns the result of interpreting the object as an instance of '*State Machine*'.
`[T](UMLSwitch.html)`
`[caseStereotype](#caseStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../mdprofiles/Stereotype.html) object)`
Returns the result of interpreting the object as an instance of '*Stereotype*'.
`[T](UMLSwitch.html)`
`[caseStringExpression](#caseStringExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression))([StringExpression](../auxiliaryconstructs/mdtemplates/StringExpression.html) object)`
Returns the result of interpreting the object as an instance of '*String Expression*'.
`[T](UMLSwitch.html)`
`[caseStructuralFeature](#caseStructuralFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature))([StructuralFeature](../classes/mdkernel/StructuralFeature.html) object)`
Returns the result of interpreting the object as an instance of '*Structural Feature*'.
`[T](UMLSwitch.html)`
`[caseStructuralFeatureAction](#caseStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.StructuralFeatureAction))([StructuralFeatureAction](../actions/mdintermediateactions/StructuralFeatureAction.html) object)`
Returns the result of interpreting the object as an instance of '*Structural Feature Action*'.
`[T](UMLSwitch.html)`
`[caseStructuredActivityNode](#caseStructuredActivityNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode))([StructuredActivityNode](../activities/mdstructuredactivities/StructuredActivityNode.html) object)`
Returns the result of interpreting the object as an instance of '*Structured Activity Node*'.
`[T](UMLSwitch.html)`
`[caseStructuredClassifier](#caseStructuredClassifier(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier))([StructuredClassifier](../compositestructures/mdinternalstructures/StructuredClassifier.html) object)`
Returns the result of interpreting the object as an instance of '*Structured Classifier*'.
`[T](UMLSwitch.html)`
`[caseSubstitution](#caseSubstitution(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Substitution))([Substitution](../classes/mddependencies/Substitution.html) object)`
Returns the result of interpreting the object as an instance of '*Substitution*'.
`[T](UMLSwitch.html)`
`[caseTemplateableElement](#caseTemplateableElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateableElement))([TemplateableElement](../auxiliaryconstructs/mdtemplates/TemplateableElement.html) object)`
Returns the result of interpreting the object as an instance of '*Templateable Element*'.
`[T](UMLSwitch.html)`
`[caseTemplateBinding](#caseTemplateBinding(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding))([TemplateBinding](../auxiliaryconstructs/mdtemplates/TemplateBinding.html) object)`
Returns the result of interpreting the object as an instance of '*Template Binding*'.
`[T](UMLSwitch.html)`
`[caseTemplateParameter](#caseTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))([TemplateParameter](../auxiliaryconstructs/mdtemplates/TemplateParameter.html) object)`
Returns the result of interpreting the object as an instance of '*Template Parameter*'.
`[T](UMLSwitch.html)`
`[caseTemplateParameterSubstitution](#caseTemplateParameterSubstitution(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution))([TemplateParameterSubstitution](../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html) object)`
Returns the result of interpreting the object as an instance of '*Template Parameter Substitution*'.
`[T](UMLSwitch.html)`
`[caseTemplateSignature](#caseTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature))([TemplateSignature](../auxiliaryconstructs/mdtemplates/TemplateSignature.html) object)`
Returns the result of interpreting the object as an instance of '*Template Signature*'.
`[T](UMLSwitch.html)`
`[caseTestIdentityAction](#caseTestIdentityAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction))([TestIdentityAction](../actions/mdintermediateactions/TestIdentityAction.html) object)`
Returns the result of interpreting the object as an instance of '*Test Identity Action*'.
`[T](UMLSwitch.html)`
`[caseTimeConstraint](#caseTimeConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint))([TimeConstraint](../commonbehaviors/mdsimpletime/TimeConstraint.html) object)`
Returns the result of interpreting the object as an instance of '*Time Constraint*'.
`[T](UMLSwitch.html)`
`[caseTimeEvent](#caseTimeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.TimeEvent))([TimeEvent](../commonbehaviors/mdcommunications/TimeEvent.html) object)`
Returns the result of interpreting the object as an instance of '*Time Event*'.
`[T](UMLSwitch.html)`
`[caseTimeExpression](#caseTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression))([TimeExpression](../commonbehaviors/mdsimpletime/TimeExpression.html) object)`
Returns the result of interpreting the object as an instance of '*Time Expression*'.
`[T](UMLSwitch.html)`
`[caseTimeInterval](#caseTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval))([TimeInterval](../commonbehaviors/mdsimpletime/TimeInterval.html) object)`
Returns the result of interpreting the object as an instance of '*Time Interval*'.
`[T](UMLSwitch.html)`
`[caseTimeObservation](#caseTimeObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeObservation))([TimeObservation](../commonbehaviors/mdsimpletime/TimeObservation.html) object)`
Returns the result of interpreting the object as an instance of '*Time Observation*'.
`[T](UMLSwitch.html)`
`[caseTransition](#caseTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))([Transition](../statemachines/mdbehaviorstatemachines/Transition.html) object)`
Returns the result of interpreting the object as an instance of '*Transition*'.
`[T](UMLSwitch.html)`
`[caseTrigger](#caseTrigger(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger))([Trigger](../commonbehaviors/mdcommunications/Trigger.html) object)`
Returns the result of interpreting the object as an instance of '*Trigger*'.
`[T](UMLSwitch.html)`
`[caseType](#caseType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([Type](../classes/mdkernel/Type.html) object)`
Returns the result of interpreting the object as an instance of '*Type*'.
`[T](UMLSwitch.html)`
`[caseTypedElement](#caseTypedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement))([TypedElement](../classes/mdkernel/TypedElement.html) object)`
Returns the result of interpreting the object as an instance of '*Typed Element*'.
`[T](UMLSwitch.html)`
`[caseUnmarshallAction](#caseUnmarshallAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction))([UnmarshallAction](../actions/mdcompleteactions/UnmarshallAction.html) object)`
Returns the result of interpreting the object as an instance of '*Unmarshall Action*'.
`[T](UMLSwitch.html)`
`[caseUsage](#caseUsage(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Usage))([Usage](../classes/mddependencies/Usage.html) object)`
Returns the result of interpreting the object as an instance of '*Usage*'.
`[T](UMLSwitch.html)`
`[caseUseCase](#caseUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase))([UseCase](../mdusecases/UseCase.html) object)`
Returns the result of interpreting the object as an instance of '*Use Case*'.
`[T](UMLSwitch.html)`
`[caseValuePin](#caseValuePin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin))([ValuePin](../actions/mdbasicactions/ValuePin.html) object)`
Returns the result of interpreting the object as an instance of '*Value Pin*'.
`[T](UMLSwitch.html)`
`[caseValueSpecification](#caseValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](../classes/mdkernel/ValueSpecification.html) object)`
Returns the result of interpreting the object as an instance of '*Value Specification*'.
`[T](UMLSwitch.html)`
`[caseValueSpecificationAction](#caseValueSpecificationAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction))([ValueSpecificationAction](../actions/mdintermediateactions/ValueSpecificationAction.html) object)`
Returns the result of interpreting the object as an instance of '*Value Specification Action*'.
`[T](UMLSwitch.html)`
`[caseVariable](#caseVariable(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Variable))([Variable](../activities/mdstructuredactivities/Variable.html) object)`
Returns the result of interpreting the object as an instance of '*Variable*'.
`[T](UMLSwitch.html)`
`[caseVariableAction](#caseVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.VariableAction))([VariableAction](../actions/mdstructuredactions/VariableAction.html) object)`
Returns the result of interpreting the object as an instance of '*Variable Action*'.
`[T](UMLSwitch.html)`
`[caseVertex](#caseVertex(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex))([Vertex](../statemachines/mdbehaviorstatemachines/Vertex.html) object)`
Returns the result of interpreting the object as an instance of '*Vertex*'.
`[T](UMLSwitch.html)`
`[caseWriteLinkAction](#caseWriteLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteLinkAction))([WriteLinkAction](../actions/mdintermediateactions/WriteLinkAction.html) object)`
Returns the result of interpreting the object as an instance of '*Write Link Action*'.
`[T](UMLSwitch.html)`
`[caseWriteStructuralFeatureAction](#caseWriteStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction))([WriteStructuralFeatureAction](../actions/mdintermediateactions/WriteStructuralFeatureAction.html) object)`
Returns the result of interpreting the object as an instance of '*Write Structural Feature Action*'.
`[T](UMLSwitch.html)`
`[caseWriteVariableAction](#caseWriteVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.WriteVariableAction))([WriteVariableAction](../actions/mdstructuredactions/WriteVariableAction.html) object)`
Returns the result of interpreting the object as an instance of '*Write Variable Action*'.
`[T](UMLSwitch.html)`
`[defaultCase](#defaultCase(org.eclipse.emf.ecore.EObject))(org.eclipse.emf.ecore.EObject object)`
Returns the result of interpreting the object as an instance of '*EObject*'.
`protected [T](UMLSwitch.html)`
`[doSwitch](#doSwitch(int,org.eclipse.emf.ecore.EObject))(int classifierID,
 org.eclipse.emf.ecore.EObject theEObject)`
Calls `caseXXX` for each class of the model until one returns a non null result; it yields that result.
`protected [T](UMLSwitch.html)`
`[doSwitch](#doSwitch(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EObject))(org.eclipse.emf.ecore.EClass theEClass,
 org.eclipse.emf.ecore.EObject theEObject)`
Calls `caseXXX` for each class of the model until one returns a non null result; it yields that result.
`[T](UMLSwitch.html)`
`[doSwitch](#doSwitch(org.eclipse.emf.ecore.EObject))(org.eclipse.emf.ecore.EObject theEObject)`
Calls `caseXXX` for each class of the model until one returns a non null result; it yields that result.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
modelPackage
protected static [UMLPackage](../metadata/UMLPackage.html) modelPackage
The cached model package
 begin-user-doc 
 end-user-doc
Generated:
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
UMLSwitch
public UMLSwitch()
Creates an instance of the switch.
 begin-user-doc 
 end-user-doc
Generated:
 ============ METHOD DETAIL ========== 
Method Details
doSwitch
public [T](UMLSwitch.html) doSwitch(org.eclipse.emf.ecore.EObject theEObject)
Calls `caseXXX` for each class of the model until one returns a non null result; it yields that result.
 begin-user-doc 
 end-user-doc
Returns:
the first non-null result returned by a `caseXXX` call.
Generated:
doSwitch
protected [T](UMLSwitch.html) doSwitch(org.eclipse.emf.ecore.EClass theEClass,
 org.eclipse.emf.ecore.EObject theEObject)
Calls `caseXXX` for each class of the model until one returns a non null result; it yields that result.
 begin-user-doc 
 end-user-doc
Returns:
the first non-null result returned by a `caseXXX` call.
Generated:
doSwitch
protected [T](UMLSwitch.html) doSwitch(int classifierID,
 org.eclipse.emf.ecore.EObject theEObject)
Calls `caseXXX` for each class of the model until one returns a non null result; it yields that result.
 begin-user-doc 
 end-user-doc
Returns:
the first non-null result returned by a `caseXXX` call.
Generated:
caseSendSignalAction
public [T](UMLSwitch.html) caseSendSignalAction([SendSignalAction](../actions/mdbasicactions/SendSignalAction.html) object)
Returns the result of interpreting the object as an instance of '*Send Signal Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Send Signal Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInvocationAction
public [T](UMLSwitch.html) caseInvocationAction([InvocationAction](../actions/mdbasicactions/InvocationAction.html) object)
Returns the result of interpreting the object as an instance of '*Invocation Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Invocation Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseAction
public [T](UMLSwitch.html) caseAction([Action](../actions/mdbasicactions/Action.html) object)
Returns the result of interpreting the object as an instance of '*Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseExecutableNode
public [T](UMLSwitch.html) caseExecutableNode([ExecutableNode](../activities/mdstructuredactivities/ExecutableNode.html) object)
Returns the result of interpreting the object as an instance of '*Executable Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Executable Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseActivityNode
public [T](UMLSwitch.html) caseActivityNode([ActivityNode](../activities/mdfundamentalactivities/ActivityNode.html) object)
Returns the result of interpreting the object as an instance of '*Activity Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Activity Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseRedefinableElement
public [T](UMLSwitch.html) caseRedefinableElement([RedefinableElement](../classes/mdkernel/RedefinableElement.html) object)
Returns the result of interpreting the object as an instance of '*Redefinable Element*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Redefinable Element*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseNamedElement
public [T](UMLSwitch.html) caseNamedElement([NamedElement](../classes/mdkernel/NamedElement.html) object)
Returns the result of interpreting the object as an instance of '*Named Element*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Named Element*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseElement
public [T](UMLSwitch.html) caseElement([Element](../classes/mdkernel/Element.html) object)
Returns the result of interpreting the object as an instance of '*Element*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Element*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseComment
public [T](UMLSwitch.html) caseComment([Comment](../classes/mdkernel/Comment.html) object)
Returns the result of interpreting the object as an instance of '*Comment*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Comment*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInstanceSpecification
public [T](UMLSwitch.html) caseInstanceSpecification([InstanceSpecification](../classes/mdkernel/InstanceSpecification.html) object)
Returns the result of interpreting the object as an instance of '*Instance Specification*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Instance Specification*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
casePackageableElement
public [T](UMLSwitch.html) casePackageableElement([PackageableElement](../classes/mdkernel/PackageableElement.html) object)
Returns the result of interpreting the object as an instance of '*Packageable Element*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Packageable Element*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseParameterableElement
public [T](UMLSwitch.html) caseParameterableElement([ParameterableElement](../auxiliaryconstructs/mdtemplates/ParameterableElement.html) object)
Returns the result of interpreting the object as an instance of '*Parameterable Element*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Parameterable Element*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTemplateParameter
public [T](UMLSwitch.html) caseTemplateParameter([TemplateParameter](../auxiliaryconstructs/mdtemplates/TemplateParameter.html) object)
Returns the result of interpreting the object as an instance of '*Template Parameter*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Template Parameter*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTemplateSignature
public [T](UMLSwitch.html) caseTemplateSignature([TemplateSignature](../auxiliaryconstructs/mdtemplates/TemplateSignature.html) object)
Returns the result of interpreting the object as an instance of '*Template Signature*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Template Signature*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTemplateableElement
public [T](UMLSwitch.html) caseTemplateableElement([TemplateableElement](../auxiliaryconstructs/mdtemplates/TemplateableElement.html) object)
Returns the result of interpreting the object as an instance of '*Templateable Element*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Templateable Element*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTemplateBinding
public [T](UMLSwitch.html) caseTemplateBinding([TemplateBinding](../auxiliaryconstructs/mdtemplates/TemplateBinding.html) object)
Returns the result of interpreting the object as an instance of '*Template Binding*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Template Binding*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDirectedRelationship
public [T](UMLSwitch.html) caseDirectedRelationship([DirectedRelationship](../classes/mdkernel/DirectedRelationship.html) object)
Returns the result of interpreting the object as an instance of '*Directed Relationship*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Directed Relationship*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseRelationship
public [T](UMLSwitch.html) caseRelationship([Relationship](../classes/mdkernel/Relationship.html) object)
Returns the result of interpreting the object as an instance of '*Relationship*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Relationship*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInformationFlow
public [T](UMLSwitch.html) caseInformationFlow([InformationFlow](../auxiliaryconstructs/mdinformationflows/InformationFlow.html) object)
Returns the result of interpreting the object as an instance of '*Information Flow*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Information Flow*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseClassifier
public [T](UMLSwitch.html) caseClassifier([Classifier](../classes/mdkernel/Classifier.html) object)
Returns the result of interpreting the object as an instance of '*Classifier*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Classifier*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseNamespace
public [T](UMLSwitch.html) caseNamespace([Namespace](../classes/mdkernel/Namespace.html) object)
Returns the result of interpreting the object as an instance of '*Namespace*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Namespace*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseElementImport
public [T](UMLSwitch.html) caseElementImport([ElementImport](../classes/mdkernel/ElementImport.html) object)
Returns the result of interpreting the object as an instance of '*Element Import*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Element Import*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseProfile
public [T](UMLSwitch.html) caseProfile([Profile](../mdprofiles/Profile.html) object)
Returns the result of interpreting the object as an instance of '*Profile*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Profile*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
casePackage
public [T](UMLSwitch.html) casePackage([Package](../classes/mdkernel/Package.html) object)
Returns the result of interpreting the object as an instance of '*Package*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Package*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseStereotype
public [T](UMLSwitch.html) caseStereotype([Stereotype](../mdprofiles/Stereotype.html) object)
Returns the result of interpreting the object as an instance of '*Stereotype*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Stereotype*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseClass
public [T](UMLSwitch.html) caseClass([Class](../classes/mdkernel/Class.html) object)
Returns the result of interpreting the object as an instance of '*Class*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Class*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseBehavioredClassifier
public [T](UMLSwitch.html) caseBehavioredClassifier([BehavioredClassifier](../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) object)
Returns the result of interpreting the object as an instance of '*Behaviored Classifier*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Behaviored Classifier*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseBehavior
public [T](UMLSwitch.html) caseBehavior([Behavior](../commonbehaviors/mdbasicbehaviors/Behavior.html) object)
Returns the result of interpreting the object as an instance of '*Behavior*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Behavior*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseParameter
public [T](UMLSwitch.html) caseParameter([Parameter](../classes/mdkernel/Parameter.html) object)
Returns the result of interpreting the object as an instance of '*Parameter*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Parameter*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseMultiplicityElement
public [T](UMLSwitch.html) caseMultiplicityElement([MultiplicityElement](../classes/mdkernel/MultiplicityElement.html) object)
Returns the result of interpreting the object as an instance of '*Multiplicity Element*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Multiplicity Element*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseValueSpecification
public [T](UMLSwitch.html) caseValueSpecification([ValueSpecification](../classes/mdkernel/ValueSpecification.html) object)
Returns the result of interpreting the object as an instance of '*Value Specification*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Value Specification*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTypedElement
public [T](UMLSwitch.html) caseTypedElement([TypedElement](../classes/mdkernel/TypedElement.html) object)
Returns the result of interpreting the object as an instance of '*Typed Element*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Typed Element*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseType
public [T](UMLSwitch.html) caseType([Type](../classes/mdkernel/Type.html) object)
Returns the result of interpreting the object as an instance of '*Type*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Type*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseAssociation
public [T](UMLSwitch.html) caseAssociation([Association](../classes/mdkernel/Association.html) object)
Returns the result of interpreting the object as an instance of '*Association*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Association*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseProperty
public [T](UMLSwitch.html) caseProperty([Property](../classes/mdkernel/Property.html) object)
Returns the result of interpreting the object as an instance of '*Property*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Property*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseStructuralFeature
public [T](UMLSwitch.html) caseStructuralFeature([StructuralFeature](../classes/mdkernel/StructuralFeature.html) object)
Returns the result of interpreting the object as an instance of '*Structural Feature*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Structural Feature*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseFeature
public [T](UMLSwitch.html) caseFeature([Feature](../classes/mdkernel/Feature.html) object)
Returns the result of interpreting the object as an instance of '*Feature*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Feature*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseSlot
public [T](UMLSwitch.html) caseSlot([Slot](../classes/mdkernel/Slot.html) object)
Returns the result of interpreting the object as an instance of '*Slot*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Slot*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseStructuralFeatureAction
public [T](UMLSwitch.html) caseStructuralFeatureAction([StructuralFeatureAction](../actions/mdintermediateactions/StructuralFeatureAction.html) object)
Returns the result of interpreting the object as an instance of '*Structural Feature Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Structural Feature Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInputPin
public [T](UMLSwitch.html) caseInputPin([InputPin](../actions/mdbasicactions/InputPin.html) object)
Returns the result of interpreting the object as an instance of '*Input Pin*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Input Pin*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
casePin
public [T](UMLSwitch.html) casePin([Pin](../actions/mdbasicactions/Pin.html) object)
Returns the result of interpreting the object as an instance of '*Pin*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Pin*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseObjectNode
public [T](UMLSwitch.html) caseObjectNode([ObjectNode](../activities/mdbasicactivities/ObjectNode.html) object)
Returns the result of interpreting the object as an instance of '*Object Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Object Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseState
public [T](UMLSwitch.html) caseState([State](../statemachines/mdbehaviorstatemachines/State.html) object)
Returns the result of interpreting the object as an instance of '*State*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*State*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseVertex
public [T](UMLSwitch.html) caseVertex([Vertex](../statemachines/mdbehaviorstatemachines/Vertex.html) object)
Returns the result of interpreting the object as an instance of '*Vertex*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Vertex*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseRegion
public [T](UMLSwitch.html) caseRegion([Region](../statemachines/mdbehaviorstatemachines/Region.html) object)
Returns the result of interpreting the object as an instance of '*Region*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Region*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseStateMachine
public [T](UMLSwitch.html) caseStateMachine([StateMachine](../statemachines/mdbehaviorstatemachines/StateMachine.html) object)
Returns the result of interpreting the object as an instance of '*State Machine*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*State Machine*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
casePseudostate
public [T](UMLSwitch.html) casePseudostate([Pseudostate](../statemachines/mdbehaviorstatemachines/Pseudostate.html) object)
Returns the result of interpreting the object as an instance of '*Pseudostate*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Pseudostate*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseConnectionPointReference
public [T](UMLSwitch.html) caseConnectionPointReference([ConnectionPointReference](../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html) object)
Returns the result of interpreting the object as an instance of '*Connection Point Reference*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Connection Point Reference*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTransition
public [T](UMLSwitch.html) caseTransition([Transition](../statemachines/mdbehaviorstatemachines/Transition.html) object)
Returns the result of interpreting the object as an instance of '*Transition*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Transition*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseConstraint
public [T](UMLSwitch.html) caseConstraint([Constraint](../classes/mdkernel/Constraint.html) object)
Returns the result of interpreting the object as an instance of '*Constraint*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Constraint*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseOperation
public [T](UMLSwitch.html) caseOperation([Operation](../classes/mdkernel/Operation.html) object)
Returns the result of interpreting the object as an instance of '*Operation*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Operation*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseBehavioralFeature
public [T](UMLSwitch.html) caseBehavioralFeature([BehavioralFeature](../classes/mdkernel/BehavioralFeature.html) object)
Returns the result of interpreting the object as an instance of '*Behavioral Feature*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Behavioral Feature*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseParameterSet
public [T](UMLSwitch.html) caseParameterSet([ParameterSet](../activities/mdcompleteactivities/ParameterSet.html) object)
Returns the result of interpreting the object as an instance of '*Parameter Set*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Parameter Set*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDataType
public [T](UMLSwitch.html) caseDataType([DataType](../classes/mdkernel/DataType.html) object)
Returns the result of interpreting the object as an instance of '*Data Type*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Data Type*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInterface
public [T](UMLSwitch.html) caseInterface([Interface](../classes/mdinterfaces/Interface.html) object)
Returns the result of interpreting the object as an instance of '*Interface*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Interface*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseReception
public [T](UMLSwitch.html) caseReception([Reception](../commonbehaviors/mdcommunications/Reception.html) object)
Returns the result of interpreting the object as an instance of '*Reception*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Reception*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseSignal
public [T](UMLSwitch.html) caseSignal([Signal](../commonbehaviors/mdcommunications/Signal.html) object)
Returns the result of interpreting the object as an instance of '*Signal*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Signal*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseBroadcastSignalAction
public [T](UMLSwitch.html) caseBroadcastSignalAction([BroadcastSignalAction](../actions/mdintermediateactions/BroadcastSignalAction.html) object)
Returns the result of interpreting the object as an instance of '*Broadcast Signal Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Broadcast Signal Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseSignalEvent
public [T](UMLSwitch.html) caseSignalEvent([SignalEvent](../commonbehaviors/mdcommunications/SignalEvent.html) object)
Returns the result of interpreting the object as an instance of '*Signal Event*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Signal Event*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseMessageEvent
public [T](UMLSwitch.html) caseMessageEvent([MessageEvent](../commonbehaviors/mdcommunications/MessageEvent.html) object)
Returns the result of interpreting the object as an instance of '*Message Event*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Message Event*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseEvent
public [T](UMLSwitch.html) caseEvent([Event](../commonbehaviors/mdcommunications/Event.html) object)
Returns the result of interpreting the object as an instance of '*Event*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Event*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTrigger
public [T](UMLSwitch.html) caseTrigger([Trigger](../commonbehaviors/mdcommunications/Trigger.html) object)
Returns the result of interpreting the object as an instance of '*Trigger*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Trigger*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
casePort
public [T](UMLSwitch.html) casePort([Port](../compositestructures/mdports/Port.html) object)
Returns the result of interpreting the object as an instance of '*Port*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Port*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseProtocolStateMachine
public [T](UMLSwitch.html) caseProtocolStateMachine([ProtocolStateMachine](../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html) object)
Returns the result of interpreting the object as an instance of '*Protocol State Machine*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Protocol State Machine*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseProtocolConformance
public [T](UMLSwitch.html) caseProtocolConformance([ProtocolConformance](../statemachines/mdprotocolstatemachines/ProtocolConformance.html) object)
Returns the result of interpreting the object as an instance of '*Protocol Conformance*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Protocol Conformance*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseEncapsulatedClassifier
public [T](UMLSwitch.html) caseEncapsulatedClassifier([EncapsulatedClassifier](../compositestructures/mdports/EncapsulatedClassifier.html) object)
Returns the result of interpreting the object as an instance of '*Encapsulated Classifier*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Encapsulated Classifier*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseStructuredClassifier
public [T](UMLSwitch.html) caseStructuredClassifier([StructuredClassifier](../compositestructures/mdinternalstructures/StructuredClassifier.html) object)
Returns the result of interpreting the object as an instance of '*Structured Classifier*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Structured Classifier*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseConnector
public [T](UMLSwitch.html) caseConnector([Connector](../compositestructures/mdinternalstructures/Connector.html) object)
Returns the result of interpreting the object as an instance of '*Connector*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Connector*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseConnectorEnd
public [T](UMLSwitch.html) caseConnectorEnd([ConnectorEnd](../compositestructures/mdinternalstructures/ConnectorEnd.html) object)
Returns the result of interpreting the object as an instance of '*Connector End*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Connector End*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseConnectableElement
public [T](UMLSwitch.html) caseConnectableElement([ConnectableElement](../compositestructures/mdinternalstructures/ConnectableElement.html) object)
Returns the result of interpreting the object as an instance of '*Connectable Element*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Connectable Element*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseConnectableElementTemplateParameter
public [T](UMLSwitch.html) caseConnectableElementTemplateParameter([ConnectableElementTemplateParameter](../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html) object)
Returns the result of interpreting the object as an instance of '*Connectable Element Template Parameter*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Connectable Element Template Parameter*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseCollaboration
public [T](UMLSwitch.html) caseCollaboration([Collaboration](../compositestructures/mdcollaborations/Collaboration.html) object)
Returns the result of interpreting the object as an instance of '*Collaboration*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Collaboration*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseCollaborationUse
public [T](UMLSwitch.html) caseCollaborationUse([CollaborationUse](../compositestructures/mdcollaborations/CollaborationUse.html) object)
Returns the result of interpreting the object as an instance of '*Collaboration Use*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Collaboration Use*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDependency
public [T](UMLSwitch.html) caseDependency([Dependency](../classes/mddependencies/Dependency.html) object)
Returns the result of interpreting the object as an instance of '*Dependency*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Dependency*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseLifeline
public [T](UMLSwitch.html) caseLifeline([Lifeline](../interactions/mdbasicinteractions/Lifeline.html) object)
Returns the result of interpreting the object as an instance of '*Lifeline*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Lifeline*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInteractionFragment
public [T](UMLSwitch.html) caseInteractionFragment([InteractionFragment](../interactions/mdbasicinteractions/InteractionFragment.html) object)
Returns the result of interpreting the object as an instance of '*Interaction Fragment*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Interaction Fragment*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInteraction
public [T](UMLSwitch.html) caseInteraction([Interaction](../interactions/mdbasicinteractions/Interaction.html) object)
Returns the result of interpreting the object as an instance of '*Interaction*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Interaction*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseGate
public [T](UMLSwitch.html) caseGate([Gate](../interactions/mdfragments/Gate.html) object)
Returns the result of interpreting the object as an instance of '*Gate*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Gate*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseMessageEnd
public [T](UMLSwitch.html) caseMessageEnd([MessageEnd](../interactions/mdbasicinteractions/MessageEnd.html) object)
Returns the result of interpreting the object as an instance of '*Message End*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Message End*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseMessage
public [T](UMLSwitch.html) caseMessage([Message](../interactions/mdbasicinteractions/Message.html) object)
Returns the result of interpreting the object as an instance of '*Message*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Message*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInteractionUse
public [T](UMLSwitch.html) caseInteractionUse([InteractionUse](../interactions/mdfragments/InteractionUse.html) object)
Returns the result of interpreting the object as an instance of '*Interaction Use*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Interaction Use*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseCombinedFragment
public [T](UMLSwitch.html) caseCombinedFragment([CombinedFragment](../interactions/mdfragments/CombinedFragment.html) object)
Returns the result of interpreting the object as an instance of '*Combined Fragment*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Combined Fragment*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInteractionOperand
public [T](UMLSwitch.html) caseInteractionOperand([InteractionOperand](../interactions/mdfragments/InteractionOperand.html) object)
Returns the result of interpreting the object as an instance of '*Interaction Operand*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Interaction Operand*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInteractionConstraint
public [T](UMLSwitch.html) caseInteractionConstraint([InteractionConstraint](../interactions/mdfragments/InteractionConstraint.html) object)
Returns the result of interpreting the object as an instance of '*Interaction Constraint*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Interaction Constraint*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseGeneralOrdering
public [T](UMLSwitch.html) caseGeneralOrdering([GeneralOrdering](../interactions/mdbasicinteractions/GeneralOrdering.html) object)
Returns the result of interpreting the object as an instance of '*General Ordering*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*General Ordering*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseOccurrenceSpecification
public [T](UMLSwitch.html) caseOccurrenceSpecification([OccurrenceSpecification](../interactions/mdbasicinteractions/OccurrenceSpecification.html) object)
Returns the result of interpreting the object as an instance of '*Occurrence Specification*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Occurrence Specification*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseExecutionSpecification
public [T](UMLSwitch.html) caseExecutionSpecification([ExecutionSpecification](../interactions/mdbasicinteractions/ExecutionSpecification.html) object)
Returns the result of interpreting the object as an instance of '*Execution Specification*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Execution Specification*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseExecutionOccurrenceSpecification
public [T](UMLSwitch.html) caseExecutionOccurrenceSpecification([ExecutionOccurrenceSpecification](../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html) object)
Returns the result of interpreting the object as an instance of '*Execution Occurrence Specification*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Execution Occurrence Specification*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
casePartDecomposition
public [T](UMLSwitch.html) casePartDecomposition([PartDecomposition](../interactions/mdfragments/PartDecomposition.html) object)
Returns the result of interpreting the object as an instance of '*Part Decomposition*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Part Decomposition*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseStateInvariant
public [T](UMLSwitch.html) caseStateInvariant([StateInvariant](../interactions/mdbasicinteractions/StateInvariant.html) object)
Returns the result of interpreting the object as an instance of '*State Invariant*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*State Invariant*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseReplyAction
public [T](UMLSwitch.html) caseReplyAction([ReplyAction](../actions/mdcompleteactions/ReplyAction.html) object)
Returns the result of interpreting the object as an instance of '*Reply Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Reply Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseAcceptEventAction
public [T](UMLSwitch.html) caseAcceptEventAction([AcceptEventAction](../actions/mdcompleteactions/AcceptEventAction.html) object)
Returns the result of interpreting the object as an instance of '*Accept Event Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Accept Event Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseOutputPin
public [T](UMLSwitch.html) caseOutputPin([OutputPin](../actions/mdbasicactions/OutputPin.html) object)
Returns the result of interpreting the object as an instance of '*Output Pin*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Output Pin*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseClause
public [T](UMLSwitch.html) caseClause([Clause](../activities/mdstructuredactivities/Clause.html) object)
Returns the result of interpreting the object as an instance of '*Clause*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Clause*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseConditionalNode
public [T](UMLSwitch.html) caseConditionalNode([ConditionalNode](../activities/mdstructuredactivities/ConditionalNode.html) object)
Returns the result of interpreting the object as an instance of '*Conditional Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Conditional Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseStructuredActivityNode
public [T](UMLSwitch.html) caseStructuredActivityNode([StructuredActivityNode](../activities/mdstructuredactivities/StructuredActivityNode.html) object)
Returns the result of interpreting the object as an instance of '*Structured Activity Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Structured Activity Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseActivityGroup
public [T](UMLSwitch.html) caseActivityGroup([ActivityGroup](../activities/mdfundamentalactivities/ActivityGroup.html) object)
Returns the result of interpreting the object as an instance of '*Activity Group*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Activity Group*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseActivityEdge
public [T](UMLSwitch.html) caseActivityEdge([ActivityEdge](../activities/mdbasicactivities/ActivityEdge.html) object)
Returns the result of interpreting the object as an instance of '*Activity Edge*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Activity Edge*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseActivity
public [T](UMLSwitch.html) caseActivity([Activity](../activities/mdfundamentalactivities/Activity.html) object)
Returns the result of interpreting the object as an instance of '*Activity*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Activity*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseActivityPartition
public [T](UMLSwitch.html) caseActivityPartition([ActivityPartition](../activities/mdintermediateactivities/ActivityPartition.html) object)
Returns the result of interpreting the object as an instance of '*Activity Partition*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Activity Partition*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseVariable
public [T](UMLSwitch.html) caseVariable([Variable](../activities/mdstructuredactivities/Variable.html) object)
Returns the result of interpreting the object as an instance of '*Variable*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Variable*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseVariableAction
public [T](UMLSwitch.html) caseVariableAction([VariableAction](../actions/mdstructuredactions/VariableAction.html) object)
Returns the result of interpreting the object as an instance of '*Variable Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Variable Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInterruptibleActivityRegion
public [T](UMLSwitch.html) caseInterruptibleActivityRegion([InterruptibleActivityRegion](../activities/mdcompleteactivities/InterruptibleActivityRegion.html) object)
Returns the result of interpreting the object as an instance of '*Interruptible Activity Region*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Interruptible Activity Region*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseLoopNode
public [T](UMLSwitch.html) caseLoopNode([LoopNode](../activities/mdstructuredactivities/LoopNode.html) object)
Returns the result of interpreting the object as an instance of '*Loop Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Loop Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseOpaqueAction
public [T](UMLSwitch.html) caseOpaqueAction([OpaqueAction](../actions/mdbasicactions/OpaqueAction.html) object)
Returns the result of interpreting the object as an instance of '*Opaque Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Opaque Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseCallAction
public [T](UMLSwitch.html) caseCallAction([CallAction](../actions/mdbasicactions/CallAction.html) object)
Returns the result of interpreting the object as an instance of '*Call Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Call Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseClearStructuralFeatureAction
public [T](UMLSwitch.html) caseClearStructuralFeatureAction([ClearStructuralFeatureAction](../actions/mdintermediateactions/ClearStructuralFeatureAction.html) object)
Returns the result of interpreting the object as an instance of '*Clear Structural Feature Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Clear Structural Feature Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseCreateLinkObjectAction
public [T](UMLSwitch.html) caseCreateLinkObjectAction([CreateLinkObjectAction](../actions/mdcompleteactions/CreateLinkObjectAction.html) object)
Returns the result of interpreting the object as an instance of '*Create Link Object Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Create Link Object Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseCreateLinkAction
public [T](UMLSwitch.html) caseCreateLinkAction([CreateLinkAction](../actions/mdintermediateactions/CreateLinkAction.html) object)
Returns the result of interpreting the object as an instance of '*Create Link Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Create Link Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseWriteLinkAction
public [T](UMLSwitch.html) caseWriteLinkAction([WriteLinkAction](../actions/mdintermediateactions/WriteLinkAction.html) object)
Returns the result of interpreting the object as an instance of '*Write Link Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Write Link Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseLinkAction
public [T](UMLSwitch.html) caseLinkAction([LinkAction](../actions/mdintermediateactions/LinkAction.html) object)
Returns the result of interpreting the object as an instance of '*Link Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Link Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseLinkEndData
public [T](UMLSwitch.html) caseLinkEndData([LinkEndData](../actions/mdintermediateactions/LinkEndData.html) object)
Returns the result of interpreting the object as an instance of '*Link End Data*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Link End Data*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseQualifierValue
public [T](UMLSwitch.html) caseQualifierValue([QualifierValue](../actions/mdcompleteactions/QualifierValue.html) object)
Returns the result of interpreting the object as an instance of '*Qualifier Value*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Qualifier Value*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseLinkEndCreationData
public [T](UMLSwitch.html) caseLinkEndCreationData([LinkEndCreationData](../actions/mdintermediateactions/LinkEndCreationData.html) object)
Returns the result of interpreting the object as an instance of '*Link End Creation Data*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Link End Creation Data*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseCreateObjectAction
public [T](UMLSwitch.html) caseCreateObjectAction([CreateObjectAction](../actions/mdintermediateactions/CreateObjectAction.html) object)
Returns the result of interpreting the object as an instance of '*Create Object Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Create Object Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseReadExtentAction
public [T](UMLSwitch.html) caseReadExtentAction([ReadExtentAction](../actions/mdcompleteactions/ReadExtentAction.html) object)
Returns the result of interpreting the object as an instance of '*Read Extent Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Read Extent Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseReadIsClassifiedObjectAction
public [T](UMLSwitch.html) caseReadIsClassifiedObjectAction([ReadIsClassifiedObjectAction](../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html) object)
Returns the result of interpreting the object as an instance of '*Read Is Classified Object Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Read Is Classified Object Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseReadLinkAction
public [T](UMLSwitch.html) caseReadLinkAction([ReadLinkAction](../actions/mdintermediateactions/ReadLinkAction.html) object)
Returns the result of interpreting the object as an instance of '*Read Link Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Read Link Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseReadLinkObjectEndAction
public [T](UMLSwitch.html) caseReadLinkObjectEndAction([ReadLinkObjectEndAction](../actions/mdcompleteactions/ReadLinkObjectEndAction.html) object)
Returns the result of interpreting the object as an instance of '*Read Link Object End Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Read Link Object End Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseReadLinkObjectEndQualifierAction
public [T](UMLSwitch.html) caseReadLinkObjectEndQualifierAction([ReadLinkObjectEndQualifierAction](../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html) object)
Returns the result of interpreting the object as an instance of '*Read Link Object End Qualifier Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Read Link Object End Qualifier Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseReadSelfAction
public [T](UMLSwitch.html) caseReadSelfAction([ReadSelfAction](../actions/mdintermediateactions/ReadSelfAction.html) object)
Returns the result of interpreting the object as an instance of '*Read Self Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Read Self Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseReadStructuralFeatureAction
public [T](UMLSwitch.html) caseReadStructuralFeatureAction([ReadStructuralFeatureAction](../actions/mdintermediateactions/ReadStructuralFeatureAction.html) object)
Returns the result of interpreting the object as an instance of '*Read Structural Feature Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Read Structural Feature Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseReadVariableAction
public [T](UMLSwitch.html) caseReadVariableAction([ReadVariableAction](../actions/mdstructuredactions/ReadVariableAction.html) object)
Returns the result of interpreting the object as an instance of '*Read Variable Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Read Variable Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseReduceAction
public [T](UMLSwitch.html) caseReduceAction([ReduceAction](../actions/mdcompleteactions/ReduceAction.html) object)
Returns the result of interpreting the object as an instance of '*Reduce Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Reduce Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTestIdentityAction
public [T](UMLSwitch.html) caseTestIdentityAction([TestIdentityAction](../actions/mdintermediateactions/TestIdentityAction.html) object)
Returns the result of interpreting the object as an instance of '*Test Identity Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Test Identity Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseUnmarshallAction
public [T](UMLSwitch.html) caseUnmarshallAction([UnmarshallAction](../actions/mdcompleteactions/UnmarshallAction.html) object)
Returns the result of interpreting the object as an instance of '*Unmarshall Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Unmarshall Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseValueSpecificationAction
public [T](UMLSwitch.html) caseValueSpecificationAction([ValueSpecificationAction](../actions/mdintermediateactions/ValueSpecificationAction.html) object)
Returns the result of interpreting the object as an instance of '*Value Specification Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Value Specification Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseWriteStructuralFeatureAction
public [T](UMLSwitch.html) caseWriteStructuralFeatureAction([WriteStructuralFeatureAction](../actions/mdintermediateactions/WriteStructuralFeatureAction.html) object)
Returns the result of interpreting the object as an instance of '*Write Structural Feature Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Write Structural Feature Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseAcceptCallAction
public [T](UMLSwitch.html) caseAcceptCallAction([AcceptCallAction](../actions/mdcompleteactions/AcceptCallAction.html) object)
Returns the result of interpreting the object as an instance of '*Accept Call Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Accept Call Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInterfaceRealization
public [T](UMLSwitch.html) caseInterfaceRealization([InterfaceRealization](../classes/mdinterfaces/InterfaceRealization.html) object)
Returns the result of interpreting the object as an instance of '*Interface Realization*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Interface Realization*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseRealization
public [T](UMLSwitch.html) caseRealization([Realization](../classes/mddependencies/Realization.html) object)
Returns the result of interpreting the object as an instance of '*Realization*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Realization*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseAbstraction
public [T](UMLSwitch.html) caseAbstraction([Abstraction](../classes/mddependencies/Abstraction.html) object)
Returns the result of interpreting the object as an instance of '*Abstraction*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Abstraction*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseOpaqueExpression
public [T](UMLSwitch.html) caseOpaqueExpression([OpaqueExpression](../classes/mdkernel/OpaqueExpression.html) object)
Returns the result of interpreting the object as an instance of '*Opaque Expression*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Opaque Expression*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseComponent
public [T](UMLSwitch.html) caseComponent([Component](../components/mdbasiccomponents/Component.html) object)
Returns the result of interpreting the object as an instance of '*Component*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Component*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseComponentRealization
public [T](UMLSwitch.html) caseComponentRealization([ComponentRealization](../components/mdbasiccomponents/ComponentRealization.html) object)
Returns the result of interpreting the object as an instance of '*Component Realization*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Component Realization*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseOperationTemplateParameter
public [T](UMLSwitch.html) caseOperationTemplateParameter([OperationTemplateParameter](../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html) object)
Returns the result of interpreting the object as an instance of '*Operation Template Parameter*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Operation Template Parameter*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseCallEvent
public [T](UMLSwitch.html) caseCallEvent([CallEvent](../commonbehaviors/mdcommunications/CallEvent.html) object)
Returns the result of interpreting the object as an instance of '*Call Event*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Call Event*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseCallOperationAction
public [T](UMLSwitch.html) caseCallOperationAction([CallOperationAction](../actions/mdbasicactions/CallOperationAction.html) object)
Returns the result of interpreting the object as an instance of '*Call Operation Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Call Operation Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseArtifact
public [T](UMLSwitch.html) caseArtifact([Artifact](../deployments/mdartifacts/Artifact.html) object)
Returns the result of interpreting the object as an instance of '*Artifact*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Artifact*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDeployedArtifact
public [T](UMLSwitch.html) caseDeployedArtifact([DeployedArtifact](../deployments/mdnodes/DeployedArtifact.html) object)
Returns the result of interpreting the object as an instance of '*Deployed Artifact*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Deployed Artifact*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDeployment
public [T](UMLSwitch.html) caseDeployment([Deployment](../deployments/mdnodes/Deployment.html) object)
Returns the result of interpreting the object as an instance of '*Deployment*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Deployment*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDeploymentSpecification
public [T](UMLSwitch.html) caseDeploymentSpecification([DeploymentSpecification](../deployments/mdcomponentdeployments/DeploymentSpecification.html) object)
Returns the result of interpreting the object as an instance of '*Deployment Specification*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Deployment Specification*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDeploymentTarget
public [T](UMLSwitch.html) caseDeploymentTarget([DeploymentTarget](../deployments/mdnodes/DeploymentTarget.html) object)
Returns the result of interpreting the object as an instance of '*Deployment Target*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Deployment Target*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseManifestation
public [T](UMLSwitch.html) caseManifestation([Manifestation](../deployments/mdartifacts/Manifestation.html) object)
Returns the result of interpreting the object as an instance of '*Manifestation*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Manifestation*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseProtocolTransition
public [T](UMLSwitch.html) caseProtocolTransition([ProtocolTransition](../statemachines/mdprotocolstatemachines/ProtocolTransition.html) object)
Returns the result of interpreting the object as an instance of '*Protocol Transition*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Protocol Transition*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseExtend
public [T](UMLSwitch.html) caseExtend([Extend](../mdusecases/Extend.html) object)
Returns the result of interpreting the object as an instance of '*Extend*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Extend*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseUseCase
public [T](UMLSwitch.html) caseUseCase([UseCase](../mdusecases/UseCase.html) object)
Returns the result of interpreting the object as an instance of '*Use Case*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Use Case*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseExtensionPoint
public [T](UMLSwitch.html) caseExtensionPoint([ExtensionPoint](../mdusecases/ExtensionPoint.html) object)
Returns the result of interpreting the object as an instance of '*Extension Point*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Extension Point*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInclude
public [T](UMLSwitch.html) caseInclude([Include](../mdusecases/Include.html) object)
Returns the result of interpreting the object as an instance of '*Include*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Include*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseExceptionHandler
public [T](UMLSwitch.html) caseExceptionHandler([ExceptionHandler](../activities/mdextrastructuredactivities/ExceptionHandler.html) object)
Returns the result of interpreting the object as an instance of '*Exception Handler*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Exception Handler*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseLinkEndDestructionData
public [T](UMLSwitch.html) caseLinkEndDestructionData([LinkEndDestructionData](../actions/mdintermediateactions/LinkEndDestructionData.html) object)
Returns the result of interpreting the object as an instance of '*Link End Destruction Data*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Link End Destruction Data*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDestroyLinkAction
public [T](UMLSwitch.html) caseDestroyLinkAction([DestroyLinkAction](../actions/mdintermediateactions/DestroyLinkAction.html) object)
Returns the result of interpreting the object as an instance of '*Destroy Link Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Destroy Link Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseRaiseExceptionAction
public [T](UMLSwitch.html) caseRaiseExceptionAction([RaiseExceptionAction](../actions/mdstructuredactions/RaiseExceptionAction.html) object)
Returns the result of interpreting the object as an instance of '*Raise Exception Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Raise Exception Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseAddStructuralFeatureValueAction
public [T](UMLSwitch.html) caseAddStructuralFeatureValueAction([AddStructuralFeatureValueAction](../actions/mdintermediateactions/AddStructuralFeatureValueAction.html) object)
Returns the result of interpreting the object as an instance of '*Add Structural Feature Value Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Add Structural Feature Value Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseAddVariableValueAction
public [T](UMLSwitch.html) caseAddVariableValueAction([AddVariableValueAction](../actions/mdstructuredactions/AddVariableValueAction.html) object)
Returns the result of interpreting the object as an instance of '*Add Variable Value Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Add Variable Value Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseWriteVariableAction
public [T](UMLSwitch.html) caseWriteVariableAction([WriteVariableAction](../actions/mdstructuredactions/WriteVariableAction.html) object)
Returns the result of interpreting the object as an instance of '*Write Variable Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Write Variable Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseClearAssociationAction
public [T](UMLSwitch.html) caseClearAssociationAction([ClearAssociationAction](../actions/mdintermediateactions/ClearAssociationAction.html) object)
Returns the result of interpreting the object as an instance of '*Clear Association Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Clear Association Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseReclassifyObjectAction
public [T](UMLSwitch.html) caseReclassifyObjectAction([ReclassifyObjectAction](../actions/mdcompleteactions/ReclassifyObjectAction.html) object)
Returns the result of interpreting the object as an instance of '*Reclassify Object Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Reclassify Object Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseStartClassifierBehaviorAction
public [T](UMLSwitch.html) caseStartClassifierBehaviorAction([StartClassifierBehaviorAction](../actions/mdcompleteactions/StartClassifierBehaviorAction.html) object)
Returns the result of interpreting the object as an instance of '*Start Classifier Behavior Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Start Classifier Behavior Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseStartObjectBehaviorAction
public [T](UMLSwitch.html) caseStartObjectBehaviorAction([StartObjectBehaviorAction](../actions/mdcompleteactions/StartObjectBehaviorAction.html) object)
Returns the result of interpreting the object as an instance of '*Start Object Behavior Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Start Object Behavior Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseRemoveStructuralFeatureValueAction
public [T](UMLSwitch.html) caseRemoveStructuralFeatureValueAction([RemoveStructuralFeatureValueAction](../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html) object)
Returns the result of interpreting the object as an instance of '*Remove Structural Feature Value Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Remove Structural Feature Value Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseRemoveVariableValueAction
public [T](UMLSwitch.html) caseRemoveVariableValueAction([RemoveVariableValueAction](../actions/mdstructuredactions/RemoveVariableValueAction.html) object)
Returns the result of interpreting the object as an instance of '*Remove Variable Value Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Remove Variable Value Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseSendObjectAction
public [T](UMLSwitch.html) caseSendObjectAction([SendObjectAction](../actions/mdintermediateactions/SendObjectAction.html) object)
Returns the result of interpreting the object as an instance of '*Send Object Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Send Object Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDestroyObjectAction
public [T](UMLSwitch.html) caseDestroyObjectAction([DestroyObjectAction](../actions/mdintermediateactions/DestroyObjectAction.html) object)
Returns the result of interpreting the object as an instance of '*Destroy Object Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Destroy Object Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseChangeEvent
public [T](UMLSwitch.html) caseChangeEvent([ChangeEvent](../commonbehaviors/mdcommunications/ChangeEvent.html) object)
Returns the result of interpreting the object as an instance of '*Change Event*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Change Event*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDuration
public [T](UMLSwitch.html) caseDuration([Duration](../commonbehaviors/mdsimpletime/Duration.html) object)
Returns the result of interpreting the object as an instance of '*Duration*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Duration*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseObservation
public [T](UMLSwitch.html) caseObservation([Observation](../commonbehaviors/mdsimpletime/Observation.html) object)
Returns the result of interpreting the object as an instance of '*Observation*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Observation*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTimeExpression
public [T](UMLSwitch.html) caseTimeExpression([TimeExpression](../commonbehaviors/mdsimpletime/TimeExpression.html) object)
Returns the result of interpreting the object as an instance of '*Time Expression*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Time Expression*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTimeInterval
public [T](UMLSwitch.html) caseTimeInterval([TimeInterval](../commonbehaviors/mdsimpletime/TimeInterval.html) object)
Returns the result of interpreting the object as an instance of '*Time Interval*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Time Interval*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInterval
public [T](UMLSwitch.html) caseInterval([Interval](../commonbehaviors/mdsimpletime/Interval.html) object)
Returns the result of interpreting the object as an instance of '*Interval*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Interval*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseIntervalConstraint
public [T](UMLSwitch.html) caseIntervalConstraint([IntervalConstraint](../commonbehaviors/mdsimpletime/IntervalConstraint.html) object)
Returns the result of interpreting the object as an instance of '*Interval Constraint*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Interval Constraint*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTimeConstraint
public [T](UMLSwitch.html) caseTimeConstraint([TimeConstraint](../commonbehaviors/mdsimpletime/TimeConstraint.html) object)
Returns the result of interpreting the object as an instance of '*Time Constraint*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Time Constraint*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTimeEvent
public [T](UMLSwitch.html) caseTimeEvent([TimeEvent](../commonbehaviors/mdcommunications/TimeEvent.html) object)
Returns the result of interpreting the object as an instance of '*Time Event*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Time Event*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDurationInterval
public [T](UMLSwitch.html) caseDurationInterval([DurationInterval](../commonbehaviors/mdsimpletime/DurationInterval.html) object)
Returns the result of interpreting the object as an instance of '*Duration Interval*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Duration Interval*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDurationConstraint
public [T](UMLSwitch.html) caseDurationConstraint([DurationConstraint](../commonbehaviors/mdsimpletime/DurationConstraint.html) object)
Returns the result of interpreting the object as an instance of '*Duration Constraint*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Duration Constraint*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseJoinNode
public [T](UMLSwitch.html) caseJoinNode([JoinNode](../activities/mdintermediateactivities/JoinNode.html) object)
Returns the result of interpreting the object as an instance of '*Join Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Join Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseControlNode
public [T](UMLSwitch.html) caseControlNode([ControlNode](../activities/mdbasicactivities/ControlNode.html) object)
Returns the result of interpreting the object as an instance of '*Control Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Control Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseExpression
public [T](UMLSwitch.html) caseExpression([Expression](../classes/mdkernel/Expression.html) object)
Returns the result of interpreting the object as an instance of '*Expression*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Expression*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseValuePin
public [T](UMLSwitch.html) caseValuePin([ValuePin](../actions/mdbasicactions/ValuePin.html) object)
Returns the result of interpreting the object as an instance of '*Value Pin*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Value Pin*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseActivityParameterNode
public [T](UMLSwitch.html) caseActivityParameterNode([ActivityParameterNode](../activities/mdbasicactivities/ActivityParameterNode.html) object)
Returns the result of interpreting the object as an instance of '*Activity Parameter Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Activity Parameter Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseBehaviorExecutionSpecification
public [T](UMLSwitch.html) caseBehaviorExecutionSpecification([BehaviorExecutionSpecification](../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html) object)
Returns the result of interpreting the object as an instance of '*Behavior Execution Specification*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Behavior Execution Specification*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseCallBehaviorAction
public [T](UMLSwitch.html) caseCallBehaviorAction([CallBehaviorAction](../actions/mdbasicactions/CallBehaviorAction.html) object)
Returns the result of interpreting the object as an instance of '*Call Behavior Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Call Behavior Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDecisionNode
public [T](UMLSwitch.html) caseDecisionNode([DecisionNode](../activities/mdintermediateactivities/DecisionNode.html) object)
Returns the result of interpreting the object as an instance of '*Decision Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Decision Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseObjectFlow
public [T](UMLSwitch.html) caseObjectFlow([ObjectFlow](../activities/mdbasicactivities/ObjectFlow.html) object)
Returns the result of interpreting the object as an instance of '*Object Flow*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Object Flow*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseExtension
public [T](UMLSwitch.html) caseExtension([Extension](../mdprofiles/Extension.html) object)
Returns the result of interpreting the object as an instance of '*Extension*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Extension*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseExtensionEnd
public [T](UMLSwitch.html) caseExtensionEnd([ExtensionEnd](../mdprofiles/ExtensionEnd.html) object)
Returns the result of interpreting the object as an instance of '*Extension End*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Extension End*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseImage
public [T](UMLSwitch.html) caseImage([Image](../mdprofiles/Image.html) object)
Returns the result of interpreting the object as an instance of '*Image*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Image*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
casePackageMerge
public [T](UMLSwitch.html) casePackageMerge([PackageMerge](../classes/mdkernel/PackageMerge.html) object)
Returns the result of interpreting the object as an instance of '*Package Merge*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Package Merge*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseProfileApplication
public [T](UMLSwitch.html) caseProfileApplication([ProfileApplication](../mdprofiles/ProfileApplication.html) object)
Returns the result of interpreting the object as an instance of '*Profile Application*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Profile Application*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
casePackageImport
public [T](UMLSwitch.html) casePackageImport([PackageImport](../classes/mdkernel/PackageImport.html) object)
Returns the result of interpreting the object as an instance of '*Package Import*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Package Import*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDiagram
public [T](UMLSwitch.html) caseDiagram([Diagram](../classes/mdkernel/Diagram.html) object)
Returns the result of interpreting the object as an instance of '*Diagram*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Diagram*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseGeneralization
public [T](UMLSwitch.html) caseGeneralization([Generalization](../classes/mdkernel/Generalization.html) object)
Returns the result of interpreting the object as an instance of '*Generalization*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Generalization*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseGeneralizationSet
public [T](UMLSwitch.html) caseGeneralizationSet([GeneralizationSet](../classes/mdpowertypes/GeneralizationSet.html) object)
Returns the result of interpreting the object as an instance of '*Generalization Set*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Generalization Set*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseRedefinableTemplateSignature
public [T](UMLSwitch.html) caseRedefinableTemplateSignature([RedefinableTemplateSignature](../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html) object)
Returns the result of interpreting the object as an instance of '*Redefinable Template Signature*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Redefinable Template Signature*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseSubstitution
public [T](UMLSwitch.html) caseSubstitution([Substitution](../classes/mddependencies/Substitution.html) object)
Returns the result of interpreting the object as an instance of '*Substitution*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Substitution*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseClassifierTemplateParameter
public [T](UMLSwitch.html) caseClassifierTemplateParameter([ClassifierTemplateParameter](../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html) object)
Returns the result of interpreting the object as an instance of '*Classifier Template Parameter*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Classifier Template Parameter*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInformationItem
public [T](UMLSwitch.html) caseInformationItem([InformationItem](../auxiliaryconstructs/mdinformationflows/InformationItem.html) object)
Returns the result of interpreting the object as an instance of '*Information Item*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Information Item*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTemplateParameterSubstitution
public [T](UMLSwitch.html) caseTemplateParameterSubstitution([TemplateParameterSubstitution](../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html) object)
Returns the result of interpreting the object as an instance of '*Template Parameter Substitution*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Template Parameter Substitution*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInstanceValue
public [T](UMLSwitch.html) caseInstanceValue([InstanceValue](../classes/mdkernel/InstanceValue.html) object)
Returns the result of interpreting the object as an instance of '*Instance Value*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Instance Value*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseElementValue
public [T](UMLSwitch.html) caseElementValue([ElementValue](../classes/mdkernel/ElementValue.html) object)
Returns the result of interpreting the object as an instance of '*Element Value*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Element Value*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseStringExpression
public [T](UMLSwitch.html) caseStringExpression([StringExpression](../auxiliaryconstructs/mdtemplates/StringExpression.html) object)
Returns the result of interpreting the object as an instance of '*String Expression*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*String Expression*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDurationObservation
public [T](UMLSwitch.html) caseDurationObservation([DurationObservation](../commonbehaviors/mdsimpletime/DurationObservation.html) object)
Returns the result of interpreting the object as an instance of '*Duration Observation*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Duration Observation*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseTimeObservation
public [T](UMLSwitch.html) caseTimeObservation([TimeObservation](../commonbehaviors/mdsimpletime/TimeObservation.html) object)
Returns the result of interpreting the object as an instance of '*Time Observation*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Time Observation*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseConsiderIgnoreFragment
public [T](UMLSwitch.html) caseConsiderIgnoreFragment([ConsiderIgnoreFragment](../interactions/mdfragments/ConsiderIgnoreFragment.html) object)
Returns the result of interpreting the object as an instance of '*Consider Ignore Fragment*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Consider Ignore Fragment*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseSequenceNode
public [T](UMLSwitch.html) caseSequenceNode([SequenceNode](../activities/mdstructuredactivities/SequenceNode.html) object)
Returns the result of interpreting the object as an instance of '*Sequence Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Sequence Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseActionExecutionSpecification
public [T](UMLSwitch.html) caseActionExecutionSpecification([ActionExecutionSpecification](../interactions/mdbasicinteractions/ActionExecutionSpecification.html) object)
Returns the result of interpreting the object as an instance of '*Action Execution Specification*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Action Execution Specification*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseActionInputPin
public [T](UMLSwitch.html) caseActionInputPin([ActionInputPin](../actions/mdstructuredactions/ActionInputPin.html) object)
Returns the result of interpreting the object as an instance of '*Action Input Pin*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Action Input Pin*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseLiteralString
public [T](UMLSwitch.html) caseLiteralString([LiteralString](../classes/mdkernel/LiteralString.html) object)
Returns the result of interpreting the object as an instance of '*Literal String*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Literal String*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseLiteralSpecification
public [T](UMLSwitch.html) caseLiteralSpecification([LiteralSpecification](../classes/mdkernel/LiteralSpecification.html) object)
Returns the result of interpreting the object as an instance of '*Literal Specification*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Literal Specification*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDataStoreNode
public [T](UMLSwitch.html) caseDataStoreNode([DataStoreNode](../activities/mdcompleteactivities/DataStoreNode.html) object)
Returns the result of interpreting the object as an instance of '*Data Store Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Data Store Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseCentralBufferNode
public [T](UMLSwitch.html) caseCentralBufferNode([CentralBufferNode](../activities/mdintermediateactivities/CentralBufferNode.html) object)
Returns the result of interpreting the object as an instance of '*Central Buffer Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Central Buffer Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseInitialNode
public [T](UMLSwitch.html) caseInitialNode([InitialNode](../activities/mdbasicactivities/InitialNode.html) object)
Returns the result of interpreting the object as an instance of '*Initial Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Initial Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDevice
public [T](UMLSwitch.html) caseDevice([Device](../deployments/mdnodes/Device.html) object)
Returns the result of interpreting the object as an instance of '*Device*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Device*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseNode
public [T](UMLSwitch.html) caseNode([Node](../deployments/mdnodes/Node.html) object)
Returns the result of interpreting the object as an instance of '*Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseAssociationClass
public [T](UMLSwitch.html) caseAssociationClass([AssociationClass](../classes/mdassociationclasses/AssociationClass.html) object)
Returns the result of interpreting the object as an instance of '*Association Class*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Association Class*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseActor
public [T](UMLSwitch.html) caseActor([Actor](../mdusecases/Actor.html) object)
Returns the result of interpreting the object as an instance of '*Actor*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Actor*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseExecutionEnvironment
public [T](UMLSwitch.html) caseExecutionEnvironment([ExecutionEnvironment](../deployments/mdnodes/ExecutionEnvironment.html) object)
Returns the result of interpreting the object as an instance of '*Execution Environment*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Execution Environment*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseFunctionBehavior
public [T](UMLSwitch.html) caseFunctionBehavior([FunctionBehavior](../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html) object)
Returns the result of interpreting the object as an instance of '*Function Behavior*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Function Behavior*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseOpaqueBehavior
public [T](UMLSwitch.html) caseOpaqueBehavior([OpaqueBehavior](../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html) object)
Returns the result of interpreting the object as an instance of '*Opaque Behavior*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Opaque Behavior*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseFinalNode
public [T](UMLSwitch.html) caseFinalNode([FinalNode](../activities/mdintermediateactivities/FinalNode.html) object)
Returns the result of interpreting the object as an instance of '*Final Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Final Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseActivityFinalNode
public [T](UMLSwitch.html) caseActivityFinalNode([ActivityFinalNode](../activities/mdbasicactivities/ActivityFinalNode.html) object)
Returns the result of interpreting the object as an instance of '*Activity Final Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Activity Final Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseFlowFinalNode
public [T](UMLSwitch.html) caseFlowFinalNode([FlowFinalNode](../activities/mdintermediateactivities/FlowFinalNode.html) object)
Returns the result of interpreting the object as an instance of '*Flow Final Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Flow Final Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseLiteralReal
public [T](UMLSwitch.html) caseLiteralReal([LiteralReal](../classes/mdkernel/LiteralReal.html) object)
Returns the result of interpreting the object as an instance of '*Literal Real*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Literal Real*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseForkNode
public [T](UMLSwitch.html) caseForkNode([ForkNode](../activities/mdintermediateactivities/ForkNode.html) object)
Returns the result of interpreting the object as an instance of '*Fork Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Fork Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseControlFlow
public [T](UMLSwitch.html) caseControlFlow([ControlFlow](../activities/mdbasicactivities/ControlFlow.html) object)
Returns the result of interpreting the object as an instance of '*Control Flow*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Control Flow*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseUsage
public [T](UMLSwitch.html) caseUsage([Usage](../classes/mddependencies/Usage.html) object)
Returns the result of interpreting the object as an instance of '*Usage*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Usage*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseLiteralUnlimitedNatural
public [T](UMLSwitch.html) caseLiteralUnlimitedNatural([LiteralUnlimitedNatural](../classes/mdkernel/LiteralUnlimitedNatural.html) object)
Returns the result of interpreting the object as an instance of '*Literal Unlimited Natural*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Literal Unlimited Natural*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseLiteralInteger
public [T](UMLSwitch.html) caseLiteralInteger([LiteralInteger](../classes/mdkernel/LiteralInteger.html) object)
Returns the result of interpreting the object as an instance of '*Literal Integer*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Literal Integer*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseEnumeration
public [T](UMLSwitch.html) caseEnumeration([Enumeration](../classes/mdkernel/Enumeration.html) object)
Returns the result of interpreting the object as an instance of '*Enumeration*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Enumeration*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseEnumerationLiteral
public [T](UMLSwitch.html) caseEnumerationLiteral([EnumerationLiteral](../classes/mdkernel/EnumerationLiteral.html) object)
Returns the result of interpreting the object as an instance of '*Enumeration Literal*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Enumeration Literal*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseExpansionNode
public [T](UMLSwitch.html) caseExpansionNode([ExpansionNode](../activities/mdextrastructuredactivities/ExpansionNode.html) object)
Returns the result of interpreting the object as an instance of '*Expansion Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Expansion Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseExpansionRegion
public [T](UMLSwitch.html) caseExpansionRegion([ExpansionRegion](../activities/mdextrastructuredactivities/ExpansionRegion.html) object)
Returns the result of interpreting the object as an instance of '*Expansion Region*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Expansion Region*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseCommunicationPath
public [T](UMLSwitch.html) caseCommunicationPath([CommunicationPath](../deployments/mdnodes/CommunicationPath.html) object)
Returns the result of interpreting the object as an instance of '*Communication Path*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Communication Path*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
casePrimitiveType
public [T](UMLSwitch.html) casePrimitiveType([PrimitiveType](../classes/mdkernel/PrimitiveType.html) object)
Returns the result of interpreting the object as an instance of '*Primitive Type*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Primitive Type*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseFinalState
public [T](UMLSwitch.html) caseFinalState([FinalState](../statemachines/mdbehaviorstatemachines/FinalState.html) object)
Returns the result of interpreting the object as an instance of '*Final State*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Final State*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseAnyReceiveEvent
public [T](UMLSwitch.html) caseAnyReceiveEvent([AnyReceiveEvent](../commonbehaviors/mdcommunications/AnyReceiveEvent.html) object)
Returns the result of interpreting the object as an instance of '*Any Receive Event*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Any Receive Event*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseMergeNode
public [T](UMLSwitch.html) caseMergeNode([MergeNode](../activities/mdintermediateactivities/MergeNode.html) object)
Returns the result of interpreting the object as an instance of '*Merge Node*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Merge Node*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseContinuation
public [T](UMLSwitch.html) caseContinuation([Continuation](../interactions/mdfragments/Continuation.html) object)
Returns the result of interpreting the object as an instance of '*Continuation*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Continuation*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseLiteralNull
public [T](UMLSwitch.html) caseLiteralNull([LiteralNull](../classes/mdkernel/LiteralNull.html) object)
Returns the result of interpreting the object as an instance of '*Literal Null*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Literal Null*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseMessageOccurrenceSpecification
public [T](UMLSwitch.html) caseMessageOccurrenceSpecification([MessageOccurrenceSpecification](../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html) object)
Returns the result of interpreting the object as an instance of '*Message Occurrence Specification*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Message Occurrence Specification*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseLiteralBoolean
public [T](UMLSwitch.html) caseLiteralBoolean([LiteralBoolean](../classes/mdkernel/LiteralBoolean.html) object)
Returns the result of interpreting the object as an instance of '*Literal Boolean*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Literal Boolean*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseDestructionOccurrenceSpecification
public [T](UMLSwitch.html) caseDestructionOccurrenceSpecification([DestructionOccurrenceSpecification](../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html) object)
Returns the result of interpreting the object as an instance of '*Destruction Occurrence Specification*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Destruction Occurrence Specification*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseModel
public [T](UMLSwitch.html) caseModel([Model](../auxiliaryconstructs/mdmodels/Model.html) object)
Returns the result of interpreting the object as an instance of '*Model*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Model*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseClearVariableAction
public [T](UMLSwitch.html) caseClearVariableAction([ClearVariableAction](../actions/mdstructuredactions/ClearVariableAction.html) object)
Returns the result of interpreting the object as an instance of '*Clear Variable Action*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Clear Variable Action*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseModelObject
public [T](UMLSwitch.html) caseModelObject([ModelObject](../base/ModelObject.html) object)
Returns the result of interpreting the object as an instance of '*Model Object*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Model Object*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
caseMDObject
public [T](UMLSwitch.html) caseMDObject([MDObject](../../../../magicdraw/foundation/MDObject.html) object)
Returns the result of interpreting the object as an instance of '*MD Object*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*MD Object*'.
See Also:
[`doSwitch(EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:
defaultCase
public [T](UMLSwitch.html) defaultCase(org.eclipse.emf.ecore.EObject object)
Returns the result of interpreting the object as an instance of '*EObject*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch, but this is the last case anyway.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*EObject*'.
See Also:
[`doSwitch(org.eclipse.emf.ecore.EObject)`](#doSwitch(org.eclipse.emf.ecore.EObject))
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.util</a></div>
<h1 class="title" title="Class UMLSwitch">Class UMLSwitch&lt;T&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.magicdraw.util.UMLSwitch&lt;T&gt;</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">UMLSwitch&lt;T&gt;</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><!-- begin-user-doc -->
 The <b>Switch</b> for the model's inheritance hierarchy.
 It supports the call <a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(object)</code></a>
 to invoke the <code>caseXXX</code> method for each class of the model,
 starting with the actual class of the object
 and proceeding up the inheritance hierarchy
 until a non-null result is returned,
 which is the result of the switch.
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
<div class="block">The cached model package
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">UMLSwitch</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an instance of the switch.</div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseAbstraction(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Abstraction)">caseAbstraction</a><wbr/>(<a href="../classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Abstraction</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseAcceptCallAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptCallAction)">caseAcceptCallAction</a><wbr/>(<a href="../actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Accept Call Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseAcceptEventAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">caseAcceptEventAction</a><wbr/>(<a href="../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Accept Event Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)">caseAction</a><wbr/>(<a href="../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseActionExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ActionExecutionSpecification)">caseActionExecutionSpecification</a><wbr/>(<a href="../interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecification</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Action Execution Specification</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseActionInputPin(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin)">caseActionInputPin</a><wbr/>(<a href="../actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Action Input Pin</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">caseActivity</a><wbr/>(<a href="../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseActivityEdge(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)">caseActivityEdge</a><wbr/>(<a href="../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity Edge</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseActivityFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityFinalNode)">caseActivityFinalNode</a><wbr/>(<a href="../activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNode</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity Final Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseActivityGroup(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup)">caseActivityGroup</a><wbr/>(<a href="../activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity Group</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseActivityNode(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode)">caseActivityNode</a><wbr/>(<a href="../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseActivityParameterNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode)">caseActivityParameterNode</a><wbr/>(<a href="../activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity Parameter Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseActivityPartition(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ActivityPartition)">caseActivityPartition</a><wbr/>(<a href="../activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity Partition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseActor(com.nomagic.uml2.ext.magicdraw.mdusecases.Actor)">caseActor</a><wbr/>(<a href="../mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Actor</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseAddStructuralFeatureValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.AddStructuralFeatureValueAction)">caseAddStructuralFeatureValueAction</a><wbr/>(<a href="../actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Add Structural Feature Value Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseAddVariableValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.AddVariableValueAction)">caseAddVariableValueAction</a><wbr/>(<a href="../actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Add Variable Value Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseAnyReceiveEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.AnyReceiveEvent)">caseAnyReceiveEvent</a><wbr/>(<a href="../commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEvent</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Any Receive Event</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseArtifact(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact)">caseArtifact</a><wbr/>(<a href="../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Artifact</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">caseAssociation</a><wbr/>(<a href="../classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Association</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseAssociationClass(com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses.AssociationClass)">caseAssociationClass</a><wbr/>(<a href="../classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Association Class</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">caseBehavior</a><wbr/>(<a href="../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Behavior</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseBehavioralFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">caseBehavioralFeature</a><wbr/>(<a href="../classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Behavioral Feature</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseBehavioredClassifier(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">caseBehavioredClassifier</a><wbr/>(<a href="../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Behaviored Classifier</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseBehaviorExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.BehaviorExecutionSpecification)">caseBehaviorExecutionSpecification</a><wbr/>(<a href="../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecification</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Behavior Execution Specification</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseBroadcastSignalAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.BroadcastSignalAction)">caseBroadcastSignalAction</a><wbr/>(<a href="../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Broadcast Signal Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseCallAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallAction)">caseCallAction</a><wbr/>(<a href="../actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Call Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseCallBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction)">caseCallBehaviorAction</a><wbr/>(<a href="../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Call Behavior Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseCallEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallEvent)">caseCallEvent</a><wbr/>(<a href="../commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Call Event</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseCallOperationAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallOperationAction)">caseCallOperationAction</a><wbr/>(<a href="../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Call Operation Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseCentralBufferNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.CentralBufferNode)">caseCentralBufferNode</a><wbr/>(<a href="../activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Central Buffer Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseChangeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent)">caseChangeEvent</a><wbr/>(<a href="../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Change Event</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">caseClass</a><wbr/>(<a href="../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Class</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">caseClassifier</a><wbr/>(<a href="../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Classifier</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseClassifierTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)">caseClassifierTemplateParameter</a><wbr/>(<a href="../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Classifier Template Parameter</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseClause(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">caseClause</a><wbr/>(<a href="../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Clause</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseClearAssociationAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearAssociationAction)">caseClearAssociationAction</a><wbr/>(<a href="../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Clear Association Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseClearStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearStructuralFeatureAction)">caseClearStructuralFeatureAction</a><wbr/>(<a href="../actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Clear Structural Feature Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseClearVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ClearVariableAction)">caseClearVariableAction</a><wbr/>(<a href="../actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Clear Variable Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseCollaboration(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.Collaboration)">caseCollaboration</a><wbr/>(<a href="../compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Collaboration</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseCollaborationUse(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">caseCollaborationUse</a><wbr/>(<a href="../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Collaboration Use</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseCombinedFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)">caseCombinedFragment</a><wbr/>(<a href="../interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Combined Fragment</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">caseComment</a><wbr/>(<a href="../classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Comment</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseCommunicationPath(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.CommunicationPath)">caseCommunicationPath</a><wbr/>(<a href="../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Communication Path</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseComponent(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)">caseComponent</a><wbr/>(<a href="../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Component</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseComponentRealization(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.ComponentRealization)">caseComponentRealization</a><wbr/>(<a href="../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Component Realization</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseConditionalNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode)">caseConditionalNode</a><wbr/>(<a href="../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Conditional Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseConnectableElement(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement)">caseConnectableElement</a><wbr/>(<a href="../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Connectable Element</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseConnectableElementTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter)">caseConnectableElementTemplateParameter</a><wbr/>(<a href="../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Connectable Element Template Parameter</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseConnectionPointReference(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.ConnectionPointReference)">caseConnectionPointReference</a><wbr/>(<a href="../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Connection Point Reference</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector)">caseConnector</a><wbr/>(<a href="../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Connector</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseConnectorEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectorEnd)">caseConnectorEnd</a><wbr/>(<a href="../compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Connector End</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseConsiderIgnoreFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.ConsiderIgnoreFragment)">caseConsiderIgnoreFragment</a><wbr/>(<a href="../interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragment</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Consider Ignore Fragment</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">caseConstraint</a><wbr/>(<a href="../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Constraint</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseContinuation(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Continuation)">caseContinuation</a><wbr/>(<a href="../interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Continuation</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Continuation</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseControlFlow(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ControlFlow)">caseControlFlow</a><wbr/>(<a href="../activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Control Flow</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseControlNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ControlNode)">caseControlNode</a><wbr/>(<a href="../activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Control Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseCreateLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateLinkAction)">caseCreateLinkAction</a><wbr/>(<a href="../actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Create Link Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseCreateLinkObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.CreateLinkObjectAction)">caseCreateLinkObjectAction</a><wbr/>(<a href="../actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Create Link Object Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseCreateObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateObjectAction)">caseCreateObjectAction</a><wbr/>(<a href="../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Create Object Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDataStoreNode(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.DataStoreNode)">caseDataStoreNode</a><wbr/>(<a href="../activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Data Store Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDataType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType)">caseDataType</a><wbr/>(<a href="../classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Data Type</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDecisionNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.DecisionNode)">caseDecisionNode</a><wbr/>(<a href="../activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Decision Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDependency(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Dependency)">caseDependency</a><wbr/>(<a href="../classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Dependency</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDeployedArtifact(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeployedArtifact)">caseDeployedArtifact</a><wbr/>(<a href="../deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeployedArtifact</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Deployed Artifact</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDeployment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Deployment)">caseDeployment</a><wbr/>(<a href="../deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Deployment</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDeploymentSpecification(com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments.DeploymentSpecification)">caseDeploymentSpecification</a><wbr/>(<a href="../deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Deployment Specification</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDeploymentTarget(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeploymentTarget)">caseDeploymentTarget</a><wbr/>(<a href="../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Deployment Target</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDestroyLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyLinkAction)">caseDestroyLinkAction</a><wbr/>(<a href="../actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Destroy Link Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDestroyObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyObjectAction)">caseDestroyObjectAction</a><wbr/>(<a href="../actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Destroy Object Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDestructionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.DestructionOccurrenceSpecification)">caseDestructionOccurrenceSpecification</a><wbr/>(<a href="../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Destruction Occurrence Specification</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDevice(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Device)">caseDevice</a><wbr/>(<a href="../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Device</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">caseDiagram</a><wbr/>(<a href="../classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Diagram</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDirectedRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DirectedRelationship)">caseDirectedRelationship</a><wbr/>(<a href="../classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Directed Relationship</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration)">caseDuration</a><wbr/>(<a href="../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Duration</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDurationConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint)">caseDurationConstraint</a><wbr/>(<a href="../commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Duration Constraint</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval)">caseDurationInterval</a><wbr/>(<a href="../commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Duration Interval</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDurationObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationObservation)">caseDurationObservation</a><wbr/>(<a href="../commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Duration Observation</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">caseElement</a><wbr/>(<a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Element</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseElementImport(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementImport)">caseElementImport</a><wbr/>(<a href="../classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Element Import</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementValue)">caseElementValue</a><wbr/>(<a href="../classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Element Value</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseEncapsulatedClassifier(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier)">caseEncapsulatedClassifier</a><wbr/>(<a href="../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Encapsulated Classifier</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseEnumeration(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration)">caseEnumeration</a><wbr/>(<a href="../classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Enumeration</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseEnumerationLiteral(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">caseEnumerationLiteral</a><wbr/>(<a href="../classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Enumeration Literal</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event)">caseEvent</a><wbr/>(<a href="../commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Event</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseExceptionHandler(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExceptionHandler)">caseExceptionHandler</a><wbr/>(<a href="../activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Exception Handler</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ExecutableNode)">caseExecutableNode</a><wbr/>(<a href="../activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Executable Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseExecutionEnvironment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.ExecutionEnvironment)">caseExecutionEnvironment</a><wbr/>(<a href="../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Execution Environment</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseExecutionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ExecutionOccurrenceSpecification)">caseExecutionOccurrenceSpecification</a><wbr/>(<a href="../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionOccurrenceSpecification</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Execution Occurrence Specification</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ExecutionSpecification)">caseExecutionSpecification</a><wbr/>(<a href="../interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionSpecification</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Execution Specification</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseExpansionNode(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExpansionNode)">caseExpansionNode</a><wbr/>(<a href="../activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Expansion Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseExpansionRegion(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExpansionRegion)">caseExpansionRegion</a><wbr/>(<a href="../activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Expansion Region</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression)">caseExpression</a><wbr/>(<a href="../classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseExtend(com.nomagic.uml2.ext.magicdraw.mdusecases.Extend)">caseExtend</a><wbr/>(<a href="../mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Extend</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseExtension(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension)">caseExtension</a><wbr/>(<a href="../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Extension</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseExtensionEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.ExtensionEnd)">caseExtensionEnd</a><wbr/>(<a href="../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Extension End</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseExtensionPoint(com.nomagic.uml2.ext.magicdraw.mdusecases.ExtensionPoint)">caseExtensionPoint</a><wbr/>(<a href="../mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPoint</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Extension Point</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Feature)">caseFeature</a><wbr/>(<a href="../classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Feature</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.FinalNode)">caseFinalNode</a><wbr/>(<a href="../activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FinalNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Final Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseFinalState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.FinalState)">caseFinalState</a><wbr/>(<a href="../statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Final State</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseFlowFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.FlowFinalNode)">caseFlowFinalNode</a><wbr/>(<a href="../activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Flow Final Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseForkNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ForkNode)">caseForkNode</a><wbr/>(<a href="../activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNode</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Fork Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseFunctionBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.FunctionBehavior)">caseFunctionBehavior</a><wbr/>(<a href="../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Function Behavior</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate)">caseGate</a><wbr/>(<a href="../interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Gate</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseGeneralization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Generalization)">caseGeneralization</a><wbr/>(<a href="../classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Generalization</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseGeneralizationSet(com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes.GeneralizationSet)">caseGeneralizationSet</a><wbr/>(<a href="../classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Generalization Set</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseGeneralOrdering(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.GeneralOrdering)">caseGeneralOrdering</a><wbr/>(<a href="../interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">GeneralOrdering</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>General Ordering</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseImage(com.nomagic.uml2.ext.magicdraw.mdprofiles.Image)">caseImage</a><wbr/>(<a href="../mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Image</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInclude(com.nomagic.uml2.ext.magicdraw.mdusecases.Include)">caseInclude</a><wbr/>(<a href="../mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Include</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Include</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInformationFlow(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows.InformationFlow)">caseInformationFlow</a><wbr/>(<a href="../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Information Flow</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInformationItem(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows.InformationItem)">caseInformationItem</a><wbr/>(<a href="../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Information Item</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInitialNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.InitialNode)">caseInitialNode</a><wbr/>(<a href="../activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNode</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Initial Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInputPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin)">caseInputPin</a><wbr/>(<a href="../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Input Pin</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInstanceSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">caseInstanceSpecification</a><wbr/>(<a href="../classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Instance Specification</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInstanceValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceValue)">caseInstanceValue</a><wbr/>(<a href="../classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Instance Value</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">caseInteraction</a><wbr/>(<a href="../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interaction</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInteractionConstraint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)">caseInteractionConstraint</a><wbr/>(<a href="../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interaction Constraint</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInteractionFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.InteractionFragment)">caseInteractionFragment</a><wbr/>(<a href="../interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interaction Fragment</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInteractionOperand(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand)">caseInteractionOperand</a><wbr/>(<a href="../interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interaction Operand</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInteractionUse(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)">caseInteractionUse</a><wbr/>(<a href="../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interaction Use</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">caseInterface</a><wbr/>(<a href="../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interface</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInterfaceRealization(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.InterfaceRealization)">caseInterfaceRealization</a><wbr/>(<a href="../classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interface Realization</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInterruptibleActivityRegion(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.InterruptibleActivityRegion)">caseInterruptibleActivityRegion</a><wbr/>(<a href="../activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interruptible Activity Region</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Interval)">caseInterval</a><wbr/>(<a href="../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interval</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseIntervalConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint)">caseIntervalConstraint</a><wbr/>(<a href="../commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interval Constraint</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseInvocationAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction)">caseInvocationAction</a><wbr/>(<a href="../actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Invocation Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseJoinNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode)">caseJoinNode</a><wbr/>(<a href="../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Join Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseLifeline(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">caseLifeline</a><wbr/>(<a href="../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Lifeline</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction)">caseLinkAction</a><wbr/>(<a href="../actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Link Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseLinkEndCreationData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndCreationData)">caseLinkEndCreationData</a><wbr/>(<a href="../actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Link End Creation Data</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseLinkEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndData)">caseLinkEndData</a><wbr/>(<a href="../actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Link End Data</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseLinkEndDestructionData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndDestructionData)">caseLinkEndDestructionData</a><wbr/>(<a href="../actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Link End Destruction Data</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseLiteralBoolean(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralBoolean)">caseLiteralBoolean</a><wbr/>(<a href="../classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBoolean</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal Boolean</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseLiteralInteger(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralInteger)">caseLiteralInteger</a><wbr/>(<a href="../classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralInteger</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal Integer</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseLiteralNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralNull)">caseLiteralNull</a><wbr/>(<a href="../classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNull</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal Null</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseLiteralReal(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralReal)">caseLiteralReal</a><wbr/>(<a href="../classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralReal</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal Real</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseLiteralSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralSpecification)">caseLiteralSpecification</a><wbr/>(<a href="../classes/mdkernel/LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralSpecification</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal Specification</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseLiteralString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralString)">caseLiteralString</a><wbr/>(<a href="../classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralString</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal String</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseLiteralUnlimitedNatural(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralUnlimitedNatural)">caseLiteralUnlimitedNatural</a><wbr/>(<a href="../classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNatural</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal Unlimited Natural</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseLoopNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">caseLoopNode</a><wbr/>(<a href="../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Loop Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseManifestation(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Manifestation)">caseManifestation</a><wbr/>(<a href="../deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Manifestation</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Manifestation</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseMDObject(com.nomagic.magicdraw.foundation.MDObject)">caseMDObject</a><wbr/>(<a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>MD Object</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseMergeNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.MergeNode)">caseMergeNode</a><wbr/>(<a href="../activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Merge Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">caseMessage</a><wbr/>(<a href="../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Message</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseMessageEnd(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd)">caseMessageEnd</a><wbr/>(<a href="../interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Message End</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseMessageEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.MessageEvent)">caseMessageEvent</a><wbr/>(<a href="../commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">MessageEvent</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Message Event</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseMessageOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageOccurrenceSpecification)">caseMessageOccurrenceSpecification</a><wbr/>(<a href="../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecification</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Message Occurrence Specification</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseModel(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model)">caseModel</a><wbr/>(<a href="../auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Model</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseModelObject(com.nomagic.uml2.ext.magicdraw.base.ModelObject)">caseModelObject</a><wbr/>(<a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Model Object</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseMultiplicityElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">caseMultiplicityElement</a><wbr/>(<a href="../classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Multiplicity Element</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseNamedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement)">caseNamedElement</a><wbr/>(<a href="../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Named Element</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">caseNamespace</a><wbr/>(<a href="../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Namespace</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseNode(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Node)">caseNode</a><wbr/>(<a href="../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseObjectFlow(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectFlow)">caseObjectFlow</a><wbr/>(<a href="../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Object Flow</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseObjectNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode)">caseObjectNode</a><wbr/>(<a href="../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Object Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Observation)">caseObservation</a><wbr/>(<a href="../commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Observation</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Observation</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.OccurrenceSpecification)">caseOccurrenceSpecification</a><wbr/>(<a href="../interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecification</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Occurrence Specification</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseOpaqueAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction)">caseOpaqueAction</a><wbr/>(<a href="../actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Opaque Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseOpaqueBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.OpaqueBehavior)">caseOpaqueBehavior</a><wbr/>(<a href="../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Opaque Behavior</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseOpaqueExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression)">caseOpaqueExpression</a><wbr/>(<a href="../classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Opaque Expression</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">caseOperation</a><wbr/>(<a href="../classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Operation</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseOperationTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.OperationTemplateParameter)">caseOperationTemplateParameter</a><wbr/>(<a href="../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Operation Template Parameter</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseOutputPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin)">caseOutputPin</a><wbr/>(<a href="../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Output Pin</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#casePackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">casePackage</a><wbr/>(<a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Package</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#casePackageableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement)">casePackageableElement</a><wbr/>(<a href="../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Packageable Element</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#casePackageImport(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageImport)">casePackageImport</a><wbr/>(<a href="../classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Package Import</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#casePackageMerge(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageMerge)">casePackageMerge</a><wbr/>(<a href="../classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageMerge</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Package Merge</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter)">caseParameter</a><wbr/>(<a href="../classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Parameter</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseParameterableElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">caseParameterableElement</a><wbr/>(<a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Parameterable Element</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseParameterSet(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterSet)">caseParameterSet</a><wbr/>(<a href="../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Parameter Set</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#casePartDecomposition(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.PartDecomposition)">casePartDecomposition</a><wbr/>(<a href="../interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Part Decomposition</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#casePin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin)">casePin</a><wbr/>(<a href="../actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Pin</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#casePort(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port)">casePort</a><wbr/>(<a href="../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Port</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#casePrimitiveType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PrimitiveType)">casePrimitiveType</a><wbr/>(<a href="../classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Primitive Type</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">caseProfile</a><wbr/>(<a href="../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Profile</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseProfileApplication(com.nomagic.uml2.ext.magicdraw.mdprofiles.ProfileApplication)">caseProfileApplication</a><wbr/>(<a href="../mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplication</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Profile Application</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">caseProperty</a><wbr/>(<a href="../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Property</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseProtocolConformance(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolConformance)">caseProtocolConformance</a><wbr/>(<a href="../statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolConformance</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Protocol Conformance</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseProtocolStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine)">caseProtocolStateMachine</a><wbr/>(<a href="../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Protocol State Machine</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseProtocolTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition)">caseProtocolTransition</a><wbr/>(<a href="../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Protocol Transition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#casePseudostate(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Pseudostate)">casePseudostate</a><wbr/>(<a href="../statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Pseudostate</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseQualifierValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.QualifierValue)">caseQualifierValue</a><wbr/>(<a href="../actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Qualifier Value</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseRaiseExceptionAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RaiseExceptionAction)">caseRaiseExceptionAction</a><wbr/>(<a href="../actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Raise Exception Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseReadExtentAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadExtentAction)">caseReadExtentAction</a><wbr/>(<a href="../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Extent Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseReadIsClassifiedObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction)">caseReadIsClassifiedObjectAction</a><wbr/>(<a href="../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Is Classified Object Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseReadLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadLinkAction)">caseReadLinkAction</a><wbr/>(<a href="../actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Link Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseReadLinkObjectEndAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction)">caseReadLinkObjectEndAction</a><wbr/>(<a href="../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Link Object End Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseReadLinkObjectEndQualifierAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction)">caseReadLinkObjectEndQualifierAction</a><wbr/>(<a href="../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Link Object End Qualifier Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseReadSelfAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadSelfAction)">caseReadSelfAction</a><wbr/>(<a href="../actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Self Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseReadStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadStructuralFeatureAction)">caseReadStructuralFeatureAction</a><wbr/>(<a href="../actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Structural Feature Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseReadVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ReadVariableAction)">caseReadVariableAction</a><wbr/>(<a href="../actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Variable Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseRealization(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Realization)">caseRealization</a><wbr/>(<a href="../classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Realization</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseReception(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception)">caseReception</a><wbr/>(<a href="../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Reception</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseReclassifyObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReclassifyObjectAction)">caseReclassifyObjectAction</a><wbr/>(<a href="../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Reclassify Object Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseRedefinableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement)">caseRedefinableElement</a><wbr/>(<a href="../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Redefinable Element</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseRedefinableTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)">caseRedefinableTemplateSignature</a><wbr/>(<a href="../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Redefinable Template Signature</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseReduceAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction)">caseReduceAction</a><wbr/>(<a href="../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Reduce Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseRegion(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region)">caseRegion</a><wbr/>(<a href="../statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Region</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Relationship)">caseRelationship</a><wbr/>(<a href="../classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Relationship</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseRemoveStructuralFeatureValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.RemoveStructuralFeatureValueAction)">caseRemoveStructuralFeatureValueAction</a><wbr/>(<a href="../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Remove Structural Feature Value Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseRemoveVariableValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RemoveVariableValueAction)">caseRemoveVariableValueAction</a><wbr/>(<a href="../actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Remove Variable Value Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseReplyAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction)">caseReplyAction</a><wbr/>(<a href="../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Reply Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseSendObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction)">caseSendObjectAction</a><wbr/>(<a href="../actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Send Object Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseSendSignalAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.SendSignalAction)">caseSendSignalAction</a><wbr/>(<a href="../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Send Signal Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseSequenceNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode)">caseSequenceNode</a><wbr/>(<a href="../activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Sequence Node</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)">caseSignal</a><wbr/>(<a href="../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Signal</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseSignalEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.SignalEvent)">caseSignalEvent</a><wbr/>(<a href="../commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Signal Event</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">caseSlot</a><wbr/>(<a href="../classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Slot</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseStartClassifierBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartClassifierBehaviorAction)">caseStartClassifierBehaviorAction</a><wbr/>(<a href="../actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Start Classifier Behavior Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseStartObjectBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartObjectBehaviorAction)">caseStartObjectBehaviorAction</a><wbr/>(<a href="../actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Start Object Behavior Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">caseState</a><wbr/>(<a href="../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>State</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseStateInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant)">caseStateInvariant</a><wbr/>(<a href="../interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>State Invariant</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine)">caseStateMachine</a><wbr/>(<a href="../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>State Machine</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">caseStereotype</a><wbr/>(<a href="../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Stereotype</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseStringExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">caseStringExpression</a><wbr/>(<a href="../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>String Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseStructuralFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature)">caseStructuralFeature</a><wbr/>(<a href="../classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Structural Feature</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.StructuralFeatureAction)">caseStructuralFeatureAction</a><wbr/>(<a href="../actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Structural Feature Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseStructuredActivityNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">caseStructuredActivityNode</a><wbr/>(<a href="../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Structured Activity Node</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseStructuredClassifier(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier)">caseStructuredClassifier</a><wbr/>(<a href="../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Structured Classifier</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseSubstitution(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Substitution)">caseSubstitution</a><wbr/>(<a href="../classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Substitution</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTemplateableElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateableElement)">caseTemplateableElement</a><wbr/>(<a href="../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Templateable Element</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTemplateBinding(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding)">caseTemplateBinding</a><wbr/>(<a href="../auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Template Binding</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">caseTemplateParameter</a><wbr/>(<a href="../auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Template Parameter</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTemplateParameterSubstitution(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">caseTemplateParameterSubstitution</a><wbr/>(<a href="../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Template Parameter Substitution</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature)">caseTemplateSignature</a><wbr/>(<a href="../auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Template Signature</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTestIdentityAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction)">caseTestIdentityAction</a><wbr/>(<a href="../actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Test Identity Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTimeConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint)">caseTimeConstraint</a><wbr/>(<a href="../commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Time Constraint</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTimeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.TimeEvent)">caseTimeEvent</a><wbr/>(<a href="../commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEvent</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Time Event</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)">caseTimeExpression</a><wbr/>(<a href="../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Time Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval)">caseTimeInterval</a><wbr/>(<a href="../commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Time Interval</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTimeObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeObservation)">caseTimeObservation</a><wbr/>(<a href="../commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Time Observation</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">caseTransition</a><wbr/>(<a href="../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Transition</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTrigger(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger)">caseTrigger</a><wbr/>(<a href="../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Trigger</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">caseType</a><wbr/>(<a href="../classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Type</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseTypedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement)">caseTypedElement</a><wbr/>(<a href="../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Typed Element</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseUnmarshallAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction)">caseUnmarshallAction</a><wbr/>(<a href="../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Unmarshall Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseUsage(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Usage)">caseUsage</a><wbr/>(<a href="../classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Usage</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Usage</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">caseUseCase</a><wbr/>(<a href="../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Use Case</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseValuePin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin)">caseValuePin</a><wbr/>(<a href="../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Value Pin</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">caseValueSpecification</a><wbr/>(<a href="../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Value Specification</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseValueSpecificationAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction)">caseValueSpecificationAction</a><wbr/>(<a href="../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Value Specification Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseVariable(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Variable)">caseVariable</a><wbr/>(<a href="../activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Variable</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.VariableAction)">caseVariableAction</a><wbr/>(<a href="../actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">VariableAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Variable Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseVertex(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex)">caseVertex</a><wbr/>(<a href="../statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Vertex</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseWriteLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteLinkAction)">caseWriteLinkAction</a><wbr/>(<a href="../actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteLinkAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Write Link Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseWriteStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction)">caseWriteStructuralFeatureAction</a><wbr/>(<a href="../actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Write Structural Feature Action</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseWriteVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.WriteVariableAction)">caseWriteVariableAction</a><wbr/>(<a href="../actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Write Variable Action</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#defaultCase(org.eclipse.emf.ecore.EObject)">defaultCase</a><wbr/>(org.eclipse.emf.ecore.EObject object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>EObject</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#doSwitch(int,org.eclipse.emf.ecore.EObject)">doSwitch</a><wbr/>(int classifierID,
 org.eclipse.emf.ecore.EObject theEObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calls <code>caseXXX</code> for each class of the model until one returns a non null result; it yields that result.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#doSwitch(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EObject)">doSwitch</a><wbr/>(org.eclipse.emf.ecore.EClass theEClass,
 org.eclipse.emf.ecore.EObject theEObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calls <code>caseXXX</code> for each class of the model until one returns a non null result; it yields that result.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#doSwitch(org.eclipse.emf.ecore.EObject)">doSwitch</a><wbr/>(org.eclipse.emf.ecore.EObject theEObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calls <code>caseXXX</code> for each class of the model until one returns a non null result; it yields that result.</div>
</div>
</div>
</div>
</div>
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
<div class="block">The cached model package
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
<h3>UMLSwitch</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">UMLSwitch</span>()</div>
<div class="block">Creates an instance of the switch.
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
<section class="detail" id="doSwitch(org.eclipse.emf.ecore.EObject)">
<h3>doSwitch</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">doSwitch</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EObject theEObject)</span></div>
<div class="block">Calls <code>caseXXX</code> for each class of the model until one returns a non null result; it yields that result.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the first non-null result returned by a <code>caseXXX</code> call.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="doSwitch(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EObject)">
<h3>doSwitch</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">doSwitch</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass theEClass,
 org.eclipse.emf.ecore.EObject theEObject)</span></div>
<div class="block">Calls <code>caseXXX</code> for each class of the model until one returns a non null result; it yields that result.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the first non-null result returned by a <code>caseXXX</code> call.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="doSwitch(int,org.eclipse.emf.ecore.EObject)">
<h3>doSwitch</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">doSwitch</span><wbr/><span class="parameters">(int classifierID,
 org.eclipse.emf.ecore.EObject theEObject)</span></div>
<div class="block">Calls <code>caseXXX</code> for each class of the model until one returns a non null result; it yields that result.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the first non-null result returned by a <code>caseXXX</code> call.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseSendSignalAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.SendSignalAction)">
<h3>caseSendSignalAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseSendSignalAction</span><wbr/><span class="parameters">(<a href="../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Send Signal Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Send Signal Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInvocationAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction)">
<h3>caseInvocationAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInvocationAction</span><wbr/><span class="parameters">(<a href="../actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Invocation Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Invocation Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)">
<h3>caseAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseAction</span><wbr/><span class="parameters">(<a href="../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ExecutableNode)">
<h3>caseExecutableNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseExecutableNode</span><wbr/><span class="parameters">(<a href="../activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Executable Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Executable Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseActivityNode(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode)">
<h3>caseActivityNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseActivityNode</span><wbr/><span class="parameters">(<a href="../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Activity Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseRedefinableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement)">
<h3>caseRedefinableElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseRedefinableElement</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Redefinable Element</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Redefinable Element</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseNamedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement)">
<h3>caseNamedElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseNamedElement</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Named Element</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Named Element</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>caseElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseElement</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Element</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Element</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">
<h3>caseComment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseComment</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Comment</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Comment</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInstanceSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>caseInstanceSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInstanceSpecification</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Instance Specification</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Instance Specification</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="casePackageableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement)">
<h3>casePackageableElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">casePackageableElement</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Packageable Element</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Packageable Element</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseParameterableElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">
<h3>caseParameterableElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseParameterableElement</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Parameterable Element</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Parameterable Element</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">
<h3>caseTemplateParameter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTemplateParameter</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Template Parameter</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Template Parameter</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature)">
<h3>caseTemplateSignature</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTemplateSignature</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Template Signature</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Template Signature</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTemplateableElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateableElement)">
<h3>caseTemplateableElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTemplateableElement</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Templateable Element</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Templateable Element</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTemplateBinding(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding)">
<h3>caseTemplateBinding</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTemplateBinding</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Template Binding</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Template Binding</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDirectedRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DirectedRelationship)">
<h3>caseDirectedRelationship</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDirectedRelationship</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Directed Relationship</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Directed Relationship</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Relationship)">
<h3>caseRelationship</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseRelationship</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Relationship</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Relationship</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInformationFlow(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows.InformationFlow)">
<h3>caseInformationFlow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInformationFlow</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Information Flow</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Information Flow</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>caseClassifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseClassifier</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Classifier</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Classifier</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>caseNamespace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseNamespace</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Namespace</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Namespace</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseElementImport(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementImport)">
<h3>caseElementImport</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseElementImport</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Element Import</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Element Import</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">
<h3>caseProfile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseProfile</span><wbr/><span class="parameters">(<a href="../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Profile</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Profile</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="casePackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>casePackage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">casePackage</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Package</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Package</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>caseStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseStereotype</span><wbr/><span class="parameters">(<a href="../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Stereotype</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Stereotype</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>caseClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseClass</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Class</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Class</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseBehavioredClassifier(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">
<h3>caseBehavioredClassifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseBehavioredClassifier</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Behaviored Classifier</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Behaviored Classifier</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">
<h3>caseBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseBehavior</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Behavior</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Behavior</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter)">
<h3>caseParameter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseParameter</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Parameter</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Parameter</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseMultiplicityElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">
<h3>caseMultiplicityElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseMultiplicityElement</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Multiplicity Element</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Multiplicity Element</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>caseValueSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseValueSpecification</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Value Specification</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Value Specification</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTypedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement)">
<h3>caseTypedElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTypedElement</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Typed Element</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Typed Element</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>caseType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseType</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Type</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Type</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>caseAssociation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseAssociation</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Association</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Association</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>caseProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseProperty</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Property</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Property</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseStructuralFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature)">
<h3>caseStructuralFeature</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseStructuralFeature</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Structural Feature</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Structural Feature</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Feature)">
<h3>caseFeature</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseFeature</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Feature</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Feature</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">
<h3>caseSlot</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseSlot</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Slot</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Slot</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.StructuralFeatureAction)">
<h3>caseStructuralFeatureAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseStructuralFeatureAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Structural Feature Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Structural Feature Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInputPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin)">
<h3>caseInputPin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInputPin</span><wbr/><span class="parameters">(<a href="../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Input Pin</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Input Pin</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="casePin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin)">
<h3>casePin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">casePin</span><wbr/><span class="parameters">(<a href="../actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Pin</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Pin</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseObjectNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode)">
<h3>caseObjectNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseObjectNode</span><wbr/><span class="parameters">(<a href="../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Object Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Object Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">
<h3>caseState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseState</span><wbr/><span class="parameters">(<a href="../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>State</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>State</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseVertex(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex)">
<h3>caseVertex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseVertex</span><wbr/><span class="parameters">(<a href="../statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Vertex</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Vertex</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseRegion(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region)">
<h3>caseRegion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseRegion</span><wbr/><span class="parameters">(<a href="../statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Region</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Region</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine)">
<h3>caseStateMachine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseStateMachine</span><wbr/><span class="parameters">(<a href="../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>State Machine</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>State Machine</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="casePseudostate(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Pseudostate)">
<h3>casePseudostate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">casePseudostate</span><wbr/><span class="parameters">(<a href="../statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Pseudostate</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Pseudostate</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseConnectionPointReference(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.ConnectionPointReference)">
<h3>caseConnectionPointReference</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseConnectionPointReference</span><wbr/><span class="parameters">(<a href="../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Connection Point Reference</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Connection Point Reference</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">
<h3>caseTransition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTransition</span><wbr/><span class="parameters">(<a href="../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Transition</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Transition</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>caseConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseConstraint</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Constraint</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Constraint</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">
<h3>caseOperation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseOperation</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Operation</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Operation</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseBehavioralFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">
<h3>caseBehavioralFeature</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseBehavioralFeature</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Behavioral Feature</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Behavioral Feature</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseParameterSet(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterSet)">
<h3>caseParameterSet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseParameterSet</span><wbr/><span class="parameters">(<a href="../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Parameter Set</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Parameter Set</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDataType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType)">
<h3>caseDataType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDataType</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Data Type</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Data Type</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">
<h3>caseInterface</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInterface</span><wbr/><span class="parameters">(<a href="../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interface</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Interface</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseReception(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception)">
<h3>caseReception</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseReception</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Reception</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Reception</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)">
<h3>caseSignal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseSignal</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Signal</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Signal</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseBroadcastSignalAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.BroadcastSignalAction)">
<h3>caseBroadcastSignalAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseBroadcastSignalAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Broadcast Signal Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Broadcast Signal Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseSignalEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.SignalEvent)">
<h3>caseSignalEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseSignalEvent</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Signal Event</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Signal Event</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseMessageEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.MessageEvent)">
<h3>caseMessageEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseMessageEvent</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">MessageEvent</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Message Event</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Message Event</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event)">
<h3>caseEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseEvent</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Event</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Event</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTrigger(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger)">
<h3>caseTrigger</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTrigger</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Trigger</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Trigger</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="casePort(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port)">
<h3>casePort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">casePort</span><wbr/><span class="parameters">(<a href="../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Port</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Port</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseProtocolStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine)">
<h3>caseProtocolStateMachine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseProtocolStateMachine</span><wbr/><span class="parameters">(<a href="../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Protocol State Machine</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Protocol State Machine</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseProtocolConformance(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolConformance)">
<h3>caseProtocolConformance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseProtocolConformance</span><wbr/><span class="parameters">(<a href="../statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolConformance</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Protocol Conformance</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Protocol Conformance</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseEncapsulatedClassifier(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier)">
<h3>caseEncapsulatedClassifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseEncapsulatedClassifier</span><wbr/><span class="parameters">(<a href="../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Encapsulated Classifier</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Encapsulated Classifier</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseStructuredClassifier(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier)">
<h3>caseStructuredClassifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseStructuredClassifier</span><wbr/><span class="parameters">(<a href="../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Structured Classifier</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Structured Classifier</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector)">
<h3>caseConnector</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseConnector</span><wbr/><span class="parameters">(<a href="../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Connector</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Connector</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseConnectorEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectorEnd)">
<h3>caseConnectorEnd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseConnectorEnd</span><wbr/><span class="parameters">(<a href="../compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Connector End</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Connector End</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseConnectableElement(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement)">
<h3>caseConnectableElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseConnectableElement</span><wbr/><span class="parameters">(<a href="../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Connectable Element</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Connectable Element</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseConnectableElementTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter)">
<h3>caseConnectableElementTemplateParameter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseConnectableElementTemplateParameter</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Connectable Element Template Parameter</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Connectable Element Template Parameter</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseCollaboration(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.Collaboration)">
<h3>caseCollaboration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseCollaboration</span><wbr/><span class="parameters">(<a href="../compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Collaboration</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Collaboration</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseCollaborationUse(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">
<h3>caseCollaborationUse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseCollaborationUse</span><wbr/><span class="parameters">(<a href="../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Collaboration Use</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Collaboration Use</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDependency(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Dependency)">
<h3>caseDependency</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDependency</span><wbr/><span class="parameters">(<a href="../classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Dependency</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Dependency</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseLifeline(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">
<h3>caseLifeline</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseLifeline</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Lifeline</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Lifeline</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInteractionFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.InteractionFragment)">
<h3>caseInteractionFragment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInteractionFragment</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interaction Fragment</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Interaction Fragment</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">
<h3>caseInteraction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInteraction</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interaction</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Interaction</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate)">
<h3>caseGate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseGate</span><wbr/><span class="parameters">(<a href="../interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Gate</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Gate</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseMessageEnd(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd)">
<h3>caseMessageEnd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseMessageEnd</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Message End</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Message End</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>caseMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseMessage</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Message</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Message</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInteractionUse(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)">
<h3>caseInteractionUse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInteractionUse</span><wbr/><span class="parameters">(<a href="../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interaction Use</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Interaction Use</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseCombinedFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)">
<h3>caseCombinedFragment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseCombinedFragment</span><wbr/><span class="parameters">(<a href="../interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Combined Fragment</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Combined Fragment</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInteractionOperand(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand)">
<h3>caseInteractionOperand</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInteractionOperand</span><wbr/><span class="parameters">(<a href="../interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interaction Operand</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Interaction Operand</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInteractionConstraint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)">
<h3>caseInteractionConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInteractionConstraint</span><wbr/><span class="parameters">(<a href="../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interaction Constraint</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Interaction Constraint</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseGeneralOrdering(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.GeneralOrdering)">
<h3>caseGeneralOrdering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseGeneralOrdering</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">GeneralOrdering</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>General Ordering</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>General Ordering</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.OccurrenceSpecification)">
<h3>caseOccurrenceSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseOccurrenceSpecification</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecification</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Occurrence Specification</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Occurrence Specification</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ExecutionSpecification)">
<h3>caseExecutionSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseExecutionSpecification</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionSpecification</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Execution Specification</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Execution Specification</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseExecutionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ExecutionOccurrenceSpecification)">
<h3>caseExecutionOccurrenceSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseExecutionOccurrenceSpecification</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionOccurrenceSpecification</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Execution Occurrence Specification</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Execution Occurrence Specification</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="casePartDecomposition(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.PartDecomposition)">
<h3>casePartDecomposition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">casePartDecomposition</span><wbr/><span class="parameters">(<a href="../interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Part Decomposition</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Part Decomposition</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseStateInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant)">
<h3>caseStateInvariant</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseStateInvariant</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>State Invariant</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>State Invariant</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseReplyAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction)">
<h3>caseReplyAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseReplyAction</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Reply Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Reply Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseAcceptEventAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">
<h3>caseAcceptEventAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseAcceptEventAction</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Accept Event Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Accept Event Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseOutputPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin)">
<h3>caseOutputPin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseOutputPin</span><wbr/><span class="parameters">(<a href="../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Output Pin</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Output Pin</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseClause(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">
<h3>caseClause</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseClause</span><wbr/><span class="parameters">(<a href="../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Clause</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Clause</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseConditionalNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode)">
<h3>caseConditionalNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseConditionalNode</span><wbr/><span class="parameters">(<a href="../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Conditional Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Conditional Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseStructuredActivityNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">
<h3>caseStructuredActivityNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseStructuredActivityNode</span><wbr/><span class="parameters">(<a href="../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Structured Activity Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Structured Activity Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseActivityGroup(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup)">
<h3>caseActivityGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseActivityGroup</span><wbr/><span class="parameters">(<a href="../activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity Group</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Activity Group</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseActivityEdge(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)">
<h3>caseActivityEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseActivityEdge</span><wbr/><span class="parameters">(<a href="../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity Edge</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Activity Edge</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">
<h3>caseActivity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseActivity</span><wbr/><span class="parameters">(<a href="../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Activity</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseActivityPartition(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ActivityPartition)">
<h3>caseActivityPartition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseActivityPartition</span><wbr/><span class="parameters">(<a href="../activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity Partition</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Activity Partition</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseVariable(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Variable)">
<h3>caseVariable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseVariable</span><wbr/><span class="parameters">(<a href="../activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Variable</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Variable</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.VariableAction)">
<h3>caseVariableAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseVariableAction</span><wbr/><span class="parameters">(<a href="../actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">VariableAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Variable Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Variable Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInterruptibleActivityRegion(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.InterruptibleActivityRegion)">
<h3>caseInterruptibleActivityRegion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInterruptibleActivityRegion</span><wbr/><span class="parameters">(<a href="../activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interruptible Activity Region</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Interruptible Activity Region</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseLoopNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">
<h3>caseLoopNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseLoopNode</span><wbr/><span class="parameters">(<a href="../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Loop Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Loop Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseOpaqueAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction)">
<h3>caseOpaqueAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseOpaqueAction</span><wbr/><span class="parameters">(<a href="../actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Opaque Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Opaque Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseCallAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallAction)">
<h3>caseCallAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseCallAction</span><wbr/><span class="parameters">(<a href="../actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Call Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Call Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseClearStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearStructuralFeatureAction)">
<h3>caseClearStructuralFeatureAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseClearStructuralFeatureAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Clear Structural Feature Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Clear Structural Feature Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseCreateLinkObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.CreateLinkObjectAction)">
<h3>caseCreateLinkObjectAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseCreateLinkObjectAction</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Create Link Object Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Create Link Object Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseCreateLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateLinkAction)">
<h3>caseCreateLinkAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseCreateLinkAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Create Link Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Create Link Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseWriteLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteLinkAction)">
<h3>caseWriteLinkAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseWriteLinkAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteLinkAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Write Link Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Write Link Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction)">
<h3>caseLinkAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseLinkAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Link Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Link Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseLinkEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndData)">
<h3>caseLinkEndData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseLinkEndData</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Link End Data</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Link End Data</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseQualifierValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.QualifierValue)">
<h3>caseQualifierValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseQualifierValue</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Qualifier Value</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Qualifier Value</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseLinkEndCreationData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndCreationData)">
<h3>caseLinkEndCreationData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseLinkEndCreationData</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Link End Creation Data</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Link End Creation Data</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseCreateObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateObjectAction)">
<h3>caseCreateObjectAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseCreateObjectAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Create Object Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Create Object Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseReadExtentAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadExtentAction)">
<h3>caseReadExtentAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseReadExtentAction</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Extent Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Read Extent Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseReadIsClassifiedObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction)">
<h3>caseReadIsClassifiedObjectAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseReadIsClassifiedObjectAction</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Is Classified Object Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Read Is Classified Object Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseReadLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadLinkAction)">
<h3>caseReadLinkAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseReadLinkAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Link Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Read Link Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseReadLinkObjectEndAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction)">
<h3>caseReadLinkObjectEndAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseReadLinkObjectEndAction</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Link Object End Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Read Link Object End Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseReadLinkObjectEndQualifierAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction)">
<h3>caseReadLinkObjectEndQualifierAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseReadLinkObjectEndQualifierAction</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Link Object End Qualifier Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Read Link Object End Qualifier Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseReadSelfAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadSelfAction)">
<h3>caseReadSelfAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseReadSelfAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Self Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Read Self Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseReadStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadStructuralFeatureAction)">
<h3>caseReadStructuralFeatureAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseReadStructuralFeatureAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Structural Feature Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Read Structural Feature Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseReadVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ReadVariableAction)">
<h3>caseReadVariableAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseReadVariableAction</span><wbr/><span class="parameters">(<a href="../actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Read Variable Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Read Variable Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseReduceAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction)">
<h3>caseReduceAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseReduceAction</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Reduce Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Reduce Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTestIdentityAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction)">
<h3>caseTestIdentityAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTestIdentityAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Test Identity Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Test Identity Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseUnmarshallAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction)">
<h3>caseUnmarshallAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseUnmarshallAction</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Unmarshall Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Unmarshall Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseValueSpecificationAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction)">
<h3>caseValueSpecificationAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseValueSpecificationAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Value Specification Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Value Specification Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseWriteStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction)">
<h3>caseWriteStructuralFeatureAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseWriteStructuralFeatureAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Write Structural Feature Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Write Structural Feature Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseAcceptCallAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptCallAction)">
<h3>caseAcceptCallAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseAcceptCallAction</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Accept Call Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Accept Call Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInterfaceRealization(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.InterfaceRealization)">
<h3>caseInterfaceRealization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInterfaceRealization</span><wbr/><span class="parameters">(<a href="../classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interface Realization</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Interface Realization</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseRealization(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Realization)">
<h3>caseRealization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseRealization</span><wbr/><span class="parameters">(<a href="../classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Realization</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Realization</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseAbstraction(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Abstraction)">
<h3>caseAbstraction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseAbstraction</span><wbr/><span class="parameters">(<a href="../classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Abstraction</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Abstraction</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseOpaqueExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression)">
<h3>caseOpaqueExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseOpaqueExpression</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Opaque Expression</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Opaque Expression</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseComponent(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)">
<h3>caseComponent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseComponent</span><wbr/><span class="parameters">(<a href="../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Component</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Component</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseComponentRealization(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.ComponentRealization)">
<h3>caseComponentRealization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseComponentRealization</span><wbr/><span class="parameters">(<a href="../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Component Realization</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Component Realization</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseOperationTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.OperationTemplateParameter)">
<h3>caseOperationTemplateParameter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseOperationTemplateParameter</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Operation Template Parameter</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Operation Template Parameter</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseCallEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallEvent)">
<h3>caseCallEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseCallEvent</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Call Event</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Call Event</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseCallOperationAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallOperationAction)">
<h3>caseCallOperationAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseCallOperationAction</span><wbr/><span class="parameters">(<a href="../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Call Operation Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Call Operation Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseArtifact(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact)">
<h3>caseArtifact</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseArtifact</span><wbr/><span class="parameters">(<a href="../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Artifact</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Artifact</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDeployedArtifact(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeployedArtifact)">
<h3>caseDeployedArtifact</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDeployedArtifact</span><wbr/><span class="parameters">(<a href="../deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeployedArtifact</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Deployed Artifact</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Deployed Artifact</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDeployment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Deployment)">
<h3>caseDeployment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDeployment</span><wbr/><span class="parameters">(<a href="../deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Deployment</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Deployment</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDeploymentSpecification(com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments.DeploymentSpecification)">
<h3>caseDeploymentSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDeploymentSpecification</span><wbr/><span class="parameters">(<a href="../deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Deployment Specification</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Deployment Specification</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDeploymentTarget(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeploymentTarget)">
<h3>caseDeploymentTarget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDeploymentTarget</span><wbr/><span class="parameters">(<a href="../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Deployment Target</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Deployment Target</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseManifestation(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Manifestation)">
<h3>caseManifestation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseManifestation</span><wbr/><span class="parameters">(<a href="../deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Manifestation</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Manifestation</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Manifestation</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseProtocolTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition)">
<h3>caseProtocolTransition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseProtocolTransition</span><wbr/><span class="parameters">(<a href="../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Protocol Transition</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Protocol Transition</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseExtend(com.nomagic.uml2.ext.magicdraw.mdusecases.Extend)">
<h3>caseExtend</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseExtend</span><wbr/><span class="parameters">(<a href="../mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Extend</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Extend</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">
<h3>caseUseCase</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseUseCase</span><wbr/><span class="parameters">(<a href="../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Use Case</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Use Case</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseExtensionPoint(com.nomagic.uml2.ext.magicdraw.mdusecases.ExtensionPoint)">
<h3>caseExtensionPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseExtensionPoint</span><wbr/><span class="parameters">(<a href="../mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPoint</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Extension Point</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Extension Point</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInclude(com.nomagic.uml2.ext.magicdraw.mdusecases.Include)">
<h3>caseInclude</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInclude</span><wbr/><span class="parameters">(<a href="../mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Include</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Include</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Include</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseExceptionHandler(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExceptionHandler)">
<h3>caseExceptionHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseExceptionHandler</span><wbr/><span class="parameters">(<a href="../activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Exception Handler</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Exception Handler</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseLinkEndDestructionData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndDestructionData)">
<h3>caseLinkEndDestructionData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseLinkEndDestructionData</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Link End Destruction Data</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Link End Destruction Data</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDestroyLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyLinkAction)">
<h3>caseDestroyLinkAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDestroyLinkAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Destroy Link Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Destroy Link Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseRaiseExceptionAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RaiseExceptionAction)">
<h3>caseRaiseExceptionAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseRaiseExceptionAction</span><wbr/><span class="parameters">(<a href="../actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Raise Exception Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Raise Exception Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseAddStructuralFeatureValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.AddStructuralFeatureValueAction)">
<h3>caseAddStructuralFeatureValueAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseAddStructuralFeatureValueAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Add Structural Feature Value Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Add Structural Feature Value Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseAddVariableValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.AddVariableValueAction)">
<h3>caseAddVariableValueAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseAddVariableValueAction</span><wbr/><span class="parameters">(<a href="../actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Add Variable Value Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Add Variable Value Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseWriteVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.WriteVariableAction)">
<h3>caseWriteVariableAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseWriteVariableAction</span><wbr/><span class="parameters">(<a href="../actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Write Variable Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Write Variable Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseClearAssociationAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearAssociationAction)">
<h3>caseClearAssociationAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseClearAssociationAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Clear Association Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Clear Association Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseReclassifyObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReclassifyObjectAction)">
<h3>caseReclassifyObjectAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseReclassifyObjectAction</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Reclassify Object Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Reclassify Object Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseStartClassifierBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartClassifierBehaviorAction)">
<h3>caseStartClassifierBehaviorAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseStartClassifierBehaviorAction</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Start Classifier Behavior Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Start Classifier Behavior Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseStartObjectBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartObjectBehaviorAction)">
<h3>caseStartObjectBehaviorAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseStartObjectBehaviorAction</span><wbr/><span class="parameters">(<a href="../actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Start Object Behavior Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Start Object Behavior Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseRemoveStructuralFeatureValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.RemoveStructuralFeatureValueAction)">
<h3>caseRemoveStructuralFeatureValueAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseRemoveStructuralFeatureValueAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Remove Structural Feature Value Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Remove Structural Feature Value Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseRemoveVariableValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RemoveVariableValueAction)">
<h3>caseRemoveVariableValueAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseRemoveVariableValueAction</span><wbr/><span class="parameters">(<a href="../actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Remove Variable Value Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Remove Variable Value Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseSendObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction)">
<h3>caseSendObjectAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseSendObjectAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Send Object Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Send Object Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDestroyObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyObjectAction)">
<h3>caseDestroyObjectAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDestroyObjectAction</span><wbr/><span class="parameters">(<a href="../actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Destroy Object Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Destroy Object Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseChangeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent)">
<h3>caseChangeEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseChangeEvent</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Change Event</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Change Event</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration)">
<h3>caseDuration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDuration</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Duration</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Duration</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Observation)">
<h3>caseObservation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseObservation</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Observation</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Observation</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Observation</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)">
<h3>caseTimeExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTimeExpression</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Time Expression</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Time Expression</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval)">
<h3>caseTimeInterval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTimeInterval</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Time Interval</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Time Interval</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Interval)">
<h3>caseInterval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInterval</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interval</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Interval</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseIntervalConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint)">
<h3>caseIntervalConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseIntervalConstraint</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Interval Constraint</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Interval Constraint</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTimeConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint)">
<h3>caseTimeConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTimeConstraint</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Time Constraint</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Time Constraint</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTimeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.TimeEvent)">
<h3>caseTimeEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTimeEvent</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEvent</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Time Event</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Time Event</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval)">
<h3>caseDurationInterval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDurationInterval</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Duration Interval</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Duration Interval</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDurationConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint)">
<h3>caseDurationConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDurationConstraint</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Duration Constraint</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Duration Constraint</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseJoinNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode)">
<h3>caseJoinNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseJoinNode</span><wbr/><span class="parameters">(<a href="../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Join Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Join Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseControlNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ControlNode)">
<h3>caseControlNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseControlNode</span><wbr/><span class="parameters">(<a href="../activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Control Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Control Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression)">
<h3>caseExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseExpression</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Expression</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Expression</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseValuePin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin)">
<h3>caseValuePin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseValuePin</span><wbr/><span class="parameters">(<a href="../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Value Pin</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Value Pin</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseActivityParameterNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode)">
<h3>caseActivityParameterNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseActivityParameterNode</span><wbr/><span class="parameters">(<a href="../activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity Parameter Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Activity Parameter Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseBehaviorExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.BehaviorExecutionSpecification)">
<h3>caseBehaviorExecutionSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseBehaviorExecutionSpecification</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecification</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Behavior Execution Specification</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Behavior Execution Specification</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseCallBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction)">
<h3>caseCallBehaviorAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseCallBehaviorAction</span><wbr/><span class="parameters">(<a href="../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Call Behavior Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Call Behavior Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDecisionNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.DecisionNode)">
<h3>caseDecisionNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDecisionNode</span><wbr/><span class="parameters">(<a href="../activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Decision Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Decision Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseObjectFlow(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectFlow)">
<h3>caseObjectFlow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseObjectFlow</span><wbr/><span class="parameters">(<a href="../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Object Flow</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Object Flow</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseExtension(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension)">
<h3>caseExtension</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseExtension</span><wbr/><span class="parameters">(<a href="../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Extension</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Extension</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseExtensionEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.ExtensionEnd)">
<h3>caseExtensionEnd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseExtensionEnd</span><wbr/><span class="parameters">(<a href="../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Extension End</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Extension End</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseImage(com.nomagic.uml2.ext.magicdraw.mdprofiles.Image)">
<h3>caseImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseImage</span><wbr/><span class="parameters">(<a href="../mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Image</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Image</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="casePackageMerge(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageMerge)">
<h3>casePackageMerge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">casePackageMerge</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageMerge</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Package Merge</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Package Merge</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseProfileApplication(com.nomagic.uml2.ext.magicdraw.mdprofiles.ProfileApplication)">
<h3>caseProfileApplication</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseProfileApplication</span><wbr/><span class="parameters">(<a href="../mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplication</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Profile Application</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Profile Application</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="casePackageImport(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageImport)">
<h3>casePackageImport</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">casePackageImport</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Package Import</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Package Import</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>caseDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDiagram</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Diagram</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Diagram</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseGeneralization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Generalization)">
<h3>caseGeneralization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseGeneralization</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Generalization</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Generalization</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseGeneralizationSet(com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes.GeneralizationSet)">
<h3>caseGeneralizationSet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseGeneralizationSet</span><wbr/><span class="parameters">(<a href="../classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Generalization Set</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Generalization Set</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseRedefinableTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)">
<h3>caseRedefinableTemplateSignature</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseRedefinableTemplateSignature</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Redefinable Template Signature</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Redefinable Template Signature</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseSubstitution(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Substitution)">
<h3>caseSubstitution</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseSubstitution</span><wbr/><span class="parameters">(<a href="../classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Substitution</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Substitution</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseClassifierTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)">
<h3>caseClassifierTemplateParameter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseClassifierTemplateParameter</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Classifier Template Parameter</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Classifier Template Parameter</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInformationItem(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows.InformationItem)">
<h3>caseInformationItem</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInformationItem</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Information Item</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Information Item</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTemplateParameterSubstitution(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">
<h3>caseTemplateParameterSubstitution</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTemplateParameterSubstitution</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Template Parameter Substitution</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Template Parameter Substitution</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInstanceValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceValue)">
<h3>caseInstanceValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInstanceValue</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Instance Value</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Instance Value</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementValue)">
<h3>caseElementValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseElementValue</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Element Value</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Element Value</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseStringExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">
<h3>caseStringExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseStringExpression</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>String Expression</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>String Expression</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDurationObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationObservation)">
<h3>caseDurationObservation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDurationObservation</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Duration Observation</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Duration Observation</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseTimeObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeObservation)">
<h3>caseTimeObservation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseTimeObservation</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Time Observation</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Time Observation</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseConsiderIgnoreFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.ConsiderIgnoreFragment)">
<h3>caseConsiderIgnoreFragment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseConsiderIgnoreFragment</span><wbr/><span class="parameters">(<a href="../interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragment</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Consider Ignore Fragment</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Consider Ignore Fragment</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseSequenceNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode)">
<h3>caseSequenceNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseSequenceNode</span><wbr/><span class="parameters">(<a href="../activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Sequence Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Sequence Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseActionExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ActionExecutionSpecification)">
<h3>caseActionExecutionSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseActionExecutionSpecification</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecification</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Action Execution Specification</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Action Execution Specification</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseActionInputPin(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin)">
<h3>caseActionInputPin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseActionInputPin</span><wbr/><span class="parameters">(<a href="../actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Action Input Pin</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Action Input Pin</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseLiteralString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralString)">
<h3>caseLiteralString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseLiteralString</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralString</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal String</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Literal String</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseLiteralSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralSpecification)">
<h3>caseLiteralSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseLiteralSpecification</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralSpecification</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal Specification</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Literal Specification</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDataStoreNode(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.DataStoreNode)">
<h3>caseDataStoreNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDataStoreNode</span><wbr/><span class="parameters">(<a href="../activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Data Store Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Data Store Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseCentralBufferNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.CentralBufferNode)">
<h3>caseCentralBufferNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseCentralBufferNode</span><wbr/><span class="parameters">(<a href="../activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Central Buffer Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Central Buffer Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseInitialNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.InitialNode)">
<h3>caseInitialNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseInitialNode</span><wbr/><span class="parameters">(<a href="../activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Initial Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Initial Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDevice(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Device)">
<h3>caseDevice</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDevice</span><wbr/><span class="parameters">(<a href="../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Device</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Device</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseNode(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Node)">
<h3>caseNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseNode</span><wbr/><span class="parameters">(<a href="../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseAssociationClass(com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses.AssociationClass)">
<h3>caseAssociationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseAssociationClass</span><wbr/><span class="parameters">(<a href="../classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Association Class</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Association Class</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseActor(com.nomagic.uml2.ext.magicdraw.mdusecases.Actor)">
<h3>caseActor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseActor</span><wbr/><span class="parameters">(<a href="../mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Actor</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Actor</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseExecutionEnvironment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.ExecutionEnvironment)">
<h3>caseExecutionEnvironment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseExecutionEnvironment</span><wbr/><span class="parameters">(<a href="../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Execution Environment</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Execution Environment</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseFunctionBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.FunctionBehavior)">
<h3>caseFunctionBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseFunctionBehavior</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Function Behavior</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Function Behavior</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseOpaqueBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.OpaqueBehavior)">
<h3>caseOpaqueBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseOpaqueBehavior</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Opaque Behavior</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Opaque Behavior</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.FinalNode)">
<h3>caseFinalNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseFinalNode</span><wbr/><span class="parameters">(<a href="../activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FinalNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Final Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Final Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseActivityFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityFinalNode)">
<h3>caseActivityFinalNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseActivityFinalNode</span><wbr/><span class="parameters">(<a href="../activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Activity Final Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Activity Final Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseFlowFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.FlowFinalNode)">
<h3>caseFlowFinalNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseFlowFinalNode</span><wbr/><span class="parameters">(<a href="../activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Flow Final Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Flow Final Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseLiteralReal(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralReal)">
<h3>caseLiteralReal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseLiteralReal</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralReal</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal Real</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Literal Real</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseForkNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ForkNode)">
<h3>caseForkNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseForkNode</span><wbr/><span class="parameters">(<a href="../activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Fork Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Fork Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseControlFlow(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ControlFlow)">
<h3>caseControlFlow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseControlFlow</span><wbr/><span class="parameters">(<a href="../activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Control Flow</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Control Flow</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseUsage(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Usage)">
<h3>caseUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseUsage</span><wbr/><span class="parameters">(<a href="../classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Usage</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Usage</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Usage</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseLiteralUnlimitedNatural(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralUnlimitedNatural)">
<h3>caseLiteralUnlimitedNatural</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseLiteralUnlimitedNatural</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNatural</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal Unlimited Natural</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Literal Unlimited Natural</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseLiteralInteger(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralInteger)">
<h3>caseLiteralInteger</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseLiteralInteger</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralInteger</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal Integer</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Literal Integer</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseEnumeration(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration)">
<h3>caseEnumeration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseEnumeration</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Enumeration</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Enumeration</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseEnumerationLiteral(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>caseEnumerationLiteral</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseEnumerationLiteral</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Enumeration Literal</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Enumeration Literal</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseExpansionNode(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExpansionNode)">
<h3>caseExpansionNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseExpansionNode</span><wbr/><span class="parameters">(<a href="../activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Expansion Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Expansion Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseExpansionRegion(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExpansionRegion)">
<h3>caseExpansionRegion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseExpansionRegion</span><wbr/><span class="parameters">(<a href="../activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Expansion Region</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Expansion Region</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseCommunicationPath(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.CommunicationPath)">
<h3>caseCommunicationPath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseCommunicationPath</span><wbr/><span class="parameters">(<a href="../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Communication Path</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Communication Path</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="casePrimitiveType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PrimitiveType)">
<h3>casePrimitiveType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">casePrimitiveType</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Primitive Type</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Primitive Type</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseFinalState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.FinalState)">
<h3>caseFinalState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseFinalState</span><wbr/><span class="parameters">(<a href="../statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Final State</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Final State</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseAnyReceiveEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.AnyReceiveEvent)">
<h3>caseAnyReceiveEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseAnyReceiveEvent</span><wbr/><span class="parameters">(<a href="../commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEvent</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Any Receive Event</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Any Receive Event</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseMergeNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.MergeNode)">
<h3>caseMergeNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseMergeNode</span><wbr/><span class="parameters">(<a href="../activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Merge Node</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Merge Node</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseContinuation(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Continuation)">
<h3>caseContinuation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseContinuation</span><wbr/><span class="parameters">(<a href="../interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Continuation</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Continuation</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Continuation</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseLiteralNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralNull)">
<h3>caseLiteralNull</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseLiteralNull</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNull</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal Null</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Literal Null</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseMessageOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageOccurrenceSpecification)">
<h3>caseMessageOccurrenceSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseMessageOccurrenceSpecification</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecification</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Message Occurrence Specification</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Message Occurrence Specification</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseLiteralBoolean(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralBoolean)">
<h3>caseLiteralBoolean</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseLiteralBoolean</span><wbr/><span class="parameters">(<a href="../classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBoolean</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Literal Boolean</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Literal Boolean</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDestructionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.DestructionOccurrenceSpecification)">
<h3>caseDestructionOccurrenceSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseDestructionOccurrenceSpecification</span><wbr/><span class="parameters">(<a href="../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Destruction Occurrence Specification</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Destruction Occurrence Specification</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseModel(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model)">
<h3>caseModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseModel</span><wbr/><span class="parameters">(<a href="../auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Model</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Model</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseClearVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ClearVariableAction)">
<h3>caseClearVariableAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseClearVariableAction</span><wbr/><span class="parameters">(<a href="../actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Clear Variable Action</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Clear Variable Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseModelObject(com.nomagic.uml2.ext.magicdraw.base.ModelObject)">
<h3>caseModelObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseModelObject</span><wbr/><span class="parameters">(<a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Model Object</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Model Object</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseMDObject(com.nomagic.magicdraw.foundation.MDObject)">
<h3>caseMDObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">caseMDObject</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>MD Object</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>MD Object</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(EObject)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="defaultCase(org.eclipse.emf.ecore.EObject)">
<h3>defaultCase</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UMLSwitch.html" title="type parameter in UMLSwitch">T</a></span> <span class="element-name">defaultCase</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EObject object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>EObject</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch, but this is the last case anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>EObject</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#doSwitch(org.eclipse.emf.ecore.EObject)"><code>doSwitch(org.eclipse.emf.ecore.EObject)</code></a></li>
</ul>
</dd>
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
