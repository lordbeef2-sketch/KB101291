# JAVA OPENAPI: ClassTypeHierarchyVisitor (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/uml2/ext/jmi/reflect/ClassTypeHierarchyVisitor.html
- source_path: `com/nomagic/uml2/ext/jmi/reflect/ClassTypeHierarchyVisitor.html`
- source_sha256: `3dd3e4dc1c9c00e0bb7dbe83aba215251423a07f9520bc20fe80a34a5e8e4b6b`
- captured_utc: `2026-07-14T16:56:13.772663+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.reflect](package-summary.html)

## Class ClassTypeHierarchyVisitor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.jmi.reflect.ClassTypeHierarchyVisitor

public classClassTypeHierarchyVisitor
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ClassTypeHierarchyVisitor](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`final void`
`[visit](#visit(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> type)`

`void`
`[visitAbstraction](#visitAbstraction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Abstraction`](../../magicdraw/classes/mddependencies/Abstraction.html).
`void`
`[visitAcceptCallAction](#visitAcceptCallAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`AcceptCallAction`](../../magicdraw/actions/mdcompleteactions/AcceptCallAction.html).
`void`
`[visitAcceptEventAction](#visitAcceptEventAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`AcceptEventAction`](../../magicdraw/actions/mdcompleteactions/AcceptEventAction.html).
`void`
`[visitAction](#visitAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Action`](../../magicdraw/actions/mdbasicactions/Action.html).
`void`
`[visitActionExecutionSpecification](#visitActionExecutionSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ActionExecutionSpecification`](../../magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html).
`void`
`[visitActionInputPin](#visitActionInputPin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ActionInputPin`](../../magicdraw/actions/mdstructuredactions/ActionInputPin.html).
`void`
`[visitActivity](#visitActivity(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Activity`](../../magicdraw/activities/mdfundamentalactivities/Activity.html).
`void`
`[visitActivityEdge](#visitActivityEdge(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ActivityEdge`](../../magicdraw/activities/mdbasicactivities/ActivityEdge.html).
`void`
`[visitActivityFinalNode](#visitActivityFinalNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ActivityFinalNode`](../../magicdraw/activities/mdbasicactivities/ActivityFinalNode.html).
`void`
`[visitActivityGroup](#visitActivityGroup(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ActivityGroup`](../../magicdraw/activities/mdfundamentalactivities/ActivityGroup.html).
`void`
`[visitActivityNode](#visitActivityNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ActivityNode`](../../magicdraw/activities/mdfundamentalactivities/ActivityNode.html).
`void`
`[visitActivityParameterNode](#visitActivityParameterNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ActivityParameterNode`](../../magicdraw/activities/mdbasicactivities/ActivityParameterNode.html).
`void`
`[visitActivityPartition](#visitActivityPartition(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ActivityPartition`](../../magicdraw/activities/mdintermediateactivities/ActivityPartition.html).
`void`
`[visitActor](#visitActor(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Actor`](../../magicdraw/mdusecases/Actor.html).
`void`
`[visitAddStructuralFeatureValueAction](#visitAddStructuralFeatureValueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`AddStructuralFeatureValueAction`](../../magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html).
`void`
`[visitAddVariableValueAction](#visitAddVariableValueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`AddVariableValueAction`](../../magicdraw/actions/mdstructuredactions/AddVariableValueAction.html).
`void`
`[visitAnyReceiveEvent](#visitAnyReceiveEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`AnyReceiveEvent`](../../magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html).
`void`
`[visitArtifact](#visitArtifact(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Artifact`](../../magicdraw/deployments/mdartifacts/Artifact.html).
`void`
`[visitAssociation](#visitAssociation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Association`](../../magicdraw/classes/mdkernel/Association.html).
`void`
`[visitAssociationClass](#visitAssociationClass(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`AssociationClass`](../../magicdraw/classes/mdassociationclasses/AssociationClass.html).
`void`
`[visitBehavior](#visitBehavior(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Behavior`](../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html).
`void`
`[visitBehavioralFeature](#visitBehavioralFeature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`BehavioralFeature`](../../magicdraw/classes/mdkernel/BehavioralFeature.html).
`void`
`[visitBehavioredClassifier](#visitBehavioredClassifier(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`BehavioredClassifier`](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html).
`void`
`[visitBehaviorExecutionSpecification](#visitBehaviorExecutionSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`BehaviorExecutionSpecification`](../../magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html).
`void`
`[visitBooleanTaggedValue](#visitBooleanTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`

`void`
`[visitBroadcastSignalAction](#visitBroadcastSignalAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`BroadcastSignalAction`](../../magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html).
`void`
`[visitCallAction](#visitCallAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`CallAction`](../../magicdraw/actions/mdbasicactions/CallAction.html).
`void`
`[visitCallBehaviorAction](#visitCallBehaviorAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`CallBehaviorAction`](../../magicdraw/actions/mdbasicactions/CallBehaviorAction.html).
`void`
`[visitCallEvent](#visitCallEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`CallEvent`](../../magicdraw/commonbehaviors/mdcommunications/CallEvent.html).
`void`
`[visitCallOperationAction](#visitCallOperationAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`CallOperationAction`](../../magicdraw/actions/mdbasicactions/CallOperationAction.html).
`void`
`[visitCentralBufferNode](#visitCentralBufferNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`CentralBufferNode`](../../magicdraw/activities/mdintermediateactivities/CentralBufferNode.html).
`void`
`[visitChangeEvent](#visitChangeEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ChangeEvent`](../../magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html).
`void`
`[visitClass](#visitClass(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Class`](../../magicdraw/classes/mdkernel/Class.html).
`void`
`[visitClassifier](#visitClassifier(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Classifier`](../../magicdraw/classes/mdkernel/Classifier.html).
`void`
`[visitClassifierTemplateParameter](#visitClassifierTemplateParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ClassifierTemplateParameter`](../../magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html).
`void`
`[visitClause](#visitClause(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Clause`](../../magicdraw/activities/mdstructuredactivities/Clause.html).
`void`
`[visitClearAssociationAction](#visitClearAssociationAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ClearAssociationAction`](../../magicdraw/actions/mdintermediateactions/ClearAssociationAction.html).
`void`
`[visitClearStructuralFeatureAction](#visitClearStructuralFeatureAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ClearStructuralFeatureAction`](../../magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html).
`void`
`[visitClearVariableAction](#visitClearVariableAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ClearVariableAction`](../../magicdraw/actions/mdstructuredactions/ClearVariableAction.html).
`void`
`[visitCollaboration](#visitCollaboration(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Collaboration`](../../magicdraw/compositestructures/mdcollaborations/Collaboration.html).
`void`
`[visitCollaborationUse](#visitCollaborationUse(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`CollaborationUse`](../../magicdraw/compositestructures/mdcollaborations/CollaborationUse.html).
`void`
`[visitCombinedFragment](#visitCombinedFragment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`CombinedFragment`](../../magicdraw/interactions/mdfragments/CombinedFragment.html).
`void`
`[visitComment](#visitComment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Comment`](../../magicdraw/classes/mdkernel/Comment.html).
`void`
`[visitCommunicationPath](#visitCommunicationPath(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`CommunicationPath`](../../magicdraw/deployments/mdnodes/CommunicationPath.html).
`void`
`[visitComponent](#visitComponent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Component`](../../magicdraw/components/mdbasiccomponents/Component.html).
`void`
`[visitComponentRealization](#visitComponentRealization(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ComponentRealization`](../../magicdraw/components/mdbasiccomponents/ComponentRealization.html).
`void`
`[visitConditionalNode](#visitConditionalNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ConditionalNode`](../../magicdraw/activities/mdstructuredactivities/ConditionalNode.html).
`void`
`[visitConnectableElement](#visitConnectableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ConnectableElement`](../../magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html).
`void`
`[visitConnectableElementTemplateParameter](#visitConnectableElementTemplateParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ConnectableElementTemplateParameter`](../../magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html).
`void`
`[visitConnectionPointReference](#visitConnectionPointReference(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ConnectionPointReference`](../../magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html).
`void`
`[visitConnector](#visitConnector(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Connector`](../../magicdraw/compositestructures/mdinternalstructures/Connector.html).
`void`
`[visitConnectorEnd](#visitConnectorEnd(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ConnectorEnd`](../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html).
`void`
`[visitConsiderIgnoreFragment](#visitConsiderIgnoreFragment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ConsiderIgnoreFragment`](../../magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html).
`void`
`[visitConstraint](#visitConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Constraint`](../../magicdraw/classes/mdkernel/Constraint.html).
`void`
`[visitContinuation](#visitContinuation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Continuation`](../../magicdraw/interactions/mdfragments/Continuation.html).
`void`
`[visitControlFlow](#visitControlFlow(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ControlFlow`](../../magicdraw/activities/mdbasicactivities/ControlFlow.html).
`void`
`[visitControlNode](#visitControlNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ControlNode`](../../magicdraw/activities/mdbasicactivities/ControlNode.html).
`void`
`[visitCreateLinkAction](#visitCreateLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`CreateLinkAction`](../../magicdraw/actions/mdintermediateactions/CreateLinkAction.html).
`void`
`[visitCreateLinkObjectAction](#visitCreateLinkObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`CreateLinkObjectAction`](../../magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html).
`void`
`[visitCreateObjectAction](#visitCreateObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`CreateObjectAction`](../../magicdraw/actions/mdintermediateactions/CreateObjectAction.html).
`void`
`[visitDataStoreNode](#visitDataStoreNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`DataStoreNode`](../../magicdraw/activities/mdcompleteactivities/DataStoreNode.html).
`void`
`[visitDataType](#visitDataType(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`DataType`](../../magicdraw/classes/mdkernel/DataType.html).
`void`
`[visitDecisionNode](#visitDecisionNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`DecisionNode`](../../magicdraw/activities/mdintermediateactivities/DecisionNode.html).
`void`
`[visitDependency](#visitDependency(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Dependency`](../../magicdraw/classes/mddependencies/Dependency.html).
`void`
`[visitDeployedArtifact](#visitDeployedArtifact(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`DeployedArtifact`](../../magicdraw/deployments/mdnodes/DeployedArtifact.html).
`void`
`[visitDeployment](#visitDeployment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Deployment`](../../magicdraw/deployments/mdnodes/Deployment.html).
`void`
`[visitDeploymentSpecification](#visitDeploymentSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`DeploymentSpecification`](../../magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html).
`void`
`[visitDeploymentTarget](#visitDeploymentTarget(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`DeploymentTarget`](../../magicdraw/deployments/mdnodes/DeploymentTarget.html).
`void`
`[visitDestroyLinkAction](#visitDestroyLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`DestroyLinkAction`](../../magicdraw/actions/mdintermediateactions/DestroyLinkAction.html).
`void`
`[visitDestroyObjectAction](#visitDestroyObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`DestroyObjectAction`](../../magicdraw/actions/mdintermediateactions/DestroyObjectAction.html).
`void`
`[visitDestructionOccurrenceSpecification](#visitDestructionOccurrenceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`DestructionOccurrenceSpecification`](../../magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html).
`void`
`[visitDevice](#visitDevice(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Device`](../../magicdraw/deployments/mdnodes/Device.html).
`void`
`[visitDiagram](#visitDiagram(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Diagram`](../../magicdraw/classes/mdkernel/Diagram.html).
`void`
`[visitDirectedRelationship](#visitDirectedRelationship(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`DirectedRelationship`](../../magicdraw/classes/mdkernel/DirectedRelationship.html).
`void`
`[visitDuration](#visitDuration(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Duration`](../../magicdraw/commonbehaviors/mdsimpletime/Duration.html).
`void`
`[visitDurationConstraint](#visitDurationConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`DurationConstraint`](../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html).
`void`
`[visitDurationInterval](#visitDurationInterval(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`DurationInterval`](../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html).
`void`
`[visitDurationObservation](#visitDurationObservation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`DurationObservation`](../../magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html).
`void`
`[visitElement](#visitElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Element`](../../magicdraw/classes/mdkernel/Element.html).
`void`
`[visitElementImport](#visitElementImport(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ElementImport`](../../magicdraw/classes/mdkernel/ElementImport.html).
`void`
`[visitElementTaggedValue](#visitElementTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`

`void`
`[visitElementValue](#visitElementValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ElementValue`](../../magicdraw/classes/mdkernel/ElementValue.html).
`void`
`[visitEncapsulatedClassifier](#visitEncapsulatedClassifier(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`EncapsulatedClassifier`](../../magicdraw/compositestructures/mdports/EncapsulatedClassifier.html).
`void`
`[visitEnumeration](#visitEnumeration(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Enumeration`](../../magicdraw/classes/mdkernel/Enumeration.html).
`void`
`[visitEnumerationLiteral](#visitEnumerationLiteral(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`EnumerationLiteral`](../../magicdraw/classes/mdkernel/EnumerationLiteral.html).
`void`
`[visitEvent](#visitEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Event`](../../magicdraw/commonbehaviors/mdcommunications/Event.html).
`void`
`[visitExceptionHandler](#visitExceptionHandler(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ExceptionHandler`](../../magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html).
`void`
`[visitExecutableNode](#visitExecutableNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ExecutableNode`](../../magicdraw/activities/mdstructuredactivities/ExecutableNode.html).
`void`
`[visitExecutionEnvironment](#visitExecutionEnvironment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ExecutionEnvironment`](../../magicdraw/deployments/mdnodes/ExecutionEnvironment.html).
`void`
`[visitExecutionOccurrenceSpecification](#visitExecutionOccurrenceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ExecutionOccurrenceSpecification`](../../magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html).
`void`
`[visitExecutionSpecification](#visitExecutionSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ExecutionSpecification`](../../magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html).
`void`
`[visitExpansionNode](#visitExpansionNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ExpansionNode`](../../magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html).
`void`
`[visitExpansionRegion](#visitExpansionRegion(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ExpansionRegion`](../../magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html).
`void`
`[visitExpression](#visitExpression(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Expression`](../../magicdraw/classes/mdkernel/Expression.html).
`void`
`[visitExtend](#visitExtend(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Extend`](../../magicdraw/mdusecases/Extend.html).
`void`
`[visitExtension](#visitExtension(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Extension`](../../magicdraw/mdprofiles/Extension.html).
`void`
`[visitExtensionEnd](#visitExtensionEnd(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ExtensionEnd`](../../magicdraw/mdprofiles/ExtensionEnd.html).
`void`
`[visitExtensionPoint](#visitExtensionPoint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ExtensionPoint`](../../magicdraw/mdusecases/ExtensionPoint.html).
`void`
`[visitFeature](#visitFeature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Feature`](../../magicdraw/classes/mdkernel/Feature.html).
`void`
`[visitFinalNode](#visitFinalNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`FinalNode`](../../magicdraw/activities/mdintermediateactivities/FinalNode.html).
`void`
`[visitFinalState](#visitFinalState(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`FinalState`](../../magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html).
`void`
`[visitFlowFinalNode](#visitFlowFinalNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`FlowFinalNode`](../../magicdraw/activities/mdintermediateactivities/FlowFinalNode.html).
`void`
`[visitForkNode](#visitForkNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ForkNode`](../../magicdraw/activities/mdintermediateactivities/ForkNode.html).
`void`
`[visitFunctionBehavior](#visitFunctionBehavior(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`FunctionBehavior`](../../magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html).
`void`
`[visitGate](#visitGate(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Gate`](../../magicdraw/interactions/mdfragments/Gate.html).
`void`
`[visitGeneralization](#visitGeneralization(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Generalization`](../../magicdraw/classes/mdkernel/Generalization.html).
`void`
`[visitGeneralizationSet](#visitGeneralizationSet(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`GeneralizationSet`](../../magicdraw/classes/mdpowertypes/GeneralizationSet.html).
`void`
`[visitGeneralOrdering](#visitGeneralOrdering(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`GeneralOrdering`](../../magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html).
`void`
`[visitImage](#visitImage(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Image`](../../magicdraw/mdprofiles/Image.html).
`void`
`[visitInclude](#visitInclude(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Include`](../../magicdraw/mdusecases/Include.html).
`void`
`[visitInformationFlow](#visitInformationFlow(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`InformationFlow`](../../magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html).
`void`
`[visitInformationItem](#visitInformationItem(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`InformationItem`](../../magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html).
`void`
`[visitInitialNode](#visitInitialNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`InitialNode`](../../magicdraw/activities/mdbasicactivities/InitialNode.html).
`void`
`[visitInputPin](#visitInputPin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`InputPin`](../../magicdraw/actions/mdbasicactions/InputPin.html).
`void`
`[visitInstanceSpecification](#visitInstanceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`InstanceSpecification`](../../magicdraw/classes/mdkernel/InstanceSpecification.html).
`void`
`[visitInstanceValue](#visitInstanceValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`InstanceValue`](../../magicdraw/classes/mdkernel/InstanceValue.html).
`void`
`[visitIntegerTaggedValue](#visitIntegerTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`

`void`
`[visitInteraction](#visitInteraction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Interaction`](../../magicdraw/interactions/mdbasicinteractions/Interaction.html).
`void`
`[visitInteractionConstraint](#visitInteractionConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`InteractionConstraint`](../../magicdraw/interactions/mdfragments/InteractionConstraint.html).
`void`
`[visitInteractionFragment](#visitInteractionFragment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`InteractionFragment`](../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html).
`void`
`[visitInteractionOperand](#visitInteractionOperand(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`InteractionOperand`](../../magicdraw/interactions/mdfragments/InteractionOperand.html).
`void`
`[visitInteractionUse](#visitInteractionUse(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`InteractionUse`](../../magicdraw/interactions/mdfragments/InteractionUse.html).
`void`
`[visitInterface](#visitInterface(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Interface`](../../magicdraw/classes/mdinterfaces/Interface.html).
`void`
`[visitInterfaceRealization](#visitInterfaceRealization(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`InterfaceRealization`](../../magicdraw/classes/mdinterfaces/InterfaceRealization.html).
`void`
`[visitInterruptibleActivityRegion](#visitInterruptibleActivityRegion(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`InterruptibleActivityRegion`](../../magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html).
`void`
`[visitInterval](#visitInterval(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Interval`](../../magicdraw/commonbehaviors/mdsimpletime/Interval.html).
`void`
`[visitIntervalConstraint](#visitIntervalConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`IntervalConstraint`](../../magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html).
`void`
`[visitInvocationAction](#visitInvocationAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`InvocationAction`](../../magicdraw/actions/mdbasicactions/InvocationAction.html).
`void`
`[visitJoinNode](#visitJoinNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`JoinNode`](../../magicdraw/activities/mdintermediateactivities/JoinNode.html).
`void`
`[visitLifeline](#visitLifeline(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Lifeline`](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html).
`void`
`[visitLinkAction](#visitLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`LinkAction`](../../magicdraw/actions/mdintermediateactions/LinkAction.html).
`void`
`[visitLinkEndCreationData](#visitLinkEndCreationData(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`LinkEndCreationData`](../../magicdraw/actions/mdintermediateactions/LinkEndCreationData.html).
`void`
`[visitLinkEndData](#visitLinkEndData(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`LinkEndData`](../../magicdraw/actions/mdintermediateactions/LinkEndData.html).
`void`
`[visitLinkEndDestructionData](#visitLinkEndDestructionData(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`LinkEndDestructionData`](../../magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html).
`void`
`[visitLiteralBoolean](#visitLiteralBoolean(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`LiteralBoolean`](../../magicdraw/classes/mdkernel/LiteralBoolean.html).
`void`
`[visitLiteralInteger](#visitLiteralInteger(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`LiteralInteger`](../../magicdraw/classes/mdkernel/LiteralInteger.html).
`void`
`[visitLiteralNull](#visitLiteralNull(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`LiteralNull`](../../magicdraw/classes/mdkernel/LiteralNull.html).
`void`
`[visitLiteralReal](#visitLiteralReal(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`LiteralReal`](../../magicdraw/classes/mdkernel/LiteralReal.html).
`void`
`[visitLiteralSpecification](#visitLiteralSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`LiteralSpecification`](../../magicdraw/classes/mdkernel/LiteralSpecification.html).
`void`
`[visitLiteralString](#visitLiteralString(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`LiteralString`](../../magicdraw/classes/mdkernel/LiteralString.html).
`void`
`[visitLiteralUnlimitedNatural](#visitLiteralUnlimitedNatural(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`LiteralUnlimitedNatural`](../../magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html).
`void`
`[visitLoopNode](#visitLoopNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`LoopNode`](../../magicdraw/activities/mdstructuredactivities/LoopNode.html).
`void`
`[visitManifestation](#visitManifestation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Manifestation`](../../magicdraw/deployments/mdartifacts/Manifestation.html).
`void`
`[visitMergeNode](#visitMergeNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`MergeNode`](../../magicdraw/activities/mdintermediateactivities/MergeNode.html).
`void`
`[visitMessage](#visitMessage(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Message`](../../magicdraw/interactions/mdbasicinteractions/Message.html).
`void`
`[visitMessageEnd](#visitMessageEnd(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`MessageEnd`](../../magicdraw/interactions/mdbasicinteractions/MessageEnd.html).
`void`
`[visitMessageEvent](#visitMessageEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`MessageEvent`](../../magicdraw/commonbehaviors/mdcommunications/MessageEvent.html).
`void`
`[visitMessageOccurrenceSpecification](#visitMessageOccurrenceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`MessageOccurrenceSpecification`](../../magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html).
`void`
`[visitModel](#visitModel(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Model`](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html).
`void`
`[visitMultiplicityElement](#visitMultiplicityElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`MultiplicityElement`](../../magicdraw/classes/mdkernel/MultiplicityElement.html).
`void`
`[visitNamedElement](#visitNamedElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`NamedElement`](../../magicdraw/classes/mdkernel/NamedElement.html).
`void`
`[visitNamespace](#visitNamespace(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Namespace`](../../magicdraw/classes/mdkernel/Namespace.html).
`void`
`[visitNode](#visitNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Node`](../../magicdraw/deployments/mdnodes/Node.html).
`void`
`[visitObjectFlow](#visitObjectFlow(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ObjectFlow`](../../magicdraw/activities/mdbasicactivities/ObjectFlow.html).
`void`
`[visitObjectNode](#visitObjectNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ObjectNode`](../../magicdraw/activities/mdbasicactivities/ObjectNode.html).
`void`
`[visitObservation](#visitObservation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Observation`](../../magicdraw/commonbehaviors/mdsimpletime/Observation.html).
`void`
`[visitOccurrenceSpecification](#visitOccurrenceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`OccurrenceSpecification`](../../magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html).
`void`
`[visitOpaqueAction](#visitOpaqueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`OpaqueAction`](../../magicdraw/actions/mdbasicactions/OpaqueAction.html).
`void`
`[visitOpaqueBehavior](#visitOpaqueBehavior(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`OpaqueBehavior`](../../magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html).
`void`
`[visitOpaqueExpression](#visitOpaqueExpression(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`OpaqueExpression`](../../magicdraw/classes/mdkernel/OpaqueExpression.html).
`void`
`[visitOperation](#visitOperation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Operation`](../../magicdraw/classes/mdkernel/Operation.html).
`void`
`[visitOperationTemplateParameter](#visitOperationTemplateParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`OperationTemplateParameter`](../../magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html).
`void`
`[visitOutputPin](#visitOutputPin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`OutputPin`](../../magicdraw/actions/mdbasicactions/OutputPin.html).
`void`
`[visitPackage](#visitPackage(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Package`](../../magicdraw/classes/mdkernel/Package.html).
`void`
`[visitPackageableElement](#visitPackageableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`PackageableElement`](../../magicdraw/classes/mdkernel/PackageableElement.html).
`void`
`[visitPackageImport](#visitPackageImport(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`PackageImport`](../../magicdraw/classes/mdkernel/PackageImport.html).
`void`
`[visitPackageMerge](#visitPackageMerge(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`PackageMerge`](../../magicdraw/classes/mdkernel/PackageMerge.html).
`void`
`[visitParameter](#visitParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Parameter`](../../magicdraw/classes/mdkernel/Parameter.html).
`void`
`[visitParameterableElement](#visitParameterableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ParameterableElement`](../../magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html).
`void`
`[visitParameterSet](#visitParameterSet(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ParameterSet`](../../magicdraw/activities/mdcompleteactivities/ParameterSet.html).
`void`
`[visitPartDecomposition](#visitPartDecomposition(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`PartDecomposition`](../../magicdraw/interactions/mdfragments/PartDecomposition.html).
`void`
`[visitPin](#visitPin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Pin`](../../magicdraw/actions/mdbasicactions/Pin.html).
`void`
`[visitPort](#visitPort(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Port`](../../magicdraw/compositestructures/mdports/Port.html).
`void`
`[visitPrimitiveType](#visitPrimitiveType(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`PrimitiveType`](../../magicdraw/classes/mdkernel/PrimitiveType.html).
`void`
`[visitProfile](#visitProfile(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Profile`](../../magicdraw/mdprofiles/Profile.html).
`void`
`[visitProfileApplication](#visitProfileApplication(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ProfileApplication`](../../magicdraw/mdprofiles/ProfileApplication.html).
`void`
`[visitProperty](#visitProperty(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Property`](../../magicdraw/classes/mdkernel/Property.html).
`void`
`[visitProtocolConformance](#visitProtocolConformance(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ProtocolConformance`](../../magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html).
`void`
`[visitProtocolStateMachine](#visitProtocolStateMachine(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ProtocolStateMachine`](../../magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html).
`void`
`[visitProtocolTransition](#visitProtocolTransition(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ProtocolTransition`](../../magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html).
`void`
`[visitPseudostate](#visitPseudostate(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Pseudostate`](../../magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html).
`void`
`[visitQualifierValue](#visitQualifierValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`QualifierValue`](../../magicdraw/actions/mdcompleteactions/QualifierValue.html).
`void`
`[visitRaiseExceptionAction](#visitRaiseExceptionAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`RaiseExceptionAction`](../../magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html).
`void`
`[visitReadExtentAction](#visitReadExtentAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ReadExtentAction`](../../magicdraw/actions/mdcompleteactions/ReadExtentAction.html).
`void`
`[visitReadIsClassifiedObjectAction](#visitReadIsClassifiedObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ReadIsClassifiedObjectAction`](../../magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html).
`void`
`[visitReadLinkAction](#visitReadLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ReadLinkAction`](../../magicdraw/actions/mdintermediateactions/ReadLinkAction.html).
`void`
`[visitReadLinkObjectEndAction](#visitReadLinkObjectEndAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ReadLinkObjectEndAction`](../../magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html).
`void`
`[visitReadLinkObjectEndQualifierAction](#visitReadLinkObjectEndQualifierAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ReadLinkObjectEndQualifierAction`](../../magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html).
`void`
`[visitReadSelfAction](#visitReadSelfAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ReadSelfAction`](../../magicdraw/actions/mdintermediateactions/ReadSelfAction.html).
`void`
`[visitReadStructuralFeatureAction](#visitReadStructuralFeatureAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ReadStructuralFeatureAction`](../../magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html).
`void`
`[visitReadVariableAction](#visitReadVariableAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ReadVariableAction`](../../magicdraw/actions/mdstructuredactions/ReadVariableAction.html).
`void`
`[visitRealization](#visitRealization(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Realization`](../../magicdraw/classes/mddependencies/Realization.html).
`void`
`[visitRealTaggedValue](#visitRealTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`

`void`
`[visitReception](#visitReception(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Reception`](../../magicdraw/commonbehaviors/mdcommunications/Reception.html).
`void`
`[visitReclassifyObjectAction](#visitReclassifyObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ReclassifyObjectAction`](../../magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html).
`void`
`[visitRedefinableElement](#visitRedefinableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`RedefinableElement`](../../magicdraw/classes/mdkernel/RedefinableElement.html).
`void`
`[visitRedefinableTemplateSignature](#visitRedefinableTemplateSignature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`RedefinableTemplateSignature`](../../magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html).
`void`
`[visitReduceAction](#visitReduceAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ReduceAction`](../../magicdraw/actions/mdcompleteactions/ReduceAction.html).
`void`
`[visitRegion](#visitRegion(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Region`](../../magicdraw/statemachines/mdbehaviorstatemachines/Region.html).
`void`
`[visitRelationship](#visitRelationship(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Relationship`](../../magicdraw/classes/mdkernel/Relationship.html).
`void`
`[visitRemoveStructuralFeatureValueAction](#visitRemoveStructuralFeatureValueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`RemoveStructuralFeatureValueAction`](../../magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html).
`void`
`[visitRemoveVariableValueAction](#visitRemoveVariableValueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`RemoveVariableValueAction`](../../magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html).
`void`
`[visitReplyAction](#visitReplyAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ReplyAction`](../../magicdraw/actions/mdcompleteactions/ReplyAction.html).
`void`
`[visitSendObjectAction](#visitSendObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`SendObjectAction`](../../magicdraw/actions/mdintermediateactions/SendObjectAction.html).
`void`
`[visitSendSignalAction](#visitSendSignalAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`SendSignalAction`](../../magicdraw/actions/mdbasicactions/SendSignalAction.html).
`void`
`[visitSequenceNode](#visitSequenceNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`SequenceNode`](../../magicdraw/activities/mdstructuredactivities/SequenceNode.html).
`void`
`[visitSignal](#visitSignal(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Signal`](../../magicdraw/commonbehaviors/mdcommunications/Signal.html).
`void`
`[visitSignalEvent](#visitSignalEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`SignalEvent`](../../magicdraw/commonbehaviors/mdcommunications/SignalEvent.html).
`void`
`[visitSlot](#visitSlot(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Slot`](../../magicdraw/classes/mdkernel/Slot.html).
`void`
`[visitStartClassifierBehaviorAction](#visitStartClassifierBehaviorAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`StartClassifierBehaviorAction`](../../magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html).
`void`
`[visitStartObjectBehaviorAction](#visitStartObjectBehaviorAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`StartObjectBehaviorAction`](../../magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html).
`void`
`[visitState](#visitState(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`State`](../../magicdraw/statemachines/mdbehaviorstatemachines/State.html).
`void`
`[visitStateInvariant](#visitStateInvariant(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`StateInvariant`](../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html).
`void`
`[visitStateMachine](#visitStateMachine(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`StateMachine`](../../magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html).
`void`
`[visitStereotype](#visitStereotype(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Stereotype`](../../magicdraw/mdprofiles/Stereotype.html).
`void`
`[visitStringExpression](#visitStringExpression(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`StringExpression`](../../magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html).
`void`
`[visitStringTaggedValue](#visitStringTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`

`void`
`[visitStructuralFeature](#visitStructuralFeature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`StructuralFeature`](../../magicdraw/classes/mdkernel/StructuralFeature.html).
`void`
`[visitStructuralFeatureAction](#visitStructuralFeatureAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`StructuralFeatureAction`](../../magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html).
`void`
`[visitStructuredActivityNode](#visitStructuredActivityNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`StructuredActivityNode`](../../magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html).
`void`
`[visitStructuredClassifier](#visitStructuredClassifier(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`StructuredClassifier`](../../magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html).
`void`
`[visitSubstitution](#visitSubstitution(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Substitution`](../../magicdraw/classes/mddependencies/Substitution.html).
`void`
`[visitTaggedValue](#visitTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`

`void`
`[visitTemplateableElement](#visitTemplateableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`TemplateableElement`](../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html).
`void`
`[visitTemplateBinding](#visitTemplateBinding(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`TemplateBinding`](../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html).
`void`
`[visitTemplateParameter](#visitTemplateParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`TemplateParameter`](../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html).
`void`
`[visitTemplateParameterSubstitution](#visitTemplateParameterSubstitution(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`TemplateParameterSubstitution`](../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html).
`void`
`[visitTemplateSignature](#visitTemplateSignature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`TemplateSignature`](../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html).
`void`
`[visitTestIdentityAction](#visitTestIdentityAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`TestIdentityAction`](../../magicdraw/actions/mdintermediateactions/TestIdentityAction.html).
`void`
`[visitTimeConstraint](#visitTimeConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`TimeConstraint`](../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html).
`void`
`[visitTimeEvent](#visitTimeEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`TimeEvent`](../../magicdraw/commonbehaviors/mdcommunications/TimeEvent.html).
`void`
`[visitTimeExpression](#visitTimeExpression(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`TimeExpression`](../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html).
`void`
`[visitTimeInterval](#visitTimeInterval(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`TimeInterval`](../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html).
`void`
`[visitTimeObservation](#visitTimeObservation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`TimeObservation`](../../magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html).
`void`
`[visitTransition](#visitTransition(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Transition`](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html).
`void`
`[visitTrigger](#visitTrigger(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Trigger`](../../magicdraw/commonbehaviors/mdcommunications/Trigger.html).
`void`
`[visitType](#visitType(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Type`](../../magicdraw/classes/mdkernel/Type.html).
`void`
`[visitTypedElement](#visitTypedElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`TypedElement`](../../magicdraw/classes/mdkernel/TypedElement.html).
`void`
`[visitUnmarshallAction](#visitUnmarshallAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`UnmarshallAction`](../../magicdraw/actions/mdcompleteactions/UnmarshallAction.html).
`void`
`[visitUsage](#visitUsage(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Usage`](../../magicdraw/classes/mddependencies/Usage.html).
`void`
`[visitUseCase](#visitUseCase(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`UseCase`](../../magicdraw/mdusecases/UseCase.html).
`void`
`[visitValuePin](#visitValuePin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ValuePin`](../../magicdraw/actions/mdbasicactions/ValuePin.html).
`void`
`[visitValueSpecification](#visitValueSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ValueSpecification`](../../magicdraw/classes/mdkernel/ValueSpecification.html).
`void`
`[visitValueSpecificationAction](#visitValueSpecificationAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`ValueSpecificationAction`](../../magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html).
`void`
`[visitVariable](#visitVariable(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Variable`](../../magicdraw/activities/mdstructuredactivities/Variable.html).
`void`
`[visitVariableAction](#visitVariableAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`VariableAction`](../../magicdraw/actions/mdstructuredactions/VariableAction.html).
`void`
`[visitVertex](#visitVertex(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`Vertex`](../../magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html).
`void`
`[visitWriteLinkAction](#visitWriteLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`WriteLinkAction`](../../magicdraw/actions/mdintermediateactions/WriteLinkAction.html).
`void`
`[visitWriteStructuralFeatureAction](#visitWriteStructuralFeatureAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`WriteStructuralFeatureAction`](../../magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html).
`void`
`[visitWriteVariableAction](#visitWriteVariableAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VisitorContext](VisitorContext.html) context)`
Visitor method for [`WriteVariableAction`](../../magicdraw/actions/mdstructuredactions/WriteVariableAction.html).
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ClassTypeHierarchyVisitor
public ClassTypeHierarchyVisitor()
 ============ METHOD DETAIL ========== 
Method Details
visit
public final void visit([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> type)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAbstraction
public void visitAbstraction([VisitorContext](VisitorContext.html) context)
Visitor method for [`Abstraction`](../../magicdraw/classes/mddependencies/Abstraction.html).
Parameters:
`context` - visitor's context.
visitAcceptCallAction
public void visitAcceptCallAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`AcceptCallAction`](../../magicdraw/actions/mdcompleteactions/AcceptCallAction.html).
Parameters:
`context` - visitor's context.
visitAcceptEventAction
public void visitAcceptEventAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`AcceptEventAction`](../../magicdraw/actions/mdcompleteactions/AcceptEventAction.html).
Parameters:
`context` - visitor's context.
visitAction
public void visitAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`Action`](../../magicdraw/actions/mdbasicactions/Action.html).
Parameters:
`context` - visitor's context.
visitActionExecutionSpecification
public void visitActionExecutionSpecification([VisitorContext](VisitorContext.html) context)
Visitor method for [`ActionExecutionSpecification`](../../magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html).
Parameters:
`context` - visitor's context.
visitActionInputPin
public void visitActionInputPin([VisitorContext](VisitorContext.html) context)
Visitor method for [`ActionInputPin`](../../magicdraw/actions/mdstructuredactions/ActionInputPin.html).
Parameters:
`context` - visitor's context.
visitActivity
public void visitActivity([VisitorContext](VisitorContext.html) context)
Visitor method for [`Activity`](../../magicdraw/activities/mdfundamentalactivities/Activity.html).
Parameters:
`context` - visitor's context.
visitActivityEdge
public void visitActivityEdge([VisitorContext](VisitorContext.html) context)
Visitor method for [`ActivityEdge`](../../magicdraw/activities/mdbasicactivities/ActivityEdge.html).
Parameters:
`context` - visitor's context.
visitActivityFinalNode
public void visitActivityFinalNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`ActivityFinalNode`](../../magicdraw/activities/mdbasicactivities/ActivityFinalNode.html).
Parameters:
`context` - visitor's context.
visitActivityGroup
public void visitActivityGroup([VisitorContext](VisitorContext.html) context)
Visitor method for [`ActivityGroup`](../../magicdraw/activities/mdfundamentalactivities/ActivityGroup.html).
Parameters:
`context` - visitor's context.
visitActivityNode
public void visitActivityNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`ActivityNode`](../../magicdraw/activities/mdfundamentalactivities/ActivityNode.html).
Parameters:
`context` - visitor's context.
visitActivityParameterNode
public void visitActivityParameterNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`ActivityParameterNode`](../../magicdraw/activities/mdbasicactivities/ActivityParameterNode.html).
Parameters:
`context` - visitor's context.
visitActivityPartition
public void visitActivityPartition([VisitorContext](VisitorContext.html) context)
Visitor method for [`ActivityPartition`](../../magicdraw/activities/mdintermediateactivities/ActivityPartition.html).
Parameters:
`context` - visitor's context.
visitActor
public void visitActor([VisitorContext](VisitorContext.html) context)
Visitor method for [`Actor`](../../magicdraw/mdusecases/Actor.html).
Parameters:
`context` - visitor's context.
visitAddStructuralFeatureValueAction
public void visitAddStructuralFeatureValueAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`AddStructuralFeatureValueAction`](../../magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html).
Parameters:
`context` - visitor's context.
visitAddVariableValueAction
public void visitAddVariableValueAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`AddVariableValueAction`](../../magicdraw/actions/mdstructuredactions/AddVariableValueAction.html).
Parameters:
`context` - visitor's context.
visitAnyReceiveEvent
public void visitAnyReceiveEvent([VisitorContext](VisitorContext.html) context)
Visitor method for [`AnyReceiveEvent`](../../magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html).
Parameters:
`context` - visitor's context.
visitArtifact
public void visitArtifact([VisitorContext](VisitorContext.html) context)
Visitor method for [`Artifact`](../../magicdraw/deployments/mdartifacts/Artifact.html).
Parameters:
`context` - visitor's context.
visitAssociation
public void visitAssociation([VisitorContext](VisitorContext.html) context)
Visitor method for [`Association`](../../magicdraw/classes/mdkernel/Association.html).
Parameters:
`context` - visitor's context.
visitAssociationClass
public void visitAssociationClass([VisitorContext](VisitorContext.html) context)
Visitor method for [`AssociationClass`](../../magicdraw/classes/mdassociationclasses/AssociationClass.html).
Parameters:
`context` - visitor's context.
visitBehavior
public void visitBehavior([VisitorContext](VisitorContext.html) context)
Visitor method for [`Behavior`](../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html).
Parameters:
`context` - visitor's context.
visitBehaviorExecutionSpecification
public void visitBehaviorExecutionSpecification([VisitorContext](VisitorContext.html) context)
Visitor method for [`BehaviorExecutionSpecification`](../../magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html).
Parameters:
`context` - visitor's context.
visitBehavioralFeature
public void visitBehavioralFeature([VisitorContext](VisitorContext.html) context)
Visitor method for [`BehavioralFeature`](../../magicdraw/classes/mdkernel/BehavioralFeature.html).
Parameters:
`context` - visitor's context.
visitBehavioredClassifier
public void visitBehavioredClassifier([VisitorContext](VisitorContext.html) context)
Visitor method for [`BehavioredClassifier`](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html).
Parameters:
`context` - visitor's context.
visitBroadcastSignalAction
public void visitBroadcastSignalAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`BroadcastSignalAction`](../../magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html).
Parameters:
`context` - visitor's context.
visitCallAction
public void visitCallAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`CallAction`](../../magicdraw/actions/mdbasicactions/CallAction.html).
Parameters:
`context` - visitor's context.
visitCallBehaviorAction
public void visitCallBehaviorAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`CallBehaviorAction`](../../magicdraw/actions/mdbasicactions/CallBehaviorAction.html).
Parameters:
`context` - visitor's context.
visitCallEvent
public void visitCallEvent([VisitorContext](VisitorContext.html) context)
Visitor method for [`CallEvent`](../../magicdraw/commonbehaviors/mdcommunications/CallEvent.html).
Parameters:
`context` - visitor's context.
visitCallOperationAction
public void visitCallOperationAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`CallOperationAction`](../../magicdraw/actions/mdbasicactions/CallOperationAction.html).
Parameters:
`context` - visitor's context.
visitCentralBufferNode
public void visitCentralBufferNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`CentralBufferNode`](../../magicdraw/activities/mdintermediateactivities/CentralBufferNode.html).
Parameters:
`context` - visitor's context.
visitChangeEvent
public void visitChangeEvent([VisitorContext](VisitorContext.html) context)
Visitor method for [`ChangeEvent`](../../magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html).
Parameters:
`context` - visitor's context.
visitClass
public void visitClass([VisitorContext](VisitorContext.html) context)
Visitor method for [`Class`](../../magicdraw/classes/mdkernel/Class.html).
Parameters:
`context` - visitor's context.
visitClassifier
public void visitClassifier([VisitorContext](VisitorContext.html) context)
Visitor method for [`Classifier`](../../magicdraw/classes/mdkernel/Classifier.html).
Parameters:
`context` - visitor's context.
visitClassifierTemplateParameter
public void visitClassifierTemplateParameter([VisitorContext](VisitorContext.html) context)
Visitor method for [`ClassifierTemplateParameter`](../../magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html).
Parameters:
`context` - visitor's context.
visitClause
public void visitClause([VisitorContext](VisitorContext.html) context)
Visitor method for [`Clause`](../../magicdraw/activities/mdstructuredactivities/Clause.html).
Parameters:
`context` - visitor's context.
visitClearAssociationAction
public void visitClearAssociationAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ClearAssociationAction`](../../magicdraw/actions/mdintermediateactions/ClearAssociationAction.html).
Parameters:
`context` - visitor's context.
visitClearStructuralFeatureAction
public void visitClearStructuralFeatureAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ClearStructuralFeatureAction`](../../magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html).
Parameters:
`context` - visitor's context.
visitClearVariableAction
public void visitClearVariableAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ClearVariableAction`](../../magicdraw/actions/mdstructuredactions/ClearVariableAction.html).
Parameters:
`context` - visitor's context.
visitCollaboration
public void visitCollaboration([VisitorContext](VisitorContext.html) context)
Visitor method for [`Collaboration`](../../magicdraw/compositestructures/mdcollaborations/Collaboration.html).
Parameters:
`context` - visitor's context.
visitCollaborationUse
public void visitCollaborationUse([VisitorContext](VisitorContext.html) context)
Visitor method for [`CollaborationUse`](../../magicdraw/compositestructures/mdcollaborations/CollaborationUse.html).
Parameters:
`context` - visitor's context.
visitCombinedFragment
public void visitCombinedFragment([VisitorContext](VisitorContext.html) context)
Visitor method for [`CombinedFragment`](../../magicdraw/interactions/mdfragments/CombinedFragment.html).
Parameters:
`context` - visitor's context.
visitComment
public void visitComment([VisitorContext](VisitorContext.html) context)
Visitor method for [`Comment`](../../magicdraw/classes/mdkernel/Comment.html).
Parameters:
`context` - visitor's context.
visitCommunicationPath
public void visitCommunicationPath([VisitorContext](VisitorContext.html) context)
Visitor method for [`CommunicationPath`](../../magicdraw/deployments/mdnodes/CommunicationPath.html).
Parameters:
`context` - visitor's context.
visitComponent
public void visitComponent([VisitorContext](VisitorContext.html) context)
Visitor method for [`Component`](../../magicdraw/components/mdbasiccomponents/Component.html).
Parameters:
`context` - visitor's context.
visitComponentRealization
public void visitComponentRealization([VisitorContext](VisitorContext.html) context)
Visitor method for [`ComponentRealization`](../../magicdraw/components/mdbasiccomponents/ComponentRealization.html).
Parameters:
`context` - visitor's context.
visitConditionalNode
public void visitConditionalNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`ConditionalNode`](../../magicdraw/activities/mdstructuredactivities/ConditionalNode.html).
Parameters:
`context` - visitor's context.
visitConnectableElement
public void visitConnectableElement([VisitorContext](VisitorContext.html) context)
Visitor method for [`ConnectableElement`](../../magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html).
Parameters:
`context` - visitor's context.
visitConnectableElementTemplateParameter
public void visitConnectableElementTemplateParameter([VisitorContext](VisitorContext.html) context)
Visitor method for [`ConnectableElementTemplateParameter`](../../magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html).
Parameters:
`context` - visitor's context.
visitConnectionPointReference
public void visitConnectionPointReference([VisitorContext](VisitorContext.html) context)
Visitor method for [`ConnectionPointReference`](../../magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html).
Parameters:
`context` - visitor's context.
visitConnector
public void visitConnector([VisitorContext](VisitorContext.html) context)
Visitor method for [`Connector`](../../magicdraw/compositestructures/mdinternalstructures/Connector.html).
Parameters:
`context` - visitor's context.
visitConnectorEnd
public void visitConnectorEnd([VisitorContext](VisitorContext.html) context)
Visitor method for [`ConnectorEnd`](../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html).
Parameters:
`context` - visitor's context.
visitConsiderIgnoreFragment
public void visitConsiderIgnoreFragment([VisitorContext](VisitorContext.html) context)
Visitor method for [`ConsiderIgnoreFragment`](../../magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html).
Parameters:
`context` - visitor's context.
visitConstraint
public void visitConstraint([VisitorContext](VisitorContext.html) context)
Visitor method for [`Constraint`](../../magicdraw/classes/mdkernel/Constraint.html).
Parameters:
`context` - visitor's context.
visitContinuation
public void visitContinuation([VisitorContext](VisitorContext.html) context)
Visitor method for [`Continuation`](../../magicdraw/interactions/mdfragments/Continuation.html).
Parameters:
`context` - visitor's context.
visitControlFlow
public void visitControlFlow([VisitorContext](VisitorContext.html) context)
Visitor method for [`ControlFlow`](../../magicdraw/activities/mdbasicactivities/ControlFlow.html).
Parameters:
`context` - visitor's context.
visitControlNode
public void visitControlNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`ControlNode`](../../magicdraw/activities/mdbasicactivities/ControlNode.html).
Parameters:
`context` - visitor's context.
visitCreateLinkAction
public void visitCreateLinkAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`CreateLinkAction`](../../magicdraw/actions/mdintermediateactions/CreateLinkAction.html).
Parameters:
`context` - visitor's context.
visitCreateLinkObjectAction
public void visitCreateLinkObjectAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`CreateLinkObjectAction`](../../magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html).
Parameters:
`context` - visitor's context.
visitCreateObjectAction
public void visitCreateObjectAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`CreateObjectAction`](../../magicdraw/actions/mdintermediateactions/CreateObjectAction.html).
Parameters:
`context` - visitor's context.
visitDataStoreNode
public void visitDataStoreNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`DataStoreNode`](../../magicdraw/activities/mdcompleteactivities/DataStoreNode.html).
Parameters:
`context` - visitor's context.
visitDataType
public void visitDataType([VisitorContext](VisitorContext.html) context)
Visitor method for [`DataType`](../../magicdraw/classes/mdkernel/DataType.html).
Parameters:
`context` - visitor's context.
visitDecisionNode
public void visitDecisionNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`DecisionNode`](../../magicdraw/activities/mdintermediateactivities/DecisionNode.html).
Parameters:
`context` - visitor's context.
visitDependency
public void visitDependency([VisitorContext](VisitorContext.html) context)
Visitor method for [`Dependency`](../../magicdraw/classes/mddependencies/Dependency.html).
Parameters:
`context` - visitor's context.
visitDeployedArtifact
public void visitDeployedArtifact([VisitorContext](VisitorContext.html) context)
Visitor method for [`DeployedArtifact`](../../magicdraw/deployments/mdnodes/DeployedArtifact.html).
Parameters:
`context` - visitor's context.
visitDeployment
public void visitDeployment([VisitorContext](VisitorContext.html) context)
Visitor method for [`Deployment`](../../magicdraw/deployments/mdnodes/Deployment.html).
Parameters:
`context` - visitor's context.
visitDeploymentSpecification
public void visitDeploymentSpecification([VisitorContext](VisitorContext.html) context)
Visitor method for [`DeploymentSpecification`](../../magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html).
Parameters:
`context` - visitor's context.
visitDeploymentTarget
public void visitDeploymentTarget([VisitorContext](VisitorContext.html) context)
Visitor method for [`DeploymentTarget`](../../magicdraw/deployments/mdnodes/DeploymentTarget.html).
Parameters:
`context` - visitor's context.
visitDestroyLinkAction
public void visitDestroyLinkAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`DestroyLinkAction`](../../magicdraw/actions/mdintermediateactions/DestroyLinkAction.html).
Parameters:
`context` - visitor's context.
visitDestroyObjectAction
public void visitDestroyObjectAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`DestroyObjectAction`](../../magicdraw/actions/mdintermediateactions/DestroyObjectAction.html).
Parameters:
`context` - visitor's context.
visitDestructionOccurrenceSpecification
public void visitDestructionOccurrenceSpecification([VisitorContext](VisitorContext.html) context)
Visitor method for [`DestructionOccurrenceSpecification`](../../magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html).
Parameters:
`context` - visitor's context.
visitDevice
public void visitDevice([VisitorContext](VisitorContext.html) context)
Visitor method for [`Device`](../../magicdraw/deployments/mdnodes/Device.html).
Parameters:
`context` - visitor's context.
visitDiagram
public void visitDiagram([VisitorContext](VisitorContext.html) context)
Visitor method for [`Diagram`](../../magicdraw/classes/mdkernel/Diagram.html).
Parameters:
`context` - visitor's context.
visitDirectedRelationship
public void visitDirectedRelationship([VisitorContext](VisitorContext.html) context)
Visitor method for [`DirectedRelationship`](../../magicdraw/classes/mdkernel/DirectedRelationship.html).
Parameters:
`context` - visitor's context.
visitDuration
public void visitDuration([VisitorContext](VisitorContext.html) context)
Visitor method for [`Duration`](../../magicdraw/commonbehaviors/mdsimpletime/Duration.html).
Parameters:
`context` - visitor's context.
visitDurationConstraint
public void visitDurationConstraint([VisitorContext](VisitorContext.html) context)
Visitor method for [`DurationConstraint`](../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html).
Parameters:
`context` - visitor's context.
visitDurationInterval
public void visitDurationInterval([VisitorContext](VisitorContext.html) context)
Visitor method for [`DurationInterval`](../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html).
Parameters:
`context` - visitor's context.
visitDurationObservation
public void visitDurationObservation([VisitorContext](VisitorContext.html) context)
Visitor method for [`DurationObservation`](../../magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html).
Parameters:
`context` - visitor's context.
visitElement
public void visitElement([VisitorContext](VisitorContext.html) context)
Visitor method for [`Element`](../../magicdraw/classes/mdkernel/Element.html).
Parameters:
`context` - visitor's context.
visitElementImport
public void visitElementImport([VisitorContext](VisitorContext.html) context)
Visitor method for [`ElementImport`](../../magicdraw/classes/mdkernel/ElementImport.html).
Parameters:
`context` - visitor's context.
visitElementValue
public void visitElementValue([VisitorContext](VisitorContext.html) context)
Visitor method for [`ElementValue`](../../magicdraw/classes/mdkernel/ElementValue.html).
Parameters:
`context` - visitor's context.
visitEncapsulatedClassifier
public void visitEncapsulatedClassifier([VisitorContext](VisitorContext.html) context)
Visitor method for [`EncapsulatedClassifier`](../../magicdraw/compositestructures/mdports/EncapsulatedClassifier.html).
Parameters:
`context` - visitor's context.
visitEnumeration
public void visitEnumeration([VisitorContext](VisitorContext.html) context)
Visitor method for [`Enumeration`](../../magicdraw/classes/mdkernel/Enumeration.html).
Parameters:
`context` - visitor's context.
visitEnumerationLiteral
public void visitEnumerationLiteral([VisitorContext](VisitorContext.html) context)
Visitor method for [`EnumerationLiteral`](../../magicdraw/classes/mdkernel/EnumerationLiteral.html).
Parameters:
`context` - visitor's context.
visitEvent
public void visitEvent([VisitorContext](VisitorContext.html) context)
Visitor method for [`Event`](../../magicdraw/commonbehaviors/mdcommunications/Event.html).
Parameters:
`context` - visitor's context.
visitExceptionHandler
public void visitExceptionHandler([VisitorContext](VisitorContext.html) context)
Visitor method for [`ExceptionHandler`](../../magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html).
Parameters:
`context` - visitor's context.
visitExecutableNode
public void visitExecutableNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`ExecutableNode`](../../magicdraw/activities/mdstructuredactivities/ExecutableNode.html).
Parameters:
`context` - visitor's context.
visitExecutionEnvironment
public void visitExecutionEnvironment([VisitorContext](VisitorContext.html) context)
Visitor method for [`ExecutionEnvironment`](../../magicdraw/deployments/mdnodes/ExecutionEnvironment.html).
Parameters:
`context` - visitor's context.
visitExecutionOccurrenceSpecification
public void visitExecutionOccurrenceSpecification([VisitorContext](VisitorContext.html) context)
Visitor method for [`ExecutionOccurrenceSpecification`](../../magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html).
Parameters:
`context` - visitor's context.
visitExecutionSpecification
public void visitExecutionSpecification([VisitorContext](VisitorContext.html) context)
Visitor method for [`ExecutionSpecification`](../../magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html).
Parameters:
`context` - visitor's context.
visitExpansionNode
public void visitExpansionNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`ExpansionNode`](../../magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html).
Parameters:
`context` - visitor's context.
visitExpansionRegion
public void visitExpansionRegion([VisitorContext](VisitorContext.html) context)
Visitor method for [`ExpansionRegion`](../../magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html).
Parameters:
`context` - visitor's context.
visitExpression
public void visitExpression([VisitorContext](VisitorContext.html) context)
Visitor method for [`Expression`](../../magicdraw/classes/mdkernel/Expression.html).
Parameters:
`context` - visitor's context.
visitExtend
public void visitExtend([VisitorContext](VisitorContext.html) context)
Visitor method for [`Extend`](../../magicdraw/mdusecases/Extend.html).
Parameters:
`context` - visitor's context.
visitExtension
public void visitExtension([VisitorContext](VisitorContext.html) context)
Visitor method for [`Extension`](../../magicdraw/mdprofiles/Extension.html).
Parameters:
`context` - visitor's context.
visitExtensionEnd
public void visitExtensionEnd([VisitorContext](VisitorContext.html) context)
Visitor method for [`ExtensionEnd`](../../magicdraw/mdprofiles/ExtensionEnd.html).
Parameters:
`context` - visitor's context.
visitExtensionPoint
public void visitExtensionPoint([VisitorContext](VisitorContext.html) context)
Visitor method for [`ExtensionPoint`](../../magicdraw/mdusecases/ExtensionPoint.html).
Parameters:
`context` - visitor's context.
visitFeature
public void visitFeature([VisitorContext](VisitorContext.html) context)
Visitor method for [`Feature`](../../magicdraw/classes/mdkernel/Feature.html).
Parameters:
`context` - visitor's context.
visitFinalNode
public void visitFinalNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`FinalNode`](../../magicdraw/activities/mdintermediateactivities/FinalNode.html).
Parameters:
`context` - visitor's context.
visitFinalState
public void visitFinalState([VisitorContext](VisitorContext.html) context)
Visitor method for [`FinalState`](../../magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html).
Parameters:
`context` - visitor's context.
visitFlowFinalNode
public void visitFlowFinalNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`FlowFinalNode`](../../magicdraw/activities/mdintermediateactivities/FlowFinalNode.html).
Parameters:
`context` - visitor's context.
visitForkNode
public void visitForkNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`ForkNode`](../../magicdraw/activities/mdintermediateactivities/ForkNode.html).
Parameters:
`context` - visitor's context.
visitFunctionBehavior
public void visitFunctionBehavior([VisitorContext](VisitorContext.html) context)
Visitor method for [`FunctionBehavior`](../../magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html).
Parameters:
`context` - visitor's context.
visitGate
public void visitGate([VisitorContext](VisitorContext.html) context)
Visitor method for [`Gate`](../../magicdraw/interactions/mdfragments/Gate.html).
Parameters:
`context` - visitor's context.
visitGeneralOrdering
public void visitGeneralOrdering([VisitorContext](VisitorContext.html) context)
Visitor method for [`GeneralOrdering`](../../magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html).
Parameters:
`context` - visitor's context.
visitGeneralization
public void visitGeneralization([VisitorContext](VisitorContext.html) context)
Visitor method for [`Generalization`](../../magicdraw/classes/mdkernel/Generalization.html).
Parameters:
`context` - visitor's context.
visitGeneralizationSet
public void visitGeneralizationSet([VisitorContext](VisitorContext.html) context)
Visitor method for [`GeneralizationSet`](../../magicdraw/classes/mdpowertypes/GeneralizationSet.html).
Parameters:
`context` - visitor's context.
visitImage
public void visitImage([VisitorContext](VisitorContext.html) context)
Visitor method for [`Image`](../../magicdraw/mdprofiles/Image.html).
Parameters:
`context` - visitor's context.
visitInclude
public void visitInclude([VisitorContext](VisitorContext.html) context)
Visitor method for [`Include`](../../magicdraw/mdusecases/Include.html).
Parameters:
`context` - visitor's context.
visitInformationFlow
public void visitInformationFlow([VisitorContext](VisitorContext.html) context)
Visitor method for [`InformationFlow`](../../magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html).
Parameters:
`context` - visitor's context.
visitInformationItem
public void visitInformationItem([VisitorContext](VisitorContext.html) context)
Visitor method for [`InformationItem`](../../magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html).
Parameters:
`context` - visitor's context.
visitInitialNode
public void visitInitialNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`InitialNode`](../../magicdraw/activities/mdbasicactivities/InitialNode.html).
Parameters:
`context` - visitor's context.
visitInputPin
public void visitInputPin([VisitorContext](VisitorContext.html) context)
Visitor method for [`InputPin`](../../magicdraw/actions/mdbasicactions/InputPin.html).
Parameters:
`context` - visitor's context.
visitInstanceSpecification
public void visitInstanceSpecification([VisitorContext](VisitorContext.html) context)
Visitor method for [`InstanceSpecification`](../../magicdraw/classes/mdkernel/InstanceSpecification.html).
Parameters:
`context` - visitor's context.
visitInstanceValue
public void visitInstanceValue([VisitorContext](VisitorContext.html) context)
Visitor method for [`InstanceValue`](../../magicdraw/classes/mdkernel/InstanceValue.html).
Parameters:
`context` - visitor's context.
visitInteraction
public void visitInteraction([VisitorContext](VisitorContext.html) context)
Visitor method for [`Interaction`](../../magicdraw/interactions/mdbasicinteractions/Interaction.html).
Parameters:
`context` - visitor's context.
visitInteractionConstraint
public void visitInteractionConstraint([VisitorContext](VisitorContext.html) context)
Visitor method for [`InteractionConstraint`](../../magicdraw/interactions/mdfragments/InteractionConstraint.html).
Parameters:
`context` - visitor's context.
visitInteractionFragment
public void visitInteractionFragment([VisitorContext](VisitorContext.html) context)
Visitor method for [`InteractionFragment`](../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html).
Parameters:
`context` - visitor's context.
visitInteractionOperand
public void visitInteractionOperand([VisitorContext](VisitorContext.html) context)
Visitor method for [`InteractionOperand`](../../magicdraw/interactions/mdfragments/InteractionOperand.html).
Parameters:
`context` - visitor's context.
visitInteractionUse
public void visitInteractionUse([VisitorContext](VisitorContext.html) context)
Visitor method for [`InteractionUse`](../../magicdraw/interactions/mdfragments/InteractionUse.html).
Parameters:
`context` - visitor's context.
visitInterface
public void visitInterface([VisitorContext](VisitorContext.html) context)
Visitor method for [`Interface`](../../magicdraw/classes/mdinterfaces/Interface.html).
Parameters:
`context` - visitor's context.
visitInterfaceRealization
public void visitInterfaceRealization([VisitorContext](VisitorContext.html) context)
Visitor method for [`InterfaceRealization`](../../magicdraw/classes/mdinterfaces/InterfaceRealization.html).
Parameters:
`context` - visitor's context.
visitInterruptibleActivityRegion
public void visitInterruptibleActivityRegion([VisitorContext](VisitorContext.html) context)
Visitor method for [`InterruptibleActivityRegion`](../../magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html).
Parameters:
`context` - visitor's context.
visitInterval
public void visitInterval([VisitorContext](VisitorContext.html) context)
Visitor method for [`Interval`](../../magicdraw/commonbehaviors/mdsimpletime/Interval.html).
Parameters:
`context` - visitor's context.
visitIntervalConstraint
public void visitIntervalConstraint([VisitorContext](VisitorContext.html) context)
Visitor method for [`IntervalConstraint`](../../magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html).
Parameters:
`context` - visitor's context.
visitInvocationAction
public void visitInvocationAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`InvocationAction`](../../magicdraw/actions/mdbasicactions/InvocationAction.html).
Parameters:
`context` - visitor's context.
visitJoinNode
public void visitJoinNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`JoinNode`](../../magicdraw/activities/mdintermediateactivities/JoinNode.html).
Parameters:
`context` - visitor's context.
visitLifeline
public void visitLifeline([VisitorContext](VisitorContext.html) context)
Visitor method for [`Lifeline`](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html).
Parameters:
`context` - visitor's context.
visitLinkAction
public void visitLinkAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`LinkAction`](../../magicdraw/actions/mdintermediateactions/LinkAction.html).
Parameters:
`context` - visitor's context.
visitLinkEndCreationData
public void visitLinkEndCreationData([VisitorContext](VisitorContext.html) context)
Visitor method for [`LinkEndCreationData`](../../magicdraw/actions/mdintermediateactions/LinkEndCreationData.html).
Parameters:
`context` - visitor's context.
visitLinkEndData
public void visitLinkEndData([VisitorContext](VisitorContext.html) context)
Visitor method for [`LinkEndData`](../../magicdraw/actions/mdintermediateactions/LinkEndData.html).
Parameters:
`context` - visitor's context.
visitLinkEndDestructionData
public void visitLinkEndDestructionData([VisitorContext](VisitorContext.html) context)
Visitor method for [`LinkEndDestructionData`](../../magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html).
Parameters:
`context` - visitor's context.
visitLiteralBoolean
public void visitLiteralBoolean([VisitorContext](VisitorContext.html) context)
Visitor method for [`LiteralBoolean`](../../magicdraw/classes/mdkernel/LiteralBoolean.html).
Parameters:
`context` - visitor's context.
visitLiteralInteger
public void visitLiteralInteger([VisitorContext](VisitorContext.html) context)
Visitor method for [`LiteralInteger`](../../magicdraw/classes/mdkernel/LiteralInteger.html).
Parameters:
`context` - visitor's context.
visitLiteralNull
public void visitLiteralNull([VisitorContext](VisitorContext.html) context)
Visitor method for [`LiteralNull`](../../magicdraw/classes/mdkernel/LiteralNull.html).
Parameters:
`context` - visitor's context.
visitLiteralReal
public void visitLiteralReal([VisitorContext](VisitorContext.html) context)
Visitor method for [`LiteralReal`](../../magicdraw/classes/mdkernel/LiteralReal.html).
Parameters:
`context` - visitor's context.
visitLiteralSpecification
public void visitLiteralSpecification([VisitorContext](VisitorContext.html) context)
Visitor method for [`LiteralSpecification`](../../magicdraw/classes/mdkernel/LiteralSpecification.html).
Parameters:
`context` - visitor's context.
visitLiteralString
public void visitLiteralString([VisitorContext](VisitorContext.html) context)
Visitor method for [`LiteralString`](../../magicdraw/classes/mdkernel/LiteralString.html).
Parameters:
`context` - visitor's context.
visitLiteralUnlimitedNatural
public void visitLiteralUnlimitedNatural([VisitorContext](VisitorContext.html) context)
Visitor method for [`LiteralUnlimitedNatural`](../../magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html).
Parameters:
`context` - visitor's context.
visitLoopNode
public void visitLoopNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`LoopNode`](../../magicdraw/activities/mdstructuredactivities/LoopNode.html).
Parameters:
`context` - visitor's context.
visitManifestation
public void visitManifestation([VisitorContext](VisitorContext.html) context)
Visitor method for [`Manifestation`](../../magicdraw/deployments/mdartifacts/Manifestation.html).
Parameters:
`context` - visitor's context.
visitMergeNode
public void visitMergeNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`MergeNode`](../../magicdraw/activities/mdintermediateactivities/MergeNode.html).
Parameters:
`context` - visitor's context.
visitMessage
public void visitMessage([VisitorContext](VisitorContext.html) context)
Visitor method for [`Message`](../../magicdraw/interactions/mdbasicinteractions/Message.html).
Parameters:
`context` - visitor's context.
visitMessageEnd
public void visitMessageEnd([VisitorContext](VisitorContext.html) context)
Visitor method for [`MessageEnd`](../../magicdraw/interactions/mdbasicinteractions/MessageEnd.html).
Parameters:
`context` - visitor's context.
visitMessageEvent
public void visitMessageEvent([VisitorContext](VisitorContext.html) context)
Visitor method for [`MessageEvent`](../../magicdraw/commonbehaviors/mdcommunications/MessageEvent.html).
Parameters:
`context` - visitor's context.
visitMessageOccurrenceSpecification
public void visitMessageOccurrenceSpecification([VisitorContext](VisitorContext.html) context)
Visitor method for [`MessageOccurrenceSpecification`](../../magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html).
Parameters:
`context` - visitor's context.
visitModel
public void visitModel([VisitorContext](VisitorContext.html) context)
Visitor method for [`Model`](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html).
Parameters:
`context` - visitor's context.
visitMultiplicityElement
public void visitMultiplicityElement([VisitorContext](VisitorContext.html) context)
Visitor method for [`MultiplicityElement`](../../magicdraw/classes/mdkernel/MultiplicityElement.html).
Parameters:
`context` - visitor's context.
visitNamedElement
public void visitNamedElement([VisitorContext](VisitorContext.html) context)
Visitor method for [`NamedElement`](../../magicdraw/classes/mdkernel/NamedElement.html).
Parameters:
`context` - visitor's context.
visitNamespace
public void visitNamespace([VisitorContext](VisitorContext.html) context)
Visitor method for [`Namespace`](../../magicdraw/classes/mdkernel/Namespace.html).
Parameters:
`context` - visitor's context.
visitNode
public void visitNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`Node`](../../magicdraw/deployments/mdnodes/Node.html).
Parameters:
`context` - visitor's context.
visitObjectFlow
public void visitObjectFlow([VisitorContext](VisitorContext.html) context)
Visitor method for [`ObjectFlow`](../../magicdraw/activities/mdbasicactivities/ObjectFlow.html).
Parameters:
`context` - visitor's context.
visitObjectNode
public void visitObjectNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`ObjectNode`](../../magicdraw/activities/mdbasicactivities/ObjectNode.html).
Parameters:
`context` - visitor's context.
visitObservation
public void visitObservation([VisitorContext](VisitorContext.html) context)
Visitor method for [`Observation`](../../magicdraw/commonbehaviors/mdsimpletime/Observation.html).
Parameters:
`context` - visitor's context.
visitOccurrenceSpecification
public void visitOccurrenceSpecification([VisitorContext](VisitorContext.html) context)
Visitor method for [`OccurrenceSpecification`](../../magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html).
Parameters:
`context` - visitor's context.
visitOpaqueAction
public void visitOpaqueAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`OpaqueAction`](../../magicdraw/actions/mdbasicactions/OpaqueAction.html).
Parameters:
`context` - visitor's context.
visitOpaqueBehavior
public void visitOpaqueBehavior([VisitorContext](VisitorContext.html) context)
Visitor method for [`OpaqueBehavior`](../../magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html).
Parameters:
`context` - visitor's context.
visitOpaqueExpression
public void visitOpaqueExpression([VisitorContext](VisitorContext.html) context)
Visitor method for [`OpaqueExpression`](../../magicdraw/classes/mdkernel/OpaqueExpression.html).
Parameters:
`context` - visitor's context.
visitOperation
public void visitOperation([VisitorContext](VisitorContext.html) context)
Visitor method for [`Operation`](../../magicdraw/classes/mdkernel/Operation.html).
Parameters:
`context` - visitor's context.
visitOperationTemplateParameter
public void visitOperationTemplateParameter([VisitorContext](VisitorContext.html) context)
Visitor method for [`OperationTemplateParameter`](../../magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html).
Parameters:
`context` - visitor's context.
visitOutputPin
public void visitOutputPin([VisitorContext](VisitorContext.html) context)
Visitor method for [`OutputPin`](../../magicdraw/actions/mdbasicactions/OutputPin.html).
Parameters:
`context` - visitor's context.
visitPackage
public void visitPackage([VisitorContext](VisitorContext.html) context)
Visitor method for [`Package`](../../magicdraw/classes/mdkernel/Package.html).
Parameters:
`context` - visitor's context.
visitPackageImport
public void visitPackageImport([VisitorContext](VisitorContext.html) context)
Visitor method for [`PackageImport`](../../magicdraw/classes/mdkernel/PackageImport.html).
Parameters:
`context` - visitor's context.
visitPackageMerge
public void visitPackageMerge([VisitorContext](VisitorContext.html) context)
Visitor method for [`PackageMerge`](../../magicdraw/classes/mdkernel/PackageMerge.html).
Parameters:
`context` - visitor's context.
visitPackageableElement
public void visitPackageableElement([VisitorContext](VisitorContext.html) context)
Visitor method for [`PackageableElement`](../../magicdraw/classes/mdkernel/PackageableElement.html).
Parameters:
`context` - visitor's context.
visitParameter
public void visitParameter([VisitorContext](VisitorContext.html) context)
Visitor method for [`Parameter`](../../magicdraw/classes/mdkernel/Parameter.html).
Parameters:
`context` - visitor's context.
visitParameterSet
public void visitParameterSet([VisitorContext](VisitorContext.html) context)
Visitor method for [`ParameterSet`](../../magicdraw/activities/mdcompleteactivities/ParameterSet.html).
Parameters:
`context` - visitor's context.
visitParameterableElement
public void visitParameterableElement([VisitorContext](VisitorContext.html) context)
Visitor method for [`ParameterableElement`](../../magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html).
Parameters:
`context` - visitor's context.
visitPartDecomposition
public void visitPartDecomposition([VisitorContext](VisitorContext.html) context)
Visitor method for [`PartDecomposition`](../../magicdraw/interactions/mdfragments/PartDecomposition.html).
Parameters:
`context` - visitor's context.
visitPin
public void visitPin([VisitorContext](VisitorContext.html) context)
Visitor method for [`Pin`](../../magicdraw/actions/mdbasicactions/Pin.html).
Parameters:
`context` - visitor's context.
visitPort
public void visitPort([VisitorContext](VisitorContext.html) context)
Visitor method for [`Port`](../../magicdraw/compositestructures/mdports/Port.html).
Parameters:
`context` - visitor's context.
visitPrimitiveType
public void visitPrimitiveType([VisitorContext](VisitorContext.html) context)
Visitor method for [`PrimitiveType`](../../magicdraw/classes/mdkernel/PrimitiveType.html).
Parameters:
`context` - visitor's context.
visitProfile
public void visitProfile([VisitorContext](VisitorContext.html) context)
Visitor method for [`Profile`](../../magicdraw/mdprofiles/Profile.html).
Parameters:
`context` - visitor's context.
visitProfileApplication
public void visitProfileApplication([VisitorContext](VisitorContext.html) context)
Visitor method for [`ProfileApplication`](../../magicdraw/mdprofiles/ProfileApplication.html).
Parameters:
`context` - visitor's context.
visitProperty
public void visitProperty([VisitorContext](VisitorContext.html) context)
Visitor method for [`Property`](../../magicdraw/classes/mdkernel/Property.html).
Parameters:
`context` - visitor's context.
visitProtocolConformance
public void visitProtocolConformance([VisitorContext](VisitorContext.html) context)
Visitor method for [`ProtocolConformance`](../../magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html).
Parameters:
`context` - visitor's context.
visitProtocolStateMachine
public void visitProtocolStateMachine([VisitorContext](VisitorContext.html) context)
Visitor method for [`ProtocolStateMachine`](../../magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html).
Parameters:
`context` - visitor's context.
visitProtocolTransition
public void visitProtocolTransition([VisitorContext](VisitorContext.html) context)
Visitor method for [`ProtocolTransition`](../../magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html).
Parameters:
`context` - visitor's context.
visitPseudostate
public void visitPseudostate([VisitorContext](VisitorContext.html) context)
Visitor method for [`Pseudostate`](../../magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html).
Parameters:
`context` - visitor's context.
visitQualifierValue
public void visitQualifierValue([VisitorContext](VisitorContext.html) context)
Visitor method for [`QualifierValue`](../../magicdraw/actions/mdcompleteactions/QualifierValue.html).
Parameters:
`context` - visitor's context.
visitRaiseExceptionAction
public void visitRaiseExceptionAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`RaiseExceptionAction`](../../magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html).
Parameters:
`context` - visitor's context.
visitReadExtentAction
public void visitReadExtentAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ReadExtentAction`](../../magicdraw/actions/mdcompleteactions/ReadExtentAction.html).
Parameters:
`context` - visitor's context.
visitReadIsClassifiedObjectAction
public void visitReadIsClassifiedObjectAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ReadIsClassifiedObjectAction`](../../magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html).
Parameters:
`context` - visitor's context.
visitReadLinkAction
public void visitReadLinkAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ReadLinkAction`](../../magicdraw/actions/mdintermediateactions/ReadLinkAction.html).
Parameters:
`context` - visitor's context.
visitReadLinkObjectEndAction
public void visitReadLinkObjectEndAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ReadLinkObjectEndAction`](../../magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html).
Parameters:
`context` - visitor's context.
visitReadLinkObjectEndQualifierAction
public void visitReadLinkObjectEndQualifierAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ReadLinkObjectEndQualifierAction`](../../magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html).
Parameters:
`context` - visitor's context.
visitReadSelfAction
public void visitReadSelfAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ReadSelfAction`](../../magicdraw/actions/mdintermediateactions/ReadSelfAction.html).
Parameters:
`context` - visitor's context.
visitReadStructuralFeatureAction
public void visitReadStructuralFeatureAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ReadStructuralFeatureAction`](../../magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html).
Parameters:
`context` - visitor's context.
visitReadVariableAction
public void visitReadVariableAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ReadVariableAction`](../../magicdraw/actions/mdstructuredactions/ReadVariableAction.html).
Parameters:
`context` - visitor's context.
visitRealization
public void visitRealization([VisitorContext](VisitorContext.html) context)
Visitor method for [`Realization`](../../magicdraw/classes/mddependencies/Realization.html).
Parameters:
`context` - visitor's context.
visitReception
public void visitReception([VisitorContext](VisitorContext.html) context)
Visitor method for [`Reception`](../../magicdraw/commonbehaviors/mdcommunications/Reception.html).
Parameters:
`context` - visitor's context.
visitReclassifyObjectAction
public void visitReclassifyObjectAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ReclassifyObjectAction`](../../magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html).
Parameters:
`context` - visitor's context.
visitRedefinableElement
public void visitRedefinableElement([VisitorContext](VisitorContext.html) context)
Visitor method for [`RedefinableElement`](../../magicdraw/classes/mdkernel/RedefinableElement.html).
Parameters:
`context` - visitor's context.
visitRedefinableTemplateSignature
public void visitRedefinableTemplateSignature([VisitorContext](VisitorContext.html) context)
Visitor method for [`RedefinableTemplateSignature`](../../magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html).
Parameters:
`context` - visitor's context.
visitReduceAction
public void visitReduceAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ReduceAction`](../../magicdraw/actions/mdcompleteactions/ReduceAction.html).
Parameters:
`context` - visitor's context.
visitRegion
public void visitRegion([VisitorContext](VisitorContext.html) context)
Visitor method for [`Region`](../../magicdraw/statemachines/mdbehaviorstatemachines/Region.html).
Parameters:
`context` - visitor's context.
visitRelationship
public void visitRelationship([VisitorContext](VisitorContext.html) context)
Visitor method for [`Relationship`](../../magicdraw/classes/mdkernel/Relationship.html).
Parameters:
`context` - visitor's context.
visitRemoveStructuralFeatureValueAction
public void visitRemoveStructuralFeatureValueAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`RemoveStructuralFeatureValueAction`](../../magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html).
Parameters:
`context` - visitor's context.
visitRemoveVariableValueAction
public void visitRemoveVariableValueAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`RemoveVariableValueAction`](../../magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html).
Parameters:
`context` - visitor's context.
visitReplyAction
public void visitReplyAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ReplyAction`](../../magicdraw/actions/mdcompleteactions/ReplyAction.html).
Parameters:
`context` - visitor's context.
visitSendObjectAction
public void visitSendObjectAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`SendObjectAction`](../../magicdraw/actions/mdintermediateactions/SendObjectAction.html).
Parameters:
`context` - visitor's context.
visitSendSignalAction
public void visitSendSignalAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`SendSignalAction`](../../magicdraw/actions/mdbasicactions/SendSignalAction.html).
Parameters:
`context` - visitor's context.
visitSequenceNode
public void visitSequenceNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`SequenceNode`](../../magicdraw/activities/mdstructuredactivities/SequenceNode.html).
Parameters:
`context` - visitor's context.
visitSignal
public void visitSignal([VisitorContext](VisitorContext.html) context)
Visitor method for [`Signal`](../../magicdraw/commonbehaviors/mdcommunications/Signal.html).
Parameters:
`context` - visitor's context.
visitSignalEvent
public void visitSignalEvent([VisitorContext](VisitorContext.html) context)
Visitor method for [`SignalEvent`](../../magicdraw/commonbehaviors/mdcommunications/SignalEvent.html).
Parameters:
`context` - visitor's context.
visitSlot
public void visitSlot([VisitorContext](VisitorContext.html) context)
Visitor method for [`Slot`](../../magicdraw/classes/mdkernel/Slot.html).
Parameters:
`context` - visitor's context.
visitStartClassifierBehaviorAction
public void visitStartClassifierBehaviorAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`StartClassifierBehaviorAction`](../../magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html).
Parameters:
`context` - visitor's context.
visitStartObjectBehaviorAction
public void visitStartObjectBehaviorAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`StartObjectBehaviorAction`](../../magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html).
Parameters:
`context` - visitor's context.
visitState
public void visitState([VisitorContext](VisitorContext.html) context)
Visitor method for [`State`](../../magicdraw/statemachines/mdbehaviorstatemachines/State.html).
Parameters:
`context` - visitor's context.
visitStateInvariant
public void visitStateInvariant([VisitorContext](VisitorContext.html) context)
Visitor method for [`StateInvariant`](../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html).
Parameters:
`context` - visitor's context.
visitStateMachine
public void visitStateMachine([VisitorContext](VisitorContext.html) context)
Visitor method for [`StateMachine`](../../magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html).
Parameters:
`context` - visitor's context.
visitStereotype
public void visitStereotype([VisitorContext](VisitorContext.html) context)
Visitor method for [`Stereotype`](../../magicdraw/mdprofiles/Stereotype.html).
Parameters:
`context` - visitor's context.
visitStringExpression
public void visitStringExpression([VisitorContext](VisitorContext.html) context)
Visitor method for [`StringExpression`](../../magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html).
Parameters:
`context` - visitor's context.
visitStructuralFeature
public void visitStructuralFeature([VisitorContext](VisitorContext.html) context)
Visitor method for [`StructuralFeature`](../../magicdraw/classes/mdkernel/StructuralFeature.html).
Parameters:
`context` - visitor's context.
visitStructuralFeatureAction
public void visitStructuralFeatureAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`StructuralFeatureAction`](../../magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html).
Parameters:
`context` - visitor's context.
visitStructuredActivityNode
public void visitStructuredActivityNode([VisitorContext](VisitorContext.html) context)
Visitor method for [`StructuredActivityNode`](../../magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html).
Parameters:
`context` - visitor's context.
visitStructuredClassifier
public void visitStructuredClassifier([VisitorContext](VisitorContext.html) context)
Visitor method for [`StructuredClassifier`](../../magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html).
Parameters:
`context` - visitor's context.
visitSubstitution
public void visitSubstitution([VisitorContext](VisitorContext.html) context)
Visitor method for [`Substitution`](../../magicdraw/classes/mddependencies/Substitution.html).
Parameters:
`context` - visitor's context.
visitTemplateBinding
public void visitTemplateBinding([VisitorContext](VisitorContext.html) context)
Visitor method for [`TemplateBinding`](../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html).
Parameters:
`context` - visitor's context.
visitTemplateParameter
public void visitTemplateParameter([VisitorContext](VisitorContext.html) context)
Visitor method for [`TemplateParameter`](../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html).
Parameters:
`context` - visitor's context.
visitTemplateParameterSubstitution
public void visitTemplateParameterSubstitution([VisitorContext](VisitorContext.html) context)
Visitor method for [`TemplateParameterSubstitution`](../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html).
Parameters:
`context` - visitor's context.
visitTemplateSignature
public void visitTemplateSignature([VisitorContext](VisitorContext.html) context)
Visitor method for [`TemplateSignature`](../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html).
Parameters:
`context` - visitor's context.
visitTemplateableElement
public void visitTemplateableElement([VisitorContext](VisitorContext.html) context)
Visitor method for [`TemplateableElement`](../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html).
Parameters:
`context` - visitor's context.
visitTestIdentityAction
public void visitTestIdentityAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`TestIdentityAction`](../../magicdraw/actions/mdintermediateactions/TestIdentityAction.html).
Parameters:
`context` - visitor's context.
visitTimeConstraint
public void visitTimeConstraint([VisitorContext](VisitorContext.html) context)
Visitor method for [`TimeConstraint`](../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html).
Parameters:
`context` - visitor's context.
visitTimeEvent
public void visitTimeEvent([VisitorContext](VisitorContext.html) context)
Visitor method for [`TimeEvent`](../../magicdraw/commonbehaviors/mdcommunications/TimeEvent.html).
Parameters:
`context` - visitor's context.
visitTimeExpression
public void visitTimeExpression([VisitorContext](VisitorContext.html) context)
Visitor method for [`TimeExpression`](../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html).
Parameters:
`context` - visitor's context.
visitTimeInterval
public void visitTimeInterval([VisitorContext](VisitorContext.html) context)
Visitor method for [`TimeInterval`](../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html).
Parameters:
`context` - visitor's context.
visitTimeObservation
public void visitTimeObservation([VisitorContext](VisitorContext.html) context)
Visitor method for [`TimeObservation`](../../magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html).
Parameters:
`context` - visitor's context.
visitTransition
public void visitTransition([VisitorContext](VisitorContext.html) context)
Visitor method for [`Transition`](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html).
Parameters:
`context` - visitor's context.
visitTrigger
public void visitTrigger([VisitorContext](VisitorContext.html) context)
Visitor method for [`Trigger`](../../magicdraw/commonbehaviors/mdcommunications/Trigger.html).
Parameters:
`context` - visitor's context.
visitType
public void visitType([VisitorContext](VisitorContext.html) context)
Visitor method for [`Type`](../../magicdraw/classes/mdkernel/Type.html).
Parameters:
`context` - visitor's context.
visitTypedElement
public void visitTypedElement([VisitorContext](VisitorContext.html) context)
Visitor method for [`TypedElement`](../../magicdraw/classes/mdkernel/TypedElement.html).
Parameters:
`context` - visitor's context.
visitUnmarshallAction
public void visitUnmarshallAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`UnmarshallAction`](../../magicdraw/actions/mdcompleteactions/UnmarshallAction.html).
Parameters:
`context` - visitor's context.
visitUsage
public void visitUsage([VisitorContext](VisitorContext.html) context)
Visitor method for [`Usage`](../../magicdraw/classes/mddependencies/Usage.html).
Parameters:
`context` - visitor's context.
visitUseCase
public void visitUseCase([VisitorContext](VisitorContext.html) context)
Visitor method for [`UseCase`](../../magicdraw/mdusecases/UseCase.html).
Parameters:
`context` - visitor's context.
visitValuePin
public void visitValuePin([VisitorContext](VisitorContext.html) context)
Visitor method for [`ValuePin`](../../magicdraw/actions/mdbasicactions/ValuePin.html).
Parameters:
`context` - visitor's context.
visitValueSpecification
public void visitValueSpecification([VisitorContext](VisitorContext.html) context)
Visitor method for [`ValueSpecification`](../../magicdraw/classes/mdkernel/ValueSpecification.html).
Parameters:
`context` - visitor's context.
visitValueSpecificationAction
public void visitValueSpecificationAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`ValueSpecificationAction`](../../magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html).
Parameters:
`context` - visitor's context.
visitVariable
public void visitVariable([VisitorContext](VisitorContext.html) context)
Visitor method for [`Variable`](../../magicdraw/activities/mdstructuredactivities/Variable.html).
Parameters:
`context` - visitor's context.
visitVariableAction
public void visitVariableAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`VariableAction`](../../magicdraw/actions/mdstructuredactions/VariableAction.html).
Parameters:
`context` - visitor's context.
visitVertex
public void visitVertex([VisitorContext](VisitorContext.html) context)
Visitor method for [`Vertex`](../../magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html).
Parameters:
`context` - visitor's context.
visitWriteLinkAction
public void visitWriteLinkAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`WriteLinkAction`](../../magicdraw/actions/mdintermediateactions/WriteLinkAction.html).
Parameters:
`context` - visitor's context.
visitWriteStructuralFeatureAction
public void visitWriteStructuralFeatureAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`WriteStructuralFeatureAction`](../../magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html).
Parameters:
`context` - visitor's context.
visitWriteVariableAction
public void visitWriteVariableAction([VisitorContext](VisitorContext.html) context)
Visitor method for [`WriteVariableAction`](../../magicdraw/actions/mdstructuredactions/WriteVariableAction.html).
Parameters:
`context` - visitor's context.
visitTaggedValue
public void visitTaggedValue([VisitorContext](VisitorContext.html) context)
visitStringTaggedValue
public void visitStringTaggedValue([VisitorContext](VisitorContext.html) context)
visitBooleanTaggedValue
public void visitBooleanTaggedValue([VisitorContext](VisitorContext.html) context)
visitElementTaggedValue
public void visitElementTaggedValue([VisitorContext](VisitorContext.html) context)
visitRealTaggedValue
public void visitRealTaggedValue([VisitorContext](VisitorContext.html) context)
visitIntegerTaggedValue
public void visitIntegerTaggedValue([VisitorContext](VisitorContext.html) context)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.reflect</a></div>
<h1 class="title" title="Class ClassTypeHierarchyVisitor">Class ClassTypeHierarchyVisitor</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.reflect.ClassTypeHierarchyVisitor</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">ClassTypeHierarchyVisitor</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ClassTypeHierarchyVisitor</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(java.lang.Class)">visit</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitAbstraction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAbstraction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Abstraction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitAcceptCallAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAcceptCallAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>AcceptCallAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitAcceptEventAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAcceptEventAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>AcceptEventAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>Action</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitActionExecutionSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActionExecutionSpecification</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ActionExecutionSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitActionInputPin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActionInputPin</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ActionInputPin</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitActivity(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivity</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>Activity</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitActivityEdge(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivityEdge</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityEdge</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitActivityFinalNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivityFinalNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityFinalNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitActivityGroup(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivityGroup</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityGroup</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitActivityNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivityNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitActivityParameterNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivityParameterNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityParameterNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitActivityPartition(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivityPartition</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ActivityPartition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitActor(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActor</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Actor</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitAddStructuralFeatureValueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAddStructuralFeatureValueAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>AddStructuralFeatureValueAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitAddVariableValueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAddVariableValueAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>AddVariableValueAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitAnyReceiveEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAnyReceiveEvent</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>AnyReceiveEvent</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitArtifact(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitArtifact</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code>Artifact</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitAssociation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAssociation</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Association</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitAssociationClass(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAssociationClass</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses"><code>AssociationClass</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitBehavior(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitBehavior</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>Behavior</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitBehavioralFeature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitBehavioralFeature</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>BehavioralFeature</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitBehavioredClassifier(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitBehavioredClassifier</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>BehavioredClassifier</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitBehaviorExecutionSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitBehaviorExecutionSpecification</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>BehaviorExecutionSpecification</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitBooleanTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitBooleanTaggedValue</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitBroadcastSignalAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitBroadcastSignalAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>BroadcastSignalAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitCallAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCallAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitCallBehaviorAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCallBehaviorAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallBehaviorAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitCallEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCallEvent</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>CallEvent</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitCallOperationAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCallOperationAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallOperationAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitCentralBufferNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCentralBufferNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>CentralBufferNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitChangeEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitChangeEvent</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>ChangeEvent</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitClass(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClass</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Class</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitClassifier(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClassifier</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitClassifierTemplateParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClassifierTemplateParameter</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ClassifierTemplateParameter</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitClause(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClause</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Clause</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitClearAssociationAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClearAssociationAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ClearAssociationAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitClearStructuralFeatureAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClearStructuralFeatureAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ClearStructuralFeatureAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitClearVariableAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClearVariableAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ClearVariableAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitCollaboration(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCollaboration</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code>Collaboration</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitCollaborationUse(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCollaborationUse</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code>CollaborationUse</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitCombinedFragment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCombinedFragment</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>CombinedFragment</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitComment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitComment</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Comment</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitCommunicationPath(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCommunicationPath</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>CommunicationPath</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitComponent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitComponent</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>Component</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitComponentRealization(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitComponentRealization</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>ComponentRealization</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitConditionalNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConditionalNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>ConditionalNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitConnectableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConnectableElement</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>ConnectableElement</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitConnectableElementTemplateParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConnectableElementTemplateParameter</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ConnectableElementTemplateParameter</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitConnectionPointReference(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConnectionPointReference</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>ConnectionPointReference</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitConnector(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConnector</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>Connector</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitConnectorEnd(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConnectorEnd</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>ConnectorEnd</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitConsiderIgnoreFragment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConsiderIgnoreFragment</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>ConsiderIgnoreFragment</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConstraint</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitContinuation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitContinuation</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>Continuation</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitControlFlow(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitControlFlow</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ControlFlow</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitControlNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitControlNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ControlNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitCreateLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCreateLinkAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>CreateLinkAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitCreateLinkObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCreateLinkObjectAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>CreateLinkObjectAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitCreateObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCreateObjectAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>CreateObjectAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDataStoreNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDataStoreNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>DataStoreNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDataType(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDataType</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>DataType</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDecisionNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDecisionNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>DecisionNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDependency(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDependency</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Dependency</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDeployedArtifact(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDeployedArtifact</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>DeployedArtifact</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDeployment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDeployment</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Deployment</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDeploymentSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDeploymentSpecification</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments"><code>DeploymentSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDeploymentTarget(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDeploymentTarget</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>DeploymentTarget</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDestroyLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDestroyLinkAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>DestroyLinkAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDestroyObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDestroyObjectAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>DestroyObjectAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDestructionOccurrenceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDestructionOccurrenceSpecification</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>DestructionOccurrenceSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDevice(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDevice</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Device</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDiagram(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDiagram</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Diagram</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDirectedRelationship(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDirectedRelationship</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>DirectedRelationship</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDuration(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDuration</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Duration</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDurationConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDurationConstraint</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationConstraint</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDurationInterval(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDurationInterval</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationInterval</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitDurationObservation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDurationObservation</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationObservation</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitElement</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitElementImport(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitElementImport</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementImport</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitElementTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitElementTaggedValue</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitElementValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitElementValue</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementValue</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitEncapsulatedClassifier(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitEncapsulatedClassifier</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code>EncapsulatedClassifier</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitEnumeration(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitEnumeration</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Enumeration</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitEnumerationLiteral(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitEnumerationLiteral</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>EnumerationLiteral</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitEvent</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Event</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitExceptionHandler(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExceptionHandler</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExceptionHandler</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitExecutableNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExecutableNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>ExecutableNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitExecutionEnvironment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExecutionEnvironment</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>ExecutionEnvironment</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitExecutionOccurrenceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExecutionOccurrenceSpecification</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ExecutionOccurrenceSpecification</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitExecutionSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExecutionSpecification</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ExecutionSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitExpansionNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExpansionNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExpansionNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitExpansionRegion(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExpansionRegion</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExpansionRegion</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitExpression(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExpression</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Expression</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitExtend(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExtend</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Extend</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitExtension(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExtension</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Extension</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitExtensionEnd(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExtensionEnd</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>ExtensionEnd</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitExtensionPoint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExtensionPoint</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>ExtensionPoint</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitFeature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitFeature</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Feature</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitFinalNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitFinalNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>FinalNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitFinalState(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitFinalState</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>FinalState</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitFlowFinalNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitFlowFinalNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>FlowFinalNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitForkNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitForkNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ForkNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitFunctionBehavior(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitFunctionBehavior</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>FunctionBehavior</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitGate(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitGate</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>Gate</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitGeneralization(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitGeneralization</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Generalization</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitGeneralizationSet(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitGeneralizationSet</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes"><code>GeneralizationSet</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitGeneralOrdering(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitGeneralOrdering</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>GeneralOrdering</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitImage(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitImage</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Image</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInclude(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInclude</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Include</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInformationFlow(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInformationFlow</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationFlow</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInformationItem(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInformationItem</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationItem</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInitialNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInitialNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>InitialNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInputPin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInputPin</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>InputPin</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInstanceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInstanceSpecification</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInstanceValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInstanceValue</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceValue</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitIntegerTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitIntegerTaggedValue</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInteraction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInteraction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Interaction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInteractionConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInteractionConstraint</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionConstraint</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInteractionFragment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInteractionFragment</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>InteractionFragment</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInteractionOperand(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInteractionOperand</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionOperand</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInteractionUse(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInteractionUse</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionUse</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInterface(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInterface</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>Interface</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInterfaceRealization(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInterfaceRealization</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>InterfaceRealization</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInterruptibleActivityRegion(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInterruptibleActivityRegion</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>InterruptibleActivityRegion</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInterval(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInterval</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Interval</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitIntervalConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitIntervalConstraint</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>IntervalConstraint</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitInvocationAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInvocationAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>InvocationAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitJoinNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitJoinNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>JoinNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitLifeline(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLifeline</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Lifeline</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLinkAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitLinkEndCreationData(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLinkEndCreationData</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndCreationData</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitLinkEndData(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLinkEndData</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndData</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitLinkEndDestructionData(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLinkEndDestructionData</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndDestructionData</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitLiteralBoolean(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralBoolean</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralBoolean</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitLiteralInteger(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralInteger</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralInteger</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitLiteralNull(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralNull</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralNull</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitLiteralReal(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralReal</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralReal</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitLiteralSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralSpecification</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitLiteralString(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralString</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralString</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitLiteralUnlimitedNatural(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralUnlimitedNatural</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralUnlimitedNatural</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitLoopNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLoopNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>LoopNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitManifestation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitManifestation</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code>Manifestation</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitMergeNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitMergeNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>MergeNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitMessage(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitMessage</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Message</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitMessageEnd(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitMessageEnd</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageEnd</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitMessageEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitMessageEvent</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>MessageEvent</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitMessageOccurrenceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitMessageOccurrenceSpecification</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageOccurrenceSpecification</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitModel(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitModel</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels"><code>Model</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitMultiplicityElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitMultiplicityElement</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>MultiplicityElement</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitNamedElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitNamedElement</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>NamedElement</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitNamespace(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitNamespace</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Namespace</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Node</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitObjectFlow(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitObjectFlow</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectFlow</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitObjectNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitObjectNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitObservation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitObservation</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Observation</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitOccurrenceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOccurrenceSpecification</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>OccurrenceSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitOpaqueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOpaqueAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>OpaqueAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitOpaqueBehavior(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOpaqueBehavior</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>OpaqueBehavior</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitOpaqueExpression(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOpaqueExpression</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>OpaqueExpression</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitOperation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOperation</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Operation</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitOperationTemplateParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOperationTemplateParameter</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>OperationTemplateParameter</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitOutputPin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOutputPin</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>OutputPin</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitPackage(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPackage</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Package</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitPackageableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPackageableElement</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageableElement</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitPackageImport(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPackageImport</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageImport</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitPackageMerge(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPackageMerge</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageMerge</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitParameter</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Parameter</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitParameterableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitParameterableElement</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ParameterableElement</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitParameterSet(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitParameterSet</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>ParameterSet</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitPartDecomposition(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPartDecomposition</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>PartDecomposition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitPin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPin</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>Pin</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitPort(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPort</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code>Port</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitPrimitiveType(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPrimitiveType</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PrimitiveType</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitProfile(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitProfile</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Profile</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitProfileApplication(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitProfileApplication</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>ProfileApplication</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitProperty(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitProperty</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitProtocolConformance(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitProtocolConformance</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolConformance</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitProtocolStateMachine(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitProtocolStateMachine</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolStateMachine</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitProtocolTransition(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitProtocolTransition</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolTransition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitPseudostate(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPseudostate</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Pseudostate</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitQualifierValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitQualifierValue</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>QualifierValue</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitRaiseExceptionAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRaiseExceptionAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>RaiseExceptionAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitReadExtentAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadExtentAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadExtentAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitReadIsClassifiedObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadIsClassifiedObjectAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadIsClassifiedObjectAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitReadLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadLinkAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadLinkAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitReadLinkObjectEndAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadLinkObjectEndAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadLinkObjectEndAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitReadLinkObjectEndQualifierAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadLinkObjectEndQualifierAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadLinkObjectEndQualifierAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitReadSelfAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadSelfAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadSelfAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitReadStructuralFeatureAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadStructuralFeatureAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadStructuralFeatureAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitReadVariableAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadVariableAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ReadVariableAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitRealization(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRealization</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Realization</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitRealTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRealTaggedValue</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitReception(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReception</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Reception</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitReclassifyObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReclassifyObjectAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReclassifyObjectAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitRedefinableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRedefinableElement</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>RedefinableElement</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitRedefinableTemplateSignature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRedefinableTemplateSignature</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>RedefinableTemplateSignature</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitReduceAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReduceAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReduceAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitRegion(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRegion</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Region</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitRelationship(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRelationship</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Relationship</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitRemoveStructuralFeatureValueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRemoveStructuralFeatureValueAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>RemoveStructuralFeatureValueAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitRemoveVariableValueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRemoveVariableValueAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>RemoveVariableValueAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitReplyAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReplyAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReplyAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitSendObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSendObjectAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>SendObjectAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitSendSignalAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSendSignalAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>SendSignalAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitSequenceNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSequenceNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>SequenceNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitSignal(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSignal</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Signal</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitSignalEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSignalEvent</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>SignalEvent</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitSlot(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSlot</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Slot</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitStartClassifierBehaviorAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStartClassifierBehaviorAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>StartClassifierBehaviorAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitStartObjectBehaviorAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStartObjectBehaviorAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>StartObjectBehaviorAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitState(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitState</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>State</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitStateInvariant(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStateInvariant</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>StateInvariant</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitStateMachine(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStateMachine</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>StateMachine</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitStereotype(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStereotype</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Stereotype</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitStringExpression(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStringExpression</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>StringExpression</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitStringTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStringTaggedValue</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitStructuralFeature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStructuralFeature</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>StructuralFeature</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitStructuralFeatureAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStructuralFeatureAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>StructuralFeatureAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitStructuredActivityNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStructuredActivityNode</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>StructuredActivityNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitStructuredClassifier(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStructuredClassifier</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>StructuredClassifier</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitSubstitution(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSubstitution</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Substitution</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTaggedValue</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTemplateableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTemplateableElement</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateableElement</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTemplateBinding(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTemplateBinding</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateBinding</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTemplateParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTemplateParameter</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameter</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTemplateParameterSubstitution(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTemplateParameterSubstitution</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameterSubstitution</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTemplateSignature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTemplateSignature</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateSignature</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTestIdentityAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTestIdentityAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>TestIdentityAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTimeConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTimeConstraint</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeConstraint</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTimeEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTimeEvent</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>TimeEvent</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTimeExpression(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTimeExpression</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeExpression</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTimeInterval(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTimeInterval</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeInterval</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTimeObservation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTimeObservation</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeObservation</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTransition(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTransition</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Transition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTrigger(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTrigger</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Trigger</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitType(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitType</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Type</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitTypedElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTypedElement</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>TypedElement</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitUnmarshallAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitUnmarshallAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>UnmarshallAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitUsage(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitUsage</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Usage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitUseCase(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitUseCase</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>UseCase</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitValuePin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitValuePin</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>ValuePin</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitValueSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitValueSpecification</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ValueSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitValueSpecificationAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitValueSpecificationAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ValueSpecificationAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitVariable(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitVariable</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Variable</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitVariableAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitVariableAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>VariableAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitVertex(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitVertex</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Vertex</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitWriteLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitWriteLinkAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>WriteLinkAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitWriteStructuralFeatureAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitWriteStructuralFeatureAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>WriteStructuralFeatureAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visitWriteVariableAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitWriteVariableAction</a><wbr/>(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>WriteVariableAction</code></a>.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ClassTypeHierarchyVisitor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ClassTypeHierarchyVisitor</span>()</div>
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
<section class="detail" id="visit(java.lang.Class)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; type)</span>
                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAbstraction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAbstraction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitAbstraction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Abstraction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAcceptCallAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAcceptCallAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitAcceptCallAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>AcceptCallAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAcceptEventAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAcceptEventAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitAcceptEventAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>AcceptEventAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>Action</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActionExecutionSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActionExecutionSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitActionExecutionSpecification</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ActionExecutionSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActionInputPin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActionInputPin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitActionInputPin</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ActionInputPin</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivity(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitActivity</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>Activity</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityEdge(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivityEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitActivityEdge</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityEdge</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityFinalNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivityFinalNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitActivityFinalNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityFinalNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityGroup(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivityGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitActivityGroup</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityGroup</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivityNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitActivityNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityParameterNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivityParameterNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitActivityParameterNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityParameterNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityPartition(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivityPartition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitActivityPartition</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ActivityPartition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActor(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitActor</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Actor</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAddStructuralFeatureValueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAddStructuralFeatureValueAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitAddStructuralFeatureValueAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>AddStructuralFeatureValueAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAddVariableValueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAddVariableValueAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitAddVariableValueAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>AddVariableValueAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAnyReceiveEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAnyReceiveEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitAnyReceiveEvent</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>AnyReceiveEvent</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitArtifact(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitArtifact</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitArtifact</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code>Artifact</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssociation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAssociation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitAssociation</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Association</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssociationClass(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAssociationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitAssociationClass</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses"><code>AssociationClass</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehavior(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitBehavior</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>Behavior</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehaviorExecutionSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitBehaviorExecutionSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitBehaviorExecutionSpecification</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>BehaviorExecutionSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehavioralFeature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitBehavioralFeature</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitBehavioralFeature</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>BehavioralFeature</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehavioredClassifier(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitBehavioredClassifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitBehavioredClassifier</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>BehavioredClassifier</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBroadcastSignalAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitBroadcastSignalAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitBroadcastSignalAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>BroadcastSignalAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCallAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCallAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitCallAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCallBehaviorAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCallBehaviorAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitCallBehaviorAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallBehaviorAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCallEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCallEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitCallEvent</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>CallEvent</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCallOperationAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCallOperationAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitCallOperationAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallOperationAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCentralBufferNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCentralBufferNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitCentralBufferNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>CentralBufferNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitChangeEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitChangeEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitChangeEvent</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>ChangeEvent</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClass(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitClass</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Class</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClassifier(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClassifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitClassifier</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClassifierTemplateParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClassifierTemplateParameter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitClassifierTemplateParameter</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ClassifierTemplateParameter</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClause(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClause</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitClause</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Clause</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClearAssociationAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClearAssociationAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitClearAssociationAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ClearAssociationAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClearStructuralFeatureAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClearStructuralFeatureAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitClearStructuralFeatureAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ClearStructuralFeatureAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClearVariableAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClearVariableAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitClearVariableAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ClearVariableAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCollaboration(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCollaboration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitCollaboration</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code>Collaboration</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCollaborationUse(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCollaborationUse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitCollaborationUse</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code>CollaborationUse</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCombinedFragment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCombinedFragment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitCombinedFragment</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>CombinedFragment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitComment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitComment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitComment</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Comment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCommunicationPath(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCommunicationPath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitCommunicationPath</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>CommunicationPath</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitComponent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitComponent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitComponent</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>Component</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitComponentRealization(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitComponentRealization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitComponentRealization</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>ComponentRealization</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConditionalNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConditionalNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitConditionalNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>ConditionalNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConnectableElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitConnectableElement</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>ConnectableElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectableElementTemplateParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConnectableElementTemplateParameter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitConnectableElementTemplateParameter</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ConnectableElementTemplateParameter</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectionPointReference(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConnectionPointReference</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitConnectionPointReference</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>ConnectionPointReference</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnector(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConnector</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitConnector</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>Connector</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectorEnd(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConnectorEnd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitConnectorEnd</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>ConnectorEnd</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConsiderIgnoreFragment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConsiderIgnoreFragment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitConsiderIgnoreFragment</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>ConsiderIgnoreFragment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitConstraint</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitContinuation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitContinuation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitContinuation</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>Continuation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitControlFlow(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitControlFlow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitControlFlow</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ControlFlow</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitControlNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitControlNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitControlNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ControlNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCreateLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCreateLinkAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitCreateLinkAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>CreateLinkAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCreateLinkObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCreateLinkObjectAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitCreateLinkObjectAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>CreateLinkObjectAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCreateObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCreateObjectAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitCreateObjectAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>CreateObjectAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDataStoreNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDataStoreNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDataStoreNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>DataStoreNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDataType(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDataType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDataType</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>DataType</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDecisionNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDecisionNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDecisionNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>DecisionNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDependency(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDependency</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDependency</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Dependency</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDeployedArtifact(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDeployedArtifact</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDeployedArtifact</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>DeployedArtifact</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDeployment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDeployment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDeployment</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Deployment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDeploymentSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDeploymentSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDeploymentSpecification</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments"><code>DeploymentSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDeploymentTarget(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDeploymentTarget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDeploymentTarget</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>DeploymentTarget</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDestroyLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDestroyLinkAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDestroyLinkAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>DestroyLinkAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDestroyObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDestroyObjectAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDestroyObjectAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>DestroyObjectAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDestructionOccurrenceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDestructionOccurrenceSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDestructionOccurrenceSpecification</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>DestructionOccurrenceSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDevice(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDevice</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDevice</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Device</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDiagram(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDiagram</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Diagram</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDirectedRelationship(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDirectedRelationship</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDirectedRelationship</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>DirectedRelationship</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDuration(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDuration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDuration</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Duration</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDurationConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDurationConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDurationConstraint</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationConstraint</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDurationInterval(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDurationInterval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDurationInterval</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationInterval</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDurationObservation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDurationObservation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitDurationObservation</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationObservation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitElement</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElementImport(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitElementImport</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitElementImport</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementImport</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElementValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitElementValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitElementValue</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEncapsulatedClassifier(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitEncapsulatedClassifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitEncapsulatedClassifier</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code>EncapsulatedClassifier</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEnumeration(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitEnumeration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitEnumeration</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Enumeration</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEnumerationLiteral(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitEnumerationLiteral</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitEnumerationLiteral</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>EnumerationLiteral</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitEvent</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Event</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExceptionHandler(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExceptionHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitExceptionHandler</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExceptionHandler</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExecutableNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExecutableNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitExecutableNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>ExecutableNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExecutionEnvironment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExecutionEnvironment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitExecutionEnvironment</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>ExecutionEnvironment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExecutionOccurrenceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExecutionOccurrenceSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitExecutionOccurrenceSpecification</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ExecutionOccurrenceSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExecutionSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExecutionSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitExecutionSpecification</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ExecutionSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExpansionNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExpansionNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitExpansionNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExpansionNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExpansionRegion(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExpansionRegion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitExpansionRegion</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExpansionRegion</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExpression(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitExpression</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Expression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExtend(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExtend</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitExtend</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Extend</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExtension(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExtension</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitExtension</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Extension</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExtensionEnd(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExtensionEnd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitExtensionEnd</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>ExtensionEnd</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExtensionPoint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExtensionPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitExtensionPoint</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>ExtensionPoint</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitFeature</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitFeature</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Feature</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFinalNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitFinalNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitFinalNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>FinalNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFinalState(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitFinalState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitFinalState</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>FinalState</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFlowFinalNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitFlowFinalNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitFlowFinalNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>FlowFinalNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitForkNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitForkNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitForkNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ForkNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFunctionBehavior(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitFunctionBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitFunctionBehavior</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>FunctionBehavior</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitGate(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitGate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitGate</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>Gate</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitGeneralOrdering(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitGeneralOrdering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitGeneralOrdering</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>GeneralOrdering</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitGeneralization(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitGeneralization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitGeneralization</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Generalization</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitGeneralizationSet(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitGeneralizationSet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitGeneralizationSet</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes"><code>GeneralizationSet</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitImage(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitImage</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Image</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInclude(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInclude</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInclude</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Include</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInformationFlow(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInformationFlow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInformationFlow</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationFlow</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInformationItem(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInformationItem</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInformationItem</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationItem</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInitialNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInitialNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInitialNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>InitialNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInputPin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInputPin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInputPin</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>InputPin</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInstanceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInstanceSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInstanceSpecification</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInstanceValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInstanceValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInstanceValue</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteraction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInteraction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInteraction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Interaction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteractionConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInteractionConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInteractionConstraint</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionConstraint</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteractionFragment(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInteractionFragment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInteractionFragment</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>InteractionFragment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteractionOperand(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInteractionOperand</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInteractionOperand</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionOperand</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteractionUse(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInteractionUse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInteractionUse</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionUse</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterface(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInterface</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInterface</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>Interface</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterfaceRealization(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInterfaceRealization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInterfaceRealization</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>InterfaceRealization</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterruptibleActivityRegion(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInterruptibleActivityRegion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInterruptibleActivityRegion</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>InterruptibleActivityRegion</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterval(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInterval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInterval</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Interval</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitIntervalConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitIntervalConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitIntervalConstraint</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>IntervalConstraint</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInvocationAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInvocationAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitInvocationAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>InvocationAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitJoinNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitJoinNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitJoinNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>JoinNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLifeline(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLifeline</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitLifeline</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Lifeline</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLinkAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitLinkAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkEndCreationData(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLinkEndCreationData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitLinkEndCreationData</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndCreationData</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkEndData(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLinkEndData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitLinkEndData</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndData</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkEndDestructionData(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLinkEndDestructionData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitLinkEndDestructionData</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndDestructionData</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralBoolean(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralBoolean</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitLiteralBoolean</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralBoolean</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralInteger(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralInteger</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitLiteralInteger</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralInteger</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralNull(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralNull</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitLiteralNull</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralNull</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralReal(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralReal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitLiteralReal</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralReal</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitLiteralSpecification</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralString(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitLiteralString</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralString</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralUnlimitedNatural(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralUnlimitedNatural</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitLiteralUnlimitedNatural</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralUnlimitedNatural</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLoopNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLoopNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitLoopNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>LoopNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitManifestation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitManifestation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitManifestation</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code>Manifestation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMergeNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitMergeNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitMergeNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>MergeNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMessage(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitMessage</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Message</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMessageEnd(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitMessageEnd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitMessageEnd</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageEnd</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMessageEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitMessageEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitMessageEvent</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>MessageEvent</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMessageOccurrenceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitMessageOccurrenceSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitMessageOccurrenceSpecification</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageOccurrenceSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitModel(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitModel</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels"><code>Model</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMultiplicityElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitMultiplicityElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitMultiplicityElement</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>MultiplicityElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNamedElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitNamedElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitNamedElement</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>NamedElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNamespace(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitNamespace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitNamespace</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Namespace</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Node</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitObjectFlow(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitObjectFlow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitObjectFlow</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectFlow</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitObjectNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitObjectNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitObjectNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitObservation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitObservation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitObservation</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Observation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOccurrenceSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOccurrenceSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitOccurrenceSpecification</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>OccurrenceSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOpaqueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOpaqueAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitOpaqueAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>OpaqueAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOpaqueBehavior(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOpaqueBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitOpaqueBehavior</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>OpaqueBehavior</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOpaqueExpression(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOpaqueExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitOpaqueExpression</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>OpaqueExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOperation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOperation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitOperation</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Operation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOperationTemplateParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOperationTemplateParameter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitOperationTemplateParameter</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>OperationTemplateParameter</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOutputPin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOutputPin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitOutputPin</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>OutputPin</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackage(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPackage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitPackage</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Package</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackageImport(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPackageImport</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitPackageImport</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageImport</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackageMerge(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPackageMerge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitPackageMerge</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageMerge</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackageableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPackageableElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitPackageableElement</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageableElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitParameter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitParameter</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Parameter</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitParameterSet(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitParameterSet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitParameterSet</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>ParameterSet</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitParameterableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitParameterableElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitParameterableElement</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ParameterableElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPartDecomposition(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPartDecomposition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitPartDecomposition</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>PartDecomposition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitPin</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>Pin</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPort(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitPort</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code>Port</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPrimitiveType(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPrimitiveType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitPrimitiveType</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PrimitiveType</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProfile(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitProfile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitProfile</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Profile</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProfileApplication(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitProfileApplication</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitProfileApplication</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>ProfileApplication</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProperty(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitProperty</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProtocolConformance(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitProtocolConformance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitProtocolConformance</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolConformance</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProtocolStateMachine(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitProtocolStateMachine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitProtocolStateMachine</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolStateMachine</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProtocolTransition(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitProtocolTransition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitProtocolTransition</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolTransition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPseudostate(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPseudostate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitPseudostate</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Pseudostate</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitQualifierValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitQualifierValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitQualifierValue</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>QualifierValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRaiseExceptionAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRaiseExceptionAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitRaiseExceptionAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>RaiseExceptionAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadExtentAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadExtentAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitReadExtentAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadExtentAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadIsClassifiedObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadIsClassifiedObjectAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitReadIsClassifiedObjectAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadIsClassifiedObjectAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadLinkAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitReadLinkAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadLinkAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadLinkObjectEndAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadLinkObjectEndAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitReadLinkObjectEndAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadLinkObjectEndAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadLinkObjectEndQualifierAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadLinkObjectEndQualifierAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitReadLinkObjectEndQualifierAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadLinkObjectEndQualifierAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadSelfAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadSelfAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitReadSelfAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadSelfAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadStructuralFeatureAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadStructuralFeatureAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitReadStructuralFeatureAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadStructuralFeatureAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadVariableAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadVariableAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitReadVariableAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ReadVariableAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRealization(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRealization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitRealization</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Realization</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReception(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReception</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitReception</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Reception</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReclassifyObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReclassifyObjectAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitReclassifyObjectAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReclassifyObjectAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRedefinableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRedefinableElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitRedefinableElement</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>RedefinableElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRedefinableTemplateSignature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRedefinableTemplateSignature</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitRedefinableTemplateSignature</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>RedefinableTemplateSignature</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReduceAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReduceAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitReduceAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReduceAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRegion(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRegion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitRegion</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Region</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRelationship(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRelationship</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitRelationship</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Relationship</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRemoveStructuralFeatureValueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRemoveStructuralFeatureValueAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitRemoveStructuralFeatureValueAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>RemoveStructuralFeatureValueAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRemoveVariableValueAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRemoveVariableValueAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitRemoveVariableValueAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>RemoveVariableValueAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReplyAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReplyAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitReplyAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReplyAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSendObjectAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSendObjectAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitSendObjectAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>SendObjectAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSendSignalAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSendSignalAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitSendSignalAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>SendSignalAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSequenceNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSequenceNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitSequenceNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>SequenceNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSignal(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSignal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitSignal</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Signal</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSignalEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSignalEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitSignalEvent</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>SignalEvent</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSlot(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSlot</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitSlot</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Slot</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStartClassifierBehaviorAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStartClassifierBehaviorAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitStartClassifierBehaviorAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>StartClassifierBehaviorAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStartObjectBehaviorAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStartObjectBehaviorAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitStartObjectBehaviorAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>StartObjectBehaviorAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitState(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitState</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>State</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateInvariant(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStateInvariant</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitStateInvariant</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>StateInvariant</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateMachine(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStateMachine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitStateMachine</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>StateMachine</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStereotype(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitStereotype</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Stereotype</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStringExpression(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStringExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitStringExpression</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>StringExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStructuralFeature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStructuralFeature</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitStructuralFeature</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>StructuralFeature</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStructuralFeatureAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStructuralFeatureAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitStructuralFeatureAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>StructuralFeatureAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStructuredActivityNode(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStructuredActivityNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitStructuredActivityNode</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>StructuredActivityNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStructuredClassifier(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStructuredClassifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitStructuredClassifier</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>StructuredClassifier</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSubstitution(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSubstitution</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitSubstitution</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Substitution</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTemplateBinding(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTemplateBinding</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTemplateBinding</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateBinding</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTemplateParameter(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTemplateParameter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTemplateParameter</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameter</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTemplateParameterSubstitution(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTemplateParameterSubstitution</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTemplateParameterSubstitution</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameterSubstitution</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTemplateSignature(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTemplateSignature</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTemplateSignature</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateSignature</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTemplateableElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTemplateableElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTemplateableElement</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateableElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTestIdentityAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTestIdentityAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTestIdentityAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>TestIdentityAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTimeConstraint(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTimeConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTimeConstraint</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeConstraint</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTimeEvent(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTimeEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTimeEvent</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>TimeEvent</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTimeExpression(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTimeExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTimeExpression</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTimeInterval(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTimeInterval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTimeInterval</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeInterval</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTimeObservation(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTimeObservation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTimeObservation</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeObservation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTransition(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTransition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTransition</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Transition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTrigger(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTrigger</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTrigger</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Trigger</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitType(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitType</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Type</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTypedElement(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTypedElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTypedElement</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>TypedElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUnmarshallAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitUnmarshallAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitUnmarshallAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>UnmarshallAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUsage(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitUsage</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Usage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUseCase(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitUseCase</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitUseCase</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>UseCase</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitValuePin(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitValuePin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitValuePin</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>ValuePin</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitValueSpecification(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitValueSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitValueSpecification</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ValueSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitValueSpecificationAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitValueSpecificationAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitValueSpecificationAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ValueSpecificationAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitVariable(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitVariable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitVariable</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Variable</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitVariableAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitVariableAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitVariableAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>VariableAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitVertex(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitVertex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitVertex</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Vertex</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitWriteLinkAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitWriteLinkAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitWriteLinkAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>WriteLinkAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitWriteStructuralFeatureAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitWriteStructuralFeatureAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitWriteStructuralFeatureAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>WriteStructuralFeatureAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitWriteVariableAction(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitWriteVariableAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitWriteVariableAction</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../../magicdraw/actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>WriteVariableAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTaggedValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitTaggedValue</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
</section>
</li>
<li>
<section class="detail" id="visitStringTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStringTaggedValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitStringTaggedValue</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
</section>
</li>
<li>
<section class="detail" id="visitBooleanTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitBooleanTaggedValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitBooleanTaggedValue</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
</section>
</li>
<li>
<section class="detail" id="visitElementTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitElementTaggedValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitElementTaggedValue</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
</section>
</li>
<li>
<section class="detail" id="visitRealTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRealTaggedValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitRealTaggedValue</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
</section>
</li>
<li>
<section class="detail" id="visitIntegerTaggedValue(com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitIntegerTaggedValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visitIntegerTaggedValue</span><wbr/><span class="parameters">(<a href="VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
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
